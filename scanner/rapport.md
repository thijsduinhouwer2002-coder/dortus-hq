# Rapport koersverschil-scanner

Gemaakt 2026-11-19 14:43 UTC uit 5 runs, samen ±5.8 uur gemeten (GEZIEN).
Echte kans = winst na alle kosten (opnamekosten bekend), opnemen en storten open (en een netwerk dat aan beide kanten open is, als de beurzen dat geven), minstens €100,00 op het boek, minstens 2 minuten blijven staan, geen andere munt met dezelfde naam.
**Vergund** = beide beurzen hebben een MiCA-vergunning (ESMA-register), vaak via een EU-dochter die minder munten kan hebben dan de wereldwijde API die we meten (GOK). **Grijs** = minstens één beurs zonder vergunning (MEXC, Bitget, HTX, Poloniex, XT, Bitfinex, Binance). Zie README.md.

## Hoeveel wordt er gecontroleerd? (GEZIEN, stand.jsonl)

Per ronde (mediaan over 70 metingen): 1039 kandidaten (verschil op de ticker groter dan de takerkosten), 120 met het orderboek gecontroleerd, 2 nog nooit gecontroleerd (0%).
Bijna alle kandidaten komen aan de beurt; de aantallen hieronder missen weinig.

## Trechter (GEZIEN, eigen metingen)

| Stap | Alle beurzen | Alleen MiCA-beurzen | Met minstens één grijze beurs |
|---|---|---|---|
| Verschillen met winst op het boek na alle kosten | 4298 | 545 | 3753 |
| ...waarvan opnemen of storten dicht | 750 | 63 | 687 |
| ...waarvan status onbekend (beurs geeft het niet openbaar) | 2476 | 292 | 2184 |
| Opnemen en storten open | 1072 | 190 | 882 |
| ...en geen netwerk dat aan beide kanten open is: valt af | 14 | 0 | 14 |
| ...en opnamekosten onbekend: valt af | 0 | 0 | 0 |
| ...en minstens €100,00 op het boek | 351 | 147 | 204 |
| ...en minstens 2 minuten blijven staan | 78 | 38 | 40 |
| ...en geen andere munt met dezelfde naam | 74 | 37 | 37 |
|    ...waarvan contractadres bekend en gelijk | 5 | 1 | 4 |
|    ...waarvan contractadres onbekend (telt mee, kan een andere munt zijn) | 69 | 36 | 33 |
|    ...waarvan netwerk gekoppeld en open | 33 | 6 | 27 |
|    ...waarvan netwerk niet te koppelen (telt mee) | 41 | 31 | 10 |
| **Echte kansen** (zelfde munt overlappend in de tijd samengevoegd, beste beurspaar telt) | 60 | 37 | 26 |
| Ter vergelijking: zelfde eisen, maar opnamestatus onbekend (niet meegeteld) | 171 | 44 | 140 |

## Echte kansen per dag (GEZIEN)

| Dag | Echt, alleen MiCA | Echt, met grijs | Mediane winst per kans bij €500 (MiCA / grijs) | Mediane duur |
|---|---|---|---|---|
| 2026-11-19 | 34 | 26 | €1,11 / €0,65 | 4.3 min |
| Totaal | 34 | 26 | €1,11 / €0,65 | 4.3 min |

## Beste munten (GEZIEN)

| | Soort | Kansen | Som winst bij €500 per kans |
|---|---|---|---|
| MERL-EUR | vergund | 5 | €31,94 |
| LUNA-EUR | vergund | 5 | €12,93 |
| DYM-EUR | vergund | 16 | €11,91 |
| VERONA-USDT | grijs | 4 | €10,44 |
| LUNC-USDT | grijs | 2 | €5,69 |
| WAN-USDT | grijs | 2 | €4,87 |
| GMT-EUR | vergund | 3 | €4,75 |
| CBK-USDT | grijs | 3 | €4,13 |
| USTC-USDT | vergund | 3 | €2,25 |
| LUNA-USDT | grijs | 1 | €2,09 |

## Beste beursparen (kopen op > verkopen op) (GEZIEN)

| | Soort | Kansen | Som winst bij €500 per kans |
|---|---|---|---|
| bitvavo > kraken | vergund | 30 | €61,25 |
| bitget > gate | grijs | 3 | €9,96 |
| kucoin > htx | grijs | 4 | €5,87 |
| bitget > htx | grijs | 5 | €3,98 |
| bitget > xt | grijs | 2 | €3,96 |
| kucoin > xt | grijs | 1 | €3,65 |
| xt > htx | grijs | 1 | €3,52 |
| kucoin > gate | vergund | 3 | €2,25 |
| bitget > kucoin | grijs | 3 | €2,19 |
| poloniex > htx | grijs | 1 | €1,20 |

Beurzen die het vaakst meedoen (koop of verkoop): bitvavo 30, kraken 30, bitget (grijs) 15, kucoin 15, htx (grijs) 14, gate 9, xt (grijs) 5, poloniex (grijs) 2 (GEZIEN).

## Hoeveel kansen blijven staan terwijl je geld schuift? (GEZIEN, duur uit eigen metingen)

Wie geen voorraad op beide beurzen heeft, moet kopen, de munt opnemen, wachten tot hij binnen is en dan verkopen. Hoe lang dat duurt verschilt per munt en netwerk: een paar minuten (snelle ketens) tot een uur of meer (Bitcoin, beurzen die opnames met de hand keuren) (GOK, niet per munt gemeten).

| Overmaaktijd | Alle beurzen | Alleen MiCA-beurzen | Met minstens één grijze beurs |
|---|---|---|---|
| 5 min | 28 van 60 (47%) | 14 van 37 (38%) | 16 van 26 (62%) |
| 10 min | 13 van 60 (22%) | 8 van 37 (22%) | 6 van 26 (23%) |
| 30 min | 8 van 60 (13%) | 5 van 37 (14%) | 3 van 26 (12%) |
| 60 min | 4 van 60 (7%) | 3 van 37 (8%) | 1 van 26 (4%) |

## Wat zou het opleveren over 3 maanden? (GOK, doorgetrokken uit de metingen)

Gemeten over ±5.8 uur (GEZIEN), doorgetrokken naar 90 dagen (GOK: aanname dat de week die we maten gewoon is).

| Beurzen | Inleg | Model | Kansen per uur | Per kans (mediaan) | 3 maanden |
|---|---|---|---|---|---|
| Alleen MiCA | €2.000,00 | bovengrens: elke kans, geld overal tegelijk | 6.34 | €1,37 | €18.748,34 |
| Alleen MiCA | €2.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 5.14 | €1,76 | €35.295,73 |
| Alleen MiCA | €5.000,00 | bovengrens: elke kans, geld overal tegelijk | 6.34 | €1,72 | €23.515,91 |
| Alleen MiCA | €5.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 5.14 | €2,09 | €46.967,54 |
| Alle (met grijs) | €2.000,00 | bovengrens: elke kans, geld overal tegelijk | 10.29 | €1,09 | €24.322,17 |
| Alle (met grijs) | €2.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 5.14 | €1,76 | €35.295,73 |
| Alle (met grijs) | €5.000,00 | bovengrens: elke kans, geld overal tegelijk | 10.29 | €1,19 | €26.408,26 |
| Alle (met grijs) | €5.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 5.14 | €2,09 | €46.967,54 |

Bovengrens: elke kans met de helft van de inleg aan elke kant, alsof het geld op alle beurzen tegelijk staat (kan in het echt niet). Beste beurspaar: het paar is **achteraf** gekozen uit de metingen (vooraf kiezen levert minder op), en het model neemt aan dat je van elke munt al voorraad op de verkoopbeurs hebt.

Waarom dit te rooskleurig is (GOK): elke kans wordt maar één keer geteld met het mediane boek, maar andere bots pakken hem ook; de munt die je als voorraad aanhoudt kan dalen; na een paar kansen moet de voorraad terug (opnamekosten en tijd); minimale opname- en ordergroottes tellen niet mee; en een kans die we 2 minuten zagen staan, staat er niet per se nog als jouw order binnenkomt. Waarom het te somber kan zijn: niet alle kandidaten zijn gecontroleerd, en met voorraad op beide beurzen kun je dezelfde kans vaker pakken als het boek zich aanvult; dat telt hier niet mee.

## Over de meting

- Opnamekosten bij de echte kansen: 19 van een netwerk dat aan beide kanten open is, 38 van de beurs zelf (laagste open netwerk), 3 geschat uit wat andere beurzen voor die munt vragen (GOK). Onbekende opnamekosten tellen niet als echte kans.
- Netwerk: KuCoin, Gate, Bitget, HTX, XT, Bitstamp, Bitvavo en Poloniex geven hun netwerken per munt. Als beide beurzen dat doen en de namen te koppelen zijn, moet er een netwerk zijn dat aan beide kanten open is. Anders is het netwerk "niet te koppelen" en telt de kans mee (staat apart in de trechter).
- De duur is gemeten in stappen van ±20 seconden; een kans kan een paar rondes eerder begonnen zijn dan we zagen.
- Takerkosten: uit de API waar die ze per paar geeft, anders het standaardtarief uit de README (deels GOK).
- Laatste run: 15 beurzen antwoordden, 2287 munt-quote-paren op minstens twee beurzen (GEZIEN).
