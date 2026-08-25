# -*- coding: utf-8 -*-
"""Primitivi di lettura e scrittura per le generazioni 1 e 2.

Tutto cio' che sta qui vale per entrambe le generazioni Game Boy e per nessun'altra,
perche' due scelte lo distinguono dalla generazione 3: l'ordine dei byte, che qui e'
big-endian, e l'impaccamento in nibble, che qui e' usato per i valori individuali.

I riferimenti alle fonti sono nei docstring perche' un numero senza provenienza, in un
progetto come questo, e' un numero di cui non si puo' rispondere. La referenza completa
e' DATA-FORMATS_Gen1-Gen2-Gen3.md, sezioni 2 e 4.
"""

# Lunghezze dichiarate nei disassemblati. Gen 1: pokered, constants/pokemon_data_constants.asm
# (BOXMON_STRUCT_LENGTH EQU $21, PARTYMON_STRUCT_LENGTH EQU $2c) e constants/text_constants.asm
# (NAME_LENGTH EQU 11). Gen 2: pokecrystal, stessi file.
NAME_LENGTH = 11
PARTY_LENGTH = 6
BOX_CAPACITY = 20

SPECIES_TERMINATOR = 0xFF
TEXT_TERMINATOR = 0x50

# Ordine delle cinque Stat Experience e dei quattro DV, come stanno in memoria.
STAT_EXP_ORDER = ("hp", "atk", "def", "spd", "spc")
DV_ORDER = ("atk", "def", "spd", "spc")


class FormatError(ValueError):
    """Il buffer non ha la forma attesa. Sempre con abbastanza contesto per il debug."""


def u16(buf, off):
    """Intero a 16 bit big-endian."""
    return (buf[off] << 8) | buf[off + 1]


def put_u16(buf, off, value):
    if not 0 <= value <= 0xFFFF:
        raise FormatError("valore %d fuori intervallo per un campo a 16 bit" % value)
    buf[off] = (value >> 8) & 0xFF
    buf[off + 1] = value & 0xFF


def u24(buf, off):
    """Intero a 24 bit big-endian, il formato dell'esperienza."""
    return (buf[off] << 16) | (buf[off + 1] << 8) | buf[off + 2]


def put_u24(buf, off, value):
    if not 0 <= value <= 0xFFFFFF:
        raise FormatError("valore %d fuori intervallo per un campo a 24 bit" % value)
    buf[off] = (value >> 16) & 0xFF
    buf[off + 1] = (value >> 8) & 0xFF
    buf[off + 2] = value & 0xFF


def read_stat_exp(buf, off):
    """Le cinque Stat Experience consecutive, 2 byte ciascuna."""
    return {name: u16(buf, off + 2 * i) for i, name in enumerate(STAT_EXP_ORDER)}


def write_stat_exp(buf, off, values):
    for i, name in enumerate(STAT_EXP_ORDER):
        put_u16(buf, off + 2 * i, values[name])


def unpack_dvs(hi_byte, lo_byte):
    """Scompone i due byte dei DV nei quattro nibble.

    Ordine verificato su pokecrystal, engine/pokemon/move_mon.asm, routine CalcMonStatC:
    il primo byte porta l'Attacco nel nibble alto e la Difesa nel basso, il secondo la
    Velocita' nel nibble alto e lo Speciale nel basso.
    """
    return {"atk": (hi_byte >> 4) & 0x0F, "def": hi_byte & 0x0F,
            "spd": (lo_byte >> 4) & 0x0F, "spc": lo_byte & 0x0F}


def pack_dvs(dvs):
    """Ricompone i due byte. Inversa esatta di unpack_dvs."""
    for name in DV_ORDER:
        if not 0 <= dvs[name] <= 15:
            raise FormatError("DV %s = %d fuori intervallo 0-15" % (name, dvs[name]))
    return ((dvs["atk"] << 4) | dvs["def"], (dvs["spd"] << 4) | dvs["spc"])


def hp_dv(dvs):
    """Il DV dei punti salute, che non e' memorizzato ma derivato.

    La formula e' scritta come commento nel disassemblato stesso, in CalcMonStatC:
        DV_HP = (DV_ATK & 1) << 3 | (DV_DEF & 1) << 2 | (DV_SPD & 1) << 1 | (DV_SPC & 1)

    Non e' un grado di liberta' indipendente: chi modifica un DV per aggiustare una
    statistica modifica anche i punti salute, e non puo' evitarlo.
    """
    return (((dvs["atk"] & 1) << 3) | ((dvs["def"] & 1) << 2)
            | ((dvs["spd"] & 1) << 1) | (dvs["spc"] & 1))


def is_shiny_gen2(dvs):
    """Lucentezza in generazione 2, che e' un pattern di DV e non un flag.

    Difesa, Velocita' e Speciale a 10, e Attacco in un insieme di otto valori.
    """
    return (dvs["def"] == 10 and dvs["spd"] == 10 and dvs["spc"] == 10
            and dvs["atk"] in (2, 3, 6, 7, 10, 11, 14, 15))


def unpack_pp(byte):
    """Scompone un byte di PP: sei bit bassi i PP correnti, due bit alti i PP Up.

    In generazione 3 queste due informazioni finiscono in sottostrutture diverse, quindi
    la conversione deve smontare questo byte e distribuirlo su due posti.
    """
    return byte & 0x3F, (byte >> 6) & 0x03


def pack_pp(pp, pp_ups):
    if not 0 <= pp <= 63:
        raise FormatError("PP %d fuori intervallo 0-63" % pp)
    if not 0 <= pp_ups <= 3:
        raise FormatError("PP Up %d fuori intervallo 0-3" % pp_ups)
    return (pp_ups << 6) | pp


def read_name_array(buf, off, count, length=NAME_LENGTH):
    """Legge un array di nomi come byte grezzi.

    I nomi restano byte e non diventano testo: la transcodifica e' un'operazione a parte,
    in charmap.py, e tenerla separata e' cio' che rende possibile la prova di simmetria,
    perche' nessun byte viene perso per strada.
    """
    return [bytes(buf[off + i * length: off + (i + 1) * length]) for i in range(count)]


def write_name_array(buf, off, names, length=NAME_LENGTH):
    for i, name in enumerate(names):
        if len(name) != length:
            raise FormatError("nome in posizione %d lungo %d byte invece di %d"
                              % (i, len(name), length))
        buf[off + i * length: off + (i + 1) * length] = name
