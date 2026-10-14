#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Comprime gli export di chat conservando la prova che il contenuto non è cambiato.

Perché esiste
--------------
Gli export di DiscordChatExporter sotto `_notes/fonti/discord/dce/` sono fonti non
recuperabili: il canale da cui vengono non si riscarica, e `_notes/` è fuori da git, quindi
nessun commit li protegge. Pesano però venti volte più del loro contenuto, perché il formato
riserializza su ogni messaggio la scheda completa dell'autore, l'indirizzo del suo avatar e
cinque liste vuote. La misura è in `.claude/context/refactor-10-export-discord-compressi.md`.

Comprimerli è l'intervento ovvio, ma su una fonte non recuperabile l'intervento ovvio è anche
quello che non si può sbagliare: se la compressione perde un byte, non esiste l'originale da
cui riprovare. Questo strumento esiste per rendere quella perdita impossibile da non vedere.
Prende l'impronta di ogni file prima di toccarlo, comprime lasciando l'originale al suo posto,
rilegge il compresso decomprimendolo e confronta l'impronta. L'originale si cancella solo dopo
che il confronto è tornato uguale, e solo se lo si chiede con un'opzione apposita.

Il modo `verifica` si può rilanciare in qualsiasi momento, anche fra un anno e senza di me:
rilegge ogni file compresso, ne ricalcola l'impronta del contenuto decompresso e la confronta
con il manifesto. È la prova che la cartella contiene ancora, bit per bit, ciò che conteneva il
giorno della compressione.

Perché gzip e non zstd
----------------------
zstd comprime meglio, e il divario misurato su questa stessa cartella non è piccolo: 119 MB
contro i 186 ottenuti da gzip al livello 9, cioè oltre il cinquanta per cento in più. Non è
stato scelto perché Python 3.13, cioè l'interprete di questa macchina, non ha un modulo per
leggerlo: né `zstandard`, che è un pacchetto da installare, né `compression.zstd`, che entra
nella libreria standard solo con Python 3.14. Leggere un export compresso con zstd richiederebbe
quindi il binario esterno `zstd` presente nel PATH, cioè una dipendenza fuori dal repository per
aprire una fonte che il repository stesso dichiara non recuperabile. I sessantasette megabyte
risparmiati non valgono quel vincolo, visto che si parte da duemilacinquecentottanta.

Uso
---
    python tools/verifica-integrita-export.py manifesto _notes/fonti/discord/dce
    python tools/verifica-integrita-export.py comprimi _notes/fonti/discord/dce
    python tools/verifica-integrita-export.py verifica _notes/fonti/discord/dce
    python tools/verifica-integrita-export.py verifica _notes/fonti/discord/dce --elimina-originali

I quattro passi vanno eseguiti in quest'ordine e il quarto una volta sola, perché è l'unico che
distrugge: cancella gli originali, e lo fa soltanto se la verifica che lo precede nella stessa
esecuzione è risultata verde su ogni file della cartella.

Il codice di uscita è 0 se ogni impronta corrisponde, 1 se almeno una non corrisponde, 2 se
l'invocazione è malformata o il manifesto manca. Un codice diverso da 0 va trattato come perdita
di dati finché non è spiegato.
"""

import argparse
import gzip
import hashlib
import io
import os
import sys
import time

# I canali esportati da MankeyMite hanno l'emoji nel nome del file, perché Discord la ammette
# nel nome del canale. Senza questa riga la stampa di quei nomi muore con UnicodeEncodeError:
# la console di Windows apre in cp1252, che non ha un punto di codice per un trofeo. Il
# manifesto si scrive comunque in UTF-8, quindi il difetto era di sola presentazione, ma
# fermava lo strumento a metà lavoro, che su una cartella da duemila file non è accettabile.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

# Si comprimono solo gli export veri e propri. I `.md` estratti a mano e i `.txt` di servizio
# restano in chiaro: sono piccoli, si leggono spesso e si cercano con grep senza passaggi.
ESTENSIONI = (".json", ".parziale")

NOME_MANIFESTO = "MANIFEST-integrita.txt"

BLOCCO = 1024 * 1024

# Sotto questa soglia un export resta in chiaro. Non è una soglia di efficienza ma di utilità:
# su un file di mezzo megabyte la compressione risparmia qualche centinaio di kilobyte, che su
# una cartella da due gigabyte non si vedono, mentre il file in chiaro si apre con un editor e
# si cerca con grep senza passaggi intermedi. I file piccoli restano comunque nel manifesto e
# la verifica controlla anche loro, confrontando l'impronta del file così com'è.
SOGLIA = 1024 * 1024


def impronta_flusso(fh):
    """Ritorna (sha256 esadecimale, byte letti) consumando il flusso a blocchi.

    Si legge a blocchi e non in una volta sola perché il file più grande di questa cartella è di
    444 MB: caricarlo intero per prenderne l'impronta sprecherebbe memoria senza alcun guadagno.
    """
    h = hashlib.sha256()
    n = 0
    while True:
        b = fh.read(BLOCCO)
        if not b:
            break
        h.update(b)
        n += len(b)
    return h.hexdigest(), n


def impronta_file(path):
    with io.open(path, "rb") as fh:
        return impronta_flusso(fh)


def impronta_compresso(path):
    """Impronta del contenuto *decompresso*, che è ciò che va confrontato con l'originale."""
    with gzip.open(path, "rb") as fh:
        return impronta_flusso(fh)


def elenca(cartella):
    """Tutti gli export non compressi sotto la cartella, ricorsivamente, in ordine stabile."""
    trovati = []
    for radice, _dirs, files in os.walk(cartella):
        for nome in files:
            if nome.endswith(ESTENSIONI):
                trovati.append(os.path.join(radice, nome))
    return sorted(trovati)


def elenca_compressi(cartella):
    trovati = []
    for radice, _dirs, files in os.walk(cartella):
        for nome in files:
            if nome.endswith(".gz") and nome[:-3].endswith(ESTENSIONI):
                trovati.append(os.path.join(radice, nome))
    return sorted(trovati)


def rel(cartella, path):
    """Percorso relativo alla cartella, con barre in avanti, così il manifesto è portabile."""
    return os.path.relpath(path, cartella).replace(os.sep, "/")


def leggi_manifesto(path):
    """Ritorna {nome relativo: (sha256, dimensione)}; le righe di commento iniziano con #."""
    voci = {}
    with io.open(path, encoding="utf-8") as fh:
        for riga in fh:
            riga = riga.strip()
            if not riga or riga.startswith("#"):
                continue
            parti = riga.split(None, 2)
            if len(parti) != 3:
                continue
            voci[parti[2]] = (parti[0], int(parti[1]))
    return voci


def scrivi_manifesto(path, voci, cartella):
    with io.open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("# Impronte SHA-256 degli export di chat in %s\n" % rel(os.path.dirname(path) or ".", cartella))
        fh.write("# Generato da tools/verifica-integrita-export.py il %s\n"
                 % time.strftime("%Y-%m-%d %H:%M:%S"))
        fh.write("# L'impronta è quella del contenuto NON compresso: resta valida dopo la\n"
                 "# compressione e si riverifica con il modo `verifica` dello stesso strumento.\n")
        fh.write("# formato: <sha256> <dimensione in byte> <percorso relativo>\n")
        for nome in sorted(voci):
            sha, dim = voci[nome]
            fh.write("%s %d %s\n" % (sha, dim, nome))


def modo_manifesto(args):
    files = elenca(args.cartella)
    if not files:
        print("nessun export da registrare in %s" % args.cartella, file=sys.stderr)
        return 2
    voci = {}
    totale = 0
    for path in files:
        sha, dim = impronta_file(path)
        voci[rel(args.cartella, path)] = (sha, dim)
        totale += dim
        print("  %s  %12d  %s" % (sha[:16], dim, rel(args.cartella, path)))
    destinazione = args.manifesto or os.path.join(args.cartella, NOME_MANIFESTO)
    scrivi_manifesto(destinazione, voci, args.cartella)
    print("manifesto di %d file, %.2f GB in tutto, scritto in %s"
          % (len(voci), totale / 1e9, destinazione))
    return 0


def modo_comprimi(args):
    destinazione = args.manifesto or os.path.join(args.cartella, NOME_MANIFESTO)
    if not os.path.exists(destinazione):
        print("manca il manifesto %s: eseguire prima il modo `manifesto`" % destinazione,
              file=sys.stderr)
        return 2
    atteso = leggi_manifesto(destinazione)
    files = elenca(args.cartella)
    if not files:
        print("nessun export da comprimere: forse è già stato fatto", file=sys.stderr)
        return 2

    guasti = []
    tot_prima = tot_dopo = 0
    for path in files:
        nome = rel(args.cartella, path)
        if nome not in atteso:
            print("  SALTATO   %s: non è nel manifesto, rigenerare il manifesto" % nome)
            guasti.append(nome)
            continue
        sha_atteso, dim_attesa = atteso[nome]
        gz = path + ".gz"
        if os.path.exists(gz):
            print("  SALTATO   %s: %s esiste già" % (nome, os.path.basename(gz)))
            continue
        if os.path.getsize(path) < args.minimo:
            print("  IN CHIARO %s: sotto la soglia di %d byte" % (nome, args.minimo))
            continue

        # mtime=0 e filename vuoto rendono il risultato riproducibile: ricomprimendo lo stesso
        # input si ottiene lo stesso file, che è ciò che permette di confrontare due esecuzioni.
        with io.open(path, "rb") as sorgente:
            with io.open(gz, "wb") as uscita:
                with gzip.GzipFile(filename="", mode="wb", fileobj=uscita,
                                   compresslevel=args.livello, mtime=0) as z:
                    while True:
                        b = sorgente.read(BLOCCO)
                        if not b:
                            break
                        z.write(b)

        sha_ottenuto, dim_ottenuta = impronta_compresso(gz)
        if sha_ottenuto != sha_atteso or dim_ottenuta != dim_attesa:
            os.remove(gz)
            print("  GUASTO    %s: impronta attesa %s, ottenuta %s. Compresso rimosso, "
                  "originale intatto." % (nome, sha_atteso[:16], sha_ottenuto[:16]))
            guasti.append(nome)
            continue

        prima = os.path.getsize(path)
        dopo = os.path.getsize(gz)
        tot_prima += prima
        tot_dopo += dopo
        print("  OK        %-48s %8.1f MB -> %7.2f MB  (%4.1fx)"
              % (nome, prima / 1e6, dopo / 1e6, float(prima) / dopo))

    if tot_dopo:
        print("totale: %.2f GB -> %.0f MB  (%.1fx)"
              % (tot_prima / 1e9, tot_dopo / 1e6, float(tot_prima) / tot_dopo))
    if guasti:
        print("%d file NON verificati: %s" % (len(guasti), ", ".join(guasti)), file=sys.stderr)
        return 1
    print("originali lasciati al loro posto. Si liberano con il modo `verifica --elimina-originali`, "
          "che li cancella solo se l'intera verifica è verde.")
    return 0


def modo_verifica(args):
    destinazione = args.manifesto or os.path.join(args.cartella, NOME_MANIFESTO)
    if not os.path.exists(destinazione):
        print("manca il manifesto %s" % destinazione, file=sys.stderr)
        return 2
    atteso = leggi_manifesto(destinazione)

    # Si verifica ogni voce del manifesto, non le sole compresse: un export sotto soglia è
    # rimasto in chiaro e la sua integrità va controllata lo stesso, altrimenti il verde della
    # verifica coprirebbe una parte della cartella e tacerebbe sul resto.
    compressi = {rel(args.cartella, p)[:-3]: p for p in elenca_compressi(args.cartella)}
    chiari = {rel(args.cartella, p): p for p in elenca(args.cartella)}
    if not compressi and not chiari:
        print("nessun export da verificare in %s" % args.cartella, file=sys.stderr)
        return 2

    guasti = []
    for nome in sorted(set(compressi) | set(chiari) | set(atteso)):
        if nome not in atteso:
            print("  IGNOTO    %s: presente su disco ma non nel manifesto" % nome)
            guasti.append(nome)
            continue
        sha_atteso, dim_attesa = atteso[nome]
        if nome in compressi:
            forma, path = "compresso", compressi[nome]
            lettura = impronta_compresso
        elif nome in chiari:
            forma, path = "in chiaro", chiari[nome]
            lettura = impronta_file
        else:
            print("  ASSENTE   %s: nel manifesto ma non su disco" % nome)
            guasti.append(nome)
            continue
        try:
            sha_ottenuto, dim_ottenuta = lettura(path)
        except (OSError, EOFError, gzip.BadGzipFile) as e:
            print("  ILLEGGIBILE %s: %s" % (nome, e))
            guasti.append(nome)
            continue
        if sha_ottenuto != sha_atteso or dim_ottenuta != dim_attesa:
            print("  GUASTO    %s: attesa %s/%d byte, ottenuta %s/%d byte"
                  % (nome, sha_atteso[:16], dim_attesa, sha_ottenuto[:16], dim_ottenuta))
            guasti.append(nome)
        else:
            print("  OK        %-60s  %s" % (nome, forma))

    if guasti:
        print("verifica FALLITA su %d file. Nessun originale è stato toccato." % len(guasti),
              file=sys.stderr)
        return 1
    # I nomi si uniscono invece di sommarsi: finché l'originale sta accanto al suo compresso, lo
    # stesso export compare in entrambi gli elenchi e sommarli lo conterebbe due volte.
    nomi = set(compressi) | set(chiari)
    print("verifica superata: %d export (%d compressi, %d in chiaro), contenuto identico al manifesto"
          % (len(nomi), len(compressi), len(nomi - set(compressi))))

    # La cancellazione sta qui e non nella compressione per una ragione di ordine: il modo che
    # distrugge dev'essere lo stesso che ha appena dimostrato di poter fare a meno di ciò che
    # distrugge. Si cancella solo a verifica interamente verde, mai per i soli file passati.
    if args.elimina_originali:
        liberati = 0
        for path in elenca(args.cartella):
            if os.path.exists(path + ".gz"):
                liberati += os.path.getsize(path)
                os.remove(path)
                print("  rimosso l'originale di %s" % rel(args.cartella, path))
        print("liberati %.2f GB" % (liberati / 1e9))
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("modo", choices=("manifesto", "comprimi", "verifica"))
    ap.add_argument("cartella", help="cartella degli export, esplorata ricorsivamente")
    ap.add_argument("--manifesto", help="percorso del manifesto, per default dentro la cartella")
    ap.add_argument("--livello", type=int, default=9, help="livello gzip, da 1 a 9 (default 9)")
    ap.add_argument("--minimo", type=int, default=SOGLIA,
                    help="sotto questa dimensione in byte l'export resta in chiaro (default %d)"
                         % SOGLIA)
    ap.add_argument("--elimina-originali", action="store_true",
                    help="cancella l'originale dei soli file la cui impronta ha corrisposto")
    args = ap.parse_args()

    if not os.path.isdir(args.cartella):
        print("non è una cartella: %s" % args.cartella, file=sys.stderr)
        return 2

    return {"manifesto": modo_manifesto,
            "comprimi": modo_comprimi,
            "verifica": modo_verifica}[args.modo](args)


if __name__ == "__main__":
    sys.exit(main())
