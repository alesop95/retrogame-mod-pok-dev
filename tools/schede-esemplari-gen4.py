#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Scrive le schede di pedigree degli esemplari da evento di quarta generazione.

Perche' esiste, e perche' non legge i file prodotti
---------------------------------------------------
Un giudizio di conformita' riguarda una configurazione precisa di byte e non una categoria: vale
per quel valore di personalita', quei valori individuali, quel nome e quella data. Registrare
soltanto che una voce e' conforme perde l'informazione che serve, cioe' che cosa esattamente sia
stato dichiarato conforme, e senza quella non si puo' ne' riprodurre il caso ne' riconoscere che una
modifica successiva lo ha cambiato.

Come il documento fratello della terza generazione, questo ricalcola i campi dalle sorgenti con il
medesimo codice che scrive i file, invece di rileggerli dal disco. Ne segue che il documento e'
anche una verifica del determinismo della produzione: se due corse dessero schede diverse, la
scelta dei semi non sarebbe riproducibile, e il difetto si manifesterebbe come una modifica del
documento senza che nulla sia stato modificato a mano. L'unica riga che venga dal disco e'
l'impronta del file, presa dal manifesto che il generatore scrive accanto al lotto: nessun
ricalcolo puo' dimostrare che un file esista.

La provenienza di un gruppo, e che cosa qui si sa senza fonti esterne
---------------------------------------------------------------------
Per la quarta generazione il progetto non ha ancora un registro di provenienza scritto a mano come
quello di terza. Tre cose pero' si leggono dal dato stesso e sono fatti e non congetture, quindi
entrano nella scheda come tali: il nome dell'allenatore, che per una distribuzione ufficiale e'
l'insegna dell'evento; la lingua della carta, che dice in quale regione la consegna avvenne; e il
luogo di incontro, che distingue le tre vie della quarta generazione, cioe' l'evento in negozio,
il dono senza fili e la consegna che veniva dai giochi della serie Ranger.

Dove un registro di provenienza esiste, la sua riga sostituisce il racconto derivato. Dove non
esiste, la scheda dichiara che il gruppo non e' documentato invece di riempirlo per ipotesi, che e'
la regola di onesta' del contenuto di questo progetto.

Uso
---
    python tools/schede-esemplari-gen4.py --pkhex _notes/fonti/pkhex
    python tools/schede-esemplari-gen4.py --pkhex <clone> --check
    python tools/schede-esemplari-gen4.py --self-test
"""

import argparse
import io
import json
import os
import struct
import sys

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RADICE, "tools"))

def carica_generatore():
    """Carica il generatore, il cui nome di file porta trattini e non e' quindi importabile."""
    import importlib.util
    percorso = os.path.join(RADICE, "tools", "genera-evento-gen4.py")
    spec = importlib.util.spec_from_file_location("genera_evento_gen4", percorso)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


USCITA = os.path.join(RADICE, "recreate-pokemon-distributions-events",
                      "SCHEDE-ESEMPLARI-GEN4.md")
GIUDIZI = os.path.join(RADICE, "recreate-pokemon-distributions-events", "giudizi-esterni.json")
PROVENIENZE = os.path.join(RADICE, "recreate-pokemon-distributions-events",
                           "provenienze-eventi-gen4.json")
MANIFESTO = os.path.join(RADICE, "_notes", "lotto-gen4", "impronte.json")
TESTI = os.path.join("PKHeX.Core", "Resources", "text", "other", "it")
CONVERTITORE = os.path.join("PKHeX.Core", "PKM", "Strings", "StringConverter4Util.cs")

TERMINATORE = 0xFFFF

# Le costanti nominate che compaiono dentro la tabella dei caratteri della fonte, con il valore
# che la fonte stessa dichiara loro. Vanno riconosciute per nome e non ignorate: ciascuna occupa
# una posizione, e saltarne una sposta di uno tutte le posizioni seguenti. Il difetto e' insidioso
# perche' non produce caratteri illeggibili ma nomi plausibili e sbagliati, per esempio Pcmjwjb al
# posto di Oblivia, che a una lettura distratta sembrano stranezze di una carta straniera.
COSTANTI = {"NUL": chr(0), "EMP": chr(0), "HGM": chr(0x246D), "HGF": chr(0x246E)}

# La lunghezza attesa della tabella, che e' l'ancoraggio esterno di questo lettore: la fonte
# numera le proprie righe in commento, e l'ultima dichiara di fermarsi a 0x1EC, quindi la
# lunghezza vale 0x1ED. Un conteggio diverso dice che la lettura ha saltato o duplicato
# qualcosa, e va fermata invece che usata: e' ADR-036 applicato a un lettore di tabella.
LUNGHEZZA_TABELLA = 0x1ED

# Il secondo blocco, quello coreano, comincia al valore 0x400 e la fonte dichiara di fermarsi a
# 0xD65, quindi porta 0xD66 meno 0x400 voci.
INIZIO_COREANO = 0x400
LUNGHEZZA_COREANA = 0xD66 - 0x400

# I luoghi di incontro che la quarta generazione riserva alle consegne, cioe' i soli che il nostro
# lotto puo' produrre. Il nome sta qui e non in una tabella della fonte perche' il clone di questo
# progetto non porta il file dei nomi dei luoghi: sono stati letti dal rapporto del verificatore
# sul salvataggio di Argento SoulSilver, che li mostra in italiano accanto ai medesimi valori.
LUOGHI = {
    3000: ("luogo non nominato", "il modello non dichiara alcun luogo, quindi la consegna scrive "
           "il primo valore della tabella degli eventi"),
    3001: ("Pokémon Ranger", "la consegna proveniva da un gioco della serie Ranger, che sbloccava "
           "la missione e poi consegnava l'esemplare al gioco principale"),
    3060: ("Evento Pokémon", "la consegna avveniva di persona, all'apparecchio di un negozio o di "
           "una manifestazione"),
    3073: ("Dono Wi-Fi", "la consegna avveniva sulla rete, dal servizio senza fili della console"),
}

NATURE_DA_INDICE = None  # riempita dai testi


def leggi_testi(pkhex, nome):
    percorso = os.path.join(pkhex, TESTI, nome)
    if not os.path.exists(percorso):
        return None
    return io.open(percorso, encoding="utf-8").read().splitlines()


def _voci_tabella(testo, nome, attesa):
    """La tabella dei caratteri di quarta generazione, letta dal sorgente della fonte.

    Si legge invece di trascriverla perche' una trascrizione di quattrocentonovanta glifi e' un
    difetto che aspetta: il progetto ha gia' pagato una volta il prezzo di una tabella copiata a
    mano, quando l'elenco dei doni del disco bonus risulto' incompleto.
    """
    # Si parte dalla parentesi e non dal nome, perche' il nome stesso comincia con una
    # maiuscola e verrebbe letto come una costante nominata.
    inizio = testo.index("[", testo.index(nome + " =>"))
    fine = testo.index("];", inizio)
    blob = testo[inizio:fine]
    fughe = {"n": "\n", "t": "\t", "0": "\x00", "\\": "\\", "'": "'", '"': '"'}
    tabella, k, quanti = [], 0, len(blob)
    while k < quanti:
        if blob[k] == "/" and blob[k + 1] == "/":
            k = blob.index("\n", k)
            continue
        if blob[k] == "'":
            k += 1
            if blob[k] == "\\":
                if blob[k + 1] == "u":
                    tabella.append(chr(int(blob[k + 2:k + 6], 16)))
                    k += 6
                else:
                    tabella.append(fughe.get(blob[k + 1], blob[k + 1]))
                    k += 2
            else:
                tabella.append(blob[k])
                k += 1
            k += 1  # l'apice di chiusura
            continue
        if blob[k].isupper():
            fine = k
            while fine < quanti and (blob[fine].isupper() or blob[fine].isdigit()):
                fine += 1
            nome = blob[k:fine]
            if nome not in COSTANTI:
                # Un identificatore che la tabella delle costanti non conosce e' un difetto e non
                # un carattere: fermarsi e' preferibile a scrivere una tabella disallineata,
                # perche' uno scostamento di una sola posizione produce nomi leggibili e sbagliati.
                raise ValueError("costante non riconosciuta nella tabella dei caratteri: " + nome)
            tabella.append(COSTANTI[nome])
            k = fine
            continue
        k += 1
    if len(tabella) != attesa:
        raise ValueError("la tabella %s ha %d voci invece di %d: la lettura del sorgente della "
                         "fonte non e' allineata" % (nome, len(tabella), attesa))
    return tabella


def tabella_caratteri(pkhex):
    """Le due tabelle dei caratteri di quarta generazione, come una funzione da valore a glifo.

    La fonte ne tiene due, perche' i valori coreani non stanno nell'intervallo internazionale ma in
    un secondo blocco che comincia a 0x400. Servono entrambe: ventisei voci del lotto sono coreane,
    e con la sola tabella internazionale il loro allenatore si leggerebbe come una fila di punti
    interrogativi, cioe' come un dato mancante invece che come un dato in un altro alfabeto.
    """
    percorso = os.path.join(pkhex, CONVERTITORE)
    if not os.path.exists(percorso):
        return None
    testo = io.open(percorso, encoding="utf-8").read()
    internazionale = _voci_tabella(testo, "TableINT", LUNGHEZZA_TABELLA)
    coreana = _voci_tabella(testo, "TableKOR", LUNGHEZZA_COREANA)

    def glifo(valore):
        if valore < len(internazionale):
            return internazionale[valore]
        indice = valore - INIZIO_COREANO
        if 0 <= indice < len(coreana):
            return coreana[indice]
        return "?"

    return glifo


def stringa(pk4, offset, quanti, tabella):
    fuori = []
    for k in range(quanti):
        valore = struct.unpack_from("<H", pk4, offset + 2 * k)[0]
        if valore == TERMINATORE:
            break
        fuori.append(tabella(valore))
    return "".join(fuori)


def carica_json(percorso, difetto):
    if not os.path.exists(percorso):
        return difetto
    return json.load(io.open(percorso, encoding="utf-8"))


def stato_giudizio(giudizi, indice):
    """Lo stato del giudizio esterno di una voce, filtrato sul lotto di quarta generazione.

    Il filtro sul lotto non e' una precauzione teorica: un giudizio di massa espresso sul lotto di
    prima e seconda generazione era stato applicato per errore alle schede di terza, e la
    correzione fu introdurre il campo che dice a quale lotto un giudizio si riferisca.
    """
    for g in giudizi:
        if g.get("lotto") != "gen4":
            continue
        if g.get("tutte"):
            return g
        if indice in g.get("voci", []):
            return g
    return None


def gruppo_di(voce, provenienze):
    """La riga di provenienza di una voce: dal registro se c'e', altrimenti derivata dal dato."""
    chiave = voce["allenatore"]
    if chiave in provenienze:
        p = provenienze[chiave]
        return p["titolo"], p["racconto"], "registro di provenienza"
    nome_luogo, come = LUOGHI.get(voce["luogo"], ("luogo %d" % voce["luogo"],
                                                  "via di consegna non riconosciuta"))
    racconto = ("Gruppo non ancora documentato da una fonte esterna. Ciò che segue si legge dal "
                "dato e non da una fonte: l'insegna della distribuzione è `%s`, la carta è in "
                "lingua %s, e il luogo di incontro dice che %s."
                % (voce["allenatore"] or "(nessuna)", voce["lingua_nome"], come))
    return "Insegna %s, %s" % (voce["allenatore"] or "senza nome", nome_luogo), racconto, "derivata"


LINGUE = {1: "giapponese", 2: "inglese", 3: "francese", 4: "italiano", 5: "tedesco",
          7: "spagnolo", 8: "coreano"}

VERSIONI = {7: "Oro HeartGold", 8: "Argento SoulSilver", 10: "Diamante", 11: "Perla",
            12: "Platino"}

PALLE = {1: "Master Ball", 2: "Ultra Ball", 3: "Super Ball", 4: "Poké Ball", 16: "Pregio Ball"}


def raccogli(pkhex, gen):
    """Ricalcola le voci con il medesimo codice che scrive i file, e le arricchisce per la scheda."""
    esito, errore = gen.leggi_doni(pkhex)
    if errore:
        return None, errore
    tabella = tabella_caratteri(pkhex)
    if tabella is None:
        return None, "manca il sorgente del convertitore di stringhe sotto " + CONVERTITORE
    specie_nomi = leggi_testi(pkhex, "text_Species_it.txt")
    mosse_nomi = leggi_testi(pkhex, "text_Moves_it.txt")
    nature_nomi = leggi_testi(pkhex, "text_Natures_it.txt")
    if not (specie_nomi and mosse_nomi and nature_nomi):
        return None, "mancano i testi italiani sotto " + TESTI
    allenatore = gen.allenatore_del_progetto()
    fuori = []
    for v in esito["voci"]:
        pk4, resoconto = gen.consegna(v, allenatore)
        if pk4 is None:
            continue
        pid = struct.unpack_from("<I", pk4, gen.OFF_PID)[0]
        iv32 = struct.unpack_from("<I", pk4, gen.OFF_IV32)[0]
        tid = struct.unpack_from("<H", pk4, gen.OFF_TID)[0]
        sid = struct.unpack_from("<H", pk4, gen.OFF_SID)[0]
        mosse = [struct.unpack_from("<H", pk4, 0x28 + 2 * k)[0] for k in range(4)]
        fuori.append({
            "indice": v["indice"],
            "specie": v["specie"],
            "specie_nome": specie_nomi[v["specie"]] if v["specie"] < len(specie_nomi) else "?",
            "soprannome": stringa(pk4, 0x48, 11, tabella),
            "allenatore": stringa(pk4, gen.OFF_OT_NOME, 8, tabella),
            "tid": tid, "sid": sid,
            "pid": pid,
            "pid_origine": resoconto["pid"],
            "iv_origine": resoconto["iv"],
            "natura": nature_nomi[pid % 25] if pid % 25 < len(nature_nomi) else "?",
            "bit_abilita": pid & 1,
            "abilita": pk4[gen.OFF_ABILITA],
            "cromatico": gen.e_cromatico(pid, tid, sid),
            "iv": [(iv32 >> (5 * k)) & 31 for k in range(6)],
            "lingua": pk4[gen.OFF_LINGUA],
            "lingua_nome": LINGUE.get(pk4[gen.OFF_LINGUA], "codice %d" % pk4[gen.OFF_LINGUA]),
            "versione": v["versione"],
            "versione_nome": VERSIONI.get(v["versione"], "codice %d" % v["versione"]),
            "livello": pk4[gen.OFF_LIVELLO_INCONTRO] & 0x7F,
            "esperienza": struct.unpack_from("<I", pk4, gen.OFF_ESPERIENZA)[0],
            "mosse": [m for m in mosse if m],
            "mosse_nomi": [mosse_nomi[m] if m < len(mosse_nomi) else "?" for m in mosse if m],
            "oggetto": struct.unpack_from("<H", pk4, 0x0A)[0],
            "palla": v["palla"],
            "palla_nome": PALLE.get(v["palla"], "codice %d" % v["palla"]),
            "fatidico": bool(pk4[gen.OFF_FLAG_GENERE] & 1),
            "genere": (pk4[gen.OFF_FLAG_GENERE] >> 1) & 3,
            "luogo": struct.unpack_from("<H", pk4, gen.OFF_INCONTRO_DP)[0],
            "luogo_esteso": struct.unpack_from("<H", pk4, gen.OFF_INCONTRO_ESTESO)[0],
            "data": (2000 + pk4[gen.OFF_INCONTRO_ANNO], pk4[gen.OFF_INCONTRO_ANNO + 1],
                     pk4[gen.OFF_INCONTRO_ANNO + 2]),
            "cordialita": pk4[gen.OFF_CORDIALITA],
            "chiave_pid": "EVT-4|%d|%08X|%d|%d|pid" % (v["indice"], v["pid"], tid, sid),
            "chiave_iv": "EVT-4|%d|%08X|%d|%d|iv" % (v["indice"], v["pid"], tid, sid),
            "nome_file": "EVT-4-%04d-%03d%s.pk4"
                         % (v["indice"], v["specie"],
                            "-nostro" if resoconto["allenatore"] == "del progetto" else ""),
        })
    return fuori, None


def barrato(testo):
    """Protegge le barre verticali, che in una tabella separerebbero le celle."""
    return testo.replace("|", chr(92) + "|")


GENERI = {0: "maschio", 1: "femmina", 2: "asessuato"}
STATISTICHE = ["PS", "Att", "Dif", "Vel", "Asp", "Dsp"]


def scheda(v, provenienze, giudizi, impronte):
    titolo_gruppo, racconto, origine = gruppo_di(v, provenienze)
    g = stato_giudizio(giudizi, v["indice"])
    marca = ""
    if g:
        marca = "  (giudizio: %s, %s)" % (g.get("esito", "?"), g.get("data", "?"))
    r = []
    r.append("### %03d %s  `%s`%s" % (v["indice"], v["specie_nome"], v["allenatore"] or "-", marca))
    r.append("")
    r.append("**%s.** %s" % (titolo_gruppo, racconto))
    r.append("")
    r.append("| Campo | Valore | Da dove viene |")
    r.append("|---|---|---|")
    r.append("| posizione nella base dei doni | %d | l'indice del record nella base dei doni "
             "segreti della fonte, che è anche la chiave del seme |" % v["indice"])
    r.append("| valore di personalità | `0x%08X` | %s |"
             % (v["pid"], "dichiarato dal modello del dono, cioè il valore realmente distribuito"
                if v["pid_origine"] == "dal modello" else
                "composto da noi, perché il modello portava il segnale `0x00000001` invece di un "
                "valore, cioè l'ordine di generarne uno non cromatico"))
    r.append("| natura | %s | resto per venticinque del valore di personalità |" % v["natura"])
    r.append("| bit dell'abilità, abilità dichiarata | %d, numero %d | bit meno significativo del "
             "valore di personalità, e numero di abilità che il modello scrive |"
             % (v["bit_abilita"], v["abilita"]))
    r.append("| cromatico | %s | somma esclusiva delle quattro parole sotto otto |"
             % ("sì" if v["cromatico"] else "no"))
    r.append("| valori individuali | %s | %s |"
             % (" / ".join("%d %s" % (n, s) for n, s in zip(v["iv"], STATISTICHE)),
                "dichiarati dal modello" if v["iv_origine"] == "dal modello" else
                "composti da noi, perché il modello li portava tutti a zero: la console di chi "
                "riceveva li tirava al momento della consegna"))
    r.append("| allenatore | `%s` | dichiarato dal modello |" % (v["allenatore"] or "-"))
    r.append("| identificativo, segreto | %d, %d | dichiarati dal modello |" % (v["tid"], v["sid"]))
    r.append("| sesso | %s | dichiarato dal modello, e vincolo sulla composizione del valore |"
             % GENERI.get(v["genere"], "?"))
    r.append("| lingua | %s | dichiarata dal modello |" % v["lingua_nome"])
    r.append("| specie interna, soprannome | %d, `%s` | numero nazionale, nome nella lingua della "
             "voce |" % (v["specie"], v["soprannome"]))
    r.append("| livello, esperienza | %d, %d | dichiarati dal modello |"
             % (v["livello"], v["esperienza"]))
    r.append("| mosse | %s | dichiarate dal modello |"
             % (", ".join(v["mosse_nomi"]) if v["mosse_nomi"] else "nessuna"))
    r.append("| oggetto tenuto | %s | dichiarato dal modello |"
             % (str(v["oggetto"]) if v["oggetto"] else "nessuno"))
    r.append("| palla | %s | dichiarata dal modello |" % v["palla_nome"])
    r.append("| incontro fatidico | %s | dichiarato dal modello |"
             % ("sì" if v["fatidico"] else "no"))
    r.append("| versione di origine | %s | dichiarata dal modello |" % v["versione_nome"])
    nome_luogo = LUOGHI.get(v["luogo"], ("luogo %d" % v["luogo"], ""))[0]
    r.append("| luogo di incontro | %d, %s | il luogo che il modello tiene nel campo dell'uovo, "
             "spostato dalla consegna nel campo dell'incontro con l'aggiunta di tremila |"
             % (v["luogo"], nome_luogo))
    r.append("| campo esteso del luogo | %d | scritto perché il lotto è composto per essere "
             "riscosso su Argento SoulSilver; su Diamante e Perla resterebbe nullo |"
             % v["luogo_esteso"])
    r.append("| data di incontro | %04d-%02d-%02d | costante dichiarata nel generatore, non il "
             "giorno della corsa, perché il lotto deve essere riproducibile |" % v["data"])
    r.append("| cordialità | %d | valore base della specie, come fa la consegna |"
             % v["cordialita"])
    # La barra verticale separa i campi della chiave e separa anche le celle di una tabella, quindi
    # va protetta: senza la protezione ciascuna di queste due righe diventerebbe otto celle invece
    # di tre, e il resto della riga finirebbe fuori dalla griglia.
    r.append("| chiave del seme del valore di personalità | `%s` | l'impronta SHA-256 di questa "
             "stringa dà i primi quattro byte del seme |" % barrato(v["chiave_pid"]))
    r.append("| chiave del seme dei valori individuali | `%s` | sale diverso dal precedente, "
             "perché la coppia non deve esibire correlazione |" % barrato(v["chiave_iv"]))
    imp = impronte.get(v["nome_file"])
    if imp:
        r.append("| impronta del file prodotto | `%s` | SHA-256 della forma di scatola scritta in "
                 "`_notes/lotto-gen4/`, presa dal manifesto che il generatore scrive accanto al "
                 "lotto. Le schede ricalcolano i campi dalle sorgenti e non leggono i file, quindi "
                 "questa riga è la sola che venga dal disco: è la prova che il file esiste ed è "
                 "quell'esemplare, non una sua descrizione |" % imp["sha256"])
    else:
        r.append("| impronta del file prodotto | non disponibile | il manifesto delle impronte non "
                 "è stato trovato accanto al lotto, oppure questa voce non è stata prodotta "
                 "nell'ultima corsa: si rigenera con `--lotto` |")
    r.append("")
    return "\n".join(r)


def componi(pkhex):
    gen = carica_generatore()
    voci, errore = raccogli(pkhex, gen)
    if errore:
        return None, errore
    provenienze = carica_json(PROVENIENZE, {})
    registro = carica_json(GIUDIZI, {})
    giudizi = registro.get("giudizi", []) if isinstance(registro, dict) else registro
    manifesto = carica_json(MANIFESTO, {})
    impronte = manifesto.get("voci", {}) if isinstance(manifesto, dict) else {}
    giudicate = sum(1 for v in voci if stato_giudizio(giudizi, v["indice"]))
    composte = sum(1 for v in voci if v["pid_origine"] == "composto")
    r = []
    r.append("# Schede tecniche degli esemplari da evento di quarta generazione")
    r.append("")
    r.append("> Documento generato da `tools/schede-esemplari-gen4.py`. Non si modifica a mano, e "
             "non legge i file prodotti: ricalcola gli esemplari dalle sorgenti con il medesimo "
             "codice che li scrive.")
    r.append("")
    r.append("Un giudizio di conformità riguarda una configurazione precisa di byte e non una "
             "categoria: vale per quel valore di personalità, quei valori individuali, quel nome e "
             "quella data. Questo documento è dunque l'inventario delle caratteristiche univoche "
             "di ciascun esemplare, accanto allo stato del suo giudizio.")
    r.append("")
    r.append("La quarta generazione ha una particolarità che le prime tre non hanno, e va letta "
             "prima delle schede perché cambia il senso di due righe di ciascuna. Il dono di "
             "quarta generazione non contiene l'esemplare ma il suo modello: il valore di "
             "personalità è dichiarato su %d voci e assente sulle altre %d, dove il modello porta "
             "il segnale che ordina di generarne uno non cromatico, e i valori individuali sono "
             "assenti su tutte e %d. Le righe che dicono composto da noi non denunciano quindi una "
             "licenza che ci siamo presi, ma il fatto che quei bit non esistevano prima della "
             "consegna e li tirava la console di chi riceveva."
             % (len(voci) - composte, composte, len(voci)))
    r.append("")
    r.append("Stato: %d voci prodotte, di cui %d giudicate da un verificatore indipendente al "
             "momento dell'ultima generazione di questo documento. Le voci giudicate portano la "
             "dicitura accanto al titolo." % (len(voci), giudicate))
    r.append("")
    for v in voci:
        r.append(scheda(v, provenienze, giudizi, impronte))
    return "\n".join(r) + "\n", None


def self_test():
    falliti = 0

    def prova(nome, atteso, ottenuto):
        nonlocal falliti
        if atteso != ottenuto:
            falliti += 1
            print("  FALLITO %s: atteso %r, ottenuto %r" % (nome, atteso, ottenuto))

    prova("i quattro luoghi di consegna sono nominati", 4, len(LUOGHI))
    prova("le costanti nominate della tabella sono quattro", 4, len(COSTANTI))
    prova("la lunghezza attesa della tabella", 493, LUNGHEZZA_TABELLA)
    prova("la lunghezza attesa della tabella coreana", 0x966, LUNGHEZZA_COREANA)
    prova("le barre della chiave del seme sono protette", "a" + chr(92) + "|b", barrato("a|b"))
    prova("l'evento in negozio", "Evento Pokémon", LUOGHI[3060][0])
    prova("il dono senza fili", "Dono Wi-Fi", LUOGHI[3073][0])

    # Il filtro sul lotto: un giudizio di massa espresso su un altro lotto non deve toccare queste
    # schede, ed e' il difetto che il campo del lotto e' stato introdotto per impedire.
    giudizi = [{"lotto": "gb", "tutte": True, "esito": "conforme", "data": "2026-09-04"},
               {"lotto": "gen4", "voci": [7], "esito": "conforme", "data": "2026-09-05"}]
    prova("un giudizio di un altro lotto non tocca la voce", None, stato_giudizio(giudizi, 3))
    prova("un giudizio del lotto giusto la tocca", "2026-09-05",
          stato_giudizio(giudizi, 7)["data"])

    # La provenienza derivata dichiara di essere derivata, che e' la regola di onesta'.
    voce = {"allenatore": "TRU", "lingua_nome": "inglese", "luogo": 3060}
    titolo, racconto, origine = gruppo_di(voce, {})
    prova("una provenienza senza registro si dichiara derivata", "derivata", origine)
    prova("e dice che il gruppo non e' documentato", True,
          "non ancora documentato" in racconto)
    titolo, racconto, origine = gruppo_di(
        voce, {"TRU": {"titolo": "Manaphy di Toys R Us", "racconto": "Racconto."}})
    prova("una provenienza registrata prevale", "registro di provenienza", origine)
    prova("e ne porta il titolo", "Manaphy di Toys R Us", titolo)

    print("self-test: %d controlli falliti" % falliti)
    return 1 if falliti else 0


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--pkhex", help="clone del verificatore")
    ap.add_argument("--check", action="store_true",
                    help="non scrive: dice soltanto se il documento sul disco sia allineato")
    ap.add_argument("--self-test", action="store_true", dest="self_test")
    a = ap.parse_args(argv)
    if a.self_test:
        return self_test()
    if not a.pkhex:
        ap.error("serve --pkhex, oppure --self-test")
    testo, errore = componi(a.pkhex)
    if errore:
        print("rifiutato: " + errore)
        return 1
    if a.check:
        vecchio = io.open(USCITA, encoding="utf-8").read() if os.path.exists(USCITA) else ""
        if vecchio == testo:
            print("allineato: %s" % USCITA)
            return 0
        print("disallineato: %s va rigenerato" % USCITA)
        return 1
    io.open(USCITA, "w", encoding="utf-8", newline="\n").write(testo)
    print("scritto %s" % USCITA)
    return 0


if __name__ == "__main__":
    sys.exit(main())
