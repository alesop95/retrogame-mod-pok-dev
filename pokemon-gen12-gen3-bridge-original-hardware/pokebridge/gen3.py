# -*- coding: utf-8 -*-
"""Lettore e scrittore delle strutture Pokemon di generazione 3.

Qui cambia la natura del problema rispetto alle due generazioni Game Boy. La struttura di
box è 80 byte e quella di squadra 100, ma i 48 byte centrali sono cifrati, permutati in
uno di ventiquattro ordini possibili, e protetti da un checksum che se non torna non
produce un Pokemon strano: produce un Uovo Peste, cioè distrugge il dato in modo
visibile e definitivo. Ogni passo di quella catena è verificato sul sorgente e non su una
fonte secondaria, perché su questo punto le fonti secondarie sbagliano in un modo che
distrugge i dati: una pagina enciclopedica descrive il checksum come somma byte per byte,
mentre il sorgente somma parole da 16 bit.

Due scelte separano questo modulo da `gb.py`, ed è la ragione per cui i primitivi non si
riusano: qui l'ordine dei byte è little-endian, e non esiste impaccamento in nibble ma
campi di bit su parole da 16 e 32 bit. Resta condivisa la sola classe di errore,
`gb.FormatError`, perché un pacchetto con due gerarchie di eccezioni per la stessa
categoria di problema costringe chi lo usa a intercettarne due.

Riferimenti primari, letti su `pret/pokeemerald` il 2026-08-26:
    include/pokemon.h   struct BoxPokemon, struct Pokemon, le quattro PokemonSubstruct
    src/pokemon.c       EncryptBoxMon, DecryptBoxMon, CalculateBoxMonChecksum, GetSubstruct
La sintesi in prosa è nella sezione 5 di DATA-FORMATS_Gen1-Gen2-Gen3.md.

Ciò che questo modulo non copre, e che è lo strato successivo: la struttura del
salvataggio da 128 KiB, cioè le sezioni da 4096 byte con il loro piede, la scelta dello
slot valido e il buffer contiguo del deposito. Quella è la sezione 6 della referenza.
"""

from dataclasses import dataclass, field

from . import gb

BOX_STRUCT_LENGTH = 0x50    # 80
PARTY_STRUCT_LENGTH = 0x64  # 100
SECURE_LENGTH = 48
SUBSTRUCT_LENGTH = 12
SUBSTRUCT_COUNT = 4

# POKEMON_NAME_LENGTH e PLAYER_NAME_LENGTH di pokeemerald. Non coincidono con
# gb.NAME_LENGTH, che è 11: i nomi si accorciano passando alla generazione 3, ed è uno
# dei vincoli veri della conversione.
NICKNAME_LENGTH = 10
OT_NAME_LENGTH = 7

OFF_PERSONALITY = 0x00
OFF_OT_ID = 0x04
OFF_NICKNAME = 0x08
OFF_LANGUAGE = 0x12
OFF_FLAGS = 0x13
OFF_OT_NAME = 0x14
OFF_MARKINGS = 0x1B
OFF_CHECKSUM = 0x1C
OFF_UNKNOWN = 0x1E
OFF_SECURE = 0x20

# I venti byte in più della struttura di squadra, da struct Pokemon.
OFF_STATUS = 0x50
OFF_LEVEL = 0x54
OFF_MAIL = 0x55
OFF_STATS = 0x56

PARTY_STAT_ORDER = ("hp", "max_hp", "atk", "def", "spd", "satk", "sdef")
EV_ORDER = ("hp", "atk", "def", "spd", "satk", "sdef")
CONTEST_ORDER = ("cool", "beauty", "cute", "smart", "tough")

NO_MAIL = 0xFF

# Gioco di origine, dal campo metGame. I valori 6 e 7 non esistono in generazione 3: il 15
# copre Colosseum e XD, che non sono giochi GBA.
ORIGIN_GAMES = {0: "nessuno", 1: "Zaffiro", 2: "Rubino", 3: "Smeraldo",
                4: "Rosso Fuoco", 5: "Verde Foglia", 15: "Colosseum o XD"}

# Tabella di permutazione, verbatim dalla macro SUBSTRUCT_CASE di src/pokemon.c. Ogni riga
# è indicizzata da personality % 24 e dice in quale dei quattro slot da 12 byte si trova
# la sottostruttura di ciascun tipo, nell'ordine Growth, Attacks, EV e condizione,
# Miscellaneous. È la forma nativa del sorgente, cioè posizione-per-tipo; la tabella
# della referenza è la sua trasposta, cioè tipo-per-posizione, e il test verifica che le
# due coincidano invece di far scegliere a chi legge quale delle due sia giusta.
SUBSTRUCT_POSITIONS = (
    (0, 1, 2, 3), (0, 1, 3, 2), (0, 2, 1, 3), (0, 3, 1, 2),
    (0, 2, 3, 1), (0, 3, 2, 1), (1, 0, 2, 3), (1, 0, 3, 2),
    (2, 0, 1, 3), (3, 0, 1, 2), (2, 0, 3, 1), (3, 0, 2, 1),
    (1, 2, 0, 3), (1, 3, 0, 2), (2, 1, 0, 3), (3, 1, 0, 2),
    (2, 3, 0, 1), (3, 2, 0, 1), (1, 2, 3, 0), (1, 3, 2, 0),
    (2, 1, 3, 0), (3, 1, 2, 0), (2, 3, 1, 0), (3, 2, 1, 0),
)

SUBSTRUCT_LETTERS = "GAEM"


def u16(buf, off):
    """Intero a 16 bit little-endian. L'opposto di gb.u16, e non è un dettaglio."""
    return buf[off] | (buf[off + 1] << 8)


def put_u16(buf, off, value):
    if not 0 <= value <= 0xFFFF:
        raise gb.FormatError("valore %d fuori intervallo per un campo a 16 bit" % value)
    buf[off] = value & 0xFF
    buf[off + 1] = (value >> 8) & 0xFF


def u32(buf, off):
    """Intero a 32 bit little-endian."""
    return (buf[off] | (buf[off + 1] << 8) | (buf[off + 2] << 16) | (buf[off + 3] << 24))


def put_u32(buf, off, value):
    if not 0 <= value <= 0xFFFFFFFF:
        raise gb.FormatError("valore %d fuori intervallo per un campo a 32 bit" % value)
    buf[off] = value & 0xFF
    buf[off + 1] = (value >> 8) & 0xFF
    buf[off + 2] = (value >> 16) & 0xFF
    buf[off + 3] = (value >> 24) & 0xFF


def substruct_order(personality):
    """L'ordine delle sottostrutture negli slot, per esempio "GAEM".

    È la forma leggibile della tabella, ricavata invertendo SUBSTRUCT_POSITIONS: se il
    tipo 0 sta nello slot 2, allora lo slot 2 contiene una G.
    """
    positions = SUBSTRUCT_POSITIONS[personality % 24]
    letters = [None] * SUBSTRUCT_COUNT
    for type_index, slot in enumerate(positions):
        letters[slot] = SUBSTRUCT_LETTERS[type_index]
    return "".join(letters)


def crypt_key(personality, ot_id):
    """La chiave di cifratura, che non è un segreto ma un dato pubblico della struttura.

    EncryptBoxMon mette ogni parola in XOR prima con il valore di personalità e poi con
    l'ID dell'allenatore, e due XOR consecutivi equivalgono a un XOR con la combinazione
    dei due. DecryptBoxMon fa la stessa cosa nell'ordine inverso, che sulla stessa parola
    è la stessa operazione: la cifratura è involutiva, quindi una sola funzione serve per
    entrambi i versi e non c'è modo di sbagliare la direzione.
    """
    return (personality ^ ot_id) & 0xFFFFFFFF


def crypt_secure(raw, personality, ot_id):
    """Cifra o decifra i 48 byte, indifferentemente: l'operazione è la propria inversa.

    Lo XOR agisce su parole da 32 bit little-endian, non su byte, e la differenza si vede
    solo quando la chiave non è simmetrica nei suoi quattro byte: è il genere di errore
    che passa i test costruiti a mano e rompe i dati reali.
    """
    if len(raw) != SECURE_LENGTH:
        raise gb.FormatError("il blocco cifrato è %d byte, attesi %d"
                             % (len(raw), SECURE_LENGTH))
    key = crypt_key(personality, ot_id)
    out = bytearray(SECURE_LENGTH)
    for i in range(0, SECURE_LENGTH, 4):
        put_u32(out, i, u32(raw, i) ^ key)
    return bytes(out)


def compute_checksum(plain):
    """Il checksum dei 48 byte in chiaro: somma delle 24 parole da 16 bit, troncata.

    Il sorgente somma sei parole per ciascuna delle quattro sottostrutture, prese nel loro
    ordine logico attraverso GetSubstruct. Poiché l'addizione è commutativa, la somma
    delle ventiquattro parole non dipende dall'ordine degli slot: ne segue che il checksum
    si verifica senza sapere quale permutazione sia in uso, e questa proprietà è comoda
    ma va detta, perché chi la scopre da sé rischia di credere di aver trovato un errore.

    Il troncamento a 16 bit non è una scelta nostra: l'accumulatore nel sorgente è un u16
    e l'aritmetica C tronca da sé.
    """
    if len(plain) != SECURE_LENGTH:
        raise gb.FormatError("il blocco in chiaro è %d byte, attesi %d"
                             % (len(plain), SECURE_LENGTH))
    total = 0
    for i in range(0, SECURE_LENGTH, 2):
        total += u16(plain, i)
    return total & 0xFFFF


@dataclass
class Growth:
    """Sottostruttura 0: specie, oggetto, esperienza, bonus PP, amicizia.

    Il campo `filler` esiste nel sorgente con quel nome e va conservato invece che azzerato,
    perché su un salvataggio reale può non essere nullo e perderlo romperebbe la simmetria.
    """

    species: int = 0
    held_item: int = 0
    experience: int = 0
    pp_bonuses: int = 0
    friendship: int = 0
    filler: int = 0

    @classmethod
    def from_bytes(cls, data):
        return cls(species=u16(data, 0), held_item=u16(data, 2), experience=u32(data, 4),
                   pp_bonuses=data[8], friendship=data[9], filler=u16(data, 10))

    def to_bytes(self):
        buf = bytearray(SUBSTRUCT_LENGTH)
        put_u16(buf, 0, self.species)
        put_u16(buf, 2, self.held_item)
        put_u32(buf, 4, self.experience)
        buf[8] = self.pp_bonuses & 0xFF
        buf[9] = self.friendship & 0xFF
        put_u16(buf, 10, self.filler)
        return bytes(buf)

    def pp_bonus(self, index):
        """I PP Up di una mossa, due bit per mossa dentro un solo byte.

        In generazione 2 i PP correnti e i PP Up stanno impaccati nello stesso byte, che
        gb.unpack_pp scompone; qui le due informazioni finiscono in sottostrutture diverse,
        i PP in Attacks e i PP Up qui, ed è per questo che la conversione deve smontare
        quel byte e distribuirlo su due posti.
        """
        if not 0 <= index <= 3:
            raise gb.FormatError("indice di mossa %d fuori intervallo 0-3" % index)
        return (self.pp_bonuses >> (2 * index)) & 0x03


@dataclass
class Attacks:
    """Sottostruttura 1: quattro mosse e i loro PP correnti."""

    moves: list = field(default_factory=lambda: [0, 0, 0, 0])
    pp: list = field(default_factory=lambda: [0, 0, 0, 0])

    @classmethod
    def from_bytes(cls, data):
        return cls(moves=[u16(data, 2 * i) for i in range(4)],
                   pp=list(data[8:12]))

    def to_bytes(self):
        buf = bytearray(SUBSTRUCT_LENGTH)
        for i, move in enumerate(self.moves):
            put_u16(buf, 2 * i, move)
        buf[8:12] = bytes(p & 0xFF for p in self.pp)
        return bytes(buf)


@dataclass
class EvsCondition:
    """Sottostruttura 2: sei EV, cinque statistiche da gara e la lucentezza estetica.

    L'ordine degli EV è quello interno della generazione 3, con la Velocità al quarto
    posto e non all'ultimo, e non coincide con l'ordine di visualizzazione. Le cinque
    statistiche da gara e lo `sheen` non hanno alcun corrispondente nelle generazioni 1 e 2:
    una conversione le lascia a zero e non ha alternative, perché il dato non esiste a monte.
    """

    evs: dict = field(default_factory=lambda: {n: 0 for n in EV_ORDER})
    contest: dict = field(default_factory=lambda: {n: 0 for n in CONTEST_ORDER})
    sheen: int = 0

    @classmethod
    def from_bytes(cls, data):
        return cls(evs={n: data[i] for i, n in enumerate(EV_ORDER)},
                   contest={n: data[6 + i] for i, n in enumerate(CONTEST_ORDER)},
                   sheen=data[11])

    def to_bytes(self):
        buf = bytearray(SUBSTRUCT_LENGTH)
        for i, name in enumerate(EV_ORDER):
            buf[i] = self.evs[name] & 0xFF
        for i, name in enumerate(CONTEST_ORDER):
            buf[6 + i] = self.contest[name] & 0xFF
        buf[11] = self.sheen & 0xFF
        return bytes(buf)

    @property
    def ev_total(self):
        """La somma degli EV, che il gioco non lascia superare 510.

        Non è un vincolo imposto qui, perché un lettore che rifiuta un dato reale è
        inutile: è un criterio che lo strato di conversione deve rispettare quando li
        assegna, ed è esposto perché quello strato lo consulti.
        """
        return sum(self.evs.values())


@dataclass
class Misc:
    """Sottostruttura 3: Pokerus, provenienza, IV, uovo, abilità e nastri.

    È quella densa di campi di bit, e la sola in cui la referenza in prosa non basta:
    tutti i confini fra campi qui sono presi dalle dichiarazioni di bitfield di
    include/pokemon.h, comprese le quattro posizioni che la referenza non nominava, cioè
    i bit 27-30, che nel sorgente sono `unusedRibbons` e vengono scartati dalla quarta
    generazione. Restano conservati perché un lettore che li perde rompe la simmetria su
    un salvataggio che li abbia non nulli.
    """

    pokerus: int = 0
    met_location: int = 0
    met_level: int = 0
    met_game: int = 0
    pokeball: int = 0
    ot_female: bool = False
    ivs: dict = field(default_factory=lambda: {n: 0 for n in EV_ORDER})
    is_egg: bool = False
    ability_num: int = 0
    contest_ribbons: dict = field(default_factory=lambda: {n: 0 for n in CONTEST_ORDER})
    merit_ribbons: int = 0
    unused_ribbons: int = 0
    modern_fateful_encounter: bool = False

    # I dodici nastri di merito a un bit, nell'ordine di dichiarazione, a partire dal bit 15
    # della parola dei nastri. Sono tenuti come maschera intera e non come dodici booleani
    # perché nessuno strato di questo progetto li interpreta, e una maschera si conserva
    # senza doverli nominare tutti.
    MERIT_RIBBON_NAMES = ("champion", "winning", "victory", "artist", "effort", "marine",
                          "land", "sky", "country", "national", "earth", "world")

    @classmethod
    def from_bytes(cls, data):
        origins = u16(data, 2)
        iv_word = u32(data, 4)
        ribbons = u32(data, 8)
        return cls(
            pokerus=data[0],
            met_location=data[1],
            met_level=origins & 0x7F,
            met_game=(origins >> 7) & 0x0F,
            pokeball=(origins >> 11) & 0x0F,
            ot_female=bool((origins >> 15) & 0x01),
            ivs={n: (iv_word >> (5 * i)) & 0x1F for i, n in enumerate(EV_ORDER)},
            is_egg=bool((iv_word >> 30) & 0x01),
            ability_num=(iv_word >> 31) & 0x01,
            contest_ribbons={n: (ribbons >> (3 * i)) & 0x07
                             for i, n in enumerate(CONTEST_ORDER)},
            merit_ribbons=(ribbons >> 15) & 0x0FFF,
            unused_ribbons=(ribbons >> 27) & 0x0F,
            modern_fateful_encounter=bool((ribbons >> 31) & 0x01),
        )

    def to_bytes(self):
        if not 0 <= self.met_level <= 127:
            raise gb.FormatError("livello di incontro %d fuori intervallo 0-127"
                                 % self.met_level)
        for name, value in self.ivs.items():
            if not 0 <= value <= 31:
                raise gb.FormatError("IV %s = %d fuori intervallo 0-31" % (name, value))

        buf = bytearray(SUBSTRUCT_LENGTH)
        buf[0] = self.pokerus & 0xFF
        buf[1] = self.met_location & 0xFF

        origins = ((self.met_level & 0x7F)
                   | ((self.met_game & 0x0F) << 7)
                   | ((self.pokeball & 0x0F) << 11)
                   | ((0x01 if self.ot_female else 0x00) << 15))
        put_u16(buf, 2, origins)

        iv_word = 0
        for i, name in enumerate(EV_ORDER):
            iv_word |= (self.ivs[name] & 0x1F) << (5 * i)
        iv_word |= (0x01 if self.is_egg else 0x00) << 30
        iv_word |= (self.ability_num & 0x01) << 31
        put_u32(buf, 4, iv_word)

        ribbons = 0
        for i, name in enumerate(CONTEST_ORDER):
            ribbons |= (self.contest_ribbons[name] & 0x07) << (3 * i)
        ribbons |= (self.merit_ribbons & 0x0FFF) << 15
        ribbons |= (self.unused_ribbons & 0x0F) << 27
        ribbons |= (0x01 if self.modern_fateful_encounter else 0x00) << 31
        put_u32(buf, 8, ribbons)
        return bytes(buf)

    @property
    def pokerus_days(self):
        return self.pokerus & 0x0F

    @property
    def pokerus_strain(self):
        return (self.pokerus >> 4) & 0x0F

    @property
    def origin_game_name(self):
        return ORIGIN_GAMES.get(self.met_game, "sconosciuto (%d)" % self.met_game)

    def has_merit_ribbon(self, name):
        return bool(self.merit_ribbons & (1 << self.MERIT_RIBBON_NAMES.index(name)))


SUBSTRUCT_TYPES = (Growth, Attacks, EvsCondition, Misc)


@dataclass
class Gen3Mon:
    """Un Pokemon di generazione 3, con le quattro sottostrutture già decifrate.

    Il valore di personalità è immutabile dopo la costruzione, ed è una scelta di
    progettazione e non una limitazione: quel valore è anche chiave di cifratura e
    selettore della permutazione, quindi cambiarlo su una struttura già composta la
    invaliderebbe silenziosamente, che è il modo tipico di produrre Uova Peste. Chi
    deve cambiarlo, e in conversione serve davvero perché il valore di personalità decide
    anche natura e sesso, usa `with_personality`, che ricompone tutto da capo.

    I campi di sola squadra sono None in una struttura di box, come in gen1 e gen2. Nomi e
    soprannomi restano byte grezzi: la transcodifica è un'operazione a parte, in charmap.py,
    e tenerla fuori da qui è ciò che rende possibile la prova di simmetria.
    """

    personality: int = 0
    ot_id: int = 0
    nickname: bytes = b"\x00" * NICKNAME_LENGTH
    language: int = 0
    flags: int = 0
    ot_name: bytes = b"\x00" * OT_NAME_LENGTH
    markings: int = 0
    unknown: int = 0
    growth: Growth = field(default_factory=Growth)
    attacks: Attacks = field(default_factory=Attacks)
    evs: EvsCondition = field(default_factory=EvsCondition)
    misc: Misc = field(default_factory=Misc)
    checksum_stored: int = None
    status: int = None
    level: int = None
    mail: int = None
    stats: dict = None

    _frozen = False

    def __post_init__(self):
        object.__setattr__(self, "_frozen", True)

    def __setattr__(self, name, value):
        if name == "personality" and getattr(self, "_frozen", False):
            raise gb.FormatError(
                "il valore di personalità non si modifica dopo la costruzione: è chiave "
                "di cifratura e selettore di permutazione, e cambiarlo qui invaliderebbe "
                "la struttura senza dirlo. Usa with_personality per ottenere una copia.")
        object.__setattr__(self, name, value)

    def with_personality(self, personality):
        """Una copia con un altro valore di personalità, ricomposta da zero.

        Serve allo strato di conversione, che cerca un valore capace di soddisfare insieme
        natura, sesso e lucentezza desiderate. Il checksum memorizzato non viene copiato,
        perché riferito a una cifratura diversa non significherebbe nulla: la copia si
        riscrive ricalcolandolo.
        """
        import copy
        clone = copy.deepcopy(self)
        object.__setattr__(clone, "personality", personality & 0xFFFFFFFF)
        object.__setattr__(clone, "checksum_stored", None)
        return clone

    @property
    def is_party(self):
        return self.status is not None

    @property
    def substruct_order(self):
        return substruct_order(self.personality)

    @property
    def is_bad_egg(self):
        """Bit 0 del byte dei flag, da struct BoxPokemon."""
        return bool(self.flags & 0x01)

    @property
    def has_species(self):
        return bool(self.flags & 0x02)

    @property
    def is_egg(self):
        """Il flag di uovo esiste in due posti, qui e in Misc, e il gioco li tiene allineati."""
        return bool(self.flags & 0x04)

    @property
    def block_box_rs(self):
        """Bit 3: Pokemon Box Ruby e Sapphire rifiuta di depositare chi lo ha alzato."""
        return bool(self.flags & 0x08)

    @property
    def is_shiny(self):
        """In generazione 3 la lucentezza non è un pattern di DV ma un conto sui 32 bit.

        Si mettono in XOR le due metà dell'ID dell'allenatore e le due metà del valore di
        personalità, e il Pokemon è cromatico se il risultato sta sotto la soglia. La
        differenza con la generazione 2, dove la lucentezza è un pattern di DV, è la
        ragione per cui un Pokemon cromatico non resta cromatico attraverso una conversione
        se non si sceglie il valore di personalità apposta.
        """
        tid = self.ot_id & 0xFFFF
        sid = (self.ot_id >> 16) & 0xFFFF
        low = self.personality & 0xFFFF
        high = (self.personality >> 16) & 0xFFFF
        return (tid ^ sid ^ low ^ high) < 8

    @property
    def nature_index(self):
        """La natura è il valore di personalità modulo 25, e non è memorizzata da nessuna parte.

        È il primo campo della generazione 3 che non ha alcun corrispondente a monte: le
        generazioni 1 e 2 non hanno nature, quindi una conversione la determina scegliendo
        il valore di personalità, non copiando un dato.
        """
        return self.personality % 25

    @property
    def checksum_computed(self):
        """Il checksum dei quattro blocchi in chiaro, nell'ordine logico.

        L'ordine non conta per il risultato, come spiegato in compute_checksum, ma comporre
        i quarantotto byte nell'ordine logico invece che in quello permutato tiene il codice
        leggibile e non cambia il valore.
        """
        plain = b"".join(getattr(self, name).to_bytes()
                         for name in ("growth", "attacks", "evs", "misc"))
        return compute_checksum(plain)

    @property
    def checksum_ok(self):
        """Vero se il checksum letto dal buffer coincide con quello calcolato.

        None quando non c'è un checksum memorizzato, cioè su una struttura costruita a
        mano e non letta da byte. Un lettore non deve rifiutare un buffer con checksum
        sbagliato, perché è esattamente il caso che si vuole poter diagnosticare: il gioco
        in quella situazione alza il flag di Uovo Peste e distrugge il Pokemon, e uno
        strumento che si limita a sollevare un'eccezione non dice quale dei due sia il dato
        buono.
        """
        if self.checksum_stored is None:
            return None
        return self.checksum_stored == self.checksum_computed

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

        personality = u32(data, OFF_PERSONALITY)
        ot_id = u32(data, OFF_OT_ID)
        plain = crypt_secure(data[OFF_SECURE:OFF_SECURE + SECURE_LENGTH],
                            personality, ot_id)

        # De-permutazione: la riga della tabella dice in quale slot cercare ciascun tipo.
        positions = SUBSTRUCT_POSITIONS[personality % 24]
        parsed = []
        for type_index, slot in enumerate(positions):
            chunk = plain[slot * SUBSTRUCT_LENGTH:(slot + 1) * SUBSTRUCT_LENGTH]
            parsed.append(SUBSTRUCT_TYPES[type_index].from_bytes(chunk))

        mon = cls(
            personality=personality,
            ot_id=ot_id,
            nickname=bytes(data[OFF_NICKNAME:OFF_NICKNAME + NICKNAME_LENGTH]),
            language=data[OFF_LANGUAGE],
            flags=data[OFF_FLAGS],
            ot_name=bytes(data[OFF_OT_NAME:OFF_OT_NAME + OT_NAME_LENGTH]),
            markings=data[OFF_MARKINGS],
            unknown=u16(data, OFF_UNKNOWN),
            growth=parsed[0], attacks=parsed[1], evs=parsed[2], misc=parsed[3],
            checksum_stored=u16(data, OFF_CHECKSUM),
        )
        if party:
            mon.status = u32(data, OFF_STATUS)
            mon.level = data[OFF_LEVEL]
            mon.mail = data[OFF_MAIL]
            mon.stats = {name: u16(data, OFF_STATS + 2 * i)
                         for i, name in enumerate(PARTY_STAT_ORDER)}
        return mon

    def to_bytes(self, party=None, preserve_checksum=False):
        """Ricompone i byte, cifrando e permutando secondo il valore di personalità.

        Il checksum viene ricalcolato, ed è il comportamento di default perché è l'unico
        sicuro: propagare un checksum letto e non più coerente con i dati è precisamente
        il modo di produrre un Uovo Peste. `preserve_checksum` riscrive invece quello
        memorizzato, e serve a due cose legittime, cioè dimostrare che la lettura e la
        riscrittura non perdono un solo bit anche su un buffer arbitrario, e conservare un
        dump corrotto tale e quale per poterlo studiare.
        """
        if party is None:
            party = self.is_party
        if party and not self.is_party:
            raise gb.FormatError("richiesta una struttura di squadra ma i campi di sola "
                                 "squadra non sono presenti")

        buf = bytearray(PARTY_STRUCT_LENGTH if party else BOX_STRUCT_LENGTH)
        put_u32(buf, OFF_PERSONALITY, self.personality)
        put_u32(buf, OFF_OT_ID, self.ot_id)

        if len(self.nickname) != NICKNAME_LENGTH:
            raise gb.FormatError("soprannome lungo %d byte invece di %d"
                                 % (len(self.nickname), NICKNAME_LENGTH))
        if len(self.ot_name) != OT_NAME_LENGTH:
            raise gb.FormatError("nome dell'allenatore lungo %d byte invece di %d"
                                 % (len(self.ot_name), OT_NAME_LENGTH))
        buf[OFF_NICKNAME:OFF_NICKNAME + NICKNAME_LENGTH] = self.nickname
        buf[OFF_LANGUAGE] = self.language & 0xFF
        buf[OFF_FLAGS] = self.flags & 0xFF
        buf[OFF_OT_NAME:OFF_OT_NAME + OT_NAME_LENGTH] = self.ot_name
        buf[OFF_MARKINGS] = self.markings & 0xFF
        put_u16(buf, OFF_UNKNOWN, self.unknown)

        # Permutazione: ogni tipo va nello slot che la tabella gli assegna.
        positions = SUBSTRUCT_POSITIONS[self.personality % 24]
        plain = bytearray(SECURE_LENGTH)
        for type_index, name in enumerate(("growth", "attacks", "evs", "misc")):
            slot = positions[type_index]
            chunk = getattr(self, name).to_bytes()
            plain[slot * SUBSTRUCT_LENGTH:(slot + 1) * SUBSTRUCT_LENGTH] = chunk

        if preserve_checksum:
            if self.checksum_stored is None:
                raise gb.FormatError("nessun checksum memorizzato da conservare: questa "
                                     "struttura non è stata letta da byte")
            checksum = self.checksum_stored
        else:
            checksum = compute_checksum(bytes(plain))
        put_u16(buf, OFF_CHECKSUM, checksum)

        buf[OFF_SECURE:OFF_SECURE + SECURE_LENGTH] = crypt_secure(
            bytes(plain), self.personality, self.ot_id)

        if party:
            put_u32(buf, OFF_STATUS, self.status)
            buf[OFF_LEVEL] = self.level & 0xFF
            buf[OFF_MAIL] = self.mail & 0xFF
            for i, name in enumerate(PARTY_STAT_ORDER):
                put_u16(buf, OFF_STATS + 2 * i, self.stats[name])
        return bytes(buf)

    def refresh_checksum(self):
        """Allinea il checksum memorizzato a quello dei dati attuali.

        Va chiamata dopo aver modificato una sottostruttura, se si intende poi riscrivere
        con `preserve_checksum`. Il percorso di default non ne ha bisogno.
        """
        object.__setattr__(self, "checksum_stored", self.checksum_computed)
        return self.checksum_stored
