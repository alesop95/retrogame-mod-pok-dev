# -*- coding: utf-8 -*-
"""Transcodifica del testo, sulle tabelle generate dai disassemblati.

Le tabelle non stanno qui: stanno in data/, prodotte da tools/extract_charmaps.py dai
charmap di pret. La ragione e' in docs/05-testo-e-charmap.md, e in breve e' che le fonti
secondarie sbagliavano quelle tabelle in due punti, con un errore che produce nomi
plausibili e sbagliati invece di un fallimento visibile. Una tabella scritta a mano si
puo' sbagliare di nuovo a mano; una generata no.

Questo modulo non decide che fare dei caratteri che in generazione 3 non esistono: li
segnala. E' una decisione di prodotto, non un dettaglio di codifica, e va presa dal
chiamante in modo esplicito.
"""

import json
import os

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")

GEN12_TERMINATOR = 0x50
GEN3_TERMINATOR = 0xFF


class UntranslatableCharacter(ValueError):
    """Un byte di generazione 1 o 2 senza corrispondente in generazione 3."""

    def __init__(self, byte, char):
        self.byte = byte
        self.char = char
        super().__init__("il byte 0x%02X, che rende %r, non esiste in generazione 3"
                         % (byte, char))


def _load(name):
    with open(os.path.join(DATA_DIR, name), encoding="utf-8") as fh:
        return json.load(fh)


class Charmap:
    """Una delle due tabelle, con decodifica e codifica."""

    def __init__(self, payload):
        self.terminator = payload["terminatore"]
        self.space = payload["spazio"]
        self.byte_to_char = {int(k, 16): v for k, v in payload["stampabili"].items()}
        self.control = {int(k, 16): v for k, v in payload["controllo"].items()}
        self.char_to_byte = {}
        for byte, char in sorted(self.byte_to_char.items()):
            self.char_to_byte.setdefault(char, byte)
        self.source = payload["fonte"]

    @classmethod
    def gen12(cls):
        return cls(_load("charmap-gen12.json"))

    @classmethod
    def gen3(cls):
        return cls(_load("charmap-gen3.json"))

    def decode(self, raw, stop_at_terminator=True):
        """Da byte a testo. I byte non stampabili diventano una forma leggibile.

        Non solleva mai: una decodifica che fallisce su un salvataggio corrotto non
        aiuta nessuno, mentre vedere dove sta il byte strano aiuta.
        """
        out = []
        for byte in raw:
            if byte == self.terminator and stop_at_terminator:
                break
            if byte in self.byte_to_char:
                out.append(self.byte_to_char[byte])
            elif byte in self.control:
                out.append("{%s}" % self.control[byte])
            else:
                out.append("\\x%02X" % byte)
        return "".join(out)

    def encode(self, text, length=None):
        """Da testo a byte, con riempimento al terminatore se length e' data."""
        out = bytearray()
        for char in text:
            if char not in self.char_to_byte:
                raise ValueError("il carattere %r non esiste in questa codifica" % char)
            out.append(self.char_to_byte[char])
        if length is not None:
            if len(out) >= length:
                out = out[:length - 1]
            out.append(self.terminator)
            while len(out) < length:
                out.append(self.terminator)
        return bytes(out)


class Gen12ToGen3:
    """La traduzione diretta fra i due spazi di codifica.

    E' questa la tabella che un convertitore usa davvero: tradurre passando dal testo
    farebbe due conversioni invece di una e introdurrebbe un punto in cui perdere byte.
    """

    def __init__(self):
        payload = _load("charmap-gen12-to-gen3.json")
        self.mapping = {int(k, 16): int(v, 16) for k, v in payload["traduzione"].items()}
        self.orphans = {int(k, 16): v for k, v in payload["senza_destinazione"].items()}

    def translate(self, raw, length, on_missing="raise", filler=None):
        """Traduce un nome, troncandolo e terminandolo alla lunghezza di destinazione.

        Il parametro on_missing rende esplicita la decisione sui caratteri privi di
        destinazione: "raise" si ferma, "skip" li salta, "replace" li sostituisce con
        filler. Nessuno dei tre e' il comportamento corretto in assoluto, e per questo
        non c'e' un valore di default silenzioso che non sia il fallimento.
        """
        out = bytearray()
        for byte in raw:
            if byte == GEN12_TERMINATOR:
                break
            if byte in self.mapping:
                out.append(self.mapping[byte])
                continue
            if on_missing == "raise":
                raise UntranslatableCharacter(byte, self.orphans.get(byte, "?"))
            if on_missing == "skip":
                continue
            if on_missing == "replace":
                if filler is None:
                    raise ValueError("on_missing=replace richiede un filler")
                out.append(filler)
                continue
            raise ValueError("on_missing sconosciuto: %r" % on_missing)

        if len(out) > length:
            out = out[:length]
        while len(out) < length:
            out.append(GEN3_TERMINATOR)
        return bytes(out)
