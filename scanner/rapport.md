# Rapport koersverschil-scanner

Gemaakt 2026-11-20 00:50 UTC uit 17 runs, samen ±15.8 uur gemeten (GEZIEN).
Echte kans = winst na alle kosten (opnamekosten bekend), opnemen en storten open (en een netwerk dat aan beide kanten open is, als de beurzen dat geven), minstens €100,00 op het boek, minstens 2 minuten blijven staan, geen andere munt met dezelfde naam.
**Vergund** = beide beurzen hebben een MiCA-vergunning (ESMA-register), vaak via een EU-dochter die minder munten kan hebben dan de wereldwijde API die we meten (GOK). **Grijs** = minstens één beurs zonder vergunning (MEXC, Bitget, HTX, Poloniex, XT, Bitfinex, Binance). Zie README.md.
**Kraken-tarief:** Kraken rekent 0,80% taker op munt tegen EUR, USD, USDT of USDC (GEZIEN, kraken.com/pro/fees, laagste trede); de scanner rekende tot 19 nov met 0,40%. 399 opgeslagen kansen met Kraken uit die runs zijn hier **opnieuw doorgerekend met 0,80%** (GOK-benadering: 0,40% van de inzet aan de Kraken-kant extra op elk gemeten punt van het boek; het boek zelf is niet bewaard). 233 houden daarna nog winst op het boek. Dat ze met hogere kosten ook korter bleven staan, telt niet mee (dus eerder te gunstig).

## Hoeveel wordt er gecontroleerd? (GEZIEN, stand.jsonl)

Per ronde (mediaan over 189 metingen): 1060 kandidaten (verschil op de ticker groter dan de takerkosten), 120 met het orderboek gecontroleerd, 2 nog nooit gecontroleerd (0%).
Bijna alle kandidaten komen aan de beurt; de aantallen hieronder missen weinig.

## Trechter (GEZIEN, eigen metingen)

| Stap | Alle beurzen | Alleen MiCA-beurzen | Met minstens één grijze beurs |
|---|---|---|---|
| Verschillen met winst op het boek na alle kosten | 14466 | 2063 | 12403 |
| ...waarvan opnemen of storten dicht | 3379 | 318 | 3061 |
| ...waarvan status onbekend (beurs geeft het niet openbaar) | 8515 | 1465 | 7050 |
| Opnemen en storten open | 2572 | 280 | 2292 |
| ...en geen netwerk dat aan beide kanten open is: valt af | 36 | 2 | 34 |
| ...en opnamekosten onbekend: valt af | 0 | 0 | 0 |
| ...en minstens €100,00 op het boek | 733 | 156 | 577 |
| ...en minstens 2 minuten blijven staan | 232 | 80 | 152 |
| ...en geen andere munt met dezelfde naam | 206 | 69 | 137 |
|    ...waarvan contractadres bekend en gelijk | 16 | 3 | 13 |
|    ...waarvan contractadres onbekend (telt mee, kan een andere munt zijn) | 190 | 66 | 124 |
|    ...waarvan netwerk gekoppeld en open | 117 | 22 | 95 |
|    ...waarvan netwerk niet te koppelen (telt mee) | 89 | 47 | 42 |
| **Echte kansen** (zelfde munt overlappend in de tijd samengevoegd, beste beurspaar telt) | 135 | 69 | 85 |
| Ter vergelijking: zelfde eisen, maar opnamestatus onbekend (niet meegeteld) | 483 | 108 | 419 |

## Echte kansen per dag (GEZIEN)

| Dag | Echt, alleen MiCA | Echt, met grijs | Mediane winst per kans bij €500 (MiCA / grijs) | Mediane duur |
|---|---|---|---|---|
| 2026-11-19 | 49 | 85 | €1,72 / €1,20 | 5.3 min |
| 2026-11-20 | 1 | 0 | €0,17 / geen | 6.3 min |
| Totaal | 50 | 85 | €1,65 / €1,20 | 5.3 min |

## Beste munten (GEZIEN)

| | Soort | Kansen | Som winst bij €500 per kans |
|---|---|---|---|
| MERL-EUR | vergund | 14 | €149,78 |
| LUNC-USDT | grijs | 10 | €50,37 |
| USTC-USDT | grijs en vergund | 8 | €27,88 |
| SKY-USD | vergund | 2 | €21,52 |
| YB-USDT | grijs | 1 | €16,34 |
| GMT-EUR | vergund | 14 | €15,31 |
| WAN-USDT | grijs | 4 | €14,24 |
| VERONA-USDT | grijs | 8 | €13,53 |
| AVA-EUR | vergund | 4 | €11,22 |
| LUNA-EUR | vergund | 4 | €10,37 |

## Beste beursparen (kopen op > verkopen op) (GEZIEN)

| | Soort | Kansen | Som winst bij €500 per kans |
|---|---|---|---|
| bitvavo > kraken | vergund | 43 | €190,63 |
| kucoin > bitget | grijs | 10 | €28,27 |
| kucoin > htx | grijs | 13 | €25,07 |
| bitget > xt | grijs | 8 | €24,93 |
| bitget > gate | grijs | 6 | €23,63 |
| bitstamp > kraken | vergund | 2 | €21,52 |
| gate > xt | grijs | 2 | €19,11 |
| bitget > htx | grijs | 17 | €12,94 |
| htx > xt | grijs | 2 | €11,08 |
| kucoin > xt | grijs | 3 | €10,44 |

Beurzen die het vaakst meedoen (koop of verkoop): bitget (grijs) 52, kraken 45, kucoin 44, bitvavo 43, htx (grijs) 41, gate 20, xt (grijs) 20, poloniex (grijs) 3 (GEZIEN).

## Hoeveel kansen blijven staan terwijl je geld schuift? (GEZIEN, duur uit eigen metingen)

Wie geen voorraad op beide beurzen heeft, moet kopen, de munt opnemen, wachten tot hij binnen is en dan verkopen. Hoe lang dat duurt verschilt per munt en netwerk: een paar minuten (snelle ketens) tot een uur of meer (Bitcoin, beurzen die opnames met de hand keuren) (GOK, niet per munt gemeten).

| Overmaaktijd | Alle beurzen | Alleen MiCA-beurzen | Met minstens één grijze beurs |
|---|---|---|---|
| 5 min | 73 van 135 (54%) | 36 van 69 (52%) | 45 van 85 (53%) |
| 10 min | 43 van 135 (32%) | 23 van 69 (33%) | 25 van 85 (29%) |
| 30 min | 28 van 135 (21%) | 16 van 69 (23%) | 15 van 85 (18%) |
| 60 min | 13 van 135 (10%) | 7 van 69 (10%) | 8 van 85 (9%) |

## Wat zou het opleveren over 3 maanden? (GOK, doorgetrokken uit de metingen)

Gemeten over ±15.8 uur (GEZIEN), doorgetrokken naar 90 dagen (GOK: aanname dat de week die we maten gewoon is).

| Beurzen | Inleg | Model | Kansen per uur | Per kans (mediaan) | 3 maanden |
|---|---|---|---|---|---|
| Alleen MiCA | €2.000,00 | bovengrens: elke kans, geld overal tegelijk | 4.38 | €2,20 | €20.784,43 |
| Alleen MiCA | €2.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 2.73 | €2,92 | €42.062,30 |
| Alleen MiCA | €5.000,00 | bovengrens: elke kans, geld overal tegelijk | 4.38 | €2,65 | €25.098,40 |
| Alleen MiCA | €5.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 2.73 | €3,15 | €61.063,53 |
| Alle (met grijs) | €2.000,00 | bovengrens: elke kans, geld overal tegelijk | 8.57 | €1,58 | €29.262,65 |
| Alle (met grijs) | €2.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 2.73 | €2,92 | €42.062,30 |
| Alle (met grijs) | €5.000,00 | bovengrens: elke kans, geld overal tegelijk | 8.57 | €1,64 | €30.338,29 |
| Alle (met grijs) | €5.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 2.73 | €3,15 | €61.063,53 |

Bovengrens: elke kans met de helft van de inleg aan elke kant, alsof het geld op alle beurzen tegelijk staat (kan in het echt niet). Beste beurspaar: het paar is **achteraf** gekozen uit de metingen (vooraf kiezen levert minder op), en het model neemt aan dat je van elke munt al voorraad op de verkoopbeurs hebt.

Waarom dit te rooskleurig is (GOK): elke kans wordt maar één keer geteld met het mediane boek, maar andere bots pakken hem ook; de munt die je als voorraad aanhoudt kan dalen; na een paar kansen moet de voorraad terug (opnamekosten en tijd); minimale opname- en ordergroottes tellen niet mee; en een kans die we 2 minuten zagen staan, staat er niet per se nog als jouw order binnenkomt. Waarom het te somber kan zijn: niet alle kandidaten zijn gecontroleerd, en met voorraad op beide beurzen kun je dezelfde kans vaker pakken als het boek zich aanvult; dat telt hier niet mee.

## Wat houd je echt over? Voorraad op twee beurzen (simulatie)

Per beurspaar: geld en munten op beide beurzen, elke echte kans uitgevoerd tegen het boek zoals gemeten (niet meer dan de ruimte op het boek en niet meer dan de voorraad op die beurs), terugschuiven als een kant leeg dreigt te raken (met opnamekosten en tijd onderweg), en het koerseffect van de aangehouden munten apart. Netto = bruto min kosten terugschuiven plus koerseffect. **Gemeten** (GEZIEN): de kansen, het boek en de koersen; **de rest is een rekenmodel** (GOK, aannames onder de tabel). Geen advies.

**Met €150: netto €0,89 per dag op bitstamp - kraken (koerseffect erbovenop €0,35), €0,07 per dag op bitvavo - kraken (koerseffect erbovenop €-0,29), €0,19 per dag op gate - kucoin (koerseffect erbovenop €-0,95) (GOK: netto handel, rekenmodel op ±7.9 uur meting per dag, alleen MiCA).** "Per dag" is hier gemiddeld over 2 gemeten dagen achter elkaar; de eerste begint met een gelijk verdeelde voorraad; aan het eind staat de voorraad scheef, dus een volgende dag levert waarschijnlijk minder op, tenzij kansen de andere kant op hem terugbrengen (GOK).

### Alleen MiCA-beurzen (alle paren met echte kansen)

| Beurspaar | Inleg | Dag | Gemeten | Kansen | Gemist (geen voorraad) | Kleiner door voorraad | Bruto winst | Kosten terugschuiven | **Netto handel (bruto min kosten)** | Rendement handel | Koerseffect voorraad | Netto met koerseffect | Rendement met koerseffect |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| bitstamp - kraken | €100,00 | 2026-11-19 | 14.9 u | 2 | 1 | 1 | €1,18 | €0,00 (0x) | **€1,18** | 1.18% | €0,63 | €1,81 | 1.81% |
| bitstamp - kraken | €100,00 | 2026-11-20 | 0.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,16 | €-0,16 | -0.16% |
| bitstamp - kraken | €150,00 | 2026-11-19 | 14.9 u | 2 | 1 | 1 | €1,78 | €0,00 (0x) | **€1,78** | 1.18% | €0,94 | €2,72 | 1.81% |
| bitstamp - kraken | €150,00 | 2026-11-20 | 0.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,24 | €-0,24 | -0.16% |
| bitstamp - kraken | €200,00 | 2026-11-19 | 14.9 u | 2 | 1 | 1 | €2,37 | €0,00 (0x) | **€2,37** | 1.18% | €1,25 | €3,62 | 1.81% |
| bitstamp - kraken | €200,00 | 2026-11-20 | 0.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,32 | €-0,32 | -0.16% |
| bitstamp - kraken | €2.000,00 | 2026-11-19 | 14.9 u | 2 | 1 | 0 | €11,71 | €0,00 (0x) | **€11,71** | 0.59% | €12,53 | €24,24 | 1.21% |
| bitstamp - kraken | €2.000,00 | 2026-11-20 | 0.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,24 | €-3,24 | -0.16% |
| bitstamp - kraken | €5.000,00 | 2026-11-19 | 14.9 u | 2 | 1 | 0 | €11,71 | €0,00 (0x) | **€11,71** | 0.23% | €31,33 | €43,04 | 0.86% |
| bitstamp - kraken | €5.000,00 | 2026-11-20 | 0.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-8,10 | €-8,10 | -0.16% |
| bitvavo - kraken | €100,00 | 2026-11-19 | 14.9 u | 42 | 42 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,53 | €-0,53 | -0.53% |
| bitvavo - kraken | €100,00 | 2026-11-20 | 0.8 u | 1 | 1 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,15 | €0,15 | 0.15% |
| bitvavo - kraken | €150,00 | 2026-11-19 | 14.9 u | 42 | 36 | 6 | €0,14 | €0,00 (0x) | **€0,14** | 0.09% | €-0,80 | €-0,66 | -0.44% |
| bitvavo - kraken | €150,00 | 2026-11-20 | 0.8 u | 1 | 1 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,22 | €0,22 | 0.15% |
| bitvavo - kraken | €200,00 | 2026-11-19 | 14.9 u | 42 | 36 | 6 | €0,19 | €0,00 (0x) | **€0,19** | 0.09% | €-1,07 | €-0,88 | -0.44% |
| bitvavo - kraken | €200,00 | 2026-11-20 | 0.8 u | 1 | 1 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,29 | €0,29 | 0.15% |
| bitvavo - kraken | €2.000,00 | 2026-11-19 | 14.9 u | 42 | 26 | 16 | €14,65 | €7,37 (17x) | **€7,28** | 0.36% | €-10,61 | €-3,33 | -0.17% |
| bitvavo - kraken | €2.000,00 | 2026-11-20 | 0.8 u | 1 | 1 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €2,92 | €2,92 | 0.15% |
| bitvavo - kraken | €5.000,00 | 2026-11-19 | 14.9 u | 42 | 18 | 24 | €31,16 | €16,84 (26x) | **€14,32** | 0.29% | €-26,61 | €-12,29 | -0.25% |
| bitvavo - kraken | €5.000,00 | 2026-11-20 | 0.8 u | 1 | 0 | 1 | €0,48 | €0,98 (1x) | **€-0,50** | -0.01% | €7,36 | €6,86 | 0.14% |
| gate - kucoin | €100,00 | 2026-11-19 | 14.9 u | 24 | 16 | 8 | €0,25 | €0,00 (0x) | **€0,25** | 0.25% | €-1,10 | €-0,85 | -0.85% |
| gate - kucoin | €100,00 | 2026-11-20 | 0.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,17 | €-0,17 | -0.17% |
| gate - kucoin | €150,00 | 2026-11-19 | 14.9 u | 24 | 16 | 8 | €0,37 | €0,00 (0x) | **€0,37** | 0.25% | €-1,65 | €-1,27 | -0.85% |
| gate - kucoin | €150,00 | 2026-11-20 | 0.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,26 | €-0,26 | -0.17% |
| gate - kucoin | €200,00 | 2026-11-19 | 14.9 u | 24 | 16 | 8 | €0,50 | €0,00 (0x) | **€0,50** | 0.25% | €-2,19 | €-1,70 | -0.85% |
| gate - kucoin | €200,00 | 2026-11-20 | 0.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,35 | €-0,35 | -0.17% |
| gate - kucoin | €2.000,00 | 2026-11-19 | 14.9 u | 24 | 6 | 18 | €9,51 | €5,42 (19x) | **€4,09** | 0.20% | €-21,92 | €-17,83 | -0.89% |
| gate - kucoin | €2.000,00 | 2026-11-20 | 0.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,47 | €-3,47 | -0.17% |
| gate - kucoin | €5.000,00 | 2026-11-19 | 14.9 u | 24 | 5 | 14 | €19,13 | €5,05 (17x) | **€14,08** | 0.28% | €-54,82 | €-40,75 | -0.81% |
| gate - kucoin | €5.000,00 | 2026-11-20 | 0.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-8,69 | €-8,69 | -0.17% |

- bitstamp - kraken, €100,00: munten SKY; bruto zonder voorraadgrens zou €22,30 zijn, met voorraad €1,18 (GEZIEN boek, GOK model).
- bitstamp - kraken, €150,00: munten SKY; bruto zonder voorraadgrens zou €21,71 zijn, met voorraad €1,78 (GEZIEN boek, GOK model).
- bitstamp - kraken, €200,00: munten SKY; bruto zonder voorraadgrens zou €21,12 zijn, met voorraad €2,37 (GEZIEN boek, GOK model).
- bitstamp - kraken, €2.000,00: munten SKY; bruto zonder voorraadgrens zou €11,71 zijn, met voorraad €11,71 (GEZIEN boek, GOK model).
- bitstamp - kraken, €5.000,00: munten SKY; bruto zonder voorraadgrens zou €11,71 zijn, met voorraad €11,71 (GEZIEN boek, GOK model).
- bitvavo - kraken, €100,00: munten AVA, DYM, GMT, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €585,86 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitvavo - kraken, €150,00: munten AVA, DYM, GMT, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €585,45 zijn, met voorraad €0,14 (GEZIEN boek, GOK model).
- bitvavo - kraken, €200,00: munten AVA, DYM, GMT, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €585,32 zijn, met voorraad €0,19 (GEZIEN boek, GOK model).
- bitvavo - kraken, €2.000,00: munten AVA, DYM, GMT, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €565,62 zijn, met voorraad €14,65 (GEZIEN boek, GOK model).
- bitvavo - kraken, €5.000,00: munten AVA, DYM, GMT, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €532,11 zijn, met voorraad €31,64 (GEZIEN boek, GOK model).
- gate - kucoin, €100,00: munten ALKIMI, ERG, IR, LUNC, RARI, USTC, VERONA; bruto zonder voorraadgrens zou €75,85 zijn, met voorraad €0,25 (GEZIEN boek, GOK model).
- gate - kucoin, €150,00: munten ALKIMI, ERG, IR, LUNC, RARI, USTC, VERONA; bruto zonder voorraadgrens zou €75,85 zijn, met voorraad €0,37 (GEZIEN boek, GOK model).
- gate - kucoin, €200,00: munten ALKIMI, ERG, IR, LUNC, RARI, USTC, VERONA; bruto zonder voorraadgrens zou €75,85 zijn, met voorraad €0,50 (GEZIEN boek, GOK model).
- gate - kucoin, €2.000,00: munten ALKIMI, ERG, IR, LUNC, RARI, USTC, VERONA; bruto zonder voorraadgrens zou €73,19 zijn, met voorraad €9,51 (GEZIEN boek, GOK model).
- gate - kucoin, €5.000,00: munten ALKIMI, ERG, IR, LUNC, RARI, USTC, VERONA; bruto zonder voorraadgrens zou €70,08 zijn, met voorraad €19,13 (GEZIEN boek, GOK model).

### Met minstens één grijze beurs (de 5 paren met de meeste bruto winst)

| Beurspaar | Inleg | Dag | Gemeten | Kansen | Gemist (geen voorraad) | Kleiner door voorraad | Bruto winst | Kosten terugschuiven | **Netto handel (bruto min kosten)** | Rendement handel | Koerseffect voorraad | Netto met koerseffect | Rendement met koerseffect |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| kucoin - xt | €100,00 | 2026-11-19 | 14.9 u | 12 | 12 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,15 | €-0,15 | -0.15% |
| kucoin - xt | €100,00 | 2026-11-20 | 0.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,03 | €-0,03 | -0.03% |
| kucoin - xt | €150,00 | 2026-11-19 | 14.9 u | 12 | 9 | 3 | €0,35 | €0,00 (0x) | **€0,35** | 0.24% | €-0,22 | €0,13 | 0.09% |
| kucoin - xt | €150,00 | 2026-11-20 | 0.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,04 | €-0,04 | -0.03% |
| kucoin - xt | €200,00 | 2026-11-19 | 14.9 u | 12 | 9 | 3 | €0,47 | €0,00 (0x) | **€0,47** | 0.24% | €-0,30 | €0,18 | 0.09% |
| kucoin - xt | €200,00 | 2026-11-20 | 0.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,06 | €-0,06 | -0.03% |
| kucoin - xt | €2.000,00 | 2026-11-19 | 14.9 u | 12 | 3 | 9 | €14,56 | €5,16 (10x) | **€9,39** | 0.47% | €-2,94 | €6,45 | 0.32% |
| kucoin - xt | €2.000,00 | 2026-11-20 | 0.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,56 | €-0,56 | -0.03% |
| kucoin - xt | €5.000,00 | 2026-11-19 | 14.9 u | 12 | 2 | 9 | €29,75 | €4,82 (9x) | **€24,93** | 0.50% | €-7,39 | €17,55 | 0.35% |
| kucoin - xt | €5.000,00 | 2026-11-20 | 0.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,40 | €-1,40 | -0.03% |
| bitget - xt | €100,00 | 2026-11-19 | 14.9 u | 12 | 12 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €1,32 | €1,32 | 1.32% |
| bitget - xt | €100,00 | 2026-11-20 | 0.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €3,46 | €3,46 | 3.46% |
| bitget - xt | €150,00 | 2026-11-19 | 14.9 u | 12 | 9 | 3 | €0,49 | €0,11 (3x) | **€0,38** | 0.25% | €1,98 | €2,36 | 1.57% |
| bitget - xt | €150,00 | 2026-11-20 | 0.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €5,18 | €5,18 | 3.45% |
| bitget - xt | €200,00 | 2026-11-19 | 14.9 u | 12 | 9 | 3 | €0,65 | €0,11 (3x) | **€0,54** | 0.27% | €2,65 | €3,19 | 1.59% |
| bitget - xt | €200,00 | 2026-11-20 | 0.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €6,91 | €6,91 | 3.45% |
| bitget - xt | €2.000,00 | 2026-11-19 | 14.9 u | 12 | 4 | 7 | €11,59 | €1,85 (9x) | **€9,74** | 0.49% | €26,48 | €36,22 | 1.81% |
| bitget - xt | €2.000,00 | 2026-11-20 | 0.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €69,30 | €69,30 | 3.46% |
| bitget - xt | €5.000,00 | 2026-11-19 | 14.9 u | 12 | 4 | 6 | €21,85 | €1,84 (8x) | **€20,00** | 0.40% | €66,19 | €86,19 | 1.72% |
| bitget - xt | €5.000,00 | 2026-11-20 | 0.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €173,24 | €173,24 | 3.46% |
| bitget - gate | €100,00 | 2026-11-19 | 14.9 u | 14 | 14 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,85 | €0,85 | 0.85% |
| bitget - gate | €100,00 | 2026-11-20 | 0.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,39 | €0,39 | 0.39% |
| bitget - gate | €150,00 | 2026-11-19 | 14.9 u | 14 | 14 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €1,27 | €1,27 | 0.85% |
| bitget - gate | €150,00 | 2026-11-20 | 0.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,59 | €0,59 | 0.39% |
| bitget - gate | €200,00 | 2026-11-19 | 14.9 u | 14 | 13 | 1 | €0,18 | €0,00 (0x) | **€0,18** | 0.09% | €1,69 | €1,87 | 0.93% |
| bitget - gate | €200,00 | 2026-11-20 | 0.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,78 | €0,78 | 0.39% |
| bitget - gate | €2.000,00 | 2026-11-19 | 14.9 u | 14 | 4 | 10 | €10,38 | €2,20 (10x) | **€8,18** | 0.41% | €16,96 | €25,14 | 1.26% |
| bitget - gate | €2.000,00 | 2026-11-20 | 0.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €7,82 | €7,82 | 0.39% |
| bitget - gate | €5.000,00 | 2026-11-19 | 14.9 u | 14 | 4 | 8 | €20,16 | €3,49 (9x) | **€16,67** | 0.33% | €42,31 | €58,98 | 1.18% |
| bitget - gate | €5.000,00 | 2026-11-20 | 0.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €19,55 | €19,55 | 0.39% |
| htx - xt | €100,00 | 2026-11-19 | 14.9 u | 18 | 18 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,08 | €-0,08 | -0.08% |
| htx - xt | €100,00 | 2026-11-20 | 0.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,09 | €-0,09 | -0.09% |
| htx - xt | €150,00 | 2026-11-19 | 14.9 u | 18 | 18 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,12 | €-0,12 | -0.08% |
| htx - xt | €150,00 | 2026-11-20 | 0.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,14 | €-0,14 | -0.09% |
| htx - xt | €200,00 | 2026-11-19 | 14.9 u | 18 | 14 | 4 | €0,42 | €0,00 (0x) | **€0,42** | 0.21% | €-0,16 | €0,25 | 0.13% |
| htx - xt | €200,00 | 2026-11-20 | 0.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,19 | €-0,19 | -0.09% |
| htx - xt | €2.000,00 | 2026-11-19 | 14.9 u | 18 | 5 | 12 | €15,21 | €8,02 (15x) | **€7,19** | 0.36% | €-1,68 | €5,50 | 0.28% |
| htx - xt | €2.000,00 | 2026-11-20 | 0.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,87 | €-1,87 | -0.09% |
| htx - xt | €5.000,00 | 2026-11-19 | 14.9 u | 18 | 5 | 12 | €30,14 | €7,56 (14x) | **€22,58** | 0.45% | €-4,16 | €18,42 | 0.37% |
| htx - xt | €5.000,00 | 2026-11-20 | 0.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-4,69 | €-4,69 | -0.09% |
| gate - htx | €100,00 | 2026-11-19 | 14.9 u | 19 | 19 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,49 | €-0,49 | -0.49% |
| gate - htx | €100,00 | 2026-11-20 | 0.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,07 | €-0,07 | -0.07% |
| gate - htx | €150,00 | 2026-11-19 | 14.9 u | 19 | 19 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,74 | €-0,74 | -0.49% |
| gate - htx | €150,00 | 2026-11-20 | 0.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,11 | €-0,11 | -0.07% |
| gate - htx | €200,00 | 2026-11-19 | 14.9 u | 19 | 16 | 3 | €0,27 | €0,00 (0x) | **€0,27** | 0.13% | €-0,98 | €-0,72 | -0.36% |
| gate - htx | €200,00 | 2026-11-20 | 0.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,14 | €-0,14 | -0.07% |
| gate - htx | €2.000,00 | 2026-11-19 | 14.9 u | 19 | 6 | 13 | €13,80 | €4,51 (12x) | **€9,29** | 0.46% | €-9,86 | €-0,57 | -0.03% |
| gate - htx | €2.000,00 | 2026-11-20 | 0.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,43 | €-1,43 | -0.07% |
| gate - htx | €5.000,00 | 2026-11-19 | 14.9 u | 19 | 6 | 9 | €22,53 | €5,75 (12x) | **€16,79** | 0.34% | €-24,67 | €-7,88 | -0.16% |
| gate - htx | €5.000,00 | 2026-11-20 | 0.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,58 | €-3,58 | -0.07% |

- kucoin - xt, €100,00: munten DAG, FIGHT, LUNC; bruto zonder voorraadgrens zou €483,41 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- kucoin - xt, €150,00: munten DAG, FIGHT, LUNC; bruto zonder voorraadgrens zou €483,41 zijn, met voorraad €0,35 (GEZIEN boek, GOK model).
- kucoin - xt, €200,00: munten DAG, FIGHT, LUNC; bruto zonder voorraadgrens zou €483,41 zijn, met voorraad €0,47 (GEZIEN boek, GOK model).
- kucoin - xt, €2.000,00: munten DAG, FIGHT, LUNC; bruto zonder voorraadgrens zou €477,87 zijn, met voorraad €14,56 (GEZIEN boek, GOK model).
- kucoin - xt, €5.000,00: munten DAG, FIGHT, LUNC; bruto zonder voorraadgrens zou €470,01 zijn, met voorraad €29,75 (GEZIEN boek, GOK model).
- bitget - xt, €100,00: munten KOR, KUB, LUNC; bruto zonder voorraadgrens zou €464,05 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - xt, €150,00: munten KOR, KUB, LUNC; bruto zonder voorraadgrens zou €463,68 zijn, met voorraad €0,49 (GEZIEN boek, GOK model).
- bitget - xt, €200,00: munten KOR, KUB, LUNC; bruto zonder voorraadgrens zou €463,55 zijn, met voorraad €0,65 (GEZIEN boek, GOK model).
- bitget - xt, €2.000,00: munten KOR, KUB, LUNC; bruto zonder voorraadgrens zou €455,75 zijn, met voorraad €11,59 (GEZIEN boek, GOK model).
- bitget - xt, €5.000,00: munten KOR, KUB, LUNC; bruto zonder voorraadgrens zou €445,36 zijn, met voorraad €21,85 (GEZIEN boek, GOK model).
- bitget - gate, €100,00: munten BABYSHARK, IR, LUNC, RARE, SNEK, VERONA; bruto zonder voorraadgrens zou €81,03 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - gate, €150,00: munten BABYSHARK, IR, LUNC, RARE, SNEK, VERONA; bruto zonder voorraadgrens zou €81,03 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - gate, €200,00: munten BABYSHARK, IR, LUNC, RARE, SNEK, VERONA; bruto zonder voorraadgrens zou €81,03 zijn, met voorraad €0,18 (GEZIEN boek, GOK model).
- bitget - gate, €2.000,00: munten BABYSHARK, IR, LUNC, RARE, SNEK, VERONA; bruto zonder voorraadgrens zou €77,17 zijn, met voorraad €10,38 (GEZIEN boek, GOK model).
- bitget - gate, €5.000,00: munten BABYSHARK, IR, LUNC, RARE, SNEK, VERONA; bruto zonder voorraadgrens zou €72,95 zijn, met voorraad €20,16 (GEZIEN boek, GOK model).
- htx - xt, €100,00: munten CBK, LUNC, SEI, XDC; bruto zonder voorraadgrens zou €86,41 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - xt, €150,00: munten CBK, LUNC, SEI, XDC; bruto zonder voorraadgrens zou €86,41 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - xt, €200,00: munten CBK, LUNC, SEI, XDC; bruto zonder voorraadgrens zou €86,26 zijn, met voorraad €0,42 (GEZIEN boek, GOK model).
- htx - xt, €2.000,00: munten CBK, LUNC, SEI, XDC; bruto zonder voorraadgrens zou €82,76 zijn, met voorraad €15,21 (GEZIEN boek, GOK model).
- htx - xt, €5.000,00: munten CBK, LUNC, SEI, XDC; bruto zonder voorraadgrens zou €79,51 zijn, met voorraad €30,14 (GEZIEN boek, GOK model).
- gate - htx, €100,00: munten CBK, KAS, LUNC, SEI, WARD; bruto zonder voorraadgrens zou €58,03 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- gate - htx, €150,00: munten CBK, KAS, LUNC, SEI, WARD; bruto zonder voorraadgrens zou €58,03 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- gate - htx, €200,00: munten CBK, KAS, LUNC, SEI, WARD; bruto zonder voorraadgrens zou €58,03 zijn, met voorraad €0,27 (GEZIEN boek, GOK model).
- gate - htx, €2.000,00: munten CBK, KAS, LUNC, SEI, WARD; bruto zonder voorraadgrens zou €53,17 zijn, met voorraad €13,80 (GEZIEN boek, GOK model).
- gate - htx, €5.000,00: munten CBK, KAS, LUNC, SEI, WARD; bruto zonder voorraadgrens zou €49,90 zijn, met voorraad €22,53 (GEZIEN boek, GOK model).

### Andere keuzes bij bitvavo - kraken (netto handel, alle dagen samen; GOK)

| Keuze | Inleg | Kansen | Gemist | Bruto winst | Kosten terugschuiven | Netto handel |
|---|---|---|---|---|---|---|
| standaard (schuifdrempel 25%, kostengrens 1%) | €150,00 | 43 | 37 | €0,14 | €0,00 | **€0,14** |
| standaard (schuifdrempel 25%, kostengrens 1%) | €2.000,00 | 43 | 27 | €14,65 | €7,37 | **€7,28** |
| schuifdrempel 10% | €150,00 | 43 | 37 | €0,14 | €0,00 | **€0,14** |
| schuifdrempel 10% | €2.000,00 | 43 | 30 | €10,77 | €5,44 | **€5,32** |
| schuifdrempel 40% | €150,00 | 43 | 37 | €0,14 | €0,00 | **€0,14** |
| schuifdrempel 40% | €2.000,00 | 43 | 27 | €11,83 | €7,04 | **€4,78** |
| kostengrens 2% (achteraf vergeleken) | €150,00 | 43 | 37 | €0,14 | €0,00 | **€0,14** |
| kostengrens 2% (achteraf vergeleken) | €2.000,00 | 43 | 19 | €14,71 | €17,81 | **€-3,11** |
| kostengrens 5% (achteraf vergeleken) | €150,00 | 43 | 34 | €0,18 | €2,48 | **€-2,31** |
| kostengrens 5% (achteraf vergeleken) | €2.000,00 | 43 | 19 | €14,71 | €17,81 | **€-3,11** |
| alleen MERL en GMT (meer voorraad per munt, achteraf gekozen) | €150,00 | 28 | 26 | €0,19 | €0,00 | **€0,19** |
| alleen MERL en GMT (meer voorraad per munt, achteraf gekozen) | €2.000,00 | 28 | 15 | €20,78 | €14,45 | **€6,32** |

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
- Geld terugschuiven per beurs: bitget USDT: 1 USDT, GOK (1 USDT, 30 min; niet nagekeken); bitstamp USD: 1 USD, GOK (1 USD, 24 uur; niet nagekeken); bitvavo EUR: 0 EUR, kosten GEZIEN (api.bitvavo.com/v2/assets: EUR withdrawalFee 0), tijd GOK (1 werkdag, SEPA), minimum 0 EUR (GEZIEN, api.bitvavo.com/v2/assets withdrawalMinAmount); gate USDT: 1 USDT, GOK (1 USDT, 30 min; niet nagekeken), minimum 1 USDT (GEZIEN, api.gateio.ws/api/v4/wallet/currency_chains withdraw_amount_min); htx USDT: 1 USDT, GOK (1 USDT, 30 min; niet nagekeken); kraken EUR: 1 EUR, kosten GEZIEN (support.kraken.com/articles/360000381846: Instant SEPA, Banking Circle, 1 EUR, near-instant), tijd GOK (1 uur tot het op de andere beurs staat), minimum 2 EUR (GEZIEN, support.kraken.com/articles/360000381846 Instant SEPA (Banking Circle)); kraken USD: 1 USD, GOK (1 USD, 24 uur; niet nagekeken); kucoin USDT: 1 USDT, kosten GEZIEN (api.kucoin.com/api/v3/currencies/USDT: BEP20 1 USDT), tijd GOK, minimum 5 USDT (GEZIEN, api.kucoin.com/api/v3/currencies/USDT BEP20 withdrawalMinSize); xt USDT: 1 USDT, GOK (1 USDT, 30 min; niet nagekeken).

## Over de meting

- Opnamekosten bij de echte kansen: 49 van een netwerk dat aan beide kanten open is, 70 van de beurs zelf (laagste open netwerk), 16 geschat uit wat andere beurzen voor die munt vragen (GOK). Onbekende opnamekosten tellen niet als echte kans.
- Netwerk: KuCoin, Gate, Bitget, HTX, XT, Bitstamp, Bitvavo en Poloniex geven hun netwerken per munt. Als beide beurzen dat doen en de namen te koppelen zijn, moet er een netwerk zijn dat aan beide kanten open is. Anders is het netwerk "niet te koppelen" en telt de kans mee (staat apart in de trechter).
- De duur is gemeten in stappen van ±20 seconden; een kans kan een paar rondes eerder begonnen zijn dan we zagen.
- Takerkosten: uit de API waar die ze per paar geeft, anders het standaardtarief uit de README (deels GOK).
- Laatste run: 15 beurzen antwoordden, 2287 munt-quote-paren op minstens twee beurzen (GEZIEN).
