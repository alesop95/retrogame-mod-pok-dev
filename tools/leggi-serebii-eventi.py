#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Attraversa l'archivio delle distribuzioni di Serebii e ne ricava un censimento tracciato.

Perche' questa fonte, e perche' non basta la base dei doni del verificatore
--------------------------------------------------------------------------
La base dei doni che questo progetto usa da giorni conosce le carte, cioe' i file che una
distribuzione consegnava. Non conosce e non puo' conoscere gli eventi che una carta non l'hanno mai
lasciata: le consegne fatte da un apparecchio di negozio che scriveva direttamente nel salvataggio,
i biglietti che sbloccavano un incontro invece di consegnare un esemplare, le ricompense di un
gioco della serie derivata. Quelli esistono soltanto nella memoria di chi li ha documentati mentre
accadevano, ed e' esattamente cio' che questo archivio e': un registro tenuto dal 1999, anno per
anno, con una pagina per ciascuna delle milleventicinque specie.

Ne segue che le due fonti non si sovrappongono ma si completano, e che il confronto fra loro e' la
sola via per sapere quanto della nostra enumerazione sia enumerazione e quanto sia soltanto lo
specchio di un unico archivio. E' la stessa disciplina di ADR-036, cioe' che ogni lettura vuole un
ancoraggio che non venga da se stessa.

Come si attraversa, e con quale misura
--------------------------------------
La navigazione dell'archivio non sta dentro collegamenti ma dentro tendine di selezione, quindi i
suoi indirizzi si leggono dai valori delle opzioni e non dagli attributi di destinazione. E' il
motivo per cui una prima estrazione dei collegamenti aveva riferito zero pagine su una pagina che
ne indicizza millesettantasei.

Lo scaricamento e' deliberatamente lento e non parallelo, con una pausa fra una richiesta e la
successiva, e non riscarica cio' che ha gia'. Non e' scrupolo formale: e' un sito tenuto da una
persona, e mille richieste in pochi secondi sono un carico che non gli va imposto per una comodita'
nostra. Le pagine grezze restano sotto `_notes/`, che git ignora, perche' sono contenuto di terzi;
cio' che entra nel version control e' il censimento con l'attribuzione, non la copia, secondo la
regola gia' scritta nel registro delle fonti.

Che cosa porta una voce, e che cosa se ne sa con certezza
--------------------------------------------------------
Ogni distribuzione porta la palla, il livello, i contrassegni, l'allenatore con le sue traduzioni,
l'identificativo, l'abilita', l'oggetto tenuto, la natura, il testo della data di incontro, le
mosse, i fiocchi, la descrizione dell'evento, il metodo di consegna, il luogo, la finestra di date
e i giochi in cui la carta funziona.

Dei tre contrassegni che compaiono accanto al livello, uno e' certo e due sono dichiarati come
inferiti. La stella e' certa perche' e' stata provata per costruzione: la pagina dedicata alle
distribuzioni cromatiche porta duecentoventicinque voci e tutte e duecentoventicinque la portano.
Gli altri due, il pentagono e la croce, sono con ogni probabilita' i marchi di origine delle
generazioni sesta e settima, ma nessuna legenda dell'archivio lo dichiara e questo programma li
riferisce senza interpretarli.

Uso
---
    python tools/leggi-serebii-eventi.py --mappa
    python tools/leggi-serebii-eventi.py --scarica --limite 20
    python tools/leggi-serebii-eventi.py --scarica
    python tools/leggi-serebii-eventi.py --censimento
    python tools/leggi-serebii-eventi.py --self-test
"""

import argparse
import collections
import io
import json
import os
import re
import sys
import time
import urllib.request
from html import unescape

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = os.path.join(RADICE, "_notes", "fonti", "serebii")
MAPPA = os.path.join(CACHE, "mappa.json")
USCITA = os.path.join(RADICE, "pokedex-home-completo", "CENSIMENTO-SEREBII.md")
TABELLA = os.path.join(RADICE, "pokedex-home-completo", "serebii-eventi.csv")
SOLO_INDICE = os.path.join(RADICE, "pokedex-home-completo", "serebii-eventi-senza-specie.csv")

BASE = "https://www.serebii.net"
INDICE = "/events/"
# Uno user agent da browser e' necessario: senza, il servizio risponde con un guscio vuoto invece
# che con il contenuto. Non e' un aggiramento ma la condizione minima per ricevere la pagina che un
# lettore umano riceve, e la regola sulle fonti non recuperabili la indica come prima via.
AGENTE = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
          "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
PAUSA = 1.0

# I contrassegni che compaiono accanto al livello, come punti di codice decimali.
STELLA = "9733"      # cromatico, provato per costruzione sulla pagina dei cromatici
PENTAGONO = "11039"  # inferito: marchio di origine di sesta generazione, non dichiarato dalla fonte
CROCE = "10010"      # inferito: marchio di origine di settima generazione, non dichiarato
MASCHIO = "9794"
FEMMINA = "9792"

MAX_SPECIE = 1025


def indirizzi_dalla_mappa(html):
    """Gli indirizzi dell'archivio, letti dai valori delle opzioni delle tendine.

    Non dagli attributi di destinazione: l'archivio non ne ha, e cercarli la' e' l'errore che ha
    fatto riferire zero pagine su una pagina che ne indicizza piu' di mille.
    """
    fuori = []
    for valore, testo in re.findall(r'<option value="([^"]+)">([^<]*)</option>', html):
        if not valore.startswith("/"):
            continue
        fuori.append({"url": valore, "titolo": " ".join(testo.split())})
    return fuori


def scarica(url, destinazione, pausa=PAUSA):
    richiesta = urllib.request.Request(BASE + url, headers={"User-Agent": AGENTE})
    with urllib.request.urlopen(richiesta, timeout=30) as risposta:
        dati = risposta.read()
    io.open(destinazione, "wb").write(dati)
    time.sleep(pausa)
    return len(dati)


def nome_file(url):
    return url.strip("/").replace("/", "__") or "indice"


def pulisci(html):
    """Toglie i marcatori, scioglie le entita' e normalizza gli spazi.

    Sciogliere le entita' non e' cosmetico: gli allenatori giapponesi e coreani sono scritti
    interamente come entita' numeriche, e senza lo scioglimento il censimento porterebbe file di
    numeri al posto dei nomi, cioe' un dato illeggibile che sembra un difetto di codifica.
    """
    testo = re.sub(r"<br\s*/?>", " ", html)
    testo = re.sub(r"<[^>]+>", " ", testo)
    return " ".join(unescape(testo).split())


def entita(html):
    """I punti di codice delle entita' numeriche presenti, come stringhe decimali."""
    return set(re.findall(r"&#(\d+);", html))


def immagini(html):
    """I nomi delle immagini presenti, senza cartella ne' estensione.

    Servono perche' i contrassegni recenti non sono caratteri ma figure: il marchio di regione e il
    fattore Gigantamax compaiono come immagini accanto al livello.
    """
    return {os.path.splitext(os.path.basename(s))[0]
            for s in re.findall(r'<img[^>]+src="([^"]+)"', html)}


def celle_di_tabella(html, intestazione):
    """Le celle di una tabella interna che porti una data intestazione, per etichetta.

    L'archivio impagina le coppie di etichetta e valore come due righe successive, la prima con la
    classe delle intestazioni e la seconda con i valori, e la corrispondenza e' posizionale.
    """
    for blocco in re.findall(r"<table[^>]*>(.*?)</table>", html, re.S):
        if intestazione not in blocco:
            continue
        righe = re.findall(r"<tr[^>]*>(.*?)</tr>", blocco, re.S)
        for k, riga in enumerate(righe):
            if intestazione in riga and 'class="detailhead"' in riga:
                etichette = [pulisci(c) for c in re.findall(r"<td[^>]*>(.*?)</td>", riga, re.S)]
                if k + 1 < len(righe):
                    valori = [pulisci(c)
                              for c in re.findall(r"<td[^>]*>(.*?)</td>", righe[k + 1], re.S)]
                    return dict(zip(etichette, valori))
    return {}


def campo_multiplo(html, etichetta):
    """Le varianti di un campo etichettato, separate dall'archivio con una interruzione di riga.

    Il separatore e' l'informazione, e questa funzione esiste perche' la pulizia generale lo
    distrugge trasformandolo in uno spazio. La conseguenza era che un nome contenente uno spazio,
    per esempio quello del decennale, veniva contato come due nomi, e che le quattro lettere del
    Centro di New York non si distinguevano da esso in alcun modo.

    Che cosa una variante significhi non lo decide questa funzione, perche' non e' deducibile dal
    separatore: quattro lettere consecutive sono quattro allenatori distinti della medesima
    consegna, mentre un nome scritto in giapponese e poi in quattro lingue europee e' un allenatore
    solo tradotto. La distinzione richiede di guardare la regione della distribuzione, e resta al
    lettore del documento.
    """
    m = re.search(r'<td[^>]*class="detailhead"[^>]*>\s*%s\s*</td>\s*<td[^>]*>(.*?)</td>'
                  % re.escape(etichetta), html, re.S)
    if not m:
        return []
    pezzi = re.split(r"<br\s*/?>", m.group(1))
    return [x for x in (pulisci(p) for p in pezzi) if x]


def campo_etichettato(html, etichetta):
    """Il valore che segue una etichetta scritta nella cella di intestazione, sulla stessa riga."""
    m = re.search(r'<td[^>]*class="detailhead"[^>]*>\s*%s\s*</td>\s*<td[^>]*>(.*?)</td>'
                  % re.escape(etichetta), html, re.S)
    return pulisci(m.group(1)) if m else ""


def voci_della_pagina(html, sorgente):
    """Le distribuzioni di una pagina dell'archivio, una per record.

    Il contesto di anno e regione non sta dentro il record ma nei titoli che lo precedono, quindi
    si porta avanti scorrendo la pagina invece di cercarlo dentro il blocco.
    """
    pezzi = re.split(r'<table class="eventpoke">', html)
    anno, regione = "", ""
    fuori = []
    for testa in pezzi[:-1]:
        anni = re.findall(r"<u>\s*((?:19|20)\d\d)\s*</u>", testa)
        if anni:
            anno = anni[-1]
            regione = ""
        regioni = re.findall(r"<u>\s*([^<]{3,40})\s*</u>", testa)
        for r in regioni:
            if not re.fullmatch(r"(?:19|20)\d\d", r.strip()):
                regione = r.strip()
    for k, blocco in enumerate(pezzi[1:], 1):
        testa = pezzi[k - 1]
        anni = re.findall(r"<u>\s*((?:19|20)\d\d)\s*</u>", testa)
        if anni:
            anno = anni[-1]
            regione = ""
        for r in re.findall(r"<u>\s*([^<]{3,40})\s*</u>", testa):
            if not re.fullmatch(r"(?:19|20)\d\d", r.strip()):
                regione = r.strip()
        corpo = blocco.split("</table><br />")[0]

        palla = ""
        m = re.search(r"/itemdex/sprites/([a-z]+)\.png", corpo)
        if m:
            palla = m.group(1)
        nome, sesso = "", ""
        m = re.search(r'<td class="label">((?:(?!</td>).)*?)</td>', corpo, re.S)
        if m:
            cella = m.group(1)
            # Il nome sta fra lo sprite della palla e gli eventuali simboli di sesso, che sono
            # entita' numeriche dentro elementi di colore: si toglie il primo e si taglia ai
            # secondi, invece di pretendere che la cella finisca subito dopo il nome.
            senza_immagini = re.sub(r"<img[^>]*/?>", " ", cella)
            nome = pulisci(senza_immagini.split("<")[0])
            simboli = entita(cella)
            if MASCHIO in simboli and FEMMINA in simboli:
                sesso = "entrambi"
            elif MASCHIO in simboli:
                sesso = "maschio"
            elif FEMMINA in simboli:
                sesso = "femmina"
        livello, contrassegni = "", set()
        m = re.search(r'<td class="label">\s*Level\s*(\d*)((?:(?!</td>).)*)</td>', corpo, re.S)
        if m:
            # Il livello puo' mancare, e l'archivio in quel caso scrive due punti interrogativi.
            # Pretenderlo come cifra faceva perdere anche i contrassegni della medesima cella, e
            # una distribuzione cinese di un Arbok cromatico risultava cosi' non cromatica: uno
            # scarto di una voce sola fra il nostro conto e quello della pagina dedicata ai
            # cromatici, che e' quanto e' bastato a trovarlo.
            livello = m.group(1)
            # I contrassegni compaiono in due forme a seconda dell'epoca del record: come entita'
            # numeriche nelle voci antiche e come immagini in quelle recenti. Prenderne una sola
            # significherebbe dichiarare privi di contrassegno tutti i record di una delle due
            # epoche, che e' un difetto invisibile perche' produce un campo vuoto e non un errore.
            contrassegni = entita(m.group(2)) | immagini(m.group(2))

        descrizione = celle_di_tabella(corpo, "Description")
        date = celle_di_tabella(corpo, "Start Date")
        giochi = campo_etichettato(corpo, "Games Available")
        mosse = [pulisci(x) for x in re.findall(r'/attackdex[^"]*"[^>]*>([^<]+)</a>', corpo)]
        fiocchi = re.findall(r'title="([^"]*Ribbon[^"]*)"', corpo)
        natura = ""
        m = re.search(r'<td class="column">((?:(?!</td>).)*?Nature\.(?:(?!</td>).)*?)</td>',
                      corpo, re.S)
        if m:
            natura = pulisci(m.group(1))

        fuori.append({
            "sorgente": sorgente,
            "anno": anno,
            "regione": regione,
            "nome": nome,
            "palla": palla,
            "livello": livello,
            "sesso": sesso,
            "cromatico": "si" if STELLA in contrassegni else "no",
            "gigantamax": "si" if "dynamaxicon" in contrassegni else "no",
            "contrassegni": " ".join(sorted(contrassegni)),
            "allenatore": " / ".join(campo_multiplo(corpo, "OT:")),
            "allenatori": len(campo_multiplo(corpo, "OT:")),
            "identificativo": campo_etichettato(corpo, "ID:"),
            "abilita": campo_etichettato(corpo, "Ability:"),
            "natura_e_incontro": natura,
            "mosse": " / ".join(mosse[:4]),
            "fiocchi": " / ".join(sorted(set(fiocchi))),
            "descrizione": descrizione.get("Description", ""),
            "metodo": descrizione.get("Type", ""),
            "luogo": descrizione.get("Location", ""),
            "inizio": date.get("Start Date", ""),
            "fine": date.get("End Date", ""),
            "giochi": giochi,
        })
    return fuori


CAMPI = ["sorgente", "anno", "regione", "nome", "sesso", "palla", "livello", "cromatico",
         "gigantamax", "contrassegni",
         "allenatore", "allenatori", "identificativo", "abilita", "natura_e_incontro", "mosse", "fiocchi",
         "descrizione", "metodo", "luogo", "inizio", "fine", "giochi"]


def in_csv(voci):
    def cella(v):
        v = str(v if v is not None else "").replace(chr(10), " ")
        return '"%s"' % v.replace('"', '""') if ("," in v or '"' in v) else v
    righe = [",".join(CAMPI)]
    for v in voci:
        righe.append(",".join(cella(v.get(c, "")) for c in CAMPI))
    return "\n".join(righe) + "\n"


SENZA_CARTA = os.path.join(RADICE, "pokedex-home-completo", "EVENTI-SENZA-CARTA.md")

# I metodi di consegna che non producono alcuna carta, e che quindi la base dei doni del
# verificatore non puo' conoscere per costruzione. Sono la ragione per cui questo archivio esiste
# nel progetto: 978 distribuzioni su 1880 passano di qui.
METODI_SENZA_CARTA = {"In-Life", "In Life", "In-Game", "Global Link"}

# Le diciture con cui l'archivio dichiara che un campo appartiene a chi riceve invece che alla
# distribuzione. Vanno riconosciute perche' cambiano la natura del lavoro: dove compaiono, il campo
# non si copia ma si scrive con l'allenatore del progetto.
DEL_RICEVENTE = ("Yours", "yours", "Your OT", "Player")


def del_ricevente(valore):
    return any(s in valore for s in DEL_RICEVENTE)


def ambiguo(valore):
    """Vero se il campo dichiara un'alternativa invece di un valore, per esempio due abilita'."""
    return " or " in valore or "/" in valore or "??" in valore


def righe_allenatore(v):
    """Le varianti dell'allenatore di una distribuzione, gia' separate dal censimento."""
    return [x.strip() for x in (v.get("allenatore") or "").split(" / ") if x.strip()]


def scrivi_senza_carta(voci, specie_bersaglio, nomi_specie):
    """Il documento di produzione delle distribuzioni che non hanno lasciato una carta.

    E' la coda di lavoro di una via nuova. Per ogni altra generazione il generatore parte da una
    carta e ne compone i campi mancanti; qui la carta non esiste e non e' mai esistita, quindi il
    solo dato disponibile e' quello che un archivio ha registrato mentre l'evento accadeva. Il
    documento riporta per ciascuna voce i campi tecnici cosi' come l'archivio li porta, e segnala
    separatamente i due casi in cui un campo non e' un valore: quando appartiene a chi riceve, e
    quando l'archivio dichiara un'alternativa invece di una scelta.
    """
    scelte = [v for v in voci
              if v["dex"] in specie_bersaglio and v["metodo"] in METODI_SENZA_CARTA]
    r = []
    r.append("# Distribuzioni senza carta: la coda di produzione")
    r.append("")
    r.append("> Documento generato da `tools/leggi-serebii-eventi.py --senza-carta`. Non si "
             "modifica a mano: si rigenera. Ogni riga porta accanto la pagina dell'archivio da cui "
             "viene, che è la fonte di quel dato.")
    r.append("")
    r.append("Questa è la coda di una via di produzione che il progetto non ha mai percorso. Per "
             "ogni altra generazione il generatore parte da una carta, cioè dal file che la "
             "distribuzione consegnava, e ne compone i campi che la carta lascia liberi. Qui la "
             "carta non esiste e non è mai esistita: la consegna avveniva presso un apparecchio "
             "che scriveva direttamente nel salvataggio, oppure dentro il gioco, oppure attraverso "
             "il servizio in rete della quinta generazione. Il solo dato disponibile è quello che "
             "un archivio ha registrato mentre l'evento accadeva.")
    r.append("")
    r.append("Le distribuzioni qui elencate sono %d e riguardano le %d specie che l'archivio "
             "conosce e la nostra enumerazione no. Sono la cecità misurata il 2026-09-07, non una "
             "stima." % (len(scelte), len(specie_bersaglio)))
    r.append("")
    r.append("## I due casi in cui un campo non è un valore")
    r.append("")
    ric = [v for v in scelte if del_ricevente(v["allenatore"]) or del_ricevente(v["identificativo"])]
    amb = [v for v in scelte if ambiguo(v["abilita"]) or ambiguo(v["livello"])]
    r.append("Il primo è il campo che appartiene a chi riceve. L'archivio lo dichiara scrivendo "
             "che il valore è quello del giocatore, e riguarda %d voci di questa coda. Per quelle "
             "il campo non si copia ma si scrive con l'allenatore del progetto, come già si fa per "
             "le voci di seconda e terza generazione che la fonte marca allo stesso modo."
             % len(ric))
    r.append("")
    r.append("Il secondo è il campo che dichiara un'alternativa invece di una scelta, tipicamente "
             "due abilità possibili oppure un livello che l'archivio non conosce. Riguarda %d voci "
             "e richiede una decisione per ciascuna, che non è di questo documento: qui si segnala "
             "soltanto che la decisione serve." % len(amb))
    r.append("")
    r.append("## Le voci")
    r.append("")
    r.append("## L'espansione per allenatore")
    r.append("")
    r.append("La decisione dell'utente del 2026-09-07 è che una distribuzione con più allenatori "
             "dichiarati vale un esemplare per ciascun allenatore, non uno solo. L'archivio separa "
             "le varianti con una interruzione di riga, e questo documento le espande di "
             "conseguenza: le %d righe di distribuzione diventano %d esemplari da produrre."
             % (len(scelte), sum(max(1, len(righe_allenatore(v))) for v in scelte)))
    r.append("")
    r.append("Va dichiarato il limite della regola, perché non è meccanica. Una interruzione di "
             "riga separa varianti, ma che cosa una variante sia dipende dalla distribuzione: "
             "quattro lettere consecutive del medesimo negozio sono quattro allenatori distinti, "
             "mentre un nome scritto in giapponese e poi in quattro lingue europee è un allenatore "
             "solo, tradotto. La regione aiuta e non basta, perché esistono distribuzioni di una "
             "sola regione i cui due nomi sono manifestamente lo stesso nome in due lingue. Nelle "
             "voci di questo documento la distinzione è stata fatta a mano e ciascuna riga dichiara "
             "quale lettura si sia applicata.")
    r.append("")
    r.append("| Dex | Specie | Anno | Regione | Metodo | Livello | Allenatore | Identificativo | "
             "Abilità | Palla | Mosse | Da decidere | Fonte |")
    r.append("|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    for v in sorted(scelte, key=lambda x: (x["dex"], x["anno"])):
        note = []
        if del_ricevente(v["allenatore"]) or del_ricevente(v["identificativo"]):
            note.append("allenatore del progetto")
        if ambiguo(v["abilita"]):
            note.append("abilità alternativa")
        if ambiguo(v["livello"]) or not v["livello"]:
            note.append("livello ignoto")
        if not v["palla"]:
            note.append("palla non dichiarata")
        allenatori = righe_allenatore(v) or ["-"]
        if len(allenatori) > 1:
            note.append("%d allenatori, una voce ciascuno" % len(allenatori))
        for nome_ot in allenatori:
            r.append("| %d | %s | %s | %s | %s | %s | `%s` | `%s` | %s | %s | %s | %s | `%s` |"
                     % (v["dex"], nomi_specie.get(v["dex"], "?"), v["anno"] or "-",
                        v["regione"] or "-", v["metodo"] or "-", v["livello"] or "?",
                        nome_ot.replace("|", "/"),
                        (v["identificativo"] or "-").replace("|", "/"),
                        (v["abilita"] or "-").replace("|", "/"),
                        v["palla"] or "-", (v["mosse"] or "-").replace("|", "/"),
                        ", ".join(note) or "nulla", v["sorgente"]))
    r.append("")
    io.open(SENZA_CARTA, "w", encoding="utf-8", newline="\n").write("\n".join(r) + "\n")
    return len(scelte), len(ric), len(amb)


def self_test():
    falliti = 0

    def prova(nome, atteso, ottenuto):
        nonlocal falliti
        if atteso != ottenuto:
            falliti += 1
            print("  FALLITO %s: atteso %r, ottenuto %r" % (nome, atteso, ottenuto))

    # Gli indirizzi si leggono dalle opzioni e non dai collegamenti: e' la lezione che ha fatto
    # riferire zero pagine su una pagina che ne indicizza piu' di mille.
    html = ('<a href="/events/finto.shtml">non una opzione</a>'
            '<option value="/events/dex/001.shtml">001 Bulbasaur</option>'
            '<option value="/events/2003.shtml">2003 Events</option>'
            '<option value="#">non un indirizzo</option>')
    voci = indirizzi_dalla_mappa(html)
    prova("legge le sole opzioni con un indirizzo", 2, len(voci))
    prova("e ne conserva il titolo", "001 Bulbasaur", voci[0]["titolo"])
    prova("il collegamento non entra", True,
          all("finto" not in v["url"] for v in voci))

    prova("il nome del file appiattisce il percorso", "events__dex__001.shtml",
          nome_file("/events/dex/001.shtml"))

    prova("la stella e' il contrassegno del cromatico", "9733", STELLA)
    prova("le entita' numeriche si estraggono", {"9733", "10010"}, entita("a&#9733;b&#10010;c"))

    prova("la pulizia toglie i marcatori", "uno due", pulisci("<b>uno</b><br />due"))
    prova("e normalizza gli spazi", "a b", pulisci("a   \n  b"))

    # Il separatore delle varianti e' una interruzione di riga, e la pulizia generale lo
    # distruggerebbe: un nome con uno spazio dentro verrebbe contato come due.
    quattro = '<td class="detailhead">OT:</td><td>PCNYa<br />PCNYb<br />PCNYc<br />PCNYd</td>'
    prova("quattro lettere separate danno quattro nomi", 4, len(campo_multiplo(quattro, "OT:")))
    prova("e il primo e' quello giusto", "PCNYa", campo_multiplo(quattro, "OT:")[0])
    uno = '<td class="detailhead">OT:</td><td>10 ANIV</td>'
    prova("un nome con uno spazio resta un nome solo", 1, len(campo_multiplo(uno, "OT:")))
    prova("e conserva il proprio spazio", "10 ANIV", campo_multiplo(uno, "OT:")[0])
    prova("un campo assente da' un elenco vuoto", [], campo_multiplo(uno, "ID:"))

    campo = ('<td class="detailhead">OT:</td><td>Ilex</td>')
    prova("il campo etichettato si legge", "Ilex", campo_etichettato(campo, "OT:"))
    prova("una etichetta assente da' stringa vuota", "", campo_etichettato(campo, "ID:"))

    tab = ('<table><tr><td class="detailhead">Description</td>'
           '<td class="detailhead">Type</td><td class="detailhead">Location</td></tr>'
           '<tr><td>Regalo</td><td>Serial Code</td><td>Japan</td></tr></table>')
    d = celle_di_tabella(tab, "Description")
    prova("la tabella per etichetta rende il metodo", "Serial Code", d.get("Type"))
    prova("e il luogo", "Japan", d.get("Location"))

    # Un record minimo, per verificare che il contesto di anno e regione venga dai titoli che
    # precedono il blocco e non da dentro il blocco.
    pagina = ('<p><u>2017</u></p><p><u>America</u></p><table class="eventpoke">'
              '<td class="label"><img src="/itemdex/sprites/cherishball.png" /> Celebi </td>'
              '<td class="label">Level 30<br /><b>&#9733;</b></td>'
              '<td class="detailhead">OT:</td><td>Ilex</td>'
              '</table><br />')
    v = voci_della_pagina(pagina, "prova")
    prova("un record viene letto", 1, len(v))
    prova("con l'anno dal titolo che precede", "2017", v[0]["anno"])
    prova("con la regione dal titolo che precede", "America", v[0]["regione"])
    prova("con la palla dal nome dello sprite", "cherishball", v[0]["palla"])
    prova("con il livello", "30", v[0]["livello"])

    # Un record il cui livello l'archivio non conosce conserva comunque i propri contrassegni.
    pagina = ('<p><u>2025</u></p><p><u>China</u></p><table class="eventpoke">'
              '<td class="label"><img src="/itemdex/sprites/pokeball.png" /> Arbok </td>'
              '<td class="label">Level ??<br /><b>&#9733;</b></td>'
              '</table><br />')
    w = voci_della_pagina(pagina, "prova")
    prova("un livello ignoto non fa perdere il record", 1, len(w))
    prova("il livello resta vuoto", "", w[0]["livello"])
    prova("ma il contrassegno di cromatico si legge lo stesso", "si", w[0]["cromatico"])
    prova("e riconosciuto come cromatico", "si", v[0]["cromatico"])

    testo = in_csv([{c: "" for c in CAMPI} | {"descrizione": "uno, due"}])
    prova("la virgola dentro una descrizione viene protetta", True, '"uno, due"' in testo)
    prova("e la riga resta una sola", 2, len(testo.rstrip("\n").split("\n")))

    print("self-test: %d controlli falliti" % falliti)
    return 1 if falliti else 0


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--mappa", action="store_true", help="scarica l'indice e ne estrae gli indirizzi")
    ap.add_argument("--scarica", action="store_true", help="scarica le pagine che mancano dalla cache")
    ap.add_argument("--censimento", action="store_true", help="spoglia la cache e scrive i documenti")
    ap.add_argument("--limite", type=int, default=0, help="quante pagine scaricare al massimo")
    ap.add_argument("--pausa", type=float, default=PAUSA, help="secondi fra una richiesta e l'altra")
    ap.add_argument("--senza-carta", action="store_true", dest="senza_carta",
                    help="scrive la coda delle distribuzioni che non hanno lasciato una carta")
    ap.add_argument("--self-test", action="store_true", dest="self_test")
    a = ap.parse_args(argv)
    if a.self_test:
        return self_test()
    if not os.path.isdir(CACHE):
        os.makedirs(CACHE)

    if a.mappa:
        percorso = os.path.join(CACHE, nome_file(INDICE) + ".html")
        scarica(INDICE, percorso, a.pausa)
        html = io.open(percorso, encoding="utf-8", errors="replace").read()
        voci = indirizzi_dalla_mappa(html)
        io.open(MAPPA, "w", encoding="utf-8").write(
            json.dumps(voci, ensure_ascii=False, indent=1) + "\n")
        specie = [v for v in voci if v["url"].startswith("/events/dex/")]
        print("mappa scritta in %s" % MAPPA)
        print("  indirizzi totali %d, di cui pagine di specie %d" % (len(voci), len(specie)))
        return 0

    if a.scarica:
        if not os.path.exists(MAPPA):
            print("rifiutato: manca la mappa, si ottiene con --mappa")
            return 1
        voci = json.load(io.open(MAPPA, encoding="utf-8"))
        fatte, saltate, byte = 0, 0, 0
        for v in voci:
            percorso = os.path.join(CACHE, nome_file(v["url"]) + ".html")
            if os.path.exists(percorso):
                saltate += 1
                continue
            if a.limite and fatte >= a.limite:
                break
            try:
                byte += scarica(v["url"], percorso, a.pausa)
                fatte += 1
            except Exception as errore:
                print("  非 %s: %s" % (v["url"], errore))
        print("scaricate %d pagine (%d KiB), gia' presenti %d, mancanti %d"
              % (fatte, byte // 1024, saltate,
                 len(voci) - saltate - fatte))
        return 0

    if a.senza_carta:
        if not os.path.exists(TABELLA):
            print("rifiutato: manca il censimento, si ottiene con --censimento")
            return 1
        import csv
        voci = []
        for riga in csv.DictReader(io.open(TABELLA, encoding="utf-8")):
            m = re.search(r"(\d+)\.shtml", riga["sorgente"])
            if not m:
                continue
            riga["dex"] = int(m.group(1))
            voci.append(riga)
        # Le specie che l'archivio conosce e la nostra enumerazione no, misurate il 2026-09-07.
        bersaglio = {23, 252, 258, 270, 292, 332, 336, 353, 358, 367, 368, 396, 513, 515}
        nomi = {}
        percorso = os.path.join(RADICE, "_notes", "fonti", "pkhex", "PKHeX.Core", "Resources",
                                "text", "other", "it", "text_Species_it.txt")
        if os.path.exists(percorso):
            nomi = dict(enumerate(io.open(percorso, encoding="utf-8").read().splitlines()))
        quante, ric, amb = scrivi_senza_carta(voci, bersaglio, nomi)
        print("scritta la coda in %s" % SENZA_CARTA)
        print("  voci %d, di cui %d con un campo di chi riceve e %d con un campo alternativo"
              % (quante, ric, amb))
        return 0

    if a.censimento:
        if not os.path.exists(MAPPA):
            print("rifiutato: manca la mappa, si ottiene con --mappa")
            return 1
        voci_mappa = json.load(io.open(MAPPA, encoding="utf-8"))

        def raccolta(filtro):
            fuori, pagine = [], 0
            for v in voci_mappa:
                if not filtro(v["url"]):
                    continue
                percorso = os.path.join(CACHE, nome_file(v["url"]) + ".html")
                if not os.path.exists(percorso):
                    continue
                html = io.open(percorso, encoding="utf-8", errors="replace").read()
                fuori.extend(voci_della_pagina(html, v["url"]))
                pagine += 1
            return fuori, pagine

        # Le pagine di specie restano la tabella primaria, perche' sono le sole che diano il numero
        # di catalogo e perche' il loro conto e' gia' verificato su tre assi indipendenti.
        specie, n_specie = raccolta(lambda u: u.startswith("/events/dex/"))
        io.open(TABELLA, "w", encoding="utf-8", newline=chr(10)).write(in_csv(specie))
        print("censite %d distribuzioni da %d pagine di specie" % (len(specie), n_specie))

        # Le pagine indice sono un sovrainsieme e servono per cio' che nessuna specie indicizza,
        # cioe' tipicamente le consegne di biglietti, che sbloccano un incontro invece di
        # consegnare un esemplare. Il confronto non puo' usare il nome della specie, perche' le
        # pagine indice lo scrivono nella lingua della distribuzione e quelle di specie in
        # inglese, ne la regione, che nelle due viste e' dichiarata diversamente.
        indice, n_indice = raccolta(lambda u: not u.startswith("/events/dex/"))
        def chiave(x):
            return (x["descrizione"], x["allenatore"], x["identificativo"], x["livello"])
        note = {chiave(x) for x in specie}
        viste, fuori = set(), []
        for x in indice:
            k = chiave(x)
            if k in note or k in viste:
                continue
            viste.add(k)
            fuori.append(x)
        io.open(SOLO_INDICE, "w", encoding="utf-8", newline=chr(10)).write(in_csv(fuori))
        print("dalle %d pagine indice: %d record, di cui %d non indicizzati da alcuna specie"
              % (n_indice, len(indice), len(fuori)))
        print("scritte le tabelle in %s e %s" % (TABELLA, SOLO_INDICE))
        return 0

        if not os.path.exists(MAPPA):
            print("rifiutato: manca la mappa, si ottiene con --mappa")
            return 1
        voci_mappa = json.load(io.open(MAPPA, encoding="utf-8"))
        tutte, pagine = [], 0
        for v in voci_mappa:
            if not v["url"].startswith("/events/dex/"):
                continue
            percorso = os.path.join(CACHE, nome_file(v["url"]) + ".html")
            if not os.path.exists(percorso):
                continue
            html = io.open(percorso, encoding="utf-8", errors="replace").read()
            tutte.extend(voci_della_pagina(html, v["url"]))
            pagine += 1
        io.open(TABELLA, "w", encoding="utf-8", newline="\n").write(in_csv(tutte))
        print("censite %d distribuzioni da %d pagine di specie" % (len(tutte), pagine))
        print("scritta la tabella in %s" % TABELLA)
        return 0

    ap.error("serve una fra --mappa, --scarica, --censimento e --self-test")


if __name__ == "__main__":
    sys.exit(main())
