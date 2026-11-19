# Rapport koersverschil-scanner

Gemaakt 2026-11-19 09:42 UTC uit 4 runs, samen ±0.8 uur gemeten (GEZIEN).
Echte kans = winst na alle kosten (opnamekosten bekend), opnemen en storten open (en een netwerk dat aan beide kanten open is, als de beurzen dat geven), minstens €100,00 op het boek, minstens 2 minuten blijven staan, geen andere munt met dezelfde naam.
**Vergund** = beide beurzen hebben een MiCA-vergunning (ESMA-register), vaak via een EU-dochter die minder munten kan hebben dan de wereldwijde API die we meten (GOK). **Grijs** = minstens één beurs zonder vergunning (MEXC, Bitget, HTX, Poloniex, XT, Bitfinex, Binance). Zie README.md.

## Hoeveel wordt er gecontroleerd? (GEZIEN, stand.jsonl)

Per ronde (mediaan over 9 metingen): 988 kandidaten (verschil op de ticker groter dan de takerkosten), 100 met het orderboek gecontroleerd, 715 nog nooit gecontroleerd (70%).
**Daarom zijn de aantallen en sommen hieronder een ondergrens:** een deel van de kandidaten is nooit met het boek bekeken.

## Trechter (GEZIEN, eigen metingen)

| Stap | Alle beurzen | Alleen MiCA-beurzen | Met minstens één grijze beurs |
|---|---|---|---|
| Verschillen met winst op het boek na alle kosten | 478 | 51 | 427 |
| ...waarvan opnemen of storten dicht | 132 | 11 | 121 |
| ...waarvan status onbekend (beurs geeft het niet openbaar) | 232 | 24 | 208 |
| Opnemen en storten open | 114 | 16 | 98 |
| ...en geen netwerk dat aan beide kanten open is: valt af | 3 | 0 | 3 |
| ...en opnamekosten onbekend: valt af | 0 | 0 | 0 |
| ...en minstens €100,00 op het boek | 32 | 9 | 23 |
| ...en minstens 2 minuten blijven staan | 11 | 2 | 9 |
| ...en geen andere munt met dezelfde naam | 9 | 1 | 8 |
|    ...waarvan contractadres bekend en gelijk | 0 | 0 | 0 |
|    ...waarvan contractadres onbekend (telt mee, kan een andere munt zijn) | 9 | 1 | 8 |
|    ...waarvan netwerk gekoppeld en open | 4 | 0 | 4 |
|    ...waarvan netwerk niet te koppelen (telt mee) | 5 | 1 | 4 |
| **Echte kansen** (zelfde munt overlappend in de tijd samengevoegd, beste beurspaar telt) | 6 | 1 | 5 |
| Ter vergelijking: zelfde eisen, maar opnamestatus onbekend (niet meegeteld) | 20 | 6 | 15 |

## Echte kansen per dag (GEZIEN)

| Dag | Echt, alleen MiCA | Echt, met grijs | Mediane winst per kans bij €500 (MiCA / grijs) | Mediane duur |
|---|---|---|---|---|
| 2026-11-19 | 1 | 5 | €5,15 / €0,52 | 7.2 min |
| Totaal | 1 | 5 | €5,15 / €0,52 | 7.2 min |

## Beste munten (GEZIEN)

| | Soort | Kansen | Som winst bij €500 per kans |
|---|---|---|---|
| MERL-EUR | vergund | 1 | €5,15 |
| CBK-USDT | grijs | 2 | €3,86 |
| LUNC-USDT | grijs | 1 | €2,04 |
| VERONA-USDT | grijs | 1 | €0,52 |
| CORE-USDT | grijs | 1 | €0,32 |

## Beste beursparen (kopen op > verkopen op) (GEZIEN)

| | Soort | Kansen | Som winst bij €500 per kans |
|---|---|---|---|
| bitvavo > kraken | vergund | 1 | €5,15 |
| xt > htx | grijs | 1 | €3,52 |
| bitget > xt | grijs | 1 | €2,04 |
| bitget > htx | grijs | 2 | €0,67 |
| bitget > kucoin | grijs | 1 | €0,52 |

Beurzen die het vaakst meedoen (koop of verkoop): bitget (grijs) 4, htx (grijs) 3, xt (grijs) 2, bitvavo 1, kraken 1, kucoin 1 (GEZIEN).

## Hoeveel kansen blijven staan terwijl je geld schuift? (GEZIEN, duur uit eigen metingen)

Wie geen voorraad op beide beurzen heeft, moet kopen, de munt opnemen, wachten tot hij binnen is en dan verkopen. Hoe lang dat duurt verschilt per munt en netwerk: een paar minuten (snelle ketens) tot een uur of meer (Bitcoin, beurzen die opnames met de hand keuren) (GOK, niet per munt gemeten).

| Overmaaktijd | Alle beurzen | Alleen MiCA-beurzen | Met minstens één grijze beurs |
|---|---|---|---|
| 5 min | 4 van 6 (67%) | 1 van 1 (100%) | 3 van 5 (60%) |
| 10 min | 0 van 6 (0%) | 0 van 1 (0%) | 0 van 5 (0%) |
| 30 min | 0 van 6 (0%) | 0 van 1 (0%) | 0 van 5 (0%) |
| 60 min | 0 van 6 (0%) | 0 van 1 (0%) | 0 van 5 (0%) |

## Wat zou het opleveren over 3 maanden? (GOK, doorgetrokken uit de metingen)

Te weinig gemeten om door te trekken.

## Over de meting

- Opnamekosten bij de echte kansen: 2 van een netwerk dat aan beide kanten open is, 4 van de beurs zelf (laagste open netwerk), 0 geschat uit wat andere beurzen voor die munt vragen (GOK). Onbekende opnamekosten tellen niet als echte kans.
- Netwerk: KuCoin, Gate, Bitget, HTX, XT, Bitstamp, Bitvavo en Poloniex geven hun netwerken per munt. Als beide beurzen dat doen en de namen te koppelen zijn, moet er een netwerk zijn dat aan beide kanten open is. Anders is het netwerk "niet te koppelen" en telt de kans mee (staat apart in de trechter).
- De duur is gemeten in stappen van ±20 seconden; een kans kan een paar rondes eerder begonnen zijn dan we zagen.
- Takerkosten: uit de API waar die ze per paar geeft, anders het standaardtarief uit de README (deels GOK).
- Laatste run: 15 beurzen antwoordden, 2294 munt-quote-paren op minstens twee beurzen (GEZIEN).
