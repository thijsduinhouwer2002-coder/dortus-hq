# Rapport koersverschil-scanner

Gemaakt 2026-11-20 17:23 UTC uit 20 runs, samen ±31.6 uur gemeten (GEZIEN).
Echte kans = winst na alle kosten (opnamekosten bekend), opnemen en storten open (en een netwerk dat aan beide kanten open is, als de beurzen dat geven), minstens €100,00 op het boek, minstens 2 minuten blijven staan, geen andere munt met dezelfde naam.
**Vergund** = beide beurzen hebben een MiCA-vergunning (ESMA-register), vaak via een EU-dochter die minder munten kan hebben dan de wereldwijde API die we meten (GOK). **Grijs** = minstens één beurs zonder vergunning (MEXC, Bitget, HTX, Poloniex, XT, Bitfinex, Binance). Zie README.md.
**Kraken-tarief:** Kraken rekent 0,80% taker op munt tegen EUR, USD, USDT of USDC (GEZIEN, kraken.com/pro/fees, laagste trede); de scanner rekende tot 19 nov met 0,40%. 399 opgeslagen kansen met Kraken uit die runs zijn hier **opnieuw doorgerekend met 0,80%** (GOK-benadering: 0,40% van de inzet aan de Kraken-kant extra op elk gemeten punt van het boek; het boek zelf is niet bewaard). 233 houden daarna nog winst op het boek. Dat ze met hogere kosten ook korter bleven staan, telt niet mee (dus eerder te gunstig).

## Hoeveel wordt er gecontroleerd? (GEZIEN, stand.jsonl)

Per ronde (mediaan over 379 metingen): 1127 kandidaten (verschil op de ticker groter dan de takerkosten), 120 met het orderboek gecontroleerd, 2 nog nooit gecontroleerd (0%).
Bijna alle kandidaten komen aan de beurt; de aantallen hieronder missen weinig.

## Trechter (GEZIEN, eigen metingen)

| Stap | Alle beurzen | Alleen MiCA-beurzen | Met minstens één grijze beurs |
|---|---|---|---|
| Verschillen met winst op het boek na alle kosten | 27786 | 4204 | 23582 |
| ...waarvan opnemen of storten dicht | 5993 | 638 | 5355 |
| ...waarvan status onbekend (beurs geeft het niet openbaar) | 16327 | 2972 | 13355 |
| Opnemen en storten open | 5466 | 594 | 4872 |
| ...en geen netwerk dat aan beide kanten open is: valt af | 141 | 8 | 133 |
| ...en opnamekosten onbekend: valt af | 0 | 0 | 0 |
| ...en minstens €100,00 op het boek | 1627 | 326 | 1301 |
| ...en minstens 2 minuten blijven staan | 459 | 135 | 324 |
| ...en geen andere munt met dezelfde naam | 422 | 119 | 303 |
|    ...waarvan contractadres bekend en gelijk | 55 | 22 | 33 |
|    ...waarvan contractadres onbekend (telt mee, kan een andere munt zijn) | 367 | 97 | 270 |
|    ...waarvan netwerk gekoppeld en open | 275 | 55 | 220 |
|    ...waarvan netwerk niet te koppelen (telt mee) | 147 | 64 | 83 |
| **Echte kansen** (zelfde munt overlappend in de tijd samengevoegd, beste beurspaar telt) | 267 | 118 | 182 |
| Ter vergelijking: zelfde eisen, maar opnamestatus onbekend (niet meegeteld) | 924 | 232 | 778 |

## Echte kansen per dag (GEZIEN)

| Dag | Echt, alleen MiCA | Echt, met grijs | Mediane winst per kans bij €500 (MiCA / grijs) | Mediane duur |
|---|---|---|---|---|
| 2026-11-19 | 49 | 86 | €2,00 / €1,21 | 5.3 min |
| 2026-11-20 | 39 | 93 | €0,74 / €1,10 | 6.7 min |
| Totaal | 88 | 179 | €1,55 / €1,17 | 6.0 min |

## Beste munten (GEZIEN)

| | Soort | Kansen | Som winst bij €500 per kans |
|---|---|---|---|
| MERL-EUR | vergund | 18 | €234,30 |
| LUNC-USDT | grijs | 13 | €67,33 |
| KERNEL-EUR | vergund | 1 | €47,33 |
| USTC-USDT | grijs en vergund | 11 | €42,13 |
| MEME-USDT | grijs | 1 | €37,90 |
| KYO-USDT | vergund | 4 | €24,15 |
| SKY-USD | vergund | 2 | €21,52 |
| LAT-USDT | grijs | 3 | €17,59 |
| GMT-EUR | vergund | 21 | €17,57 |
| YB-USDT | grijs | 2 | €17,52 |

## Beste beursparen (kopen op > verkopen op) (GEZIEN)

| | Soort | Kansen | Som winst bij €500 per kans |
|---|---|---|---|
| bitvavo > kraken | vergund | 56 | €327,52 |
| bitget > htx | grijs | 43 | €106,80 |
| kucoin > htx | grijs | 24 | €57,34 |
| gate > kucoin | vergund | 20 | €54,23 |
| kucoin > bitget | grijs | 18 | €45,64 |
| bitget > xt | grijs | 12 | €43,27 |
| bitget > gate | grijs | 10 | €30,26 |
| gate > xt | grijs | 3 | €23,21 |
| bitstamp > kraken | vergund | 2 | €21,52 |
| htx > xt | grijs | 3 | €19,34 |

Beurzen die het vaakst meedoen (koop of verkoop): bitget (grijs) 115, kucoin 102, htx (grijs) 92, kraken 68, gate 59, bitvavo 56, xt (grijs) 29, poloniex (grijs) 11 (GEZIEN).

## Hoeveel kansen blijven staan terwijl je geld schuift? (GEZIEN, duur uit eigen metingen)

Wie geen voorraad op beide beurzen heeft, moet kopen, de munt opnemen, wachten tot hij binnen is en dan verkopen. Hoe lang dat duurt verschilt per munt en netwerk: een paar minuten (snelle ketens) tot een uur of meer (Bitcoin, beurzen die opnames met de hand keuren) (GOK, niet per munt gemeten).

| Overmaaktijd | Alle beurzen | Alleen MiCA-beurzen | Met minstens één grijze beurs |
|---|---|---|---|
| 5 min | 159 van 267 (60%) | 69 van 118 (58%) | 108 van 182 (59%) |
| 10 min | 96 van 267 (36%) | 45 van 118 (38%) | 64 van 182 (35%) |
| 30 min | 53 van 267 (20%) | 26 van 118 (22%) | 36 van 182 (20%) |
| 60 min | 26 van 267 (10%) | 16 van 118 (14%) | 17 van 182 (9%) |

## Wat zou het opleveren over 3 maanden? (GOK, doorgetrokken uit de metingen)

Gemeten over ±31.6 uur (GEZIEN), doorgetrokken naar 90 dagen (GOK: aanname dat de week die we maten gewoon is).

| Beurzen | Inleg | Model | Kansen per uur | Per kans (mediaan) | 3 maanden |
|---|---|---|---|---|---|
| Alleen MiCA | €2.000,00 | bovengrens: elke kans, geld overal tegelijk | 3.74 | €1,76 | €14.227,05 |
| Alleen MiCA | €2.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 1.77 | €2,73 | €37.966,64 |
| Alleen MiCA | €5.000,00 | bovengrens: elke kans, geld overal tegelijk | 3.74 | €2,55 | €20.541,66 |
| Alleen MiCA | €5.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 1.77 | €3,21 | €56.055,54 |
| Alle (met grijs) | €2.000,00 | bovengrens: elke kans, geld overal tegelijk | 8.45 | €1,51 | €27.619,50 |
| Alle (met grijs) | €2.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 1.77 | €2,73 | €37.966,64 |
| Alle (met grijs) | €5.000,00 | bovengrens: elke kans, geld overal tegelijk | 8.45 | €1,78 | €32.465,61 |
| Alle (met grijs) | €5.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 1.77 | €3,21 | €56.055,54 |

Bovengrens: elke kans met de helft van de inleg aan elke kant, alsof het geld op alle beurzen tegelijk staat (kan in het echt niet). Beste beurspaar: het paar is **achteraf** gekozen uit de metingen (vooraf kiezen levert minder op), en het model neemt aan dat je van elke munt al voorraad op de verkoopbeurs hebt.

Waarom dit te rooskleurig is (GOK): elke kans wordt maar één keer geteld met het mediane boek, maar andere bots pakken hem ook; de munt die je als voorraad aanhoudt kan dalen; na een paar kansen moet de voorraad terug (opnamekosten en tijd); minimale opname- en ordergroottes tellen niet mee; en een kans die we 2 minuten zagen staan, staat er niet per se nog als jouw order binnenkomt. Waarom het te somber kan zijn: niet alle kandidaten zijn gecontroleerd, en met voorraad op beide beurzen kun je dezelfde kans vaker pakken als het boek zich aanvult; dat telt hier niet mee.

## Wat houd je echt over? Voorraad op twee beurzen (simulatie)

Per beurspaar: geld en munten op beide beurzen, elke echte kans uitgevoerd tegen het boek zoals gemeten (niet meer dan de ruimte op het boek en niet meer dan de voorraad op die beurs), terugschuiven als een kant leeg dreigt te raken (met opnamekosten en tijd onderweg), en het koerseffect van de aangehouden munten apart. Netto = bruto min kosten terugschuiven plus koerseffect. **Gemeten** (GEZIEN): de kansen, het boek en de koersen; **de rest is een rekenmodel** (GOK, aannames onder de tabel). Geen advies.

**Met €150: netto €0,89 per dag op bitstamp - kraken (koerseffect erbovenop €-2,68), €-0,00 per dag op bitstamp - kucoin (koerseffect erbovenop €0,12), €0,38 per dag op bitvavo - kraken (koerseffect erbovenop €-1,63), €0,12 per dag op gate - kucoin (koerseffect erbovenop €0,53), €0,02 per dag op kraken - kucoin (koerseffect erbovenop €0,11) (GOK: netto handel, rekenmodel op ±15.8 uur meting per dag, alleen MiCA).** "Per dag" is hier gemiddeld over 2 gemeten dagen achter elkaar; de eerste begint met een gelijk verdeelde voorraad; aan het eind staat de voorraad scheef, dus een volgende dag levert waarschijnlijk minder op, tenzij kansen de andere kant op hem terugbrengen (GOK).

### Alleen MiCA-beurzen (alle paren met echte kansen)

| Beurspaar | Inleg | Dag | Gemeten | Kansen | Gemist (geen voorraad) | Kleiner door voorraad | Bruto winst | Kosten terugschuiven | **Netto handel (bruto min kosten)** | Rendement handel | Koerseffect voorraad | Netto met koerseffect | Rendement met koerseffect |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| bitstamp - kraken | €100,00 | 2026-11-19 | 14.9 u | 2 | 1 | 1 | €1,18 | €0,00 (0x) | **€1,18** | 1.18% | €0,63 | €1,81 | 1.81% |
| bitstamp - kraken | €100,00 | 2026-11-20 | 16.7 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-4,20 | €-4,20 | -4.20% |
| bitstamp - kraken | €150,00 | 2026-11-19 | 14.9 u | 2 | 1 | 1 | €1,78 | €0,00 (0x) | **€1,78** | 1.18% | €0,94 | €2,72 | 1.81% |
| bitstamp - kraken | €150,00 | 2026-11-20 | 16.7 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-6,30 | €-6,30 | -4.20% |
| bitstamp - kraken | €200,00 | 2026-11-19 | 14.9 u | 2 | 1 | 1 | €2,37 | €0,00 (0x) | **€2,37** | 1.18% | €1,25 | €3,62 | 1.81% |
| bitstamp - kraken | €200,00 | 2026-11-20 | 16.7 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-8,41 | €-8,41 | -4.20% |
| bitstamp - kraken | €2.000,00 | 2026-11-19 | 14.9 u | 2 | 1 | 0 | €11,71 | €0,00 (0x) | **€11,71** | 0.59% | €12,53 | €24,24 | 1.21% |
| bitstamp - kraken | €2.000,00 | 2026-11-20 | 16.7 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-84,05 | €-84,05 | -4.20% |
| bitstamp - kraken | €5.000,00 | 2026-11-19 | 14.9 u | 2 | 1 | 0 | €11,71 | €0,00 (0x) | **€11,71** | 0.23% | €31,33 | €43,04 | 0.86% |
| bitstamp - kraken | €5.000,00 | 2026-11-20 | 16.7 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-210,13 | €-210,13 | -4.20% |
| bitstamp - kucoin | €100,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,14 | €0,14 | 0.14% |
| bitstamp - kucoin | €100,00 | 2026-11-20 | 16.7 u | 1 | 0 | 1 | €0,01 | €0,01 (1x) | **€-0,00** | -0.00% | €0,03 | €0,02 | 0.02% |
| bitstamp - kucoin | €150,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,21 | €0,21 | 0.14% |
| bitstamp - kucoin | €150,00 | 2026-11-20 | 16.7 u | 1 | 0 | 1 | €0,01 | €0,01 (1x) | **€-0,00** | -0.00% | €0,04 | €0,04 | 0.03% |
| bitstamp - kucoin | €200,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,27 | €0,27 | 0.14% |
| bitstamp - kucoin | €200,00 | 2026-11-20 | 16.7 u | 1 | 0 | 1 | €0,01 | €0,01 (1x) | **€0,00** | 0.00% | €0,05 | €0,06 | 0.03% |
| bitstamp - kucoin | €2.000,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €2,74 | €2,74 | 0.14% |
| bitstamp - kucoin | €2.000,00 | 2026-11-20 | 16.7 u | 1 | 0 | 1 | €0,10 | €1,01 (2x) | **€-0,91** | -0.05% | €0,55 | €-0,36 | -0.02% |
| bitstamp - kucoin | €5.000,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €6,86 | €6,86 | 0.14% |
| bitstamp - kucoin | €5.000,00 | 2026-11-20 | 16.7 u | 1 | 0 | 1 | €0,25 | €1,01 (2x) | **€-0,76** | -0.02% | €1,37 | €0,61 | 0.01% |
| bitvavo - kraken | €100,00 | 2026-11-19 | 14.9 u | 43 | 43 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,62 | €-0,62 | -0.62% |
| bitvavo - kraken | €100,00 | 2026-11-20 | 16.7 u | 13 | 13 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,55 | €-1,55 | -1.55% |
| bitvavo - kraken | €150,00 | 2026-11-19 | 14.9 u | 43 | 43 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,93 | €-0,93 | -0.62% |
| bitvavo - kraken | €150,00 | 2026-11-20 | 16.7 u | 13 | 12 | 1 | €0,76 | €0,00 (0x) | **€0,76** | 0.51% | €-2,33 | €-1,57 | -1.04% |
| bitvavo - kraken | €200,00 | 2026-11-19 | 14.9 u | 43 | 37 | 6 | €0,14 | €0,00 (0x) | **€0,14** | 0.07% | €-1,24 | €-1,10 | -0.55% |
| bitvavo - kraken | €200,00 | 2026-11-20 | 16.7 u | 13 | 12 | 1 | €1,01 | €0,00 (0x) | **€1,01** | 0.51% | €-3,10 | €-2,09 | -1.04% |
| bitvavo - kraken | €2.000,00 | 2026-11-19 | 14.9 u | 43 | 27 | 16 | €11,14 | €6,39 (16x) | **€4,75** | 0.24% | €-12,32 | €-7,57 | -0.38% |
| bitvavo - kraken | €2.000,00 | 2026-11-20 | 16.7 u | 13 | 9 | 4 | €16,20 | €1,64 (3x) | **€14,55** | 0.73% | €-30,56 | €-16,00 | -0.80% |
| bitvavo - kraken | €5.000,00 | 2026-11-19 | 14.9 u | 43 | 22 | 21 | €28,08 | €14,95 (24x) | **€13,12** | 0.26% | €-30,85 | €-17,73 | -0.35% |
| bitvavo - kraken | €5.000,00 | 2026-11-20 | 16.7 u | 13 | 2 | 11 | €42,61 | €10,66 (12x) | **€31,96** | 0.64% | €-75,81 | €-43,86 | -0.88% |
| gate - kucoin | €100,00 | 2026-11-19 | 14.9 u | 25 | 25 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,65 | €-0,65 | -0.65% |
| gate - kucoin | €100,00 | 2026-11-20 | 16.7 u | 31 | 30 | 1 | €0,07 | €0,00 (1x) | **€0,07** | 0.07% | €1,35 | €1,42 | 1.42% |
| gate - kucoin | €150,00 | 2026-11-19 | 14.9 u | 25 | 25 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,97 | €-0,97 | -0.65% |
| gate - kucoin | €150,00 | 2026-11-20 | 16.7 u | 31 | 28 | 3 | €0,24 | €0,00 (1x) | **€0,24** | 0.16% | €2,03 | €2,27 | 1.51% |
| gate - kucoin | €200,00 | 2026-11-19 | 14.9 u | 25 | 19 | 6 | €0,15 | €0,00 (0x) | **€0,15** | 0.08% | €-1,29 | €-1,14 | -0.57% |
| gate - kucoin | €200,00 | 2026-11-20 | 16.7 u | 31 | 22 | 9 | €0,67 | €0,02 (2x) | **€0,65** | 0.33% | €2,70 | €3,36 | 1.68% |
| gate - kucoin | €2.000,00 | 2026-11-19 | 14.9 u | 25 | 10 | 15 | €2,63 | €2,18 (12x) | **€0,45** | 0.02% | €-12,92 | €-12,47 | -0.62% |
| gate - kucoin | €2.000,00 | 2026-11-20 | 16.7 u | 31 | 9 | 22 | €10,59 | €1,92 (14x) | **€8,67** | 0.43% | €27,16 | €35,84 | 1.79% |
| gate - kucoin | €5.000,00 | 2026-11-19 | 14.9 u | 25 | 6 | 19 | €10,16 | €4,84 (19x) | **€5,32** | 0.11% | €-32,31 | €-26,98 | -0.54% |
| gate - kucoin | €5.000,00 | 2026-11-20 | 16.7 u | 31 | 5 | 26 | €27,78 | €6,68 (24x) | **€21,11** | 0.42% | €68,17 | €89,28 | 1.79% |
| kraken - kucoin | €100,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,11 | €0,11 | 0.11% |
| kraken - kucoin | €100,00 | 2026-11-20 | 16.7 u | 4 | 2 | 2 | €0,03 | €0,01 (1x) | **€0,02** | 0.02% | €0,04 | €0,06 | 0.06% |
| kraken - kucoin | €150,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,16 | €0,16 | 0.11% |
| kraken - kucoin | €150,00 | 2026-11-20 | 16.7 u | 4 | 2 | 2 | €0,05 | €0,01 (1x) | **€0,04** | 0.02% | €0,06 | €0,10 | 0.07% |
| kraken - kucoin | €200,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,22 | €0,22 | 0.11% |
| kraken - kucoin | €200,00 | 2026-11-20 | 16.7 u | 4 | 2 | 2 | €0,06 | €0,24 (2x) | **€-0,18** | -0.09% | €0,08 | €-0,10 | -0.05% |
| kraken - kucoin | €2.000,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €2,19 | €2,19 | 0.11% |
| kraken - kucoin | €2.000,00 | 2026-11-20 | 16.7 u | 4 | 2 | 2 | €0,61 | €1,24 (3x) | **€-0,63** | -0.03% | €0,82 | €0,19 | 0.01% |
| kraken - kucoin | €5.000,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €5,49 | €5,49 | 0.11% |
| kraken - kucoin | €5.000,00 | 2026-11-20 | 16.7 u | 4 | 2 | 2 | €1,53 | €1,24 (3x) | **€0,29** | 0.01% | €2,06 | €2,34 | 0.05% |

- bitstamp - kraken, €100,00: munten SKY; bruto zonder voorraadgrens zou €22,30 zijn, met voorraad €1,18 (GEZIEN boek, GOK model).
- bitstamp - kraken, €150,00: munten SKY; bruto zonder voorraadgrens zou €21,71 zijn, met voorraad €1,78 (GEZIEN boek, GOK model).
- bitstamp - kraken, €200,00: munten SKY; bruto zonder voorraadgrens zou €21,12 zijn, met voorraad €2,37 (GEZIEN boek, GOK model).
- bitstamp - kraken, €2.000,00: munten SKY; bruto zonder voorraadgrens zou €11,71 zijn, met voorraad €11,71 (GEZIEN boek, GOK model).
- bitstamp - kraken, €5.000,00: munten SKY; bruto zonder voorraadgrens zou €11,71 zijn, met voorraad €11,71 (GEZIEN boek, GOK model).
- bitstamp - kucoin, €100,00: munten USDT; bruto zonder voorraadgrens zou €1,20 zijn, met voorraad €0,01 (GEZIEN boek, GOK model).
- bitstamp - kucoin, €150,00: munten USDT; bruto zonder voorraadgrens zou €1,20 zijn, met voorraad €0,01 (GEZIEN boek, GOK model).
- bitstamp - kucoin, €200,00: munten USDT; bruto zonder voorraadgrens zou €1,20 zijn, met voorraad €0,01 (GEZIEN boek, GOK model).
- bitstamp - kucoin, €2.000,00: munten USDT; bruto zonder voorraadgrens zou €1,20 zijn, met voorraad €0,10 (GEZIEN boek, GOK model).
- bitstamp - kucoin, €5.000,00: munten USDT; bruto zonder voorraadgrens zou €1,20 zijn, met voorraad €0,25 (GEZIEN boek, GOK model).
- bitvavo - kraken, €100,00: munten AVA, CVX, DYM, GMT, KERNEL, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €1.115,19 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitvavo - kraken, €150,00: munten AVA, CVX, DYM, GMT, KERNEL, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €1.115,19 zijn, met voorraad €0,76 (GEZIEN boek, GOK model).
- bitvavo - kraken, €200,00: munten AVA, CVX, DYM, GMT, KERNEL, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €1.114,78 zijn, met voorraad €1,15 (GEZIEN boek, GOK model).
- bitvavo - kraken, €2.000,00: munten AVA, CVX, DYM, GMT, KERNEL, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €1.093,02 zijn, met voorraad €27,33 (GEZIEN boek, GOK model).
- bitvavo - kraken, €5.000,00: munten AVA, CVX, DYM, GMT, KERNEL, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €1.060,60 zijn, met voorraad €70,69 (GEZIEN boek, GOK model).
- gate - kucoin, €100,00: munten ALKIMI, AVAIL, CCD, CHR, CYBER, EDEN, ERG, FTT, IKA, IR, KYO, LUNC, NAKA, NIM, OVR, RARI, USTC, VERONA; bruto zonder voorraadgrens zou €199,93 zijn, met voorraad €0,07 (GEZIEN boek, GOK model).
- gate - kucoin, €150,00: munten ALKIMI, AVAIL, CCD, CHR, CYBER, EDEN, ERG, FTT, IKA, IR, KYO, LUNC, NAKA, NIM, OVR, RARI, USTC, VERONA; bruto zonder voorraadgrens zou €199,90 zijn, met voorraad €0,24 (GEZIEN boek, GOK model).
- gate - kucoin, €200,00: munten ALKIMI, AVAIL, CCD, CHR, CYBER, EDEN, ERG, FTT, IKA, IR, KYO, LUNC, NAKA, NIM, OVR, RARI, USTC, VERONA; bruto zonder voorraadgrens zou €199,71 zijn, met voorraad €0,82 (GEZIEN boek, GOK model).
- gate - kucoin, €2.000,00: munten ALKIMI, AVAIL, CCD, CHR, CYBER, EDEN, ERG, FTT, IKA, IR, KYO, LUNC, NAKA, NIM, OVR, RARI, USTC, VERONA; bruto zonder voorraadgrens zou €197,75 zijn, met voorraad €13,22 (GEZIEN boek, GOK model).
- gate - kucoin, €5.000,00: munten ALKIMI, AVAIL, CCD, CHR, CYBER, EDEN, ERG, FTT, IKA, IR, KYO, LUNC, NAKA, NIM, OVR, RARI, USTC, VERONA; bruto zonder voorraadgrens zou €192,31 zijn, met voorraad €37,95 (GEZIEN boek, GOK model).
- kraken - kucoin, €100,00: munten USDC, USDT; bruto zonder voorraadgrens zou €26,96 zijn, met voorraad €0,03 (GEZIEN boek, GOK model).
- kraken - kucoin, €150,00: munten USDC, USDT; bruto zonder voorraadgrens zou €26,95 zijn, met voorraad €0,05 (GEZIEN boek, GOK model).
- kraken - kucoin, €200,00: munten USDC, USDT; bruto zonder voorraadgrens zou €26,94 zijn, met voorraad €0,06 (GEZIEN boek, GOK model).
- kraken - kucoin, €2.000,00: munten USDC, USDT; bruto zonder voorraadgrens zou €26,66 zijn, met voorraad €0,61 (GEZIEN boek, GOK model).
- kraken - kucoin, €5.000,00: munten USDC, USDT; bruto zonder voorraadgrens zou €26,20 zijn, met voorraad €1,53 (GEZIEN boek, GOK model).

### Met minstens één grijze beurs (de 5 paren met de meeste bruto winst)

| Beurspaar | Inleg | Dag | Gemeten | Kansen | Gemist (geen voorraad) | Kleiner door voorraad | Bruto winst | Kosten terugschuiven | **Netto handel (bruto min kosten)** | Rendement handel | Koerseffect voorraad | Netto met koerseffect | Rendement met koerseffect |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| htx - xt | €100,00 | 2026-11-19 | 14.9 u | 18 | 18 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,69 | €-0,69 | -0.69% |
| htx - xt | €100,00 | 2026-11-20 | 16.7 u | 12 | 12 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,19 | €-3,19 | -3.19% |
| htx - xt | €150,00 | 2026-11-19 | 14.9 u | 18 | 18 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,03 | €-1,03 | -0.69% |
| htx - xt | €150,00 | 2026-11-20 | 16.7 u | 12 | 12 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-4,79 | €-4,79 | -3.19% |
| htx - xt | €200,00 | 2026-11-19 | 14.9 u | 18 | 18 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,38 | €-1,38 | -0.69% |
| htx - xt | €200,00 | 2026-11-20 | 16.7 u | 12 | 12 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-6,38 | €-6,38 | -3.19% |
| htx - xt | €2.000,00 | 2026-11-19 | 14.9 u | 18 | 5 | 13 | €6,47 | €4,36 (11x) | **€2,11** | 0.11% | €-13,84 | €-11,73 | -0.59% |
| htx - xt | €2.000,00 | 2026-11-20 | 16.7 u | 12 | 1 | 11 | €12,78 | €2,95 (7x) | **€9,82** | 0.49% | €-63,16 | €-53,34 | -2.67% |
| htx - xt | €5.000,00 | 2026-11-19 | 14.9 u | 18 | 5 | 12 | €15,21 | €6,19 (13x) | **€9,02** | 0.18% | €-34,52 | €-25,50 | -0.51% |
| htx - xt | €5.000,00 | 2026-11-20 | 16.7 u | 12 | 0 | 12 | €31,87 | €6,57 (11x) | **€25,30** | 0.51% | €-158,67 | €-133,37 | -2.67% |
| gate - htx | €100,00 | 2026-11-19 | 14.9 u | 19 | 19 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,89 | €-0,89 | -0.89% |
| gate - htx | €100,00 | 2026-11-20 | 16.7 u | 23 | 23 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,75 | €-3,75 | -3.75% |
| gate - htx | €150,00 | 2026-11-19 | 14.9 u | 19 | 19 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,34 | €-1,34 | -0.89% |
| gate - htx | €150,00 | 2026-11-20 | 16.7 u | 23 | 23 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-5,63 | €-5,63 | -3.75% |
| gate - htx | €200,00 | 2026-11-19 | 14.9 u | 19 | 19 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,79 | €-1,79 | -0.89% |
| gate - htx | €200,00 | 2026-11-20 | 16.7 u | 23 | 23 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-7,51 | €-7,51 | -3.75% |
| gate - htx | €2.000,00 | 2026-11-19 | 14.9 u | 19 | 14 | 5 | €1,30 | €0,46 (2x) | **€0,83** | 0.04% | €-17,85 | €-17,02 | -0.85% |
| gate - htx | €2.000,00 | 2026-11-20 | 16.7 u | 23 | 8 | 15 | €8,23 | €1,46 (8x) | **€6,77** | 0.34% | €-75,02 | €-68,25 | -3.41% |
| gate - htx | €5.000,00 | 2026-11-19 | 14.9 u | 19 | 6 | 13 | €10,80 | €4,50 (12x) | **€6,30** | 0.13% | €-44,66 | €-38,36 | -0.77% |
| gate - htx | €5.000,00 | 2026-11-20 | 16.7 u | 23 | 3 | 20 | €25,67 | €4,66 (16x) | **€21,01** | 0.42% | €-186,98 | €-165,97 | -3.32% |
| kucoin - xt | €100,00 | 2026-11-19 | 14.9 u | 13 | 13 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,06 | €-0,06 | -0.06% |
| kucoin - xt | €100,00 | 2026-11-20 | 16.7 u | 4 | 4 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,97 | €-2,97 | -2.97% |
| kucoin - xt | €150,00 | 2026-11-19 | 14.9 u | 13 | 13 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,09 | €-0,09 | -0.06% |
| kucoin - xt | €150,00 | 2026-11-20 | 16.7 u | 4 | 4 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-4,46 | €-4,46 | -2.97% |
| kucoin - xt | €200,00 | 2026-11-19 | 14.9 u | 13 | 11 | 2 | €0,17 | €0,00 (0x) | **€0,17** | 0.09% | €-0,11 | €0,06 | 0.03% |
| kucoin - xt | €200,00 | 2026-11-20 | 16.7 u | 4 | 3 | 1 | €0,18 | €0,00 (0x) | **€0,18** | 0.09% | €-5,95 | €-5,77 | -2.89% |
| kucoin - xt | €2.000,00 | 2026-11-19 | 14.9 u | 13 | 3 | 10 | €11,08 | €5,50 (11x) | **€5,58** | 0.28% | €-1,12 | €4,46 | 0.22% |
| kucoin - xt | €2.000,00 | 2026-11-20 | 16.7 u | 4 | 0 | 4 | €4,66 | €2,41 (4x) | **€2,25** | 0.11% | €-59,04 | €-56,79 | -2.84% |
| kucoin - xt | €5.000,00 | 2026-11-19 | 14.9 u | 13 | 3 | 9 | €23,53 | €5,50 (11x) | **€18,04** | 0.36% | €-2,83 | €15,21 | 0.30% |
| kucoin - xt | €5.000,00 | 2026-11-20 | 16.7 u | 4 | 0 | 4 | €13,61 | €3,46 (5x) | **€10,16** | 0.20% | €-148,23 | €-138,07 | -2.76% |
| htx - kucoin | €100,00 | 2026-11-19 | 14.9 u | 16 | 16 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,18 | €-2,18 | -2.18% |
| htx - kucoin | €100,00 | 2026-11-20 | 16.7 u | 33 | 33 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-4,03 | €-4,03 | -4.03% |
| htx - kucoin | €150,00 | 2026-11-19 | 14.9 u | 16 | 16 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,27 | €-3,27 | -2.18% |
| htx - kucoin | €150,00 | 2026-11-20 | 16.7 u | 33 | 33 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-6,04 | €-6,04 | -4.03% |
| htx - kucoin | €200,00 | 2026-11-19 | 14.9 u | 16 | 16 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-4,36 | €-4,36 | -2.18% |
| htx - kucoin | €200,00 | 2026-11-20 | 16.7 u | 33 | 33 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-8,05 | €-8,05 | -4.03% |
| htx - kucoin | €2.000,00 | 2026-11-19 | 14.9 u | 16 | 9 | 7 | €1,46 | €0,00 (1x) | **€1,46** | 0.07% | €-43,59 | €-42,13 | -2.11% |
| htx - kucoin | €2.000,00 | 2026-11-20 | 16.7 u | 33 | 17 | 16 | €7,88 | €0,00 (1x) | **€7,88** | 0.39% | €-80,51 | €-72,63 | -3.63% |
| htx - kucoin | €5.000,00 | 2026-11-19 | 14.9 u | 16 | 3 | 13 | €7,82 | €3,83 (12x) | **€3,99** | 0.08% | €-108,89 | €-104,90 | -2.10% |
| htx - kucoin | €5.000,00 | 2026-11-20 | 16.7 u | 33 | 8 | 25 | €21,94 | €5,14 (17x) | **€16,81** | 0.34% | €-200,76 | €-183,95 | -3.68% |
| bitget - xt | €100,00 | 2026-11-19 | 14.9 u | 13 | 13 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €2,07 | €2,07 | 2.07% |
| bitget - xt | €100,00 | 2026-11-20 | 16.7 u | 5 | 5 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-4,71 | €-4,71 | -4.71% |
| bitget - xt | €150,00 | 2026-11-19 | 14.9 u | 13 | 13 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €3,11 | €3,11 | 2.07% |
| bitget - xt | €150,00 | 2026-11-20 | 16.7 u | 5 | 5 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-7,07 | €-7,07 | -4.71% |
| bitget - xt | €200,00 | 2026-11-19 | 14.9 u | 13 | 9 | 4 | €0,50 | €0,01 (3x) | **€0,50** | 0.25% | €4,15 | €4,64 | 2.32% |
| bitget - xt | €200,00 | 2026-11-20 | 16.7 u | 5 | 5 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-9,42 | €-9,42 | -4.71% |
| bitget - xt | €2.000,00 | 2026-11-19 | 14.9 u | 13 | 4 | 9 | €9,96 | €1,96 (11x) | **€8,00** | 0.40% | €41,46 | €49,46 | 2.47% |
| bitget - xt | €2.000,00 | 2026-11-20 | 16.7 u | 5 | 0 | 5 | €5,94 | €2,06 (6x) | **€3,88** | 0.19% | €-94,20 | €-90,31 | -4.52% |
| bitget - xt | €5.000,00 | 2026-11-19 | 14.9 u | 13 | 4 | 8 | €19,47 | €1,85 (10x) | **€17,62** | 0.35% | €103,65 | €121,27 | 2.43% |
| bitget - xt | €5.000,00 | 2026-11-20 | 16.7 u | 5 | 0 | 5 | €12,98 | €2,06 (6x) | **€10,93** | 0.22% | €-235,61 | €-224,68 | -4.49% |

- htx - xt, €100,00: munten BSV, CARV, CBK, HBAR, LUNC, MEME, SEI, XCH, XDC, XMR; bruto zonder voorraadgrens zou €209,28 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - xt, €150,00: munten BSV, CARV, CBK, HBAR, LUNC, MEME, SEI, XCH, XDC, XMR; bruto zonder voorraadgrens zou €209,28 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - xt, €200,00: munten BSV, CARV, CBK, HBAR, LUNC, MEME, SEI, XCH, XDC, XMR; bruto zonder voorraadgrens zou €209,28 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - xt, €2.000,00: munten BSV, CARV, CBK, HBAR, LUNC, MEME, SEI, XCH, XDC, XMR; bruto zonder voorraadgrens zou €207,68 zijn, met voorraad €19,25 (GEZIEN boek, GOK model).
- htx - xt, €5.000,00: munten BSV, CARV, CBK, HBAR, LUNC, MEME, SEI, XCH, XDC, XMR; bruto zonder voorraadgrens zou €205,63 zijn, met voorraad €47,07 (GEZIEN boek, GOK model).
- gate - htx, €100,00: munten BRISE, BSV, CBK, CRTS, ENJ, ENS, KAS, LAT, LUNC, MEME, MOVR, SEI, SSV, WARD, WLD, XCN; bruto zonder voorraadgrens zou €173,93 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- gate - htx, €150,00: munten BRISE, BSV, CBK, CRTS, ENJ, ENS, KAS, LAT, LUNC, MEME, MOVR, SEI, SSV, WARD, WLD, XCN; bruto zonder voorraadgrens zou €173,93 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- gate - htx, €200,00: munten BRISE, BSV, CBK, CRTS, ENJ, ENS, KAS, LAT, LUNC, MEME, MOVR, SEI, SSV, WARD, WLD, XCN; bruto zonder voorraadgrens zou €173,93 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- gate - htx, €2.000,00: munten BRISE, BSV, CBK, CRTS, ENJ, ENS, KAS, LAT, LUNC, MEME, MOVR, SEI, SSV, WARD, WLD, XCN; bruto zonder voorraadgrens zou €173,31 zijn, met voorraad €9,52 (GEZIEN boek, GOK model).
- gate - htx, €5.000,00: munten BRISE, BSV, CBK, CRTS, ENJ, ENS, KAS, LAT, LUNC, MEME, MOVR, SEI, SSV, WARD, WLD, XCN; bruto zonder voorraadgrens zou €168,58 zijn, met voorraad €36,47 (GEZIEN boek, GOK model).
- kucoin - xt, €100,00: munten DAG, ENSO, FIGHT, LUNC, XMR; bruto zonder voorraadgrens zou €677,33 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- kucoin - xt, €150,00: munten DAG, ENSO, FIGHT, LUNC, XMR; bruto zonder voorraadgrens zou €677,33 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- kucoin - xt, €200,00: munten DAG, ENSO, FIGHT, LUNC, XMR; bruto zonder voorraadgrens zou €677,33 zijn, met voorraad €0,35 (GEZIEN boek, GOK model).
- kucoin - xt, €2.000,00: munten DAG, ENSO, FIGHT, LUNC, XMR; bruto zonder voorraadgrens zou €673,85 zijn, met voorraad €15,74 (GEZIEN boek, GOK model).
- kucoin - xt, €5.000,00: munten DAG, ENSO, FIGHT, LUNC, XMR; bruto zonder voorraadgrens zou €668,85 zijn, met voorraad €37,15 (GEZIEN boek, GOK model).
- htx - kucoin, €100,00: munten ANIME, BSV, CFX, CHIP, ENJ, ENS, FET, JASMY, LAT, LUNC, MEME, MOVR, ONE, SOMI, SSV, WAN, WARD, WLD, XCH, XCN, XEC, XMR; bruto zonder voorraadgrens zou €186,52 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - kucoin, €150,00: munten ANIME, BSV, CFX, CHIP, ENJ, ENS, FET, JASMY, LAT, LUNC, MEME, MOVR, ONE, SOMI, SSV, WAN, WARD, WLD, XCH, XCN, XEC, XMR; bruto zonder voorraadgrens zou €186,52 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - kucoin, €200,00: munten ANIME, BSV, CFX, CHIP, ENJ, ENS, FET, JASMY, LAT, LUNC, MEME, MOVR, ONE, SOMI, SSV, WAN, WARD, WLD, XCH, XCN, XEC, XMR; bruto zonder voorraadgrens zou €186,52 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - kucoin, €2.000,00: munten ANIME, BSV, CFX, CHIP, ENJ, ENS, FET, JASMY, LAT, LUNC, MEME, MOVR, ONE, SOMI, SSV, WAN, WARD, WLD, XCH, XCN, XEC, XMR; bruto zonder voorraadgrens zou €185,92 zijn, met voorraad €9,35 (GEZIEN boek, GOK model).
- htx - kucoin, €5.000,00: munten ANIME, BSV, CFX, CHIP, ENJ, ENS, FET, JASMY, LAT, LUNC, MEME, MOVR, ONE, SOMI, SSV, WAN, WARD, WLD, XCH, XCN, XEC, XMR; bruto zonder voorraadgrens zou €185,03 zijn, met voorraad €29,76 (GEZIEN boek, GOK model).
- bitget - xt, €100,00: munten ENSO, KOR, KUB, LUNC, YB; bruto zonder voorraadgrens zou €788,49 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - xt, €150,00: munten ENSO, KOR, KUB, LUNC, YB; bruto zonder voorraadgrens zou €788,49 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - xt, €200,00: munten ENSO, KOR, KUB, LUNC, YB; bruto zonder voorraadgrens zou €788,06 zijn, met voorraad €0,50 (GEZIEN boek, GOK model).
- bitget - xt, €2.000,00: munten ENSO, KOR, KUB, LUNC, YB; bruto zonder voorraadgrens zou €783,09 zijn, met voorraad €15,90 (GEZIEN boek, GOK model).
- bitget - xt, €5.000,00: munten ENSO, KOR, KUB, LUNC, YB; bruto zonder voorraadgrens zou €776,50 zijn, met voorraad €32,45 (GEZIEN boek, GOK model).

### Andere keuzes bij bitvavo - kraken (netto handel, alle dagen samen; GOK)

| Keuze | Inleg | Kansen | Gemist | Bruto winst | Kosten terugschuiven | Netto handel |
|---|---|---|---|---|---|---|
| standaard (schuifdrempel 25%, kostengrens 1%) | €150,00 | 56 | 55 | €0,76 | €0,00 | **€0,76** |
| standaard (schuifdrempel 25%, kostengrens 1%) | €2.000,00 | 56 | 36 | €27,33 | €8,03 | **€19,30** |
| schuifdrempel 10% | €150,00 | 56 | 55 | €0,76 | €0,00 | **€0,76** |
| schuifdrempel 10% | €2.000,00 | 56 | 37 | €27,37 | €6,72 | **€20,65** |
| schuifdrempel 40% | €150,00 | 56 | 55 | €0,76 | €0,00 | **€0,76** |
| schuifdrempel 40% | €2.000,00 | 56 | 34 | €30,25 | €9,65 | **€20,60** |
| kostengrens 2% (achteraf vergeleken) | €150,00 | 56 | 55 | €0,76 | €0,00 | **€0,76** |
| kostengrens 2% (achteraf vergeleken) | €2.000,00 | 56 | 24 | €30,04 | €25,61 | **€4,43** |
| kostengrens 5% (achteraf vergeleken) | €150,00 | 56 | 55 | €0,76 | €0,00 | **€0,76** |
| kostengrens 5% (achteraf vergeleken) | €2.000,00 | 56 | 24 | €30,04 | €25,61 | **€4,43** |
| alleen MERL en KERNEL (meer voorraad per munt, achteraf gekozen) | €150,00 | 19 | 17 | €2,05 | €0,00 | **€2,05** |
| alleen MERL en KERNEL (meer voorraad per munt, achteraf gekozen) | €2.000,00 | 19 | 9 | €78,49 | €7,90 | **€70,59** |

Kostengrens: terugschuiven mag alleen als de opnamekosten hooguit dat deel van het bedrag zijn. De standaard van 1% is **achteraf** gekozen, nadat bleek dat bij 5% de kosten de winst opaten; de rijen met 2% en 5% laten zien hoeveel de uitkomst van die ene regel afhangt. Bij "alleen ..." tellen de kansen in andere munten niet mee (je hebt die munten dan niet).

Dag en Gemeten: de kansen komen alleen uit de uren dat de scanner mat (GEZIEN); het koerseffect loopt door over de hele tijd van de eerste tot de laatste meting. Rendement = netto gedeeld door de inleg, voor die dag. * = koers niet op te halen, koerseffect onbekend (niet als 0 bedoeld). **Het koerseffect is het risico van de voorraad, geen opbrengst van de methode:** bij één munt over een paar uur is het vooral toeval. Kijk voor wat de methode oplevert naar Netto handel.

**Aannames:**

- Winst per kans: de mediaan van wat de scanner op het boek mat bij €100, €500, €1.000, €2.500 en de volle ruimte (GEZIEN), lineair daartussen (GOK). Uitgevoerd 2 minuten na het begin (dan pas weet je dat hij meetelt), één keer per kans; gaat dezelfde kans binnen 5 minuten weer open, dan is het deel van het boek dat je al gebruikte op (GOK).
- Inleg: de helft geld (de quote van de kansen), de helft munten, verdeeld over de munten die op dat paar echte kansen hadden, en alles half op elke beurs (GOK). Die munten zijn **achteraf** gekozen; vooraf weet je dat niet.
- Terugschuiven zodra een kant onder 25% van zijn beginvoorraad komt: de helft van het verschil gaat terug, alleen als de opnamekosten hooguit 1% van het bedrag zijn (GOK, eigen regel). Die 1% is **achteraf** gekozen: eerst stond hier 5%, en pas nadat bleek dat de kosten bij 5% de winst opaten, is het 1% geworden (reden: een kans levert ±0,3 tot 1% bruto). Zie de rijen kostengrens 2% en 5% bij Andere keuzes.
- Opnamekosten van de munt: wat de scanner bij die beurs zag (GEZIEN uit de API van de beurs; bij Kraken en Gate geschat uit andere beurzen, GOK). Geld: zie de tabel hieronder.
- Een munt is na 30 minuten op de andere beurs (GOK). Zolang iets onderweg is, telt het niet als voorraad; kansen die daardoor niet of kleiner konden, staan als gemist of beperkt.
- Minimale order (in euro en in munten) en minimale opname van de munt per beurs en munt: uit de openbare API van Bitvavo, Kraken, KuCoin en Gate (GEZIEN, opgehaald bij het maken van het rapport). Een kans onder het minimum telt als gemist; een terugschuif onder het opnameminimum wordt opgehoogd tot het minimum. Andere beurzen of geen antwoord: minimale order 10 euro (GOK). Kraken geeft zijn opnameminimum niet openbaar: daar geen minimum (GOK). USDT telt tegen de koers van het moment van de kans; de koers USDT-EUR zelf beweegt niet mee (GOK).
- Koerseffect: slotkoers per 15 minuten (of per uur) uit de openbare candles van Bitvavo, Kraken, KuCoin of Gate (GEZIEN), over alle aangehouden munten, ook als de scanner tussen twee runs even niet mat.
- Niet meegeteld: andere bots die dezelfde kans pakken, dat het boek zich na jouw order aanvult (dan kan het vaker), belasting, en dat de EU-versie van een beurs minder munten kan hebben dan de API die we meten.
- Geld terugschuiven per beurs: bitget USDT: 1 USDT, GOK (1 USDT, 30 min; niet nagekeken); bitstamp EUR: 1 EUR, GOK (1 EUR, 24 uur; niet nagekeken); bitstamp USD: 1 USD, GOK (1 USD, 24 uur; niet nagekeken); bitvavo EUR: 0 EUR, kosten GEZIEN (api.bitvavo.com/v2/assets: EUR withdrawalFee 0), tijd GOK (1 werkdag, SEPA), minimum 0 EUR (GEZIEN, api.bitvavo.com/v2/assets withdrawalMinAmount); gate USDT: 1 USDT, GOK (1 USDT, 30 min; niet nagekeken), minimum 1 USDT (GEZIEN, api.gateio.ws/api/v4/wallet/currency_chains withdraw_amount_min); htx USDT: 1 USDT, GOK (1 USDT, 30 min; niet nagekeken); kraken EUR: 1 EUR, kosten GEZIEN (support.kraken.com/articles/360000381846: Instant SEPA, Banking Circle, 1 EUR, near-instant), tijd GOK (1 uur tot het op de andere beurs staat), minimum 2 EUR (GEZIEN, support.kraken.com/articles/360000381846 Instant SEPA (Banking Circle)); kraken USD: 1 USD, GOK (1 USD, 24 uur; niet nagekeken); kucoin EUR: 1 EUR, GOK (1 EUR, 24 uur; niet nagekeken); kucoin USDT: 1 USDT, kosten GEZIEN (api.kucoin.com/api/v3/currencies/USDT: BEP20 1 USDT), tijd GOK, minimum 5 USDT (GEZIEN, api.kucoin.com/api/v3/currencies/USDT BEP20 withdrawalMinSize); xt USDT: 1 USDT, GOK (1 USDT, 30 min; niet nagekeken).

## Over de meting

- Opnamekosten bij de echte kansen: 116 van een netwerk dat aan beide kanten open is, 97 van de beurs zelf (laagste open netwerk), 54 geschat uit wat andere beurzen voor die munt vragen (GOK). Onbekende opnamekosten tellen niet als echte kans.
- Netwerk: KuCoin, Gate, Bitget, HTX, XT, Bitstamp, Bitvavo en Poloniex geven hun netwerken per munt. Als beide beurzen dat doen en de namen te koppelen zijn, moet er een netwerk zijn dat aan beide kanten open is. Anders is het netwerk "niet te koppelen" en telt de kans mee (staat apart in de trechter).
- De duur is gemeten in stappen van ±20 seconden; een kans kan een paar rondes eerder begonnen zijn dan we zagen.
- Takerkosten: uit de API waar die ze per paar geeft, anders het standaardtarief uit de README (deels GOK).
- Laatste run: 15 beurzen antwoordden, 2289 munt-quote-paren op minstens twee beurzen (GEZIEN).
