# -*- coding: utf-8 -*-
"""Sintetizza in software il passaggio del Parco Amici, dalla terza alla quarta generazione.

Perche' questo modulo esiste
-----------------------------
Il 2026-09-16 due prove a mano in `PKHeX` hanno dimostrato che trascinare un file di terza
generazione in un salvataggio di quarta applica davvero la trasformazione del Parco Amici, non un
passaggio a vuoto: un Mew normale diventa Legale con il luogo scritto come Parco Amici, un
esemplare non schiuso si schiude, un esemplare con una macchina nascosta perde la mossa invece di
essere rifiutato. Questo modulo rifa' la stessa trasformazione leggendo il sorgente vero del
verificatore, `PK3.ConvertToPK4()` in `_notes/fonti/cloni/pkhex/PKHeX.Core/PKM/PK3.cs`, cosi' da
produrre l'esemplare di quarta generazione senza passare da alcuna console o emulatore.

Le mutazioni, una per una, con la loro fonte
---------------------------------------------
Identificativo, valore di personalita', sfera, valori individuali (i trenta bit bassi), punti
esperienza, valori di sforzo e statistiche da gara si copiano senza ricalcolo: `PK3.ConvertToPK4`
li assegna direttamente dal record di partenza.

La cordialita' si azzera a settanta (`OriginalTrainerFriendship = 70`), sempre, indipendentemente
da quella di partenza.

Il livello d'incontro diventa il livello di arrivo (`MetLevel = CurrentLevel`). Questo modulo
assume che il livello di arrivo coincida con il livello con cui l'esemplare e' stato composto,
perche' nessun esemplare prodotto da questo progetto viene mai fatto crescere prima del
trasferimento: e' una decisione dichiarata e non un'approssimazione silenziosa.

Il luogo d'incontro diventa un'unica costante, `Locations.Transfer3 = 0x37`, indipendentemente dal
gioco di origine. Questo corregge un'affermazione precedente di questo stesso documento
(`pokedex-home-completo/CATENA-DI-TRASFERIMENTO.md`), che descriveva luoghi diversi per gioco di
origine: il campo numerico e' identico per tutti, e la sola cosa che varia con il gioco di origine
e' il campo `Version`, che resta quello originale e non viene toccato da questa funzione.

Il contrassegno di uovo si spegne sempre. Un esemplare non schiuso viene fatto schiudere: la specie,
le mosse e i valori individuali non cambiano (verificato il 2026-09-16 trascinando
`_notes/lotti/lotto-eventi/127-PichuwithTeeterDance-Pichu.pk3`, che dopo la conversione resta un Pichu
con le stesse mosse e lo stesso livello, con la sola casella "Da un Uovo" spuntata prima e vuota
dopo), e il soprannome diventa il nome della specie nella lingua dell'esemplare, da
`SpeciesName.GetSpeciesNameGeneration`.

Le mosse che sono macchine nascoste di terza generazione si tolgono, da
`PersonalInfo3.MachineMovesHidden`: Taglio (15), Volo (19), Surf (57), Forza (70), Flash (148),
Frantumaroccia (249), Cascata (127), Immersione (291). La fonte le toglie e poi richiude le
posizioni vuote (`FixMoves`) e ricarica i punti potenza al massimo (`HealPP`). Questo modulo NON
applica questa correzione in automatico: la mossa tolta e' spesso la ragione per cui l'esemplare e'
un collezionabile (il caso dei Pikachu Surfisti e Volanti), quindi la scelta di perderla o di non
trasferire l'esemplare resta una decisione dell'utente, gia' registrata come domanda aperta in
`pokedex-home-completo/CATENA-DI-TRASFERIMENTO.md`. Una voce che porta una di queste mosse viene
esclusa dal lotto prodotto e elencata, non corretta.

Il contrassegno "senza soprannome" non si rideriva confrontando il nome con la lingua del gioco di
arrivo, come questo progetto aveva scritto in precedenza: la fonte (`G3PKM.IsNicknamed`) confronta
il nome corrente con il nome della specie NELLA LINGUA CHE L'ESEMPLARE STESSO DICHIARA, poi copia
quel solo bit sul record di quarta generazione (`pk4.IsNicknamed = IsNicknamed`). Un esemplare
giapponese con il proprio nome giapponese di specie risulta quindi "senza soprannome" anche dopo il
passaggio a un gioco occidentale: cio' che resta sbagliato e' solo la resa a video del testo, non il
contrassegno. Questo modulo replica lo stesso confronto, nella lingua dichiarata dall'esemplare.

L'abilita' si legge dalla tabella personale di quarta generazione (identica a quella di terza per
le specie che qui contano) e si sceglie fra le due caselle con la parita' del valore di
personalita', come fanno gli altri generatori di quarta generazione di questo progetto.

Cosa questo modulo non fa
--------------------------
Non tocca gli oggetti tenuti (nessuno dei lotti Gen3 di questo progetto ne porta uno rilevante per
questo passaggio), non applica i fiocchi di gara oltre a quelli gia' nel record, e non gestisce le
forme alternative. Nessuna di queste omissioni e' silenziosa: se un giorno servisse un campo non
gestito qui, il modo di scoprirlo e' il confronto con un'osservazione umana in PKHeX, non
un'assunzione.
"""

from __future__ import annotations

import importlib.util
import io
import os
import struct
from dataclasses import dataclass, field

from . import charmap as charmap_mod
from .gen3 import Gen3Mon

RADICE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PKHEX_DEFAULT = os.path.join(RADICE, "_notes", "fonti", "cloni", "pkhex")

# Da PersonalInfo3.MachineMovesHidden, letto il 2026-09-16.
MACCHINE_NASCOSTE_GEN3 = frozenset({15, 19, 57, 70, 148, 249, 127, 291})

# Da Locations.Transfer3, letto il 2026-09-16: un'unica costante per ogni gioco di origine.
LUOGO_PARCO_AMICI = 0x37

DIM_PERSONALE = 0x2C
OFF_P_GENERE = 0x10
OFF_P_ABILITA1 = 0x16
OFF_P_ABILITA2 = 0x17

_moduli_cache = {}


def _modulo(nome_file, alias):
    if alias in _moduli_cache:
        return _moduli_cache[alias]
    percorso = os.path.join(RADICE, "tools", nome_file)
    spec = importlib.util.spec_from_file_location(alias, percorso)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    _moduli_cache[alias] = modulo
    return modulo


def _g4():
    return _modulo("genera-evento-gen4.py", "genera_evento_gen4_pa")


def _i4():
    i4 = _modulo("genera-incontro-gen4.py", "genera_incontro_gen4_pa")
    if not hasattr(i4, "G4"):
        i4.G4 = _g4()
    return i4


@dataclass
class EsitoConversione:
    """Cio' che la conversione ha fatto, oltre ai byte prodotti."""

    byte: bytes
    schiuso: bool
    macchina_nascosta_trovata: int | None
    is_nicknamed: bool
    soprannome_testo: str
    ot_testo: str
    esclusioni: list = field(default_factory=list)


class MacchinaNascostaTrovata(Exception):
    """L'esemplare conosce una macchina nascosta: non si corregge, si esclude."""

    def __init__(self, mossa):
        super().__init__("mossa %d e' una macchina nascosta di terza generazione" % mossa)
        self.mossa = mossa


def _leggi_personale(pkhex, specie):
    percorso = os.path.join(pkhex, "PKHeX.Core", "Resources", "byte", "personal", "personal_hgss")
    dati = io.open(percorso, "rb").read()
    inizio = specie * DIM_PERSONALE
    blocco = dati[inizio:inizio + DIM_PERSONALE]
    if len(blocco) < DIM_PERSONALE:
        raise KeyError("numero nazionale fuori dalla tabella personale: %d" % specie)
    return blocco


def _nome_specie(pkhex, specie, lingua_codice):
    """Il nome della specie, dalla tabella di testo del verificatore, per una lingua data."""
    cartelle = {1: "ja", 2: "en", 3: "fr", 4: "it", 5: "de", 7: "es"}
    cartella = cartelle.get(lingua_codice, "en")
    for tentativo in (cartella, "en"):
        percorso = os.path.join(pkhex, "PKHeX.Core", "Resources", "text", "other", tentativo,
                                "text_Species_%s.txt" % tentativo)
        if os.path.exists(percorso):
            righe = io.open(percorso, encoding="utf-8-sig").read().splitlines()
            if specie < len(righe) and righe[specie].strip():
                return righe[specie].strip()
    raise KeyError("nome di specie assente per %d in lingua %d" % (specie, lingua_codice))


def _decodifica_gen3(byte_grezzi, lingua_codice):
    cm = charmap_mod.Charmap.gen3_jp() if lingua_codice == 1 else charmap_mod.Charmap.gen3()
    return cm.decode(byte_grezzi)


# La tabella di terza generazione di questo progetto decodifica l'apostrofo come apice destro
# (U+2019, "'"), ma la tabella di quarta generazione del verificatore non ha quel carattere: porta
# solo l'apice sinistro (U+2018, "'") e l'apostrofo dritto (U+0027). DA VERIFICARE quale dei due sia
# quello storicamente giusto per la quarta generazione: qui si normalizza al primo trovato nella
# tabella (apice sinistro) solo per non fallire la transcodifica, non perche' sia stato confermato
# sul gioco vero.
_NORMALIZZAZIONE_TESTO = {"’": "‘"}


def _normalizza_per_gen4(testo):
    return "".join(_NORMALIZZAZIONE_TESTO.get(ch, ch) for ch in testo)


def convertibile(mon: Gen3Mon):
    """Vero se nessuna mossa e' una macchina nascosta di terza generazione; altrimenti la mossa."""
    for m in mon.attacks.moves:
        if m in MACCHINE_NASCOSTE_GEN3:
            return m
    return None


def converti(mon: Gen3Mon, pkhex=PKHEX_DEFAULT, escludi_macchine_nascoste=True):
    """Produce il record di scatola di quarta generazione equivalente al passaggio dal Parco Amici.

    Lancia `MacchinaNascostaTrovata` se una mossa e' una macchina nascosta di terza generazione e
    `escludi_macchine_nascoste` e' vero (il default): la mossa non si toglie in automatico, la voce
    si esclude, perche' toglierla e' una perdita di identita' dell'esemplare che l'utente deve
    decidere lui, non lo strumento di sua iniziativa.
    """
    macchina = convertibile(mon)
    if macchina is not None and escludi_macchine_nascoste:
        raise MacchinaNascostaTrovata(macchina)

    g4 = _g4()
    i4 = _i4()
    pk4 = bytearray(g4.DIM_PK4_SCATOLA)

    struct.pack_into("<I", pk4, g4.OFF_PID, mon.personality)
    struct.pack_into("<H", pk4, g4.OFF_SANITA, 0)
    struct.pack_into("<H", pk4, g4.OFF_SPECIE, mon.growth.species)
    struct.pack_into("<H", pk4, g4.OFF_TID, mon.ot_id & 0xFFFF)
    struct.pack_into("<H", pk4, g4.OFF_SID, (mon.ot_id >> 16) & 0xFFFF)

    schiuso = bool(mon.is_egg)
    exp = mon.growth.experience
    struct.pack_into("<I", pk4, g4.OFF_ESPERIENZA, exp)

    # La cordialita' si azzera a settanta, sempre: PK3.ConvertToPK4 non guarda quella di partenza.
    pk4[g4.OFF_CORDIALITA] = 70

    personale = _leggi_personale(pkhex, mon.growth.species)
    ab1, ab2 = personale[OFF_P_ABILITA1], personale[OFF_P_ABILITA2]
    pk4[g4.OFF_ABILITA] = ab2 if (mon.misc.ability_num & 1) else ab1

    pk4[g4.OFF_LINGUA] = mon.language

    iv32 = 0
    for i, nome in enumerate(("hp", "atk", "def", "spd", "satk", "sdef")):
        iv32 |= (mon.misc.ivs[nome] & 0x1F) << (5 * i)
    # bit 30 uovo: sempre spento, l'esemplare arriva sempre schiuso.
    # bit 31 senza-soprannome: dalla fonte, confrontato nella lingua che l'esemplare dichiara.
    nome_specie_lingua = _nome_specie(pkhex, mon.growth.species, mon.language)
    if schiuso:
        soprannome_testo = nome_specie_lingua
        is_nicknamed = False
    else:
        soprannome_testo = _decodifica_gen3(mon.nickname, mon.language)
        is_nicknamed = soprannome_testo.upper() != nome_specie_lingua.upper()
    if is_nicknamed:
        iv32 |= 1 << 31
    struct.pack_into("<I", pk4, g4.OFF_IV32, iv32)

    rapporto = personale[OFF_P_GENERE]
    genere = g4.genere_da_pid(mon.personality, rapporto)
    fatidico = 1 if mon.misc.modern_fateful_encounter else 0
    pk4[g4.OFF_FLAG_GENERE] = fatidico | (genere << 1)

    struct.pack_into("<H", pk4, g4.OFF_INCONTRO_DP, LUOGO_PARCO_AMICI)
    struct.pack_into("<H", pk4, g4.OFF_INCONTRO_ESTESO, LUOGO_PARCO_AMICI)
    struct.pack_into("<H", pk4, g4.OFF_UOVO_DP, 0)
    struct.pack_into("<H", pk4, g4.OFF_UOVO_ESTESO, 0)
    anno, mese, giorno = g4.DATA_INCONTRO
    pk4[g4.OFF_INCONTRO_ANNO] = (anno - 2000) & 0xFF
    pk4[g4.OFF_INCONTRO_ANNO + 1] = mese
    pk4[g4.OFF_INCONTRO_ANNO + 2] = giorno
    pk4[g4.OFF_VERSIONE] = mon.misc.met_game
    pk4[g4.OFF_LIVELLO_INCONTRO] = mon.misc.met_level & 0x7F
    pk4[g4.OFF_PALLA_DPPT] = mon.misc.pokeball
    pk4[g4.OFF_PALLA_HGSS] = mon.misc.pokeball

    for i, m in enumerate(mon.attacks.moves):
        struct.pack_into("<H", pk4, 0x28 + 2 * i, m)
        struct.pack_into("B", pk4, 0x30 + i, mon.attacks.pp[i] & 0xFF)

    # Da PK4.cs: EV_HP..EV_SPD sono 0x18-0x1D, le statistiche da gara 0x1E-0x23 le seguono subito.
    for i, nome in enumerate(("hp", "atk", "def", "spd", "satk", "sdef")):
        pk4[0x18 + i] = mon.evs.evs[nome]
    for i, nome in enumerate(("cool", "beauty", "cute", "smart", "tough")):
        pk4[0x1E + i] = mon.evs.contest[nome]
    pk4[0x23] = mon.evs.sheen

    caratteri = i4.tabella_caratteri(pkhex)
    ot_testo = _decodifica_gen3(mon.ot_name, mon.language)
    soprannome_bytes = i4.codifica_nome(_normalizza_per_gen4(soprannome_testo), caratteri)
    pk4[0x48:0x48 + len(soprannome_bytes)] = soprannome_bytes
    ot_bytes = i4.codifica_nome(_normalizza_per_gen4(ot_testo), caratteri)
    pk4[g4.OFF_OT_NOME:g4.OFF_OT_NOME + len(ot_bytes)] = ot_bytes

    struct.pack_into("<H", pk4, g4.OFF_CHECKSUM, g4.somma_controllo(pk4))

    return EsitoConversione(
        byte=bytes(pk4), schiuso=schiuso, macchina_nascosta_trovata=macchina,
        is_nicknamed=is_nicknamed, soprannome_testo=soprannome_testo, ot_testo=ot_testo,
    )
