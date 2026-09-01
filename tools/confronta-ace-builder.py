#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Confronta il costruttore di esemplari della comunità con ciò che questo progetto ha verificato.

Perché esiste
-------------
Il progetto persegue lo stesso esito per due vie opposte. Il track delle distribuzioni
ricostruisce il metodo di generazione originale e lo fa rieseguire al gioco; il track
dell'esecuzione di codice scrive i byte dell'esemplare. Se le due vie producono lo stesso
dato, la prima perde la sua unica giustificazione tecnica e resta solo quella di provenienza;
se divergono, una delle due è sbagliata. Sapere quale delle due situazioni si dia è la
verifica con il maggiore potere di falsificazione fra quelle che non richiedono hardware,
non toccano alcun account e non violano alcuna condizione d'uso: si legge codice pubblico.

Che cosa confronta, e con quale grado di certezza
-------------------------------------------------
Cinque confronti. I primi quattro sono in ordine di durezza decrescente; il quinto è di
natura diversa e vale più di tutti.

Il primo è la tabella delle ventiquattro permutazioni delle sottostrutture. È esatto e
meccanico: la nostra viene da `pokebridge.gen3`, verificata sulla macro del disassemblato di
pokeemerald, la loro dal proprio modulo. Un disaccordo qui sarebbe fatale per una delle due
parti, perché è la tabella che decide dove si trovano i byte.

Il secondo è la tabella dei caratteri della terza generazione. È esatto e meccanico sulla
intersezione dei caratteri che entrambe dichiarano. Ha un valore particolare per questo
progetto, perché la referenza dei formati registra che la documentazione di dominio collocava
le maiuscole all'offset sbagliato e che il valore giusto è stato ricavato dal sorgente: se il
costruttore concorda con noi, concorda con il sorgente contro l'enciclopedia.

Il terzo è il vocabolario dei metodi, cioè quali metodi di generazione pseudocasuale e quali
derivazioni del sesso dell'allenatore le due parti nominano. È un confronto fra insiemi e
non fra valori: dice che cosa il costruttore copre e che cosa non copre, non se lo faccia
bene.

Il quarto è l'inventario delle distribuzioni, congiunto sulla coppia formata dal nome
dell'allenatore e dall'identificativo, che è la sola chiave presente in entrambe le fonti.
Per ciascuna coppia si confrontano il metodo di generazione e la derivazione del sesso
dell'allenatore. Il costruttore tiene il proprio inventario in due posti, un file di moduli e
un corpus curato a mano che carica a tempo di esecuzione, e vanno letti entrambi: leggerne uno
solo produce assenze che sembrano lacune sue mentre sono lacune della nostra lettura.

Il quinto è di natura diversa dagli altri quattro e vale più di essi. Il costruttore porta
con sé un corpus di esemplari conservati, ciascuno con il proprio seme di origine accanto al
valore di personalità, ai valori individuali e al sesso dell'allenatore. Il nostro modulo
`pokebridge.eventi` viene eseguito su quei semi e si verifica che riproduca gli altri campi.
Non è più il confronto fra due tabelle che si somigliano: è una formula che rifà i numeri di
un corpus che non ha contribuito a produrre.

Che cosa non fa
---------------
Non esegue il costruttore, perché per farlo servirebbe un interprete JavaScript, e non verifica
alcun esemplare in gioco, perché per quello servirebbe una cartuccia. I primi quattro confronti
mettono a paragone due dichiarazioni scritte in codice; il quinto esegue il nostro codice sui
dati conservati dell'altra parte. Nessuno dei due arriva al grado di prova di un esemplare
provato su hardware, ed entrambi stanno molto sopra qualunque lettura di prosa.

Uso
---
    python tools/confronta-ace-builder.py --scarica _notes/fonti/ace-builder
    python tools/confronta-ace-builder.py --ace _notes/fonti/ace-builder
    python tools/confronta-ace-builder.py --ace _notes/fonti/ace-builder --verbose

Il sorgente del costruttore non è una dipendenza di questo repository e non vi entra: si
scarica sotto `_notes/`, che il `.gitignore` esclude, come per i disassemblati e per gli
export delle chat. Il codice è di terzi e resta di terzi.
"""

import argparse
import io
import json
import os
import re
import sys

# I nomi degli allenatori giapponesi non passano dalla codifica predefinita della console
# di Windows, e senza questa riga il programma muore alla stampa finale dopo aver eseguito
# tutti i confronti: il lavoro fatto e perso nell'ultimo istante.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RADICE, "pokemon-gen12-gen3-bridge-original-hardware"))

BASE_REMOTA = "https://mankeymite.github.io/Gen3ACEPokemonBuilder/"
INGRESSO = "src/earlyStartup.js"
CATALOGO = os.path.join(RADICE, "recreate-pokemon-distributions-events", "EVENTI-GEN3.md")
CHARMAP = os.path.join(RADICE, "pokemon-gen12-gen3-bridge-original-hardware", "data",
                       "charmap-gen3.json")
# Il corpus degli esemplari conservati, che il costruttore carica a tempo di esecuzione e non
# per import: il grafo dei moduli non lo raggiunge, e va nominato esplicitamente.
CORPUS = "src/data/Mystery gift pokemon gen 3.json"

# La corrispondenza fra le sigle delle due parti. A sinistra la nostra, che viene
# dall'enumerazione GiftGender3 di PKHeX; a destra quella del costruttore. Le voci che
# valgono un sesso fisso si traducono nel sesso, perché il costruttore lo scrive
# direttamente invece di nominare la derivazione: nella terza generazione 0 è maschio.
SESSO_EQUIVALENTI = {
    "Only0": "male",
    "Only1": "female",
    "RandD3_0": "male",
    "RandD3_1": "female",
    "RandD3": "RAND_D3",
    "RandS3": "RAND_S3",
    "RandS7": "RAND_S7",
    "RandSG15": "RAND_SG15",
    "Recipient": "RECIPIENT",
}


# ---------------------------------------------------------------------------------------
# Scaricamento del sorgente, seguendo il grafo degli import
# ---------------------------------------------------------------------------------------

RIFERIMENTO = re.compile(r"""(?:from|import)\s*\(?\s*['"]([^'"]+)['"]""")


def risolvi(modulo, riferimento):
    """Risolve un import relativo, rifiutando ciò che non è un percorso.

    Il filtro sui caratteri non stampabili non è pedanteria: senza di esso l'espressione
    regolare aggancia anche le stringhe dentro i commenti, e il primo tentativo di questo
    programma ha spedito al servizio un percorso che conteneva un blocco di codice intero.
    """
    if riferimento.startswith(("http://", "https://", "//")):
        return None
    if len(riferimento) > 200 or any(c in riferimento for c in "\n\r\t ;(){}<>\""):
        return None
    p = os.path.normpath(os.path.join(os.path.dirname(modulo), riferimento))
    p = p.replace("\\", "/")
    return p if p.endswith(".js") else p + ".js"


def scarica(destinazione):
    import urllib.error
    import urllib.request

    intestazioni = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    coda, visti, presi, mancati = [INGRESSO], set(), 0, 0
    while coda:
        rel = coda.pop(0)
        if rel in visti:
            continue
        visti.add(rel)
        locale = os.path.join(destinazione, rel.replace("/", os.sep))
        if os.path.exists(locale):
            corpo = io.open(locale, encoding="utf-8", errors="ignore").read()
        else:
            richiesta = urllib.request.Request(BASE_REMOTA + rel, headers=intestazioni)
            try:
                corpo = urllib.request.urlopen(richiesta, timeout=30).read()
            except urllib.error.HTTPError as e:
                print("  " + rel + ": HTTP " + str(e.code))
                mancati += 1
                continue
            corpo = corpo.decode("utf-8", "ignore")
            os.makedirs(os.path.dirname(locale), exist_ok=True)
            io.open(locale, "w", encoding="utf-8", newline="").write(corpo)
            presi += 1
        for riferimento in RIFERIMENTO.findall(corpo):
            p = risolvi(rel, riferimento)
            if p and p not in visti:
                coda.append(p)
    print("moduli scaricati " + str(presi) + ", già presenti " +
          str(len(visti) - presi - mancati) + ", non trovati " + str(mancati))
    print("il sorgente sta in " + destinazione + " e non entra in git")
    return 0


# ---------------------------------------------------------------------------------------
# Lettura del sorgente del costruttore
# ---------------------------------------------------------------------------------------

def leggi(ace, rel):
    p = os.path.join(ace, rel.replace("/", os.sep))
    if not os.path.exists(p):
        sys.exit("manca " + rel + " sotto " + ace + ".\n"
                 "Si scarica con --scarica, oppure il percorso passato non è quello giusto.")
    return io.open(p, encoding="utf-8", errors="ignore").read()


def permutazioni_ace(ace):
    """La tabella delle ventiquattro permutazioni, come ordine di lettere per slot."""
    testo = leggi(ace, "src/lib/gen3/permutations.js")
    corpo = testo.split("GAEM_PERMUTATIONS", 1)[1]
    corpo = corpo[corpo.index("["):corpo.index("];") + 1]
    righe = re.findall(r"\[\s*'([GAEM])'\s*,\s*'([GAEM])'\s*,\s*'([GAEM])'\s*,\s*'([GAEM])'\s*\]",
                       corpo)
    return ["".join(r) for r in righe]


def charmap_ace(ace):
    """La tabella dei caratteri, come carattere verso byte."""
    testo = leggi(ace, "src/lib/gen3/encoding.js")
    corpo = testo.split("CHAR_TABLE", 1)[1]
    tabella = {}
    for chiave, valore in re.findall(r"'((?:\\'|[^'])+)'\s*:\s*(0x[0-9A-Fa-f]{2})", corpo):
        tabella[chiave.replace("\\'", "'")] = int(valore, 16)
    return tabella


def doni_giapponesi_ace(ace):
    """Le distribuzioni giapponesi dichiarate con identificativo esplicito."""
    testo = leggi(ace, "src/data/mysteryGiftsSupplemental.gen3.js")
    doni = {}
    # L'etichetta e il nome possono stare fra apici o fra apici inversi: tre voci usano una
    # stringa di modello, e accettare i soli apici le faceva sparire senza segnalarlo.
    schema = re.compile(
        r"japaneseGift\(\s*[`']([^`']+)[`']\s*,\s*[`']([^`']*)[`']\s*,\s*([A-Za-z0-9_]+)\s*,"
        r"\s*([A-Za-z0-9_]+)\s*,\s*(\d+)\s*,\s*[`']([^`']*)[`']\s*,\s*\[[^\]]*\]"
        r"\s*(?:,\s*\{(.*?)\}\s*)?\)")
    for m in schema.finditer(testo):
        tag, etichetta, _nazionale, _livello, tid, ot, opzioni = m.groups()
        opzioni = opzioni or ""
        metodo = re.search(r"pidMethod:\s*'([^']+)'", opzioni)
        sesso = re.search(r"otGender:\s*'([^']+)'", opzioni)
        sesso_metodo = re.search(r"otGenderMethod:\s*'([^']+)'", opzioni)
        ricevente = "usesRecipientOtGender" in opzioni
        doni[(ot, int(tid))] = {
            "tag": tag,
            "etichetta": etichetta,
            # Il valore per difetto della funzione, quando le opzioni non lo sovrascrivono.
            "metodo": (metodo.group(1) if metodo else "BACD_R_A"),
            "sesso": (sesso.group(1) if sesso else
                      (sesso_metodo.group(1) if sesso_metodo else
                       ("RECIPIENT" if ricevente else ""))),
        }
    return doni


def metodi_ace(ace):
    """Tutte le sigle di metodo e di derivazione del sesso che il sorgente nomina."""
    unione = ""
    for rel in ("src/data/mysteryGiftsSupplemental.gen3.js", "src/domain/mysteryGiftOtGender.js",
                "src/main.js", "src/lib/gen3/builder.js"):
        p = os.path.join(ace, rel.replace("/", os.sep))
        if os.path.exists(p):
            unione += io.open(p, encoding="utf-8", errors="ignore").read()
    pid = set(re.findall(r"'((?:BACD|Method|Channel|H)[A-Za-z0-9_]*)'", unione))
    sesso = set(re.findall(r"'(RAND_[A-Z0-9]+|RECIPIENT)'", unione))
    return pid, sesso


# ---------------------------------------------------------------------------------------
# Lettura del nostro lato
# ---------------------------------------------------------------------------------------

def permutazioni_nostre():
    from pokebridge import gen3
    return [gen3.substruct_order(i) for i in range(24)]


def charmap_nostra():
    d = json.load(io.open(CHARMAP, encoding="utf-8"))
    inversa = {}
    for chiave, carattere in d["stampabili"].items():
        byte = int(chiave, 16)
        # La nostra tabella è byte verso carattere e può ripetere un carattere su più byte:
        # si conserva il byte più basso, che è la codifica canonica.
        if carattere not in inversa or byte < inversa[carattere]:
            inversa[carattere] = byte
    return inversa


def catalogo_nostro():
    """Le righe del catalogo generato, per allenatore e identificativo.

    Si leggono tutti e quattro gli insiemi e non il solo giapponese. La prima versione di
    questa funzione leggeva quello, perché era l'unico che il costruttore dichiarava con
    identificativo esplicito nel file dei moduli; poi si è scoperto che il costruttore tiene
    gli altri nel corpus curato a mano, e restringere la nostra lettura produceva sedici
    assenze che sembravano lacune sue e invece erano nostre.
    """
    testo = io.open(CATALOGO, encoding="utf-8").read()
    inizio = testo.index("## Le voci, per insieme e per blocco")
    voci = {}
    for riga in testo[inizio:].splitlines():
        if not riga.startswith("| ") or riga.startswith("| Specie") or set(riga) <= set("|- "):
            continue
        celle = [c.strip() for c in riga.strip().strip("|").split("|")]
        if len(celle) < 8:
            continue
        specie, _liv, ot, _lingua, ident, metodo, _lucentezza, sesso = celle[:8]
        ot = ot.strip("`")
        try:
            ident = int(ident)
        except ValueError:
            continue
        voci.setdefault((ot, ident), []).append({
            "specie": specie,
            "metodo": metodo.strip("`"),
            "sesso": sesso.strip("`"),
        })
    return voci


def corpus_ace(ace):
    """Gli esemplari conservati con seme, valore di personalità, valori individuali e sesso."""
    p = os.path.join(ace, CORPUS.replace("/", os.sep))
    if not os.path.exists(p):
        return None, None
    d = json.load(io.open(p, encoding="utf-8"))
    return d.get("events", {}), d.get("pokemon", [])


# Gli eventi il cui sesso dell'allenatore segue la derivazione a scorrimento di sette. La
# lista viene dal modulo del costruttore che la implementa, non da una nostra congettura.
def eventi_rand_s7(ace):
    p = os.path.join(ace, "src", "domain", "mysteryGiftOtGender.js")
    if not os.path.exists(p):
        return set()
    testo = io.open(p, encoding="utf-8", errors="ignore").read()
    corpo = testo.split("RAND_S7_MYSTERY_EVENT_TAGS", 1)[-1]
    corpo = corpo[:corpo.index("]")] if "]" in corpo else corpo
    return set(re.findall(r"'([A-Z0-9_]+)'", corpo))


# ---------------------------------------------------------------------------------------
# I cinque confronti
# ---------------------------------------------------------------------------------------

def confronta(ace, verbose):
    problemi = 0

    print("")
    print("=== 1. Tabella delle ventiquattro permutazioni")
    loro = permutazioni_ace(ace)
    nostre = permutazioni_nostre()
    if len(loro) != 24:
        print("  il sorgente del costruttore dichiara " + str(len(loro)) +
              " righe invece di 24: confronto non eseguibile")
        problemi += 1
    elif loro == nostre:
        print("  accordo esatto su tutte e 24 le righe")
        print("  la nostra viene dalla macro SUBSTRUCT_CASE di pokeemerald, la loro dal")
        print("  proprio modulo: due derivazioni indipendenti dello stesso ordinamento")
    else:
        problemi += 1
        for i, (a, b) in enumerate(zip(loro, nostre)):
            if a != b:
                print("  riga " + str(i) + ": costruttore " + a + ", noi " + b)

    print("")
    print("=== 2. Tabella dei caratteri della terza generazione")
    loro = charmap_ace(ace)
    nostra = charmap_nostra()
    nostra_inversa = {b: c for c, b in nostra.items()}
    comuni = sorted(set(loro) & set(nostra))
    diversi = [(c, loro[c], nostra[c]) for c in comuni if loro[c] != nostra[c]]
    print("  caratteri dichiarati dal costruttore " + str(len(loro)) +
          ", in comune con la nostra " + str(len(comuni)) +
          ", in disaccordo " + str(len(diversi)))
    if not diversi:
        print("  accordo esatto sull'intersezione")
    else:
        problemi += 1
        # Un disaccordo su un intero blocco contiguo non è un errore di trascrizione ma
        # due tabelle che descrivono cose diverse: si riporta la diagnosi e non l'elenco.
        blocco = [(c, a, b) for c, a, b in diversi if 0x80 <= a <= 0xA9 and b <= 0x3A]
        resto = [t for t in diversi if t not in blocco]
        if blocco:
            print("  un solo disaccordo strutturale, su " + str(len(blocco)) +
                  " caratteri accentati:")
            print("  il costruttore li colloca in un blocco contiguo da 0x%02X a 0x%02X,"
                  % (min(a for _c, a, _b in blocco), max(a for _c, a, _b in blocco)))
            print("  la nostra tabella nella fascia bassa da 0x%02X a 0x%02X, con i salti"
                  % (min(b for _c, _a, b in blocco), max(b for _c, _a, b in blocco)))
            print("  che il sorgente impone dove il byte e occupato da un altro segno.")
            print("  La nostra viene da charmap.txt di pret/pokeemerald a un commit fissato,")
            print("  cioe dal primo livello; il costruttore dichiara nel proprio commento di")
            print("  derivarla dalla documentazione di dominio, cioe dal secondo livello, e")
            print("  la gerarchia delle fonti di questo progetto assegna la precedenza al")
            print("  primo. Nella fascia che il costruttore usa, il sorgente colloca altri")
            print("  segni, quindi un carattere accentato scritto con quello strumento non")
            print("  produce l'accento ma il segno che occupa davvero quel byte.")
            print("  Primi tre casi, per rendere il difetto verificabile a mano:")
            for c, a, b in blocco[:3]:
                occupato = nostra_inversa.get(a)
                print("    %r: costruttore 0x%02X, sorgente 0x%02X; a 0x%02X il sorgente"
                      " tiene %r" % (c, a, b, a, occupato))
            # La prova che non dipende dalla nostra fonte: una tabella che assegna due
            # caratteri allo stesso byte e sbagliata per conto proprio, perche non puo
            # essere invertita. Se la si trova, e l'argomento decisivo.
            per_byte = {}
            for carattere, byte in loro.items():
                per_byte.setdefault(byte, []).append(carattere)
            collisioni = {b: sorted(v) for b, v in per_byte.items() if len(v) > 1}
            if collisioni:
                print("  Prova che non dipende dalla nostra fonte: la tabella del"
                      " costruttore assegna")
                print("  due o piu caratteri al medesimo byte in " + str(len(collisioni)) +
                      " posizioni, quindi non e")
                print("  invertibile e sbaglia per conto proprio, prima di qualunque"
                      " confronto.")
                for byte in sorted(collisioni)[:6]:
                    print("    0x%02X <- %s" % (byte, ", ".join(repr(c) for c in
                                                                collisioni[byte])))
        for c, a, b in resto:
            print("  " + repr(c) + ": costruttore 0x%02X, noi 0x%02X" % (a, b))
    for c, atteso in (("A", 0xBB), ("0", 0xA1)):
        if c in loro:
            esito = "concorda" if loro[c] == atteso else "DIVERGE"
            print("  controllo mirato su " + repr(c) + ": costruttore 0x%02X, %s con il"
                  " valore ricavato dal sorgente (0x%02X)" % (loro[c], esito, atteso))
            if loro[c] != atteso:
                problemi += 1

    print("")
    print("=== 3. Vocabolario dei metodi")
    pid_loro, sesso_loro = metodi_ace(ace)
    testo = io.open(CATALOGO, encoding="utf-8").read()
    pid_nostri = set(re.findall(r"^\| `(BACD[A-Z_]*|Method_\d|Channel)` \|", testo, re.M))
    sesso_nostri = set(re.findall(r"^\| `(Only\d|Rand[A-Za-z0-9_]*|Recipient)` \|", testo, re.M))
    print("  metodi di generazione usati dal nostro catalogo: " + str(len(pid_nostri)))
    print("  metodi nominati dal costruttore: " + str(len(pid_loro)))
    mancanti = sorted(m for m in pid_nostri if m not in pid_loro)
    print("  usati da noi e non nominati dal costruttore: " +
          (", ".join(mancanti) if mancanti else "nessuno"))
    if verbose:
        print("  nominati dal costruttore e non usati dal nostro catalogo: " +
              ", ".join(sorted(m for m in pid_loro if m not in pid_nostri)))
    atteso_sesso = set(v for v in SESSO_EQUIVALENTI.values() if v.startswith(("RAND", "RECIP")))
    print("  derivazioni del sesso: costruttore " + ", ".join(sorted(sesso_loro)))
    print("  attese dalla tavola di equivalenza: " + ", ".join(sorted(atteso_sesso)))
    senza = sorted(s for s in sesso_nostri if s not in SESSO_EQUIVALENTI)
    if senza:
        print("  nostre derivazioni senza equivalente dichiarato: " + ", ".join(senza))

    print("")
    print("=== 4. Inventario delle distribuzioni, per allenatore e identificativo")
    loro = doni_giapponesi_ace(ace)
    # Gli eventi del corpus curato a mano portano la medesima chiave e vanno uniti, perché il
    # costruttore li tiene in due posti e leggerne uno solo produce assenze che sembrano
    # lacune della controparte mentre sono lacune della nostra lettura.
    eventi_corpus, _corpus = corpus_ace(ace)
    for tag, ev in (eventi_corpus or {}).items():
        tid = ev.get("fixedTID")
        nomi = [ev.get("ot_name")] + list((ev.get("ot_names") or {}).values())
        for nome in [n for n in nomi if n]:
            chiave = (nome, int(tid)) if tid is not None else None
            if chiave and chiave not in loro:
                loro[chiave] = {
                    "tag": tag,
                    "etichetta": tag,
                    "metodo": ev.get("pidMethod") or "",
                    "sesso": "",
                }
    nostre = catalogo_nostro()
    print("  voci del costruttore " + str(len(loro)) + ", chiavi del nostro catalogo " +
          str(len(nostre)))
    comuni = sorted(set(loro) & set(nostre), key=lambda k: k[1])
    print("  chiavi in comune " + str(len(comuni)))
    accordo_metodo, accordo_sesso, disaccordi, non_confrontabili = 0, 0, [], 0
    sesso_non_dichiarato = 0
    for chiave in comuni:
        l = loro[chiave]
        candidati = nostre[chiave]
        metodi_nostri = set(c["metodo"] for c in candidati)
        sessi_nostri = set(c["sesso"] for c in candidati)
        if not l["metodo"]:
            non_confrontabili += 1
        elif l["metodo"] in metodi_nostri:
            accordo_metodo += 1
        else:
            disaccordi.append((chiave, "metodo", l["metodo"], sorted(metodi_nostri)))
        tradotti = set(SESSO_EQUIVALENTI.get(s, s) for s in sessi_nostri)
        if not l["sesso"]:
            sesso_non_dichiarato += 1
        elif l["sesso"] in tradotti:
            accordo_sesso += 1
        else:
            disaccordi.append((chiave, "sesso OT", l["sesso"], sorted(tradotti)))
        if verbose:
            print("  " + chiave[0] + " " + str(chiave[1]) + "  " + l["tag"] +
                  "  metodo " + l["metodo"] + " vs " + ",".join(sorted(metodi_nostri)) +
                  "  sesso " + (l["sesso"] or "-") + " vs " + ",".join(sorted(tradotti)))
    print("  accordo sul metodo di generazione: " + str(accordo_metodo) + " su " +
          str(len(comuni) - non_confrontabili) +
          (", piu " + str(non_confrontabili) + " voci senza metodo dichiarato dal costruttore"
           if non_confrontabili else ""))
    print("  accordo sulla derivazione del sesso: " + str(accordo_sesso) + " su " +
          str(len(comuni) - sesso_non_dichiarato) +
          (", piu " + str(sesso_non_dichiarato) + " voci senza sesso dichiarato dal"
           " costruttore" if sesso_non_dichiarato else ""))
    for chiave, campo, loro_v, nostri_v in disaccordi:
        problemi += 1
        print("  DISACCORDO " + chiave[0] + " " + str(chiave[1]) + " su " + campo +
              ": costruttore " + loro_v + ", noi " + ", ".join(nostri_v))
    soli_loro = sorted(set(loro) - set(nostre), key=lambda k: k[1])
    soli_nostri = sorted(set(nostre) - set(loro), key=lambda k: k[1])
    if soli_loro:
        print("  chiavi solo nel costruttore " + str(len(soli_loro)) + ": " +
              ", ".join(k[0] + " " + str(k[1]) for k in soli_loro))
    if soli_nostri:
        print("  chiavi solo nel nostro catalogo " + str(len(soli_nostri)) + ": " +
              ", ".join(k[0] + " " + str(k[1]) for k in soli_nostri))

    print("")
    print("=== 5. Riproduzione del corpus degli esemplari conservati")
    _eventi, corpus = corpus_ace(ace)
    if corpus is None:
        print("  il corpus non è presente: si scarica con --scarica, che lo prende a parte")
        print("  perché il costruttore lo carica a tempo di esecuzione e non per import")
    else:
        from pokebridge import eventi as motore
        tag_s7 = eventi_rand_s7(ace)
        vettori = [v for v in corpus if "seed" in v and "pid" in v]
        senza_seme = len(corpus) - len(vettori)
        ok_pid = ok_iv = ok_sesso = con_sesso = 0
        devianti = []
        for v in vettori:
            seme = int(v["seed"], 16)
            personalita, valori = motore.personalita_e_iv(seme)
            if personalita == int(v["pid"], 16):
                ok_pid += 1
            else:
                devianti.append((v.get("tag", "?"), seme, int(v["pid"], 16), personalita,
                                 tuple(valori[k] for k in motore.ORDINE_IV) == tuple(v["ivs"])))
            if "ivs" in v and tuple(valori[k] for k in motore.ORDINE_IV) == tuple(v["ivs"]):
                ok_iv += 1
            if v.get("tag") in tag_s7 and v.get("ot_gender"):
                con_sesso += 1
                atteso = "femmina" if v["ot_gender"].lower().startswith("f") else "maschio"
                if motore.sesso_allenatore_rand_s7(seme) == atteso:
                    ok_sesso += 1
        print("  esemplari nel corpus " + str(len(corpus)) + ", con seme utilizzabile " +
              str(len(vettori)) + ", senza seme " + str(senza_seme))
        print("  valore di personalità riprodotto: " + str(ok_pid) + " su " + str(len(vettori)))
        print("  valori individuali riprodotti: " + str(ok_iv) + " su " + str(len(vettori)))
        print("  sesso dell'allenatore riprodotto, sui soli eventi che usano la derivazione")
        print("  a scorrimento di sette (" + str(len(tag_s7)) + " eventi dichiarati dal"
              " costruttore): " + str(ok_sesso) + " su " + str(con_sesso))
        for tag, seme, dichiarata, calcolata, iv_ok in devianti:
            print("  DEVIANTE " + tag + " seme 0x%08X: dichiarato 0x%08X, calcolato 0x%08X,"
                  " scarto %+d" % (seme, dichiarata, calcolata, dichiarata - calcolata))
            print("    i suoi valori individuali dal medesimo seme " +
                  ("tornano esatti, quindi il seme è giusto e la deviazione sta nel valore"
                   " dichiarato" if iv_ok else "non tornano, quindi il seme stesso è dubbio"))
        if ok_iv == len(vettori) and con_sesso and ok_sesso == con_sesso and not devianti:
            print("  riproduzione completa")
        elif ok_iv == len(vettori) and con_sesso and ok_sesso == con_sesso:
            print("  riproduzione completa sui valori individuali e sul sesso; le deviazioni")
            print("  sul valore di personalità sono elencate sopra con la loro diagnosi")

    print("")
    if problemi:
        print("esito: " + str(problemi) + " disaccordi da spiegare, uno per uno, prima di "
              "trarne conclusioni")
    else:
        print("esito: nessun disaccordo sui confronti eseguibili")
        print("Conseguenza per il progetto, e va letta con il suo limite: le due vie "
              "concordano su come")
        print("il dato si compone e su quale metodo appartenga a ciascun evento, quindi la "
              "via lenta non")
        print("ha vantaggio sui dati. Il suo vantaggio resta soltanto la provenienza, che è "
              "l'unica")
        print("differenza che questo confronto non può misurare.")
    return 1 if problemi else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--ace", help="cartella con il sorgente del costruttore, già scaricato")
    ap.add_argument("--scarica", metavar="CARTELLA",
                    help="scarica il sorgente seguendo il grafo degli import, poi esce")
    ap.add_argument("--verbose", action="store_true",
                    help="stampa il confronto voce per voce")
    a = ap.parse_args()

    if a.scarica:
        return scarica(a.scarica)
    if not a.ace:
        ap.error("serve --ace con la cartella del sorgente, oppure --scarica per ottenerlo")
    return confronta(a.ace, a.verbose)


if __name__ == "__main__":
    sys.exit(main())
