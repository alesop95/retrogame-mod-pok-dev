# -*- coding: utf-8 -*-
"""Lettore e scrittore delle strutture Pokemon di generazione 2.

Struttura di box 32 byte, di squadra 48. Rispetto alla generazione 1 non è un'estensione
ma un riordino, quindi non si riusa il parser con un offset diverso: gli offset stanno
nella sezione 4 di DATA-FORMATS_Gen1-Gen2-Gen3.md.

Tre campi sono nuovi rispetto alla generazione 1 e vanno capiti prima di scriverli.
L'amicizia, che nella stessa posizione tiene i cicli di cova se il Pokemon è un uovo.
Il Pokerus, due nibble. E i dati di cattura, due byte densi di campi di bit che solo
Cristallo popola: è il solo posto in tutte le generazioni 1 e 2 dove esista un dato di
provenienza, ed è per questo che una conversione verso la generazione 3 può conservare
il sesso dell'allenatore solo da Cristallo.
"""

from dataclasses import dataclass, field

from . import gb

BOX_STRUCT_LENGTH = 0x20   # 32
PARTY_STRUCT_LENGTH = 0x30  # 48

OFF_SPECIES = 0x00
OFF_HELD_ITEM = 0x01
OFF_MOVES = 0x02
OFF_OT_ID = 0x06
OFF_EXP = 0x08
OFF_STAT_EXP = 0x0B
OFF_DVS = 0x15
OFF_PP = 0x17
OFF_FRIENDSHIP = 0x1B
OFF_POKERUS = 0x1C
OFF_CAUGHT_DATA = 0x1D
OFF_LEVEL = 0x1F
OFF_STATUS = 0x20
OFF_UNUSED = 0x21
OFF_HP = 0x22
OFF_STATS = 0x24

STAT_ORDER = ("max_hp", "atk", "def", "spd", "satk", "sdef")

TIME_OF_DAY = {0: "non impostato", 1: "mattina", 2: "giorno", 3: "notte"}


@dataclass
class CaughtData:
    """I due byte di cattura, popolati solo da Cristallo.

    Primo byte: bit 7-6 momento della giornata, bit 5-0 livello di cattura.
    Secondo byte: bit 7 sesso dell'allenatore, bit 6-0 indice del luogo.
    """

    time_of_day: int = 0
    level: int = 0
    ot_female: bool = False
    location: int = 0

    @classmethod
    def from_bytes(cls, hi, lo):
        return cls(time_of_day=(hi >> 6) & 0x03, level=hi & 0x3F,
                   ot_female=bool(lo & 0x80), location=lo & 0x7F)

    def to_bytes(self):
        if not 0 <= self.level <= 63:
            raise gb.FormatError("livello di cattura %d fuori intervallo 0-63" % self.level)
        if not 0 <= self.location <= 127:
            raise gb.FormatError("indice di luogo %d fuori intervallo 0-127" % self.location)
        return (((self.time_of_day & 0x03) << 6) | (self.level & 0x3F),
                ((0x80 if self.ot_female else 0x00) | (self.location & 0x7F)))

    @property
    def is_empty(self):
        """Vero sui giochi che non popolano questi byte, cioè Oro e Argento."""
        return self.to_bytes() == (0, 0)


@dataclass
class Gen2Mon:
    """Un Pokemon di generazione 2. I campi di sola squadra sono None in un box mon."""

    species: int = 0
    held_item: int = 0
    moves: list = field(default_factory=lambda: [0, 0, 0, 0])
    ot_id: int = 0
    exp: int = 0
    stat_exp: dict = field(default_factory=lambda: {n: 0 for n in gb.STAT_EXP_ORDER})
    dvs: dict = field(default_factory=lambda: {n: 0 for n in gb.DV_ORDER})
    pp: list = field(default_factory=lambda: [(0, 0)] * 4)
    friendship: int = 0
    pokerus: int = 0
    caught: CaughtData = field(default_factory=CaughtData)
    level: int = 0
    status: int = None
    unused: int = None
    hp: int = None
    stats: dict = None

    @property
    def is_party(self):
        return self.status is not None

    @property
    def hp_dv(self):
        return gb.hp_dv(self.dvs)

    @property
    def is_shiny(self):
        """In generazione 2 la lucentezza è un pattern di DV. Vedi gb.is_shiny_gen2."""
        return gb.is_shiny_gen2(self.dvs)

    @property
    def pokerus_strain(self):
        return (self.pokerus >> 4) & 0x0F

    @property
    def pokerus_days(self):
        return self.pokerus & 0x0F

    @classmethod
    def from_bytes(cls, data, party=None):
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
            held_item=data[OFF_HELD_ITEM],
            moves=list(data[OFF_MOVES:OFF_MOVES + 4]),
            ot_id=gb.u16(data, OFF_OT_ID),
            exp=gb.u24(data, OFF_EXP),
            stat_exp=gb.read_stat_exp(data, OFF_STAT_EXP),
            dvs=gb.unpack_dvs(data[OFF_DVS], data[OFF_DVS + 1]),
            pp=[gb.unpack_pp(data[OFF_PP + i]) for i in range(4)],
            friendship=data[OFF_FRIENDSHIP],
            pokerus=data[OFF_POKERUS],
            caught=CaughtData.from_bytes(data[OFF_CAUGHT_DATA], data[OFF_CAUGHT_DATA + 1]),
            level=data[OFF_LEVEL],
        )
        if party:
            mon.status = data[OFF_STATUS]
            mon.unused = data[OFF_UNUSED]
            mon.hp = gb.u16(data, OFF_HP)
            mon.stats = {name: gb.u16(data, OFF_STATS + 2 * i)
                         for i, name in enumerate(STAT_ORDER)}
        return mon

    def to_bytes(self, party=None):
        if party is None:
            party = self.is_party
        if party and not self.is_party:
            raise gb.FormatError("richiesta una struttura di squadra ma i campi di sola "
                                 "squadra non sono presenti")
        buf = bytearray(PARTY_STRUCT_LENGTH if party else BOX_STRUCT_LENGTH)

        buf[OFF_SPECIES] = self.species & 0xFF
        buf[OFF_HELD_ITEM] = self.held_item & 0xFF
        buf[OFF_MOVES:OFF_MOVES + 4] = bytes(m & 0xFF for m in self.moves)
        gb.put_u16(buf, OFF_OT_ID, self.ot_id)
        gb.put_u24(buf, OFF_EXP, self.exp)
        gb.write_stat_exp(buf, OFF_STAT_EXP, self.stat_exp)
        hi, lo = gb.pack_dvs(self.dvs)
        buf[OFF_DVS], buf[OFF_DVS + 1] = hi, lo
        for i, (pp, ups) in enumerate(self.pp):
            buf[OFF_PP + i] = gb.pack_pp(pp, ups)
        buf[OFF_FRIENDSHIP] = self.friendship & 0xFF
        buf[OFF_POKERUS] = self.pokerus & 0xFF
        c_hi, c_lo = self.caught.to_bytes()
        buf[OFF_CAUGHT_DATA], buf[OFF_CAUGHT_DATA + 1] = c_hi, c_lo
        buf[OFF_LEVEL] = self.level & 0xFF

        if party:
            buf[OFF_STATUS] = self.status & 0xFF
            buf[OFF_UNUSED] = self.unused & 0xFF
            gb.put_u16(buf, OFF_HP, self.hp)
            for i, name in enumerate(STAT_ORDER):
                gb.put_u16(buf, OFF_STATS + 2 * i, self.stats[name])
        return bytes(buf)


@dataclass
class Gen2PartyList:
    """La lista della squadra di generazione 2, 428 byte nelle versioni occidentali.

    Stessa forma di quella di generazione 1, con strutture da 48 byte invece di 44. La
    dimensione dei nomi cambia nelle versioni giapponesi, dove sono 6 byte invece di 11,
    e questo lettore non le copre: è uno dei punti dichiarati aperti nella sezione 11
    della referenza.
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
            mons=[Gen2Mon.from_bytes(
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
        return min(self.count, self.CAPACITY)
