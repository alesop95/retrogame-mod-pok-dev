#!/usr/bin/env python3
"""Estrae dai thread Smogon le squadre dichiarate e le serie di vittorie con cui sono state provate, e le ordina per risultato.

Perche' esiste
--------------

Il catalogo degli avversari dice contro che cosa si combatte; non dice che cosa ha funzionato. Quello lo dicono le persone che una serie l'hanno tenuta per centinaia di lotte e hanno poi scritto la squadra con cui l'hanno tenuta, e quelle dichiarazioni stanno sparse in duemilaquattrocento post, insieme a domande, correzioni e discussioni che non portano alcuna squadra. Leggerli tutti non e' praticabile e non e' nemmeno utile: la parte che serve ha una forma riconoscibile, cioe' il blocco in cui una specie e' seguita dallo strumento dopo la chiocciola, dalla natura, dai punti base e dalle mosse col trattino, e accanto una cifra che dichiara quante lotte ha retto.

Questo strumento fa quindi il lavoro deterministico che `token-economy.md` prescrive di tenere su codice: riconosce quei blocchi, li associa al post e al suo autore, cerca nello stesso post una dichiarazione di serie e l'edificio a cui si riferisce, e ordina il risultato per lunghezza della serie. Cio' che resta da fare a una lettura umana e' guardare le prime venti righe di una tabella invece di duemila post, che e' precisamente il salto dal Livello 1 al Livello 2.

Che cosa non fa, e va detto
---------------------------

Non giudica una squadra e non decide se la serie dichiarata sia vera. La lunghezza di una serie e' una affermazione di chi la scrive, e il thread stesso avverte nel proprio post di apertura che il sistema regge su una fiducia reciproca e che l'amministratore si riserva di rifiutare una dichiarazione dubbia. Qui la cifra si riporta con l'autore accanto, come dichiarazione e non come misura, ed e' la stessa disciplina che `interaction-style.md` impone su qualunque contenuto non verificato.

Non riconosce nemmeno tutte le forme in cui una squadra si puo' scrivere. Alcuni post mettono la squadra in un'immagine, altri la descrivono in prosa, altri rimandano a un post precedente. Cio' che sfugge non e' perduto, perche' il grezzo resta su disco e l'indice di Livello 1 elenca comunque il post fra quelli con una squadra probabile: semplicemente non entra in questa tabella, e il conteggio finale dichiara quanti post contrassegnati non abbiano prodotto alcun blocco, cosicche' la copertura parziale resti dichiarata invece di somigliare a una completa.

Uso
---

    python gba-save-extraction-smeraldo/tools/parco_lotta_squadre_dai_thread.py --derivato _notes/fonti/raccolte/smogon-parco-lotta-2026-09-21/derivato --out _notes/fonti/raccolte/smogon-parco-lotta-2026-09-21
"""

import argparse
import collections
import json
import re
from pathlib import Path

NATURE = ("Adamant|Modest|Jolly|Timid|Bold|Calm|Careful|Impish|Brave|Quiet|Relaxed|Sassy|Hasty|Naive|"
          "Lonely|Mild|Rash|Naughty|Gentle|Docile|Hardy|Serious|Bashful|Quirky|Lax")

# Il capo di un blocco di squadra: la specie, la chiocciola, lo strumento. E' la forma che questo forum usa
# da vent'anni e non cambia, il che la rende un ancoraggio piu' solido della riga delle mosse.
CAPO = re.compile(r"^[ \t]*([A-Z][A-Za-z2.'♀♂-]{2,14}(?:\s[A-Z][a-z]+)?)\s*@\s*([A-Za-z][A-Za-z .'-]{2,24}?)\s*$", re.M)
RIGA_NATURA = re.compile(r"\b(%s)\b\s*Nature" % NATURE, re.I)
RIGA_PUNTI = re.compile(r"EVs?\s*:\s*([0-9]{1,3}(?:\s*(?:HP|Atk|Def|SpA|SpD|Spe|/)\s*[0-9]{0,3})*[^\n]*)", re.I)
RIGA_MOSSA = re.compile(r"^[ \t]*-\s*([A-Z][A-Za-z' -]{2,22})\s*$", re.M)
ABILITA = re.compile(r"\bAbility\s*:\s*([A-Za-z ]{3,20})", re.I)

# Le forme in cui su questo forum si dichiara una serie. Il numero si prende sempre dal gruppo uno.
SERIE = [
    re.compile(r"\bstreak\s+of\s+([0-9]{2,4})\b", re.I),
    re.compile(r"\b([0-9]{2,4})\s+(?:win|battle)s?\s+streak\b", re.I),
    re.compile(r"\bstreak\s*:?\s*([0-9]{2,4})\b", re.I),
    re.compile(r"\b([0-9]{2,4})\s+(?:consecutive\s+)?wins\b", re.I),
    re.compile(r"\bwon\s+([0-9]{2,4})\s+(?:straight|in a row)\b", re.I),
    re.compile(r"\bended?\s+at\s+([0-9]{2,4})\b", re.I),
]

# Il testo che un post cita da un altro va tolto prima di cercarvi una squadra, altrimenti chi risponde a
# un rapporto si vede attribuire la squadra di chi lo ha scritto, e la stessa serie compare due volte con due
# autori diversi. Il difetto si e' manifestato al primo giro, con quattro coppie di righe identiche fra le
# prime venti, ed e' il genere di errore che in una tabella ordinata per risultato falsa proprio la testa.
SENZA_CITAZIONI = re.compile(r"\[citazione\].*?\[/citazione\]", re.S)

# Gli edifici nominati in inglese, con il nome italiano verificato accanto. La tabella e' la stessa della
# sezione 3 di STUDIO-04 e sta qui perche' l'uscita di questo strumento si legge insieme a quel documento.
EDIFICI = [
    ("Tower", "Torre Lotta"),
    ("Palace", "Palazzo Lotta"),
    ("Factory", "Azienda Lotta"),
    ("Pyramid", "Piramide Lotta"),
    ("Dome", "Cupola Lotta"),
    ("Arena", "Dojo Lotta"),
    ("Pike", "Serpe Lotta"),
]


def blocchi_squadra(testo):
    """Riconosce i blocchi di squadra dentro un post e ne restituisce le voci.

    L'ancoraggio e' la riga con la chiocciola, e cio' che appartiene a quella voce e' quanto la segue fino alla riga con la chiocciola successiva o fino a una riga vuota doppia. E' una regola grossolana e lo e' di proposito: una regola fine su un testo scritto a mano da centinaia di persone diverse sbaglia piu' spesso di una grossolana, e qui un falso positivo costa una riga in piu' da guardare mentre un falso negativo costa una squadra perduta.
    """
    voci = []
    capi = list(CAPO.finditer(testo))
    for i, capo in enumerate(capi):
        fine = capi[i + 1].start() if i + 1 < len(capi) else len(testo)
        corpo = testo[capo.end():fine]
        taglio = corpo.find("\n\n\n")
        if taglio > 0:
            corpo = corpo[:taglio]
        natura = RIGA_NATURA.search(corpo)
        punti = RIGA_PUNTI.search(corpo)
        mosse = [m.group(1).strip() for m in RIGA_MOSSA.finditer(corpo)][:4]
        if not (natura or punti or len(mosse) >= 2):
            continue
        abilita = ABILITA.search(corpo)
        voci.append({
            "specie": capo.group(1).strip(),
            "strumento": capo.group(2).strip(),
            "natura": natura.group(1).capitalize() if natura else None,
            "punti_base": punti.group(1).strip()[:60] if punti else None,
            "abilita": abilita.group(1).strip() if abilita else None,
            "mosse": mosse,
        })
    return voci


def serie_dichiarata(testo):
    valori = []
    for r in SERIE:
        for m in r.finditer(testo):
            n = int(m.group(1))
            if 7 <= n <= 9999:
                valori.append(n)
    return max(valori) if valori else None


def edificio_nominato(testo):
    conteggi = [(testo.lower().count(ingl.lower()), ingl, ita) for ingl, ita in EDIFICI]
    conteggi.sort(reverse=True)
    if conteggi[0][0] == 0:
        return None, None
    return conteggi[0][1], conteggi[0][2]


def leggi(cartella):
    rapporti = []
    contrassegnati = 0
    senza_blocco = 0
    for percorso in sorted(Path(cartella).glob("*.md")):
        testo = percorso.read_text(encoding="utf-8")
        pezzi = re.split(r"\n## (post-\d+), pagina (\d+), di ([^,]+), ([^\n]*)\n", testo)
        for i in range(1, len(pezzi), 5):
            identificativo, pagina, autore, data = pezzi[i], int(pezzi[i + 1]), pezzi[i + 2], pezzi[i + 3]
            corpo = SENZA_CITAZIONI.sub(chr(10), pezzi[i + 4])
            marcato = "[SQUADRA PROBABILE]" in data
            if marcato:
                contrassegnati += 1
            voci = blocchi_squadra(corpo)
            if not voci:
                if marcato:
                    senza_blocco += 1
                continue
            ingl, ita = edificio_nominato(corpo)
            rapporti.append({
                "fonte": percorso.stem,
                "post": identificativo,
                "pagina": pagina,
                "autore": autore.strip(),
                "data": data.replace("[SQUADRA PROBABILE]", "").strip()[:10],
                "edificio_inglese": ingl,
                "edificio": ita,
                "serie_dichiarata": serie_dichiarata(corpo),
                "esemplari": voci,
            })
    return rapporti, contrassegnati, senza_blocco


def scrivi(uscita, rapporti, contrassegnati, senza_blocco):
    uscita = Path(uscita)
    uscita.joinpath("squadre.json").write_text(json.dumps(rapporti, ensure_ascii=False, indent=1), encoding="utf-8")

    con_serie = [r for r in rapporti if r["serie_dichiarata"]]
    con_serie.sort(key=lambda r: -r["serie_dichiarata"])

    r = ["# Le squadre dichiarate nei thread, ordinate per serie", "",
         "> Generato da `gba-save-extraction-smeraldo/tools/parco_lotta_squadre_dai_thread.py`. Non si modifica a mano: si rigenera. Va letto insieme alla sezione 3 di `STUDIO-04`, che porta i nomi italiani degli edifici.", "",
         "La lunghezza della serie e' una dichiarazione di chi scrive e non una misura: il post di apertura del thread avverte esso stesso che il sistema regge sulla fiducia reciproca e che una dichiarazione dubbia puo' essere rifiutata. Qui la cifra si riporta con l'autore accanto e in quella forma va citata.", "",
         "Blocchi di squadra riconosciuti: %d in altrettanti post, di cui %d con una serie dichiarata. Post che l'indice di Livello 1 contrassegnava come contenenti una squadra: %d, di cui %d non hanno prodotto alcun blocco, perche' mettono la squadra in un'immagine, la descrivono in prosa o rimandano a un post precedente. Quei post restano nel grezzo e nell'indice, e questa riga esiste perche' la copertura parziale resti dichiarata." % (len(rapporti), len(con_serie), contrassegnati, senza_blocco), ""]

    r.append("## Le cinquanta serie piu' lunghe, con la squadra dichiarata")
    r.append("")
    r.append("| Serie | Edificio | Autore | Post | Squadra |")
    r.append("|---|---|---|---|---|")
    for v in con_serie[:50]:
        squadra = "; ".join("%s @ %s%s" % (e["specie"], e["strumento"], (" (" + e["natura"] + ")") if e["natura"] else "") for e in v["esemplari"][:6])
        r.append("| %d | %s | %s | %s pagina %d | %s |" % (
            v["serie_dichiarata"], v["edificio"] or "non dichiarato", v["autore"], v["post"], v["pagina"], squadra))
    r.append("")

    r.append("## Quali specie ricorrono nelle squadre dichiarate, per edificio")
    r.append("")
    r.append("E' il dato che dice quali scelte la pratica ha corroborato, ed e' l'altra meta' del lavoro rispetto alle distribuzioni di `SPOGLIO.md`, che dicono invece che cosa si incontra. Si contano i post e non gli esemplari, cosicche' un autore che ripete la stessa squadra in dieci post pesi dieci e non sessanta.")
    r.append("")
    per_edificio = collections.defaultdict(collections.Counter)
    strumenti = collections.defaultdict(collections.Counter)
    for v in rapporti:
        chiave = v["edificio"] or "non dichiarato"
        for e in {x["specie"] for x in v["esemplari"]}:
            per_edificio[chiave][e] += 1
        for e in {x["strumento"] for x in v["esemplari"]}:
            strumenti[chiave][e] += 1
    for _, ita in EDIFICI:
        if ita not in per_edificio:
            continue
        r.append("### %s, %d post con una squadra" % (ita, sum(1 for v in rapporti if v["edificio"] == ita)))
        r.append("")
        r.append("Specie: " + ", ".join("%s (%d)" % x for x in per_edificio[ita].most_common(20)) + ".")
        r.append("")
        r.append("Strumenti: " + ", ".join("%s (%d)" % x for x in strumenti[ita].most_common(12)) + ".")
        r.append("")
    uscita.joinpath("SQUADRE.md").write_text("\n".join(r) + "\n", encoding="utf-8")


def main():
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--derivato", required=True)
    p.add_argument("--out", required=True)
    args = p.parse_args()
    rapporti, contrassegnati, senza_blocco = leggi(args.derivato)
    scrivi(args.out, rapporti, contrassegnati, senza_blocco)
    print("post con almeno un blocco di squadra: %d" % len(rapporti))
    print("di cui con una serie dichiarata:      %d" % sum(1 for r in rapporti if r["serie_dichiarata"]))
    print("contrassegnati dall'indice:           %d, senza blocco: %d" % (contrassegnati, senza_blocco))
    print("uscita in %s" % args.out)


if __name__ == "__main__":
    main()
