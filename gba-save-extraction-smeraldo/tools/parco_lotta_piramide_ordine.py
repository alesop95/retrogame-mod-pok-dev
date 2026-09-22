#!/usr/bin/env python3
"""Calcola, per ciascuno dei venti giri della Piramide Lotta, quale esemplare della squadra conviene mandare per primo.

Perche' esiste
--------------

La guida di chi ha completato i sette simboli d'oro dice quale dei tre esemplari condurre in ciascuno dei primi dieci giri, perche' l'oro arriva a settanta piani e oltre non serviva. I giri sono pero' venti, e chi punta a una serie lunga li attraversa tutti: per i dieci successivi non esiste alcuna fonte, e riempirli a occhio sarebbe esattamente il genere di affermazione inferita che `interaction-style.md` vieta di presentare come fatto.

Questo strumento li calcola invece di indovinarli, e adotta il criterio che la guida stessa dichiara di seguire, cioe' mandare per primo chi mette a terra in un colpo il maggior numero delle otto specie del giro, e in mancanza di quello chi regge meglio. E' un calcolo di danno e non un confronto di tipi, e la distinzione non e' accademica: una prima versione di questo strumento confrontava i soli tipi e ricostruiva la scelta della guida in due giri su dieci, cioe' peggio del caso. La tabella dei tipi da sola non basta perche' un colpo efficace di una mossa debole non abbatte, e una mossa neutra e potente abbatte.

La ragione per cui un calcolo e' credibile qui, e non lo sarebbe altrove, sta nel presidio: lo strumento calcola anche i primi dieci giri, per i quali la risposta e' nota, e la confronta con quella della guida. La concordanza si stampa in testa all'uscita e va guardata prima di usare la tabella. Se le due concordano su quei dieci, la stessa formula applicata ai dieci successivi vale qualcosa; se divergono, chi legge sa quanto fidarsi. E' la stessa logica del confronto fra due copie indipendenti del catalogo degli avversari, applicata a una previsione invece che a un dato.

Le ipotesi del calcolo, che vanno dichiarate
--------------------------------------------

Gli esemplari della squadra sono a livello 50 con punti individuali perfetti e i punti base del catalogo, perche' sono generati. Gli esemplari selvatici della Piramide hanno il livello che il sorgente dichiara per quel giro, punti individuali medi, nessun punto base e natura neutra: il gioco li genera con livello variabile di cinque in piu' o in meno e natura casuale, quindi il conto e' sul caso centrale e non sul peggiore. Il danno usa la formula della terza generazione con il tiro medio e senza colpi critici, e la divisione fra mosse fisiche e speciali segue il tipo della mossa e non la mossa stessa, che e' la regola di quella generazione e non di quelle successive.

Che cosa non calcola
--------------------

Non calcola il piano a cui sostituire chi conduce, perche' quello dipende dai punti salute residui e dagli oggetti raccolti dentro l'edificio, che sono stato di partita e non tabella. Non tiene conto delle abilita' ne' degli effetti secondari delle mosse.

Uso
---

    python gba-save-extraction-smeraldo/tools/parco_lotta_piramide_ordine.py --sorgente <clone di pret/pokeemerald> --giri _notes/fonti/parco-lotta-spoglio-2026-09-21/piramide-giri.json --catalogo gba-save-extraction-smeraldo/squadre-parco-lotta.json --out _notes/fonti/parco-lotta-spoglio-2026-09-21/PIRAMIDE-ORDINE.md
"""

import argparse
import json
import re
import sys
from pathlib import Path

MOLTIPLICATORE = {"TYPE_MUL_NO_EFFECT": 0.0, "TYPE_MUL_NOT_EFFECTIVE": 0.5, "TYPE_MUL_SUPER_EFFECTIVE": 2.0}

# L'ordine di conduzione che la guida al completamento dichiara per i primi dieci giri, in due parti:
# chi conduce e, dove previsto, chi lo sostituisce e da quale piano. Serve da controllo sul calcolo e non
# da dato: se il calcolo non ricostruisce questi dieci, non merita fiducia sugli altri.
#
# Il confronto si fa su entrambe le parti e non sulla sola prima, ed e' una correzione a una prima stesura
# che confrontava il solo conduttore. In sei giri su dieci la guida non nomina un esemplare ma due, cioe'
# prescrive di alternarli dentro lo stesso giro: contare come divergenza il caso in cui il calcolo indica
# il secondo dei due significherebbe punire una risposta che la guida da' essa stessa. I due conteggi
# restano pero' entrambi nell'uscita, perche' misurano cose diverse e il piu' severo e' il piu' onesto.
GUIDA = {
    1: {"conduce": "Latios", "cambio": None},
    2: {"conduce": "Latios", "cambio": None},
    3: {"conduce": "Latios", "cambio": None},
    4: {"conduce": "Metagross", "cambio": None},
    5: {"conduce": "Metagross", "cambio": "Latios"},
    6: {"conduce": "Metagross", "cambio": "Latios"},
    7: {"conduce": "Metagross", "cambio": "Latios"},
    8: {"conduce": "Latios", "cambio": "Swampert"},
    9: {"conduce": "Latios", "cambio": "Metagross"},
    10: {"conduce": "Swampert", "cambio": "Metagross"},
}


def tabella_tipi(percorso_sorgente):
    """Estrae `gTypeEffectiveness` da `src/battle_main.c`.

    La tabella e' una sequenza piatta di terne, attaccante-difensore-moltiplicatore, e contiene una riga sentinella a meta' che separa le voci ordinarie da quelle che valgono solo quando l'immunita' e' stata rimossa. Si legge fino alla sentinella, perche' oltre quella le voci descrivono un caso che al Parco non si presenta.
    """
    percorso = Path(percorso_sorgente).joinpath("src/battle_main.c")
    if not percorso.exists():
        sys.exit("sorgente non trovato: %s\nserve un clone di pret/pokeemerald" % percorso)
    testo = percorso.read_text(encoding="utf-8")
    blocco = re.search(r"gTypeEffectiveness\[\d+\]\s*=\s*\{(.*?)\n\};", testo, re.S)
    if blocco is None:
        sys.exit("gTypeEffectiveness non trovata: la forma della fonte e' cambiata, non indovino")
    corpo = blocco.group(1).split("TYPE_FORESIGHT")[0]
    voci = [v.strip() for v in corpo.replace("\n", " ").split(",") if v.strip()]
    tabella = {}
    for i in range(0, len(voci) - 2, 3):
        att, dif, mul = voci[i], voci[i + 1], voci[i + 2]
        if not att.startswith("TYPE_") or mul not in MOLTIPLICATORE:
            continue
        tabella[(att[5:].title(), dif[5:].title())] = MOLTIPLICATORE[mul]
    if len(tabella) < 60:
        sys.exit("tabella dei tipi letta solo in parte: %d voci" % len(tabella))
    return tabella


# In terza generazione una mossa e' fisica o speciale secondo il proprio TIPO e non secondo se stessa.
# E' la regola che le generazioni successive hanno abbandonato, ed e' il primo errore che commette chi
# porta qui un calcolatore scritto per un gioco piu' recente.
TIPI_FISICI = {"Normal", "Fighting", "Flying", "Ground", "Rock", "Bug", "Ghost", "Poison", "Steel"}

TIRO_MEDIO = 0.925
IV_SELVATICO = 15


def efficacia(tabella, tipo_mossa, tipi_bersaglio):
    valore = 1.0
    for t in tipi_bersaglio:
        valore *= tabella.get((tipo_mossa, t), 1.0)
    return valore


def statistica(base, iv, ev, livello, moltiplicatore):
    return int((int((2 * base + iv + ev // 4) * livello / 100) + 5) * moltiplicatore)


def punti_salute(base, iv, ev, livello):
    return int((2 * base + iv + ev // 4) * livello / 100) + livello + 10


def leggi_punti_base(testo):
    """Legge una stringa come `252 HP / 252 Atk / 4 Spe` nella forma che il calcolo usa."""
    etichette = {"hp": "hp", "atk": "atk", "def": "def", "spa": "spa", "spd": "spd", "spe": "spe"}
    fuori = {k: 0 for k in etichette.values()}
    for pezzo in testo.split("/"):
        parti = pezzo.strip().split()
        if len(parti) == 2 and parti[0].isdigit():
            chiave = etichette.get(parti[1].lower())
            if chiave:
                fuori[chiave] = int(parti[0])
    return fuori


def danno(tabella, attaccante, mossa, difensore, livello_difensore):
    """Danno medio di una mossa, in frazione dei punti salute del bersaglio."""
    tipo = mossa["type"]
    potenza = mossa.get("power") or 0
    if not potenza:
        return 0.0
    eff = efficacia(tabella, tipo, difensore["tipi"])
    if eff == 0.0:
        return 0.0
    fisica = tipo in TIPI_FISICI
    attacco = attaccante["atk"] if fisica else attaccante["spa"]
    difesa = statistica(difensore["base"]["def" if fisica else "spd"], IV_SELVATICO, 0, livello_difensore, 1.0)
    grezzo = int(int(int(2 * attaccante["livello"] / 5 + 2) * potenza * attacco / difesa) / 50) + 2
    stab = 1.5 if tipo in attaccante["tipi"] else 1.0
    salute = punti_salute(difensore["base"]["hp"], IV_SELVATICO, 0, livello_difensore)
    return grezzo * stab * eff * TIRO_MEDIO / salute


def main():
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--sorgente", required=True)
    p.add_argument("--giri", required=True)
    p.add_argument("--catalogo", required=True)
    p.add_argument("--specie", required=True, help="pokemon.js di DomeAssistantWeb, per tipi e statistiche base")
    p.add_argument("--mosse", required=True, help="moves.js di DomeAssistantWeb, per tipo e potenza di ogni mossa")
    p.add_argument("--nature", required=True, help="natures.js di DomeAssistantWeb")
    p.add_argument("--out", required=True)
    args = p.parse_args()

    sys.path.insert(0, str(Path(__file__).parent))
    from parco_lotta_spoglio_avversari import _oggetto_javascript

    tabella = tabella_tipi(args.sorgente)
    giri = json.loads(Path(args.giri).read_text(encoding="utf-8"))
    catalogo = json.loads(Path(args.catalogo).read_text(encoding="utf-8"))
    dati_specie = _oggetto_javascript(Path(args.specie).read_text(encoding="utf-8"), "pokemon")
    dati_mosse = _oggetto_javascript(Path(args.mosse).read_text(encoding="utf-8"), "moves")
    dati_nature = _oggetto_javascript(Path(args.nature).read_text(encoding="utf-8"), "natures")

    piramide = next(s for s in catalogo["squadre"] if s["edificio"] == "Piramide Lotta")
    livello = catalogo["livello"]
    squadra = []
    for v in piramide["esemplari"]:
        e = catalogo["esemplari"][v["chiave"]]
        mosse = list(e["mosse"])
        for vecchia, nuova in (v.get("mosse_sostituite") or {}).items():
            if vecchia in mosse:
                mosse[mosse.index(vecchia)] = nuova
        info = dati_specie[e["specie"]]
        pb = leggi_punti_base(e["punti_base"])
        mult = dati_nature[e["natura"]]["multipliers"]
        squadra.append({
            "nome": e["specie"],
            "livello": livello,
            "tipi": [t for t in (info.get("type1"), info.get("type2")) if t],
            "base": info["baseStats"],
            "atk": statistica(info["baseStats"]["atk"], 31, pb["atk"], livello, mult["atk"]),
            "spa": statistica(info["baseStats"]["spa"], 31, pb["spa"], livello, mult["spa"]),
            "mosse": [dati_mosse[m] for m in mosse if m in dati_mosse and dati_mosse[m].get("power")],
        })

    righe = []
    concordi, concordi_impiego, confrontati = 0, 0, 0
    for g in giri:
        bersagli = []
        for v in g["specie"]:
            info = dati_specie.get(v["specie"])
            if info is None:
                continue
            bersagli.append({
                "nome": v["specie"],
                "livello": v["livello"] or livello,
                "tipi": [t for t in (info.get("type1"), info.get("type2")) if t],
                "base": info["baseStats"],
                "mosse": [dati_mosse[m] for m in v["mosse"] if m in dati_mosse and dati_mosse[m].get("power")],
            })
        punteggi = []
        for membro in squadra:
            abbattuti, subiti = 0, 0
            for b in bersagli:
                migliore = max((danno(tabella, membro, m, b, b["livello"]) for m in membro["mosse"]), default=0.0)
                if migliore >= 1.0:
                    abbattuti += 1
                selvatico = {"atk": statistica(b["base"]["atk"], IV_SELVATICO, 0, b["livello"], 1.0),
                             "spa": statistica(b["base"]["spa"], IV_SELVATICO, 0, b["livello"], 1.0),
                             "tipi": b["tipi"], "livello": b["livello"]}
                bersaglio_nostro = {"base": membro["base"], "tipi": membro["tipi"]}
                peggiore = max((danno(tabella, selvatico, m, bersaglio_nostro, membro["livello"]) for m in b["mosse"]), default=0.0)
                if peggiore >= 0.5:
                    subiti += 1
            punteggi.append({"nome": membro["nome"], "abbattuti": abbattuti,
                             "colpi_pesanti_subiti": subiti, "saldo": abbattuti - subiti})
        punteggi.sort(key=lambda x: (-x["saldo"], -x["abbattuti"]))
        scelto = punteggi[0]["nome"]
        atteso = GUIDA.get(g["giro_sorgente"])
        if atteso:
            confrontati += 1
            impiegati = {atteso["conduce"]} | ({atteso["cambio"]} if atteso["cambio"] else set())
            if atteso["conduce"] == scelto:
                concordi += 1
            if scelto in impiegati:
                concordi_impiego += 1
        righe.append({"giro": g["giro_sorgente"], "tema": g["tema"], "calcolato": scelto,
                      "guida": atteso, "punteggi": punteggi, "specie": [b["nome"] for b in bersagli]})

    if concordi_impiego >= confrontati * 0.6:
        fiducia = ("sui dieci giri di cui la guida parla, il calcolo indica un esemplare che la guida impiega davvero in quel giro in **%d casi su %d**, e indovina anche quale dei due conduca in **%d su %d**. Il primo numero e' quello che conta per l'uso che se ne fa qui, cioe' sapere su chi appoggiarsi in un giro; il secondo dice che l'ordine fra i due membri impiegati resta materia di campo e non di calcolo. Su questa base le righe dall'undicesimo al ventesimo si leggono come una preferenza motivata, non come una prescrizione." % (concordi_impiego, confrontati, concordi, confrontati))
    else:
        fiducia = ("il calcolo indica un esemplare che la guida impiega in quel giro in **%d casi su %d soltanto**, e il conduttore esatto in %d su %d: NON e' affidabile, e le righe dall'undicesimo al ventesimo vanno trattate come una ipotesi da verificare sul campo invece che come una raccomandazione. La causa e' verosimilmente che la guida sceglie anche su criteri che questo calcolo non modella, per esempio la fuga dagli incontri, il consumo dei punti potere su sette piani senza cure, o la sopravvivenza cumulata invece che il singolo scontro." % (concordi_impiego, confrontati, concordi, confrontati))

    r = ["# L'ordine di conduzione alla Piramide Lotta, calcolato per tutti e venti i giri", "",
         "> Generato da `gba-save-extraction-smeraldo/tools/parco_lotta_piramide_ordine.py` sulla tabella dei tipi estratta da `pret/pokeemerald`, `src/battle_main.c`, e sulle statistiche base del catalogo degli avversari. Non si modifica a mano: si rigenera.", "",
         "Il criterio e' quello che la guida dichiara di seguire: conduce chi abbatte in un colpo il maggior numero delle otto specie del giro, meno il numero di quelle che gli portano via almeno meta' dei punti salute in un colpo solo. Le ipotesi del calcolo stanno nel docstring dello strumento e vanno lette prima della tabella.", "",
         "Controllo sul metodo: " + fiducia, "",
         "| Giro | Tema del bestiario | Calcolato | Guida: conduce, poi cambio | Abbattuti su otto, e colpi pesanti subiti |", "|---|---|---|---|---|"]
    for v in righe:
        dettaglio = ", ".join("%s %d abbattuti, %d subiti" % (x["nome"], x["abbattuti"], x["colpi_pesanti_subiti"]) for x in v["punteggi"])
        if v["guida"]:
            impiegati = [v["guida"]["conduce"]] + ([v["guida"]["cambio"]] if v["guida"]["cambio"] else [])
            segno = " poi ".join(impiegati)
            if v["calcolato"] not in impiegati:
                segno += " (diverge)"
        else:
            segno = "nessuna fonte"
        r.append("| %d | %s | %s | %s | %s |" % (v["giro"], v["tema"], v["calcolato"], segno, dettaglio))
    r.append("")
    Path(args.out).write_text("\n".join(r) + "\n", encoding="utf-8")
    Path(args.out).with_suffix(".json").write_text(json.dumps(righe, ensure_ascii=False, indent=1), encoding="utf-8")
    print("venti giri calcolati; sui primi dieci il calcolo indica un esemplare impiegato dalla guida in %d casi su %d, e il conduttore esatto in %d su %d" % (concordi_impiego, confrontati, concordi, confrontati))
    print("uscita in %s" % args.out)


if __name__ == "__main__":
    main()
