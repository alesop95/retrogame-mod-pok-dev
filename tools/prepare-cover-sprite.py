#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Prepara uno sprite per la copertina: sfondo trasparente e margini ritagliati.

Perché esiste
-------------
Lo sprite scaricato ha lo sfondo opaco di un grigio chiarissimo, che su una pagina bianca
si presenta come un rettangolo visibile attorno alla figura. Il canale alfa esiste ma non
è usato. Questo strumento rende trasparenti i pixel di sfondo e ritaglia i margini vuoti,
così che l'immagine si appoggi alla pagina senza cornice e la sua altezza corrisponda alla
figura e non alla tela.

Perché non a mano in un editor
------------------------------
Perché l'operazione va ripetuta se lo sprite cambia, e perché la soglia con cui si decide
che un pixel è sfondo è un parametro che conviene poter rileggere. Un'immagine preparata a
mano in un editor è un dato di cui nessuno sa più come è stato prodotto.

Il vincolo della pixel art
--------------------------
Il ritaglio e la trasparenza non ricampionano nulla: ogni pixel resta dov'era e con il
proprio colore. Lo strumento non ridimensiona, e questo è deliberato. Un'immagine di pixel
art ridimensionata con interpolazione perde i bordi netti che la caratterizzano, e se
serve ingrandirla il fattore deve essere intero e l'interpolazione dev'essere del vicino
più prossimo. Nel documento la dimensione finale si stabilisce in LaTeX, dove l'immagine
viene rimpicciolita e non ingrandita, caso in cui l'artefatto è tollerabile.

Uso
---
    python tools/prepare-cover-sprite.py <sorgente.png> <destinazione.png>
    python tools/prepare-cover-sprite.py <sorgente.png> <destinazione.png> --soglia 12
"""

import argparse
import os
import sys

try:
    from PIL import Image
except ImportError:
    print("serve Pillow: python -m pip install --user Pillow")
    sys.exit(1)


def prepara(sorgente, destinazione, soglia):
    img = Image.open(sorgente).convert("RGBA")
    larghezza, altezza = img.size
    pixel = img.load()

    # Il colore di sfondo si ricava dall'angolo in alto a sinistra invece di essere
    # scritto nel codice: uno sprite diverso può avere un fondo diverso, e leggerlo
    # dall'immagine rende lo strumento riusabile senza modifiche.
    fondo = pixel[0, 0][:3]

    resi_trasparenti = 0
    for y in range(altezza):
        for x in range(larghezza):
            r, g, b, a = pixel[x, y]
            if (abs(r - fondo[0]) <= soglia and abs(g - fondo[1]) <= soglia
                    and abs(b - fondo[2]) <= soglia):
                pixel[x, y] = (r, g, b, 0)
                resi_trasparenti += 1

    # Il ritaglio usa il riquadro dei pixel non trasparenti: se la figura tocca i bordi
    # getbbox restituisce l'intera tela, che è il comportamento corretto.
    riquadro = img.getbbox()
    ritagliata = img.crop(riquadro) if riquadro else img

    ritagliata.save(destinazione, "PNG", optimize=True)
    return {
        "fondo": fondo,
        "originale": (larghezza, altezza),
        "ritagliata": ritagliata.size,
        "trasparenti": resi_trasparenti,
        "byte": os.path.getsize(destinazione),
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("sorgente")
    ap.add_argument("destinazione")
    ap.add_argument("--soglia", type=int, default=8,
                    help="tolleranza per riconoscere un pixel come sfondo, 0 significa "
                         "corrispondenza esatta col colore dell'angolo")
    args = ap.parse_args()

    if not os.path.exists(args.sorgente):
        print("sorgente inesistente: %s" % args.sorgente)
        return 1
    os.makedirs(os.path.dirname(os.path.abspath(args.destinazione)), exist_ok=True)

    esito = prepara(args.sorgente, args.destinazione, args.soglia)
    print("colore di sfondo riconosciuto: RGB%s" % (esito["fondo"],))
    print("pixel resi trasparenti: %d" % esito["trasparenti"])
    print("dimensioni: %dx%d -> %dx%d px"
          % (esito["originale"][0], esito["originale"][1],
             esito["ritagliata"][0], esito["ritagliata"][1]))
    print("scritto %s, %d byte" % (args.destinazione, esito["byte"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
