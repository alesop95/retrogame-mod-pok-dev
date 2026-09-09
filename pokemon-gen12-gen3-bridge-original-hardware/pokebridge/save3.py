# -*- coding: utf-8 -*-
"""Lo strato del salvataggio di generazione 3: 128 KiB di flash, due slot, quattordici sezioni.

Perche' questo strato esiste, e perche' arriva ora
--------------------------------------------------
Il modulo `gen3` sa comporre e leggere un esemplare, cioe' ottanta byte cifrati e permutati. Non
sa dove metterlo. Questo modulo e' il contenitore: apre un file da 128 KiB come quello che un
lettore di cartucce produce, dice quale dei due slot sia quello valido, ricompone i buffer che le
sezioni frammentano, e permette di leggere e scrivere le posizioni del deposito e della squadra
ricalcolando i checksum. E' il pezzo che trasforma un lotto di file in un salvataggio caricabile,
e il pezzo che permette di leggere un salvataggio reale invece di un vettore costruito.

La struttura, e le tre cose che la rendono diversa da un salvataggio lineare
---------------------------------------------------------------------------
La prima e' che i dati logici sono spezzati in sezioni da 4096 byte di cui solo 3968 sono dati:
gli ultimi dodici byte portano identificatore, checksum, firma e indice di salvataggio, e il resto
e' riempimento. Ricomporre un buffer logico significa quindi concatenare i primi 3968 byte delle
sezioni nell'ordine dei loro identificatori, che nel file non e' garantito.

La seconda e' che gli slot sono due e si alternano a ogni salvataggio, perche' la flash si scrive
a blocchi e un'interruzione a metta' non deve distruggere l'unica copia. Lo slot valido e' quello
con l'indice di salvataggio maggiore, e la regola in caso di parita' va scritta perche' e' l'unico
punto dove due implementazioni ragionevoli divergono: qui lo slot A vince soltanto se il suo
indice e' strettamente maggiore, quindi a parita' vince B.

La terza e' che il checksum non copre la sezione intera ma i suoi 3968 byte di dati, si accumula
come somma di parole da 32 bit little-endian su una variabile a 32 bit, e si chiude sommando i
sedici bit alti ai sedici bassi. La verifica di questa formula sta nel `--self-test` e la sua
provenienza nella sezione 6 della referenza, con la conferma sul sorgente del verificatore.

Che cosa questo modulo non fa
-----------------------------
Non interpreta il contenuto delle sezioni oltre alla squadra e al deposito, perche' e' il minimo
che serve a portare esemplari dentro e fuori: la chiave di sicurezza, lo zaino e il resto della
sezione zero appartengono al track dell'inventario e hanno gia' il loro strumento. Non scrive
alcun file da se': espone i byte e chi chiama decide dove metterli, cosicche' nessuna operazione
distruttiva possa avvenire per un errore di questo modulo.
"""

import struct

SEZIONE = 0x1000          # 4096, la sezione fisica
DATI_SEZIONE = 0x0F80     # 3968, i byte di dati dentro la sezione
SEZIONI_PER_SLOT = 14
SLOT = SEZIONI_PER_SLOT * SEZIONE   # 57344
DIMENSIONE = 0x20000      # 128 KiB

OFF_ID = 0x0FF4
OFF_CHECKSUM = 0x0FF6
OFF_FIRMA = 0x0FF8
OFF_INDICE = 0x0FFC
FIRMA = 0x08012025

# I buffer logici e le sezioni che li compongono, secondo la referenza e il verificatore.
SEZIONI_SMALL = (0,)
SEZIONI_LARGE = (1, 2, 3, 4)
SEZIONI_STORAGE = (5, 6, 7, 8, 9, 10, 11, 12, 13)

# Il deposito, dentro il buffer ricomposto delle sezioni da 5 a 13.
OFF_BOX_CORRENTE = 0x0000
OFF_RECORD = 0x0004
RECORD = 80
POSIZIONI = 420
OFF_NOMI_BOX = 0x8344
PASSO_NOME_BOX = 9
OFF_SFONDI = 0x83C2
DEPOSITO_UTILE = 0x83D0   # 33744, la parte del buffer che il gioco usa

# La squadra, dentro il buffer ricomposto delle sezioni da 1 a 4. I due offset differiscono fra i
# titoli di Hoenn e quelli di Kanto rifatto, ed e' la ragione per cui il gioco va dichiarato:
# leggere la squadra all'offset sbagliato non produce un errore ma sei strutture di rumore.
OFFSET_SQUADRA = {
    "RSE": (0x0234, 0x0238),
    "FRLG": (0x0034, 0x0038),
}
STRUTTURA_SQUADRA = 100
SQUADRA_MAX = 6


def checksum(dati):
    """Il checksum di una sezione: somma delle parole da 32 bit, poi alti piu' bassi."""
    totale = 0
    for (parola,) in struct.iter_unpack("<I", dati[:DATI_SEZIONE]):
        totale = (totale + parola) & 0xFFFFFFFF
    return (totale + (totale >> 16)) & 0xFFFF


class Sezione(object):
    """Una sezione fisica, con il suo piede letto e non assunto."""

    def __init__(self, grezzo, posizione):
        self.posizione = posizione
        self.dati = bytearray(grezzo[:DATI_SEZIONE])
        self.id = struct.unpack_from("<H", grezzo, OFF_ID)[0]
        self.checksum = struct.unpack_from("<H", grezzo, OFF_CHECKSUM)[0]
        self.firma = struct.unpack_from("<I", grezzo, OFF_FIRMA)[0]
        self.indice = struct.unpack_from("<I", grezzo, OFF_INDICE)[0]

    @property
    def firma_valida(self):
        return self.firma == FIRMA

    @property
    def checksum_valido(self):
        return self.checksum == checksum(self.dati)

    @property
    def valida(self):
        return self.firma_valida and self.checksum_valido and self.id < SEZIONI_PER_SLOT


class Save3(object):
    """Un salvataggio di generazione 3, con i suoi due slot e i suoi buffer ricomposti."""

    def __init__(self, dati, gioco="RSE"):
        if len(dati) < 2 * SLOT:
            raise ValueError("il salvataggio e' piu' corto dei due slot: %d byte" % len(dati))
        if gioco not in OFFSET_SQUADRA:
            raise ValueError("gioco ignoto: %r, attesi %s" % (gioco, sorted(OFFSET_SQUADRA)))
        self.grezzo = bytearray(dati)
        self.gioco = gioco
        self.slot = [self._leggi_slot(0), self._leggi_slot(1)]
        self.attivo = self._scegli_slot()

    # ----------------------------------------------------------------- lettura della struttura

    def _leggi_slot(self, quale):
        base = quale * SLOT
        return [Sezione(self.grezzo[base + i * SEZIONE: base + (i + 1) * SEZIONE],
                        base + i * SEZIONE)
                for i in range(SEZIONI_PER_SLOT)]

    def _indice_slot(self, quale):
        """L'indice di salvataggio di uno slot, preso dalle sole sezioni valide.

        Prendere l'indice da una sezione qualunque sarebbe un errore silenzioso: una sezione con
        la firma sbagliata porta byte che non sono un indice, e su un file mai scritto in quello
        slot sarebbero 0xFFFFFFFF, cioe' il valore piu' grande possibile.
        """
        indici = [s.indice for s in self.slot[quale] if s.firma_valida]
        return max(indici) if indici else None

    def _scegli_slot(self):
        a, b = self._indice_slot(0), self._indice_slot(1)
        if a is None and b is None:
            return None
        if b is None:
            return 0
        if a is None:
            return 1
        return 0 if a > b else 1

    def sezioni_valide(self, quale=None):
        quale = self.attivo if quale is None else quale
        return [s for s in self.slot[quale] if s.valida]

    def integro(self, quale=None):
        """Uno slot e' integro quando porta tutte e quattordici le sezioni, valide e distinte."""
        quale = self.attivo if quale is None else quale
        if quale is None:
            return False
        valide = self.sezioni_valide(quale)
        return len(valide) == SEZIONI_PER_SLOT and len({s.id for s in valide}) == SEZIONI_PER_SLOT

    # ----------------------------------------------------------------- i buffer logici

    def _buffer(self, ids, quale=None):
        quale = self.attivo if quale is None else quale
        per_id = {s.id: s for s in self.slot[quale] if s.firma_valida}
        fuori = bytearray()
        for i in ids:
            if i not in per_id:
                raise ValueError("manca la sezione %d nello slot %d" % (i, quale))
            fuori += per_id[i].dati
        return fuori

    def small(self, quale=None):
        return self._buffer(SEZIONI_SMALL, quale)

    def large(self, quale=None):
        return self._buffer(SEZIONI_LARGE, quale)

    def storage(self, quale=None):
        return self._buffer(SEZIONI_STORAGE, quale)

    # ----------------------------------------------------------------- deposito e squadra

    def box_corrente(self):
        return struct.unpack_from("<I", self.storage(), OFF_BOX_CORRENTE)[0]

    def leggi_posizione(self, indice):
        """Gli ottanta byte di una posizione del deposito, nella loro forma cifrata."""
        if not 0 <= indice < POSIZIONI:
            raise ValueError("posizione fuori intervallo: %d" % indice)
        buf = self.storage()
        off = OFF_RECORD + indice * RECORD
        return bytes(buf[off:off + RECORD])

    def scrivi_posizione(self, indice, record):
        """Scrive una posizione del deposito e ricalcola i checksum delle sezioni toccate."""
        if not 0 <= indice < POSIZIONI:
            raise ValueError("posizione fuori intervallo: %d" % indice)
        if len(record) != RECORD:
            raise ValueError("il record del deposito misura %d byte, non %d" % (RECORD, len(record)))
        self._scrivi_in_buffer(SEZIONI_STORAGE, OFF_RECORD + indice * RECORD, record)

    def conteggio_squadra(self):
        off, _ = OFFSET_SQUADRA[self.gioco]
        return struct.unpack_from("<I", self.large(), off)[0]

    def leggi_squadra(self, indice):
        """I cento byte di una posizione della squadra, nella loro forma cifrata."""
        if not 0 <= indice < SQUADRA_MAX:
            raise ValueError("posizione di squadra fuori intervallo: %d" % indice)
        _, off = OFFSET_SQUADRA[self.gioco]
        buf = self.large()
        inizio = off + indice * STRUTTURA_SQUADRA
        return bytes(buf[inizio:inizio + STRUTTURA_SQUADRA])

    def nome_box(self, indice):
        if not 0 <= indice < SEZIONI_PER_SLOT:
            raise ValueError("box fuori intervallo: %d" % indice)
        buf = self.storage()
        off = OFF_NOMI_BOX + indice * PASSO_NOME_BOX
        return bytes(buf[off:off + PASSO_NOME_BOX])

    # ----------------------------------------------------------------- scrittura

    def _scrivi_in_buffer(self, ids, offset, blocco):
        """Scrive dentro un buffer logico, riportando i byte nelle sezioni che li ospitano.

        E' il punto in cui la frammentazione conta: un record da ottanta byte che cade a cavallo
        fra due sezioni va spezzato, e scriverlo come se il buffer fosse contiguo sovrascriverebbe
        il piede di una sezione. La divisione la fa l'aritmetica qui sotto e non chi chiama.
        """
        quale = self.attivo
        if quale is None:
            raise ValueError("nessuno slot valido: non si scrive su un salvataggio non letto")
        per_id = {s.id: s for s in self.slot[quale] if s.firma_valida}
        toccate = []
        scritto = 0
        while scritto < len(blocco):
            assoluto = offset + scritto
            quale_sezione = ids[assoluto // DATI_SEZIONE]
            dentro = assoluto % DATI_SEZIONE
            quanti = min(DATI_SEZIONE - dentro, len(blocco) - scritto)
            if quale_sezione not in per_id:
                raise ValueError("manca la sezione %d nello slot attivo" % quale_sezione)
            sezione = per_id[quale_sezione]
            sezione.dati[dentro:dentro + quanti] = blocco[scritto:scritto + quanti]
            toccate.append(sezione)
            scritto += quanti
        for sezione in toccate:
            sezione.checksum = checksum(sezione.dati)

    def to_bytes(self):
        """Il salvataggio come byte, con le sezioni dello slot attivo riscritte e richecksummate."""
        fuori = bytearray(self.grezzo)
        for quale in (0, 1):
            for sezione in self.slot[quale]:
                base = sezione.posizione
                fuori[base:base + DATI_SEZIONE] = sezione.dati
                struct.pack_into("<H", fuori, base + OFF_ID, sezione.id)
                struct.pack_into("<H", fuori, base + OFF_CHECKSUM, sezione.checksum)
                struct.pack_into("<I", fuori, base + OFF_FIRMA, sezione.firma)
                struct.pack_into("<I", fuori, base + OFF_INDICE, sezione.indice)
        return bytes(fuori)


def record_da_file(dati):
    """Da un file dell'editor alla forma che il salvataggio vuole: permutata e cifrata.

    I due formati non sono lo stesso, e la differenza costa un lotto se si scopre tardi. Un file
    con estensione pk3 e' scritto nella forma che l'editor usa in memoria, cioe' in chiaro e con
    le quattro sottostrutture nell'ordine logico; dentro un salvataggio quelle quarantotto byte
    sono permutate secondo il valore di personalita' e mascherate in XOR con la chiave derivata.
    Scrivere il file cosi' come e' dentro una posizione del deposito produce un esemplare che il
    gioco marca come Uovo Peste, e il difetto non si vede finche' non si carica la partita.

    Il checksum non si ricalcola qui: e' calcolato sui dati in chiaro e la permutazione non lo
    cambia, perche' e' una somma e la somma non dipende dall'ordine dei blocchi.
    """
    from pokebridge.gen3 import (OFF_SECURE, SECURE_LENGTH, SUBSTRUCT_LENGTH,
                                 SUBSTRUCT_POSITIONS, crypt_secure, u32)
    if len(dati) < OFF_SECURE + SECURE_LENGTH:
        raise ValueError("servono almeno %d byte, ricevuti %d"
                         % (OFF_SECURE + SECURE_LENGTH, len(dati)))
    personality = u32(dati, 0x00)
    ot_id = u32(dati, 0x04)
    logico = dati[OFF_SECURE:OFF_SECURE + SECURE_LENGTH]
    posizioni = SUBSTRUCT_POSITIONS[personality % 24]
    permutato = bytearray(SECURE_LENGTH)
    for tipo, slot in enumerate(posizioni):
        permutato[slot * SUBSTRUCT_LENGTH:(slot + 1) * SUBSTRUCT_LENGTH] = \
            logico[tipo * SUBSTRUCT_LENGTH:(tipo + 1) * SUBSTRUCT_LENGTH]
    cifrato = crypt_secure(bytes(permutato), personality, ot_id)
    return bytes(dati[:OFF_SECURE]) + cifrato


def file_da_record(record):
    """L'inverso: da una posizione del deposito alla forma dell'editor, in chiaro e in ordine."""
    from pokebridge.gen3 import (OFF_SECURE, SECURE_LENGTH, SUBSTRUCT_LENGTH,
                                 SUBSTRUCT_POSITIONS, crypt_secure, u32)
    if len(record) < OFF_SECURE + SECURE_LENGTH:
        raise ValueError("servono almeno %d byte, ricevuti %d"
                         % (OFF_SECURE + SECURE_LENGTH, len(record)))
    personality = u32(record, 0x00)
    ot_id = u32(record, 0x04)
    permutato = crypt_secure(record[OFF_SECURE:OFF_SECURE + SECURE_LENGTH], personality, ot_id)
    posizioni = SUBSTRUCT_POSITIONS[personality % 24]
    logico = bytearray(SECURE_LENGTH)
    for tipo, slot in enumerate(posizioni):
        logico[tipo * SUBSTRUCT_LENGTH:(tipo + 1) * SUBSTRUCT_LENGTH] = \
            permutato[slot * SUBSTRUCT_LENGTH:(slot + 1) * SUBSTRUCT_LENGTH]
    return bytes(record[:OFF_SECURE]) + bytes(logico)


def crea_vuoto(gioco="RSE", indice=1):
    """Un salvataggio sintetico da 128 KiB, valido e vuoto.

    Serve a due cose che il progetto aveva dichiarato in sospeso. La prima e' collaudare lo strato
    del deposito senza avere un salvataggio reale, che e' cio' che ha permesso di scrivere questo
    modulo prima che il lettore arrivasse. La seconda e' produrre il contenitore da confrontare
    con quello che il verificatore genera, che e' la prova che manca alla simmetria: due
    implementazioni indipendenti che producono lo stesso file.

    Lo slot A porta l'indice richiesto e lo slot B resta non scritto, cioe' con la firma a zero,
    che e' lo stato di una flash mai usata per quello slot e il caso che la scelta dello slot deve
    trattare senza confondersi.
    """
    dati = bytearray(DIMENSIONE)
    for i in range(SEZIONI_PER_SLOT):
        base = i * SEZIONE
        struct.pack_into("<H", dati, base + OFF_ID, i)
        struct.pack_into("<I", dati, base + OFF_FIRMA, FIRMA)
        struct.pack_into("<I", dati, base + OFF_INDICE, indice)
        struct.pack_into("<H", dati, base + OFF_CHECKSUM,
                         checksum(dati[base:base + DATI_SEZIONE]))
    return Save3(bytes(dati), gioco)
