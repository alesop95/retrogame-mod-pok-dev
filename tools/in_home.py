"""Quali gruppi ed esemplari delle copie sono davvero in HOME, per gli strumenti che misurano la copertura.

Perché esiste. Fino al 2026-11-25 `copertura-lotti.py`, `sfide-bank.py` e `fiocchi-e-sfere-prima-di-bank.py` leggevano un
giudizio fisso del 2026-11-04 e contavano in HOME i soli gruppi il cui nome comincia per «HOME»: restavano fuori GIAPPONE2,
RIDATA1, RIDATA2, DIAMANTE1, VERDEFOGLIA1 e ZAFFIRO1, e con ZAFFIRO1 il Training Ribbon. Lo stato di ogni gruppo sta in un
posto solo, `STATO_GRUPPO` di `stampa-collezione.py`, che si aggiorna al punto 18 di ogni giro; qui lo si legge da lì,
insieme alla regola degli esemplari che il gioco non lascia uscire (Pikachu Cosplay, doni di taglia totem).
"""
import importlib.util
import os

QUI = os.path.dirname(os.path.abspath(__file__))
RADICE = os.path.dirname(QUI)
# il giudizio di tutte le copie dopo l'ultimo giro passato a HOME: si aggiorna al punto 18 di ogni giro
GIUDIZIO_CORRENTE = os.path.join(RADICE, "_notes", "lavoro", "giudizi-copie", "dopo-20261126-giro17.json")

_s = importlib.util.spec_from_file_location("stampa_collezione", os.path.join(QUI, "stampa-collezione.py"))
_sc = importlib.util.module_from_spec(_s)
_s.loader.exec_module(_sc)

GRUPPI_IN_HOME = frozenset(g for g, (_, testo) in _sc.STATO_GRUPPO.items() if testo == "in HOME")


def in_home(gruppo, esemplare):
    """Vero se l'esemplare di quel gruppo è passato a HOME."""
    return gruppo in GRUPPI_IN_HOME and _sc.resta_in_console(esemplare) is None


def esemplari_in_home(copie):
    """Gli esemplari in HOME di un elenco di copie di `tools/pkhex-elenco-copie`, con il gruppo accanto."""
    return [(c["gruppo"], x) for c in copie for x in c["esemplari"] if in_home(c["gruppo"], x)]
