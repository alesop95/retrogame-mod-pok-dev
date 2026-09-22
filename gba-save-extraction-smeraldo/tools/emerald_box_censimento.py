#!/usr/bin/env python3
"""Censisce in sola lettura l'occupazione dei quattordici box del deposito di un salvataggio di terza generazione.

Perche' esiste
--------------

La produzione degli esemplari per il Parco Lotta scrivera' trenta posizioni nel deposito della cartuccia vera, ed e' la prima scrittura di questo progetto che tocca la struttura di un Pokemon invece di flag, voci di inventario o riordini. Prima di decidere dove scriverli serve sapere dove c'e' posto, e la domanda non e' quante posizioni siano libere in totale, che sono certamente molte, ma se esista un box gia' vuoto: una scrittura che atterra in un box vuoto non sposta nulla, mentre una che debba farsi spazio richiede prima uno spostamento, cioe' una seconda scrittura e una seconda occasione di sbagliare.

Lo strumento non scrive nulla e non apre alcun file in scrittura. E' una misura, e la sua uscita e' pensata per essere letta accanto a `PIANO-BOX.md`, che dice quante posizioni servono.

Che cosa legge, e con quale cautela
------------------------------------

Un record di deposito misura ottanta byte ed e' cifrato: la specie non si legge direttamente ma sta nella sottostruttura di crescita, e per arrivarci occorrono la chiave, che e' l'identificativo dell'allenatore in XOR con il valore di personalita', e la permutazione, che dipende dal valore di personalita' modulo ventiquattro. Tutto questo lo fa gia' `pokebridge.gen3`, verificato da una suite di prove, e qui si riusa invece di riscriverlo: un secondo decifratore scritto per l'occasione sarebbe un secondo posto dove sbagliare.

Una posizione vuota si riconosce da una specie pari a zero dopo la decifratura, e non dal record tutto a zero, perche' un record puo' portare byte residui di un esemplare rimosso. Dove la decifratura fallisce o il checksum non torna, la posizione si conta come occupata e si segnala: e' la scelta prudente, perche' contare come libera una posizione che il gioco considera piena significherebbe proporre di scrivervi sopra.

Uso
---

    python gba-save-extraction-smeraldo/tools/emerald_box_censimento.py SALVATAGGIO.sav
    python gba-save-extraction-smeraldo/tools/emerald_box_censimento.py SALVATAGGIO.sav --out gba-save-extraction-smeraldo/CENSIMENTO-BOX.md
"""

import argparse
import sys
from pathlib import Path

RADICE_PONTE = Path(__file__).resolve().parents[2].joinpath("pokemon-gen12-gen3-bridge-original-hardware")
sys.path.insert(0, str(RADICE_PONTE))

try:
    from pokebridge import save3, gen3, charmap
except ImportError as errore:  # pragma: no cover
    sys.exit("non trovo il pacchetto pokebridge in %s: %s" % (RADICE_PONTE, errore))

BOX = 14
POSIZIONI_PER_BOX = 30


_TABELLA = charmap.Charmap.gen3()


def nome_leggibile(grezzo):
    """Decodifica un nome dalla tabella di caratteri del gioco, tollerando i byte di riempimento."""
    try:
        return _TABELLA.decode(grezzo).strip()
    except Exception:
        return grezzo.hex()


def carica_specie(percorso):
    """La mappa fra indice interno di specie e nome, estratta dal sorgente.

    Senza di essa il censimento resta corretto nei conteggi e muto sui nomi, che e' meglio del rischio opposto: l'indice interno non e' il numero del Pokedex nazionale, e tradurlo con quella numerazione darebbe a ogni specie di Hoenn il nome di un'altra senza produrre alcun errore.
    """
    if not percorso:
        return {}
    import json
    return json.loads(Path(percorso).read_text(encoding="utf-8"))


def censisci(percorso, specie_per_indice=None):
    salvataggio = save3.Save3(Path(percorso).read_bytes(), gioco="RSE")
    box = []
    for indice in range(BOX):
        voci = []
        for posizione in range(POSIZIONI_PER_BOX):
            assoluta = indice * POSIZIONI_PER_BOX + posizione
            grezzo = salvataggio.leggi_posizione(assoluta)
            if not any(grezzo):
                continue
            try:
                mostro = gen3.Gen3Mon.from_bytes(grezzo)
                specie = mostro.growth.species
            except Exception:
                voci.append({"posizione": posizione, "specie": None, "nota": "record non decifrabile, contato come occupato"})
                continue
            if specie == 0:
                continue
            voci.append({
                "posizione": posizione,
                "specie": specie,
                "nome_specie": (specie_per_indice or {}).get(str(specie), "indice %d" % specie),
                "soprannome": nome_leggibile(mostro.nickname),
                "allenatore": nome_leggibile(mostro.ot_name),
                "id_allenatore": mostro.ot_id & 0xFFFF,
            })
        box.append({
            "indice": indice,
            "nome": nome_leggibile(salvataggio.nome_box(indice)) if indice < BOX else "",
            "occupate": len(voci),
            "libere": POSIZIONI_PER_BOX - len(voci),
            "voci": voci,
        })
    return salvataggio, box


def scrivi(percorso, sorgente, box, servono):
    totale_occupate = sum(b["occupate"] for b in box)
    vuoti = [b for b in box if b["occupate"] == 0]
    capienti = [b for b in box if b["libere"] >= servono]

    r = ["# Censimento dell'occupazione dei box del deposito", "",
         "> Generato in sola lettura da `gba-save-extraction-smeraldo/tools/emerald_box_censimento.py` su `%s`. Nessun byte e' stato scritto. Si rigenera a ogni nuovo dump, e va letto accanto a `PIANO-BOX.md`, che dice quante posizioni servono." % Path(sorgente).name, "",
         "## La risposta in una riga", ""]
    if vuoti:
        r.append("Servono **%d** posizioni. Box completamente vuoti: **%d**, cioe' %s. Una scrittura che atterri in uno di questi non sposta nulla, ed e' la collocazione da preferire." % (
            servono, len(vuoti), ", ".join("il numero %d" % (b["indice"] + 1) for b in vuoti)))
    elif capienti:
        r.append("Servono **%d** posizioni. Nessun box e' del tutto vuoto, ma %d hanno abbastanza spazio libero, cioe' %s. La scrittura dovra' convivere con cio' che gia' c'e', quindi va scelta la posizione voce per voce invece che il box in blocco." % (
            servono, len(capienti), ", ".join("il numero %d con %d libere" % (b["indice"] + 1, b["libere"]) for b in capienti)))
    else:
        r.append("Servono **%d** posizioni e nessun box da solo le ospita: il piano va diviso su due box, oppure va liberato spazio prima di scrivere." % servono)
    r.append("")
    r.append("Posizioni occupate in tutto il deposito: %d su %d." % (totale_occupate, BOX * POSIZIONI_PER_BOX))
    r.append("")
    r.append("## Box per box")
    r.append("")
    r.append("| Box | Nome | Occupate | Libere |")
    r.append("|---|---|---|---|")
    for b in box:
        r.append("| %d | %s | %d | %d |" % (b["indice"] + 1, b["nome"] or "(senza nome)", b["occupate"], b["libere"]))
    r.append("")
    Path(percorso).write_text("\n".join(r) + "\n", encoding="utf-8")


def main():
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("salvataggio")
    p.add_argument("--servono", type=int, default=30, help="quante posizioni deve ospitare la scrittura prevista")
    p.add_argument("--specie", help="specie-gen3.json, la mappa fra indice interno e nome")
    p.add_argument("--dettaglio", action="store_true", help="elenca anche il contenuto di ogni box")
    p.add_argument("--out", help="documento Markdown da scrivere; senza, stampa soltanto")
    args = p.parse_args()

    salvataggio, box = censisci(args.salvataggio, carica_specie(args.specie))
    totale = sum(b["occupate"] for b in box)
    print("box corrente dichiarato dal salvataggio: %d" % (salvataggio.box_corrente() + 1))
    print("posizioni occupate: %d su %d" % (totale, BOX * POSIZIONI_PER_BOX))
    for b in box:
        segno = "  VUOTO" if b["occupate"] == 0 else ("  ospita le %d che servono" % args.servono if b["libere"] >= args.servono else "")
        print("  box %2d  %-10s occupate %2d, libere %2d%s" % (b["indice"] + 1, b["nome"] or "", b["occupate"], b["libere"], segno))
    if args.dettaglio:
        for b in box:
            if not b["voci"]:
                continue
            print("")
            print("  box %d, %s:" % (b["indice"] + 1, b["nome"] or "senza nome"))
            for v in b["voci"]:
                print("    %2d  %-12s %-11s allenatore %s (%d)" % (
                    v["posizione"] + 1, v.get("nome_specie", "?"), v.get("soprannome", ""),
                    v.get("allenatore", ""), v.get("id_allenatore", 0)))
    if args.out:
        scrivi(args.out, args.salvataggio, box, args.servono)
        print("uscita in %s" % args.out)


if __name__ == "__main__":
    main()
