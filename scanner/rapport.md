# Rapport koersverschil-scanner

Gemaakt 2026-11-20 20:34 UTC uit 20 runs, samen ±34.8 uur gemeten (GEZIEN).
Echte kans = winst na alle kosten (opnamekosten bekend), opnemen en storten open (en een netwerk dat aan beide kanten open is, als de beurzen dat geven), minstens €100,00 op het boek, minstens 2 minuten blijven staan, geen andere munt met dezelfde naam.
**Vergund** = beide beurzen hebben een MiCA-vergunning (ESMA-register), vaak via een EU-dochter die minder munten kan hebben dan de wereldwijde API die we meten (GOK). **Grijs** = minstens één beurs zonder vergunning (MEXC, Bitget, HTX, Poloniex, XT, Bitfinex, Binance). Zie README.md.
**Kraken-tarief:** Kraken rekent 0,80% taker op munt tegen EUR, USD, USDT of USDC (GEZIEN, kraken.com/pro/fees, laagste trede); de scanner rekende tot 19 nov met 0,40%. 399 opgeslagen kansen met Kraken uit die runs zijn hier **opnieuw doorgerekend met 0,80%** (GOK-benadering: 0,40% van de inzet aan de Kraken-kant extra op elk gemeten punt van het boek; het boek zelf is niet bewaard). 233 houden daarna nog winst op het boek. Dat ze met hogere kosten ook korter bleven staan, telt niet mee (dus eerder te gunstig).

## Hoeveel wordt er gecontroleerd? (GEZIEN, stand.jsonl)

Per ronde (mediaan over 417 metingen): 1138 kandidaten (verschil op de ticker groter dan de takerkosten), 120 met het orderboek gecontroleerd, 2 nog nooit gecontroleerd (0%).
Bijna alle kandidaten komen aan de beurt; de aantallen hieronder missen weinig.

## Trechter (GEZIEN, eigen metingen)

| Stap | Alle beurzen | Alleen MiCA-beurzen | Met minstens één grijze beurs |
|---|---|---|---|
| Verschillen met winst op het boek na alle kosten | 31475 | 4677 | 26798 |
| ...waarvan opnemen of storten dicht | 6437 | 700 | 5737 |
| ...waarvan status onbekend (beurs geeft het niet openbaar) | 18739 | 3331 | 15408 |
| Opnemen en storten open | 6299 | 646 | 5653 |
| ...en geen netwerk dat aan beide kanten open is: valt af | 153 | 11 | 142 |
| ...en opnamekosten onbekend: valt af | 0 | 0 | 0 |
| ...en minstens €100,00 op het boek | 1794 | 363 | 1431 |
| ...en minstens 2 minuten blijven staan | 495 | 145 | 350 |
| ...en geen andere munt met dezelfde naam | 458 | 129 | 329 |
|    ...waarvan contractadres bekend en gelijk | 62 | 25 | 37 |
|    ...waarvan contractadres onbekend (telt mee, kan een andere munt zijn) | 396 | 104 | 292 |
|    ...waarvan netwerk gekoppeld en open | 294 | 60 | 234 |
|    ...waarvan netwerk niet te koppelen (telt mee) | 164 | 69 | 95 |
| **Echte kansen** (zelfde munt overlappend in de tijd samengevoegd, beste beurspaar telt) | 299 | 128 | 206 |
| Ter vergelijking: zelfde eisen, maar opnamestatus onbekend (niet meegeteld) | 1068 | 262 | 900 |

## Echte kansen per dag (GEZIEN)

| Dag | Echt, alleen MiCA | Echt, met grijs | Mediane winst per kans bij €500 (MiCA / grijs) | Mediane duur |
|---|---|---|---|---|
| 2026-11-19 | 49 | 86 | €2,00 / €1,21 | 5.3 min |
| 2026-11-20 | 48 | 116 | €0,87 / €1,03 | 6.7 min |
| Totaal | 97 | 202 | €1,53 / €1,15 | 6.0 min |

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
| BSV-USDT | grijs | 13 | €17,59 |
| GMT-EUR | vergund | 21 | €17,57 |

## Beste beursparen (kopen op > verkopen op) (GEZIEN)

| | Soort | Kansen | Som winst bij €500 per kans |
|---|---|---|---|
| bitvavo > kraken | vergund | 56 | €327,52 |
| bitget > htx | grijs | 45 | €110,22 |
| kucoin > htx | grijs | 28 | €62,34 |
| gate > kucoin | vergund | 23 | €59,95 |
| kucoin > bitget | grijs | 19 | €46,16 |
| bitget > xt | grijs | 12 | €43,27 |
| bitget > gate | grijs | 10 | €30,26 |
| gate > xt | grijs | 4 | €28,67 |
| bitstamp > kraken | vergund | 2 | €21,52 |
| htx > xt | grijs | 3 | €19,34 |

Beurzen die het vaakst meedoen (koop of verkoop): bitget (grijs) 127, kucoin 120, htx (grijs) 101, kraken 76, gate 71, bitvavo 56, xt (grijs) 32, poloniex (grijs) 13 (GEZIEN).

## Hoeveel kansen blijven staan terwijl je geld schuift? (GEZIEN, duur uit eigen metingen)

Wie geen voorraad op beide beurzen heeft, moet kopen, de munt opnemen, wachten tot hij binnen is en dan verkopen. Hoe lang dat duurt verschilt per munt en netwerk: een paar minuten (snelle ketens) tot een uur of meer (Bitcoin, beurzen die opnames met de hand keuren) (GOK, niet per munt gemeten).

| Overmaaktijd | Alle beurzen | Alleen MiCA-beurzen | Met minstens één grijze beurs |
|---|---|---|---|
| 5 min | 179 van 299 (60%) | 75 van 128 (59%) | 124 van 206 (60%) |
| 10 min | 110 van 299 (37%) | 47 van 128 (37%) | 77 van 206 (37%) |
| 30 min | 55 van 299 (18%) | 27 van 128 (21%) | 38 van 206 (18%) |
| 60 min | 26 van 299 (9%) | 16 van 128 (12%) | 18 van 206 (9%) |

## Wat zou het opleveren over 3 maanden? (GOK, doorgetrokken uit de metingen)

Gemeten over ±34.8 uur (GEZIEN), doorgetrokken naar 90 dagen (GOK: aanname dat de week die we maten gewoon is).

| Beurzen | Inleg | Model | Kansen per uur | Per kans (mediaan) | 3 maanden |
|---|---|---|---|---|---|
| Alleen MiCA | €2.000,00 | bovengrens: elke kans, geld overal tegelijk | 3.68 | €1,68 | €13.357,23 |
| Alleen MiCA | €2.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 1.61 | €2,73 | €34.506,68 |
| Alleen MiCA | €5.000,00 | bovengrens: elke kans, geld overal tegelijk | 3.68 | €2,19 | €17.392,48 |
| Alleen MiCA | €5.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 1.61 | €3,21 | €50.947,12 |
| Alle (met grijs) | €2.000,00 | bovengrens: elke kans, geld overal tegelijk | 8.60 | €1,49 | €27.720,76 |
| Alle (met grijs) | €2.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 1.61 | €2,73 | €34.506,68 |
| Alle (met grijs) | €5.000,00 | bovengrens: elke kans, geld overal tegelijk | 8.60 | €1,64 | €30.454,55 |
| Alle (met grijs) | €5.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 1.61 | €3,21 | €50.947,12 |

Bovengrens: elke kans met de helft van de inleg aan elke kant, alsof het geld op alle beurzen tegelijk staat (kan in het echt niet). Beste beurspaar: het paar is **achteraf** gekozen uit de metingen (vooraf kiezen levert minder op), en het model neemt aan dat je van elke munt al voorraad op de verkoopbeurs hebt.

Waarom dit te rooskleurig is (GOK): elke kans wordt maar één keer geteld met het mediane boek, maar andere bots pakken hem ook; de munt die je als voorraad aanhoudt kan dalen; na een paar kansen moet de voorraad terug (opnamekosten en tijd); minimale opname- en ordergroottes tellen niet mee; en een kans die we 2 minuten zagen staan, staat er niet per se nog als jouw order binnenkomt. Waarom het te somber kan zijn: niet alle kandidaten zijn gecontroleerd, en met voorraad op beide beurzen kun je dezelfde kans vaker pakken als het boek zich aanvult; dat telt hier niet mee.

## Wat houd je echt over? Voorraad op twee beurzen (simulatie)

Per beurspaar: geld en munten op beide beurzen, elke echte kans uitgevoerd tegen het boek zoals gemeten (niet meer dan de ruimte op het boek en niet meer dan de voorraad op die beurs), terugschuiven als een kant leeg dreigt te raken (met opnamekosten en tijd onderweg), en het koerseffect van de aangehouden munten apart. Netto = bruto min kosten terugschuiven plus koerseffect. **Gemeten** (GEZIEN): de kansen, het boek en de koersen; **de rest is een rekenmodel** (GOK, aannames onder de tabel). Geen advies.

**Met €150: netto €0,89 per dag op bitstamp - kraken (koerseffect erbovenop €-2,50), €-0,00 per dag op bitstamp - kucoin (koerseffect erbovenop €0,18), €0,38 per dag op bitvavo - kraken (koerseffect erbovenop €-2,42), €0,06 per dag op gate - kucoin (koerseffect erbovenop €-1,22), €0,02 per dag op kraken - kucoin (koerseffect erbovenop €0,18) (GOK: netto handel, rekenmodel op ±17.4 uur meting per dag, alleen MiCA).** "Per dag" is hier gemiddeld over 2 gemeten dagen achter elkaar; de eerste begint met een gelijk verdeelde voorraad; aan het eind staat de voorraad scheef, dus een volgende dag levert waarschijnlijk minder op, tenzij kansen de andere kant op hem terugbrengen (GOK).

### Alleen MiCA-beurzen (alle paren met echte kansen)

| Beurspaar | Inleg | Dag | Gemeten | Kansen | Gemist (geen voorraad) | Kleiner door voorraad | Bruto winst | Kosten terugschuiven | **Netto handel (bruto min kosten)** | Rendement handel | Koerseffect voorraad | Netto met koerseffect | Rendement met koerseffect |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| bitstamp - kraken | €100,00 | 2026-11-19 | 14.9 u | 2 | 1 | 1 | €1,18 | €0,00 (0x) | **€1,18** | 1.18% | €0,63 | €1,81 | 1.81% |
| bitstamp - kraken | €100,00 | 2026-11-20 | 19.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,96 | €-3,96 | -3.96% |
| bitstamp - kraken | €150,00 | 2026-11-19 | 14.9 u | 2 | 1 | 1 | €1,78 | €0,00 (0x) | **€1,78** | 1.18% | €0,94 | €2,72 | 1.81% |
| bitstamp - kraken | €150,00 | 2026-11-20 | 19.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-5,95 | €-5,95 | -3.96% |
| bitstamp - kraken | €200,00 | 2026-11-19 | 14.9 u | 2 | 1 | 1 | €2,37 | €0,00 (0x) | **€2,37** | 1.18% | €1,25 | €3,62 | 1.81% |
| bitstamp - kraken | €200,00 | 2026-11-20 | 19.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-7,93 | €-7,93 | -3.96% |
| bitstamp - kraken | €2.000,00 | 2026-11-19 | 14.9 u | 2 | 1 | 0 | €11,71 | €0,00 (0x) | **€11,71** | 0.59% | €12,53 | €24,24 | 1.21% |
| bitstamp - kraken | €2.000,00 | 2026-11-20 | 19.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-79,30 | €-79,30 | -3.96% |
| bitstamp - kraken | €5.000,00 | 2026-11-19 | 14.9 u | 2 | 1 | 0 | €11,71 | €0,00 (0x) | **€11,71** | 0.23% | €31,33 | €43,04 | 0.86% |
| bitstamp - kraken | €5.000,00 | 2026-11-20 | 19.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-198,25 | €-198,25 | -3.96% |
| bitstamp - kucoin | €100,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,14 | €0,14 | 0.14% |
| bitstamp - kucoin | €100,00 | 2026-11-20 | 19.8 u | 1 | 0 | 1 | €0,01 | €0,01 (1x) | **€-0,00** | -0.00% | €0,10 | €0,09 | 0.09% |
| bitstamp - kucoin | €150,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,21 | €0,21 | 0.14% |
| bitstamp - kucoin | €150,00 | 2026-11-20 | 19.8 u | 1 | 0 | 1 | €0,01 | €0,01 (1x) | **€-0,00** | -0.00% | €0,15 | €0,15 | 0.10% |
| bitstamp - kucoin | €200,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,27 | €0,27 | 0.14% |
| bitstamp - kucoin | €200,00 | 2026-11-20 | 19.8 u | 1 | 0 | 1 | €0,01 | €0,01 (1x) | **€0,00** | 0.00% | €0,20 | €0,20 | 0.10% |
| bitstamp - kucoin | €2.000,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €2,74 | €2,74 | 0.14% |
| bitstamp - kucoin | €2.000,00 | 2026-11-20 | 19.8 u | 1 | 0 | 1 | €0,10 | €1,01 (2x) | **€-0,91** | -0.05% | €1,98 | €1,07 | 0.05% |
| bitstamp - kucoin | €5.000,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €6,86 | €6,86 | 0.14% |
| bitstamp - kucoin | €5.000,00 | 2026-11-20 | 19.8 u | 1 | 0 | 1 | €0,25 | €1,01 (2x) | **€-0,76** | -0.02% | €4,94 | €4,18 | 0.08% |
| bitvavo - kraken | €100,00 | 2026-11-19 | 14.9 u | 43 | 43 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,62 | €-0,62 | -0.62% |
| bitvavo - kraken | €100,00 | 2026-11-20 | 19.8 u | 13 | 13 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,61 | €-2,61 | -2.61% |
| bitvavo - kraken | €150,00 | 2026-11-19 | 14.9 u | 43 | 43 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,93 | €-0,93 | -0.62% |
| bitvavo - kraken | €150,00 | 2026-11-20 | 19.8 u | 13 | 12 | 1 | €0,76 | €0,00 (0x) | **€0,76** | 0.51% | €-3,91 | €-3,15 | -2.10% |
| bitvavo - kraken | €200,00 | 2026-11-19 | 14.9 u | 43 | 37 | 6 | €0,14 | €0,00 (0x) | **€0,14** | 0.07% | €-1,24 | €-1,10 | -0.55% |
| bitvavo - kraken | €200,00 | 2026-11-20 | 19.8 u | 13 | 12 | 1 | €1,01 | €0,00 (0x) | **€1,01** | 0.51% | €-5,22 | €-4,20 | -2.10% |
| bitvavo - kraken | €2.000,00 | 2026-11-19 | 14.9 u | 43 | 27 | 16 | €11,14 | €6,39 (16x) | **€4,75** | 0.24% | €-12,32 | €-7,57 | -0.38% |
| bitvavo - kraken | €2.000,00 | 2026-11-20 | 19.8 u | 13 | 9 | 4 | €16,20 | €1,64 (3x) | **€14,55** | 0.73% | €-51,77 | €-37,21 | -1.86% |
| bitvavo - kraken | €5.000,00 | 2026-11-19 | 14.9 u | 43 | 22 | 21 | €28,08 | €14,95 (24x) | **€13,12** | 0.26% | €-30,85 | €-17,73 | -0.35% |
| bitvavo - kraken | €5.000,00 | 2026-11-20 | 19.8 u | 13 | 2 | 11 | €42,61 | €10,66 (12x) | **€31,96** | 0.64% | €-128,69 | €-96,74 | -1.93% |
| gate - kucoin | €100,00 | 2026-11-19 | 14.9 u | 25 | 25 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,83 | €-0,83 | -0.83% |
| gate - kucoin | €100,00 | 2026-11-20 | 19.8 u | 39 | 39 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,79 | €-0,79 | -0.79% |
| gate - kucoin | €150,00 | 2026-11-19 | 14.9 u | 25 | 25 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,25 | €-1,25 | -0.83% |
| gate - kucoin | €150,00 | 2026-11-20 | 19.8 u | 39 | 37 | 2 | €0,13 | €0,00 (1x) | **€0,13** | 0.09% | €-1,19 | €-1,06 | -0.71% |
| gate - kucoin | €200,00 | 2026-11-19 | 14.9 u | 25 | 25 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,66 | €-1,66 | -0.83% |
| gate - kucoin | €200,00 | 2026-11-20 | 19.8 u | 39 | 36 | 3 | €0,26 | €0,00 (1x) | **€0,26** | 0.13% | €-1,58 | €-1,32 | -0.66% |
| gate - kucoin | €2.000,00 | 2026-11-19 | 14.9 u | 25 | 9 | 16 | €2,39 | €2,15 (12x) | **€0,24** | 0.01% | €-16,61 | €-16,37 | -0.82% |
| gate - kucoin | €2.000,00 | 2026-11-20 | 19.8 u | 39 | 12 | 27 | €9,90 | €1,83 (14x) | **€8,07** | 0.40% | €-15,65 | €-7,59 | -0.38% |
| gate - kucoin | €5.000,00 | 2026-11-19 | 14.9 u | 25 | 6 | 19 | €8,36 | €4,84 (19x) | **€3,52** | 0.07% | €-41,56 | €-38,04 | -0.76% |
| gate - kucoin | €5.000,00 | 2026-11-20 | 19.8 u | 39 | 7 | 32 | €26,40 | €6,26 (26x) | **€20,14** | 0.40% | €-39,04 | €-18,90 | -0.38% |
| kraken - kucoin | €100,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,11 | €0,11 | 0.11% |
| kraken - kucoin | €100,00 | 2026-11-20 | 19.8 u | 6 | 4 | 2 | €0,03 | €0,01 (1x) | **€0,02** | 0.02% | €0,13 | €0,15 | 0.15% |
| kraken - kucoin | €150,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,16 | €0,16 | 0.11% |
| kraken - kucoin | €150,00 | 2026-11-20 | 19.8 u | 6 | 4 | 2 | €0,05 | €0,01 (1x) | **€0,04** | 0.02% | €0,19 | €0,23 | 0.15% |
| kraken - kucoin | €200,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,22 | €0,22 | 0.11% |
| kraken - kucoin | €200,00 | 2026-11-20 | 19.8 u | 6 | 4 | 2 | €0,06 | €0,24 (2x) | **€-0,18** | -0.09% | €0,25 | €0,07 | 0.04% |
| kraken - kucoin | €2.000,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €2,19 | €2,19 | 0.11% |
| kraken - kucoin | €2.000,00 | 2026-11-20 | 19.8 u | 6 | 4 | 2 | €0,61 | €1,24 (3x) | **€-0,63** | -0.03% | €2,52 | €1,89 | 0.09% |
| kraken - kucoin | €5.000,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €5,49 | €5,49 | 0.11% |
| kraken - kucoin | €5.000,00 | 2026-11-20 | 19.8 u | 6 | 4 | 2 | €1,53 | €1,24 (3x) | **€0,29** | 0.01% | €6,31 | €6,59 | 0.13% |

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
- gate - kucoin, €100,00: munten ALKIMI, AVAIL, CCD, CHR, CWEB, CYBER, EDEN, ERG, FTT, HTR, IKA, IR, KYO, LUNC, NAKA, NIM, OVR, POKT, RARI, STREAM, USTC, VERONA; bruto zonder voorraadgrens zou €215,30 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- gate - kucoin, €150,00: munten ALKIMI, AVAIL, CCD, CHR, CWEB, CYBER, EDEN, ERG, FTT, HTR, IKA, IR, KYO, LUNC, NAKA, NIM, OVR, POKT, RARI, STREAM, USTC, VERONA; bruto zonder voorraadgrens zou €215,28 zijn, met voorraad €0,13 (GEZIEN boek, GOK model).
- gate - kucoin, €200,00: munten ALKIMI, AVAIL, CCD, CHR, CWEB, CYBER, EDEN, ERG, FTT, HTR, IKA, IR, KYO, LUNC, NAKA, NIM, OVR, POKT, RARI, STREAM, USTC, VERONA; bruto zonder voorraadgrens zou €215,27 zijn, met voorraad €0,26 (GEZIEN boek, GOK model).
- gate - kucoin, €2.000,00: munten ALKIMI, AVAIL, CCD, CHR, CWEB, CYBER, EDEN, ERG, FTT, HTR, IKA, IR, KYO, LUNC, NAKA, NIM, OVR, POKT, RARI, STREAM, USTC, VERONA; bruto zonder voorraadgrens zou €213,42 zijn, met voorraad €12,28 (GEZIEN boek, GOK model).
- gate - kucoin, €5.000,00: munten ALKIMI, AVAIL, CCD, CHR, CWEB, CYBER, EDEN, ERG, FTT, HTR, IKA, IR, KYO, LUNC, NAKA, NIM, OVR, POKT, RARI, STREAM, USTC, VERONA; bruto zonder voorraadgrens zou €208,82 zijn, met voorraad €34,76 (GEZIEN boek, GOK model).
- kraken - kucoin, €100,00: munten USDC, USDT; bruto zonder voorraadgrens zou €28,92 zijn, met voorraad €0,03 (GEZIEN boek, GOK model).
- kraken - kucoin, €150,00: munten USDC, USDT; bruto zonder voorraadgrens zou €28,91 zijn, met voorraad €0,05 (GEZIEN boek, GOK model).
- kraken - kucoin, €200,00: munten USDC, USDT; bruto zonder voorraadgrens zou €28,91 zijn, met voorraad €0,06 (GEZIEN boek, GOK model).
- kraken - kucoin, €2.000,00: munten USDC, USDT; bruto zonder voorraadgrens zou €28,63 zijn, met voorraad €0,61 (GEZIEN boek, GOK model).
- kraken - kucoin, €5.000,00: munten USDC, USDT; bruto zonder voorraadgrens zou €28,17 zijn, met voorraad €1,53 (GEZIEN boek, GOK model).

### Met minstens één grijze beurs (de 5 paren met de meeste bruto winst)

| Beurspaar | Inleg | Dag | Gemeten | Kansen | Gemist (geen voorraad) | Kleiner door voorraad | Bruto winst | Kosten terugschuiven | **Netto handel (bruto min kosten)** | Rendement handel | Koerseffect voorraad | Netto met koerseffect | Rendement met koerseffect |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| htx - xt | €100,00 | 2026-11-19 | 14.9 u | 18 | 18 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,69 | €-0,69 | -0.69% |
| htx - xt | €100,00 | 2026-11-20 | 19.8 u | 12 | 12 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,26 | €-3,26 | -3.26% |
| htx - xt | €150,00 | 2026-11-19 | 14.9 u | 18 | 18 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,03 | €-1,03 | -0.69% |
| htx - xt | €150,00 | 2026-11-20 | 19.8 u | 12 | 12 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-4,90 | €-4,90 | -3.26% |
| htx - xt | €200,00 | 2026-11-19 | 14.9 u | 18 | 18 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,38 | €-1,38 | -0.69% |
| htx - xt | €200,00 | 2026-11-20 | 19.8 u | 12 | 12 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-6,53 | €-6,53 | -3.26% |
| htx - xt | €2.000,00 | 2026-11-19 | 14.9 u | 18 | 5 | 13 | €6,47 | €4,36 (11x) | **€2,11** | 0.11% | €-13,84 | €-11,73 | -0.59% |
| htx - xt | €2.000,00 | 2026-11-20 | 19.8 u | 12 | 1 | 11 | €12,78 | €2,95 (7x) | **€9,82** | 0.49% | €-64,62 | €-54,79 | -2.74% |
| htx - xt | €5.000,00 | 2026-11-19 | 14.9 u | 18 | 5 | 12 | €15,21 | €6,19 (13x) | **€9,02** | 0.18% | €-34,52 | €-25,50 | -0.51% |
| htx - xt | €5.000,00 | 2026-11-20 | 19.8 u | 12 | 0 | 12 | €31,87 | €6,57 (11x) | **€25,30** | 0.51% | €-162,31 | €-137,01 | -2.74% |
| gate - htx | €100,00 | 2026-11-19 | 14.9 u | 19 | 19 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,89 | €-0,89 | -0.89% |
| gate - htx | €100,00 | 2026-11-20 | 19.8 u | 27 | 27 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,31 | €-3,31 | -3.31% |
| gate - htx | €150,00 | 2026-11-19 | 14.9 u | 19 | 19 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,34 | €-1,34 | -0.89% |
| gate - htx | €150,00 | 2026-11-20 | 19.8 u | 27 | 27 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-4,96 | €-4,96 | -3.31% |
| gate - htx | €200,00 | 2026-11-19 | 14.9 u | 19 | 19 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,78 | €-1,78 | -0.89% |
| gate - htx | €200,00 | 2026-11-20 | 19.8 u | 27 | 27 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-6,61 | €-6,61 | -3.31% |
| gate - htx | €2.000,00 | 2026-11-19 | 14.9 u | 19 | 14 | 5 | €1,09 | €0,17 (1x) | **€0,92** | 0.05% | €-17,82 | €-16,89 | -0.84% |
| gate - htx | €2.000,00 | 2026-11-20 | 19.8 u | 27 | 9 | 18 | €7,81 | €1,46 (8x) | **€6,35** | 0.32% | €-66,11 | €-59,76 | -2.99% |
| gate - htx | €5.000,00 | 2026-11-19 | 14.9 u | 19 | 6 | 13 | €9,08 | €4,50 (12x) | **€4,58** | 0.09% | €-44,56 | €-39,98 | -0.80% |
| gate - htx | €5.000,00 | 2026-11-20 | 19.8 u | 27 | 4 | 23 | €23,80 | €4,61 (17x) | **€19,18** | 0.38% | €-164,66 | €-145,48 | -2.91% |
| htx - kucoin | €100,00 | 2026-11-19 | 14.9 u | 16 | 16 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,17 | €-2,17 | -2.17% |
| htx - kucoin | €100,00 | 2026-11-20 | 19.8 u | 38 | 38 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-4,06 | €-4,06 | -4.06% |
| htx - kucoin | €150,00 | 2026-11-19 | 14.9 u | 16 | 16 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,26 | €-3,26 | -2.17% |
| htx - kucoin | €150,00 | 2026-11-20 | 19.8 u | 38 | 38 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-6,09 | €-6,09 | -4.06% |
| htx - kucoin | €200,00 | 2026-11-19 | 14.9 u | 16 | 16 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-4,34 | €-4,34 | -2.17% |
| htx - kucoin | €200,00 | 2026-11-20 | 19.8 u | 38 | 38 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-8,12 | €-8,12 | -4.06% |
| htx - kucoin | €2.000,00 | 2026-11-19 | 14.9 u | 16 | 9 | 7 | €1,40 | €0,00 (1x) | **€1,40** | 0.07% | €-43,43 | €-42,03 | -2.10% |
| htx - kucoin | €2.000,00 | 2026-11-20 | 19.8 u | 38 | 21 | 17 | €7,88 | €0,00 (1x) | **€7,88** | 0.39% | €-81,23 | €-73,35 | -3.67% |
| htx - kucoin | €5.000,00 | 2026-11-19 | 14.9 u | 16 | 3 | 13 | €7,48 | €3,83 (12x) | **€3,65** | 0.07% | €-108,48 | €-104,84 | -2.10% |
| htx - kucoin | €5.000,00 | 2026-11-20 | 19.8 u | 38 | 10 | 28 | €22,18 | €6,62 (20x) | **€15,56** | 0.31% | €-202,51 | €-186,95 | -3.74% |
| kucoin - xt | €100,00 | 2026-11-19 | 14.9 u | 13 | 13 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,06 | €-0,06 | -0.06% |
| kucoin - xt | €100,00 | 2026-11-20 | 19.8 u | 5 | 5 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,20 | €-3,20 | -3.20% |
| kucoin - xt | €150,00 | 2026-11-19 | 14.9 u | 13 | 13 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,09 | €-0,09 | -0.06% |
| kucoin - xt | €150,00 | 2026-11-20 | 19.8 u | 5 | 5 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-4,80 | €-4,80 | -3.20% |
| kucoin - xt | €200,00 | 2026-11-19 | 14.9 u | 13 | 11 | 2 | €0,17 | €0,00 (0x) | **€0,17** | 0.09% | €-0,11 | €0,06 | 0.03% |
| kucoin - xt | €200,00 | 2026-11-20 | 19.8 u | 5 | 4 | 1 | €0,18 | €0,00 (0x) | **€0,18** | 0.09% | €-6,40 | €-6,22 | -3.11% |
| kucoin - xt | €2.000,00 | 2026-11-19 | 14.9 u | 13 | 3 | 10 | €11,08 | €5,50 (11x) | **€5,58** | 0.28% | €-1,12 | €4,46 | 0.22% |
| kucoin - xt | €2.000,00 | 2026-11-20 | 19.8 u | 5 | 1 | 4 | €4,66 | €2,42 (4x) | **€2,25** | 0.11% | €-63,54 | €-61,29 | -3.06% |
| kucoin - xt | €5.000,00 | 2026-11-19 | 14.9 u | 13 | 3 | 9 | €23,53 | €5,50 (11x) | **€18,04** | 0.36% | €-2,83 | €15,20 | 0.30% |
| kucoin - xt | €5.000,00 | 2026-11-20 | 19.8 u | 5 | 0 | 5 | €15,18 | €4,50 (6x) | **€10,68** | 0.21% | €-159,50 | €-148,82 | -2.98% |
| bitget - xt | €100,00 | 2026-11-19 | 14.9 u | 13 | 13 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €2,07 | €2,07 | 2.07% |
| bitget - xt | €100,00 | 2026-11-20 | 19.8 u | 5 | 5 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-4,74 | €-4,74 | -4.74% |
| bitget - xt | €150,00 | 2026-11-19 | 14.9 u | 13 | 13 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €3,11 | €3,11 | 2.07% |
| bitget - xt | €150,00 | 2026-11-20 | 19.8 u | 5 | 5 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-7,11 | €-7,11 | -4.74% |
| bitget - xt | €200,00 | 2026-11-19 | 14.9 u | 13 | 9 | 4 | €0,50 | €0,01 (3x) | **€0,50** | 0.25% | €4,15 | €4,64 | 2.32% |
| bitget - xt | €200,00 | 2026-11-20 | 19.8 u | 5 | 5 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-9,48 | €-9,48 | -4.74% |
| bitget - xt | €2.000,00 | 2026-11-19 | 14.9 u | 13 | 4 | 9 | €9,96 | €1,96 (11x) | **€8,00** | 0.40% | €41,46 | €49,46 | 2.47% |
| bitget - xt | €2.000,00 | 2026-11-20 | 19.8 u | 5 | 0 | 5 | €5,94 | €2,06 (6x) | **€3,88** | 0.19% | €-94,69 | €-90,81 | -4.54% |
| bitget - xt | €5.000,00 | 2026-11-19 | 14.9 u | 13 | 4 | 8 | €19,47 | €1,85 (10x) | **€17,62** | 0.35% | €103,65 | €121,27 | 2.43% |
| bitget - xt | €5.000,00 | 2026-11-20 | 19.8 u | 5 | 0 | 5 | €12,98 | €2,06 (6x) | **€10,93** | 0.22% | €-236,88 | €-225,95 | -4.52% |

- htx - xt, €100,00: munten BSV, CARV, CBK, HBAR, LUNC, MEME, SEI, XCH, XDC, XMR; bruto zonder voorraadgrens zou €209,28 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - xt, €150,00: munten BSV, CARV, CBK, HBAR, LUNC, MEME, SEI, XCH, XDC, XMR; bruto zonder voorraadgrens zou €209,28 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - xt, €200,00: munten BSV, CARV, CBK, HBAR, LUNC, MEME, SEI, XCH, XDC, XMR; bruto zonder voorraadgrens zou €209,28 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - xt, €2.000,00: munten BSV, CARV, CBK, HBAR, LUNC, MEME, SEI, XCH, XDC, XMR; bruto zonder voorraadgrens zou €207,68 zijn, met voorraad €19,25 (GEZIEN boek, GOK model).
- htx - xt, €5.000,00: munten BSV, CARV, CBK, HBAR, LUNC, MEME, SEI, XCH, XDC, XMR; bruto zonder voorraadgrens zou €205,63 zijn, met voorraad €47,07 (GEZIEN boek, GOK model).
- gate - htx, €100,00: munten APEPE, BRISE, BSV, CBK, CRTS, ENJ, ENS, GOMINING, KAS, LAT, LUNC, MEME, MOVR, SEI, SSV, WARD, WLD, XCH, XCN; bruto zonder voorraadgrens zou €181,08 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- gate - htx, €150,00: munten APEPE, BRISE, BSV, CBK, CRTS, ENJ, ENS, GOMINING, KAS, LAT, LUNC, MEME, MOVR, SEI, SSV, WARD, WLD, XCH, XCN; bruto zonder voorraadgrens zou €181,08 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- gate - htx, €200,00: munten APEPE, BRISE, BSV, CBK, CRTS, ENJ, ENS, GOMINING, KAS, LAT, LUNC, MEME, MOVR, SEI, SSV, WARD, WLD, XCH, XCN; bruto zonder voorraadgrens zou €181,08 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- gate - htx, €2.000,00: munten APEPE, BRISE, BSV, CBK, CRTS, ENJ, ENS, GOMINING, KAS, LAT, LUNC, MEME, MOVR, SEI, SSV, WARD, WLD, XCH, XCN; bruto zonder voorraadgrens zou €180,41 zijn, met voorraad €8,90 (GEZIEN boek, GOK model).
- gate - htx, €5.000,00: munten APEPE, BRISE, BSV, CBK, CRTS, ENJ, ENS, GOMINING, KAS, LAT, LUNC, MEME, MOVR, SEI, SSV, WARD, WLD, XCH, XCN; bruto zonder voorraadgrens zou €176,22 zijn, met voorraad €32,88 (GEZIEN boek, GOK model).
- htx - kucoin, €100,00: munten ANIME, BSV, CFX, CHIP, ELA, ENJ, ENS, FET, JASMY, LAT, LUNC, MEME, MOVR, ONE, SOMI, SSV, WAN, WARD, WLD, XCH, XCN, XEC, XMR; bruto zonder voorraadgrens zou €193,44 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - kucoin, €150,00: munten ANIME, BSV, CFX, CHIP, ELA, ENJ, ENS, FET, JASMY, LAT, LUNC, MEME, MOVR, ONE, SOMI, SSV, WAN, WARD, WLD, XCH, XCN, XEC, XMR; bruto zonder voorraadgrens zou €193,44 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - kucoin, €200,00: munten ANIME, BSV, CFX, CHIP, ELA, ENJ, ENS, FET, JASMY, LAT, LUNC, MEME, MOVR, ONE, SOMI, SSV, WAN, WARD, WLD, XCH, XCN, XEC, XMR; bruto zonder voorraadgrens zou €193,44 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - kucoin, €2.000,00: munten ANIME, BSV, CFX, CHIP, ELA, ENJ, ENS, FET, JASMY, LAT, LUNC, MEME, MOVR, ONE, SOMI, SSV, WAN, WARD, WLD, XCH, XCN, XEC, XMR; bruto zonder voorraadgrens zou €192,87 zijn, met voorraad €9,28 (GEZIEN boek, GOK model).
- htx - kucoin, €5.000,00: munten ANIME, BSV, CFX, CHIP, ELA, ENJ, ENS, FET, JASMY, LAT, LUNC, MEME, MOVR, ONE, SOMI, SSV, WAN, WARD, WLD, XCH, XCN, XEC, XMR; bruto zonder voorraadgrens zou €192,01 zijn, met voorraad €29,65 (GEZIEN boek, GOK model).
- kucoin - xt, €100,00: munten DAG, ENSO, FIGHT, LUNC, XMR; bruto zonder voorraadgrens zou €680,88 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- kucoin - xt, €150,00: munten DAG, ENSO, FIGHT, LUNC, XMR; bruto zonder voorraadgrens zou €680,88 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- kucoin - xt, €200,00: munten DAG, ENSO, FIGHT, LUNC, XMR; bruto zonder voorraadgrens zou €680,88 zijn, met voorraad €0,35 (GEZIEN boek, GOK model).
- kucoin - xt, €2.000,00: munten DAG, ENSO, FIGHT, LUNC, XMR; bruto zonder voorraadgrens zou €677,41 zijn, met voorraad €15,74 (GEZIEN boek, GOK model).
- kucoin - xt, €5.000,00: munten DAG, ENSO, FIGHT, LUNC, XMR; bruto zonder voorraadgrens zou €672,40 zijn, met voorraad €38,71 (GEZIEN boek, GOK model).
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

- Opnamekosten bij de echte kansen: 126 van een netwerk dat aan beide kanten open is, 104 van de beurs zelf (laagste open netwerk), 69 geschat uit wat andere beurzen voor die munt vragen (GOK). Onbekende opnamekosten tellen niet als echte kans.
- Netwerk: KuCoin, Gate, Bitget, HTX, XT, Bitstamp, Bitvavo en Poloniex geven hun netwerken per munt. Als beide beurzen dat doen en de namen te koppelen zijn, moet er een netwerk zijn dat aan beide kanten open is. Anders is het netwerk "niet te koppelen" en telt de kans mee (staat apart in de trechter).
- De duur is gemeten in stappen van ±20 seconden; een kans kan een paar rondes eerder begonnen zijn dan we zagen.
- Takerkosten: uit de API waar die ze per paar geeft, anders het standaardtarief uit de README (deels GOK).
- Laatste run: 15 beurzen antwoordden, 2288 munt-quote-paren op minstens twee beurzen (GEZIEN).
