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
composizioni plausibili, selezionate perché riproducono un corpus di esemplari conservati, e
infine confrontate riga per riga con il codice della implementazione di riferimento. La
verifica sta in `tests/test_eventi.py` sui vettori riportati là, e la verifica estesa sui 209
esemplari del corpus completo la esegue `tools/confronta-ace-builder.py`, che li legge da una
copia locale non versionata. L'esito registrato il 2026-09-01, dopo il confronto con il
sorgente, è che il valore di personalità si riproduce su 209 vettori su 209, i valori
individuali su 209 su 209, e la derivazione del sesso dell'allenatore su tutti i 100
esemplari degli eventi che la usano.

Il vettore che prima non si riproduceva, e la correzione che ne è venuta
-----------------------------------------------------------------------
Fino al confronto con il sorgente questo modulo si fermava a 208 su 209, e il vettore che
mancava era descritto qui come internamente incoerente: il valore di personalità dichiarato
accanto al suo seme differisce di due unità da quello che il seme produce, mentre i suoi
valori individuali si riproducono esatti dal medesimo seme. La diagnosi era sbagliata, e il
modo in cui lo era vale più del fatto, perché è un errore di metodo e non di calcolo.

Quella differenza di due unità è la mutazione antilucente, che il modulo non conosceva. Il
ramo a lucentezza negata calcola il valore di personalità nel modo ordinario e poi, se il
risultato sarebbe cromatico, gli somma otto e azzera i tre bit bassi. Sul vettore in
questione il valore ordinario ha i tre bit bassi a sei, quindi la mutazione lo sposta di
esattamente due, e i valori individuali restano intatti perché la mutazione non consuma
estrazioni: entrambi i fatti che sembravano rendere la voce incoerente sono conseguenze
dell'unica formula che mancava. La prova non è solo che ora il vettore torni, ma che la
mutazione scatti su un solo esemplare del corpus, e sia proprio quello.

Il metodo da correggere era avere trattato una deviazione inspiegata come un difetto della
fonte anziché come un'ipotesi sul proprio modello, e avere poi scritto quella lettura come
una virtù, cioè come il caso deviante che il modello sa spiegare. Un modello non spiega ciò
che dichiara incoerente: lo esclude. Quando i conti tornano su duecentootto casi su
duecentonove, la probabilità che a sbagliare sia il caso solo è più bassa di quella che a
sbagliare sia il modello, e la via per deciderlo non è la statistica ma la fonte.
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
# ---------------------------------------------------------------------------------------------
# Le quattro composizioni del valore di personalita', e perche' sono quattro e non una
# ---------------------------------------------------------------------------------------------
# Fino al 2026-09-01 questo modulo conosceva una sola composizione, cioe' quella invertita che
# da' il nome alla famiglia BACD, e la lucentezza la trattava come un vincolo da soddisfare
# cercando un seme fortunato. Leggere il ramo di scelta della implementazione di riferimento ha
# mostrato che il modello era incompleto in un modo che vale enunciare, perche' e' la differenza
# fra un esemplare accettato e uno rifiutato: la lucentezza non e' un vincolo sul seme ma un
# ramo dell'algoritmo, e i rami sono quattro. Due di essi consumano un numero di estrazioni
# diverso dagli altri, quindi cambiano anche da dove vengono i valori individuali.
#
# L'ordine dei rami e' quello della fonte e non va riordinato per leggibilita', perche' e'
# significativo: il primo caso e' piu' specifico del secondo e li' la specie del metodo conta.
#
#   lucentezza negata e metodo BACD_U_AX  ->  antilucente per somma esclusiva, estrazioni variabili
#   lucentezza negata                     ->  composizione invertita, poi correzione se cromatico
#   lucentezza garantita                  ->  lucente forzata, tre estrazioni, la seconda scartata
#   metodo Method_2                       ->  composizione diretta, poi una estrazione di quadro
#   ogni altro caso                       ->  composizione invertita, due estrazioni
#
# Il punto che la vecchia implementazione sbagliava e' il terzo. Su un evento a lucentezza
# garantita nessun seme produce, con la composizione invertita, un valore che il verificatore
# accetti: la lucentezza si ottiene scrivendo i bit alti dell'identificativo dentro il valore di
# personalita', non pescando finche' non si e' fortunati. Cercare avrebbe prodotto esemplari che
# sembrano giusti e non lo sono. Nessuno dei centoquattro esemplari gia' prodotti e' interessato,
# perche' nel catalogo le voci a lucentezza garantita appartengono tutte a metodi che il
# programma non sapeva ancora fare e quindi rifiutava; e' fortuna e non merito, e per questo la
# prova che la fissa e' un controllo negativo e non una conferma.


def prossima16(stato):
    """Un passo del generatore, e la meta' alta dello stato risultante.

    Restituisce la coppia `(stato, parola)` invece della sola parola, perche' i rami che
    seguono hanno bisogno di portare avanti lo stato: un ramo che consuma tre estrazioni e uno
    che ne consuma due lasciano i valori individuali in posizioni diverse, e questo e'
    esattamente cio' che la vecchia interfaccia a sole estrazioni contate dal seme non poteva
    esprimere.
    """
    stato = avanza(stato)
    return stato, stato >> 16


def personalita_invertita(a, b):
    """La composizione della famiglia BACD: la prima estrazione in alto, la seconda in basso."""
    return (((a & 0xFFFF) << 16) | (b & 0xFFFF)) & 0xFFFFFFFF


def personalita_diretta(a, b):
    """La composizione ordinaria, cioe' quella degli incontri non da evento: la prima in basso.

    Serve al solo metodo delle uova, che di BACD porta il nome per comodita' di catalogazione e
    non la sostanza: la sua composizione e' quella comune, e cio' che lo distingue e' una
    estrazione scartata fra il valore di personalita' e i valori individuali.
    """
    return (((b & 0xFFFF) << 16) | (a & 0xFFFF)) & 0xFFFFFFFF


def correggi_antilucente(personalita):
    """La mutazione che rende non cromatico un valore che lo era: somma otto e azzera i bit bassi.

    Va conosciuta anche da chi non la impiega per produrre, perche' spiega una forma di
    esemplare che esiste in natura e che una ricerca per soli semi non genererebbe mai.
    """
    return (personalita + 8) & 0xFFFFFFF8


def personalita_antilucente(a, b, id_xor):
    """La composizione per somma esclusiva, del metodo non ristretto a lucentezza negata.

    La prima estrazione entra nella meta' alta dopo essere stata combinata con la somma
    esclusiva fra l'identificativo e la meta' bassa, ed e' pescata di nuovo finche' i suoi bit
    sopra il terzo non sono tutti nulli: un valore in cui lo fossero produrrebbe per costruzione
    un esemplare cromatico, che e' cio' che questo ramo deve evitare.
    """
    return ((((a ^ (id_xor ^ b)) & 0xFFFF) << 16) | (b & 0xFFFF)) & 0xFFFFFFFF


def personalita_lucente_forzata(x, b, id_xor):
    """La composizione a lucentezza garantita: i bit dell'identificativo scritti nel valore.

    Tre estrazioni, e la seconda si scarta. La meta' alta e' la prima estrazione; la meta' bassa
    e' la somma esclusiva fra identificativo e meta' alta nei tredici bit superiori, e i tre bit
    inferiori vengono dalla terza estrazione. Che i tredici bit siano proprio quelli e' la
    definizione stessa di cromatico letta al contrario: la somma esclusiva delle quattro parole
    sta sotto otto se e solo se quei tredici bit si annullano.
    """
    return ((((x & 0xFFFF) << 16)
             | (((id_xor ^ x) & 0xFFF8) | (b & 0b111))) & 0xFFFFFFFF)


def iv_sequenziali(stato):
    """I sei valori individuali dalle due estrazioni successive, e lo stato che ne risulta.

    Quindici bit per estrazione e non sedici: il bit alto non entra in nessun campo, ed e' la
    ragione per cui il valore complessivo dei valori individuali sta in trenta bit.
    """
    stato, prima = prossima16(stato)
    stato, seconda = prossima16(stato)
    ps, attacco, difesa = spacchetta_iv(prima)
    velocita, speciale_attacco, speciale_difesa = spacchetta_iv(seconda)
    return stato, {
        "ps": ps,
        "attacco": attacco,
        "difesa": difesa,
        "velocita": velocita,
        "attacco_speciale": speciale_attacco,
        "difesa_speciale": speciale_difesa,
    }


def e_cromatico_da_xor(personalita, id_xor):
    """La stessa prova di `e_cromatico`, quando l'identificativo e' gia' somma esclusiva."""
    x = ((id_xor & 0xFFFF) ^ ((personalita >> 16) & 0xFFFF) ^ (personalita & 0xFFFF))
    return x < 8


# Il numero massimo di estrazioni che il ramo antilucente non ristretto puo' consumare prima di
# trovare una prima estrazione utilizzabile. Non e' un limite dell'algoritmo, che non ne ha uno,
# ma un presidio contro il ciclo infinito: la probabilita' di fallire una estrazione e' di otto
# su sessantacinquemila, quindi fallirne mille di seguito e' impossibile in pratica e se accade
# significa che il generatore e' stato invocato con uno stato degenere.
TENTATIVI_MASSIMI_ANTILUCENTE = 1000


def genera(metodo, seme_generatore, lucentezza=None, id_xor=0):
    """Il valore di personalita', i valori individuali e lo stato residuo, secondo il ramo giusto.

    Il seme che entra qui e' quello effettivo, cioe' quello che `seme_effettivo` ha gia'
    trasformato: la separazione fra la trasformazione del seme e la generazione dai suoi valori
    e' quella della fonte, e tenerla evita di dover ripetere la trasformazione in ogni ramo.

    Lo stato residuo si restituisce perche' serve a chi viene dopo: il sesso dell'allenatore e
    l'oggetto tenuto si leggono da la', e non dal seme, poiche' i rami consumano un numero di
    estrazioni diverso.
    """
    stato = seme_generatore & 0xFFFFFFFF

    if lucentezza == "Never" and metodo == "BACD_U_AX":
        for _tentativo in range(TENTATIVI_MASSIMI_ANTILUCENTE):
            stato, a = prossima16(stato)
            if (a & ~0b111) != 0:
                break
        else:
            raise gb.FormatError(
                "il ramo antilucente non ristretto non ha trovato una prima estrazione "
                "utilizzabile in %d tentativi: lo stato di partenza e degenere"
                % (TENTATIVI_MASSIMI_ANTILUCENTE,))
        stato, b = prossima16(stato)
        personalita = personalita_antilucente(a, b, id_xor)
    elif lucentezza == "Never":
        stato, a = prossima16(stato)
        stato, b = prossima16(stato)
        personalita = personalita_invertita(a, b)
        if e_cromatico_da_xor(personalita, id_xor):
            personalita = correggi_antilucente(personalita)
    elif lucentezza == "Always":
        stato, x = prossima16(stato)
        stato, _scartata = prossima16(stato)
        stato, b = prossima16(stato)
        personalita = personalita_lucente_forzata(x, b, id_xor)
    elif metodo == "Method_2":
        stato, a = prossima16(stato)
        stato, b = prossima16(stato)
        personalita = personalita_diretta(a, b)
        # L'estrazione di quadro: consumata e non usata, ed e' cio' che distingue questo metodo.
        stato = avanza(stato)
    else:
        stato, a = prossima16(stato)
        stato, b = prossima16(stato)
        personalita = personalita_invertita(a, b)

    stato, iv = iv_sequenziali(stato)
    return personalita, iv, stato


# ---------------------------------------------------------------------------------------------
# La tabella del quinto anniversario del centro Pokemon giapponese
# ---------------------------------------------------------------------------------------------
# Due metodi del catalogo non generano l'esemplare direttamente dal seme: prima consultano una
# tabella di otto voci per sapere quale dono si sta ricevendo, e solo il seme che quella tabella
# accetta diventa il seme dell'esemplare. Vale registrare che la tabella non e' un elenco di
# dati ma una funzione aritmetica: le otto voci hanno peso uguale, e specie, insieme di mosse e
# lucentezza si ricavano dividendo il peso estratto. Averlo verificato sul sorgente invece di
# trascrivere una tabella e' cio' che permette di scriverla in venti righe senza dati copiati.
#
#   indice 0  Pichu  danza tremula   |  indice 0 con desiderio  Pichu  desiderio
#   indice 1  Bagon  ferrodifesa     |  indice 1 con desiderio  Bagon  desiderio
#   indice 2  Absol  dispetto        |  indice 2 con desiderio  Absol  desiderio
#   indice 3  Ralts  incanto         |  indice 3 con desiderio  Ralts  desiderio
#
# La lucentezza appartiene alla tabella e non all'evento: soltanto il Pichu puo' essere
# cromatico, e lo e' quando il peso estratto cade negli ultimi venticinque valori del suo
# intervallo.

PESO_MASSIMO_TABELLA = 1000
PESO_VOCE = 125
SOGLIA_CROMATICO_TABELLA = 100


def peso_periodico(casuale, massimo):
    """Il peso ridotto nell'intervallo richiesto, con la periodicita' che la fonte descrive.

    Non e' un resto della divisione e non va sostituito con uno: e' una moltiplicazione a
    precisione estesa scritta a mano su parole da sedici bit, e riscriverla in forma piu' breve
    ne cambierebbe il risultato. Le righe seguono la fonte una per una.
    """
    alta = (casuale >> 16) & 0xFFFF
    primo = ((alta << 2) & 0xFFFF) + alta
    secondo = ((casuale & 0xFFFF) << 1) + (primo >> 16)
    secondo += alta + (secondo >> 16)
    return (massimo * (secondo & 0xFFFF)) >> 16


def casuale32_tabella(seme):
    """Le due estrazioni che compongono il numero con cui si interroga la tabella."""
    a, b = estrazioni(seme, 2)
    return (((a & 0xFFFF) << 16) | (b & 0xFFFF)) & 0xFFFFFFFF


def risultato_quinto_anniversario(seme16):
    """Indice della specie, presenza del desiderio e lucentezza, per un seme a sedici bit."""
    peso = peso_periodico(casuale32_tabella(seme16 & 0xFFFF), PESO_MASSIMO_TABELLA)
    ottavo = peso // PESO_VOCE
    desiderio = (ottavo & 1) == 1
    indice = ottavo >> 1
    cromatico = (indice == 0 and (peso % PESO_VOCE) >= SOGLIA_CROMATICO_TABELLA)
    return indice, desiderio, cromatico


def indice_quinto_anniversario(specie):
    """L'indice che la specie occupa nella tabella, per la via aritmetica della fonte.

    Le quattro specie hanno identificativi i cui bit secondo e terzo sono distinti e in ordine,
    quindi l'indice si ottiene da quelli invece che da un elenco. Vale ripeterlo perche' e' la
    ragione per cui questo modulo non contiene nessuna tabella di specie: uno spostamento e una
    somma bastano, e un elenco copiato a mano potrebbe sbagliare.
    """
    return (((specie & 0xFFFF) >> 2) + 1) & 3


def combacia_quinto_anniversario(specie, cromatico, desiderio, seme16):
    """Se quel seme a sedici bit produca proprio quel dono."""
    indice, ha_desiderio, cromatico_tabella = risultato_quinto_anniversario(seme16)
    return (indice_quinto_anniversario(specie) == indice
            and bool(desiderio) == ha_desiderio
            and bool(cromatico) == cromatico_tabella)


def seme_quinto_anniversario(specie, cromatico, desiderio, seme, tentativi=0x20000):
    """Il primo seme a sedici bit che la tabella risolve in quel dono, partendo da quello dato.

    La fonte avanza il seme completo a trentadue bit e prova ogni volta i suoi sedici bit bassi,
    quindi i valori provati non sono consecutivi. Qui si fa la stessa cosa, e il limite di
    tentativi esiste per la sola ragione per cui esiste quello del ramo antilucente: la fonte
    cicla senza limite perche' sa che un dono esiste sempre, ma un vincolo impossibile passato
    per errore non deve bloccare il programma.
    """
    corrente = seme & 0xFFFFFFFF
    for _ in range(tentativi):
        u16 = corrente & 0xFFFF
        if combacia_quinto_anniversario(specie, cromatico, desiderio, u16):
            return u16
        corrente = avanza(corrente)
    return None


# ---------------------------------------------------------------------------------------------
# La trasformazione del seme, fra il numero letto dall'orologio e la generazione
# ---------------------------------------------------------------------------------------------
# I metodi del catalogo non partono tutti dal seme cosi' com'e'. Quattro voci lo restringono a un
# intervallo di duecentoquattordici valori, undici lo passano per la tabella del quinto
# anniversario e poi lo avanzano di due, una lo cerca in un elenco di semi conosciuti, e due
# derivazioni del sesso lo vincolano a produrre un bit determinato. L'ordine dei casi e' quello
# della fonte, e va conservato: la voce a orologio dichiara una derivazione del sesso vincolata,
# ma il suo caso viene prima, quindi il vincolo non si applica e la derivazione resta dichiarata
# invece che derivata.

# I metodi che restringono il seme ai suoi sedici bit bassi. Non e' un dettaglio di comodo: e'
# cio' che rende esauribile la ricerca inversa, e i metodi che non vi appartengono ammettono un
# seme qualunque a trentadue bit, cosicche' restringerlo comunque e' un restringimento legittimo
# della produzione e non un errore.
METODI_A_SEME_RISTRETTO = ("BACD_R", "BACD_R_A", "BACD_RBCD", "BACD_TA", "BACD_TS", "BACD_M")

# L'intervallo del metodo a orologio, e da dove viene. Il seme non e' un numero qualunque ma la
# somma delle cifre di un'ora scritta in decimale codificato in binario, quindi il suo massimo e'
# duecentotredici. Il nome del metodo porta quella sigla proprio per questo.
SEME_MASSIMO_OROLOGIO = 213

SPECIE_JIRACHI = 385


def seme_ristretto_per_sesso(seme, bit_atteso, tentativi=0x20000):
    """Il primo seme a sedici bit la cui quinta estrazione da' quel bit di sesso.

    Esiste perche' due derivazioni dichiarano il sesso invece di derivarlo, e la fonte tiene
    comunque il seme coerente con la derivazione: il valore dichiarato e quello che si
    calcolerebbe devono combaciare, altrimenti un verificatore che ricalcola troverebbe una
    contraddizione. Il bit e' quello per divisione per tre, che e' la derivazione di riferimento.
    """
    corrente = seme & 0xFFFFFFFF
    for _ in range(tentativi):
        u16 = corrente & 0xFFFF
        quinta = estrazioni(u16, 5)[4]
        if _bit0_diviso_tre(quinta) == bit_atteso:
            return u16
        corrente = avanza(corrente)
    return None


def semi_ammessi(metodo, semi_mystry=None):
    """L'insieme dei semi di partenza che vale la pena provare, per quel metodo.

    Serve perche' due metodi rendono inutile percorrere i sessantacinquemila: quello a orologio
    li schiaccia tutti su duecentoquattordici valori, e quello a elenco su ottantasei. Provare
    gli altri non produrrebbe un errore ma ripeterebbe lo stesso esemplare migliaia di volte,
    che e' peggio, perche' darebbe l'impressione di una ricerca dove non ce n'e' nessuna.
    """
    if metodo == "BACD_RBCD":
        return range(SEME_MASSIMO_OROLOGIO + 1)
    if metodo == "BACD_M":
        return range(len(semi_mystry) if semi_mystry else 0)
    return semi_a_sedici_bit()


def seme_effettivo(metodo, seme, specie=None, lucentezza=None, desiderio=None,
                   derivazione=None, semi_mystry=None):
    """Il seme da cui si genera davvero, dato quello di partenza e il metodo dichiarato.

    Restituisce un valore a trentadue bit, che nei casi a tabella non e' piu' a sedici: la
    tabella consuma due estrazioni per scegliere il dono, e cio' che resta e' lo stato dopo
    quelle due. E' la ragione per cui un verificatore, per riconoscere questi esemplari, deve
    tornare indietro di due passi prima di cercare il seme fra gli ammessi.
    """
    if metodo == "BACD_RBCD":
        return min(max(seme, 0), SEME_MASSIMO_OROLOGIO)
    if metodo == "BACD_TA" and specie == SPECIE_JIRACHI:
        # La tabella esiste anche qui, ma tutte le sue voci danno il medesimo dono, quindi
        # consultarla e' indistinguibile dal saltarla: restano le due estrazioni che consuma.
        return avanza(avanza(seme & 0xFFFF))
    if metodo in ("BACD_TA", "BACD_TS"):
        if specie is None:
            raise gb.FormatError(
                "i metodi a tabella hanno bisogno della specie, perche e la specie a "
                "selezionare la voce della tabella e non l'evento")
        u16 = seme_quinto_anniversario(specie, lucentezza == "Always", bool(desiderio), seme)
        if u16 is None:
            raise gb.FormatError(
                "nessun seme risolve la tabella del quinto anniversario in specie %r con "
                "desiderio %r e lucentezza %r: i vincoli sono incompatibili"
                % (specie, bool(desiderio), lucentezza))
        return avanza(avanza(u16))
    if metodo == "BACD_M":
        if not semi_mystry:
            raise gb.FormatError(
                "il metodo a elenco ha bisogno dei semi ammessi, che non sono derivabili da "
                "una formula e vanno estratti dalla fonte: passali in semi_mystry")
        return semi_mystry[seme % len(semi_mystry)]
    if derivazione == "RandD3_0":
        return seme_ristretto_per_sesso(seme, 0)
    if derivazione == "RandD3_1":
        return seme_ristretto_per_sesso(seme, 1)
    return (seme & 0xFFFF) if metodo in METODI_A_SEME_RISTRETTO else (seme & 0xFFFFFFFF)


# L'identificativo dell'allenatore dell'evento che consuma una estrazione per l'oggetto tenuto.
# Va conosciuto perche' sposta di uno la posizione da cui si legge il sesso, e perche' un
# esemplare di quell'evento senza oggetto tenuto e' incompleto.
ID_ALLENATORE_CON_OGGETTO = 20043


def sesso_allenatore_da_stato(derivazione, stato, sesso_ricevente=None):
    """Il sesso dell'allenatore letto dallo stato residuo, invece che ricontato dal seme.

    E' la forma corretta, e quella che prende il seme resta come comodita' per il solo caso in
    cui le estrazioni consumate siano quattro. La differenza si vede sui rami che ne consumano
    tre o cinque: la' ricontare dal seme leggerebbe la parola sbagliata.
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
            "riferimento salta il campo invece di calcolarlo.")
    if derivazione == "RandSG15":
        # Due passi e non uno: fra i valori individuali e il sesso si consuma l'oggetto tenuto,
        # e il commento della fonte lo dice per nome accanto alla definizione della derivazione.
        stato_locale, _prima = prossima16(stato)
        stato_locale, parola = prossima16(stato_locale)
        return "femmina" if _bit(parola, 15) == 1 else "maschio"

    _stato_locale, parola = prossima16(stato)
    if derivazione == "RandD3":
        return "femmina" if _bit0_diviso_tre(parola) == 1 else "maschio"
    if derivazione == "RandS3":
        return "femmina" if _bit(parola, 3) == 1 else "maschio"
    if derivazione == "RandS7":
        return "femmina" if _bit(parola, 7) == 0 else "maschio"
    raise gb.FormatError("derivazione del sesso sconosciuta: %r" % (derivazione,))


def esemplare_da_evento(metodo, id_allenatore, id_segreto=0, lucentezza=None, specie=None,
                        desiderio=None, derivazione=None, sesso_ricevente=None,
                        semi_mystry=None, semi=None):
    """Tutto cio' che il generatore pseudocasuale decide di un esemplare da evento.

    Restituisce un dizionario con il seme di partenza, quello effettivo, il valore di
    personalita', i valori individuali, il sesso dell'allenatore e l'oggetto tenuto quando
    l'evento ne consuma uno. Il seme si cerca fra quelli ammessi verificando i vincoli, e la
    verifica e' il punto: la lucentezza garantita ora si ottiene per costruzione, ma quella
    negata resta un vincolo, perche' il ramo che la nega ammette due esiti e noi produciamo solo
    quello non mutato, che e' un sottoinsieme legittimo e non tutto l'insieme.

    Restituisce None se nessun seme soddisfa i vincoli, che e' informazione e non un guasto.
    """
    id_xor = (id_allenatore & 0xFFFF) ^ (id_segreto & 0xFFFF)
    insieme = semi if semi is not None else semi_ammessi(metodo, semi_mystry)
    for seme in insieme:
        effettivo = seme_effettivo(metodo, seme, specie=specie, lucentezza=lucentezza,
                                   desiderio=desiderio, derivazione=derivazione,
                                   semi_mystry=semi_mystry)
        if effettivo is None:
            continue
        personalita, iv, stato = genera(metodo, effettivo, lucentezza, id_xor)
        cromatico = e_cromatico_da_xor(personalita, id_xor)
        if lucentezza == "Never" and cromatico:
            continue
        if lucentezza == "Always" and not cromatico:
            continue
        estrazione_oggetto = None
        if (id_allenatore & 0xFFFF) == ID_ALLENATORE_CON_OGGETTO:
            stato, estrazione_oggetto = prossima16(stato)
        try:
            sesso = sesso_allenatore_da_stato(derivazione or "Only0", stato, sesso_ricevente)
        except gb.FormatError:
            continue
        return {
            "seme": seme,
            "seme_effettivo": effettivo,
            "personalita": personalita,
            "iv": iv,
            "cromatico": cromatico,
            "sesso_ot": sesso,
            "estrazione_oggetto": estrazione_oggetto,
        }
    return None
# Le due bacche che l'evento del desiderio puo' consegnare, e la formula che scegle fra esse.
# Vale scriverla perche' e' un caso in cui una estrazione gia' consumata portava informazione
# che il generatore buttava: il modulo contava quella estrazione per leggere il sesso
# dell'allenatore nella posizione giusta, ma non ne usava il valore, quindi gli esemplari di
# quell'evento uscivano senza l'oggetto che l'originale porta.
#
# La formula e' la medesima della derivazione del sesso per divisione per tre, applicata a un
# altro campo, e la coincidenza non e' un caso: il gioco riusa la stessa riduzione a un bit.
OGGETTO_DESIDERIO = (170, 169)


def oggetto_tenuto_desiderio(estrazione):
    """L'oggetto tenuto dell'evento del desiderio, dalla sua estrazione dedicata.

    Restituisce l'identificativo di una delle due bacche. La forma della fonte e' una
    sottrazione da centosettanta, e si conserva cosi' invece di indicizzare una coppia,
    perche' e' quella che si confronta a vista con il sorgente.
    """
    return OGGETTO_DESIDERIO[0] - (_bit0_diviso_tre(estrazione) & 1)
