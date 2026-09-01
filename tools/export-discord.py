#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Esporta i canali di community scelti dal progetto, invocando DiscordChatExporter.

Perché esiste
--------------
L'esportazione periodica dei canali di community è una operazione rara, poche volte
l'anno, e proprio per questo è quella che si sbaglia: fra una corsa e la successiva nessuno
ricorda quali canali contavano, con quali opzioni, e perché quel canale e non un altro.
Uno strumento che porta con sé la scelta dei canali e la sua motivazione trasforma una
procedura da ricordare in una da eseguire.

La scelta dei canali non è un dato di configurazione ma conoscenza del progetto: dice
quale canale risponde a quale domanda aperta. Vive quindi in questo file insieme al codice
che la usa, con lo stesso principio della tabella delle fonti di `build-source-map.py`, e
si stampa con `--elenco` per poterla leggere senza aprire il sorgente.

Il token non tocca il disco
---------------------------
Il token si chiede in modo interattivo e non compare né sulla riga di comando né in un
file. La ragione è concreta e va conosciuta perché è un errore già commesso in questo
progetto: PowerShell registra la cronologia dei comandi in un file di testo in chiaro, il
cui percorso si ottiene con `(Get-PSReadlineOption).HistorySavePath`, quindi un token
passato come argomento finisce su disco senza che nessuno lo abbia scritto lì. La
richiesta interattiva non lascia quella traccia.

Resta possibile passarlo dall'ambiente con DISCORD_USER_TOKEN per chi automatizza, ed è
una scelta di chi lo fa: anche l'ambiente di un processo è leggibile, e la cadenza rara
rende il costo di digitarlo nullo.

Quale token, e perché è una decisione registrata
------------------------------------------------
Vale il token di un account personale, secondo ADR-019, che è la decisione con cui
l'utente ha scelto questa via per i server dove un bot non può essere invitato, accettando
il rischio dopo che gli era stato esposto. Dove il bot è dentro, la via preferibile resta
`tools/fetch-discord.py`, che non mette a rischio nulla e legge il solo incremento.

Uso
---
    python tools/export-discord.py --elenco
    python tools/export-discord.py --tier 1 --dry-run
    python tools/export-discord.py --tier 1
    python tools/export-discord.py --tier 1 --html
    python tools/export-discord.py --server insideGadgets

Il percorso dell'eseguibile di DiscordChatExporter si passa con `--dce` oppure si mette
nella variabile d'ambiente DCE_PATH. Non è una dipendenza del repository e non vi entra.

Che cosa fa e che cosa non fa
-----------------------------
Non riesporta un canale il cui file esiste già, a meno che non si passi `--forza`: una
esportazione ripetuta per errore costa tempo e richieste al servizio senza aggiungere
nulla. Non tocca il contenuto: la riduzione a Markdown filtrato è il passo successivo, e
lo fa `tools/read-chat-export.py`. E non cancella nulla.
"""

import argparse
import getpass
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
USCITA = os.path.join(ROOT, "_notes", "fonti", "dce")

# ---------------------------------------------------------------------------------------
# La scelta dei canali, decisa il 2026-08-31 leggendo gli elenchi dei nove server
# pertinenti. Ogni voce dice a quale domanda aperta del progetto quel canale risponde,
# perché un canale senza domanda è un canale che produrrà materiale da leggere e non
# risposte. Le sigle dei track sono quelle di SOURCES.md.
#
# Schema: (tier, server, canale, id, track, domanda a cui serve)
# ---------------------------------------------------------------------------------------
CANALI = [
    # --- Tier 1: piccoli, e ciascuno sopra una domanda dichiarata aperta in pending.md.
    (1, "insideGadgets", "gbxcart", "586059097925746719", "SME",
     "driver CH340, porta COM e uso del lettore GBxCart RW: è il canale del produttore, "
     "e il prossimo passo dichiarato del track Smeraldo è precisamente quello"),
    (1, "insideGadgets", "faq", "605532563876085770", "SME",
     "le domande ricorrenti sul lettore, dove finiscono i problemi già risolti"),
    (1, "insideGadgets", "wirelessgb", "586059241912270868", "BRI, LDN",
     "Game Boy senza fili: tocca il cavo Link e il ponte, ed è un canale che il progetto "
     "non sapeva esistere"),
    (1, "PMR", "switch-gen3", "1519230126729203822", "LDN",
     "lo scambio di Rosso Fuoco e Verde Foglia su Switch, cioè il cuore del track LDN"),
    (1, "PMR", "support", "1519239074685124780", "LDN",
     "allestimento, schede Wi-Fi e modalità monitor: da qui viene la sola testimonianza "
     "di campo che il progetto possiede sugli adattatori"),
    (1, "PMR", "general", "1519231335032688742", "LDN, BRI",
     "la discussione generale, dove è emerso che il Wireless Adapter non è 802.11"),
    (1, "GlitchCity", "ace-channel", "732385538769813567", "BRI",
     "esecuzione di codice arbitrario: è il canale dedicato alla tecnica su cui poggia il "
     "trasferimento vero invece della clonazione"),
    (1, "GlitchCity", "gen-1-glitches", "731900394460020807", "BRI",
     "i glitch di generazione 1, compreso il traboccamento della squadra"),
    (1, "GlitchCity", "gen-2-glitches", "731900507844640858", "BRI",
     "i glitch di generazione 2, e la questione del terminatore mancante"),
    (1, "GlitchCity", "gen-3-glitches", "731900526467350538", "BRI, SME, EVT",
     "i glitch di generazione 3, dove si discutono posta, sezioni del salvataggio e i "
     "codici di controllo del motore di testo"),
    (1, "gbadev", "e-reader", "1328901175180918876", "EVT",
     "il dispositivo di lettura delle carte: è il canale del secondo canale di "
     "distribuzione degli eventi, e il progetto non sapeva che esistesse"),

    # --- Tier 2: i canali dei disassemblati, dove stanno gli offset e le formule.
    (2, "pret", "pokered", "442462691542695957", "BRI",
     "strutture, salvataggio e protocollo di scambio di Rosso e Blu; qui va chiesta la "
     "tabella dagli indici interni ai numeri nazionali"),
    (2, "pret", "pokecrystal", "487424856913346580", "BRI",
     "generazione 2: offset del salvataggio per lingue diverse dall'inglese, dimensione "
     "del blocco di posta, e la formula da Stat Experience a Effort Value"),
    (2, "pret", "pokeemerald", "442465020291317760", "BRI, SME, EVT",
     "generazione 3: sezioni del salvataggio, collocazione della posta, chiave di "
     "cifratura e maschera delle quantità"),
    (2, "pret", "pokefirered", "487425035997282324", "BRI, LDN",
     "Rosso Fuoco e Verde Foglia, che sono i giochi del track LDN"),
    (2, "pret", "pokeruby", "442465003140939776", "BRI, SME",
     "Rubino e Zaffiro, l'unico gioco Gen 3 senza maschera sulle quantità"),
    (2, "pret", "gen-3-help", "533083367818657792", "BRI, SME",
     "canale archiviato di aiuto su generazione 3: archiviato non significa inutile, "
     "significa che nessuno vi risponderà più"),

    # --- Tier 3: riferimenti tecnici, per le domande sull'hardware e sul BIOS.
    (3, "gbadev", "documentation", "829440691754237952", "BRI",
     "documentazione dell'hardware: qui va verificato il numero della funzione di BIOS "
     "della decompressione, punto aperto del track degli eventi"),
    (3, "gbadev", "hardware", "950008154731737169", "BRI",
     "hardware del Game Boy Advance, multiboot e porta seriale"),
    (3, "gbadev", "asm", "833314924766953482", "BRI",
     "assembly ARM e Thumb, per il codice che il ponte deve produrre"),
    (3, "GlitchCity", "glitch-documentation-archive", "1110038622893260810", "BRI",
     "archivio di documentazione dei glitch: è materiale già distillato da altri"),
    (3, "GlitchCity", "glitch-general", "731906626285469726", "BRI",
     "la discussione generale sui glitch, per ciò che non ha un canale proprio"),
    (3, "HexManiac", "thumb-asm", "1456804570348126481", "SME, EVT",
     "assembly Thumb nel contesto dell'editing di ROM di generazione 3"),

    # --- Tier 4: a richiesta, quando una domanda specifica lo giustifica.
    (4, "insideGadgets", "flashcarts", "586059516328542218", "SME",
     "cartucce riprogrammabili, che servono a tre delle quattro vie di iniezione di un evento"),
    (4, "OSCR", "development", "1048701692310462474", "SME",
     "il dumper alternativo: sviluppo e formati supportati"),
    (4, "OSCR", "help", "1038272253852401694", "SME",
     "i problemi reali di chi dumpa cartucce con quel dispositivo"),
    (4, "Azahar", "azahar-support", "1230219199801065552", "3DS",
     "verifica dei dump delle cartucce 3DS fuori dalla console"),
    (4, "HexManiac", "pokemon-and-pokedex", "1116808271823654992", "EVT",
     "dati di specie e Pokedex nell'editing di ROM, utile alla ricreazione degli eventi"),
    (4, "HexManiac", "event-scripting", "1116807427967422525", "EVT",
     "script di evento, che è il meccanismo del Dono Segreto"),
]

# ---------------------------------------------------------------------------------------
# I server da esportare interi, invece che canale per canale. Sono i server piccoli e
# monotematici, dove la selezione dei canali costerebbe più di quanto risparmi e dove il
# progetto non conosce gli identificativi dei canali: esportare tutto è più economico che
# enumerare. Il meccanismo è exportguild di DiscordChatExporter, che non richiede alcun
# identificativo di canale.
#
# Schema: (server, id del server, track, domanda a cui serve)
# ---------------------------------------------------------------------------------------
GUILDS = [
    ("MankeyMite", "1219279603286409346", "ACE, EVT",
     "il server dedicato all'esecuzione di codice arbitrario in terza generazione: il suo "
     "canale dei collegamenti è la fonte dell'inventario degli strumenti registrato in "
     "SOURCES.md, e il resto del server è la sola testimonianza di campo che il progetto "
     "possa avere sull'accettazione degli esemplari così prodotti"),
]

# I server esclusi, con il motivo, perché una esclusione senza motivo è indistinguibile da
# una dimenticanza e verrà riaperta dalla prossima sessione.
ESCLUSI = {
    "PokeCoders": "community di codici trucco, che SOURCES.md esclude già esplicitamente: "
                  "sono la causa più probabile del problema del track Smeraldo e non la sua "
                  "soluzione",
    "Domesday86": "conservazione di LaserDisc, estranea al dominio",
    "Reddit Marche": "estraneo al dominio",
    "Direct Messages": "messaggi privati, fuori perimetro per scelta",
}


def token():
    """Il token, dall'ambiente o chiesto in modo interattivo, mai dalla riga di comando.

    La riga di comando è esclusa deliberatamente: PowerShell registra la cronologia dei
    comandi in un file in chiaro, quindi un token passato come argomento finisce su disco
    senza che nessuno lo abbia scritto lì.
    """
    t = os.environ.get("DISCORD_USER_TOKEN")
    if t:
        return t.strip()
    print("Il token non viene mostrato mentre lo incolli e non finisce in alcun file.")
    t = getpass.getpass("Token Discord: ").strip()
    if not t:
        sys.exit("nessun token: nulla da fare")
    return t


def eseguibile(indicato):
    for candidato in (indicato, os.environ.get("DCE_PATH")):
        if candidato and os.path.exists(candidato):
            return candidato
    sys.exit("manca il percorso di DiscordChatExporter.\n"
             "Si passa con --dce, oppure si mette nella variabile d'ambiente DCE_PATH.\n"
             "Non è una dipendenza del repository e non vi entra: la procedura di "
             "installazione sta in docs/22-strumenti.md.")


def elenco():
    per_tier = {}
    for t, srv, can, cid, track, perche in CANALI:
        per_tier.setdefault(t, []).append((srv, can, cid, track, perche))
    for t in sorted(per_tier):
        print("")
        print("=== Tier " + str(t) + ", " + str(len(per_tier[t])) + " canali")
        for srv, can, cid, track, perche in per_tier[t]:
            print("")
            print("  " + srv + " / " + can + "  [" + track + "]")
            print("  id " + cid)
            print("  " + perche)
    print("")
    print("=== Server esportati interi")
    for srv, gid, track, perche in GUILDS:
        print("")
        print("  " + srv + "  [" + track + "]")
        print("  id " + gid)
        print("  " + perche)
    print("")
    print("=== Server esclusi")
    for srv, motivo in ESCLUSI.items():
        print("  " + srv + ": " + motivo)


def interi(a):
    """Esporta interi i server di GUILDS, ciascuno in una cartella propria.

    Il percorso di destinazione è una cartella e non un file: DiscordChatExporter, quando
    riceve una cartella, nomina da sé i file dei singoli canali, ed è precisamente ciò che
    serve qui, perché i nomi dei canali non li conosciamo in anticipo.
    """
    scelti = [g for g in GUILDS if not a.server or g[0] in a.server]
    if not scelti:
        sys.exit("nessun server corrisponde ai criteri; provare --elenco")

    exe = eseguibile(a.dce) if not a.dry_run else (a.dce or "<percorso di DCE>")
    t = None if a.dry_run else token()

    fatti, falliti = 0, 0
    for i, (srv, gid, _track, _perche) in enumerate(scelti, 1):
        cartella = os.path.join(USCITA, srv)
        etichetta = "[" + str(i) + "/" + str(len(scelti)) + "] " + srv + " -> " + cartella
        if os.path.isdir(cartella) and os.listdir(cartella) and not a.forza:
            print(etichetta + ": la cartella esiste e non è vuota, salto; "
                  "con --forza si riesporta")
            continue
        os.makedirs(cartella, exist_ok=True)
        comando = [exe, "exportguild", "-t", "<token>" if a.dry_run else t,
                   "-g", gid, "-f", "Json", "-o", cartella + os.sep]
        if a.after:
            comando += ["--after", a.after]
        if a.media:
            comando += ["--media"]
        print(etichetta)
        if a.dry_run:
            continue
        esito = subprocess.run(comando)
        if esito.returncode == 0:
            fatti += 1
        else:
            print("   non riuscito, codice " + str(esito.returncode) +
                  "; si prosegue con gli altri")
            falliti += 1

    if a.dry_run:
        print("")
        print("nulla eseguito: " + str(len(scelti)) + " server sarebbero stati esportati")
        return 0
    print("")
    print("server esportati " + str(fatti) + ", non riusciti " + str(falliti))
    return 1 if falliti else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--elenco", action="store_true",
                    help="stampa la scelta dei canali con la ragione di ciascuno")
    ap.add_argument("--tier", type=int, action="append",
                    help="quale gruppo esportare; ripetibile")
    ap.add_argument("--guilds", action="store_true",
                    help="esporta interi i server della tabella GUILDS, invece dei canali")
    ap.add_argument("--server", action="append", help="limita a questi server; ripetibile")
    ap.add_argument("--dce", help="percorso dell'eseguibile di DiscordChatExporter")
    ap.add_argument("--html", action="store_true",
                    help="esporta anche la resa leggibile, oltre al JSON")
    ap.add_argument("--media", action="store_true",
                    help="scarica anche gli allegati; moltiplica il volume")
    ap.add_argument("--after", help="ignora i messaggi anteriori a questa data")
    ap.add_argument("--forza", action="store_true",
                    help="riesporta anche i canali il cui file esiste già")
    ap.add_argument("--dry-run", action="store_true",
                    help="stampa che cosa farebbe, senza eseguire e senza chiedere il token")
    a = ap.parse_args()

    if a.elenco:
        elenco()
        return 0

    if a.guilds:
        return interi(a)

    scelti = [c for c in CANALI
              if (not a.tier or c[0] in a.tier)
              and (not a.server or c[1] in a.server)]
    if not scelti:
        sys.exit("nessun canale corrisponde ai criteri; provare --elenco")

    os.makedirs(USCITA, exist_ok=True)
    exe = eseguibile(a.dce) if not a.dry_run else (a.dce or "<percorso di DCE>")
    t = None if a.dry_run else token()

    fatti, saltati, falliti = 0, 0, 0
    for i, (tier, srv, can, cid, track, _perche) in enumerate(scelti, 1):
        formati = [("Json", "json")] + ([("HtmlDark", "html")] if a.html else [])
        for formato, estensione in formati:
            nome = srv + "-" + can + "." + estensione
            destinazione = os.path.join(USCITA, nome)
            if os.path.exists(destinazione) and not a.forza:
                print("[" + str(i) + "/" + str(len(scelti)) + "] salto " + nome +
                      ", esiste già; con --forza si riesporta")
                saltati += 1
                continue
            comando = [exe, "export", "-t", "<token>" if a.dry_run else t,
                       "-c", cid, "-f", formato, "-o", destinazione]
            if a.after:
                comando += ["--after", a.after]
            if a.media:
                comando += ["--media"]
            if a.dry_run:
                print("[" + str(i) + "/" + str(len(scelti)) + "] " + srv + "/" + can +
                      " -> " + nome)
                continue
            print("[" + str(i) + "/" + str(len(scelti)) + "] " + srv + "/" + can +
                  " -> " + nome)
            esito = subprocess.run(comando)
            if esito.returncode == 0:
                fatti += 1
            else:
                # Un canale può fallire perché l'account non lo vede più, perché è stato
                # cancellato, o per un limite di frequenza persistente: si prosegue con gli
                # altri e si riferisce alla fine, invece di interrompere l'intera corsa.
                print("   non riuscito, codice " + str(esito.returncode) +
                      "; si prosegue con gli altri")
                falliti += 1

    if a.dry_run:
        print("")
        print("nulla eseguito: " + str(len(scelti)) + " canali sarebbero stati esportati")
        return 0
    print("")
    print("esportati " + str(fatti) + ", saltati " + str(saltati) +
          ", non riusciti " + str(falliti))
    print("il passo seguente è ridurre a Markdown filtrato con "
          "tools/read-chat-export.py, e la catena completa è in docs/22-strumenti.md")
    return 1 if falliti else 0


if __name__ == "__main__":
    sys.exit(main())
