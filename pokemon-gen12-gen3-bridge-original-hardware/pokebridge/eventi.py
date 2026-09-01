# -*- coding: utf-8 -*-
"""Generazione pseudocasuale degli esemplari da evento della terza generazione.

Che cosa contiene, e perché è un modulo a sé
--------------------------------------------
Il modulo `gen3` sa comporre e cifrare la struttura di un esemplare, cioè sa dove vanno i
byte. Non sa da dove vengono i valori. Per un esemplare da evento quei valori non sono
scelti da chi lo costruisce ma prodotti da un generatore pseudocasuale a partire da un seme,
e riprodurre quella produzione è ciò che distingue una ricreazione fedele da un dato
inventato che per caso passa i controlli.

La distinzione ha una conseguenza pratica sulla struttura del codice, e per questo il modulo
è separato: `gen3` è un lettore e uno scrittore di formato, e sarebbe corretto anche se il
generatore non esistesse; questo modulo è la ricostruzione di un comportamento osservato, e
il suo grado di verità è diverso. Tenerli insieme mescolerebbe due gradi di certezza.

Il generatore
-------------
La terza generazione impiega un generatore congruenziale lineare a 32 bit, cioè la ricorrenza
`s(n+1) = (a * s(n) + c) mod 2^32` con `a = 0x41C64E6D` e `c = 0x6073`. Di ogni stato il
gioco usa la sola metà alta, cioè `s >> 16`, e la ragione è nota e generale: nei generatori
di questa famiglia il bit di posizione `k` ha periodo `2^(k+1)`, quindi i bit bassi sono
quasi periodici e inservibili, mentre i bit alti sono quelli buoni.

L'ordine invertito, e la sigla BACD
-----------------------------------
Un incontro ordinario consuma quattro estrazioni consecutive. Chiamandole `A`, `B`, `C`, `D`
nell'ordine in cui escono, le prime due compongono il valore di personalità e le altre due i
valori individuali. In un incontro ordinario `A` va nella metà bassa del valore di
personalità e `B` in quella alta. In un esemplare da evento le due assegnazioni sono
scambiate: `B` va nella metà bassa e `A` in quella alta, cioè il valore di personalità è
`(A << 16) | B`. Non si tratta di un algoritmo diverso ma del medesimo generatore letto in un
ordine diverso, e la sigla con cui la comunità nomina la famiglia dei metodi che ne
discendono, cioè BACD, è la trascrizione di quell'ordine.

I valori individuali si compongono invece nello stesso modo dei casi ordinari: la terza
estrazione porta punti vita, attacco e difesa, la quarta velocità, attacco speciale e difesa
speciale, cinque bit per campo a partire dal bit meno significativo.

Il grado di verifica di questo modulo
-------------------------------------
Le formule qui scritte non sono inferite dalla prosa di una fonte: sono state cercate fra le
composizioni plausibili e selezionate perché riproducono un corpus di esemplari conservati.
La verifica sta in `tests/test_eventi.py` sui vettori riportati là, e la verifica estesa sui
209 esemplari del corpus completo la esegue `tools/confronta-ace-builder.py`, che li legge da
una copia locale non versionata. L'esito registrato il 2026-09-01 è che il valore di
personalità si riproduce su 208 vettori su 209, i valori individuali su 209 su 209, e la
derivazione del sesso dell'allenatore su tutti i 125 esemplari degli eventi che la usano.

Il vettore che non si riproduce è documentato e non è una lacuna del modulo: il valore di
personalità dichiarato accanto al suo seme differisce di due unità nella metà bassa da quello
che quel seme produce, mentre i suoi valori individuali si riproducono esattamente dallo
stesso seme, il che rende quella voce internamente incoerente. Una sola eccezione spiegata
vale più di duecentootto conferme, perché un modello che spiega anche il caso deviante è
diverso da un modello che ha avuto fortuna.
"""

from pokebridge import gb

MOLTIPLICATORE = 0x41C64E6D
INCREMENTO = 0x6073
MODULO = 0x100000000

# I sei campi dei valori individuali, nell'ordine in cui le due estrazioni li producono.
# L'ordine non è quello in cui il gioco li mostra e non è quello alfabetico: è quello del
# generatore, e scriverlo qui evita di dedurlo ogni volta dalla posizione dei bit.
ORDINE_IV = ("ps", "attacco", "difesa", "velocita", "attacco_speciale", "difesa_speciale")

# Le derivazioni del sesso dell'allenatore di provenienza che questo modulo implementa. Le
# altre esistono e non sono implementate: si dichiarano qui perché un elenco di ciò che manca
# è più utile di un errore generico al momento della chiamata.
DERIVAZIONI_SESSO = ("RandS7",)
DERIVAZIONI_NOTE_NON_IMPLEMENTATE = ("RandD3", "RandS3", "RandSG15", "RandAlgo", "Recipient")


def avanza(stato):
    """Un passo del generatore congruenziale lineare della terza generazione."""
    return (MOLTIPLICATORE * (stato & 0xFFFFFFFF) + INCREMENTO) % MODULO


def estrazioni(seme, quante):
    """Le metà alte dei primi `quante` stati successivi al seme.

    Restituisce le metà alte e non gli stati, perché la metà alta è ciò che il gioco usa e
    tenere lo stato completo nell'interfaccia inviterebbe a usarne i bit bassi, che sono
    quasi periodici.
    """
    if quante < 0:
        raise gb.FormatError("il numero di estrazioni non può essere negativo")
    stato, fuori = seme & 0xFFFFFFFF, []
    for _ in range(quante):
        stato = avanza(stato)
        fuori.append(stato >> 16)
    return fuori


def spacchetta_iv(parola):
    """I tre valori individuali contenuti in una estrazione, cinque bit ciascuno."""
    return (parola & 31, (parola >> 5) & 31, (parola >> 10) & 31)


def personalita_e_iv(seme):
    """Il valore di personalità e i sei valori individuali di un esemplare da evento.

    L'inversione descritta nel docstring del modulo sta in questa riga sola, e vale
    ripeterla perché è il punto in cui una ricreazione sbaglia: la prima estrazione va nella
    metà alta, la seconda nella metà bassa.
    """
    a, b, terza, quarta = estrazioni(seme, 4)
    personalita = ((a << 16) | b) & 0xFFFFFFFF
    ps, attacco, difesa = spacchetta_iv(terza)
    velocita, speciale_attacco, speciale_difesa = spacchetta_iv(quarta)
    iv = {
        "ps": ps,
        "attacco": attacco,
        "difesa": difesa,
        "velocita": velocita,
        "attacco_speciale": speciale_attacco,
        "difesa_speciale": speciale_difesa,
    }
    return personalita, iv


def sesso_allenatore_rand_s7(seme):
    """Il sesso dell'allenatore di provenienza secondo la derivazione a scorrimento di sette.

    Cinque avanzamenti dal seme, poi il bit di posizione sette della metà alta, negato: se il
    risultato è uno l'allenatore è femmina. La negazione non è un abbellimento e va conservata
    così com'è: senza di essa la formula sbaglia esattamente tutti i casi invece di metà, che è
    il modo in cui questo genere di errore si nasconde meglio.

    Il numero cinque va notato perché non è deducibile dalla struttura: il sesso è determinato
    dopo il valore di personalità e i valori individuali, che consumano quattro estrazioni, e
    la quinta è quella che lo decide.
    """
    stato = seme & 0xFFFFFFFF
    for _ in range(5):
        stato = avanza(stato)
    return "femmina" if (((stato >> 16) >> 7) & 1) == 0 else "maschio"


def semi_a_sedici_bit():
    """I semi ammessi dai metodi che li restringono a sedici bit.

    Molti metodi da evento dichiarano il seme ristretto a sedici bit, e la restrizione è ciò
    che rende esauribile la ricerca inversa: sono 65536 possibilità, cioè un insieme che si
    percorre interamente in una frazione di secondo, e non 2^32.
    """
    return range(0x10000)


def cerca_seme(personalita, iv=None):
    """I semi a sedici bit che producono quel valore di personalità, e se dato quegli IV.

    È la ricerca inversa, ed è esaustiva e non euristica perché lo spazio è piccolo: si
    prova ogni seme. Restituisce una lista, perché più semi possono produrre lo stesso valore
    di personalità e sarebbe scorretto restituirne uno solo dando l'impressione che sia unico.
    """
    trovati = []
    for seme in semi_a_sedici_bit():
        p, valori = personalita_e_iv(seme)
        if p != (personalita & 0xFFFFFFFF):
            continue
        if iv is not None and any(valori[k] != iv[k] for k in iv):
            continue
        trovati.append(seme)
    return trovati
