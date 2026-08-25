# -*- coding: utf-8 -*-
"""Lettore e scrittore delle strutture Pokemon di generazione 1.

Struttura di box 33 byte, di squadra 44. La forma canonica e' la macro box_struct di
pret/pokered in macros/ram.asm; gli offset assoluti stanno nella sezione 2 di
DATA-FORMATS_Gen1-Gen2-Gen3.md.

Due scelte di progettazione, motivate in docs/20-architettura-codice.md. I nomi restano
byte grezzi e non diventano testo, cosi' che leggere e riscrivere renda byte identici.
I campi derivati, cioe' le statistiche calcolate, sono letti e conservati ma non
ricalcolati: ricalcolarli e' un'operazione esplicita, non un effetto collaterale della
lettura, perche' sbagliarla di nascosto produce un Pokemon che cambia da solo.
"""

from dataclasses import dataclass, field

from . import gb

BOX_STRUCT_LENGTH = 0x21   # 33
PARTY_STRUCT_LENGTH = 0x2C  # 44

# Offset dentro la struttura, dalla macro box_struct di pokered.
OFF_SPECIES = 0x00
OFF_HP = 0x01
OFF_BOX_LEVEL = 0x03
OFF_STATUS = 0x04
OFF_TYPE1 = 0x05
OFF_TYPE2 = 0x06
OFF_CATCH_RATE = 0x07
OFF_MOVES = 0x08
OFF_OT_ID = 0x0C
OFF_EXP = 0x0E
OFF_STAT_EXP = 0x11
OFF_DVS = 0x1B
OFF_PP = 0x1D
OFF_LEVEL = 0x21
OFF_STATS = 0x22

STAT_ORDER = ("max_hp", "atk", "def", "spd", "spc")


@dataclass
class Gen1Mon:
    """Un Pokemon di generazione 1. I campi di sola squadra sono None in un box mon."""

    species: int = 0
    hp: int = 0
    box_level: int = 0
    status: int = 0
    type1: int = 0
    type2: int = 0
    catch_rate: int = 0
    moves: list = field(default_factory=lambda: [0, 0, 0, 0])
    ot_id: int = 0
    exp: int = 0
    stat_exp: dict = field(default_factory=lambda: {n: 0 for n in gb.STAT_EXP_ORDER})
    dvs: dict = field(default_factory=lambda: {n: 0 for n in gb.DV_ORDER})
    pp: list = field(default_factory=lambda: [(0, 0)] * 4)
    level: int = None
    stats: dict = None

    @property
    def is_party(self):
        return self.level is not None

    @property
    def hp_dv(self):
        """Il quinto DV, derivato dagli altri quattro. Vedi gb.hp_dv."""
        return gb.hp_dv(self.dvs)

    @classmethod
    def from_bytes(cls, data, party=None):
        """Legge una struttura. Con party=None la modalita' si deduce dalla lunghezza."""
        if party is None:
            if len(data) == PARTY_STRUCT_LENGTH:
                party = True
            elif len(data) == BOX_STRUCT_LENGTH:
                party = False
            else:
                raise gb.FormatError(
                    "lunghezza %d: attesi %d per un box mon o %d per un party mon"
                    % (len(data), BOX_STRUCT_LENGTH, PARTY_STRUCT_LENGTH))
        expected = PARTY_STRUCT_LENGTH if party else BOX_STRUCT_LENGTH
        if len(data) < expected:
            raise gb.FormatError("servono %d byte, ricevuti %d" % (expected, len(data)))

        mon = cls(
            species=data[OFF_SPECIES],
            hp=gb.u16(data, OFF_HP),
            box_level=data[OFF_BOX_LEVEL],
            status=data[OFF_STATUS],
            type1=data[OFF_TYPE1],
            type2=data[OFF_TYPE2],
            catch_rate=data[OFF_CATCH_RATE],
            moves=list(data[OFF_MOVES:OFF_MOVES + 4]),
            ot_id=gb.u16(data, OFF_OT_ID),
            exp=gb.u24(data, OFF_EXP),
            stat_exp=gb.read_stat_exp(data, OFF_STAT_EXP),
            dvs=gb.unpack_dvs(data[OFF_DVS], data[OFF_DVS + 1]),
            pp=[gb.unpack_pp(data[OFF_PP + i]) for i in range(4)],
        )
        if party:
            mon.level = data[OFF_LEVEL]
            mon.stats = {name: gb.u16(data, OFF_STATS + 2 * i)
                         for i, name in enumerate(STAT_ORDER)}
        return mon

    def to_bytes(self, party=None):
        """Scrive la struttura. Inversa esatta di from_bytes sui byte validi."""
        if party is None:
            party = self.is_party
        if party and not self.is_party:
            raise gb.FormatError("richiesta una struttura di squadra ma livello e "
                                 "statistiche non sono presenti")
        buf = bytearray(PARTY_STRUCT_LENGTH if party else BOX_STRUCT_LENGTH)

        buf[OFF_SPECIES] = self.species & 0xFF
        gb.put_u16(buf, OFF_HP, self.hp)
        buf[OFF_BOX_LEVEL] = self.box_level & 0xFF
        buf[OFF_STATUS] = self.status & 0xFF
        buf[OFF_TYPE1] = self.type1 & 0xFF
        buf[OFF_TYPE2] = self.type2 & 0xFF
        buf[OFF_CATCH_RATE] = self.catch_rate & 0xFF
        buf[OFF_MOVES:OFF_MOVES + 4] = bytes(m & 0xFF for m in self.moves)
        gb.put_u16(buf, OFF_OT_ID, self.ot_id)
        gb.put_u24(buf, OFF_EXP, self.exp)
        gb.write_stat_exp(buf, OFF_STAT_EXP, self.stat_exp)
        hi, lo = gb.pack_dvs(self.dvs)
        buf[OFF_DVS], buf[OFF_DVS + 1] = hi, lo
        for i, (pp, ups) in enumerate(self.pp):
            buf[OFF_PP + i] = gb.pack_pp(pp, ups)

        if party:
            buf[OFF_LEVEL] = self.level & 0xFF
            for i, name in enumerate(STAT_ORDER):
                gb.put_u16(buf, OFF_STATS + 2 * i, self.stats[name])
        return bytes(buf)


@dataclass
class Gen1PartyList:
    """La lista della squadra: quattro array paralleli, non un array di record.

    Forma: contatore, lista di specie terminata da 0xFF, strutture, nomi dell'allenatore
    originale, soprannomi. Il terminatore della lista di specie non e' decorativo: e' la
    condizione di uscita dei cicli del gioco, e la sua assenza e' la primitiva su cui si
    costruisce l'esecuzione di codice arbitrario descritta in docs/09-esecuzione-codice.md.

    La dimensione totale e' 0x194, cioe' 404 byte, e vale la pena scriverlo in entrambe
    le basi: una fonte secondaria riporta "194 byte", che e' la dimensione esadecimale
    letta come decimale.
    """

    count: int = 0
    species: list = field(default_factory=lambda: [gb.SPECIES_TERMINATOR] * (gb.PARTY_LENGTH + 1))
    mons: list = field(default_factory=list)
    ot_names: list = field(default_factory=list)
    nicknames: list = field(default_factory=list)

    CAPACITY = gb.PARTY_LENGTH
    STRUCT_LENGTH = PARTY_STRUCT_LENGTH
    TOTAL_LENGTH = (1 + (gb.PARTY_LENGTH + 1)
                    + gb.PARTY_LENGTH * PARTY_STRUCT_LENGTH
                    + 2 * gb.PARTY_LENGTH * gb.NAME_LENGTH)

    @classmethod
    def from_bytes(cls, data):
        if len(data) < cls.TOTAL_LENGTH:
            raise gb.FormatError("servono %d byte per una lista di squadra, ricevuti %d"
                                 % (cls.TOTAL_LENGTH, len(data)))
        n = cls.CAPACITY
        off_species = 1
        off_mons = off_species + n + 1
        off_ot = off_mons + n * cls.STRUCT_LENGTH
        off_nick = off_ot + n * gb.NAME_LENGTH

        return cls(
            count=data[0],
            species=list(data[off_species:off_species + n + 1]),
            mons=[Gen1Mon.from_bytes(
                data[off_mons + i * cls.STRUCT_LENGTH:
                     off_mons + (i + 1) * cls.STRUCT_LENGTH], party=True)
                for i in range(n)],
            ot_names=gb.read_name_array(data, off_ot, n),
            nicknames=gb.read_name_array(data, off_nick, n),
        )

    def to_bytes(self):
        n = self.CAPACITY
        buf = bytearray(self.TOTAL_LENGTH)
        buf[0] = self.count & 0xFF
        off_species = 1
        buf[off_species:off_species + n + 1] = bytes(s & 0xFF for s in self.species)
        off_mons = off_species + n + 1
        for i, mon in enumerate(self.mons):
            buf[off_mons + i * self.STRUCT_LENGTH:
                off_mons + (i + 1) * self.STRUCT_LENGTH] = mon.to_bytes(party=True)
        off_ot = off_mons + n * self.STRUCT_LENGTH
        gb.write_name_array(buf, off_ot, self.ot_names)
        gb.write_name_array(buf, off_ot + n * gb.NAME_LENGTH, self.nicknames)
        return bytes(buf)

    def occupied(self):
        """Le posizioni realmente occupate, secondo il contatore."""
        return min(self.count, self.CAPACITY)
