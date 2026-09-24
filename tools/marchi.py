#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Enumera l'asse dei marchi e dichiara, per ciascuno, da dove viene e se la scadenza lo tocchi.

Perché esiste
-------------
Il progetto conosceva l'asse dei fiocchi e non quello dei marchi, e la differenza fra i due non
era stata vista perché il formato li tiene nello stesso posto: un marchio è un bit dentro la
stessa regione di byte che ospita i fiocchi, e chi guarda i byte non vede alcun confine. Il
confine però esiste ed è di significato, non di rappresentazione. Un fiocco si conferisce per un
merito, cioè per qualcosa che il giocatore ha fatto, e chi lo insegue ripete un'impresa. Un
marchio si conferisce per una circostanza dell'incontro, cioè per qualcosa che era vero nel
momento in cui l'esemplare è stato trovato, e chi lo insegue aspetta che quella circostanza si
ripresenti oppure scopre che non si ripresenterà mai.

Tre fonti del lotto di lettura del 2026-09-12 hanno reso l'asse impossibile da ignorare. Le prime
due sono le pagine di Serebii sui Pokemon titanici e sugli incontri a cristallo nero, che
descrivono due marchi conferiti da incontri irripetibili, il secondo dei quali è legato a una
settimana di calendario e conta novantuno edizioni. La terza è la pagina dei titoli di Pokemon
Champions, dove gli stessi marchi compaiono sotto un altro nome perché quel gioco non li disegna,
e dove sta anche l'avvertenza che un esemplare che vi guadagni il titolo di rango non torna
indietro attraverso il deposito.

Perché si legge dal formato del deposito
-----------------------------------------
La collezione di questo progetto vive nel deposito, quindi la domanda su che cosa sia un marchio
va posta al formato del deposito e non a quello di un gioco. Il programma legge perciò
`PKHeX.Core/PKM/HOME/GameDataCore.cs`, che è la rappresentazione che il verificatore dà del dato
conservato dal servizio, e ne estrae le posizioni invece di trascriverle. Vale qui la stessa
ragione di `tools/fiocchi.py`: una trascrizione lunga sbaglia in un modo che nessun controllo
interno rivela, perché un bit letto nella posizione sbagliata restituisce comunque un booleano
plausibile.

Che cosa la misura dice, e che cosa non dice
---------------------------------------------
Dice quanti marchi esistano, come si raggruppino per circostanza, e quali appartengano
all'insieme introdotto dalla nona generazione contro quello nato con l'ottava.

Non dice quanti dei nostri esemplari ne portino, e la ragione va detta perché è un limite e non
una dimenticanza: i lotti di questo progetto arrivano alla quinta generazione, dove le posizioni
dei marchi non esistono affatto e i medesimi byte appartengono ad altri campi. Misurarvi sopra la
copertura darebbe un numero plausibile e privo di senso, che è precisamente il difetto contro cui
il resto di questo programma è scritto. La copertura si misura quindi soltanto su file del formato
del deposito, che si passano con `--lotti`, e in loro assenza non si misura.

Non dice quante voci di collezione l'asse produca, e la distinzione è la stessa che il progetto
ha già fissato per i cromatici e per le sfere: un marchio non si moltiplica per le specie, si
misura. Un marchio meteorologico è comune e si riottiene aspettando il tempo giusto; il marchio
del titano appartiene a sei incontri e basta; il marchio del più forte appartiene a una lista di
edizioni chiuse che va contata sulla fonte e non dedotta dal bit.

Uso
---
    python tools/marchi.py --pkhex <clone>
    python tools/marchi.py --pkhex <clone> --out pokedex-home-completo/MARCHI.md
    python tools/marchi.py --self-test
"""

import argparse
import collections
import glob
import io
import os
import re
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CORE_HOME = os.path.join("PKHeX.Core", "PKM", "HOME", "GameDataCore.cs")
VERIFICATORE_9 = os.path.join("PKHeX.Core", "Legality", "Verifiers", "Ribbons",
                              "RibbonVerifierMark9.cs")
TESTI = os.path.join("PKHeX.Core", "Resources", "text", "other", "en", "text_Ribbons_en.txt")

RE_MARCHIO = re.compile(
    r"public bool (RibbonMark\w+)\s*\{\s*get => GetFlag\((0x[0-9A-Fa-f]+),\s*(\d+)\)")
RE_SEGNALATO_9 = re.compile(r"list\.Add\((Mark[A-Za-z0-9]+)")

# Le famiglie in cui i marchi si raggruppano per circostanza dell'incontro. Non vengono dal
# sorgente, che non le nomina, ma dal significato, e per questo stanno qui dichiarate invece di
# essere dedotte: dedurle da un prefisso del nome darebbe raggruppamenti sbagliati, perché per
# esempio il marchio nebbioso e quello del destino sono vicini nei bit e lontanissimi nel senso.
# L'ordine conta, perché una chiave si assegna alla prima famiglia che la contiene.
FAMIGLIE = [
    ("momento del giorno", ["Lunchtime", "SleepyTime", "Dusk", "Dawn"]),
    ("tempo atmosferico", ["Cloudy", "Rainy", "Stormy", "Snowy", "Blizzard", "Dry", "Sandstorm",
                           "Misty"]),
    ("modo della cattura", ["Fishing", "Curry", "Destiny", "Itemfinder", "Gourmand", "Partner"]),
    ("rarità dell'incontro", ["Uncommon", "Rare", "Alpha", "Mightiest", "Titan"]),
    ("taglia dell'esemplare", ["Jumbo", "Mini"]),
]
# Tutto cio che resta appartiene alla famiglia dell'indole, che è la più numerosa e la sola in cui
# il marchio non dice nulla dell'incontro ma dell'esemplare: per questo si definisce per
# differenza invece che per elenco, così un marchio nuovo di un gioco futuro vi finisce da sé
# invece di sparire da ogni conto.
FAMIGLIA_RESIDUA = "indole dell'esemplare"

# Le estensioni dei formati in cui queste posizioni hanno il significato che questo programma dà
# loro. Sono quelle dell'ottava generazione in avanti più il formato proprio del deposito: fuori
# da questo insieme gli stessi byte appartengono ad altri campi, e leggerli produrrebbe marchi
# che nessun esemplare porta.
FORMATI_DEPOSITO = ("ph1", "pk8", "pa8", "pb8", "pk9")


def carica(pkhex, relativo):
    percorso = os.path.join(pkhex, relativo)
    if not os.path.exists(percorso):
        sys.exit("manca " + relativo + " sotto " + pkhex + ": il clone non porta la parte che "
                 "serve, e questo programma non inventa le posizioni dei bit")
    return io.open(percorso, encoding="utf-8-sig").read()


def marchi(pkhex):
    """Dal nome del marchio alla coppia byte e bit, letta dal formato del deposito."""
    testo = carica(pkhex, CORE_HOME)
    fuori = {}
    for nome, byte, bit in RE_MARCHIO.findall(testo):
        fuori[nome] = (int(byte, 16), int(bit))
    if len(fuori) < 20:
        sys.exit("letti soltanto " + str(len(fuori)) + " marchi: la forma del sorgente è "
                 "cambiata e l'estrazione va rifatta, invece di proseguire su un elenco monco")
    return fuori


def insieme_nona(pkhex):
    """I marchi che il verificatore della nona generazione tratta a parte.

    Sono quelli introdotti dopo l'ottava, e la distinzione conta perché è l'unica che il sorgente
    dichiari da sé: tutti gli altri appartengono all'insieme nato con Spada e Scudo.
    """
    testo = carica(pkhex, VERIFICATORE_9)
    return set("Ribbon" + n for n in RE_SEGNALATO_9.findall(testo))


def nomi_umani(pkhex):
    fuori = {}
    for riga in carica(pkhex, TESTI).splitlines():
        if "\t" in riga:
            chiave, nome = riga.split("\t", 1)
            fuori[chiave.strip()] = nome.strip()
    return fuori


def famiglia(chiave):
    corto = chiave[len("RibbonMark"):]
    for nome, membri in FAMIGLIE:
        if corto in membri:
            return nome
    return FAMIGLIA_RESIDUA


def portati(percorsi, posizioni):
    """Quanti esemplari, fra quelli in formato del deposito, portino ciascun marchio.

    Il vincolo sul formato non è un dettaglio ed è costato una stesura. La prima versione di
    questo programma puntava le posizioni del deposito contro i file dei nostri lotti, che sono di
    generazioni dalla prima alla quinta, e riferiva quattordicimilacinquecentosettantotto marchi
    accesi su millequattrocentottantasette esemplari. Il numero non era un errore di conteggio ma
    qualcosa di peggiore: era la lettura di byte che in quei formati significano altro, cioè punti
    esperienza, valori individuali e bandierine di sistema, interpretati come marchi perché
    nessuno vietava di farlo. Un offset applicato al formato sbagliato non produce un rifiuto:
    produce un booleano plausibile per ogni bit che incontra.

    Ne segue la regola che questo programma applica: la copertura si misura sui soli file del
    formato del deposito, e in assenza di essi non si misura affatto, dichiarandolo. Zero
    esemplari esaminati è un'informazione onesta; un conto su file del formato sbagliato non lo è.
    """
    conto = collections.Counter()
    quanti = 0
    for percorso in percorsi:
        dato = open(percorso, "rb").read()
        quanti += 1
        for nome, (byte, bit) in posizioni.items():
            if byte < len(dato) and (dato[byte] & (1 << bit)):
                conto[nome] += 1
    return conto, quanti


def scrivi(posizioni, nona, nomi, conto, quanti):
    byte_distinti = len(set(b for b, _ in posizioni.values()))
    righe = []
    righe.append("# L'asse dei marchi: enumerazione, famiglie e rapporto con la scadenza")
    righe.append("")
    righe.append("> Documento generato da `tools/marchi.py`. Non si modifica a mano: si rigenera. "
                 "Le posizioni dei bit sono lette dal formato del deposito e non trascritte, per "
                 "la ragione già pagata due volte da questo progetto su tabelle lunghe.")
    righe.append("")
    righe.append("Il formato del deposito dichiara " + str(len(posizioni)) + " marchi distinti, "
                 "distribuiti su " + str(byte_distinti) + " byte dell'esemplare. Un marchio non è "
                 "un fiocco, e la differenza è di significato e non di rappresentazione, perché "
                 "i due vivono nella stessa regione di byte e chi guarda i byte non vede alcun "
                 "confine: un fiocco si conferisce per un merito, cioè per qualcosa che il "
                 "giocatore ha fatto e che può rifare, mentre un marchio si conferisce per una "
                 "circostanza dell'incontro, cioè per qualcosa che era vero nel momento in cui "
                 "l'esemplare è stato trovato.")
    righe.append("")
    righe.append("Va detto subito ciò che questa misura non dice, perché è la domanda che "
                 "verrà subito dopo. Non dice quante voci di collezione l'asse produca: un "
                 "marchio non si moltiplica per le specie, si misura, come il progetto ha già "
                 "stabilito per i cromatici e per le sfere. Un marchio meteorologico è comune e "
                 "si riottiene aspettando il tempo giusto; quello del titano appartiene a sei "
                 "incontri e basta; quello del più forte appartiene a una lista di edizioni "
                 "chiuse che va contata sulla fonte e non dedotta dal bit.")
    righe.append("")
    righe.append("## Il rapporto con la scadenza, che è il risultato principale")
    righe.append("")
    righe.append("Nessun marchio è sotto la scadenza del 26 febbraio 2027, e la ragione è "
                 "strutturale invece che fortunata: i marchi nascono con l'ottava generazione e "
                 "vivono nell'ottava e nella nona, che sono titoli per console corrente e parlano "
                 "al deposito per via diretta. La chiusura della banca non tocca alcuna via che "
                 "li conferisca. L'asse allarga quindi l'ampiezza della collezione e non la sua "
                 "urgenza, e va pianificato dopo ciò che scade.")
    righe.append("")
    righe.append("Ne discende anche il verso opposto, e va enunciato perché è il difetto tipico "
                 "di un asse nuovo: la copertura di questo asse sui nostri lotti non è zero, è "
                 "indefinita. I lotti arrivano alla quinta generazione, dove queste posizioni non "
                 "esistono e i medesimi byte appartengono ad altri campi, quindi puntarvele "
                 "contro non darebbe una misura bassa ma una misura priva di senso. La prima "
                 "stesura di questo programma lo ha fatto e ha riferito quattordicimila marchi "
                 "accesi su millequattrocentottantasette esemplari, che è esattamente il genere "
                 "di numero plausibile e sbagliato contro cui il resto del programma è scritto. "
                 "La colonna della copertura conta perciò soltanto file del formato del "
                 "deposito, e in loro assenza riporta zero esemplari esaminati.")
    righe.append("")
    righe.append("## Le famiglie")
    righe.append("")
    righe.append("| Famiglia | Marchi | Di cui dell'insieme della nona |")
    righe.append("|---|---|---|")
    per_famiglia = collections.Counter()
    nona_famiglia = collections.Counter()
    for chiave in posizioni:
        f = famiglia(chiave)
        per_famiglia[f] += 1
        if chiave in nona:
            nona_famiglia[f] += 1
    ordine = [n for n, _ in FAMIGLIE] + [FAMIGLIA_RESIDUA]
    for f in ordine:
        if per_famiglia[f]:
            righe.append("| " + f + " | " + str(per_famiglia[f]) + " | " +
                         str(nona_famiglia[f]) + " |")
    righe.append("| totale | " + str(sum(per_famiglia.values())) + " | " +
                 str(sum(nona_famiglia.values())) + " |")
    righe.append("")
    righe.append("## L'elenco, con la posizione nel formato del deposito")
    righe.append("")
    righe.append("La colonna dell'insieme dice se il marchio appartenga a quello che il "
                 "verificatore della nona generazione tratta a parte, cioè i marchi nati dopo "
                 "Spada e Scudo, oppure all'insieme originario. La colonna della copertura conta "
                 "gli esemplari dei nostri lotti che lo portano, su " + str(quanti) +
                 " esaminati.")
    righe.append("")
    righe.append("| Marchio | Chiave | Byte | Bit | Famiglia | Insieme | Nei lotti |")
    righe.append("|---|---|---|---|---|---|---|")
    for chiave, (byte, bit) in sorted(posizioni.items(), key=lambda v: (v[1][0], v[1][1])):
        righe.append("| " + nomi.get(chiave, "(senza nome nella tabella)") + " | " + chiave +
                     " | 0x%02X" % byte + " | " + str(bit) + " | " + famiglia(chiave) + " | " +
                     ("nona" if chiave in nona else "ottava") + " | " +
                     str(conto.get(chiave, 0)) + " |")
    righe.append("")
    righe.append("## Che cosa resta da misurare, e su quale fonte")
    righe.append("")
    righe.append("Il marchio del titano appartiene a sei incontri dichiarati da Serebii, cioè "
                 "Klawf, Bombirdier, Orthworm, la coppia fra Great Tusk e Iron Treads secondo la "
                 "versione, e Tatsugiri, tutti con altezza e peso al massimo e trenta in ogni "
                 "valore individuale. Il marchio del più forte appartiene invece agli incontri a "
                 "cristallo nero, che sulla stessa fonte contano novantuno edizioni di cui una "
                 "parte non lo conferisce: il conto esatto va fatto sulla pagina e non stimato, "
                 "ed è lavoro dichiarato in `pending.md`.")
    righe.append("")
    righe.append("Resta infine da chiarire una cosa che nessuna delle due fonti dice e che "
                 "riguarda il deposito, cioè se un marchio sopravviva al passaggio attraverso il "
                 "deposito in entrambi i versi. Per il timbro della banca il progetto ha già una "
                 "tensione aperta sulla rimozione permanente all'uscita, e la pagina dei titoli "
                 "di Pokemon Champions ne aggiunge una seconda, perché dichiara che un esemplare "
                 "che vi guadagni il titolo di rango non torna indietro attraverso il deposito.")
    righe.append("")
    return "\n".join(righe)


def collaudo():
    esiti = []

    def prova(nome, condizione):
        esiti.append((nome, bool(condizione)))

    finto_core = (
        '    public bool RibbonMarkLunchtime { get => GetFlag(0x36, 5); set => x; }\n'
        '    public bool RibbonMarkCloudy { get => GetFlag(0x37, 1); set => x; }\n'
        '    public bool RibbonMarkTitan { get => GetFlag(0x3F, 5); set => x; }\n'
        '    public int RibbonMarkCount => BitOperations.PopCount(x);\n'
        '    public bool RibbonChampionKalos { get => GetFlag(0x34, 0); set => x; }\n')
    trovati = dict((n, (int(b, 16), int(i))) for n, b, i in RE_MARCHIO.findall(finto_core))
    prova("si leggono i marchi con byte e bit", trovati.get("RibbonMarkTitan") == (0x3F, 5))
    prova("negativo: il conteggio dei marchi non e' un marchio, perche' non e' un booleano",
          "RibbonMarkCount" not in trovati)
    prova("negativo: un fiocco che non e' un marchio resta fuori",
          "RibbonChampionKalos" not in trovati)

    prova("una chiave si assegna alla famiglia che la contiene",
          famiglia("RibbonMarkBlizzard") == "tempo atmosferico" and
          famiglia("RibbonMarkTitan") == "rarità dell'incontro")
    prova("una chiave che nessuna famiglia elenca finisce nella residua, invece di sparire",
          famiglia("RibbonMarkInventatoDaUnGiocoFuturo") == FAMIGLIA_RESIDUA)
    prova("negativo: il marchio nebbioso e quello del destino non finiscono nella stessa "
          "famiglia benche' siano adiacenti nei bit",
          famiglia("RibbonMarkMisty") != famiglia("RibbonMarkDestiny"))

    finto_verificatore = (
        '        if (r.RibbonMarkGourmand) list.Add(MarkGourmand);\n'
        '        if (r.RibbonMarkTitan) list.Add(MarkTitan, !r.RibbonMarkTitan);\n')
    nona = set("Ribbon" + n for n in RE_SEGNALATO_9.findall(finto_verificatore))
    prova("l'insieme della nona si legge dal verificatore che lo dichiara",
          nona == set(["RibbonMarkGourmand", "RibbonMarkTitan"]))

    import tempfile
    cartella = tempfile.mkdtemp(prefix="marchi-collaudo-")
    percorso = os.path.join(cartella, "esemplare.bin")
    dato = bytearray(0x50)
    dato[0x37] |= 1 << 1
    open(percorso, "wb").write(bytes(dato))
    conto, quanti = portati([percorso], {"RibbonMarkCloudy": (0x37, 1),
                                         "RibbonMarkTitan": (0x3F, 5)})
    prova("un marchio acceso si conta", conto.get("RibbonMarkCloudy") == 1 and quanti == 1)
    prova("negativo: un marchio spento non si conta", conto.get("RibbonMarkTitan", 0) == 0)
    corto = os.path.join(cartella, "corto.bin")
    open(corto, "wb").write(b"\x00" * 4)
    conto2, _ = portati([corto], {"RibbonMarkTitan": (0x3F, 5)})
    prova("negativo: un file piu' corto della posizione non produce un errore ne' un falso "
          "positivo", conto2.get("RibbonMarkTitan", 0) == 0)

    testo = scrivi({"RibbonMarkCloudy": (0x37, 1), "RibbonMarkTitan": (0x3F, 5)},
                   set(["RibbonMarkTitan"]), {"RibbonMarkCloudy": "Cloudy Mark"}, conto, 1)
    prova("il documento dichiara il rapporto con la scadenza", "26 febbraio 2027" in testo)
    prova("il documento distingue i due insiemi", "| nona |" in testo and "| ottava |" in testo)
    prova("un marchio senza nome umano non fa saltare la scrittura",
          "(senza nome nella tabella)" in testo)

    falliti = [n for n, e in esiti if not e]
    for nome, esito in esiti:
        print(("  ok   " if esito else "  FALLITO ") + nome)
    print("")
    print(str(len(esiti) - len(falliti)) + " prove, " + str(len(falliti)) + " fallite.")
    return 1 if falliti else 0


def principale(argomenti=None):
    p = argparse.ArgumentParser(description="Enumera l'asse dei marchi dal formato del deposito.")
    p.add_argument("--pkhex", default=os.path.join(RADICE, "_notes", "fonti", "cloni", "pkhex"))
    p.add_argument("--lotti", nargs="*", default=None,
                   help="cartelle dei lotti su cui misurare la copertura")
    p.add_argument("--out", default=None)
    p.add_argument("--check", action="store_true",
                   help="non riscrive: dice se il documento sia ancora allineato alla fonte")
    p.add_argument("--self-test", action="store_true")
    a = p.parse_args(argomenti)
    if a.self_test:
        return collaudo()

    posizioni = marchi(a.pkhex)
    nona = insieme_nona(a.pkhex)
    nomi = nomi_umani(a.pkhex)
    # Nessun lotto per difetto, e la ragione sta nel docstring di `portati`: i nostri lotti sono
    # di generazioni dalla prima alla quinta, dove queste posizioni non significano nulla. Chi
    # voglia misurare la copertura passa `--lotti` con cartelle di file in formato del deposito.
    cartelle = a.lotti if a.lotti is not None else []
    percorsi = []
    for cartella in cartelle:
        for estensione in FORMATI_DEPOSITO:
            percorsi.extend(glob.glob(os.path.join(cartella, "**", "*." + estensione),
                                      recursive=True))
    conto, quanti = portati(percorsi, posizioni)
    testo = scrivi(posizioni, nona, nomi, conto, quanti)

    if a.check:
        if not a.out or not os.path.exists(a.out):
            print("nessun documento da confrontare")
            return 1
        attuale = io.open(a.out, encoding="utf-8").read()
        if attuale.strip() == testo.strip():
            print("allineato")
            return 0
        print("il documento non e' allineato alla fonte: rigenerare")
        return 1

    if a.out:
        io.open(a.out, "w", encoding="utf-8", newline="\n").write(testo + "\n")
        print(str(len(posizioni)) + " marchi, di cui " + str(len(nona)) +
              " dell'insieme della nona, scritti in " + a.out)
        print(str(quanti) + " esemplari dei lotti esaminati, " + str(sum(conto.values())) +
              " marchi accesi trovati")
    else:
        print(testo)
    return 0


if __name__ == "__main__":
    sys.exit(principale())
