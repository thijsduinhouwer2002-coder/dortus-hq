# Rapport koersverschil-scanner

Gemaakt 2026-11-19 22:47 UTC uit 17 runs, samen ±13.8 uur gemeten (GEZIEN).
Echte kans = winst na alle kosten (opnamekosten bekend), opnemen en storten open (en een netwerk dat aan beide kanten open is, als de beurzen dat geven), minstens €100,00 op het boek, minstens 2 minuten blijven staan, geen andere munt met dezelfde naam.
**Vergund** = beide beurzen hebben een MiCA-vergunning (ESMA-register), vaak via een EU-dochter die minder munten kan hebben dan de wereldwijde API die we meten (GOK). **Grijs** = minstens één beurs zonder vergunning (MEXC, Bitget, HTX, Poloniex, XT, Bitfinex, Binance). Zie README.md.
**Kraken-tarief:** Kraken rekent 0,80% taker op munt tegen EUR, USD, USDT of USDC (GEZIEN, kraken.com/pro/fees, laagste trede); de scanner rekende tot 19 nov met 0,40%. 399 opgeslagen kansen met Kraken uit die runs zijn hier **opnieuw doorgerekend met 0,80%** (GOK-benadering: 0,40% van de inzet aan de Kraken-kant extra op elk gemeten punt van het boek; het boek zelf is niet bewaard). 233 houden daarna nog winst op het boek. Dat ze met hogere kosten ook korter bleven staan, telt niet mee (dus eerder te gunstig).

## Hoeveel wordt er gecontroleerd? (GEZIEN, stand.jsonl)

Per ronde (mediaan over 165 metingen): 1060 kandidaten (verschil op de ticker groter dan de takerkosten), 120 met het orderboek gecontroleerd, 3 nog nooit gecontroleerd (0%).
Bijna alle kandidaten komen aan de beurt; de aantallen hieronder missen weinig.

## Trechter (GEZIEN, eigen metingen)

| Stap | Alle beurzen | Alleen MiCA-beurzen | Met minstens één grijze beurs |
|---|---|---|---|
| Verschillen met winst op het boek na alle kosten | 13057 | 1833 | 11224 |
| ...waarvan opnemen of storten dicht | 3117 | 291 | 2826 |
| ...waarvan status onbekend (beurs geeft het niet openbaar) | 7604 | 1281 | 6323 |
| Opnemen en storten open | 2336 | 261 | 2075 |
| ...en geen netwerk dat aan beide kanten open is: valt af | 36 | 2 | 34 |
| ...en opnamekosten onbekend: valt af | 0 | 0 | 0 |
| ...en minstens €100,00 op het boek | 671 | 146 | 525 |
| ...en minstens 2 minuten blijven staan | 220 | 75 | 145 |
| ...en geen andere munt met dezelfde naam | 194 | 64 | 130 |
|    ...waarvan contractadres bekend en gelijk | 15 | 2 | 13 |
|    ...waarvan contractadres onbekend (telt mee, kan een andere munt zijn) | 179 | 62 | 117 |
|    ...waarvan netwerk gekoppeld en open | 113 | 20 | 93 |
|    ...waarvan netwerk niet te koppelen (telt mee) | 81 | 44 | 37 |
| **Echte kansen** (zelfde munt overlappend in de tijd samengevoegd, beste beurspaar telt) | 124 | 64 | 79 |
| Ter vergelijking: zelfde eisen, maar opnamestatus onbekend (niet meegeteld) | 412 | 97 | 356 |

## Echte kansen per dag (GEZIEN)

| Dag | Echt, alleen MiCA | Echt, met grijs | Mediane winst per kans bij €500 (MiCA / grijs) | Mediane duur |
|---|---|---|---|---|
| 2026-11-19 | 45 | 79 | €2,02 / €1,20 | 5.3 min |
| Totaal | 45 | 79 | €2,02 / €1,20 | 5.3 min |

## Beste munten (GEZIEN)

| | Soort | Kansen | Som winst bij €500 per kans |
|---|---|---|---|
| MERL-EUR | vergund | 14 | €149,78 |
| LUNC-USDT | grijs | 9 | €45,13 |
| USTC-USDT | grijs | 7 | €27,56 |
| SKY-USD | vergund | 2 | €21,52 |
| YB-USDT | grijs | 1 | €16,34 |
| GMT-EUR | vergund | 12 | €14,55 |
| WAN-USDT | grijs | 4 | €14,24 |
| VERONA-USDT | grijs | 8 | €13,53 |
| AVA-EUR | vergund | 4 | €11,22 |
| LUNA-EUR | vergund | 4 | €10,37 |

## Beste beursparen (kopen op > verkopen op) (GEZIEN)

| | Soort | Kansen | Som winst bij €500 per kans |
|---|---|---|---|
| bitvavo > kraken | vergund | 41 | €189,88 |
| kucoin > bitget | grijs | 10 | €28,27 |
| kucoin > htx | grijs | 12 | €24,35 |
| bitget > gate | grijs | 6 | €23,63 |
| bitget > xt | grijs | 7 | €22,78 |
| bitstamp > kraken | vergund | 2 | €21,52 |
| gate > xt | grijs | 2 | €19,11 |
| bitget > htx | grijs | 15 | €11,71 |
| kucoin > xt | grijs | 3 | €10,44 |
| bitget > kucoin | grijs | 8 | €7,31 |

Beurzen die het vaakst meedoen (koop of verkoop): bitget (grijs) 48, kraken 43, bitvavo 41, kucoin 40, htx (grijs) 37, xt (grijs) 18, gate 16, poloniex (grijs) 3 (GEZIEN).

## Hoeveel kansen blijven staan terwijl je geld schuift? (GEZIEN, duur uit eigen metingen)

Wie geen voorraad op beide beurzen heeft, moet kopen, de munt opnemen, wachten tot hij binnen is en dan verkopen. Hoe lang dat duurt verschilt per munt en netwerk: een paar minuten (snelle ketens) tot een uur of meer (Bitcoin, beurzen die opnames met de hand keuren) (GOK, niet per munt gemeten).

| Overmaaktijd | Alle beurzen | Alleen MiCA-beurzen | Met minstens één grijze beurs |
|---|---|---|---|
| 5 min | 66 van 124 (53%) | 33 van 64 (52%) | 41 van 79 (52%) |
| 10 min | 38 van 124 (31%) | 21 van 64 (33%) | 22 van 79 (28%) |
| 30 min | 26 van 124 (21%) | 16 van 64 (25%) | 13 van 79 (16%) |
| 60 min | 11 van 124 (9%) | 7 van 64 (11%) | 6 van 79 (8%) |

## Wat zou het opleveren over 3 maanden? (GOK, doorgetrokken uit de metingen)

Gemeten over ±13.8 uur (GEZIEN), doorgetrokken naar 90 dagen (GOK: aanname dat de week die we maten gewoon is).

| Beurzen | Inleg | Model | Kansen per uur | Per kans (mediaan) | 3 maanden |
|---|---|---|---|---|---|
| Alleen MiCA | €2.000,00 | bovengrens: elke kans, geld overal tegelijk | 4.65 | €2,73 | €27.423,19 |
| Alleen MiCA | €2.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 2.98 | €3,10 | €47.950,17 |
| Alleen MiCA | €5.000,00 | bovengrens: elke kans, geld overal tegelijk | 4.65 | €3,05 | €30.694,57 |
| Alleen MiCA | €5.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 2.98 | €3,41 | €69.669,53 |
| Alle (met grijs) | €2.000,00 | bovengrens: elke kans, geld overal tegelijk | 9.02 | €1,61 | €31.384,71 |
| Alle (met grijs) | €2.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 2.98 | €3,10 | €47.950,17 |
| Alle (met grijs) | €5.000,00 | bovengrens: elke kans, geld overal tegelijk | 9.02 | €2,11 | €41.031,43 |
| Alle (met grijs) | €5.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 2.98 | €3,41 | €69.669,53 |

Bovengrens: elke kans met de helft van de inleg aan elke kant, alsof het geld op alle beurzen tegelijk staat (kan in het echt niet). Beste beurspaar: het paar is **achteraf** gekozen uit de metingen (vooraf kiezen levert minder op), en het model neemt aan dat je van elke munt al voorraad op de verkoopbeurs hebt.

Waarom dit te rooskleurig is (GOK): elke kans wordt maar één keer geteld met het mediane boek, maar andere bots pakken hem ook; de munt die je als voorraad aanhoudt kan dalen; na een paar kansen moet de voorraad terug (opnamekosten en tijd); minimale opname- en ordergroottes tellen niet mee; en een kans die we 2 minuten zagen staan, staat er niet per se nog als jouw order binnenkomt. Waarom het te somber kan zijn: niet alle kandidaten zijn gecontroleerd, en met voorraad op beide beurzen kun je dezelfde kans vaker pakken als het boek zich aanvult; dat telt hier niet mee.

## Wat houd je echt over? Voorraad op twee beurzen (simulatie)

Per beurspaar: geld en munten op beide beurzen, elke echte kans uitgevoerd tegen het boek zoals gemeten (niet meer dan de ruimte op het boek en niet meer dan de voorraad op die beurs), terugschuiven als een kant leeg dreigt te raken (met opnamekosten en tijd onderweg), en het koerseffect van de aangehouden munten apart. Netto = bruto min kosten terugschuiven plus koerseffect. **Gemeten** (GEZIEN): de kansen, het boek en de koersen; **de rest is een rekenmodel** (GOK, aannames onder de tabel). Geen advies.

**Met €150: netto €1,78 per dag op bitstamp - kraken (koerseffect erbovenop €1,46), €0,14 per dag op bitvavo - kraken (koerseffect erbovenop €-0,93), €0,39 per dag op gate - kucoin (koerseffect erbovenop €-1,51) (GOK: netto handel, rekenmodel op ±13.8 uur meting per dag, alleen MiCA).** "Per dag" is hier één gemeten dag die begint met een gelijk verdeelde voorraad; aan het eind staat de voorraad scheef, dus een volgende dag levert waarschijnlijk minder op, tenzij kansen de andere kant op hem terugbrengen (GOK).

### Alleen MiCA-beurzen (alle paren met echte kansen)

| Beurspaar | Inleg | Dag | Gemeten | Kansen | Gemist (geen voorraad) | Kleiner door voorraad | Bruto winst | Kosten terugschuiven | **Netto handel (bruto min kosten)** | Rendement handel | Koerseffect voorraad | Netto met koerseffect | Rendement met koerseffect |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| bitstamp - kraken | €100,00 | 2026-11-19 | 13.8 u | 2 | 1 | 1 | €1,18 | €0,00 (0x) | **€1,18** | 1.18% | €0,97 | €2,16 | 2.16% |
| bitstamp - kraken | €150,00 | 2026-11-19 | 13.8 u | 2 | 1 | 1 | €1,78 | €0,00 (0x) | **€1,78** | 1.18% | €1,46 | €3,23 | 2.16% |
| bitstamp - kraken | €200,00 | 2026-11-19 | 13.8 u | 2 | 1 | 1 | €2,37 | €0,00 (0x) | **€2,37** | 1.18% | €1,94 | €4,31 | 2.16% |
| bitstamp - kraken | €2.000,00 | 2026-11-19 | 13.8 u | 2 | 1 | 0 | €11,71 | €0,00 (0x) | **€11,71** | 0.59% | €19,45 | €31,15 | 1.56% |
| bitstamp - kraken | €5.000,00 | 2026-11-19 | 13.8 u | 2 | 1 | 0 | €11,71 | €0,00 (0x) | **€11,71** | 0.23% | €48,62 | €60,32 | 1.21% |
| bitvavo - kraken | €100,00 | 2026-11-19 | 13.8 u | 41 | 41 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,62 | €-0,62 | -0.62% |
| bitvavo - kraken | €150,00 | 2026-11-19 | 13.8 u | 41 | 35 | 6 | €0,14 | €0,00 (0x) | **€0,14** | 0.09% | €-0,93 | €-0,79 | -0.53% |
| bitvavo - kraken | €200,00 | 2026-11-19 | 13.8 u | 41 | 35 | 6 | €0,19 | €0,00 (0x) | **€0,19** | 0.09% | €-1,24 | €-1,06 | -0.53% |
| bitvavo - kraken | €2.000,00 | 2026-11-19 | 13.8 u | 41 | 25 | 16 | €14,65 | €7,37 (17x) | **€7,28** | 0.36% | €-12,37 | €-5,09 | -0.25% |
| bitvavo - kraken | €5.000,00 | 2026-11-19 | 13.8 u | 41 | 18 | 23 | €30,48 | €15,89 (25x) | **€14,59** | 0.29% | €-31,03 | €-16,44 | -0.33% |
| gate - kucoin | €100,00 | 2026-11-19 | 13.8 u | 21 | 14 | 7 | €0,26 | €0,00 (0x) | **€0,26** | 0.26% | €-1,00 | €-0,74 | -0.74% |
| gate - kucoin | €150,00 | 2026-11-19 | 13.8 u | 21 | 14 | 7 | €0,39 | €0,00 (0x) | **€0,39** | 0.26% | €-1,51 | €-1,11 | -0.74% |
| gate - kucoin | €200,00 | 2026-11-19 | 13.8 u | 21 | 14 | 7 | €0,52 | €0,00 (0x) | **€0,52** | 0.26% | €-2,01 | €-1,48 | -0.74% |
| gate - kucoin | €2.000,00 | 2026-11-19 | 13.8 u | 21 | 6 | 15 | €9,30 | €4,54 (16x) | **€4,76** | 0.24% | €-20,10 | €-15,34 | -0.77% |
| gate - kucoin | €5.000,00 | 2026-11-19 | 13.8 u | 21 | 4 | 12 | €19,37 | €4,17 (14x) | **€15,20** | 0.30% | €-50,22 | €-35,01 | -0.70% |

- bitstamp - kraken, €100,00: munten SKY; bruto zonder voorraadgrens zou €22,30 zijn, met voorraad €1,18 (GEZIEN boek, GOK model).
- bitstamp - kraken, €150,00: munten SKY; bruto zonder voorraadgrens zou €21,71 zijn, met voorraad €1,78 (GEZIEN boek, GOK model).
- bitstamp - kraken, €200,00: munten SKY; bruto zonder voorraadgrens zou €21,12 zijn, met voorraad €2,37 (GEZIEN boek, GOK model).
- bitstamp - kraken, €2.000,00: munten SKY; bruto zonder voorraadgrens zou €11,71 zijn, met voorraad €11,71 (GEZIEN boek, GOK model).
- bitstamp - kraken, €5.000,00: munten SKY; bruto zonder voorraadgrens zou €11,71 zijn, met voorraad €11,71 (GEZIEN boek, GOK model).
- bitvavo - kraken, €100,00: munten AVA, DYM, GMT, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €582,16 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitvavo - kraken, €150,00: munten AVA, DYM, GMT, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €581,76 zijn, met voorraad €0,14 (GEZIEN boek, GOK model).
- bitvavo - kraken, €200,00: munten AVA, DYM, GMT, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €581,62 zijn, met voorraad €0,19 (GEZIEN boek, GOK model).
- bitvavo - kraken, €2.000,00: munten AVA, DYM, GMT, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €561,93 zijn, met voorraad €14,65 (GEZIEN boek, GOK model).
- bitvavo - kraken, €5.000,00: munten AVA, DYM, GMT, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €528,42 zijn, met voorraad €30,48 (GEZIEN boek, GOK model).
- gate - kucoin, €100,00: munten ALKIMI, ERG, IR, LUNC, USTC, VERONA; bruto zonder voorraadgrens zou €73,19 zijn, met voorraad €0,26 (GEZIEN boek, GOK model).
- gate - kucoin, €150,00: munten ALKIMI, ERG, IR, LUNC, USTC, VERONA; bruto zonder voorraadgrens zou €73,19 zijn, met voorraad €0,39 (GEZIEN boek, GOK model).
- gate - kucoin, €200,00: munten ALKIMI, ERG, IR, LUNC, USTC, VERONA; bruto zonder voorraadgrens zou €73,19 zijn, met voorraad €0,52 (GEZIEN boek, GOK model).
- gate - kucoin, €2.000,00: munten ALKIMI, ERG, IR, LUNC, USTC, VERONA; bruto zonder voorraadgrens zou €70,08 zijn, met voorraad €9,30 (GEZIEN boek, GOK model).
- gate - kucoin, €5.000,00: munten ALKIMI, ERG, IR, LUNC, USTC, VERONA; bruto zonder voorraadgrens zou €66,64 zijn, met voorraad €19,37 (GEZIEN boek, GOK model).

### Met minstens één grijze beurs (de 5 paren met de meeste bruto winst)

| Beurspaar | Inleg | Dag | Gemeten | Kansen | Gemist (geen voorraad) | Kleiner door voorraad | Bruto winst | Kosten terugschuiven | **Netto handel (bruto min kosten)** | Rendement handel | Koerseffect voorraad | Netto met koerseffect | Rendement met koerseffect |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| kucoin - xt | €100,00 | 2026-11-19 | 13.8 u | 12 | 12 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,42 | €-0,42 | -0.42% |
| kucoin - xt | €150,00 | 2026-11-19 | 13.8 u | 12 | 9 | 3 | €0,35 | €0,00 (0x) | **€0,35** | 0.24% | €-0,64 | €-0,28 | -0.19% |
| kucoin - xt | €200,00 | 2026-11-19 | 13.8 u | 12 | 9 | 3 | €0,47 | €0,00 (0x) | **€0,47** | 0.24% | €-0,85 | €-0,38 | -0.19% |
| kucoin - xt | €2.000,00 | 2026-11-19 | 13.8 u | 12 | 3 | 9 | €14,56 | €5,16 (10x) | **€9,39** | 0.47% | €-8,44 | €0,95 | 0.05% |
| kucoin - xt | €5.000,00 | 2026-11-19 | 13.8 u | 12 | 2 | 9 | €29,75 | €4,82 (9x) | **€24,93** | 0.50% | €-21,17 | €3,76 | 0.08% |
| bitget - xt | €100,00 | 2026-11-19 | 13.8 u | 11 | 11 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €1,42 | €1,42 | 1.42% |
| bitget - xt | €150,00 | 2026-11-19 | 13.8 u | 11 | 8 | 3 | €0,49 | €0,11 (3x) | **€0,38** | 0.25% | €2,14 | €2,51 | 1.68% |
| bitget - xt | €200,00 | 2026-11-19 | 13.8 u | 11 | 8 | 3 | €0,65 | €0,11 (3x) | **€0,54** | 0.27% | €2,85 | €3,39 | 1.69% |
| bitget - xt | €2.000,00 | 2026-11-19 | 13.8 u | 11 | 4 | 6 | €10,37 | €1,84 (8x) | **€8,53** | 0.43% | €28,49 | €37,02 | 1.85% |
| bitget - xt | €5.000,00 | 2026-11-19 | 13.8 u | 11 | 4 | 5 | €19,95 | €1,84 (7x) | **€18,11** | 0.36% | €71,23 | €89,34 | 1.79% |
| bitget - gate | €100,00 | 2026-11-19 | 13.8 u | 13 | 13 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €1,35 | €1,35 | 1.35% |
| bitget - gate | €150,00 | 2026-11-19 | 13.8 u | 13 | 13 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €2,03 | €2,03 | 1.35% |
| bitget - gate | €200,00 | 2026-11-19 | 13.8 u | 13 | 8 | 5 | €0,75 | €0,01 (2x) | **€0,75** | 0.37% | €2,70 | €3,45 | 1.72% |
| bitget - gate | €2.000,00 | 2026-11-19 | 13.8 u | 13 | 4 | 9 | €11,01 | €3,11 (11x) | **€7,90** | 0.40% | €27,08 | €34,98 | 1.75% |
| bitget - gate | €5.000,00 | 2026-11-19 | 13.8 u | 13 | 3 | 8 | €20,55 | €1,99 (8x) | **€18,56** | 0.37% | €67,61 | €86,17 | 1.72% |
| htx - xt | €100,00 | 2026-11-19 | 13.8 u | 17 | 17 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,02 | €0,02 | 0.02% |
| htx - xt | €150,00 | 2026-11-19 | 13.8 u | 17 | 17 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,03 | €0,03 | 0.02% |
| htx - xt | €200,00 | 2026-11-19 | 13.8 u | 17 | 13 | 4 | €0,42 | €0,00 (0x) | **€0,42** | 0.21% | €0,04 | €0,46 | 0.23% |
| htx - xt | €2.000,00 | 2026-11-19 | 13.8 u | 17 | 5 | 11 | €13,54 | €6,72 (13x) | **€6,82** | 0.34% | €0,31 | €7,13 | 0.36% |
| htx - xt | €5.000,00 | 2026-11-19 | 13.8 u | 17 | 5 | 11 | €26,46 | €7,17 (13x) | **€19,29** | 0.39% | €0,87 | €20,17 | 0.40% |
| bitget - kucoin | €100,00 | 2026-11-19 | 13.8 u | 20 | 20 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,22 | €-1,22 | -1.22% |
| bitget - kucoin | €150,00 | 2026-11-19 | 13.8 u | 20 | 20 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,83 | €-1,83 | -1.22% |
| bitget - kucoin | €200,00 | 2026-11-19 | 13.8 u | 20 | 20 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,45 | €-2,45 | -1.22% |
| bitget - kucoin | €2.000,00 | 2026-11-19 | 13.8 u | 20 | 8 | 12 | €5,63 | €2,16 (11x) | **€3,47** | 0.17% | €-24,45 | €-20,98 | -1.05% |
| bitget - kucoin | €5.000,00 | 2026-11-19 | 13.8 u | 20 | 8 | 10 | €11,74 | €8,41 (18x) | **€3,33** | 0.07% | €-61,10 | €-57,77 | -1.16% |

- kucoin - xt, €100,00: munten DAG, FIGHT, LUNC; bruto zonder voorraadgrens zou €483,41 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- kucoin - xt, €150,00: munten DAG, FIGHT, LUNC; bruto zonder voorraadgrens zou €483,41 zijn, met voorraad €0,35 (GEZIEN boek, GOK model).
- kucoin - xt, €200,00: munten DAG, FIGHT, LUNC; bruto zonder voorraadgrens zou €483,41 zijn, met voorraad €0,47 (GEZIEN boek, GOK model).
- kucoin - xt, €2.000,00: munten DAG, FIGHT, LUNC; bruto zonder voorraadgrens zou €477,87 zijn, met voorraad €14,56 (GEZIEN boek, GOK model).
- kucoin - xt, €5.000,00: munten DAG, FIGHT, LUNC; bruto zonder voorraadgrens zou €470,01 zijn, met voorraad €29,75 (GEZIEN boek, GOK model).
- bitget - xt, €100,00: munten KOR, KUB, LUNC; bruto zonder voorraadgrens zou €461,52 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - xt, €150,00: munten KOR, KUB, LUNC; bruto zonder voorraadgrens zou €461,15 zijn, met voorraad €0,49 (GEZIEN boek, GOK model).
- bitget - xt, €200,00: munten KOR, KUB, LUNC; bruto zonder voorraadgrens zou €461,02 zijn, met voorraad €0,65 (GEZIEN boek, GOK model).
- bitget - xt, €2.000,00: munten KOR, KUB, LUNC; bruto zonder voorraadgrens zou €453,21 zijn, met voorraad €10,37 (GEZIEN boek, GOK model).
- bitget - xt, €5.000,00: munten KOR, KUB, LUNC; bruto zonder voorraadgrens zou €442,83 zijn, met voorraad €19,95 (GEZIEN boek, GOK model).
- bitget - gate, €100,00: munten BABYSHARK, IR, LUNC, RARE, VERONA; bruto zonder voorraadgrens zou €78,30 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - gate, €150,00: munten BABYSHARK, IR, LUNC, RARE, VERONA; bruto zonder voorraadgrens zou €78,30 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - gate, €200,00: munten BABYSHARK, IR, LUNC, RARE, VERONA; bruto zonder voorraadgrens zou €77,96 zijn, met voorraad €0,75 (GEZIEN boek, GOK model).
- bitget - gate, €2.000,00: munten BABYSHARK, IR, LUNC, RARE, VERONA; bruto zonder voorraadgrens zou €73,67 zijn, met voorraad €11,01 (GEZIEN boek, GOK model).
- bitget - gate, €5.000,00: munten BABYSHARK, IR, LUNC, RARE, VERONA; bruto zonder voorraadgrens zou €69,59 zijn, met voorraad €20,55 (GEZIEN boek, GOK model).
- htx - xt, €100,00: munten CBK, LUNC, SEI, XDC; bruto zonder voorraadgrens zou €71,90 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - xt, €150,00: munten CBK, LUNC, SEI, XDC; bruto zonder voorraadgrens zou €71,90 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - xt, €200,00: munten CBK, LUNC, SEI, XDC; bruto zonder voorraadgrens zou €71,75 zijn, met voorraad €0,42 (GEZIEN boek, GOK model).
- htx - xt, €2.000,00: munten CBK, LUNC, SEI, XDC; bruto zonder voorraadgrens zou €68,25 zijn, met voorraad €13,54 (GEZIEN boek, GOK model).
- htx - xt, €5.000,00: munten CBK, LUNC, SEI, XDC; bruto zonder voorraadgrens zou €65,01 zijn, met voorraad €26,46 (GEZIEN boek, GOK model).
- bitget - kucoin, €100,00: munten EGL1, KLV, LUNC, MTX, USDT, USTC, VERONA; bruto zonder voorraadgrens zou €53,28 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - kucoin, €150,00: munten EGL1, KLV, LUNC, MTX, USDT, USTC, VERONA; bruto zonder voorraadgrens zou €53,28 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - kucoin, €200,00: munten EGL1, KLV, LUNC, MTX, USDT, USTC, VERONA; bruto zonder voorraadgrens zou €53,28 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - kucoin, €2.000,00: munten EGL1, KLV, LUNC, MTX, USDT, USTC, VERONA; bruto zonder voorraadgrens zou €50,46 zijn, met voorraad €5,63 (GEZIEN boek, GOK model).
- bitget - kucoin, €5.000,00: munten EGL1, KLV, LUNC, MTX, USDT, USTC, VERONA; bruto zonder voorraadgrens zou €47,23 zijn, met voorraad €11,74 (GEZIEN boek, GOK model).

### Andere keuzes bij bitvavo - kraken (netto handel, alle dagen samen; GOK)

| Keuze | Inleg | Kansen | Gemist | Bruto winst | Kosten terugschuiven | Netto handel |
|---|---|---|---|---|---|---|
| standaard (schuifdrempel 25%, kostengrens 1%) | €150,00 | 41 | 35 | €0,14 | €0,00 | **€0,14** |
| standaard (schuifdrempel 25%, kostengrens 1%) | €2.000,00 | 41 | 25 | €14,65 | €7,37 | **€7,28** |
| schuifdrempel 10% | €150,00 | 41 | 35 | €0,14 | €0,00 | **€0,14** |
| schuifdrempel 10% | €2.000,00 | 41 | 28 | €10,77 | €5,44 | **€5,32** |
| schuifdrempel 40% | €150,00 | 41 | 35 | €0,14 | €0,00 | **€0,14** |
| schuifdrempel 40% | €2.000,00 | 41 | 25 | €11,83 | €7,04 | **€4,78** |
| kostengrens 2% (achteraf vergeleken) | €150,00 | 41 | 35 | €0,14 | €0,00 | **€0,14** |
| kostengrens 2% (achteraf vergeleken) | €2.000,00 | 41 | 19 | €14,21 | €15,89 | **€-1,68** |
| kostengrens 5% (achteraf vergeleken) | €150,00 | 41 | 32 | €0,18 | €2,48 | **€-2,31** |
| kostengrens 5% (achteraf vergeleken) | €2.000,00 | 41 | 19 | €14,21 | €15,89 | **€-1,68** |
| alleen MERL en GMT (meer voorraad per munt, achteraf gekozen) | €150,00 | 26 | 24 | €0,19 | €0,00 | **€0,19** |
| alleen MERL en GMT (meer voorraad per munt, achteraf gekozen) | €2.000,00 | 26 | 15 | €19,93 | €12,50 | **€7,43** |

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
- Geld terugschuiven per beurs: bitget EUR: 1 EUR, GOK (1 EUR, 24 uur; niet nagekeken); bitget USDT: 1 USDT, GOK (1 USDT, 30 min; niet nagekeken); bitstamp USD: 1 USD, GOK (1 USD, 24 uur; niet nagekeken); bitvavo EUR: 0 EUR, kosten GEZIEN (api.bitvavo.com/v2/assets: EUR withdrawalFee 0), tijd GOK (1 werkdag, SEPA), minimum 0 EUR (GEZIEN, api.bitvavo.com/v2/assets withdrawalMinAmount); gate USDT: 1 USDT, GOK (1 USDT, 30 min; niet nagekeken), minimum 1 USDT (GEZIEN, api.gateio.ws/api/v4/wallet/currency_chains withdraw_amount_min); htx USDT: 1 USDT, GOK (1 USDT, 30 min; niet nagekeken); kraken EUR: 1 EUR, kosten GEZIEN (support.kraken.com/articles/360000381846: Instant SEPA, Banking Circle, 1 EUR, near-instant), tijd GOK (1 uur tot het op de andere beurs staat), minimum 2 EUR (GEZIEN, support.kraken.com/articles/360000381846 Instant SEPA (Banking Circle)); kraken USD: 1 USD, GOK (1 USD, 24 uur; niet nagekeken); kucoin EUR: 1 EUR, GOK (1 EUR, 24 uur; niet nagekeken); kucoin USDT: 1 USDT, kosten GEZIEN (api.kucoin.com/api/v3/currencies/USDT: BEP20 1 USDT), tijd GOK, minimum 5 USDT (GEZIEN, api.kucoin.com/api/v3/currencies/USDT BEP20 withdrawalMinSize); xt USDT: 1 USDT, GOK (1 USDT, 30 min; niet nagekeken).

## Over de meting

- Opnamekosten bij de echte kansen: 48 van een netwerk dat aan beide kanten open is, 64 van de beurs zelf (laagste open netwerk), 12 geschat uit wat andere beurzen voor die munt vragen (GOK). Onbekende opnamekosten tellen niet als echte kans.
- Netwerk: KuCoin, Gate, Bitget, HTX, XT, Bitstamp, Bitvavo en Poloniex geven hun netwerken per munt. Als beide beurzen dat doen en de namen te koppelen zijn, moet er een netwerk zijn dat aan beide kanten open is. Anders is het netwerk "niet te koppelen" en telt de kans mee (staat apart in de trechter).
- De duur is gemeten in stappen van ±20 seconden; een kans kan een paar rondes eerder begonnen zijn dan we zagen.
- Takerkosten: uit de API waar die ze per paar geeft, anders het standaardtarief uit de README (deels GOK).
- Laatste run: 15 beurzen antwoordden, 2286 munt-quote-paren op minstens twee beurzen (GEZIEN).
