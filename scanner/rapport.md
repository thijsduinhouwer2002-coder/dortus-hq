# Rapport koersverschil-scanner

Gemaakt 2026-11-19 11:13 UTC uit 5 runs, samen ±2.3 uur gemeten (GEZIEN).
Echte kans = winst na alle kosten (opnamekosten bekend), opnemen en storten open (en een netwerk dat aan beide kanten open is, als de beurzen dat geven), minstens €100,00 op het boek, minstens 2 minuten blijven staan, geen andere munt met dezelfde naam.
**Vergund** = beide beurzen hebben een MiCA-vergunning (ESMA-register), vaak via een EU-dochter die minder munten kan hebben dan de wereldwijde API die we meten (GOK). **Grijs** = minstens één beurs zonder vergunning (MEXC, Bitget, HTX, Poloniex, XT, Bitfinex, Binance). Zie README.md.

## Hoeveel wordt er gecontroleerd? (GEZIEN, stand.jsonl)

Per ronde (mediaan over 28 metingen): 1017 kandidaten (verschil op de ticker groter dan de takerkosten), 120 met het orderboek gecontroleerd, 3 nog nooit gecontroleerd (0%).
Bijna alle kandidaten komen aan de beurt; de aantallen hieronder missen weinig.

## Trechter (GEZIEN, eigen metingen)

| Stap | Alle beurzen | Alleen MiCA-beurzen | Met minstens één grijze beurs |
|---|---|---|---|
| Verschillen met winst op het boek na alle kosten | 1744 | 160 | 1584 |
| ...waarvan opnemen of storten dicht | 311 | 25 | 286 |
| ...waarvan status onbekend (beurs geeft het niet openbaar) | 944 | 63 | 881 |
| Opnemen en storten open | 489 | 72 | 417 |
| ...en geen netwerk dat aan beide kanten open is: valt af | 3 | 0 | 3 |
| ...en opnamekosten onbekend: valt af | 0 | 0 | 0 |
| ...en minstens €100,00 op het boek | 147 | 54 | 93 |
| ...en minstens 2 minuten blijven staan | 39 | 13 | 26 |
| ...en geen andere munt met dezelfde naam | 37 | 12 | 25 |
|    ...waarvan contractadres bekend en gelijk | 5 | 1 | 4 |
|    ...waarvan contractadres onbekend (telt mee, kan een andere munt zijn) | 32 | 11 | 21 |
|    ...waarvan netwerk gekoppeld en open | 23 | 4 | 19 |
|    ...waarvan netwerk niet te koppelen (telt mee) | 14 | 8 | 6 |
| **Echte kansen** (zelfde munt overlappend in de tijd samengevoegd, beste beurspaar telt) | 26 | 12 | 17 |
| Ter vergelijking: zelfde eisen, maar opnamestatus onbekend (niet meegeteld) | 56 | 8 | 50 |

## Echte kansen per dag (GEZIEN)

| Dag | Echt, alleen MiCA | Echt, met grijs | Mediane winst per kans bij €500 (MiCA / grijs) | Mediane duur |
|---|---|---|---|---|
| 2026-11-19 | 9 | 17 | €0,35 / €0,56 | 5.7 min |
| Totaal | 9 | 17 | €0,35 / €0,56 | 5.7 min |

## Beste munten (GEZIEN)

| | Soort | Kansen | Som winst bij €500 per kans |
|---|---|---|---|
| VERONA-USDT | grijs | 3 | €9,42 |
| MERL-EUR | vergund | 2 | €9,35 |
| LUNC-USDT | grijs | 3 | €5,53 |
| CBK-USDT | grijs | 3 | €4,13 |
| KOR-USDT | grijs | 1 | €1,92 |
| USTC-USDT | vergund | 1 | €1,72 |
| LUNA-EUR | vergund | 1 | €1,24 |
| MTX-USDT | grijs | 1 | €1,15 |
| DYM-EUR | vergund | 5 | €1,11 |
| CORE-USDT | grijs | 2 | €1,11 |

## Beste beursparen (kopen op > verkopen op) (GEZIEN)

| | Soort | Kansen | Som winst bij €500 per kans |
|---|---|---|---|
| bitvavo > kraken | vergund | 8 | €11,71 |
| bitget > gate | grijs | 2 | €8,94 |
| bitget > xt | grijs | 2 | €3,96 |
| xt > htx | grijs | 1 | €3,52 |
| htx > xt | grijs | 1 | €3,27 |
| bitget > kucoin | grijs | 3 | €2,19 |
| kucoin > gate | vergund | 1 | €1,72 |
| bitget > htx | grijs | 3 | €1,45 |
| gate > htx | grijs | 2 | €0,94 |
| kucoin > htx | grijs | 1 | €0,55 |

Beurzen die het vaakst meedoen (koop of verkoop): bitget (grijs) 12, htx (grijs) 8, bitvavo 8, kraken 8, kucoin 7, gate 5, xt (grijs) 4 (GEZIEN).

## Hoeveel kansen blijven staan terwijl je geld schuift? (GEZIEN, duur uit eigen metingen)

Wie geen voorraad op beide beurzen heeft, moet kopen, de munt opnemen, wachten tot hij binnen is en dan verkopen. Hoe lang dat duurt verschilt per munt en netwerk: een paar minuten (snelle ketens) tot een uur of meer (Bitcoin, beurzen die opnames met de hand keuren) (GOK, niet per munt gemeten).

| Overmaaktijd | Alle beurzen | Alleen MiCA-beurzen | Met minstens één grijze beurs |
|---|---|---|---|
| 5 min | 13 van 26 (50%) | 5 van 12 (42%) | 10 van 17 (59%) |
| 10 min | 6 van 26 (23%) | 2 van 12 (17%) | 5 van 17 (29%) |
| 30 min | 2 van 26 (8%) | 1 van 12 (8%) | 1 van 17 (6%) |
| 60 min | 1 van 26 (4%) | 1 van 12 (8%) | 0 van 17 (0%) |

## Wat zou het opleveren over 3 maanden? (GOK, doorgetrokken uit de metingen)

Gemeten over ±2.3 uur (GEZIEN), doorgetrokken naar 90 dagen (GOK: aanname dat de week die we maten gewoon is).

| Beurzen | Inleg | Model | Kansen per uur | Per kans (mediaan) | 3 maanden |
|---|---|---|---|---|---|
| Alleen MiCA | €2.000,00 | bovengrens: elke kans, geld overal tegelijk | 5.14 | €0,66 | €7.307,46 |
| Alleen MiCA | €2.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 3.43 | €0,66 | €14.169,52 |
| Alleen MiCA | €5.000,00 | bovengrens: elke kans, geld overal tegelijk | 5.14 | €0,66 | €7.329,67 |
| Alleen MiCA | €5.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 3.43 | €0,66 | €16.027,39 |
| Alle (met grijs) | €2.000,00 | bovengrens: elke kans, geld overal tegelijk | 11.14 | €0,63 | €15.275,71 |
| Alle (met grijs) | €2.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 3.43 | €0,66 | €14.169,52 |
| Alle (met grijs) | €5.000,00 | bovengrens: elke kans, geld overal tegelijk | 11.14 | €0,64 | €15.323,84 |
| Alle (met grijs) | €5.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 3.43 | €0,66 | €16.027,39 |

Bovengrens: elke kans met de helft van de inleg aan elke kant, alsof het geld op alle beurzen tegelijk staat (kan in het echt niet). Beste beurspaar: het paar is **achteraf** gekozen uit de metingen (vooraf kiezen levert minder op), en het model neemt aan dat je van elke munt al voorraad op de verkoopbeurs hebt.

Waarom dit te rooskleurig is (GOK): elke kans wordt maar één keer geteld met het mediane boek, maar andere bots pakken hem ook; de munt die je als voorraad aanhoudt kan dalen; na een paar kansen moet de voorraad terug (opnamekosten en tijd); minimale opname- en ordergroottes tellen niet mee; en een kans die we 2 minuten zagen staan, staat er niet per se nog als jouw order binnenkomt. Waarom het te somber kan zijn: niet alle kandidaten zijn gecontroleerd, en met voorraad op beide beurzen kun je dezelfde kans vaker pakken als het boek zich aanvult; dat telt hier niet mee.

## Over de meting

- Opnamekosten bij de echte kansen: 10 van een netwerk dat aan beide kanten open is, 13 van de beurs zelf (laagste open netwerk), 3 geschat uit wat andere beurzen voor die munt vragen (GOK). Onbekende opnamekosten tellen niet als echte kans.
- Netwerk: KuCoin, Gate, Bitget, HTX, XT, Bitstamp, Bitvavo en Poloniex geven hun netwerken per munt. Als beide beurzen dat doen en de namen te koppelen zijn, moet er een netwerk zijn dat aan beide kanten open is. Anders is het netwerk "niet te koppelen" en telt de kans mee (staat apart in de trechter).
- De duur is gemeten in stappen van ±20 seconden; een kans kan een paar rondes eerder begonnen zijn dan we zagen.
- Takerkosten: uit de API waar die ze per paar geeft, anders het standaardtarief uit de README (deels GOK).
- Laatste run: 15 beurzen antwoordden, 2293 munt-quote-paren op minstens twee beurzen (GEZIEN).
