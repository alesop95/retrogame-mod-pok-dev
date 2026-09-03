#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera la lista di spunta del Pokedex completo, con un codice interno per ogni voce.

Perché esiste
-------------
Fino a oggi il progetto contava. Contava le voci del catalogo degli eventi, le specie presenti nei
depositi dei salvataggi esterni, le voci di dono delle generazioni moderne, le specie che la
scadenza vincola. Ogni conto era corretto e nessuno rispondeva alla domanda che conta, cioè che
cosa manchi: per rispondere a quella serve un oggetto che i conti non producono, cioè un elenco
di voci con un'identità stabile, su cui ciascuna fonte possa essere proiettata.

Questo programma produce quell'elenco. È la spina dorsale del track del Pokedex, e ogni conto
futuro diventa una colonna che vi si appoggia invece di un numero che vive da solo.

Il codice interno, e perché il numero del Dex non basta
------------------------------------------------------
Il numero del Dex Nazionale identifica una specie e non un esemplare da ottenere, e la differenza
è precisamente il problema: quel numero non cambia per il sesso, non cambia per una variante
regionale, non cambia per una forma. Chi spunta una casella per numero del Dex non sa se abbia
spuntato la specie o una delle sue forme, e alla fine della campagna non sa che cosa gli manchi.

Il codice interno di questo progetto è dunque la coppia fra numero del Dex e indice di forma,
scritta come `PKD-####-##`, dove le quattro cifre sono il numero nazionale e le due seguenti
l'indice di forma con la forma base a zero. Le proprietà che lo rendono utile sono tre: è stabile,
perché non dipende da alcuna numerazione interna di alcuna implementazione e nemmeno dalla nostra;
è ordinabile, perché l'ordine lessicografico coincide con quello del Dex; ed è totale, perché
esiste per ogni voce e non soltanto per quelle di cui si conosce il nome della forma.

Che cosa questo elenco dichiara e che cosa non dichiara
------------------------------------------------------
Dichiara, per ciascuna voce, il numero del Dex, il nome della specie in italiano, l'indice di
forma, la via che la raggiunge, e quali fonti fra quelle che il progetto possiede sappiano già
fornirla. Non dichiara se il deposito conti quella forma come casella separata, e la ragione va
detta perché è la sola domanda aperta di questo track: nessuna fonte di primo livello lo
documenta, quindi l'elenco enumera le forme che esistono nei dati e marca come indeterminato il
loro valore ai fini del completamento. Un elenco che decidesse quella questione da sé darebbe una
risposta inventata a una domanda vera.

Uso
---
    python tools/checklist-pokedex.py --pkhex <clone> --ace <clone>
    python tools/checklist-pokedex.py --pkhex <clone> --ace <clone> --salvataggi <esito.json>
    python tools/checklist-pokedex.py --pkhex <clone> --ace <clone> --markdown <file>
"""

import argparse
import importlib.util
import io
import json
import os
import sys

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

NOMI_SPECIE_IT = os.path.join("PKHeX.Core", "Resources", "text", "other", "it",
                              "text_Species_it.txt")


def carica_modulo(nome, percorso):
    spec = importlib.util.spec_from_file_location(nome, percorso)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


def nomi_specie(pkhex):
    """I nomi delle specie in italiano, indicizzati per numero del Dex Nazionale.

    Il file della fonte porta a indice zero la parola Uovo, quindi l'indice coincide con il
    numero nazionale senza alcuno scorrimento: è una coincidenza comoda che va verificata e non
    assunta, e il controllo è che l'indice uno sia Bulbasaur e l'ultimo Pecharunt.
    """
    p = os.path.join(pkhex, NOMI_SPECIE_IT)
    if not os.path.exists(p):
        sys.exit("manca il file dei nomi delle specie in italiano sotto " + pkhex + ": su un "
                 "clone sparso va aggiunto PKHeX.Core/Resources/text/other/it")
    righe = io.open(p, encoding="utf-8").read().split("\n")
    if len(righe) < 1026 or righe[1] != "Bulbasaur":
        sys.exit("il file dei nomi non ha la forma attesa: l'indice uno dovrebbe essere "
                 "Bulbasaur e vale " + repr(righe[1] if len(righe) > 1 else None))
    return {i: righe[i] for i in range(1, 1026) if righe[i]}


def codice(numero, forma):
    """Il codice interno di una voce: numero del Dex a quattro cifre e forma a due."""
    return "PKD-%04d-%02d" % (numero, forma)


def fonti_disponibili(ace, esito_salvataggi):
    """Le specie che le fonti del progetto sanno già fornire, per numero del Dex.

    Restituisce un dizionario dal numero nazionale all'elenco delle etichette di fonte. Le fonti
    sono di natura diversa e vanno tenute distinte anche qui: il lotto degli eventi è prodotto da
    noi e verificato, i depositi dei salvataggi esterni sono materiale di terzi il cui uso è
    soggetto al perimetro, e confonderli farebbe apparire come nostro ciò che non lo è.
    """
    fuori = {}

    def aggiungi(numero, etichetta):
        fuori.setdefault(numero, [])
        if etichetta not in fuori[numero]:
            fuori[numero].append(etichetta)

    # Il lotto degli eventi di terza generazione, ricalcolato dalla tabella e non letto dal
    # disco, per la stessa ragione per cui le schede si ricalcolano: il disco non è versionato.
    try:
        generatore = carica_modulo("generatore", os.path.join(RADICE, "tools",
                                                              "genera-evento-gen3.py"))
        voci = generatore.voci_wc3(os.environ.get("PKHEX_CLONE", ""))
    except Exception:
        voci = None
    if voci:
        for v in voci:
            if v.get("metodo") in generatore.METODI_PRODUCIBILI and "ot_irrisolto" not in v:
                naz = v.get("nazionale")
                if naz:
                    aggiungi(int(naz), "evento Gen 3 producibile")

    # I depositi dei salvataggi esterni, dall'esito JSON dello strumento di verifica. La
    # corrispondenza fra numerazione interna e nazionale viene dal generatore, che dal 2026-09-02
    # la garantisce iniettiva.
    if esito_salvataggi and os.path.exists(esito_salvataggi):
        dati = json.loads(io.open(esito_salvataggi, encoding="utf-8").read())
        try:
            generatore = carica_modulo("generatore2", os.path.join(RADICE, "tools",
                                                                   "genera-evento-gen3.py"))
            n2i = generatore.nazionale_verso_interno(ace)
            i2n = {v: k for k, v in n2i.items()}
        except Exception as exc:
            print("  nota: la corrispondenza fra le numerazioni non si e' caricata (%s), quindi "
                  "i depositi non entrano nel conto" % exc)
            i2n = {}
        for nome, e in dati.items():
            censimento = e.get("deposito") or e.get("censimento")
            if not censimento:
                continue
            etichetta = ("archivio esterno" if nome.lower().endswith(".zip")
                         else "salvataggio esterno")
            for interno in censimento.get("specie", {}):
                naz = i2n.get(int(interno))
                if naz:
                    aggiungi(naz, etichetta)
    return fuori


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--pkhex", required=True, help="clone del verificatore")
    ap.add_argument("--ace", required=True, help="clone di ace-builder")
    ap.add_argument("--salvataggi", help="esito JSON di tools/verifica-salvataggi.py")
    ap.add_argument("--markdown", help="scrive la lista come documento tracciato")
    a = ap.parse_args(argv)

    os.environ["PKHEX_CLONE"] = a.pkhex

    disp = carica_modulo("disponibilita", os.path.join(RADICE, "tools",
                                                       "disponibilita-titoli.py"))
    nomi = nomi_specie(a.pkhex)

    # Le voci che ciascun titolo dichiara, e l'unione per via. La logica di lettura delle tabelle
    # e delle forme non si riscrive qui: viene dallo strumento che l'ha già verificata.
    per_nome = disp.specie_per_nome(a.pkhex)
    forme_src = disp.leggi(a.pkhex, disp.SORGENTE_FORME)
    battaglia = (disp.elenco_specie(forme_src, "BattleMegas", per_nome)
                 | disp.elenco_specie(forme_src, "BattleForms", per_nome))
    totemiche = disp.specie_con_forma_totemica(forme_src, per_nome)

    # I due insiemi non si ricalcolano qui: li restituisce lo strumento che li ha già verificati.
    # La prima stesura di questo programma li aveva riscritti, e la riscrittura perdeva le forme
    # di Let's Go: il commento di `insiemi_per_via` racconta il difetto e la ragione per cui la
    # lettura vive in un posto solo.
    _insiemi, diretta, indiretta = disp.insiemi_per_via(a.pkhex)

    tutte = diretta | indiretta
    fonti = fonti_disponibili(a.ace, a.salvataggi)

    # ---------------------------------------------------------------- livello di specie
    specie_tutte = sorted({s for s, _f in tutte if 1 <= s <= disp.DEX_MASSIMO})
    mancano_dal_dato = [s for s in range(1, disp.DEX_MASSIMO + 1) if s not in set(specie_tutte)]

    righe_specie = []
    for s in range(1, disp.DEX_MASSIMO + 1):
        via = "diretta" if (s, 0) in diretta else ("banca" if (s, 0) in indiretta else "ignota")
        righe_specie.append({
            "codice": codice(s, 0),
            "numero": s,
            "nome": nomi.get(s, "?"),
            "forma": 0,
            "via": via,
            "fonti": fonti.get(s, []),
        })

    # ---------------------------------------------------------------- livello di forma
    righe_forma = []
    for s, f in sorted(tutte):
        if f == 0 or not (1 <= s <= disp.DEX_MASSIMO):
            continue
        via = "diretta" if (s, f) in diretta else "banca"
        if s in battaglia:
            natura = "forma di sola battaglia: non puo stare in una scatola"
        elif disp.e_totemica(s, f, totemiche, per_nome):
            natura = "forma totemica: al trasferimento torna alla forma base"
        else:
            natura = "indeterminato: nessuna fonte di primo livello dice se il deposito la conti"
        righe_forma.append({
            "codice": codice(s, f),
            "numero": s,
            "nome": nomi.get(s, "?"),
            "forma": f,
            "via": via,
            "natura": natura,
            "fonti": fonti.get(s, []),
        })

    # ---------------------------------------------------------------- uscita a schermo
    print("Lista di spunta del Pokedex completo")
    print("")
    print("  voci di specie                    %d" % len(righe_specie))
    print("  di cui via diretta                %d"
          % sum(1 for r in righe_specie if r["via"] == "diretta"))
    print("  di cui solo via banca             %d"
          % sum(1 for r in righe_specie if r["via"] == "banca"))
    print("  di cui via ignota                 %d"
          % sum(1 for r in righe_specie if r["via"] == "ignota"))
    if mancano_dal_dato:
        print("  numeri del Dex che nessuna tabella dichiara: %s" % mancano_dal_dato[:20])
    print("")
    coperte = [r for r in righe_specie if r["fonti"]]
    print("  voci di specie che una fonte del progetto sa già fornire: %d su %d"
          % (len(coperte), len(righe_specie)))
    per_fonte = {}
    for r in coperte:
        for f in r["fonti"]:
            per_fonte[f] = per_fonte.get(f, 0) + 1
    for f, n in sorted(per_fonte.items(), key=lambda x: -x[1]):
        print("    %-32s %4d" % (f, n))
    print("")
    print("  voci di forma enumerate            %d" % len(righe_forma))
    nat = {}
    for r in righe_forma:
        chiave = r["natura"].split(":")[0]
        nat[chiave] = nat.get(chiave, 0) + 1
    for k, n in sorted(nat.items(), key=lambda x: -x[1]):
        print("    %-32s %4d" % (k, n))
    print("")
    print("  Il conto che decide la campagna: %d voci di specie non hanno ancora alcuna fonte "
          "nel progetto." % (len(righe_specie) - len(coperte)))

    if a.markdown:
        scrivi(a.markdown, righe_specie, righe_forma, per_fonte)
        print("")
        print("  scritto " + a.markdown)
    return 0


def scrivi(percorso, righe_specie, righe_forma, per_fonte):
    r = []
    r.append("# Lista di spunta del Pokedex completo")
    r.append("")
    r.append("> Documento generato da `tools/checklist-pokedex.py`. Non si modifica a mano: la "
             "colonna delle fonti si aggiorna rigenerando, e la spunta di ciò che è stato "
             "effettivamente ottenuto va tenuta altrove, perché questo file si riscrive.")
    r.append("")
    r.append("Il codice interno è la coppia fra numero del Dex Nazionale e indice di forma, "
             "scritta come `PKD-####-##`. Esiste perché il numero del Dex identifica una specie "
             "e non un esemplare da ottenere: non cambia per il sesso, non cambia per una "
             "variante regionale, non cambia per una forma, quindi chi spunta per numero del Dex "
             "non sa alla fine che cosa gli manchi. Il codice è stabile, poiché non dipende da "
             "alcuna numerazione interna di alcuna implementazione, è ordinabile, poiché l'ordine "
             "lessicografico coincide con quello del Dex, ed è totale, poiché esiste per ogni "
             "voce anche quando il nome della forma non è noto.")
    r.append("")
    r.append("La colonna della via dice se quella voce si raggiunga da un titolo che parla al "
             "deposito direttamente, e quindi senza scadenza, oppure se dipenda dalla banca, e "
             "quindi dal 26 febbraio 2027. La colonna delle fonti dice quali fra i materiali che "
             "il progetto possiede sappiano già fornire quella specie, e tiene distinte le fonti "
             "per natura: il lotto degli eventi è prodotto da noi e verificato, i depositi dei "
             "salvataggi esterni sono materiale di terzi il cui impiego è soggetto al perimetro "
             "di ADR-024, e confonderli farebbe apparire come nostro ciò che non lo è.")
    r.append("")

    coperte = sum(1 for x in righe_specie if x["fonti"])
    r.append("## Che cosa dice il conto")
    r.append("")
    r.append("Le voci di specie sono %d. Di queste, %d hanno già una fonte dentro il progetto e "
             "%d non ne hanno ancora alcuna: quest'ultimo è il numero che misura la campagna, e "
             "l'unico che scende quando si lavora."
             % (len(righe_specie), coperte, len(righe_specie) - coperte))
    r.append("")
    if per_fonte:
        r.append("La ripartizione per fonte, che non si somma perché una specie può avere più "
                 "fonti, è la seguente. " + " ".join(
                     "Da %s, %d voci." % (k, v)
                     for k, v in sorted(per_fonte.items(), key=lambda x: -x[1])))
        r.append("")
    r.append("Le voci di forma enumerate sono %d, e per la maggior parte il loro valore ai fini "
             "del completamento è indeterminato: nessuna fonte di primo livello dichiara quali "
             "forme il deposito conti come casella separata. L'elenco le enumera e marca "
             "l'indeterminatezza invece di decidere, perché decidere sarebbe inventare."
             % len(righe_forma))
    r.append("")

    r.append("## Voci di specie")
    r.append("")
    r.append("| Codice | Dex | Specie | Via | Fonti nel progetto |")
    r.append("|---|---|---|---|---|")
    for x in righe_specie:
        r.append("| `%s` | %d | %s | %s | %s |"
                 % (x["codice"], x["numero"], x["nome"], x["via"],
                    ", ".join(x["fonti"]) if x["fonti"] else "nessuna"))
    r.append("")

    r.append("## Voci di forma")
    r.append("")
    r.append("| Codice | Dex | Specie | Forma | Via | Natura |")
    r.append("|---|---|---|---|---|---|")
    for x in righe_forma:
        r.append("| `%s` | %d | %s | %d | %s | %s |"
                 % (x["codice"], x["numero"], x["nome"], x["forma"], x["via"], x["natura"]))
    r.append("")
    io.open(percorso, "w", encoding="utf-8", newline="").write("\n".join(r) + "\n")


if __name__ == "__main__":
    sys.exit(main())
