#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Calcola le grandezze citate in docs/12-analisi-quantitativa.md.

Perché esiste
--------------
Ogni cifra di quella nota deve essere riproducibile e correggibile, invece di essere un
numero da credere. Questo strumento la produce: si rilancia, si confronta l'uscita con il
documento, e se una cifra è cambiata si sa subito quale assunzione l'ha mossa.

È anche l'attuazione del principio registrato nella regola di token economy del progetto,
cioè spingere su codice deterministico tutto ciò che non richiede comprensione semantica.
Un conteggio di punti interi in un politopo, una probabilità geometrica o una verifica
esaustiva del codice di Lehmer sono lavoro deterministico, e il loro posto è uno script.

Che cosa non fa
---------------
Non stima. Dove il documento parla di stime, per esempio i cicli per byte del processore
del Game Boy, il numero è un parametro dichiarato qui in testa alla sezione che lo usa, e
il documento lo etichetta come stima. Il resto è aritmetica esatta.

Uso
---
    python tools/analisi-quantitativa.py
"""

import math
from math import comb, log2, sqrt

print("=" * 78)
print("1. CHECKSUM COME CODICE RILEVATORE")
print("=" * 78)
for bit in (8, 16):
    p = 2.0 ** -bit
    print("  %2d bit: P(errore non rilevato) = 2^-%d = %.3e = 1 su %d"
          % (bit, bit, p, 2 ** bit))

# La somma modulo 2^n è invariante per permutazione degli addendi: quante permutazioni
# di 6 parole da 16 bit passano indenni? Tutte.
print("  la somma è invariante per permutazione: 6! = %d riordini indistinguibili"
      % math.factorial(6))
print("  su quattro sottostrutture: (4*6)! è fuori scala, ma il punto è qualitativo")

# Costo di calcolo su LR35902 a 4.194304 MHz, checksum Gen 2 di Cristallo.
CLOCK = 4194304.0
byte_gen2 = 0x2B82 - 0x2009 + 1
print("  Cristallo: byte coperti dal checksum = 0x%X - 0x%X + 1 = %d"
      % (0x2B82, 0x2009, byte_gen2))
for nome, cicli_per_byte in (("somma a 8 bit", 16), ("CRC tabellare", 24), ("CRC bit a bit", 130)):
    cicli = byte_gen2 * cicli_per_byte
    print("    %-16s ~%2d cicli/byte -> %8d cicli = %6.1f ms"
          % (nome, cicli_per_byte, cicli, 1000 * cicli / CLOCK))

print()
print("=" * 78)
print("2. CIFRATURA XOR: TASSO DI CHIAVE E RECUPERO")
print("=" * 78)
bit_messaggio = 48 * 8
bit_chiave = 32
print("  messaggio: %d bit (48 byte)" % bit_messaggio)
print("  chiave:    %d bit, riusata %d volte" % (bit_chiave, bit_messaggio // bit_chiave))
print("  tasso di chiave = %d/%d = 1/%d" % (bit_chiave, bit_messaggio, bit_messaggio // bit_chiave))
print("  condizione di Shannon per la sicurezza perfetta: chiave lunga come il messaggio")
print("  -> violata di un fattore %d" % (bit_messaggio // bit_chiave))
print("  parole da 32 bit nel blocco: %d" % (48 // 4))
print("  coppie di parole confrontabili: C(12,2) = %d" % comb(12, 2))

print()
print("=" * 78)
print("3. PERMUTAZIONE: INFORMAZIONE E CODICE DI LEHMER")
print("=" * 78)
print("  H(permutazione) = log2(24) = %.4f bit" % log2(24))
print("  ma la permutazione è funzione del valore di personalità:")
print("  I(perm ; PV) = H(perm) = %.4f bit -> contributo indipendente nullo" % log2(24))

TAB = {0:"GAEM",1:"GAME",2:"GEAM",3:"GEMA",4:"GMAE",5:"GMEA",
       6:"AGEM",7:"AGME",8:"AEGM",9:"AEMG",10:"AMGE",11:"AMEG",
       12:"EGAM",13:"EGMA",14:"EAGM",15:"EAMG",16:"EMGA",17:"EMAG",
       18:"MGAE",19:"MGEA",20:"MAGE",21:"MAEG",22:"MEGA",23:"MEAG"}

def lehmer(i, elementi="GAEM"):
    """Permutazione di indice i nell'ordine lessicografico, per codice di Lehmer."""
    resto = list(elementi)
    fuori = []
    for k in range(len(elementi) - 1, -1, -1):
        f = math.factorial(k)
        scelta = i // f
        i -= scelta * f
        fuori.append(resto.pop(scelta))
    return "".join(fuori)

falliti = [i for i in range(24) if lehmer(i) != TAB[i]]
print("  verifica della tabella del gioco contro il codice di Lehmer su tutti i 24 indici:")
print("    indici discordanti: %s" % (falliti if falliti else "nessuno"))
for i in (5, 12, 23):
    print("    i=%2d -> Lehmer %s, tabella %s" % (i, lehmer(i), TAB[i]))

print()
print("=" * 78)
print("4. CAMPIONAMENTO CON RIFIUTO: ITERAZIONI ATTESE")
print("=" * 78)
# natura = PV mod 25, abilita = PV mod 2, sesso = (PV mod 256) >= soglia
# CRT: mod 25 e mod 256 sono indipendenti perché gcd(25,256)=1
print("  gcd(25,256) = %d -> natura e (sesso,abilita) sono indipendenti per il TCR"
      % math.gcd(25, 256))
print("  ma sesso e abilità dipendono entrambi da PV mod 256: vanno contati insieme")
for nome, soglia in (("1:1 (soglia 127)", 127), ("7:1 (soglia 31)", 31), ("1:7 (soglia 225)", 225)):
    congiunta = {}
    for b in range(256):
        maschio = b >= soglia
        ab = b & 1
        congiunta[(maschio, ab)] = congiunta.get((maschio, ab), 0) + 1
    # il caso peggiore fra le quattro combinazioni richieste
    peggiore = min(congiunta.values()) / 256.0
    tipico = congiunta[(True, 0)] / 256.0
    p_peggiore = peggiore / 25.0
    p_tipico = tipico / 25.0
    print("  %-18s p tipico = %.5f -> E[N] = %6.1f | p peggiore = %.5f -> E[N] = %7.1f"
          % (nome, p_tipico, 1 / p_tipico, p_peggiore, 1 / p_peggiore))
# Unown: in più la lettera, 1/28
p_unown = (1 / 25.0) * 0.25 * (1 / 28.0)
print("  Unown, con la lettera fra i vincoli: p = %.3e -> E[N] = %.0f" % (p_unown, 1 / p_unown))
print("  varianza della geometrica: (1-p)/p^2 -> sigma ~ 1/p, cioè dell'ordine di E[N]")
print("  tempo: anche 2800 iterazioni di aritmetica intera restano sotto il millisecondo")

print()
print("=" * 78)
print("5. LUCENTEZZA: Probabilità E SODDISFACIBILITA")
print("=" * 78)
print("  condizione: (TID ^ SID ^ PValto ^ PVbasso) < 8, su 16 bit")
print("  P = 8/2^16 = 8/%d = 1/%d" % (2 ** 16, 2 ** 16 // 8))
print("  lo XOR è una biiezione in ciascun argomento: fissati TID e PV,")
print("  esistono esattamente 8 valori di SID che soddisfano la condizione,")
print("  quindi il vincolo è sempre soddisfacibile: P(esiste SID) = 1")

print()
print("=" * 78)
print("6. STAT EXPERIENCE -> EV: QUANTIZZAZIONE E PERDITA")
print("=" * 78)
print("  EV = min(252, floor(sqrt(StatExp)))")
print("  livelli in ingresso: %d ; livelli in uscita: %d" % (65536, 253))
print("  H(ingresso) <= %d bit ; H(uscita) <= log2(253) = %.3f bit" % (16, log2(253)))
print("  saturazione: sqrt(%d) = %d, e sqrt(65535) = %.2f -> troncato a 252"
      % (63504, int(sqrt(63504)), sqrt(65535)))
print("  intervallo non rappresentabile: da %d a %d, cioè %d valori (%.2f%% dello spazio)"
      % (63504, 65535, 65535 - 63504 + 1, 100.0 * (65535 - 63504 + 1) / 65536))
print("  ampiezza del gradino di quantizzazione: (k+1)^2 - k^2 = 2k+1")
for k in (0, 10, 100, 251):
    print("    a EV=%3d il gradino vale %4d unita di Stat Experience" % (k, 2 * k + 1))
print("  il contributo alla statistica satura a 63 punti -> 64 livelli osservabili,")
print("  cioè log2(64) = 6 bit: la perdita oltre quei 6 bit non è osservabile")

# Cardinalità dello spazio di arrivo: politopo Sx_i <= 510, 0 <= x_i <= 252, 6 variabili
def punti_politopo(n, totale, cap):
    """Punti interi con somma <= totale e ciascuna coordinata <= cap, per inclusione-esclusione."""
    tot = 0
    for j in range(n + 1):
        resto = totale - j * (cap + 1)
        if resto < 0:
            break
        tot += (-1) ** j * comb(n, j) * comb(resto + n, n)
    return tot

ingresso = 65536 ** 5
uscita = punti_politopo(6, 510, 252)
print()
print("  cardinalita dello spazio di partenza: 65536^5 = %.3e (%.1f bit)"
      % (ingresso, log2(ingresso)))
print("  punti interi del politopo di arrivo:   %.3e (%.1f bit)" % (uscita, log2(uscita)))
print("  rapporto: %.3e -> la perdita di %.1f bit è imposta dal formato, non dalla formula"
      % (ingresso / uscita, log2(ingresso) - log2(uscita)))
print("  somma massima convertibile senza politica: 5 * 252 = %d contro un tetto di %d"
      % (5 * 252, 510))
print("  eccesso nel caso peggiore: %d unita, cioè il %.0f%% del tetto"
      % (5 * 252 - 510, 100.0 * (5 * 252 - 510) / 510))

print()
print("=" * 78)
print("7. CAVO LINK: TEMPI, EFFICIENZA, STUFFING")
print("=" * 78)
for nome, hz in (("clock interno Game Boy", 8192), ("clock interno Color, massimo", 524288),
                 ("clock esterno massimo dichiarato", 500000)):
    print("  %-34s %8d bit/s = %8.1f byte/s" % (nome, hz, hz / 8.0))
scambio = 424
patch = 200
totale_filo = scambio + patch
utili = 418
print("  blocco di scambio: %d byte sul filo, %d di dati utili" % (scambio, utili))
print("  lista di correzione: %d byte" % patch)
for nome, hz in (("8192 Hz", 8192), ("500 kHz", 500000)):
    print("    a %-9s il solo blocco di scambio richiede %7.1f ms, i due blocchi %7.1f ms"
          % (nome, 1000 * scambio * 8 / hz, 1000 * totale_filo * 8 / hz))
print("  rapporto fra le due velocità: %.1fx" % (500000 / 8192.0))
print("  efficienza di trama: %d utili su %d trasmessi = %.1f%%"
      % (utili, totale_filo, 100.0 * utili / totale_filo))
lam = utili / 256.0
print("  byte stuffing classico: valore riservato 0xFE, P = 1/256")
print("    occorrenze attese in %d byte casuali: lambda = %.3f" % (utili, lam))
# P(X > 198) con Poisson(lam): praticamente zero. Calcolo il primo k con P(X>=k) < 1e-12
k = 1
while True:
    coda = 1 - sum(math.exp(-lam) * lam ** i / math.factorial(i) for i in range(k))
    if coda < 1e-12:
        break
    k += 1
print("    P(occorrenze >= %d) scende sotto 1e-12: la lista da %d byte e sovrabbondante"
      % (k, patch))
print("    costo dello stuffing: variabile, atteso %.2f byte" % lam)
print("    costo della lista: fisso, %d byte -> %.0f volte l'atteso" % (patch, patch / lam))
print("  ragione del costo fisso: in uno scambio sincrono simultaneo la lunghezza")
print("  del blocco deve essere concordata a priori, quindi una lunghezza variabile")
print("  non è ammissibile: non esiste canale su cui annunciarla")
print("  indici indirizzabili per parte di lista: fino a 0xFD = %d" % 0xFD)
print("  dati da indicizzare: %d byte -> serve più di una parte, ed è la ragione" % utili)

print()
print("=" * 78)
print("8. LDN: BANDA, CANALI, DUTY CYCLE")
print("=" * 78)
print("  canali 2.4 GHz: spaziatura %d MHz, larghezza DSSS %d MHz" % (5, 22))
for a, b in ((1, 6), (6, 11), (1, 11)):
    dist = (b - a) * 5
    print("    canali %2d e %2d: distanza %2d MHz %s 22 MHz -> %s"
          % (a, b, dist, ">" if dist > 22 else "<=",
             "non sovrapposti" if dist > 22 else "sovrapposti"))
periodo_ms = 100
print("  action frame ogni %d ms -> cadenza %.0f Hz" % (periodo_ms, 1000.0 / periodo_ms))
for byte_frame, rate in ((100, 1e6), (100, 11e6)):
    durata_ms = 1000.0 * byte_frame * 8 / rate
    print("    frame di %d byte a %.0f Mbit/s: %.3f ms -> duty cycle %.3f%%"
          % (byte_frame, rate / 1e6, durata_ms, 100.0 * durata_ms / periodo_ms))
print("  indirizzi link-local 169.254.0.0/16: %d indirizzi, %d utilizzabili"
      % (2 ** 16, 2 ** 16 - 2))

print()
print("=" * 78)
print("9. AUTOMAZIONE: L'ERRORE IN UNA CORSA LUNGA")
print("=" * 78)
for fps in (30, 60):
    for ore in (1, 8):
        k = fps * 3600 * ore
        for p in (1e-3, 1e-5, 1e-7):
            pfail = 1 - (1 - p) ** k
            print("  %2d fps, %d h -> %9d fotogrammi ; p=%.0e -> P(almeno un errore) = %.6f"
                  % (fps, ore, k, p, pfail))
    print()
print("  per tenere P(errore) sotto 0.01 su 8 ore a 60 fps servono:")
k = 60 * 3600 * 8
p_max = 1 - (0.99) ** (1.0 / k)
print("    p per fotogramma < %.3e, cioè un errore ogni %.0f fotogrammi" % (p_max, 1 / p_max))
print("  conclusione: su orizzonti lunghi l'errore è certo, quindi il progetto")
print("  deve essere robusto all'errore e non privo di errori")

print()
print("=" * 78)
print("10. DETTAGLI DELLE DERIVAZIONI: BIAS, PARTIZIONE, DEFICIT")
print("=" * 78)

# Il bias del modulo. PV è uniforme su 2^32, ma 25 non divide 2^32, dunque
# PV mod 25 non è esattamente uniforme: alcune nature sono più probabili.
N32 = 2 ** 32
q, r = divmod(N32, 25)
print("  BIAS DEL MODULO: 2^32 = 25*%d + %d" % (q, r))
print("    %d classi di resto con %d preimmagini, %d classi con %d"
          % (r, q + 1, 25 - r, q))
print("    verifica della partizione: %d*%d + %d*%d = %d"
          % (r, q + 1, 25 - r, q, r * (q + 1) + (25 - r) * q))
p_alta, ideale = (q + 1) / N32, 1 / 25
print("    deviazione relativa massima dalla uniforme = %.3e" % ((p_alta - ideale) / ideale))

# La partizione del quantizzatore: le regioni devono coprire esattamente lo spazio.
somma = sum(2 * k + 1 for k in range(252))
saturazione = 65536 - 63504
print("  PARTIZIONE DEL QUANTIZZATORE: sum_{k=0}^{251}(2k+1) = %d = 252^2 = %d"
      % (somma, 252 ** 2))
print("    regione di saturazione: %d valori" % saturazione)
print("    %d + %d = %d su 65536 -> %s"
      % (somma, saturazione, somma + saturazione,
         "partizione esatta" if somma + saturazione == 65536 else "INCOMPLETA"))

# Il deficit di entropia della chiave, che è grandezza diversa dal riuso.
print("  DEFICIT DI ENTROPIA: |M| = 2^384, |K| = 2^32 -> deficit %d bit, fattore 2^%d"
      % (384 - 32, 384 - 32))
print("    il fattore 12 misura il riuso della chiave, non il deficit: due grandezze")

# Il piano dei canali della banda a 2.4 GHz.
print("  CANALI 2.4 GHz: f(k) = 2412 + 5*(k-1) MHz")
for k in (1, 6, 11, 13):
    print("    canale %2d -> %d MHz" % (k, 2412 + 5 * (k - 1)))
span = 5 * 12
print("    massimo di canali non sovrapposti fra 1 e 13: floor(%d/25) + 1 = %d"
      % (span, span // 25 + 1))

# La qualità dell'approssimazione di Poisson impiegata sul byte riservato.
n_dati, p_ris = 418, 1 / 256
print("  POISSON: errore d'ordine np^2 = %.5f, cioè il %.2f per cento"
      % (n_dati * p_ris * p_ris, 100 * n_dati * p_ris * p_ris))
