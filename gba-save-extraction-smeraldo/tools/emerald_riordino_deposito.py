#!/usr/bin/env python3
"""Riordina il deposito di un salvataggio di Smeraldo secondo ADR-074 e vi inserisce il lotto del Parco Lotta, scrivendo un file NUOVO.

Perche' esiste
--------------

ADR-074 chiede tre cose in una sola scrittura: gli esemplari gia' presenti compattati nei primi box, i sessantaquattro del lotto nei box 12, 13 e 14, e i quattordici box rinominati da BOX 1 a BOX 14. Farle a mano in PKHeX sono trecentosedici trascinamenti, e un trascinamento sbagliato su un deposito di vent'anni e' esattamente il genere di errore che non si vede finche' non e' tardi. Qui le tre cose sono una trasformazione sola, deterministica e verificata.

Che cosa garantisce, e come lo dimostra
----------------------------------------

Un esemplare gia' presente non viene mai decifrato per essere riscritto: i suoi ottanta byte si copiano tali e quali in una posizione nuova, quindi nulla di cio' che portava puo' cambiare, nemmeno un difetto. Il risanamento degli irregolari e' un lavoro separato, e mescolarlo con uno spostamento renderebbe impossibile dire quale dei due abbia prodotto un eventuale errore.

La verifica non si fida della scrittura. Rilegge il file prodotto da capo e controlla cinque cose. Che lo slot attivo sia integro in tutte le quattordici sezioni. Che l'insieme dei record non vuoti del file nuovo sia esattamente l'insieme dei record del vecchio piu' i sessantaquattro del lotto, contato come multinsieme, cosi' che un esemplare perso o duplicato non possa passare. Che ogni posizione contenga precisamente il record previsto. Che fuori dal deposito nulla sia cambiato, cioe' squadra, zaino, giocatore e slot inattivo identici byte per byte. E che nessun esemplare del lotto condivida la personalita' con uno gia' presente, perche' due esemplari con la stessa personalita' sono cloni per qualunque verificatore.

Che cosa non fa
---------------

Non tocca la cartuccia e non sovrascrive l'ingresso: rifiuta di scrivere se l'uscita coincide con l'ingresso o esiste gia'. Non cambia gli sfondi, che restano associati al numero di box come sono, perche' la loro scelta e' ancora aperta. Non modifica la squadra.

Uso
---

    python gba-save-extraction-smeraldo/tools/emerald_riordino_deposito.py INGRESSO.sav USCITA.sav
    python gba-save-extraction-smeraldo/tools/emerald_riordino_deposito.py INGRESSO.sav USCITA.sav --sostituisci-lotto _notes/lotto-parco-lotta/esemplari-round6

La seconda forma serve quando il deposito e' gia' riordinato e cambia soltanto il lotto: rimpiazza le sessantaquattro posizioni dei box 12-14 dopo aver verificato che contengano esattamente i file del giro precedente.
"""

import argparse
import collections
import hashlib
import importlib.util
import json
import sys
from pathlib import Path

CARTELLA = Path(__file__).resolve().parents[1]
RADICE = CARTELLA.parent
sys.path.insert(0, str(RADICE.joinpath("pokemon-gen12-gen3-bridge-original-hardware")))

from pokebridge import charmap, gen3, save3  # noqa: E402

LOTTO = RADICE.joinpath("_notes", "lotto-parco-lotta", "esemplari")
CATALOGO = CARTELLA.joinpath("squadre-parco-lotta.json")
BOX = 14
PER_BOX = 30
BOX_ESISTENTI = 9
VUOTO = bytes(save3.RECORD)


def _percorso():
    percorso = Path(__file__).resolve().parent.joinpath("parco_lotta_percorso_oro.py")
    spec = importlib.util.spec_from_file_location("percorso_oro", percorso)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


def occupata(record):
    """Una posizione e' occupata se la specie decifrata non e' zero; se la decifratura fallisce si considera occupata, che e' la scelta prudente."""
    if record == VUOTO:
        return False
    try:
        return gen3.Gen3Mon.from_bytes(record).growth.species != 0
    except Exception:
        return True


def personalita(record):
    return int.from_bytes(record[0:4], "little")


def sostituisci_lotto(ingresso, uscita, precedente):
    """Rimpiazza nei box 12-14 il lotto gia' scritto con il lotto rigenerato, senza toccare nient'altro.

    Serve quando il deposito e' gia' stato riordinato e cambia soltanto il lotto, come il 2026-09-23 per le copie gemelle: rilanciare il riordino tratterebbe il lotto vecchio come deposito da compattare. Prima di scrivere si pretende che ogni posizione del lotto contenga esattamente il file del giro precedente previsto per quella posizione, byte per byte: se la partita nel frattempo ha spostato, liberato o sostituito anche un solo esemplare del lotto, lo strumento si ferma invece di sovrascrivere qualcosa che non conosce.
    """
    grezzo = ingresso.read_bytes()
    vecchio = save3.Save3(grezzo)
    if not vecchio.integro():
        sys.exit("lo slot attivo dell'ingresso non e' integro")
    percorso = _percorso()
    catalogo = json.loads(CATALOGO.read_text(encoding="utf-8"))
    thread = json.loads(percorso._mappa().THREAD.read_text(encoding="utf-8"))
    _, posizioni, _, _ = percorso.disposizione(catalogo, thread, storica=True)
    nuovo = save3.Save3(grezzo)
    fuori_lotto = set(range(save3.POSIZIONI))
    for (chiave, copia), (box, n) in posizioni.items():
        indice = (box - 1) * PER_BOX + (n - 1)
        fuori_lotto.discard(indice)
        atteso = precedente.joinpath("%s-copia%d.bin" % (chiave, copia)).read_bytes()
        if vecchio.leggi_posizione(indice) != atteso:
            sys.exit("la posizione del box %d, %d, non contiene il file del giro precedente %s-copia%d: "
                     "la partita l'ha cambiata, e non si sovrascrive cio' che non si conosce" % (box, n, chiave, copia))
        nuovo.scrivi_posizione(indice, LOTTO.joinpath("%s-copia%d.bin" % (chiave, copia)).read_bytes())
    prodotto = nuovo.to_bytes()
    riletto = save3.Save3(prodotto)
    errori = []
    if not riletto.integro():
        errori.append("lo slot attivo del file prodotto non e' integro")
    for i in fuori_lotto:
        if riletto.leggi_posizione(i) != vecchio.leggi_posizione(i):
            errori.append("la posizione %d, fuori dal lotto, e' cambiata" % i)
    for (chiave, copia), (box, n) in posizioni.items():
        indice = (box - 1) * PER_BOX + (n - 1)
        if riletto.leggi_posizione(indice) != LOTTO.joinpath("%s-copia%d.bin" % (chiave, copia)).read_bytes():
            errori.append("la posizione del box %d, %d, non contiene il file nuovo" % (box, n))
    if riletto.small() != vecchio.small() or riletto.large() != vecchio.large():
        errori.append("i dati fuori dal deposito sono cambiati")
    base = (1 - vecchio.attivo) * save3.SLOT
    if prodotto[base:base + save3.SLOT] != grezzo[base:base + save3.SLOT]:
        errori.append("lo slot inattivo e' cambiato")
    coda = save3.OFF_NOMI_BOX
    if riletto.storage()[coda:] != vecchio.storage()[coda:]:
        errori.append("nomi dei box, sfondi o coda del deposito cambiati")
    if errori:
        for e in errori:
            print("VERIFICA FALLITA: %s" % e)
        sys.exit("il file non e' stato scritto")
    uscita.write_bytes(prodotto)
    print("lotto sostituito: %d posizioni nei box 12-14, ciascuna verificata prima e dopo" % len(posizioni))
    print("verifica: slot integro, le altre %d posizioni identiche, nomi e sfondi identici, resto identico" % len(fuori_lotto))
    print("scritto %s" % uscita)
    print("SHA-256 %s" % hashlib.sha256(prodotto).hexdigest())


def main():
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("ingresso")
    p.add_argument("uscita")
    p.add_argument("--sostituisci-lotto", metavar="CARTELLA_PRECEDENTE",
                   help="sostituisce soltanto il lotto nei box 12-14, pretendendo che vi stiano i file di questa cartella")
    args = p.parse_args()
    if args.sostituisci_lotto:
        ingresso, uscita = Path(args.ingresso), Path(args.uscita)
        if uscita.resolve() == ingresso.resolve() or uscita.exists():
            sys.exit("l'uscita coincide con l'ingresso o esiste gia': questo strumento non sovrascrive")
        return sostituisci_lotto(ingresso, uscita, Path(args.sostituisci_lotto))
    ingresso, uscita = Path(args.ingresso), Path(args.uscita)
    if uscita.resolve() == ingresso.resolve():
        sys.exit("l'uscita coincide con l'ingresso: questo strumento non sovrascrive mai il salvataggio letto")
    if uscita.exists():
        sys.exit("%s esiste gia': scegli un nome nuovo, questo strumento non sovrascrive" % uscita)

    grezzo = ingresso.read_bytes()
    vecchio = save3.Save3(grezzo)
    if not vecchio.integro():
        sys.exit("lo slot attivo dell'ingresso non e' integro: non si riordina un salvataggio danneggiato")

    esistenti = [vecchio.leggi_posizione(i) for i in range(save3.POSIZIONI)]
    esistenti = [r for r in esistenti if occupata(r)]
    if len(esistenti) > BOX_ESISTENTI * PER_BOX:
        sys.exit("%d esemplari non entrano nei primi %d box" % (len(esistenti), BOX_ESISTENTI))

    percorso = _percorso()
    catalogo = json.loads(CATALOGO.read_text(encoding="utf-8"))
    thread = json.loads(percorso._mappa().THREAD.read_text(encoding="utf-8"))
    _, posizioni, _, _ = percorso.disposizione(catalogo, thread, storica=True)
    lotto = {}
    for (chiave, copia), (box, n) in posizioni.items():
        indice = (box - 1) * PER_BOX + (n - 1)
        lotto[indice] = LOTTO.joinpath("%s-copia%d.bin" % (chiave, copia)).read_bytes()
        if len(lotto[indice]) != save3.RECORD:
            sys.exit("%s-copia%d.bin non misura %d byte" % (chiave, copia, save3.RECORD))

    gia = {personalita(r) for r in esistenti}
    doppi = [i for i, r in lotto.items() if personalita(r) in gia]
    if doppi:
        sys.exit("%d esemplari del lotto hanno la personalita' di un esemplare gia' presente" % len(doppi))

    previsto = [VUOTO] * save3.POSIZIONI
    for i, r in enumerate(esistenti):
        previsto[i] = r
    for i, r in lotto.items():
        if previsto[i] != VUOTO:
            sys.exit("la posizione %d e' gia' occupata da un esemplare esistente" % i)
        previsto[i] = r

    nuovo = save3.Save3(grezzo)
    for i, r in enumerate(previsto):
        nuovo.scrivi_posizione(i, r)
    tabella = charmap.Charmap.gen3()
    for b in range(BOX):
        nome = tabella.encode("BOX %d" % (b + 1), length=save3.PASSO_NOME_BOX)
        nuovo._scrivi_in_buffer(save3.SEZIONI_STORAGE, save3.OFF_NOMI_BOX + b * save3.PASSO_NOME_BOX, nome)
    prodotto = nuovo.to_bytes()

    # La verifica rilegge il file dai byte prodotti, non dagli oggetti che li hanno prodotti.
    riletto = save3.Save3(prodotto)
    errori = []
    if not riletto.integro():
        errori.append("lo slot attivo del file prodotto non e' integro")
    if riletto.attivo != vecchio.attivo:
        errori.append("lo slot attivo e' cambiato")
    posti = [riletto.leggi_posizione(i) for i in range(save3.POSIZIONI)]
    for i, (atteso, letto) in enumerate(zip(previsto, posti)):
        if atteso != letto:
            errori.append("posizione %d diversa da quella prevista" % i)
    prima = collections.Counter(esistenti) + collections.Counter(lotto.values())
    dopo = collections.Counter(r for r in posti if occupata(r))
    if prima != dopo:
        errori.append("i record non vuoti non sono l'insieme atteso: %d attesi, %d letti" % (sum(prima.values()), sum(dopo.values())))
    if riletto.small() != vecchio.small() or riletto.large() != vecchio.large():
        errori.append("i dati fuori dal deposito sono cambiati")
    inattivo = 1 - vecchio.attivo
    base = inattivo * save3.SLOT
    if prodotto[base:base + save3.SLOT] != grezzo[base:base + save3.SLOT]:
        errori.append("lo slot inattivo e' cambiato")
    for b in range(BOX):
        if tabella.decode(riletto.nome_box(b)) != "BOX %d" % (b + 1):
            errori.append("il nome del box %d non e' BOX %d" % (b + 1, b + 1))
    fuori_deposito = riletto.storage()[save3.OFF_NOMI_BOX + BOX * save3.PASSO_NOME_BOX:]
    if fuori_deposito != vecchio.storage()[save3.OFF_NOMI_BOX + BOX * save3.PASSO_NOME_BOX:]:
        errori.append("sfondi o coda del deposito cambiati")
    if errori:
        for e in errori:
            print("VERIFICA FALLITA: %s" % e)
        sys.exit("il file non e' stato scritto")

    uscita.write_bytes(prodotto)
    print("esistenti compattati: %d, nei box 1-%d" % (len(esistenti), (len(esistenti) - 1) // PER_BOX + 1))
    print("lotto inserito: %d, nei box 12-14" % len(lotto))
    print("box rinominati: BOX 1 ... BOX %d; sfondi e squadra invariati" % BOX)
    print("verifica: slot integro, multinsieme dei record conservato, ogni posizione come prevista, resto identico")
    print("scritto %s" % uscita)
    print("SHA-256 %s" % hashlib.sha256(prodotto).hexdigest())


if __name__ == "__main__":
    main()
