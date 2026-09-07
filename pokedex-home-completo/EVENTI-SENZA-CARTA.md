# Distribuzioni senza carta: la coda di produzione

> Documento generato da `tools/leggi-serebii-eventi.py --senza-carta`. Non si modifica a mano: si rigenera. Ogni riga porta accanto la pagina dell'archivio da cui viene, che è la fonte di quel dato.

Questa è la coda di una via di produzione che il progetto non ha mai percorso. Per ogni altra generazione il generatore parte da una carta, cioè dal file che la distribuzione consegnava, e ne compone i campi che la carta lascia liberi. Qui la carta non esiste e non è mai esistita: la consegna avveniva presso un apparecchio che scriveva direttamente nel salvataggio, oppure dentro il gioco, oppure attraverso il servizio in rete della quinta generazione. Il solo dato disponibile è quello che un archivio ha registrato mentre l'evento accadeva.

Le distribuzioni qui elencate sono 19 e riguardano le 14 specie che l'archivio conosce e la nostra enumerazione no. Sono la cecità misurata il 2026-09-07, non una stima.

## I due casi in cui un campo non è un valore

Il primo è il campo che appartiene a chi riceve. L'archivio lo dichiara scrivendo che il valore è quello del giocatore, e riguarda 4 voci di questa coda. Per quelle il campo non si copia ma si scrive con l'allenatore del progetto, come già si fa per le voci di seconda e terza generazione che la fonte marca allo stesso modo.

Il secondo è il campo che dichiara un'alternativa invece di una scelta, tipicamente due abilità possibili oppure un livello che l'archivio non conosce. Riguarda 3 voci e richiede una decisione per ciascuna, che non è di questo documento: qui si segnala soltanto che la decisione serve.

## Le voci

## L'espansione per allenatore

La decisione dell'utente del 2026-09-07 è che una distribuzione con più allenatori dichiarati vale un esemplare per ciascun allenatore, non uno solo. L'archivio separa le varianti con una interruzione di riga, e questo documento le espande di conseguenza: le 19 righe di distribuzione diventano 62 esemplari da produrre.

Va dichiarato il limite della regola, perché non è meccanica. Una interruzione di riga separa varianti, ma che cosa una variante sia dipende dalla distribuzione: quattro lettere consecutive del medesimo negozio sono quattro allenatori distinti, mentre un nome scritto in giapponese e poi in quattro lingue europee è un allenatore solo, tradotto. La regione aiuta e non basta, perché esistono distribuzioni di una sola regione i cui due nomi sono manifestamente lo stesso nome in due lingue. Nelle voci di questo documento la distinzione è stata fatta a mano e ciascuna riga dichiara quale lettura si sia applicata.

| Dex | Specie | Anno | Regione | Metodo | Livello | Allenatore | Identificativo | Abilità | Palla | Mosse | Da decidere | Fonte |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 23 | Ekans | 2004 | America | In-Life | 14 | `JEREMY` | `24680` | Shed skin | pokeball | Leer / Wrap / Poison Sting / Bite | nulla | `/events/dex/023.shtml` |
| 23 | Ekans | 2006 | Japan | In-Life | 10 | `トウキョー` | `60114` | Intimidate or Shed Skin | pokeball | Wrap / Leer / Poison Sting | abilità alternativa, 6 allenatori, una voce ciascuno | `/events/dex/023.shtml` |
| 23 | Ekans | 2006 | Japan | In-Life | 10 | `オーサカ` | `60114` | Intimidate or Shed Skin | pokeball | Wrap / Leer / Poison Sting | abilità alternativa, 6 allenatori, una voce ciascuno | `/events/dex/023.shtml` |
| 23 | Ekans | 2006 | Japan | In-Life | 10 | `ナゴヤ` | `60114` | Intimidate or Shed Skin | pokeball | Wrap / Leer / Poison Sting | abilità alternativa, 6 allenatori, una voce ciascuno | `/events/dex/023.shtml` |
| 23 | Ekans | 2006 | Japan | In-Life | 10 | `フクオカ` | `60114` | Intimidate or Shed Skin | pokeball | Wrap / Leer / Poison Sting | abilità alternativa, 6 allenatori, una voce ciascuno | `/events/dex/023.shtml` |
| 23 | Ekans | 2006 | Japan | In-Life | 10 | `ヨコハマ` | `60114` | Intimidate or Shed Skin | pokeball | Wrap / Leer / Poison Sting | abilità alternativa, 6 allenatori, una voce ciascuno | `/events/dex/023.shtml` |
| 23 | Ekans | 2006 | Japan | In-Life | 10 | `サッポロ` | `60114` | Intimidate or Shed Skin | pokeball | Wrap / Leer / Poison Sting | abilità alternativa, 6 allenatori, una voce ciascuno | `/events/dex/023.shtml` |
| 252 | Treecko | 2005 | Japan | In-Life | 10 | `トウキョー` | `51126` | Overgrow | pokeball | Pound / Leer / Absorb | 6 allenatori, una voce ciascuno | `/events/dex/252.shtml` |
| 252 | Treecko | 2005 | Japan | In-Life | 10 | `オーサカ` | `51126` | Overgrow | pokeball | Pound / Leer / Absorb | 6 allenatori, una voce ciascuno | `/events/dex/252.shtml` |
| 252 | Treecko | 2005 | Japan | In-Life | 10 | `ナゴヤ` | `51126` | Overgrow | pokeball | Pound / Leer / Absorb | 6 allenatori, una voce ciascuno | `/events/dex/252.shtml` |
| 252 | Treecko | 2005 | Japan | In-Life | 10 | `フクオカ` | `51126` | Overgrow | pokeball | Pound / Leer / Absorb | 6 allenatori, una voce ciascuno | `/events/dex/252.shtml` |
| 252 | Treecko | 2005 | Japan | In-Life | 10 | `ヨコハマ` | `51126` | Overgrow | pokeball | Pound / Leer / Absorb | 6 allenatori, una voce ciascuno | `/events/dex/252.shtml` |
| 252 | Treecko | 2005 | Japan | In-Life | 10 | `サッポロ` | `51126` | Overgrow | pokeball | Pound / Leer / Absorb | 6 allenatori, una voce ciascuno | `/events/dex/252.shtml` |
| 252 | Treecko | 2010 | Japan | Global Link | 10 | `Yours` | `Yours` | Unburden | - | Pound / Leer / Absorb | allenatore del progetto, palla non dichiarata | `/events/dex/252.shtml` |
| 258 | Mudkip | 2005 | Japan | In-Life | 10 | `トウキョー` | `51126` | Torrent | pokeball | Tackle / Growl / Mud-slap / Water Gun | 6 allenatori, una voce ciascuno | `/events/dex/258.shtml` |
| 258 | Mudkip | 2005 | Japan | In-Life | 10 | `オーサカ` | `51126` | Torrent | pokeball | Tackle / Growl / Mud-slap / Water Gun | 6 allenatori, una voce ciascuno | `/events/dex/258.shtml` |
| 258 | Mudkip | 2005 | Japan | In-Life | 10 | `ナゴヤ` | `51126` | Torrent | pokeball | Tackle / Growl / Mud-slap / Water Gun | 6 allenatori, una voce ciascuno | `/events/dex/258.shtml` |
| 258 | Mudkip | 2005 | Japan | In-Life | 10 | `フクオカ` | `51126` | Torrent | pokeball | Tackle / Growl / Mud-slap / Water Gun | 6 allenatori, una voce ciascuno | `/events/dex/258.shtml` |
| 258 | Mudkip | 2005 | Japan | In-Life | 10 | `ヨコハマ` | `51126` | Torrent | pokeball | Tackle / Growl / Mud-slap / Water Gun | 6 allenatori, una voce ciascuno | `/events/dex/258.shtml` |
| 258 | Mudkip | 2005 | Japan | In-Life | 10 | `サッポロ` | `51126` | Torrent | pokeball | Tackle / Growl / Mud-slap / Water Gun | 6 allenatori, una voce ciascuno | `/events/dex/258.shtml` |
| 258 | Mudkip | 2010 | Japan | Global Link | 10 | `Yours` | `Yours` | Damp | - | Tackle / Growl / Mud-slap / Water Gun | allenatore del progetto, palla non dichiarata | `/events/dex/258.shtml` |
| 270 | Lotad | 2006 | Japan | In-Life | 10 | `トウキョー` | `60321` | Swift Swim or Rain Dish | pokeball | Astonish / Growl / Absorb | abilità alternativa, 6 allenatori, una voce ciascuno | `/events/dex/270.shtml` |
| 270 | Lotad | 2006 | Japan | In-Life | 10 | `オーサカ` | `60321` | Swift Swim or Rain Dish | pokeball | Astonish / Growl / Absorb | abilità alternativa, 6 allenatori, una voce ciascuno | `/events/dex/270.shtml` |
| 270 | Lotad | 2006 | Japan | In-Life | 10 | `ナゴヤ` | `60321` | Swift Swim or Rain Dish | pokeball | Astonish / Growl / Absorb | abilità alternativa, 6 allenatori, una voce ciascuno | `/events/dex/270.shtml` |
| 270 | Lotad | 2006 | Japan | In-Life | 10 | `フクオカ` | `60321` | Swift Swim or Rain Dish | pokeball | Astonish / Growl / Absorb | abilità alternativa, 6 allenatori, una voce ciascuno | `/events/dex/270.shtml` |
| 270 | Lotad | 2006 | Japan | In-Life | 10 | `ヨコハマ` | `60321` | Swift Swim or Rain Dish | pokeball | Astonish / Growl / Absorb | abilità alternativa, 6 allenatori, una voce ciascuno | `/events/dex/270.shtml` |
| 270 | Lotad | 2006 | Japan | In-Life | 10 | `サッポロ` | `60321` | Swift Swim or Rain Dish | pokeball | Astonish / Growl / Absorb | abilità alternativa, 6 allenatori, una voce ciascuno | `/events/dex/270.shtml` |
| 292 | Shedinja | 2003 | America | In-Life | 50 | `PCNYa` | `00001-01000` | Wonder Guard | pokeball | Spite / Confuse Ray / Shadow Ball / Grudge | 4 allenatori, una voce ciascuno | `/events/dex/292.shtml` |
| 292 | Shedinja | 2003 | America | In-Life | 50 | `PCNYb` | `00001-01000` | Wonder Guard | pokeball | Spite / Confuse Ray / Shadow Ball / Grudge | 4 allenatori, una voce ciascuno | `/events/dex/292.shtml` |
| 292 | Shedinja | 2003 | America | In-Life | 50 | `PCNYc` | `00001-01000` | Wonder Guard | pokeball | Spite / Confuse Ray / Shadow Ball / Grudge | 4 allenatori, una voce ciascuno | `/events/dex/292.shtml` |
| 292 | Shedinja | 2003 | America | In-Life | 50 | `PCNYd` | `00001-01000` | Wonder Guard | pokeball | Spite / Confuse Ray / Shadow Ball / Grudge | 4 allenatori, una voce ciascuno | `/events/dex/292.shtml` |
| 332 | Cacturne | 2003 | America | In-Life | 45 | `PCNYa` | `00001-01000` | Sand Veil | pokeball | Ingrain / Feint Attack / Spikes / Needle Arm | 4 allenatori, una voce ciascuno | `/events/dex/332.shtml` |
| 332 | Cacturne | 2003 | America | In-Life | 45 | `PCNYb` | `00001-01000` | Sand Veil | pokeball | Ingrain / Feint Attack / Spikes / Needle Arm | 4 allenatori, una voce ciascuno | `/events/dex/332.shtml` |
| 332 | Cacturne | 2003 | America | In-Life | 45 | `PCNYc` | `00001-01000` | Sand Veil | pokeball | Ingrain / Feint Attack / Spikes / Needle Arm | 4 allenatori, una voce ciascuno | `/events/dex/332.shtml` |
| 332 | Cacturne | 2003 | America | In-Life | 45 | `PCNYd` | `00001-01000` | Sand Veil | pokeball | Ingrain / Feint Attack / Spikes / Needle Arm | 4 allenatori, una voce ciascuno | `/events/dex/332.shtml` |
| 336 | Seviper | 2003 | America | In-Life | 18 | `PCNYa` | `00001-01000` | Shed Skin | pokeball | Wrap / Lick / Bite / Poison Tail | 4 allenatori, una voce ciascuno | `/events/dex/336.shtml` |
| 336 | Seviper | 2003 | America | In-Life | 18 | `PCNYb` | `00001-01000` | Shed Skin | pokeball | Wrap / Lick / Bite / Poison Tail | 4 allenatori, una voce ciascuno | `/events/dex/336.shtml` |
| 336 | Seviper | 2003 | America | In-Life | 18 | `PCNYc` | `00001-01000` | Shed Skin | pokeball | Wrap / Lick / Bite / Poison Tail | 4 allenatori, una voce ciascuno | `/events/dex/336.shtml` |
| 336 | Seviper | 2003 | America | In-Life | 18 | `PCNYd` | `00001-01000` | Shed Skin | pokeball | Wrap / Lick / Bite / Poison Tail | 4 allenatori, una voce ciascuno | `/events/dex/336.shtml` |
| 336 | Seviper | 2004 | America | In-Life | 30 | `PCNYc` | `000001-01000` | Shed Skin | pokeball | Poison Tail / Screech / Glare / Crunch | 2 allenatori, una voce ciascuno | `/events/dex/336.shtml` |
| 336 | Seviper | 2004 | America | In-Life | 30 | `PCNYd` | `000001-01000` | Shed Skin | pokeball | Poison Tail / Screech / Glare / Crunch | 2 allenatori, una voce ciascuno | `/events/dex/336.shtml` |
| 336 | Seviper | 2006 | Japan | In-Life | 10 | `トウキョー` | `60321` | Shed Skin | pokeball | Wrap / Lick / Bite | 6 allenatori, una voce ciascuno | `/events/dex/336.shtml` |
| 336 | Seviper | 2006 | Japan | In-Life | 10 | `オーサカ` | `60321` | Shed Skin | pokeball | Wrap / Lick / Bite | 6 allenatori, una voce ciascuno | `/events/dex/336.shtml` |
| 336 | Seviper | 2006 | Japan | In-Life | 10 | `ナゴヤ` | `60321` | Shed Skin | pokeball | Wrap / Lick / Bite | 6 allenatori, una voce ciascuno | `/events/dex/336.shtml` |
| 336 | Seviper | 2006 | Japan | In-Life | 10 | `フクオカ` | `60321` | Shed Skin | pokeball | Wrap / Lick / Bite | 6 allenatori, una voce ciascuno | `/events/dex/336.shtml` |
| 336 | Seviper | 2006 | Japan | In-Life | 10 | `ヨコハマ` | `60321` | Shed Skin | pokeball | Wrap / Lick / Bite | 6 allenatori, una voce ciascuno | `/events/dex/336.shtml` |
| 336 | Seviper | 2006 | Japan | In-Life | 10 | `サッポロ` | `60321` | Shed Skin | pokeball | Wrap / Lick / Bite | 6 allenatori, una voce ciascuno | `/events/dex/336.shtml` |
| 353 | Shuppet | 2003 | America | In-Life | 45 | `PCNYa` | `00001-01000` | Insomnia or Frisk | pokeball | Spite / Will-o-wisp / Feint Attack / Shadow Ball | abilità alternativa, 4 allenatori, una voce ciascuno | `/events/dex/353.shtml` |
| 353 | Shuppet | 2003 | America | In-Life | 45 | `PCNYb` | `00001-01000` | Insomnia or Frisk | pokeball | Spite / Will-o-wisp / Feint Attack / Shadow Ball | abilità alternativa, 4 allenatori, una voce ciascuno | `/events/dex/353.shtml` |
| 353 | Shuppet | 2003 | America | In-Life | 45 | `PCNYc` | `00001-01000` | Insomnia or Frisk | pokeball | Spite / Will-o-wisp / Feint Attack / Shadow Ball | abilità alternativa, 4 allenatori, una voce ciascuno | `/events/dex/353.shtml` |
| 353 | Shuppet | 2003 | America | In-Life | 45 | `PCNYd` | `00001-01000` | Insomnia or Frisk | pokeball | Spite / Will-o-wisp / Feint Attack / Shadow Ball | abilità alternativa, 4 allenatori, una voce ciascuno | `/events/dex/353.shtml` |
| 358 | Chimecho | 2006 | Japan | In-Life | 10 | `トウキョー` | `60321` | Levitate | pokeball | Wrap / Growl / Astonish | 6 allenatori, una voce ciascuno | `/events/dex/358.shtml` |
| 358 | Chimecho | 2006 | Japan | In-Life | 10 | `オーサカ` | `60321` | Levitate | pokeball | Wrap / Growl / Astonish | 6 allenatori, una voce ciascuno | `/events/dex/358.shtml` |
| 358 | Chimecho | 2006 | Japan | In-Life | 10 | `ナゴヤ` | `60321` | Levitate | pokeball | Wrap / Growl / Astonish | 6 allenatori, una voce ciascuno | `/events/dex/358.shtml` |
| 358 | Chimecho | 2006 | Japan | In-Life | 10 | `フクオカ` | `60321` | Levitate | pokeball | Wrap / Growl / Astonish | 6 allenatori, una voce ciascuno | `/events/dex/358.shtml` |
| 358 | Chimecho | 2006 | Japan | In-Life | 10 | `ヨコハマ` | `60321` | Levitate | pokeball | Wrap / Growl / Astonish | 6 allenatori, una voce ciascuno | `/events/dex/358.shtml` |
| 358 | Chimecho | 2006 | Japan | In-Life | 10 | `サッポロ` | `60321` | Levitate | pokeball | Wrap / Growl / Astonish | 6 allenatori, una voce ciascuno | `/events/dex/358.shtml` |
| 367 | Huntail | 2004 | America | In-Life | 20 | `PCNYd` | `00000-65535` | Swift Swim | pokeball | Whirlpool / Bite / Screech | nulla | `/events/dex/367.shtml` |
| 368 | Gorebyss | 2004 | America | In-Life | 20 | `PCNYd` | `00000-65535` | Swift Swim | pokeball | Whirlpool / Confusion / Agility | nulla | `/events/dex/368.shtml` |
| 396 | Starly | 2008 | Japan | In-Life | 1 | `だいすき` | `08311` | Keen Eye | pokeball | Tackle / Growl | nulla | `/events/dex/396.shtml` |
| 513 | Pansear | 2012 | Japan | Global Link | 10 | `Yours` | `Yours` | Blaze | - | Leer / Lick / Incinerate / Heat Wave | allenatore del progetto, palla non dichiarata | `/events/dex/513.shtml` |
| 515 | Panpour | 2012 | Japan | Global Link | 10 | `Yours` | `Yours` | Torrent | - | Leer / Lick / Water Gun / Hydro Pump | allenatore del progetto, palla non dichiarata | `/events/dex/515.shtml` |

