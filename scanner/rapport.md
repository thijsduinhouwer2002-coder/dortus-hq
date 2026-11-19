# Rapport koersverschil-scanner

Gemaakt 2026-11-19 14:13 UTC uit 5 runs, samen ±5.3 uur gemeten (GEZIEN).
Echte kans = winst na alle kosten (opnamekosten bekend), opnemen en storten open (en een netwerk dat aan beide kanten open is, als de beurzen dat geven), minstens €100,00 op het boek, minstens 2 minuten blijven staan, geen andere munt met dezelfde naam.
**Vergund** = beide beurzen hebben een MiCA-vergunning (ESMA-register), vaak via een EU-dochter die minder munten kan hebben dan de wereldwijde API die we meten (GOK). **Grijs** = minstens één beurs zonder vergunning (MEXC, Bitget, HTX, Poloniex, XT, Bitfinex, Binance). Zie README.md.

## Hoeveel wordt er gecontroleerd? (GEZIEN, stand.jsonl)

Per ronde (mediaan over 64 metingen): 1044 kandidaten (verschil op de ticker groter dan de takerkosten), 120 met het orderboek gecontroleerd, 2 nog nooit gecontroleerd (0%).
Bijna alle kandidaten komen aan de beurt; de aantallen hieronder missen weinig.

## Trechter (GEZIEN, eigen metingen)

| Stap | Alle beurzen | Alleen MiCA-beurzen | Met minstens één grijze beurs |
|---|---|---|---|
| Verschillen met winst op het boek na alle kosten | 4017 | 467 | 3550 |
| ...waarvan opnemen of storten dicht | 699 | 61 | 638 |
| ...waarvan status onbekend (beurs geeft het niet openbaar) | 2280 | 227 | 2053 |
| Opnemen en storten open | 1038 | 179 | 859 |
| ...en geen netwerk dat aan beide kanten open is: valt af | 12 | 0 | 12 |
| ...en opnamekosten onbekend: valt af | 0 | 0 | 0 |
| ...en minstens €100,00 op het boek | 335 | 139 | 196 |
| ...en minstens 2 minuten blijven staan | 75 | 35 | 40 |
| ...en geen andere munt met dezelfde naam | 71 | 34 | 37 |
|    ...waarvan contractadres bekend en gelijk | 5 | 1 | 4 |
|    ...waarvan contractadres onbekend (telt mee, kan een andere munt zijn) | 66 | 33 | 33 |
|    ...waarvan netwerk gekoppeld en open | 33 | 6 | 27 |
|    ...waarvan netwerk niet te koppelen (telt mee) | 38 | 28 | 10 |
| **Echte kansen** (zelfde munt overlappend in de tijd samengevoegd, beste beurspaar telt) | 57 | 34 | 26 |
| Ter vergelijking: zelfde eisen, maar opnamestatus onbekend (niet meegeteld) | 153 | 38 | 128 |

## Echte kansen per dag (GEZIEN)

| Dag | Echt, alleen MiCA | Echt, met grijs | Mediane winst per kans bij €500 (MiCA / grijs) | Mediane duur |
|---|---|---|---|---|
| 2026-11-19 | 31 | 26 | €0,93 / €0,65 | 4.3 min |
| Totaal | 31 | 26 | €0,93 / €0,65 | 4.3 min |

## Beste munten (GEZIEN)

| | Soort | Kansen | Som winst bij €500 per kans |
|---|---|---|---|
| MERL-EUR | vergund | 4 | €20,30 |
| VERONA-USDT | grijs | 4 | €10,44 |
| DYM-EUR | vergund | 15 | €9,97 |
| LUNA-EUR | vergund | 4 | €6,79 |
| LUNC-USDT | grijs | 2 | €5,69 |
| WAN-USDT | grijs | 2 | €4,87 |
| GMT-EUR | vergund | 3 | €4,75 |
| CBK-USDT | grijs | 3 | €4,13 |
| USTC-USDT | vergund | 3 | €2,25 |
| LUNA-USDT | grijs | 1 | €2,09 |

## Beste beursparen (kopen op > verkopen op) (GEZIEN)

| | Soort | Kansen | Som winst bij €500 per kans |
|---|---|---|---|
| bitvavo > kraken | vergund | 27 | €41,54 |
| bitget > gate | grijs | 3 | €9,96 |
| kucoin > htx | grijs | 4 | €5,87 |
| bitget > htx | grijs | 5 | €3,98 |
| bitget > xt | grijs | 2 | €3,96 |
| kucoin > xt | grijs | 1 | €3,65 |
| xt > htx | grijs | 1 | €3,52 |
| kucoin > gate | vergund | 3 | €2,25 |
| bitget > kucoin | grijs | 3 | €2,19 |
| poloniex > htx | grijs | 1 | €1,20 |

Beurzen die het vaakst meedoen (koop of verkoop): bitvavo 27, kraken 27, bitget (grijs) 15, kucoin 15, htx (grijs) 14, gate 9, xt (grijs) 5, poloniex (grijs) 2 (GEZIEN).

## Hoeveel kansen blijven staan terwijl je geld schuift? (GEZIEN, duur uit eigen metingen)

Wie geen voorraad op beide beurzen heeft, moet kopen, de munt opnemen, wachten tot hij binnen is en dan verkopen. Hoe lang dat duurt verschilt per munt en netwerk: een paar minuten (snelle ketens) tot een uur of meer (Bitcoin, beurzen die opnames met de hand keuren) (GOK, niet per munt gemeten).

| Overmaaktijd | Alle beurzen | Alleen MiCA-beurzen | Met minstens één grijze beurs |
|---|---|---|---|
| 5 min | 25 van 57 (44%) | 11 van 34 (32%) | 16 van 26 (62%) |
| 10 min | 10 van 57 (18%) | 5 van 34 (15%) | 6 van 26 (23%) |
| 30 min | 6 van 57 (11%) | 3 van 34 (9%) | 3 van 26 (12%) |
| 60 min | 4 van 57 (7%) | 3 van 34 (9%) | 1 van 26 (4%) |

## Wat zou het opleveren over 3 maanden? (GOK, doorgetrokken uit de metingen)

Gemeten over ±5.3 uur (GEZIEN), doorgetrokken naar 90 dagen (GOK: aanname dat de week die we maten gewoon is).

| Beurzen | Inleg | Model | Kansen per uur | Per kans (mediaan) | 3 maanden |
|---|---|---|---|---|---|
| Alleen MiCA | €2.000,00 | bovengrens: elke kans, geld overal tegelijk | 6.37 | €1,13 | €15.562,04 |
| Alleen MiCA | €2.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 5.06 | €1,37 | €25.053,17 |
| Alleen MiCA | €5.000,00 | bovengrens: elke kans, geld overal tegelijk | 6.37 | €1,35 | €18.656,69 |
| Alleen MiCA | €5.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 5.06 | €1,80 | €30.859,92 |
| Alle (met grijs) | €2.000,00 | bovengrens: elke kans, geld overal tegelijk | 10.69 | €0,92 | €21.214,01 |
| Alle (met grijs) | €2.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 5.06 | €1,37 | €25.053,17 |
| Alle (met grijs) | €5.000,00 | bovengrens: elke kans, geld overal tegelijk | 10.69 | €1,02 | €23.628,58 |
| Alle (met grijs) | €5.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 5.06 | €1,80 | €30.859,92 |

Bovengrens: elke kans met de helft van de inleg aan elke kant, alsof het geld op alle beurzen tegelijk staat (kan in het echt niet). Beste beurspaar: het paar is **achteraf** gekozen uit de metingen (vooraf kiezen levert minder op), en het model neemt aan dat je van elke munt al voorraad op de verkoopbeurs hebt.

Waarom dit te rooskleurig is (GOK): elke kans wordt maar één keer geteld met het mediane boek, maar andere bots pakken hem ook; de munt die je als voorraad aanhoudt kan dalen; na een paar kansen moet de voorraad terug (opnamekosten en tijd); minimale opname- en ordergroottes tellen niet mee; en een kans die we 2 minuten zagen staan, staat er niet per se nog als jouw order binnenkomt. Waarom het te somber kan zijn: niet alle kandidaten zijn gecontroleerd, en met voorraad op beide beurzen kun je dezelfde kans vaker pakken als het boek zich aanvult; dat telt hier niet mee.

## Over de meting

- Opnamekosten bij de echte kansen: 19 van een netwerk dat aan beide kanten open is, 35 van de beurs zelf (laagste open netwerk), 3 geschat uit wat andere beurzen voor die munt vragen (GOK). Onbekende opnamekosten tellen niet als echte kans.
- Netwerk: KuCoin, Gate, Bitget, HTX, XT, Bitstamp, Bitvavo en Poloniex geven hun netwerken per munt. Als beide beurzen dat doen en de namen te koppelen zijn, moet er een netwerk zijn dat aan beide kanten open is. Anders is het netwerk "niet te koppelen" en telt de kans mee (staat apart in de trechter).
- De duur is gemeten in stappen van ±20 seconden; een kans kan een paar rondes eerder begonnen zijn dan we zagen.
- Takerkosten: uit de API waar die ze per paar geeft, anders het standaardtarief uit de README (deels GOK).
- Laatste run: 15 beurzen antwoordden, 2287 munt-quote-paren op minstens twee beurzen (GEZIEN).
