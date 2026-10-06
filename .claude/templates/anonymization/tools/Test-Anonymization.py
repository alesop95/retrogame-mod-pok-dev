# -*- coding: utf-8 -*-
"""
Guard-rail di anonimizzazione sui file del repository.

Perché esiste. Quando un repository è pubblico, o anche solo condiviso più largamente di
chi lo scrive, tutto ciò che entra in un file tracciato è visibile per sempre, anche dopo
una correzione successiva, perché la storia git resta consultabile finché non viene
riscritta. La regola che governa la materia è `.claude/rules/anonymization.md`, ma una
regola scritta non impedisce un residuo: nel progetto in cui questo strumento è nato il
primo audit ne ha trovati centoquarantotto su ottantanove file, **nessuno introdotto di
proposito e nessuno appartenente alla sessione che li ha scoperti**. Un residuo non si
introduce, si eredita, e per questo il controllo si fa sull'intero perimetro e non sui soli
file toccati.

Che cosa cerca, e perché non sono soltanto i segreti. Uno scanner di credenziali cerca
chiavi e token, cioè stringhe con una forma riconoscibile. Questo cerca una categoria
diversa e più insidiosa, cioè i dati che identificano persone, luoghi e infrastrutture:
indirizzi IP reali, indirizzi fisici di apparati, nomi propri di persona, caselle di posta
personali, numeri di telefono, importi, IBAN e partite IVA. Sono dati che nessun pattern
universale riconosce, perché un nome proprio è un nome proprio solo se è di qualcuno:
per questo l'elenco di ciò che va cercato vive fuori dallo script.

Come non tradisce se stesso. Questo script è versionato e **non contiene nessun valore
reale**: prefissi di rete, nomi propri, indirizzi di posta, prefissi telefonici e segreti
letterali da cercare vivono in un file di pattern ignorato da git, accanto alla mappa dei
segnaposto. Se quel file manca, lo script lo dice e si ferma invece di dare un esito verde
che non ha calcolato. È la proprietà che rende pubblicabile lo strumento che serve a
tenere pubblicabile il repository.

Il perimetro, e perché dal 07/09/2026 non è più soltanto ciò che git traccia. Fino a
quella data lo script passava `git ls-files`, cioè i soli file già tracciati, e ne
derivava una lacuna precisa: un file **nuovo**, scritto e non ancora aggiunto all'indice,
era invisibile al controllo proprio nel momento in cui serviva guardarlo, cioè prima di
pubblicarlo. È accaduto il 04/09/2026 con tre file nuovi, e il difetto è della stessa
famiglia degli altri due già corretti in questo progetto, la cartella esclusa del delta e
i pattern di rilevanza: non si sbaglia su ciò che si conosce, si sbaglia sul confine.

Il perimetro predefinito è perciò **ciò che sta per essere pubblicato**: i file tracciati
più quelli non tracciati e non ignorati, che sono esattamente i candidati al prossimo
commit. I riscontri di entrambi i gruppi sono bloccanti, perché entrambi i gruppi finiscono
in pubblico.

Con `--tutti` entrano anche i file **ignorati**, cioè `_notes/` e `output/`. Quelli
contengono valori reali **per costruzione e per decisione**: sono il layer narrativo locale e
gli output degli script, ed è il motivo per cui git li ignora. I loro riscontri vengono
quindi elencati a parte e **non sono bloccanti**: servono a sapere che cosa vive sul disco, non
a dichiarare un difetto. Confonderli con i primi renderebbe lo script inutile, perché
fallirebbe sempre e nessuno lo guarderebbe più.

Uso, dalla radice del progetto:
    python tools/Test-Anonymization.py             # tracciati + non tracciati non ignorati
    python tools/Test-Anonymization.py --tutti     # anche il layer privato, non bloccante
    python tools/Test-Anonymization.py --quiet     # solo il conteggio e l'esito
    python tools/Test-Anonymization.py --max 20    # limita le righe stampate per categoria
    python tools/Test-Anonymization.py --patterns <percorso>   # file di pattern altrove
    python tools/Test-Anonymization.py --autotest  # prova le forme degli identificatori di console

Codice di uscita: 0 se non ci sono riscontri nelle categorie bloccanti, 1 altrimenti. Le
categorie non bloccanti raccolgono ciò che va guardato da un umano e che è spesso un
falso positivo, per esempio un numero di versione che somiglia a un indirizzo.
"""

import argparse
import collections
import io
import json
import os
import re
import subprocess
import sys

# Percorso predefinito del file di pattern. Sta in `_notes/` perché quella cartella è
# ignorata da git in questo sistema di progetto: è il layer che può contenere valori reali.
# Si sposta con --patterns nei progetti che organizzano diversamente il proprio layer privato.
PATTERNS_FILE = os.path.join("_notes", ".anonymization-patterns.json")
SKIP_EXT = {".png", ".jpg", ".jpeg", ".gif", ".pdf", ".xlsx", ".docx", ".zip", ".ico", ".drawio",
            # aggiunte il 07/09/2026 con l'allargamento del perimetro: entrando anche i file
            # non tracciati e, con --tutti, quelli ignorati, si incontrano archivi ed eseguibili
            # in cui una ricerca per riga non ha alcun senso e costa solo tempo.
            ".7z", ".rar", ".msi", ".exe", ".dll", ".pyc", ".bin", ".db", ".sqlite", ".qdff",
            ".mp4", ".mov", ".xlsm", ".pptx", ".doc", ".xls", ".vsdx", ".eml", ".msg"}
# Un file molto grande in un layer privato è tipicamente uno storico o un dump: leggerlo
# riga per riga costa minuti e non aggiunge segnale. Si dichiara di averlo saltato.
LIMITE_BYTE = 5 * 1024 * 1024

# Categorie che fanno fallire il controllo: sono valori reali, non ambiguità.
BLOCCANTI = {"IP REALE", "MAC REALE", "NOME PROPRIO", "SEGRETO LETTERALE",
             "EMAIL PERSONALE", "TELEFONO", "IBAN", "PIVA/CF", "IMPORTO", "ID CONSOLE"}

IPV4 = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}(?:/\d{1,2})?\b")
MAC = re.compile(r"\b(?:[0-9A-Fa-f]{2}[:-]){5}[0-9A-Fa-f]{2}\b")
EMAIL = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")
# I prefissi telefonici da cercare non possono stare qui: un numero di telefono è un dato
# personale solo se è di qualcuno, e quali prefissi appartengano al progetto lo sa il file
# dei pattern. Se la chiave `prefissi_telefonici` manca, si ripiega sul solo formato
# internazionale, che è riconoscibile senza sapere nulla del progetto.
PHONE_FALLBACK = re.compile(r"\b\+\d{2}\s?\d{9,10}\b")
MONEY = re.compile(r"(?:€\s?[\d.,]+|\b[\d.]+[,.]\d{2}\s?(?:€|euro|EUR)\b|\b\d+(?:[.,]\d+)?\s?euro\b)", re.I)
IBAN = re.compile(r"\bIT\d{2}[A-Z0-9]{20,25}\b")
PIVA = re.compile(r"\b(?:P\.?\s?IVA|partita iva|cod\.?\s?fisc|codice fiscale)\b[^\n]{0,40}\d{11,16}", re.I)
# Domini riservati alla documentazione da RFC 2606: non esistono, non sono registrabili
# e non possono appartenere a nessuno, quindi una casella su di essi è un esempio e non il
# dato di una persona. È la stessa ammissione per costruzione che vale per i blocchi di
# indirizzi di RFC 5737, e la sua assenza era un'asimmetria: senza di essa ogni documento
# che usa un indirizzo di esempio produce un riscontro bloccante, e chi scrive documentazione
# impara a ignorare l'esito del controllo.
DOMINI_DOC = ("example.com", "example.org", "example.net", "example.edu", ".example")

# Segnaposto legittimi per la posta: persona-a@, referente-esempio-1@, e simili.
MAIL_PLACEHOLDER = re.compile(r"^(persona|referente|collaboratore|consulente|tirocinante)-", re.I)

# Identificatori unici di una console o di un supporto, aggiunti il 2026-10-06. Non sono dati di una
# persona ma la identificano lo stesso, attraverso l'apparecchio che possiede, e non si possono
# ruotare: le cartelle ID0 e ID1 della scheda SD di un 3DS derivano da `movable.sed` e dal CID della
# scheda, il numero di serie di un volume Windows identifica il disco, e il seme `LocalFriendCodeSeed`
# è il segreto da cui la console ricava il proprio codice amico. Il caso che li ha portati qui è una
# nota tracciata che li riportava in chiaro, scoperta a mano e mascherata con <ID0-SD>, <ID1-SD> e
# <SERIALE-VOLUME>. Le forme sono riconoscibili senza conoscere il progetto, quindi stanno nello script
# e non nel file dei pattern; ciò che le rende un dato è la vicinanza della parola che le nomina,
# entro VICINANZA_ID caratteri, perché trentadue cifre esadecimali da sole sono anche un MD5 qualunque.
VICINANZA_ID = 200
HEX32 = re.compile(r"(?<![0-9A-Za-z])[0-9A-Fa-f]{32}(?![0-9A-Za-z])")
PAROLA_ID_SD = re.compile(r"\bID[01]\b")
SERIALE_LUNGO = re.compile(r"(?<![0-9A-Za-z])[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}:[0-9A-Fa-f]{4}(?![0-9A-Za-z])")
SERIALE_CORTO = re.compile(r"(?<![0-9A-Za-z:-])[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}(?![0-9A-Za-z:-])")
PAROLA_SERIALE = re.compile(r"\bseri(?:e|al|ale)\b", re.I)
# La forma corta, quella che `vol` stampa, ha la forma di un intervallo qualunque: righe di sorgente
# citate come intervallo o indirizzi di memoria di Game Boy, che in questo progetto stanno spesso accanto a
# «serie» o a «Serial» nel senso del cavo di collegamento. Per lei la parola deve essere quella del
# numero di serie, non soltanto «serie». La prima corsa con la parola generica, sul layer privato, ha
# dato 9 riscontri e tutti di questo tipo.
PAROLA_SERIALE_CORTO = re.compile(r"numero di serie|serial number|seriale del volume|n\.\s?di serie", re.I)
# Un intervallo di anni, come 1999-2000, ha la stessa forma e può stare accanto alla parola giusta.
INTERVALLO_ANNI = re.compile(r"^(?:19|20)\d\d-(?:19|20)\d\d$")
SEME_CONSOLE = re.compile(r"(?:movable\.sed|LocalFriendCodeSeed(?:_[AB])?)[^\n]{0,60}?"
                          r"(?<![0-9A-Za-z])([0-9A-Fa-f]{16,})(?![0-9A-Za-z])")


def cerca_id_console(contenuto):
    """Gli identificatori unici di console e supporto in un testo, come (posizione, valore, forma)."""
    trovati = []

    def vicino(regex, inizio, fine):
        return regex.search(contenuto, max(0, inizio - VICINANZA_ID), fine + VICINANZA_ID) is not None

    for m in HEX32.finditer(contenuto):
        if vicino(PAROLA_ID_SD, m.start(), m.end()):
            trovati.append((m.start(), m.group(0), "cartella ID0 o ID1 della SD"))
    for m in SERIALE_LUNGO.finditer(contenuto):
        if vicino(PAROLA_SERIALE, m.start(), m.end()):
            trovati.append((m.start(), m.group(0), "numero di serie di volume"))
    for m in SERIALE_CORTO.finditer(contenuto):
        if INTERVALLO_ANNI.match(m.group(0)):
            continue
        if vicino(PAROLA_SERIALE_CORTO, m.start(), m.end()):
            trovati.append((m.start(), m.group(0), "numero di serie di volume"))
    for m in SEME_CONSOLE.finditer(contenuto):
        trovati.append((m.start(1), m.group(1), "seme o chiave della console"))
    return sorted(trovati)


def autotest():
    """Prova che ogni forma di identificatore di console sia presa, e che i falsi amici non lo siano.

    I valori di prova si compongono a tempo di esecuzione e non stanno scritti per intero in questo
    file, che è tracciato: altrimenti lo strumento troverebbe sé stesso a ogni corsa sul repository.
    """
    h16 = "0123456789abcdef"
    h32 = h16 * 2
    id0, id1 = "ID" + "0", "ID" + "1"
    serie_lungo = "1A2B3C4D" + "-" + "5E6F" + ":" + "7A8B"
    serie_corto = "C0DE" + "-" + "BEEF"
    positivi = [
        ("cartella ID0 sulla stessa riga", "%s: Nintendo 3DS/%s/" % (id0, h32.upper()), h32.upper()),
        ("cartella ID1 nominata sulla riga prima",
         "La cartella %s della scheda è questa:\n\n    sdmc:/x/%s/" % (id1, h32), h32),
        ("seriale di volume in forma lunga", "Numero di serie del volume: %s" % serie_lungo, serie_lungo),
        ("seriale di volume in forma corta", "Volume Serial Number is %s" % serie_corto, serie_corto),
        ("contenuto di movable.sed", "movable.sed: " + h32, h32),
        ("seme LocalFriendCodeSeed", "LocalFriendCodeSeed_B = " + h16, h16),
    ]
    negativi = [
        ("impronta SHA-256 accanto a ID0", "%s sha256 %s" % (id0, h32 * 2)),
        ("hash di commit accanto a ID1", "%s commit %s" % (id1, (h16 * 3)[:40])),
        ("trentadue cifre lontane dalla parola", id0 + " " + "x" * (VICINANZA_ID + 10) + " " + h32),
        ("nome di file di PKHeX", "%s: 0151 - Mew - 5E7F8A9B1C2D.pk3 e 025 - Pikachu - 3A1B2C4D.pk7" % id0),
        ("intervallo di anni accanto a serie", "la serie uscita nel 1999-2000"),
        ("segnaposto già mascherati", "Nintendo 3DS/<ID0-SD>/<ID1-SD>/ numero di serie <SERIALE-VOLUME>"),
        ("data accanto a serie", "serie del 2026-10-06"),
        ("righe di sorgente accanto a serie", "la serie di vittorie, righe 1836" + "-" + "1839"),
        ("indirizzi di memoria accanto a Serial", "Serial\n FFA9" + "-" + "FFAD - Serial status data"),
    ]
    falliti = 0
    for nome, testo, atteso in positivi:
        valori = [v for _p, v, _f in cerca_id_console(testo)]
        esito = atteso in valori
        falliti += not esito
        print("  %s  preso: %s" % ("ok     " if esito else "FALLITO", nome))
    for nome, testo in negativi:
        valori = [v for _p, v, _f in cerca_id_console(testo)]
        esito = not valori
        falliti += not esito
        print("  %s  ignorato: %s%s" % ("ok     " if esito else "FALLITO", nome,
                                        "" if esito else " (preso %s)" % valori))
    print("autotest: %d controlli falliti su %d" % (falliti, len(positivi) + len(negativi)))
    return 1 if falliti else 0


def trova_radice(partenza=None):
    """Risale fino alla radice del repository partendo dalla posizione di questo file.

    Perché dalla posizione del file e non dalla cartella corrente. La cartella corrente
    dipende da chi invoca, e chi invoca può essere una sessione interattiva, un hook, una
    attività pianificata o un altro script: sono quattro cartelle diverse per lo stesso
    comando, e il messaggio d'errore che ne segue parla d'altro. La posizione del file
    invece è un fatto. Il criterio funziona identico su Windows e su Linux perché non
    guarda separatori né lettere di unità.

    `.git` si cerca sia come cartella sia come file, perché in un worktree o in un
    sottomodulo è un file che punta altrove: trattarla come sola cartella è un difetto
    che si manifesta soltanto in quei due casi, cioè tardi.
    """
    corrente = os.path.abspath(partenza or os.path.dirname(os.path.abspath(__file__)))
    while True:
        candidata = os.path.join(corrente, ".git")
        if os.path.isdir(candidata) or os.path.isfile(candidata):
            return corrente
        genitore = os.path.dirname(corrente)
        if genitore == corrente:
            return None
        corrente = genitore


def carica_pattern(percorso=PATTERNS_FILE):
    """Carica il file di pattern, oppure si ferma dichiarandolo.

    Fermarsi invece di proseguire con un elenco vuoto è una scelta e non una svista: un
    controllo senza pattern non trova nulla e stamperebbe un verde, che è la peggiore
    delle uscite possibili perché assomiglia a un esito senza esserlo."""
    if not os.path.exists(percorso):
        sys.stderr.write(
            "File dei pattern non trovato: %s\n"
            "Serve per sapere che cosa cercare, e non è versionato perché contiene i valori\n"
            "reali del progetto. Si costruisce dalla mappa dei segnaposto, partendo da\n"
            "patterns.example.json di questo pacchetto.\n"
            "Senza di esso questo controllo non si dichiara verde: si ferma.\n" % percorso)
        sys.exit(2)
    with io.open(percorso, encoding="utf-8") as fh:
        pat = json.load(fh)
    obbligatorie = ("reti_documentali_ammesse", "ip_ammessi", "prefissi_reali",
                    "mac_ammessi_prefissi", "email_ammesse", "nomi_propri")
    mancanti = [k for k in obbligatorie if k not in pat]
    if mancanti:
        sys.stderr.write(
            "Il file dei pattern non ha le chiavi obbligatorie: %s\n"
            "Vedi patterns.example.json per la forma attesa.\n" % ", ".join(mancanti))
        sys.exit(2)
    return pat


def _git(*argomenti):
    out = subprocess.run(["git"] + list(argomenti), capture_output=True, text=True,
                         encoding="utf-8", errors="replace").stdout
    return [f for f in out.split("\n") if f.strip()]


def file_perimetro(includi_ignorati):
    """Restituisce [(percorso, origine)] con origine tracciato/non tracciato/ignorato.

    L'ordine conta: prima ciò che è già pubblico, poi ciò che sta per diventarlo, poi
    il layer privato. È anche l'ordine di gravità con cui i riscontri vanno letti.
    """
    elenco = [(f, "tracciato") for f in _git("ls-files")]
    elenco += [(f, "non tracciato") for f in _git("ls-files", "--others", "--exclude-standard")]
    if includi_ignorati:
        elenco += [(f, "ignorato") for f in _git("ls-files", "--others", "--ignored",
                                                 "--exclude-standard")]
    visti = set()
    unici = []
    for f, origine in elenco:
        if f not in visti:
            visti.add(f)
            unici.append((f, origine))
    return unici


def analizza(pat, files):
    """`files` è una lista di coppie (percorso, origine). L'origine viaggia con il
    riscontro fino alla stampa, perché lo stesso valore reale ha significato opposto a
    seconda di dove sta: in un file tracciato è un leak, in `_notes/` è il dato."""
    trovati = collections.defaultdict(list)
    saltati = []

    def aggiungi(cat, path, ln, riga, hit, origine="tracciato"):
        trovati[cat].append((path, ln, hit, riga.strip()[:190], origine))

    prefissi_tel = pat.get("prefissi_telefonici", [])
    if prefissi_tel:
        alternative = "|".join(re.escape(x) + r"\s?\d{5,8}" for x in prefissi_tel)
        phone = re.compile(r"\b(?:%s|\+\d{2}\s?\d{9,10})\b" % alternative)
    else:
        phone = PHONE_FALLBACK

    doc_nets = tuple(pat["reti_documentali_ammesse"])
    ip_ok = set(pat["ip_ammessi"])
    reali = tuple(pat["prefissi_reali"])
    mac_ok = tuple(m.upper() for m in pat["mac_ammessi_prefissi"])
    mail_ok = set(m.lower() for m in pat["email_ammesse"])
    nomi = pat["nomi_propri"]
    nomi_ctx = pat.get("nomi_ammessi_in_contesto", [])
    segreti = pat.get("segreti_letterali", [])

    for f, origine in files:
        if os.path.splitext(f)[1].lower() in SKIP_EXT:
            continue
        try:
            if os.path.getsize(f) > LIMITE_BYTE:
                saltati.append(f)
                continue
            with io.open(f, encoding="utf-8", errors="replace") as fh:
                contenuto = fh.read()
        except (IOError, OSError):
            continue

        # Gli identificatori di console si cercano sul testo intero e non per riga, perché la parola
        # che li nomina può stare sulla riga prima, come in un percorso preceduto dalla sua spiegazione.
        righe = contenuto.split("\n")
        for posizione, valore, forma in cerca_id_console(contenuto):
            ln = contenuto.count("\n", 0, posizione) + 1
            aggiungi("ID CONSOLE", f, ln, righe[ln - 1], "%s: %s" % (forma, valore[:40]), origine)

        for ln, riga in enumerate(righe, 1):
            for m in IPV4.finditer(riga):
                ip = m.group(0)
                base = ip.split("/")[0]
                if base in ip_ok or base.startswith(doc_nets):
                    continue
                if base.startswith(reali):
                    aggiungi("IP REALE", f, ln, riga, ip, origine)
                elif base.startswith(("10.", "192.168.", "172.")):
                    aggiungi("IP privato fuori schema", f, ln, riga, ip, origine)
                else:
                    aggiungi("IP pubblico da valutare", f, ln, riga, ip, origine)

            for m in MAC.finditer(riga):
                mac = m.group(0).upper()
                if mac.startswith(mac_ok):
                    continue
                aggiungi("MAC REALE", f, ln, riga, mac, origine)

            for m in EMAIL.finditer(riga):
                mail = m.group(0)
                locale = mail.split("@")[0]
                dominio = mail.split("@")[-1].lower()
                if (mail.lower() in mail_ok
                        or MAIL_PLACEHOLDER.match(locale)
                        or dominio.endswith(DOMINI_DOC)):
                    continue
                aggiungi("EMAIL PERSONALE", f, ln, riga, mail, origine)

            for regex, cat in ((phone, "TELEFONO"), (MONEY, "IMPORTO"),
                               (IBAN, "IBAN"), (PIVA, "PIVA/CF")):
                for m in regex.finditer(riga):
                    aggiungi(cat, f, ln, riga, m.group(0)[:60], origine)

            for s in segreti:
                if s in riga:
                    aggiungi("SEGRETO LETTERALE", f, ln, riga, "<valore oscurato>", origine)

            bassa = riga.lower()
            for n in nomi:
                if n.lower() not in bassa:
                    continue
                # un nome dentro la ragione sociale legale è ammesso per decisione
                if any(c.lower() in bassa for c in nomi_ctx):
                    continue
                aggiungi("NOME PROPRIO", f, ln, riga, n, origine)

    return trovati, saltati


def main():
    ap = argparse.ArgumentParser(description="Guard-rail di anonimizzazione sui file del repository.")
    ap.add_argument("--quiet", action="store_true", help="stampa solo il riepilogo")
    ap.add_argument("--max", type=int, default=40, help="righe stampate per categoria")
    ap.add_argument("--tutti", action="store_true",
                    help="include anche i file ignorati (_notes/, output/): riscontri non bloccanti")
    ap.add_argument("--radice", default=None,
                    help="radice del repository (default: risalita dalla posizione dello script)")
    ap.add_argument("--patterns", default=PATTERNS_FILE,
                    help="percorso del file di pattern (default: %s)" % PATTERNS_FILE)
    ap.add_argument("--autotest", action="store_true",
                    help="prova le forme degli identificatori di console su testi costruiti, ed esce")
    args = ap.parse_args()
    if args.autotest:
        return autotest()

    radice = args.radice or trova_radice()
    if not radice:
        sys.stderr.write(
            "Radice del repository non trovata risalendo da %s.\n"
            "Indicarla con --radice, oppure eseguire lo strumento da dentro il repository.\n"
            % os.path.dirname(os.path.abspath(__file__)))
        return 2
    # Si entra nella radice: da qui in avanti ogni percorso relativo, compresi quelli
    # che git restituisce, è interpretabile senza sapere da dove si è partiti.
    os.chdir(radice)

    pat = carica_pattern(args.patterns)
    files = file_perimetro(args.tutti)
    trovati, saltati = analizza(pat, files)
    conteggio = collections.Counter(origine for _, origine in files)

    ordine = ["IP REALE", "MAC REALE", "ID CONSOLE", "SEGRETO LETTERALE", "NOME PROPRIO", "EMAIL PERSONALE",
              "TELEFONO", "IBAN", "PIVA/CF", "IMPORTO",
              "IP privato fuori schema", "IP pubblico da valutare"]

    bloccanti = 0
    da_guardare = 0
    privati = 0
    for cat in ordine:
        tutte = trovati.get(cat, [])
        if not tutte:
            continue
        # La separazione è il cuore dell'allargamento del perimetro: un valore reale in un
        # file pubblicabile è un difetto, lo stesso valore in `_notes/` è il dato per cui
        # `_notes/` esiste. Contarli insieme farebbe fallire lo script sempre.
        pubbliche = [v for v in tutte if v[4] != "ignorato"]
        riservate = [v for v in tutte if v[4] == "ignorato"]
        privati += len(riservate)
        if not pubbliche:
            continue
        if cat in BLOCCANTI:
            bloccanti += len(pubbliche)
        else:
            da_guardare += len(pubbliche)
        if args.quiet:
            continue
        etichetta = "BLOCCANTE" if cat in BLOCCANTI else "da valutare"
        print("\n" + "=" * 78)
        print("%s  [%s]  -  %d riscontri" % (cat, etichetta, len(pubbliche)))
        print("=" * 78)
        for path, ln, hit, testo, origine in pubbliche[:args.max]:
            marca = "" if origine == "tracciato" else "  <-- NON TRACCIATO, sta per essere pubblicato"
            print("  %s:%s  [%s]%s" % (path, ln, hit, marca))
            print("      %s" % testo)
        if len(pubbliche) > args.max:
            print("  ... e altri %d (usare --max)" % (len(pubbliche) - args.max))

    if args.tutti and privati and not args.quiet:
        print("\n" + "=" * 78)
        print("LAYER PRIVATO  [non bloccante]  -  %d riscontri in file ignorati da git" % privati)
        print("=" * 78)
        per_file = collections.Counter()
        for cat in ordine:
            for path, ln, hit, testo, origine in trovati.get(cat, []):
                if origine == "ignorato":
                    per_file[path] += 1
        for path, quanti in per_file.most_common(args.max):
            print("  %5d  %s" % (quanti, path))
        if len(per_file) > args.max:
            print("  ... e altri %d file (usare --max)" % (len(per_file) - args.max))
        print("\n  Questi file contengono valori reali per costruzione: sono il layer narrativo")
        print("  locale e gli output degli script, ed è la ragione per cui git li ignora. Il")
        print("  numero serve a sapere che cosa vive sul disco. Diventa un problema solo se uno")
        print("  di questi percorsi venisse tracciato, e in quel caso comparirebbe qui sopra")
        print("  come NON TRACCIATO, cioè fra i bloccanti.")

    print("\n%d file esaminati: %d tracciati, %d non tracciati, %d ignorati." % (
        len(files), conteggio.get("tracciato", 0), conteggio.get("non tracciato", 0),
        conteggio.get("ignorato", 0)))
    if saltati:
        print("%d file saltati perché oltre %d MB." % (len(saltati), LIMITE_BYTE // (1024 * 1024)))
    if not args.tutti:
        print("Layer privato (_notes/, output/) NON esaminato: usare --tutti per contarlo.")
    print("Riscontri bloccanti: %d.  Da valutare a mano: %d.%s" % (
        bloccanti, da_guardare,
        ("  Nel layer privato, non bloccanti: %d." % privati) if args.tutti else ""))
    if bloccanti:
        print("ESITO: FALLITO. Bonificare i riscontri bloccanti prima del commit.")
        return 1
    print("ESITO: pulito sulle categorie bloccanti.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
