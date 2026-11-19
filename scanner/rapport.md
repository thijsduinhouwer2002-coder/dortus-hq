# Rapport koersverschil-scanner

Gemaakt 2026-11-19 13:13 UTC uit 5 runs, samen ±4.3 uur gemeten (GEZIEN).
Echte kans = winst na alle kosten (opnamekosten bekend), opnemen en storten open (en een netwerk dat aan beide kanten open is, als de beurzen dat geven), minstens €100,00 op het boek, minstens 2 minuten blijven staan, geen andere munt met dezelfde naam.
**Vergund** = beide beurzen hebben een MiCA-vergunning (ESMA-register), vaak via een EU-dochter die minder munten kan hebben dan de wereldwijde API die we meten (GOK). **Grijs** = minstens één beurs zonder vergunning (MEXC, Bitget, HTX, Poloniex, XT, Bitfinex, Binance). Zie README.md.

## Hoeveel wordt er gecontroleerd? (GEZIEN, stand.jsonl)

Per ronde (mediaan over 52 metingen): 1039 kandidaten (verschil op de ticker groter dan de takerkosten), 120 met het orderboek gecontroleerd, 3 nog nooit gecontroleerd (0%).
Bijna alle kandidaten komen aan de beurt; de aantallen hieronder missen weinig.

## Trechter (GEZIEN, eigen metingen)

| Stap | Alle beurzen | Alleen MiCA-beurzen | Met minstens één grijze beurs |
|---|---|---|---|
| Verschillen met winst op het boek na alle kosten | 3468 | 387 | 3081 |
| ...waarvan opnemen of storten dicht | 634 | 56 | 578 |
| ...waarvan status onbekend (beurs geeft het niet openbaar) | 1920 | 172 | 1748 |
| Opnemen en storten open | 914 | 159 | 755 |
| ...en geen netwerk dat aan beide kanten open is: valt af | 11 | 0 | 11 |
| ...en opnamekosten onbekend: valt af | 0 | 0 | 0 |
| ...en minstens €100,00 op het boek | 286 | 123 | 163 |
| ...en minstens 2 minuten blijven staan | 67 | 31 | 36 |
| ...en geen andere munt met dezelfde naam | 64 | 30 | 34 |
|    ...waarvan contractadres bekend en gelijk | 5 | 1 | 4 |
|    ...waarvan contractadres onbekend (telt mee, kan een andere munt zijn) | 59 | 29 | 30 |
|    ...waarvan netwerk gekoppeld en open | 32 | 6 | 26 |
|    ...waarvan netwerk niet te koppelen (telt mee) | 32 | 24 | 8 |
| **Echte kansen** (zelfde munt overlappend in de tijd samengevoegd, beste beurspaar telt) | 52 | 30 | 25 |
| Ter vergelijking: zelfde eisen, maar opnamestatus onbekend (niet meegeteld) | 127 | 30 | 109 |

## Echte kansen per dag (GEZIEN)

| Dag | Echt, alleen MiCA | Echt, met grijs | Mediane winst per kans bij €500 (MiCA / grijs) | Mediane duur |
|---|---|---|---|---|
| 2026-11-19 | 27 | 25 | €0,93 / €0,67 | 4.2 min |
| Totaal | 27 | 25 | €0,93 / €0,67 | 4.2 min |

## Beste munten (GEZIEN)

| | Soort | Kansen | Som winst bij €500 per kans |
|---|---|---|---|
| MERL-EUR | vergund | 3 | €13,52 |
| VERONA-USDT | grijs | 4 | €10,44 |
| DYM-EUR | vergund | 13 | €8,49 |
| LUNC-USDT | grijs | 3 | €5,53 |
| WAN-USDT | grijs | 2 | €4,87 |
| GMT-EUR | vergund | 3 | €4,75 |
| LUNA-EUR | vergund | 3 | €4,33 |
| CBK-USDT | grijs | 3 | €4,13 |
| USTC-USDT | vergund | 3 | €2,25 |
| LUNA-USDT | grijs | 1 | €2,09 |

## Beste beursparen (kopen op > verkopen op) (GEZIEN)

| | Soort | Kansen | Som winst bij €500 per kans |
|---|---|---|---|
| bitvavo > kraken | vergund | 23 | €30,81 |
| bitget > gate | grijs | 3 | €9,96 |
| kucoin > htx | grijs | 4 | €5,87 |
| bitget > htx | grijs | 5 | €3,98 |
| bitget > xt | grijs | 2 | €3,96 |
| xt > htx | grijs | 1 | €3,52 |
| htx > xt | grijs | 1 | €3,27 |
| kucoin > gate | vergund | 3 | €2,25 |
| bitget > kucoin | grijs | 3 | €2,19 |
| poloniex > htx | grijs | 1 | €1,20 |

Beurzen die het vaakst meedoen (koop of verkoop): bitvavo 23, kraken 23, htx (grijs) 15, bitget (grijs) 15, kucoin 14, gate 9, xt (grijs) 4, poloniex (grijs) 1 (GEZIEN).

## Hoeveel kansen blijven staan terwijl je geld schuift? (GEZIEN, duur uit eigen metingen)

Wie geen voorraad op beide beurzen heeft, moet kopen, de munt opnemen, wachten tot hij binnen is en dan verkopen. Hoe lang dat duurt verschilt per munt en netwerk: een paar minuten (snelle ketens) tot een uur of meer (Bitcoin, beurzen die opnames met de hand keuren) (GOK, niet per munt gemeten).

| Overmaaktijd | Alle beurzen | Alleen MiCA-beurzen | Met minstens één grijze beurs |
|---|---|---|---|
| 5 min | 22 van 52 (42%) | 10 van 30 (33%) | 14 van 25 (56%) |
| 10 min | 8 van 52 (15%) | 4 van 30 (13%) | 5 van 25 (20%) |
| 30 min | 3 van 52 (6%) | 2 van 30 (7%) | 1 van 25 (4%) |
| 60 min | 2 van 52 (4%) | 2 van 30 (7%) | 0 van 25 (0%) |

## Wat zou het opleveren over 3 maanden? (GOK, doorgetrokken uit de metingen)

Gemeten over ±4.3 uur (GEZIEN), doorgetrokken naar 90 dagen (GOK: aanname dat de week die we maten gewoon is).

| Beurzen | Inleg | Model | Kansen per uur | Per kans (mediaan) | 3 maanden |
|---|---|---|---|---|---|
| Alleen MiCA | €2.000,00 | bovengrens: elke kans, geld overal tegelijk | 6.92 | €1,13 | €16.899,75 |
| Alleen MiCA | €2.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 5.31 | €1,37 | €22.856,09 |
| Alleen MiCA | €5.000,00 | bovengrens: elke kans, geld overal tegelijk | 6.92 | €1,35 | €20.260,42 |
| Alleen MiCA | €5.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 5.31 | €1,80 | €28.181,26 |
| Alle (met grijs) | €2.000,00 | bovengrens: elke kans, geld overal tegelijk | 12.00 | €0,97 | €25.174,48 |
| Alle (met grijs) | €2.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 5.31 | €1,37 | €22.856,09 |
| Alle (met grijs) | €5.000,00 | bovengrens: elke kans, geld overal tegelijk | 12.00 | €1,09 | €28.375,40 |
| Alle (met grijs) | €5.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 5.31 | €1,80 | €28.181,26 |

Bovengrens: elke kans met de helft van de inleg aan elke kant, alsof het geld op alle beurzen tegelijk staat (kan in het echt niet). Beste beurspaar: het paar is **achteraf** gekozen uit de metingen (vooraf kiezen levert minder op), en het model neemt aan dat je van elke munt al voorraad op de verkoopbeurs hebt.

Waarom dit te rooskleurig is (GOK): elke kans wordt maar één keer geteld met het mediane boek, maar andere bots pakken hem ook; de munt die je als voorraad aanhoudt kan dalen; na een paar kansen moet de voorraad terug (opnamekosten en tijd); minimale opname- en ordergroottes tellen niet mee; en een kans die we 2 minuten zagen staan, staat er niet per se nog als jouw order binnenkomt. Waarom het te somber kan zijn: niet alle kandidaten zijn gecontroleerd, en met voorraad op beide beurzen kun je dezelfde kans vaker pakken als het boek zich aanvult; dat telt hier niet mee.

## Over de meting

- Opnamekosten bij de echte kansen: 18 van een netwerk dat aan beide kanten open is, 30 van de beurs zelf (laagste open netwerk), 4 geschat uit wat andere beurzen voor die munt vragen (GOK). Onbekende opnamekosten tellen niet als echte kans.
- Netwerk: KuCoin, Gate, Bitget, HTX, XT, Bitstamp, Bitvavo en Poloniex geven hun netwerken per munt. Als beide beurzen dat doen en de namen te koppelen zijn, moet er een netwerk zijn dat aan beide kanten open is. Anders is het netwerk "niet te koppelen" en telt de kans mee (staat apart in de trechter).
- De duur is gemeten in stappen van ±20 seconden; een kans kan een paar rondes eerder begonnen zijn dan we zagen.
- Takerkosten: uit de API waar die ze per paar geeft, anders het standaardtarief uit de README (deels GOK).
- Laatste run: 15 beurzen antwoordden, 2293 munt-quote-paren op minstens twee beurzen (GEZIEN).
