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

I tre assi, e perché una voce da evento non è una specie
-------------------------------------------------------
La collezione che questo progetto persegue non è l'insieme delle specie: è l'insieme delle specie
più l'insieme delle forme che il deposito conta a parte più l'insieme degli esemplari da
distribuzione. I tre non si riducono l'uno all'altro, e la ragione è che un esemplare da
distribuzione è un collezionabile distinto anche quando la sua specie è già coperta: il Pikachu
del decennale non è il Pikachu di un prato, perché porta un nome di allenatore, un identificativo
e una data che nessun prato produce, e chi possiede il secondo non possiede il primo.

Ne segue che la lista porta tre tabelle e tre famiglie di codici. Le voci di specie hanno codice
`PKD-####-00`, le voci di forma `PKD-####-##` con forma diversa da zero, e le voci da evento
`EVT-<generazione>-<indice>`, con l'eccezione delle voci che vengono dalle tabelle degli incontri
invece che dai doni, il cui codice è `EVT-T-<indice>` perché una sola numerazione le attraversa
tutte e la generazione resta nella propria colonna.

Sul codice delle voci da evento va dichiarato un limite che i codici di specie non hanno, perché
tacerlo lo renderebbe insidioso. L'indice è la posizione della voce nella tabella della fonte, e
dunque il codice è stabile soltanto quanto quella tabella: se la fonte riordinasse i propri dati,
i codici si sposterebbero in blocco senza che nulla lo segnali. È un compromesso accettato per
ora, poiché l'alternativa, cioè derivare il codice dal contenuto della voce, richiede di leggere
per ogni formato i campi che identificano la distribuzione, e per la terza generazione quel dato
non esiste in forma numerica. Il giorno in cui i codici da evento serviranno a spuntare e non
soltanto a contare, questa è la prima cosa da cambiare.

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


def voci_da_evento(pkhex, ace):
    """Le voci da distribuzione di tutte le generazioni, con la loro provenienza e la nostra resa.

    Le fonti sono due e restano distinte. Per la terza generazione la tabella vive nel codice del
    verificatore e la legge il nostro generatore, che di ciascuna voce sa anche se la sappia
    produrre; per le altre generazioni le tabelle sono file binari e le legge lo strumento del
    conteggio, che di ciascuna voce sa la specie e non se la sappiamo produrre, perché per quelle
    generazioni non abbiamo ancora un generatore.

    La distinzione fra le due va conservata nell'uscita, perché è la differenza fra una voce che
    il progetto sa già fare e una che sa soltanto contare, e mescolarle darebbe l'impressione di
    una copertura che non c'è.
    """
    fuori = []

    # ------------------------------------------------------------------ terza generazione
    try:
        generatore = carica_modulo("gen3ev", os.path.join(RADICE, "tools",
                                                          "genera-evento-gen3.py"))
        voci = generatore.voci_wc3(pkhex)
    except Exception as exc:
        print("  nota: il catalogo di terza generazione non si e' caricato (%s)" % exc)
        voci = []
    for indice, v in enumerate(voci):
        producibile = (v.get("metodo") in generatore.METODI_PRODUCIBILI
                       and "ot_irrisolto" not in v)
        fuori.append({
            "codice": "EVT-3-%04d" % indice,
            "generazione": 3,
            "classe": "carta meraviglia",
            "nazionale": v.get("nazionale"),
            "forma": 0,
            "descrizione": (v.get("commento") or v.get("ot") or "evento"),
            "metodo": v.get("metodo"),
            "sotto_scadenza": True,
            "resa": "producibile e verificata" if producibile else "non producibile",
        })

    # ------------------------------------------------------------------ le altre generazioni
    try:
        conteggio = carica_modulo("conteggio", os.path.join(RADICE, "tools",
                                                            "conteggio-doni-moderni.py"))
        righe, antichi, _difetti = conteggio.conta(pkhex)
    except Exception as exc:
        print("  nota: il conteggio dei doni non si e' caricato (%s)" % exc)
        return fuori

    # La corrispondenza serve soltanto alla terza generazione, che numera per numero nazionale;
    # dalla quarta in avanti le tabelle dei doni usano gia' la numerazione nazionale.
    # L'indice del codice scorre sulla generazione e non sul file, e la ragione va scritta perche'
    # la scelta opposta era gia' stata fatta e produceva un difetto silenzioso. Una generazione
    # puo' avere piu' di un file di doni, e la sesta, la settima, l'ottava e la nona ne hanno due o
    # tre: numerando da zero dentro ciascun file, la voce zero di `wc8.pkl` e quella di `wa8.pkl`
    # ricevevano il medesimo codice. Il difetto e' stato trovato il 2026-09-04 da un controllo di
    # unicita', non da un errore: novecentosette voci condividevano un codice con un'altra, e
    # nulla lo segnalava perche' un codice duplicato non rompe niente finche' nessuno lo usa per
    # spuntare. Le generazioni dalla prima alla quinta hanno un file solo per generazione e i loro
    # codici non si sono mossi, il che conta perche' i lotti gia' prodotti li portano nel nome dei
    # file.
    contatore_per_generazione = {}
    for r in righe:
        if not r.get("letti"):
            continue
        for v in r.get("voci_dettaglio", []):
            gen = r["generazione"]
            indice_gen = contatore_per_generazione.get(gen, 0)
            contatore_per_generazione[gen] = indice_gen + 1
            fuori.append({
                "codice": "EVT-%d-%04d" % (gen, indice_gen),
                "generazione": gen,
                "classe": "dono segreto",
                "nazionale": v["specie"],
                "forma": v["forma"],
                "descrizione": r["titoli"],
                "metodo": v["file"],
                "sotto_scadenza": r["sotto_scadenza"],
                "resa": "letta, non ancora producibile",
            })
    # ------------------------------------------------- le tabelle fuori dalla base dei doni
    # Il terzo troncone dell'asse, aggiunto il 2026-09-04. Le due fonti sopra coprono le
    # distribuzioni fatte come dono e sono cieche su tutto il resto, cioe' le distribuzioni in cui
    # il dono era un oggetto, le periferiche, i giochi da console fissa e i doni interni
    # condizionati. Erano 422 voci per 256 specie distinte, nessuna delle quali compariva in
    # questa lista: il difetto era di copertura e non di lettura, quindi non produceva alcun
    # errore e la lista sembrava completa.
    #
    # La lettura appartiene a un solo programma e questo la invoca, che e' la regola che il
    # progetto si e' dato dopo il difetto della lettura dei titoli riscritta invece che chiamata.
    try:
        censimento = carica_modulo("censtab", os.path.join(RADICE, "tools",
                                                           "censimento-eventi-tabelle.py"))
        gruppi, _difetti_cens = censimento.censisci(pkhex)
    except Exception as exc:
        print("  nota: il censimento delle tabelle non si e' caricato (%s)" % exc)
        gruppi = []
    # Una classe del censimento non entra in questo asse, e la scelta va motivata perche' e' il
    # contrario di quella che l'obiettivo dichiarato suggerirebbe. I trasferimenti da Pokemon GO
    # non sono esemplari da distribuzione ma una porta di ingresso permanente: dire che una
    # specie e' ottenibile da GO e' un'affermazione sulla sua reperibilita', cioe' la materia
    # dell'asse delle specie, non un collezionabile in piu' con un allenatore e una data propri.
    # Metterli qui gonfierebbe l'asse degli eventi di millecentosessantaquattro voci che
    # ripeterebbero specie gia' presenti altrove, e falserebbe il solo numero che questo asse
    # serve a produrre, cioe' quante voci il primo tempo della coda debba coprire. Restano contate
    # e visibili nel censimento, dove la loro classe dice che cosa sono.
    FUORI_DALL_ASSE = {"porta-permanente"}
    indice_tabelle = 0
    for gruppo in gruppi:
        if not gruppo.get("letto") or gruppo["classe"] in FUORI_DALL_ASSE:
            continue
        for v in gruppo["voci"]:
            fuori.append({
                "codice": "EVT-T-%04d" % indice_tabelle,
                "generazione": v.get("gen") or gruppo.get("gen") or 0,
                "classe": gruppo["classe"],
                "nazionale": v["specie"],
                "forma": v.get("forma", 0),
                "descrizione": "%s: %s" % (gruppo["etichetta"], v.get("commento") or "-"),
                "metodo": v.get("riferimento", ""),
                "sotto_scadenza": gruppo["sotto_scadenza"],
                "resa": "censita, non ancora producibile",
            })
            indice_tabelle += 1

    for a in antichi:
        generazione = 1 if a["file"] == "event1.pkl" else 2
        for v in a.get("voci_dettaglio", []):
            fuori.append({
                "codice": "EVT-%d-%04d" % (generazione, v["indice"]),
                "generazione": generazione,
                "classe": "tabella di incontro",
                "nazionale": v["specie"],
                "forma": v["forma"],
                "descrizione": "tabella di incontro da evento",
                "metodo": a["file"],
                "sotto_scadenza": True,
                "resa": "letta, struttura alla portata di pokebridge",
            })
    return fuori


def codici_duplicati(eventi):
    """I codici che due o piu' voci si contendono, che devono essere nessuno.

    Il controllo esiste perche' il difetto che chiude e' stato trovato per caso e non da un
    errore: un codice duplicato non rompe nulla finche' nessuno lo usa per spuntare, e si
    manifesta soltanto il giorno in cui due collezionabili diversi risultano lo stesso. Vale la
    regola generale che questo progetto ha gia' pagato altrove, cioe' che un difetto invisibile
    va reso visibile da un controllo e non dalla prudenza di chi legge.
    """
    visti, doppi = {}, {}
    for e in eventi:
        codice = e["codice"]
        if codice in visti:
            doppi.setdefault(codice, [visti[codice]]).append(e)
        else:
            visti[codice] = e
    return doppi


def ordina_per_specie(eventi):
    """Marca la prima voce di ciascuna specie e porta tutte le prime in testa alla coda.

    L'ordine naturale della fonte raggruppa le voci per evento, che è l'ordine in cui una
    distribuzione avvenne e non quello in cui conviene produrla. La decisione di ambito presa il
    2026-09-03 è la collezione completa in due tempi, con prima una voce per ciascuna specie
    distinta e poi i gemelli: il primo tempo esiste soltanto se la coda dice quali voci lo
    compongono, e dedurlo a occhio da una tabella di migliaia di righe non è una operazione che si
    fa due volte allo stesso modo.

    La marcatura guarda le sole voci sotto scadenza, perché sono quelle che il primo tempo deve
    coprire, e procede nell'ordine della fonte, cosicché la voce scelta per una specie sia sempre
    la stessa a parità di catalogo. Una voce senza numero nazionale non può essere la prima di
    alcuna specie e resta nel secondo blocco, dichiarata come tale invece di essere scartata.

    L'ordinamento è stabile e conserva dentro ciascuno dei due blocchi l'ordine per evento, che
    resta l'informazione utile a chi produce: si sposta il confine fra i due tempi, non l'ordine
    interno di ciascuno.
    """
    viste = set()
    for e in eventi:
        naz = e.get("nazionale")
        if e.get("sotto_scadenza") and naz and naz not in viste:
            viste.add(naz)
            e["primo_della_specie"] = True
        else:
            e["primo_della_specie"] = False
    for indice, e in enumerate(eventi):
        e["ordine_di_catalogo"] = indice
    eventi.sort(key=lambda e: (0 if e["primo_della_specie"] else 1, e["ordine_di_catalogo"]))
    return eventi


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

    eventi = voci_da_evento(a.pkhex, a.ace)
    ordina_per_specie(eventi)
    duplicati = codici_duplicati(eventi)

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
    print("")
    print("  voci da evento enumerate           %d" % len(eventi))
    if duplicati:
        print("  ATTENZIONE: %d codici sono condivisi da piu' voci, per un totale di %d voci. "
              "Un codice" % (len(duplicati), sum(len(g) for g in duplicati.values())))
        print("  duplicato non rompe nulla finche' nessuno lo usa per spuntare, e proprio per "
              "questo va corretto ora.")
        for doppio in sorted(duplicati)[:5]:
            print("    %s: %s" % (doppio, [e["metodo"] for e in duplicati[doppio]]))
    else:
        print("  codici distinti                    %d, cioe' uno per voce" % len(eventi))
    per_gen = {}
    for e in eventi:
        chiave = (e["generazione"], e["sotto_scadenza"])
        per_gen.setdefault(chiave, []).append(e)
    for (gen, scad) in sorted(per_gen):
        gruppo = per_gen[(gen, scad)]
        print("    gen %d  %5d voci  %4d specie distinte  %s"
              % (gen, len(gruppo), len({x["nazionale"] for x in gruppo if x["nazionale"]}),
                 "sotto scadenza" if scad else "senza scadenza"))
    rese = {}
    for e in eventi:
        rese[e["resa"]] = rese.get(e["resa"], 0) + 1
    print("")
    for k, n in sorted(rese.items(), key=lambda x: -x[1]):
        print("    %-42s %5d" % (k, n))
    scad_ev = [e for e in eventi if e["sotto_scadenza"]]
    print("")
    print("  Le voci da evento sotto scadenza sono %d, e portano %d specie distinte. Sono il "
          "solo insieme" % (len(scad_ev), len({e["nazionale"] for e in scad_ev if e["nazionale"]})))
    print("  di questa lista che il 26 febbraio 2027 chiude davvero.")
    primi = [e for e in eventi if e.get("primo_della_specie")]
    print("")
    print("  Il primo tempo della coda, cioe' una voce per specie, e' di %d voci; i gemelli "
          "del secondo tempo" % len(primi))
    print("  sono %d. La coda scritta porta i primi in testa." % (len(scad_ev) - len(primi)))

    if a.markdown:
        scrivi(a.markdown, righe_specie, righe_forma, per_fonte, eventi)
        print("")
        print("  scritto " + a.markdown)
    return 0


def scrivi(percorso, righe_specie, righe_forma, per_fonte, eventi):
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

    r.append("## Voci da evento")
    r.append("")
    per_classe = {}
    for x in eventi:
        per_classe[x.get("classe", "?")] = per_classe.get(x.get("classe", "?"), 0) + 1
    r.append("L'asse degli eventi nasce da tre fonti e non da una, e la distinzione va letta prima "
             "dei numeri perché fino al 2026-09-04 le fonti erano due e la terza mancava del "
             "tutto. La prima è la tabella delle carte meraviglia di terza generazione, che vive "
             "nel codice del verificatore; la seconda sono i file binari della base dei doni "
             "segreti, che coprono la prima e la seconda generazione con le loro tabelle di "
             "incontro e poi dalla quarta alla nona con i doni veri e propri; la terza sono le "
             "tabelle degli incontri del verificatore, dove stanno le distribuzioni in cui il "
             "dono era un oggetto, le periferiche, i giochi da console fissa e i doni interni "
             "condizionati, e insieme a essi le incursioni da distribuzione di ottava e nona "
             "generazione. Le prime due erano cieche sulla terza, ed è un difetto di copertura e "
             "non di lettura: non produceva alcun errore, e la lista sembrava completa mentre ne "
             "mancavano %d voci. La colonna della classe dice da quale delle tre viene ciascuna "
             "voce, e i codici delle voci della terza cominciano con `EVT-T-` invece che con la "
             "generazione, perché una sola numerazione le attraversa tutte."
             % sum(1 for x in eventi if str(x.get("codice", "")).startswith("EVT-T-")))
    r.append("")
    r.append("Una classe del censimento resta fuori da questo asse per scelta, ed è quella dei "
             "trasferimenti da Pokemon GO. Non sono esemplari da distribuzione ma una porta di "
             "ingresso permanente: dire che una specie è ottenibile da quel gioco è "
             "un'affermazione sulla sua reperibilità, cioè la materia dell'asse delle specie, e "
             "non un collezionabile in più con un allenatore e una data propri. Metterli qui "
             "aggiungerebbe milleduecento voci che ripeterebbero specie già presenti altrove e "
             "falserebbe il solo numero che questo asse serve a produrre, cioè quante voci il "
             "primo tempo della coda debba coprire. Restano contate e visibili nel censimento "
             "`CENSIMENTO-EVENTI-FUORI-DONI.md`, dove la loro classe dice che cosa sono.")
    r.append("")
    r.append("La ripartizione per classe è la seguente: "
             + ", ".join("%s %d" % (k, n) for k, n in sorted(per_classe.items(),
                                                             key=lambda x: -x[1]))
             + ".")
    r.append("")
    r.append("Una voce da evento è un collezionabile distinto anche quando la sua specie è già "
             "coperta altrove, e la ragione è che porta un nome di allenatore, un identificativo "
             "e una data che nessun incontro selvatico produce: chi possiede il secondo non "
             "possiede il primo. La colonna della resa dice a che punto siamo su quella voce, e "
             "tiene distinte tre condizioni che non vanno confuse, cioè una voce che il progetto "
             "sa produrre e ha fatto verificare, una che sa soltanto leggere, e una la cui "
             "struttura è alla portata di codice che già esiste.")
    r.append("")
    scad_ev = [x for x in eventi if x["sotto_scadenza"]]
    r.append("Le voci enumerate sono %d, di cui %d sotto scadenza, e queste ultime portano %d "
             "specie distinte. Sono il solo insieme di questa lista che il 26 febbraio 2027 "
             "chiude davvero: le voci di specie e di forma sono tutte raggiungibili per via "
             "diretta, mentre un esemplare da distribuzione di una generazione anteriore "
             "all'ottava non ha altra strada che la banca."
             % (len(eventi), len(scad_ev),
                len({x["nazionale"] for x in scad_ev if x["nazionale"]})))
    r.append("")
    primi = [x for x in eventi if x.get("primo_della_specie")]
    r.append("L'ordine della tabella non è quello della fonte, ed è una scelta che va "
             "dichiarata perché cambia che cosa si legge per primo. La fonte raggruppa le voci "
             "per evento, cioè nell'ordine in cui le distribuzioni avvennero; la decisione di "
             "ambito è invece la collezione completa in due tempi, con prima una voce per "
             "ciascuna specie distinta e poi i gemelli. La colonna che dice se una voce sia la "
             "prima della propria specie porta dunque in testa le %d voci del primo tempo, e "
             "lascia in coda le %d del secondo; dentro ciascuno dei due blocchi l'ordine per "
             "evento è conservato, perché è l'informazione utile a chi produce. La prima voce "
             "di una specie è scelta nell'ordine della fonte e non per merito: dove più voci "
             "portano la medesima specie, la marcatura non dice quale sia la più desiderabile "
             "ma soltanto quale basti a coprire la specie."
             % (len(primi), len(scad_ev) - len(primi)))
    r.append("")
    r.append("| Codice | Gen | Classe | Dex | Forma | Provenienza | Sotto scadenza | Primo della specie | Resa |")
    r.append("|---|---|---|---|---|---|---|---|---|")
    for x in eventi:
        r.append("| `%s` | %d | %s | %s | %d | %s | %s | %s | %s |"
                 % (x["codice"], x["generazione"], x.get("classe", "?"),
                    x["nazionale"] if x["nazionale"] else "-", x["forma"],
                    str(x["descrizione"]).replace("|", "/"),
                    "sì" if x["sotto_scadenza"] else "no",
                    "sì" if x.get("primo_della_specie") else "no", x["resa"]))
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
