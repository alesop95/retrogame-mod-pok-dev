#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Carica un lotto di esemplari di terza generazione nelle scatole di un salvataggio da 128 KiB.

Perche' questo strumento, e perche' ora
---------------------------------------
Il progetto sa comporre un esemplare e, dal 2026-09-09, sa aprire il contenitore che lo ospita. Il
pezzo che mancava fra i due e' il caricamento: prendere i file di un lotto, sceglierne le
posizioni, scriverli e restituire un salvataggio ancora valido. Finora quell'operazione era fatta
a mano con l'editor esterno, che va bene per centosettantadue voci e non per le migliaia che
ADR-051 apre.

I quattro presidi, e perche' ciascuno esiste
--------------------------------------------
Il primo e' che il file di ingresso non si sovrascrive mai: il percorso di uscita e' obbligatorio
e deve essere diverso da quello di ingresso. Un salvataggio e' un originale, e uno strumento che
scriva sul proprio ingresso trasforma un errore di comando in una perdita.

Il secondo e' che si rifiuta di scrivere su uno slot non integro. Se le quattordici sezioni non
sono tutte valide, il salvataggio e' o corrotto o parziale, e scriverci dentro produrrebbe un file
che sembra riparato e non lo e'.

Il terzo e' che una posizione occupata non si sovrascrive senza che lo si chieda. La posizione
occupata si riconosce dal valore di personalita' diverso da zero, che e' il criterio che il gioco
stesso usa per dire se una casella e' vuota.

Il quarto e' che ogni file del lotto viene aperto e verificato prima di essere scritto, e un file
il cui checksum interno non torni viene rifiutato invece di essere caricato: un esemplare con il
checksum sbagliato e' precisamente cio' che il gioco distrugge marcandolo come Uovo Peste, quindi
caricarlo significherebbe perdere la posizione e il file.

Uso
---
    python tools/carica-lotto-gen3.py --lotto _notes/lotto-eventi --uscita /tmp/prova.sav
    python tools/carica-lotto-gen3.py --lotto _notes/lotto-eventi --salvataggio dump.sav --uscita nuovo.sav
    python tools/carica-lotto-gen3.py --self-test
"""

import argparse
import glob
import io
import os
import sys

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PONTE = os.path.join(RADICE, "pokemon-gen12-gen3-bridge-original-hardware")
sys.path.insert(0, PONTE)

from pokebridge import gb                                    # noqa: E402
from pokebridge.gen3 import (BOX_STRUCT_LENGTH, OFF_CHECKSUM as OFF_CHECKSUM_MON, OFF_SECURE,
                             PARTY_STRUCT_LENGTH, SECURE_LENGTH, Gen3Mon, compute_checksum,
                             u16, u32)  # noqa: E402
from pokebridge.save3 import (POSIZIONI, RECORD, Save3, crea_vuoto, file_da_record,
                              record_da_file)  # noqa: E402

ESTENSIONI = (".pk3", ".ek3", ".pkm")
POSIZIONI_PER_BOX = 30


def file_del_lotto(cartella):
    """I file del lotto in ordine di nome, che e' l'ordine in cui vanno nelle posizioni."""
    fuori = []
    for nome in sorted(os.listdir(cartella)):
        if os.path.splitext(nome)[1].lower() in ESTENSIONI:
            fuori.append(os.path.join(cartella, nome))
    return fuori


def leggi_esemplare(percorso):
    """Gli ottanta byte da scrivere nel deposito, oppure il motivo per cui il file non serve.

    Un file di squadra da cento byte e' accettato e troncato ai primi ottanta, perche' i venti in
    coda sono statistiche derivate che la scatola non conserva e che il gioco ricalcola.

    Il punto delicato e' la forma. Un file dell'editor e' in chiaro e con le quattro sottostrutture
    nell'ordine logico, mentre una posizione del deposito le vuole permutate secondo il valore di
    personalita' e mascherate in XOR: la conversione la fa `record_da_file`, e senza di essa il
    caricamento produce esemplari che il gioco marca come Uovo Peste. Il checksum va quindi
    verificato sulla forma del file, cioe' sui suoi quarantotto byte in chiaro, e non facendo
    decifrare al lettore del salvataggio dei byte che non sono cifrati.
    """
    dati = io.open(percorso, "rb").read()
    if len(dati) not in (BOX_STRUCT_LENGTH, PARTY_STRUCT_LENGTH):
        return None, "lunghezza %d: attesi %d o %d" % (len(dati), BOX_STRUCT_LENGTH,
                                                       PARTY_STRUCT_LENGTH)
    dati = dati[:BOX_STRUCT_LENGTH]
    if u32(dati, 0x00) == 0:
        return None, "valore di personalita' nullo: la casella risulterebbe vuota"
    memorizzato = u16(dati, OFF_CHECKSUM_MON)
    calcolato = compute_checksum(dati[OFF_SECURE:OFF_SECURE + SECURE_LENGTH])
    if memorizzato != calcolato:
        return None, ("checksum del file sbagliato: memorizzato %04X, calcolato %04X"
                      % (memorizzato, calcolato))
    try:
        record = record_da_file(dati)
    except ValueError as errore:
        return None, "non si converte: %s" % errore
    # Controprova sulla conversione: il lettore del salvataggio deve ritrovare il medesimo
    # checksum sul record permutato e cifrato. Se non lo ritrova, la conversione ha sbagliato e
    # non il file, ed e' meglio saperlo qui che dopo aver scritto quattrocento posizioni.
    try:
        mon = Gen3Mon.from_bytes(record)
    except gb.FormatError as errore:
        return None, "il record convertito non si rilegge: %s" % errore
    if mon.checksum_ok is False:
        return None, "la conversione ha prodotto un record con checksum incoerente"
    return record, None


def occupata(save, indice):
    """Vero se la posizione porta un esemplare, secondo il criterio del gioco."""
    record = save.leggi_posizione(indice)
    return any(record[:4])


def carica(save, esemplari, prima=0, sovrascrivi=False):
    """Scrive gli esemplari nelle posizioni libere a partire da una, e riferisce che cosa ha fatto."""
    scritti, saltate = [], []
    indice = prima
    for percorso, record in esemplari:
        while indice < POSIZIONI and not sovrascrivi and occupata(save, indice):
            saltate.append(indice)
            indice += 1
        if indice >= POSIZIONI:
            return scritti, saltate, "posizioni esaurite: il deposito ne ha %d" % POSIZIONI
        save.scrivi_posizione(indice, record)
        scritti.append((indice, percorso))
        indice += 1
    return scritti, saltate, None


def self_test():
    falliti = 0

    def prova(nome, atteso, ottenuto):
        nonlocal falliti
        if atteso != ottenuto:
            falliti += 1
            print("  FALLITO %s: atteso %r, ottenuto %r" % (nome, atteso, ottenuto))

    # Un esemplare sintetico valido: si compone con il modulo del ponte, cosi' il checksum e' suo
    # e non inventato qui.
    mon = Gen3Mon(personality=0x12345678, ot_id=0x0000A5A5)
    record = mon.to_bytes(party=False)
    prova("il record composto misura ottanta byte", BOX_STRUCT_LENGTH, len(record))

    # Le due forme non coincidono, ed e' la ragione per cui esiste la conversione: se coincidessero
    # questa prova fallirebbe e il presidio sarebbe inutile.
    forma_file = file_da_record(record)
    prova("le due forme differiscono", True, forma_file != record)
    prova("e la conversione e' invertibile", record, record_da_file(forma_file))

    save = crea_vuoto("RSE")
    prova("il sintetico e' integro", True, save.integro())
    prova("la prima posizione e' libera", False, occupata(save, 0))

    scritti, saltate, errore = carica(save, [("finto.pk3", record)])
    prova("nessun errore", None, errore)
    prova("una voce scritta", 1, len(scritti))
    prova("nella prima posizione", 0, scritti[0][0])
    prova("ora e' occupata", True, occupata(save, 0))

    # Il presidio sulla posizione occupata: senza sovrascrittura la seconda voce va nella
    # posizione successiva e la prima resta com'era.
    altro = Gen3Mon(personality=0x87654321, ot_id=0x00005A5A).to_bytes(party=False)
    scritti, saltate, errore = carica(save, [("altro.pk3", altro)])
    prova("la seconda voce scende di una posizione", 1, scritti[0][0])
    prova("e la prima e' stata saltata", [0], saltate)
    prova("il primo record e' intatto", record, save.leggi_posizione(0))

    # Con la sovrascrittura esplicita, invece, la prima posizione viene riscritta.
    scritti, saltate, errore = carica(save, [("terzo.pk3", altro)], sovrascrivi=True)
    prova("la sovrascrittura scrive dove chiesto", 0, scritti[0][0])
    prova("e il record e' quello nuovo", altro, save.leggi_posizione(0))

    # Dopo la serializzazione il salvataggio resta valido: e' la prova che i checksum di sezione
    # sono stati rifatti da chi scrive e non dimenticati.
    riletto = Save3(save.to_bytes(), "RSE")
    prova("il salvataggio riletto e' integro", True, riletto.integro())
    prova("e conserva il record", altro, riletto.leggi_posizione(0))

    # Controllo negativo sul quarto presidio: un record con il checksum guastato va rifiutato.
    guasto = bytearray(record)
    guasto[0x1C] ^= 0xFF
    percorso = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_prova_guasta.tmp")
    io.open(percorso, "wb").write(bytes(guasto))
    try:
        letto, motivo = leggi_esemplare(percorso)
        prova("il record guasto viene rifiutato", None, letto)
        prova("con il motivo giusto", True, motivo is not None and "checksum" in motivo)
    finally:
        os.remove(percorso)

    # E un file di lunghezza sbagliata non entra nemmeno in lettura.
    percorso = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_prova_corta.tmp")
    io.open(percorso, "wb").write(b"\x00" * 17)
    try:
        letto, motivo = leggi_esemplare(percorso)
        prova("il file corto viene rifiutato", None, letto)
        prova("con il motivo sulla lunghezza", True, motivo is not None and "lunghezza" in motivo)
    finally:
        os.remove(percorso)

    print("self-test: %d controlli falliti" % falliti)
    return 1 if falliti else 0


def main(argv=None):
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--lotto", help="la cartella con i file del lotto")
    ap.add_argument("--salvataggio", help="il salvataggio di partenza; se manca si crea sintetico")
    ap.add_argument("--gioco", default="RSE", choices=("RSE", "FRLG"))
    ap.add_argument("--uscita", help="dove scrivere il salvataggio nuovo, obbligatorio")
    ap.add_argument("--prima", type=int, default=0, help="la prima posizione del deposito da usare")
    ap.add_argument("--sovrascrivi", action="store_true",
                    help="scrive anche sulle posizioni occupate")
    ap.add_argument("--self-test", action="store_true", dest="self_test")
    a = ap.parse_args(argv)
    if a.self_test:
        return self_test()

    if not a.lotto or not a.uscita:
        print("rifiutato: servono --lotto e --uscita")
        return 1
    if not os.path.isdir(a.lotto):
        print("rifiutato: la cartella del lotto non esiste: " + a.lotto)
        return 1
    if a.salvataggio and os.path.abspath(a.salvataggio) == os.path.abspath(a.uscita):
        print("rifiutato: l'uscita non puo' essere il salvataggio di ingresso")
        return 1

    if a.salvataggio:
        if not os.path.exists(a.salvataggio):
            print("rifiutato: il salvataggio non esiste: " + a.salvataggio)
            return 1
        save = Save3(io.open(a.salvataggio, "rb").read(), a.gioco)
        provenienza = a.salvataggio
    else:
        save = crea_vuoto(a.gioco)
        provenienza = "sintetico"
    if not save.integro():
        print("rifiutato: lo slot attivo non e' integro, quindi non ci si scrive dentro")
        return 1

    esemplari, rifiutati = [], []
    for percorso in file_del_lotto(a.lotto):
        record, motivo = leggi_esemplare(percorso)
        if record is None:
            rifiutati.append((percorso, motivo))
        else:
            esemplari.append((percorso, record))

    scritti, saltate, errore = carica(save, esemplari, a.prima, a.sovrascrivi)
    if errore:
        print("rifiutato: " + errore)
        return 1

    io.open(a.uscita, "wb").write(save.to_bytes())
    print("scritto %s da %s" % (a.uscita, provenienza))
    print("  caricati %d esemplari, posizioni saltate perche' occupate %d, rifiutati %d"
          % (len(scritti), len(saltate), len(rifiutati)))
    if scritti:
        primo, ultimo = scritti[0][0], scritti[-1][0]
        print("  posizioni da %d a %d, cioe' dalla scatola %d alla %d"
              % (primo, ultimo, primo // POSIZIONI_PER_BOX + 1, ultimo // POSIZIONI_PER_BOX + 1))
    for percorso, motivo in rifiutati:
        print("  RIFIUTATO %s: %s" % (os.path.basename(percorso), motivo))
    return 0


if __name__ == "__main__":
    sys.exit(main())
