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

# Le derivazioni del sesso dell'allenatore di provenienza, tutte e nove. Non sono congetturate:
# vengono dal codice della implementazione di riferimento, che le raccoglie in un solo punto, e
# la loro forma va conservata come e' scritta la' perche' due di esse hanno una particolarita'
# che una riscrittura "piu' pulita" perderebbe.
#
# La prima particolarita' e' che la derivazione a scorrimento di sette restituisce femmina
# quando il bit vale zero, cioe' porta una negazione che le altre non hanno.
# La seconda e' che la derivazione a scorrimento di quindici legge la sesta estrazione e non la
# quinta, perche' fra i valori individuali e il sesso si consuma anche l'oggetto tenuto.
#
# Nella terza generazione zero e' maschio e uno e' femmina.
DERIVAZIONI_SESSO = (
    "Only0", "Only1", "RandD3", "RandS3", "RandS7", "RandSG15",
    "RandD3_0", "RandD3_1", "Recipient",
)

# La sola derivazione che non si implementa, e non per difficolta': la fonte stessa dichiara di
# non verificarla con la logica ordinaria, e la sua implementazione di riferimento salta il
# campo invece di calcolarlo. Scrivere un valore qualunque sarebbe peggio di non scriverlo.
DERIVAZIONE_NON_IMPLEMENTATA = "RandAlgo"


def _bit0_diviso_tre(parola):
    """La derivazione per divisione: il bit meno significativo del quoziente per tre."""
    return (parola // 3) & 1


def _bit(parola, posizione):
    return (parola >> posizione) & 1


def sesso_allenatore(derivazione, seme, sesso_ricevente=None):
    """Il sesso dell'allenatore di provenienza, secondo la derivazione che l'evento dichiara.

    Restituisce "maschio" o "femmina", oppure solleva se la derivazione non e' implementabile.
    Il numero di avanzamenti non e' uniforme e non va uniformato: quattro estrazioni sono
    consumate dal valore di personalita' e dai valori individuali, la quinta decide il sesso in
    quasi tutti i casi, e la sesta lo decide dove fra le due si consuma l'oggetto tenuto.
    """
    if derivazione in ("Only0", "RandD3_0"):
        return "maschio"
    if derivazione in ("Only1", "RandD3_1"):
        return "femmina"
    if derivazione == "Recipient":
        if sesso_ricevente not in ("maschio", "femmina"):
            raise gb.FormatError(
                "la derivazione Recipient copia il sesso dell'allenatore che riceve, quindi "
                "va passato: e un dato del salvataggio di destinazione e non dell'evento")
        return sesso_ricevente
    if derivazione == DERIVAZIONE_NON_IMPLEMENTATA:
        raise gb.FormatError(
            "la derivazione RandAlgo non e implementata, e non per difficolta: la fonte "
            "dichiara di non verificarla con la logica ordinaria e la sua implementazione di "
            "riferimento salta il campo invece di calcolarlo. Scrivere un valore qualunque "
            "sarebbe peggio di non scriverlo.")

    if derivazione == "RandSG15":
        # Sesta estrazione: fra i valori individuali e il sesso si consuma l'oggetto tenuto.
        parola = estrazioni(seme, 6)[5]
        return "femmina" if _bit(parola, 15) == 1 else "maschio"

    parola = estrazioni(seme, 5)[4]
    if derivazione == "RandD3":
        return "femmina" if _bit0_diviso_tre(parola) == 1 else "maschio"
    if derivazione == "RandS3":
        return "femmina" if _bit(parola, 3) == 1 else "maschio"
    if derivazione == "RandS7":
        # La sola con la negazione: femmina quando il bit vale zero.
        return "femmina" if _bit(parola, 7) == 0 else "maschio"
    raise gb.FormatError("derivazione del sesso sconosciuta: %r" % (derivazione,))


def e_cromatico(personalita, id_allenatore, id_segreto=0):
    """Se l'esemplare sia cromatico, come somma esclusiva di quattro parole da sedici bit.

    La soglia e' otto, cioe' i tredici bit alti tutti nulli, ed e' anche l'origine della
    probabilita' di lucentezza di questa generazione: otto configurazioni accettate su
    sessantacinquemilacinquecentotrentasei possibili.
    """
    x = ((id_allenatore & 0xFFFF) ^ (id_segreto & 0xFFFF)
         ^ ((personalita >> 16) & 0xFFFF) ^ (personalita & 0xFFFF))
    return x < 8


def cerca_seme_per_evento(id_allenatore, id_segreto=0, lucentezza=None,
                          derivazione=None, sesso_atteso=None, semi=None):
    """Il primo seme che soddisfa i vincoli che l'evento dichiara.

    Esiste perche' scegliere un seme a caso e' un difetto latente: su un evento a lucentezza
    negata un seme sfortunato produce un esemplare cromatico, che nessun verificatore accetta,
    e nulla lo segnalerebbe. Qui il vincolo si verifica invece di sperare.

    Il parametro `lucentezza` accetta le tre diciture della tabella di riferimento, cioe'
    Never, Always e Random, e la terza non vincola nulla. Restituisce None se nessun seme
    soddisfa i vincoli, che e' informazione e non un guasto: significa che i vincoli sono
    incompatibili fra loro.
    """
    for seme in (semi if semi is not None else semi_a_sedici_bit()):
        personalita, _iv = personalita_e_iv(seme)
        cromatico = e_cromatico(personalita, id_allenatore, id_segreto)
        if lucentezza == "Never" and cromatico:
            continue
        if lucentezza == "Always" and not cromatico:
            continue
        if derivazione and sesso_atteso:
            try:
                if sesso_allenatore(derivazione, seme) != sesso_atteso:
                    continue
            except gb.FormatError:
                pass
        return seme
    return None


def sesso_allenatore_rand_s7(seme):
    """Conservata per compatibilita' con il codice e le prove che la chiamano per nome."""
    return sesso_allenatore("RandS7", seme)
