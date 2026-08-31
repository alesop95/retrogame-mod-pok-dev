#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Legge la cronologia di un canale Discord tramite un bot account ufficiale.

Perché esiste, e che problema risolve davvero
---------------------------------------------
Le community su Discord sono, per alcune tecniche di questo dominio, la sola
documentazione esistente: la regola `.claude/rules/web-sources-not-fetchable.md` le
registra fra le fonti che nessuno strumento di sessione raggiunge. Fino al 2026-08-29 il
progetto conosceva due sole vie, e le aveva valutate entrambe: il token del proprio
account, chiuso con un no il 2026-08-26 perché automatizzare un account personale è
vietato dalle condizioni d'uso e la sanzione è la sospensione dell'account, e la copia
manuale dei messaggi, che funziona ed è la pratica corrente.

Esiste una terza via che il progetto non aveva considerato, e questo strumento la
implementa: un bot account creato nel portale per sviluppatori di Discord. Non è un modo
di aggirare la regola sui self-bot, è la porta che Discord ha costruito per l'automazione,
con una API pubblica, documentata e con limiti di frequenza pensati per traffico
automatico. La distinzione non è di sfumatura ed è la ragione per cui questo strumento
esiste invece di essere stato rifiutato come il precedente.

Il limite di questa via, che va conosciuto prima di allestirla
--------------------------------------------------------------
Un bot entra in un server soltanto se qualcuno con i permessi di amministrazione di quel
server lo invita. Per i server di cui l'utente non è amministratore, e sono i quattro che
interessano a questo progetto, la via richiede quindi il consenso di terzi: non è un
ostacolo tecnico aggirabile con una configurazione, è il meccanismo di consenso su cui
poggia la legittimità dell'intera via. Chiedere è gratis e va fatto; ricevere un no è un
esito possibile, e in quel caso resta la copia manuale.

Come si allestisce, una volta sola
----------------------------------
1. Su https://discord.com/developers/applications si crea una applicazione e, nella
   sezione Bot, il bot; si copia il token, che va trattato come una password.
2. Nella stessa sezione si abilita Message Content Intent, senza il quale Discord
   consegna i messaggi privi di testo anche a un bot che ha i permessi.
3. Si genera l'URL di invito con i soli permessi di lettura, cioè View Channels e Read
   Message History, e nient'altro: questo strumento non scrive nulla e non ha bisogno di
   altro.
4. Si invita il bot nel server, che richiede di esserne amministratori o di ottenere il
   consenso di chi lo è.
5. Il token va in `.env` nella radice del progetto, che il `.gitignore` esclude:

       DISCORD_BOT_TOKEN=...

   L'agente non può creare né leggere alcun file che corrisponda a `.env*`, nemmeno un
   modello: le regole di permesso del progetto lo negano per protezione. Il file va
   quindi scritto a mano, e la variabile che serve è quella sola.

Il presidio contro l'uso di un token personale
----------------------------------------------
Questo strumento invia sempre l'intestazione di autorizzazione nella forma prevista per i
bot, e prima di qualunque lettura interroga l'endpoint dell'identità corrente per
verificare che l'account autenticato sia dichiarato un bot. Se non lo è, si arresta e
spiega perché, invece di procedere: un token utente inserito per errore in quella
variabile non produce una lettura riuscita ma un rifiuto. È un presidio deliberato e non
va rimosso, perché la differenza fra le due vie non è visibile nell'esito di una singola
richiesta ma nelle conseguenze sull'account.

Uso
---
    python tools/fetch-discord.py guilds
    python tools/fetch-discord.py channels <id del server>
    python tools/fetch-discord.py fetch <id del canale> --limit 500
    python tools/fetch-discord.py fetch <id del canale> --grep "link cable" --grep checksum
    python tools/fetch-discord.py fetch <id del canale> --nuovi --out _notes/fonti/2026-08-29-pret.md
    python tools/fetch-discord.py --self-test

L'opzione `--nuovi` legge soltanto ciò che è arrivato dopo l'ultima lettura riuscita di
quel canale, usando il cursore conservato in `_notes/.discord-cursori.json`, che sta sotto
`_notes/` e quindi fuori dal version control. Serve a non rileggere ogni volta la stessa
cronologia, che è la sola parte del costo che dipende da noi.

Stato di collaudo
-----------------
La logica di impaginazione, del cursore, del filtro e della gestione del limite di
frequenza è provata con `--self-test`, che la esercita contro un trasporto finto e
comprende un controllo negativo, cioè la verifica che il presidio rifiuti un token non di
bot. Il flusso non è stato eseguito contro il servizio, perché in questa sessione non
esiste alcun token: alla prima esecuzione riuscita va aggiornata questa nota e va
aggiornata la voce di Discord nel registro delle fonti.
"""

import argparse
import io
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CURSORI = os.path.join(ROOT, "_notes", ".discord-cursori.json")
BASE = "https://discord.com/api/v10"

# Il numero massimo di messaggi che l'API restituisce in una sola richiesta. Non è una
# scelta di questo strumento ma un limite del servizio, e determina il numero di richieste
# necessarie a leggere una cronologia: mille messaggi costano dieci richieste.
PER_PAGINA = 100

# Quante volte si riprova dopo un rifiuto per eccesso di frequenza prima di arrendersi.
# Il servizio dichiara nella risposta quanti secondi attendere, quindi il numero di
# tentativi non serve a indovinare l'attesa ma a non restare in un ciclo indefinito.
TENTATIVI = 5


class Errore(Exception):
    """Un errore che va mostrato all'utente come messaggio, non come traccia di stack."""


# ---------------------------------------------------------------------------------------
# Il trasporto è un parametro e non una dipendenza nascosta, perché è ciò che rende la
# logica provabile senza credenziali: il self-test passa un trasporto finto e verifica
# impaginazione, cursore e attesa senza toccare la rete.
# ---------------------------------------------------------------------------------------

class TrasportoHTTP:
    """Il trasporto vero, che parla con l'API di Discord."""

    def __init__(self, token):
        self.token = token

    def get(self, percorso, parametri=None):
        url = BASE + percorso
        if parametri:
            url += "?" + urllib.parse.urlencode(parametri)
        richiesta = urllib.request.Request(url, headers={
            # La forma dell'intestazione è il presidio: si dichiara sempre un bot, mai un
            # account utente, e non esiste un'opzione per cambiarla.
            "Authorization": "Bot " + self.token,
            "User-Agent": "retrogame-mod-pok-dev (lettore di fonti di community, sola lettura)",
            "Accept": "application/json",
        })
        try:
            with urllib.request.urlopen(richiesta, timeout=30) as risposta:
                return 200, json.loads(risposta.read().decode("utf-8")), {}
        except urllib.error.HTTPError as e:
            corpo = e.read().decode("utf-8", errors="replace")
            try:
                dati = json.loads(corpo)
            except ValueError:
                dati = {"message": corpo[:400]}
            return e.code, dati, dict(e.headers or {})


class TrasportoFinto:
    """Un trasporto che risponde da una tabella, per provare la logica senza credenziali.

    Conserva l'elenco delle richieste ricevute, cosicché il self-test possa verificare non
    soltanto il risultato ma anche il modo in cui è stato ottenuto: quante pagine sono
    state chieste, con quale cursore, e se l'attesa dopo un rifiuto è stata rispettata.
    """

    def __init__(self, identita, messaggi, rifiuta_una_volta=False):
        self.identita = identita
        self.messaggi = messaggi
        self.rifiuta_una_volta = rifiuta_una_volta
        self.chiamate = []
        self.attese = []

    def get(self, percorso, parametri=None):
        self.chiamate.append((percorso, dict(parametri or {})))
        if percorso == "/users/@me":
            return 200, self.identita, {}
        if self.rifiuta_una_volta:
            self.rifiuta_una_volta = False
            return 429, {"retry_after": 0.01, "message": "You are being rate limited."}, {}
        if "/messages" in percorso:
            prima = (parametri or {}).get("before")
            limite = int((parametri or {}).get("limit", PER_PAGINA))
            # L'API restituisce i messaggi dal più recente al più vecchio, e `before`
            # chiede quelli anteriori a un identificativo: il finto rispetta questa forma,
            # perché è proprio la forma che la logica di impaginazione deve gestire.
            elenco = self.messaggi
            if prima is not None:
                indici = [i for i, m in enumerate(elenco) if m["id"] == prima]
                if indici:
                    elenco = elenco[indici[0] + 1:]
            return 200, elenco[:limite], {}
        raise AssertionError("percorso non previsto dal trasporto finto: " + percorso)


def dormi(secondi, trasporto):
    """L'attesa passa dal trasporto quando è finto, così il self-test la osserva."""
    if isinstance(trasporto, TrasportoFinto):
        trasporto.attese.append(secondi)
        return
    time.sleep(secondi)


def chiama(trasporto, percorso, parametri=None):
    """Una richiesta, con la gestione del limite di frequenza dichiarato dal servizio."""
    for tentativo in range(TENTATIVI):
        codice, dati, _ = trasporto.get(percorso, parametri)
        if codice == 200:
            return dati
        if codice == 429:
            attesa = float(dati.get("retry_after", 1.0))
            dormi(attesa, trasporto)
            continue
        if codice == 401:
            raise Errore("il token è stato rifiutato: verificare DISCORD_BOT_TOKEN in .env")
        if codice == 403:
            raise Errore("accesso negato su " + percorso + ": il bot non ha View Channels "
                         "e Read Message History su quel canale, oppure non è nel server")
        if codice == 404:
            raise Errore("non trovato: " + percorso + "; verificare l'identificativo")
        raise Errore("il servizio ha risposto " + str(codice) + ": " +
                     str(dati.get("message", dati))[:300])
    raise Errore("limite di frequenza non superato dopo " + str(TENTATIVI) + " tentativi")


def verifica_identita(trasporto):
    """Il presidio: si procede solo se l'account autenticato è dichiarato un bot.

    Restituisce il nome dell'account. Solleva se non è un bot, ed è il controllo che
    distingue questa via da quella che il progetto ha rifiutato: un token personale
    inserito per errore non produce una lettura ma un rifiuto con la sua ragione.
    """
    io_stesso = chiama(trasporto, "/users/@me")
    if not io_stesso.get("bot"):
        raise Errore(
            "l'account autenticato non è un bot.\n"
            "Questo strumento legge soltanto con un bot account creato nel portale per\n"
            "sviluppatori di Discord. Automatizzare un account personale è vietato dalle\n"
            "condizioni d'uso e la sanzione è la sospensione dell'account: il progetto lo\n"
            "ha deciso il 2026-08-26 e la decisione non è stata riaperta.\n"
            "Le istruzioni per creare il bot sono nel docstring di questo file.")
    return io_stesso.get("username", "senza nome")


def leggi_token():
    token = os.environ.get("DISCORD_BOT_TOKEN")
    if token:
        return token.strip()
    percorso = os.path.join(ROOT, ".env")
    if os.path.exists(percorso):
        with open(percorso, "rb") as f:
            for riga in f.read().decode("utf-8", errors="replace").split("\n"):
                riga = riga.strip()
                if riga.startswith("DISCORD_BOT_TOKEN="):
                    return riga.split("=", 1)[1].strip().strip("\"'")
    raise Errore(
        "manca DISCORD_BOT_TOKEN.\n"
        "Va scritto a mano in .env nella radice del progetto, che il .gitignore esclude,\n"
        "oppure passato nell'ambiente. L'agente non può creare quel file: le regole di\n"
        "permesso del progetto negano ogni percorso che corrisponda a .env*, ed è voluto.\n"
        "La procedura completa di allestimento è nel docstring di questo file.")


# ---------------------------------------------------------------------------------------
# Cursori: l'unica parte del costo che dipende da noi.
# ---------------------------------------------------------------------------------------

def cursori_letti():
    if not os.path.exists(CURSORI):
        return {}
    with open(CURSORI, "rb") as f:
        try:
            return json.loads(f.read().decode("utf-8"))
        except ValueError:
            return {}


def cursore_scritto(canale, ultimo):
    dati = cursori_letti()
    dati[str(canale)] = str(ultimo)
    os.makedirs(os.path.dirname(CURSORI), exist_ok=True)
    with open(CURSORI, "wb") as f:
        f.write((json.dumps(dati, indent=2, ensure_ascii=False) + "\n").encode("utf-8"))


# ---------------------------------------------------------------------------------------
# Lettura.
# ---------------------------------------------------------------------------------------

def messaggi_del_canale(trasporto, canale, limite, dopo=None):
    """Scorre la cronologia dal più recente al più vecchio, e restituisce l'ordine naturale.

    Il parametro `dopo` è l'identificativo dell'ultimo messaggio già letto in una corsa
    precedente: la lettura si arresta quando lo incontra, invece di continuare fino al
    limite richiesto. Gli identificativi di Discord crescono nel tempo, quindi il
    confronto numerico fra due di essi è un confronto cronologico, e questo è ciò che
    rende il cursore affidabile senza consultare l'orologio.
    """
    raccolti, prima = [], None
    while len(raccolti) < limite:
        parametri = {"limit": min(PER_PAGINA, limite - len(raccolti))}
        if prima is not None:
            parametri["before"] = prima
        pagina = chiama(trasporto, "/channels/" + str(canale) + "/messages", parametri)
        if not pagina:
            break
        fermati = False
        for m in pagina:
            if dopo is not None and int(m["id"]) <= int(dopo):
                fermati = True
                break
            raccolti.append(m)
        if fermati or len(pagina) < parametri["limit"]:
            break
        prima = pagina[-1]["id"]
    raccolti.reverse()
    return raccolti


def filtra(messaggi, chiavi, lunghezza_minima, da):
    """I tre filtri sono gli stessi di read-chat-export.py, per non avere due grammatiche."""
    fuori = []
    for m in messaggi:
        testo = (m.get("content") or "").strip()
        if lunghezza_minima and len(testo) < lunghezza_minima:
            continue
        if da and (m.get("timestamp") or "") < da:
            continue
        if chiavi:
            minuscolo = testo.lower()
            if not any(k.lower() in minuscolo for k in chiavi):
                continue
        fuori.append(m)
    return fuori


def markdown(messaggi, canale, nome_bot):
    """La resa segue la convenzione delle fonti procurate a mano, per essere citabile.

    L'autore viene conservato con il proprio identificativo accanto al nome, e non per
    completezza formale: senza di esso una richiesta di cancellazione mirata non è
    eseguibile, e la sezione sulla sicurezza dell'handoff lo indica come il primo dei
    quattro accorgimenti che rendono quella richiesta fattibile invece che improvvisata.
    """
    righe = []
    righe.append("# Canale Discord " + str(canale))
    righe.append("")
    righe.append("Letto con `tools/fetch-discord.py` attraverso il bot account `" + nome_bot +
                 "`, in sola lettura. Sono " + str(len(messaggi)) + " messaggi. Questo file "
                 "sta sotto `_notes/`, che il `.gitignore` esclude: è materiale grezzo di "
                 "terzi e non entra nel version control, secondo ADR-016. Ciò che entra è la "
                 "sintesi con l'attribuzione, in `SOURCES.md`.")
    righe.append("")
    for m in messaggi:
        autore = m.get("author") or {}
        nome = autore.get("global_name") or autore.get("username") or "ignoto"
        quando = (m.get("timestamp") or "")[:19].replace("T", " ")
        righe.append("## " + nome + " (" + str(autore.get("id", "?")) + ") - " + quando)
        righe.append("")
        testo = (m.get("content") or "").strip()
        righe.append(testo if testo else "(nessun testo: allegato o solo incorporazione)")
        allegati = m.get("attachments") or []
        if allegati:
            righe.append("")
            for a in allegati:
                righe.append("Allegato: " + str(a.get("filename", "?")) + " (" +
                             str(a.get("size", "?")) + " byte)")
        righe.append("")
    return "\n".join(righe).rstrip("\n") + "\n"


# ---------------------------------------------------------------------------------------
# Il self-test: prova la logica e comprende un controllo negativo.
# ---------------------------------------------------------------------------------------

def self_test():
    esiti = []

    def prova(nome, condizione, dettaglio=""):
        esiti.append((nome, bool(condizione), dettaglio))

    finti = [{"id": str(1000 - i), "content": "messaggio " + str(1000 - i),
              "timestamp": "2026-08-2" + str(i % 10) + "T10:00:00.000000+00:00",
              "author": {"id": "7", "username": "tizio"}} for i in range(250)]

    bot = {"bot": True, "username": "lettore-di-fonti"}
    utente = {"bot": False, "username": "persona"}

    # 1. Impaginazione: 250 messaggi richiedono tre pagine da cento.
    t = TrasportoFinto(bot, finti)
    verifica_identita(t)
    letti = messaggi_del_canale(t, 42, 250)
    pagine = [c for c in t.chiamate if "/messages" in c[0]]
    prova("impaginazione, messaggi raccolti", len(letti) == 250, str(len(letti)))
    prova("impaginazione, richieste effettuate", len(pagine) == 3, str(len(pagine)))
    prova("impaginazione, cursore passato dalla seconda", pagine[1][1].get("before") == "901",
          str(pagine[1][1].get("before")))
    prova("ordine cronologico crescente",
          letti[0]["id"] == "751" and letti[-1]["id"] == "1000",
          letti[0]["id"] + ".." + letti[-1]["id"])

    # 2. Il cursore ferma la lettura, invece di leggere tutto e scartare dopo.
    t = TrasportoFinto(bot, finti)
    letti = messaggi_del_canale(t, 42, 250, dopo="990")
    prova("cursore, solo il delta", len(letti) == 10, str(len(letti)))
    prova("cursore, una sola richiesta",
          len([c for c in t.chiamate if "/messages" in c[0]]) == 1)

    # 3. Il limite di frequenza: si attende quanto il servizio dichiara e si riprova.
    t = TrasportoFinto(bot, finti, rifiuta_una_volta=True)
    letti = messaggi_del_canale(t, 42, 10)
    prova("limite di frequenza, esito comunque ottenuto", len(letti) == 10, str(len(letti)))
    prova("limite di frequenza, attesa rispettata", t.attese == [0.01], str(t.attese))

    # 4. Controllo negativo: il presidio deve rifiutare un token non di bot. Se questa
    #    prova passasse senza sollevare, il presidio non ci sarebbe.
    t = TrasportoFinto(utente, finti)
    try:
        verifica_identita(t)
        prova("presidio contro il token personale", False, "non ha rifiutato")
    except Errore as e:
        prova("presidio contro il token personale", "non è un bot" in str(e))

    # 5. I filtri.
    campione = [
        {"id": "1", "content": "parla del link cable", "timestamp": "2026-01-01T00:00:00",
         "author": {"id": "1", "username": "a"}},
        {"id": "2", "content": "ok", "timestamp": "2026-01-02T00:00:00",
         "author": {"id": "2", "username": "b"}},
        {"id": "3", "content": "checksum additivo e permutazioni", "timestamp": "2025-01-01T00:00:00",
         "author": {"id": "3", "username": "c"}},
    ]
    prova("filtro per parola chiave",
          [m["id"] for m in filtra(campione, ["link cable"], 0, None)] == ["1"])
    prova("filtro per lunghezza minima",
          [m["id"] for m in filtra(campione, None, 10, None)] == ["1", "3"])
    prova("filtro per data",
          [m["id"] for m in filtra(campione, None, 0, "2026-01-01")] == ["1", "2"])

    # 6. La resa conserva l'identificativo dell'autore, che serve alla cancellazione mirata.
    reso = markdown(campione, 42, "lettore-di-fonti")
    prova("la resa conserva l'identificativo dell'autore", "(1)" in reso and "(3)" in reso)

    larghezza = max(len(n) for n, _, _ in esiti)
    falliti = 0
    for nome, esito, dettaglio in esiti:
        stato = "ok      " if esito else "FALLITO "
        if not esito:
            falliti += 1
        print("  " + stato + nome.ljust(larghezza) + ("  " + dettaglio if dettaglio else ""))
    print("self-test: " + str(falliti) + " controlli falliti su " + str(len(esiti)))
    return 1 if falliti else 0


# ---------------------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--self-test", action="store_true",
                    help="prova la logica contro un trasporto finto, senza credenziali")
    sub = ap.add_subparsers(dest="comando")

    sub.add_parser("guilds", help="i server in cui il bot è stato invitato")

    p_ch = sub.add_parser("channels", help="i canali di un server")
    p_ch.add_argument("guild")

    p_f = sub.add_parser("fetch", help="la cronologia di un canale")
    p_f.add_argument("canale")
    p_f.add_argument("--limit", type=int, default=200, help="quanti messaggi al massimo")
    p_f.add_argument("--grep", action="append", help="tieni solo i messaggi con questa parola")
    p_f.add_argument("--min-length", type=int, default=0, help="scarta i messaggi più corti")
    p_f.add_argument("--since", help="scarta i messaggi anteriori a questa data ISO")
    p_f.add_argument("--nuovi", action="store_true",
                    help="leggi solo ciò che è arrivato dopo l'ultima lettura di questo canale")
    p_f.add_argument("--out", help="dove scrivere; per difetto sotto _notes/fonti/")

    a = ap.parse_args()

    if a.self_test:
        return self_test()
    if not a.comando:
        ap.print_help()
        return 2

    try:
        trasporto = TrasportoHTTP(leggi_token())
        nome_bot = verifica_identita(trasporto)

        if a.comando == "guilds":
            for g in chiama(trasporto, "/users/@me/guilds"):
                print(g.get("id", "?") + "  " + str(g.get("name", "?")))
            return 0

        if a.comando == "channels":
            for c in chiama(trasporto, "/guilds/" + a.guild + "/channels"):
                # Il tipo 0 è un canale testuale ordinario e il 5 è un canale di annunci,
                # che è l'unico seguibile da un altro server senza il consenso di questo.
                if c.get("type") in (0, 5):
                    etichetta = "annunci" if c.get("type") == 5 else "testo   "
                    print(str(c.get("id")) + "  " + etichetta + "  #" + str(c.get("name")))
            return 0

        if a.comando == "fetch":
            dopo = cursori_letti().get(str(a.canale)) if a.nuovi else None
            messaggi = messaggi_del_canale(trasporto, a.canale, a.limit, dopo=dopo)
            if not messaggi:
                print("nessun messaggio nuovo" if a.nuovi else "nessun messaggio")
                return 0
            ultimo = messaggi[-1]["id"]
            messaggi = filtra(messaggi, a.grep, a.min_length, a.since)
            destinazione = a.out or os.path.join(
                ROOT, "_notes", "fonti",
                time.strftime("%Y-%m-%d") + "-discord-" + str(a.canale) + ".md")
            os.makedirs(os.path.dirname(destinazione), exist_ok=True)
            with open(destinazione, "wb") as f:
                f.write(markdown(messaggi, a.canale, nome_bot).encode("utf-8"))
            print("scritti " + str(len(messaggi)) + " messaggi in " +
                  os.path.relpath(destinazione, ROOT))
            cursore_scritto(a.canale, ultimo)
            print("cursore aggiornato: la prossima corsa con --nuovi parte da " + ultimo)
            return 0

    except Errore as e:
        print(str(e), file=sys.stderr)
        return 1
    return 2


if __name__ == "__main__":
    sys.exit(main())
