#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Censisce i repository di codice citati in SOURCES.md e dice quali il progetto usa già.

Perché esiste
-------------
ADR-100 del 2026-10-07 chiede di potenziare il codice del progetto su tutte le fonti tecniche e
con codice, e di censirle «per che cosa possono aggiungere agli strumenti in tools/». Le righe di
`SOURCES.md` con un indirizzo sono 1639, e i repository di codice distinti fra quelle righe sono
oltre cento: leggerli tutti sarebbe il modo più caro di rispondere. Questo strumento fa la parte
deterministica, cioè per ogni repository raccoglie le righe del registro che lo citano, la sezione
in cui stanno, i track dichiarati, l'esito di lettura scritto nella riga e se il codice o la
documentazione del progetto lo nominano già. Il giudizio su che cosa un repository possa aggiungere
resta lavoro di lettura, e si scrive in `docs/potenziamento-dalle-fonti.md`, che è autorato.

Il perimetro, da dichiarare con la misura: gli indirizzi di github.com, gitlab.com, codeberg.org,
bitbucket.org, gist.github.com e raw.githubusercontent.com nelle righe di tabella di `SOURCES.md`;
l'uso nel progetto si cerca per nome del repository, senza distinguere maiuscole, in `tools/`
(Python, C# e PowerShell), in `docs/` e nei sottoprogetti, esclusi `SOURCES.md`, la memoria, i modelli
del template, il censimento stesso e `docs/potenziamento-dalle-fonti.md`, che li nomina tutti per definizione.

Uso
---
    python tools/censimento-fonti-codice.py                  # scrive docs/censimento-fonti-codice.md
    python tools/censimento-fonti-codice.py --check          # esce con 1 se il documento è da rigenerare
"""

import argparse
import collections
import io
import json
import os
import re
import subprocess
import sys

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RACCOLTA = os.path.join(RADICE, "_notes", "fonti", "raccolte", "fonti-codice")
USCITA = os.path.join(RADICE, "docs", "censimento-fonti-codice.md")
CODICE = re.compile(r"https?://(?:www\.)?(github\.com|gitlab\.com|codeberg\.org|bitbucket\.org|gist\.github\.com|raw\.githubusercontent\.com)/([^/\s|)`]+)/([^/\s|)`#?]+)", re.I)
ESITI = [("non letto", re.compile(r"non (ancora )?lett|NON ANCORA LETTO|non aperto", re.I)),
         ("clonato", re.compile(r"clonat|clone superficiale", re.I)),
         ("letto", re.compile(r"\blett[oaie]\b|letto dal vivo|trascritt", re.I)),
         ("saltato o fuori perimetro", re.compile(r"saltato|fuori perimetro|scartato|irrecuperabil", re.I))]
NON_REPO = {"orgs", "topics", "search", "settings", "sponsors", "features", "marketplace", "login", "about"}


def righe_del_registro():
    sezione = ""
    for i, r in enumerate(io.open(os.path.join(RADICE, "SOURCES.md"), encoding="utf-8"), 1):
        if r.startswith("#"):
            sezione = r.lstrip("#").strip()
        elif r.startswith("|"):
            yield i, sezione, r.rstrip("\n")


def esito(riga):
    for nome, rx in ESITI:
        if rx.search(riga):
            return nome
    return "senza esito scritto"


def track(riga):
    celle = [c.strip() for c in riga.strip().strip("|").split("|")]
    ultima = celle[-1] if celle else ""
    return ultima if re.fullmatch(r"[A-Z0-9 ,]{2,40}", ultima) else ""


def testi_del_progetto():
    file = subprocess.run(["git", "-C", RADICE, "ls-files"], capture_output=True, text=True,
                          encoding="utf-8").stdout.splitlines()
    for f in file:
        if f == "SOURCES.md" or f.startswith(".claude/memory/") or f.startswith(".claude/templates/"):
            continue
        # il censimento stesso e il documento che giudica i repository li nominano tutti per definizione
        if f in ("docs/censimento-fonti-codice.md", "tools/censimento-fonti-codice.py", "docs/potenziamento-dalle-fonti.md"):
            continue
        if not f.endswith((".py", ".cs", ".ps1", ".md")):
            continue
        try:
            yield f, io.open(os.path.join(RADICE, f), encoding="utf-8", errors="replace").read().lower()
        except OSError:
            continue


def censisci():
    repo = collections.OrderedDict()
    for i, sezione, r in righe_del_registro():
        for m in CODICE.finditer(r):
            proprietario, nome = m.group(2), re.sub(r"\.git$", "", m.group(3))
            if proprietario.lower() in NON_REPO:
                continue
            k = f"{proprietario}/{nome}".lower()
            v = repo.setdefault(k, {"nome": f"{proprietario}/{nome}", "righe": [], "sezioni": set(),
                                    "track": set(), "esiti": collections.Counter()})
            if i not in v["righe"]:
                v["righe"].append(i)
                v["sezioni"].add(sezione)
                if track(r):
                    v["track"].update(t.strip() for t in track(r).split(","))
                v["esiti"][esito(r)] += 1
    testi = list(testi_del_progetto())
    for k, v in repo.items():
        nome = k.split("/")[1]
        chiave = k if len(nome) < 5 else nome
        v["usato"] = sorted({f for f, t in testi if chiave in t})
        v["codice"] = [f for f in v["usato"] if f.endswith((".py", ".cs", ".ps1"))]
    return repo


def metadati(nome):
    """Linguaggio, licenza, ultimo aggiornamento e stato dai file di `tools/raccogli-fonti-codice.py`.

    Senza la raccolta, che sta fuori da Git, le colonne restano vuote e il documento lo dice: un
    clone del repository non ha la raccolta, e il documento generato là non deve sembrare completo.
    """
    d = os.path.join(RACCOLTA, nome.replace("/", "__", 1))
    j = None
    for f in ("repo.json", "gist.json"):
        if os.path.exists(os.path.join(d, f)):
            j = json.load(io.open(os.path.join(d, f), encoding="utf-8"))
            break
    if j is None:
        return None
    if "files" in j:
        linguaggi = sorted({(x.get("language") or "") for x in j["files"].values()} - {""})
        return {"linguaggio": ", ".join(linguaggi) or "-", "licenza": "-", "aggiornato": (j.get("updated_at") or "")[:10],
                "stato": "gist", "stelle": "-"}
    stato = "archiviato" if j.get("archived") else ("fork" if j.get("fork") else "attivo")
    return {"linguaggio": j.get("language") or "-", "licenza": ((j.get("license") or {}).get("spdx_id") or "-"),
            "aggiornato": (j.get("pushed_at") or "")[:10], "stato": stato, "stelle": j.get("stargazers_count", "-")}


def documento(repo):
    usati = sum(1 for v in repo.values() if v["usato"])
    nel_codice = sum(1 for v in repo.values() if v["codice"])
    righe = [
        "# Censimento dei repository di codice citati dalle fonti",
        "",
        "> Documento generato da `tools/censimento-fonti-codice.py`. Non si modifica a mano: si rigenera. "
        "È la parte deterministica del censimento chiesto da ADR-100; il giudizio su che cosa ciascun "
        "repository possa aggiungere agli strumenti del progetto sta in `docs/potenziamento-dalle-fonti.md`.",
        "",
        f"Perimetro: gli indirizzi di repository di codice nelle righe di tabella di `SOURCES.md`; l'uso nel "
        f"progetto si cerca per nome del repository nei file Python, C#, PowerShell e Markdown tracciati, "
        f"esclusi `SOURCES.md`, la memoria e i modelli del template. Repository distinti: {len(repo)}; nominati "
        f"dal progetto: {usati}, di cui nominati dal codice in `tools/` e nei sottoprogetti: {nel_codice}; mai nominati fuori dal registro: {len(repo) - usati}.",
        "",
        f"Metadati letti con `tools/raccogli-fonti-codice.py` dall'API di GitHub: {sum(1 for v in repo.values() if metadati(v['nome']))} "
        f"repository su {len(repo)}; per gli altri la colonna dice «non raccolto».",
        "",
        "| Repository | Linguaggio | Licenza | Ultimo aggiornamento | Stato | Righe del registro | Track | Esito scritto | Nel codice | Nominato nel progetto in |",
        "|---|---|---|---|---|---|---|---|---|---|",
    ]
    ordine = sorted(repo.values(), key=lambda v: (not v["codice"], not v["usato"], -len(v["righe"]), v["nome"].lower()))
    for v in ordine:
        esiti = ", ".join(f"{n} {c}" for n, c in v["esiti"].most_common())
        usato = ", ".join(f"`{f}`" for f in v["usato"][:4]) + (f" e altri {len(v['usato']) - 4}" if len(v["usato"]) > 4 else "")
        md = metadati(v["nome"]) or {"linguaggio": "non raccolto", "licenza": "-", "aggiornato": "-", "stato": "-"}
        righe.append(f"| `{v['nome']}` | {md['linguaggio']} | {md['licenza']} | {md['aggiornato'] or '-'} | {md['stato']} | {', '.join(map(str, v['righe'][:6]))}{' e altre' if len(v['righe']) > 6 else ''} "
                     f"| {', '.join(sorted(v['track'])) or '-'} | {esiti} | {'sì' if v['codice'] else 'no'} | {usato or 'mai'} |")
    return "\n".join(righe) + "\n"


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    testo = documento(censisci())
    vecchio = io.open(USCITA, encoding="utf-8").read() if os.path.exists(USCITA) else None
    if a.check:
        print("allineato" if vecchio == testo else "da rigenerare")
        return 0 if vecchio == testo else 1
    io.open(USCITA, "w", encoding="utf-8", newline="\n").write(testo)
    print(testo.splitlines()[4][:240])
    return 0


if __name__ == "__main__":
    sys.exit(main())
