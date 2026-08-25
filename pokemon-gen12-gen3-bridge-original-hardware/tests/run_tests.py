# -*- coding: utf-8 -*-
"""Esecutore dei test, senza dipendenze esterne.

    python tests/run_tests.py

Usa unittest della libreria standard, per la stessa ragione per cui il resto del
progetto non ha dipendenze: gli strati di formato sono aritmetica su interi, e un
progetto che si collauda con la sola libreria standard resta eseguibile fra dieci anni.
"""

import os
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)

if __name__ == "__main__":
    suite = unittest.defaultTestLoader.discover(HERE, pattern="test_*.py", top_level_dir=ROOT)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    sys.exit(0 if result.wasSuccessful() else 1)
