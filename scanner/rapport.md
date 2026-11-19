# Rapport koersverschil-scanner

Gemaakt 2026-11-19 10:43 UTC uit 5 runs, samen ±1.8 uur gemeten (GEZIEN).
Echte kans = winst na alle kosten (opnamekosten bekend), opnemen en storten open (en een netwerk dat aan beide kanten open is, als de beurzen dat geven), minstens €100,00 op het boek, minstens 2 minuten blijven staan, geen andere munt met dezelfde naam.
**Vergund** = beide beurzen hebben een MiCA-vergunning (ESMA-register), vaak via een EU-dochter die minder munten kan hebben dan de wereldwijde API die we meten (GOK). **Grijs** = minstens één beurs zonder vergunning (MEXC, Bitget, HTX, Poloniex, XT, Bitfinex, Binance). Zie README.md.

## Hoeveel wordt er gecontroleerd? (GEZIEN, stand.jsonl)

Per ronde (mediaan over 21 metingen): 998 kandidaten (verschil op de ticker groter dan de takerkosten), 120 met het orderboek gecontroleerd, 3 nog nooit gecontroleerd (0%).
Bijna alle kandidaten komen aan de beurt; de aantallen hieronder missen weinig.

## Trechter (GEZIEN, eigen metingen)

| Stap | Alle beurzen | Alleen MiCA-beurzen | Met minstens één grijze beurs |
|---|---|---|---|
| Verschillen met winst op het boek na alle kosten | 1366 | 120 | 1246 |
| ...waarvan opnemen of storten dicht | 261 | 22 | 239 |
| ...waarvan status onbekend (beurs geeft het niet openbaar) | 739 | 52 | 687 |
| Opnemen en storten open | 366 | 46 | 320 |
| ...en geen netwerk dat aan beide kanten open is: valt af | 3 | 0 | 3 |
| ...en opnamekosten onbekend: valt af | 0 | 0 | 0 |
| ...en minstens €100,00 op het boek | 100 | 32 | 68 |
| ...en minstens 2 minuten blijven staan | 24 | 6 | 18 |
| ...en geen andere munt met dezelfde naam | 22 | 5 | 17 |
|    ...waarvan contractadres bekend en gelijk | 1 | 0 | 1 |
|    ...waarvan contractadres onbekend (telt mee, kan een andere munt zijn) | 21 | 5 | 16 |
|    ...waarvan netwerk gekoppeld en open | 14 | 2 | 12 |
|    ...waarvan netwerk niet te koppelen (telt mee) | 8 | 3 | 5 |
| **Echte kansen** (zelfde munt overlappend in de tijd samengevoegd, beste beurspaar telt) | 15 | 5 | 11 |
| Ter vergelijking: zelfde eisen, maar opnamestatus onbekend (niet meegeteld) | 46 | 6 | 41 |

## Echte kansen per dag (GEZIEN)

| Dag | Echt, alleen MiCA | Echt, met grijs | Mediane winst per kans bij €500 (MiCA / grijs) | Mediane duur |
|---|---|---|---|---|
| 2026-11-19 | 4 | 11 | €1,00 / €0,52 | 7.3 min |
| Totaal | 4 | 11 | €1,00 / €0,52 | 7.3 min |

## Beste munten (GEZIEN)

| | Soort | Kansen | Som winst bij €500 per kans |
|---|---|---|---|
| VERONA-USDT | grijs | 3 | €9,42 |
| LUNC-USDT | grijs | 2 | €5,31 |
| MERL-EUR | vergund | 1 | €5,15 |
| CBK-USDT | grijs | 3 | €4,13 |
| USTC-USDT | vergund | 1 | €1,72 |
| CORE-USDT | grijs | 2 | €1,11 |
| DYM-EUR | vergund | 2 | €0,40 |
| USDT-EUR | grijs | 1 | €0,03 |

## Beste beursparen (kopen op > verkopen op) (GEZIEN)

| | Soort | Kansen | Som winst bij €500 per kans |
|---|---|---|---|
| bitget > gate | grijs | 1 | €8,38 |
| bitvavo > kraken | vergund | 3 | €5,55 |
| xt > htx | grijs | 1 | €3,52 |
| htx > xt | grijs | 1 | €3,27 |
| bitget > xt | grijs | 1 | €2,04 |
| kucoin > gate | vergund | 1 | €1,72 |
| bitget > htx | grijs | 3 | €1,45 |
| bitget > kucoin | grijs | 2 | €1,04 |
| gate > htx | grijs | 1 | €0,27 |
| kucoin > bitget | grijs | 1 | €0,03 |

Beurzen die het vaakst meedoen (koop of verkoop): bitget (grijs) 8, htx (grijs) 6, kucoin 4, xt (grijs) 3, gate 3, bitvavo 3, kraken 3 (GEZIEN).

## Hoeveel kansen blijven staan terwijl je geld schuift? (GEZIEN, duur uit eigen metingen)

Wie geen voorraad op beide beurzen heeft, moet kopen, de munt opnemen, wachten tot hij binnen is en dan verkopen. Hoe lang dat duurt verschilt per munt en netwerk: een paar minuten (snelle ketens) tot een uur of meer (Bitcoin, beurzen die opnames met de hand keuren) (GOK, niet per munt gemeten).

| Overmaaktijd | Alle beurzen | Alleen MiCA-beurzen | Met minstens één grijze beurs |
|---|---|---|---|
| 5 min | 9 van 15 (60%) | 3 van 5 (60%) | 7 van 11 (64%) |
| 10 min | 3 van 15 (20%) | 0 van 5 (0%) | 3 van 11 (27%) |
| 30 min | 1 van 15 (7%) | 0 van 5 (0%) | 1 van 11 (9%) |
| 60 min | 0 van 15 (0%) | 0 van 5 (0%) | 0 van 11 (0%) |

## Wat zou het opleveren over 3 maanden? (GOK, doorgetrokken uit de metingen)

Gemeten over ±1.8 uur (GEZIEN), doorgetrokken naar 90 dagen (GOK: aanname dat de week die we maten gewoon is).

| Beurzen | Inleg | Model | Kansen per uur | Per kans (mediaan) | 3 maanden |
|---|---|---|---|---|---|
| Alleen MiCA | €2.000,00 | bovengrens: elke kans, geld overal tegelijk | 2.86 | €1,72 | €10.591,58 |
| Alleen MiCA | €2.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 1.71 | €0,59 | €8.779,81 |
| Alleen MiCA | €5.000,00 | bovengrens: elke kans, geld overal tegelijk | 2.86 | €1,72 | €10.591,58 |
| Alleen MiCA | €5.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 1.71 | €0,60 | €9.934,42 |
| Alle (met grijs) | €2.000,00 | bovengrens: elke kans, geld overal tegelijk | 8.57 | €0,59 | €11.010,55 |
| Alle (met grijs) | €2.000,00 | alleen het beste beurspaar (bitget > gate) | 0.57 | €9,62 | €11.869,48 |
| Alle (met grijs) | €5.000,00 | bovengrens: elke kans, geld overal tegelijk | 8.57 | €0,60 | €11.084,59 |
| Alle (met grijs) | €5.000,00 | alleen het beste beurspaar (bitget > gate) | 0.57 | €9,62 | €11.869,48 |

Bovengrens: elke kans met de helft van de inleg aan elke kant, alsof het geld op alle beurzen tegelijk staat (kan in het echt niet). Beste beurspaar: het paar is **achteraf** gekozen uit de metingen (vooraf kiezen levert minder op), en het model neemt aan dat je van elke munt al voorraad op de verkoopbeurs hebt.

Waarom dit te rooskleurig is (GOK): elke kans wordt maar één keer geteld met het mediane boek, maar andere bots pakken hem ook; de munt die je als voorraad aanhoudt kan dalen; na een paar kansen moet de voorraad terug (opnamekosten en tijd); minimale opname- en ordergroottes tellen niet mee; en een kans die we 2 minuten zagen staan, staat er niet per se nog als jouw order binnenkomt. Waarom het te somber kan zijn: niet alle kandidaten zijn gecontroleerd, en met voorraad op beide beurzen kun je dezelfde kans vaker pakken als het boek zich aanvult; dat telt hier niet mee.

## Over de meting

- Opnamekosten bij de echte kansen: 6 van een netwerk dat aan beide kanten open is, 7 van de beurs zelf (laagste open netwerk), 2 geschat uit wat andere beurzen voor die munt vragen (GOK). Onbekende opnamekosten tellen niet als echte kans.
- Netwerk: KuCoin, Gate, Bitget, HTX, XT, Bitstamp, Bitvavo en Poloniex geven hun netwerken per munt. Als beide beurzen dat doen en de namen te koppelen zijn, moet er een netwerk zijn dat aan beide kanten open is. Anders is het netwerk "niet te koppelen" en telt de kans mee (staat apart in de trechter).
- De duur is gemeten in stappen van ±20 seconden; een kans kan een paar rondes eerder begonnen zijn dan we zagen.
- Takerkosten: uit de API waar die ze per paar geeft, anders het standaardtarief uit de README (deels GOK).
- Laatste run: 15 beurzen antwoordden, 2293 munt-quote-paren op minstens twee beurzen (GEZIEN).
