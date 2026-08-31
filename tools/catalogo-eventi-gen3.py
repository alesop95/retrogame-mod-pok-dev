#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera il catalogo delle distribuzioni di evento di generazione 3 dalla tabella di PKHeX.

Perché esiste
--------------
Il sottoprogetto della ricreazione delle distribuzioni ha bisogno di un inventario: quali
eventi sono esistiti, con quali campi visibili, e soprattutto con quale metodo di
generazione pseudocasuale, perché è il metodo e non il campo visibile a distinguere una
ricreazione fedele da un dato costruito a mano.

Quell'inventario esiste già, ed è la tabella `EncountersWC3.cs` di `PKHeX`, che vive nel
codice invece che in un documento perché, come dichiara il suo stesso commento, i dati di
generazione 3 non sono mai stati conservati in forma binaria uniforme e sono quindi
scritti a mano uno per uno. Trascriverla in prosa significherebbe garantire che le due
copie divergano alla prima correzione a monte: si genera, esattamente come le tabelle dei
caratteri del ponte fra generazioni.

Il metodo si legge come un dato e non come un'opinione, e il vocabolario dei metodi viene
dall'enumerazione `PIDType.cs` dello stesso repository, che li documenta uno per uno.

Da dove vengono i dati
----------------------
Da un clone di `https://github.com/kwsch/PKHeX`. Non è una dipendenza del repository e non
viene scaricato da questo strumento: il percorso si passa sulla riga di comando, con la
stessa disciplina con cui `extract_charmaps.py` riceve il percorso dei disassemblati. Un
clone parziale basta, e i due soli file che servono sono dichiarati in FILE_RICHIESTI.

Che cosa NON fa
---------------
Non giudica la legalità di alcun esemplare e non ricostruisce alcun metodo: riporta ciò
che la fonte dichiara. Le date degli eventi, dove la fonte non le porta, restano assenti
invece di essere indovinate, e il catalogo lo dichiara nella sua intestazione.

Uso
---
    python tools/catalogo-eventi-gen3.py --pkhex <percorso del clone>
    python tools/catalogo-eventi-gen3.py --pkhex <percorso> --check
"""

import argparse
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
USCITA = os.path.join(ROOT, "recreate-pokemon-distributions-events", "EVENTI-GEN3.md")

FILE_RICHIESTI = {
    "eventi": os.path.join("PKHeX.Core", "Legality", "Encounters", "Data", "Gen3",
                           "EncountersWC3.cs"),
    "metodi": os.path.join("PKHeX.Core", "Legality", "RNG", "PIDType.cs"),
}

# I quattro insiemi in cui la fonte divide le voci, con la ragione della divisione resa in
# italiano. I nomi a sinistra sono quelli dei campi nel sorgente e non vanno tradotti,
# perché servono a ritrovare il punto.
INSIEMI = {
    "Common": "voci consultate più spesso, tenute separate dalla fonte per comodità",
    "Japan": "distribuzioni giapponesi",
    "International": "distribuzioni internazionali, divise per lingua dove la lingua cambia il nome dell'allenatore",
    "Eggs": "distribuzioni consegnate come uova, dove l'allenatore è il ricevente",
}

# Le derivazioni del sesso dell'allenatore di provenienza, come le documenta l'enumerazione
# GiftGender3 della fonte. Sono qui e non estratte perché sono dieci etichette stabili e
# perché la loro traduzione è il contributo di questo strumento, non un secondo registro.
SESSO = {
    "Recipient": "copiato dal ricevente",
    "Only0": "sempre 0",
    "Only1": "sempre 1",
    "RandAlgo": "algoritmo proprio, che la fonte dichiara di non verificare con la logica ordinaria",
    "RandD3": "divisione per 3",
    "RandS3": "scorrimento di 3",
    "RandS7": "scorrimento di 7",
    "RandSG15": "scorrimento di 15, dopo l'oggetto",
    "RandD3_0": "divisione per 3, obbligata a 0, evento a due allenatori",
    "RandD3_1": "divisione per 3, obbligata a 1, evento a due allenatori",
}

VOCE = re.compile(r"^\s*new\((?P<testa>[^)]*)\)(?P<coda>.*?)$")
CAMPO = re.compile(r"(\w+)\s*=\s*(\"[^\"]*\"|\(int\)\w+|[\w\.]+)")


def leggi(percorso_pkhex, chiave):
    rel = FILE_RICHIESTI[chiave]
    p = os.path.join(percorso_pkhex, rel)
    if not os.path.exists(p):
        sys.exit("manca " + rel + " sotto " + percorso_pkhex +
                 "\nil clone deve contenere almeno quel percorso; con un clone sparso "
                 "aggiungerlo con git sparse-checkout")
    with open(p, "rb") as f:
        return f.read().decode("utf-8")


def metodi_documentati(testo):
    """Le voci dell'enumerazione dei metodi, ciascuna con la sua descrizione.

    La descrizione sta nel commento di documentazione che precede la voce, e la fonte lo
    scrive in due forme: tutto su una riga, oppure su più righe fra le due marche di
    apertura e chiusura. Leggere soltanto la prima forma perde le voci scritte nella
    seconda, ed è accaduto: il metodo del Jirachi della console domestica risultava non
    documentato mentre la fonte lo documenta, e con esso si perdeva il rimando al
    generatore impiegato.

    Si conserva l'inglese, perché è la dichiarazione della fonte e tradurla la renderebbe
    una parafrasi non citabile, e si tiene anche il generatore nominato dalle note, quando
    c'è, perché distingue il generatore della console portatile da quello della domestica.
    """
    fuori = {}
    doc, dentro_sommario, generatore = None, False, None
    for riga in testo.split("\n"):
        s = riga.strip()
        if s.startswith("///"):
            c = s[3:].strip()
            m = re.match(r"^<summary>\s*(.*?)\s*</summary>$", c)
            if m:
                doc = m.group(1)
                continue
            if c == "<summary>":
                dentro_sommario, doc = True, ""
                continue
            if c == "</summary>":
                dentro_sommario = False
                continue
            if dentro_sommario:
                doc = ((doc + " ") if doc else "") + c
                continue
            m = re.search(r"<remarks><see cref=\"(\w+)\"\s*/></remarks>", c)
            if m:
                generatore = m.group(1)
            continue
        if s.startswith("#region") or s.startswith("#endregion"):
            continue
        m = re.match(r"^([A-Za-z_][A-Za-z_0-9]*)\s*,\s*(?://.*)?$", s)
        if m:
            testo_doc = doc
            if testo_doc and generatore:
                if not testo_doc.endswith("."):
                    testo_doc += "."
                testo_doc += " Generatore: " + generatore + "."
            fuori[m.group(1)] = testo_doc
            doc, generatore = None, None
            continue
        if s and not s.startswith("//"):
            doc, generatore = None, None
    return fuori


def voci(testo):
    """Le voci della tabella, ciascuna con l'insieme e il blocco che la contengono."""
    righe = testo.split("\n")
    insieme, blocco, risultato = None, None, []
    for riga in righe:
        s = riga.strip()
        m = re.match(r"private static readonly EncounterGift3\[\]\s+(\w+)\s*=", s)
        if m:
            insieme, blocco = m.group(1), None
            continue
        if s == "];":
            insieme = None
            continue
        if insieme is None:
            continue
        if s.startswith("//"):
            testo_commento = s[2:].strip()
            # Un commento di blocco nomina un evento; le note lunghe della fonte non sono
            # intestazioni e si riconoscono dal fatto che finiscono con un punto.
            if testo_commento and not testo_commento.endswith("."):
                blocco = testo_commento
            continue
        if not s.startswith("new("):
            continue
        m = VOCE.match(s)
        if not m:
            continue
        testa = [p.strip() for p in m.group("testa").split(",")]
        coda = m.group("coda")
        commento = None
        i = coda.rfind("//")
        if i >= 0:
            commento = coda[i + 2:].strip()
            coda = coda[:i]
        campi = {}
        for k, v in CAMPO.findall(coda):
            v = v.strip()
            if v.startswith("\""):
                v = v[1:-1]
            elif v.startswith("(int)"):
                v = v[5:]
            campi[k] = v
        risultato.append({
            "insieme": insieme,
            "blocco": blocco,
            "specie_num": testa[0] if testa else "",
            "livello": testa[1] if len(testa) > 1 else "",
            "versione": testa[2] if len(testa) > 2 else "",
            "campi": campi,
            "commento": commento,
        })
    return risultato


def etichetta_specie(v):
    """Il nome della specie viene dal commento di riga della fonte, quando c'è.

    Non si inventa una tabella di nomi: se il commento manca resta il numero interno, che
    è comunque il dato con cui si cerca. I commenti che descrivono l'evento invece della
    specie si riconoscono perché contengono uno spazio seguito da una parentesi o perché
    nominano l'evento, e in quel caso vengono riportati per intero.
    """
    c = v["commento"]
    if not c:
        return "specie " + v["specie_num"]
    return c


def righe_tabella(v, metodi):
    campi = v["campi"]
    ident = campi.get("ID32") or campi.get("TID16") or ""
    sesso = campi.get("OriginalTrainerGender", "")
    marche = []
    if campi.get("FatefulEncounter") == "true":
        marche.append("incontro fatidico")
    if campi.get("RibbonNational") == "true":
        marche.append("nastro nazionale")
    if campi.get("EggLocation"):
        marche.append("uovo")
    return {
        "specie": etichetta_specie(v),
        "livello": v["livello"],
        "ot": campi.get("OriginalTrainerName", ""),
        "lingua": campi.get("Language", ""),
        "ident": ident,
        "metodo": campi.get("Method", ""),
        "lucentezza": campi.get("Shiny", ""),
        "sesso": sesso,
        "marche": ", ".join(marche),
    }


def genera(percorso_pkhex):
    testo_eventi = leggi(percorso_pkhex, "eventi")
    testo_metodi = leggi(percorso_pkhex, "metodi")
    doc_metodi = metodi_documentati(testo_metodi)
    elenco = voci(testo_eventi)
    if not elenco:
        sys.exit("nessuna voce riconosciuta: la forma della tabella a monte è cambiata")

    usati = {}
    for v in elenco:
        m = v["campi"].get("Method")
        if m:
            usati[m] = usati.get(m, 0) + 1

    out = []
    out.append("# Catalogo delle distribuzioni di evento di generazione 3")
    out.append("")
    out.append("Questo file è generato da `tools/catalogo-eventi-gen3.py` e non si modifica a mano: si rigenera. La fonte è la tabella `PKHeX.Core/Legality/Encounters/Data/Gen3/EncountersWC3.cs` di `PKHeX`, con il vocabolario dei metodi preso da `PKHeX.Core/Legality/RNG/PIDType.cs` dello stesso repository. Il comando è `python tools/catalogo-eventi-gen3.py --pkhex <percorso del clone>`, e il clone non è una dipendenza di questo repository: si passa sulla riga di comando, come per i disassemblati.")
    out.append("")
    out.append("Il catalogo serve a una domanda operativa del sottoprogetto: quali eventi sono esistiti e con quale metodo di generazione, perché è il metodo e non il campo visibile a distinguere una ricreazione fedele da un dato costruito a mano. Chi ha bisogno del ragionamento, e non dell'elenco, legga `STUDIO-02-metodi-di-generazione.md`.")
    out.append("")
    out.append("Due avvertenze sul contenuto. La prima è che le date degli eventi non compaiono, perché la fonte le porta soltanto in alcuni commenti di blocco e indovinare le altre sarebbe peggio che ometterle: dove il blocco le dichiara, il titolo del blocco le riporta. La seconda è che il nome della specie viene dal commento di riga della fonte, e dove il commento manca resta il numero interno, che è comunque il dato con cui si cerca.")
    out.append("")
    out.append("## Che cosa contiene, in numeri")
    out.append("")
    out.append("Le voci sono " + str(len(elenco)) + ", divise nei quattro insiemi in cui la fonte le tiene separate.")
    out.append("")
    out.append("| Insieme | Voci | Perché è separato |")
    out.append("|---|---|---|")
    for nome, motivo in INSIEMI.items():
        n = sum(1 for v in elenco if v["insieme"] == nome)
        if n:
            out.append("| `" + nome + "` | " + str(n) + " | " + motivo + " |")
    out.append("")
    out.append("## I metodi di generazione, e quanto pesano")
    out.append("")
    out.append("La colonna della descrizione riporta la dichiarazione della fonte in inglese e non una sua traduzione, perché è la definizione del metodo e una parafrasi non sarebbe citabile. La sigla BACD nomina l'ordine con cui le quattro estrazioni del generatore compongono il valore di personalità e i valori individuali, ed è invertito rispetto a quello degli incontri ordinari: è questa inversione, e non un algoritmo diverso, la firma di un esemplare da evento.")
    out.append("")
    out.append("| Metodo | Voci | Che cosa dichiara la fonte |")
    out.append("|---|---|---|")
    for m, n in sorted(usati.items(), key=lambda kv: (-kv[1], kv[0])):
        out.append("| `" + m + "` | " + str(n) + " | " + (doc_metodi.get(m) or "non documentato nell'enumerazione") + " |")
    out.append("")
    non_usati = [m for m in doc_metodi if m.startswith("BACD") and m not in usati]
    if non_usati:
        out.append("Restano nell'enumerazione, e nessuna voce li usa, i metodi " + ", ".join("`" + m + "`" for m in sorted(non_usati)) + ". Il fatto va registrato perché è un risultato negativo e non una lacuna: la fonte dichiara accanto a due di essi che nessun evento li ha mai generati, e conservarli documenta lo spazio delle possibilità invece dei soli casi occorsi.")
        out.append("")
    out.append("## Le derivazioni del sesso dell'allenatore di provenienza")
    out.append("")
    out.append("La fonte le tiene in un'enumerazione propria e dichiara che, quando è casuale, il sesso è determinato dopo il valore di personalità e i valori individuali, e in un caso dopo l'oggetto tenuto. Sono la parte del formato che una ricreazione sbaglia più facilmente, perché non è visibile in gioco.")
    out.append("")
    out.append("| Sigla | Che cosa fa | Voci |")
    out.append("|---|---|---|")
    conta_sesso = {}
    for v in elenco:
        s = v["campi"].get("OriginalTrainerGender")
        if s:
            conta_sesso[s] = conta_sesso.get(s, 0) + 1
    for s, descr in SESSO.items():
        if s in conta_sesso:
            out.append("| `" + s + "` | " + descr + " | " + str(conta_sesso[s]) + " |")
    out.append("")
    out.append("## Le voci, per insieme e per blocco")
    out.append("")
    for nome in INSIEMI:
        del_insieme = [v for v in elenco if v["insieme"] == nome]
        if not del_insieme:
            continue
        out.append("### Insieme `" + nome + "`")
        out.append("")
        blocco_corrente = object()
        for v in del_insieme:
            if v["blocco"] != blocco_corrente:
                blocco_corrente = v["blocco"]
                out.append("")
                out.append("Blocco: " + (blocco_corrente or "senza intestazione nella fonte"))
                out.append("")
                out.append("| Specie | Liv. | Allenatore | Lingua | Identificativo | Metodo | Lucentezza | Sesso OT | Marche |")
                out.append("|---|---|---|---|---|---|---|---|---|")
            r = righe_tabella(v, doc_metodi)
            out.append("| " + " | ".join([
                r["specie"], r["livello"], "`" + r["ot"] + "`" if r["ot"] else "",
                r["lingua"], r["ident"],
                "`" + r["metodo"] + "`" if r["metodo"] else "",
                r["lucentezza"], "`" + r["sesso"] + "`" if r["sesso"] else "",
                r["marche"],
            ]) + " |")
        out.append("")
    return "\n".join(out).rstrip("\n") + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--pkhex", required=True, help="percorso di un clone di kwsch/PKHeX")
    ap.add_argument("--check", action="store_true",
                    help="verifica senza scrivere, esce con 1 se il file andrebbe cambiato")
    a = ap.parse_args()

    nuovo = genera(a.pkhex)
    vecchio = None
    if os.path.exists(USCITA):
        with open(USCITA, "rb") as f:
            vecchio = f.read().decode("utf-8")

    if a.check:
        if nuovo != vecchio:
            print("il catalogo andrebbe rigenerato")
            return 1
        print("catalogo allineato alla fonte")
        return 0

    os.makedirs(os.path.dirname(USCITA), exist_ok=True)
    with open(USCITA, "wb") as f:
        f.write(nuovo.encode("utf-8"))
    righe = nuovo.count("\n")
    print("scritto " + os.path.relpath(USCITA, ROOT) + ", " + str(righe) + " righe")
    return 0


if __name__ == "__main__":
    sys.exit(main())
