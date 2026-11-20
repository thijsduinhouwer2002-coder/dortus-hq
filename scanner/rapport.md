# Rapport koersverschil-scanner

Gemaakt 2026-11-20 08:20 UTC uit 18 runs, samen ±22.8 uur gemeten (GEZIEN).
Echte kans = winst na alle kosten (opnamekosten bekend), opnemen en storten open (en een netwerk dat aan beide kanten open is, als de beurzen dat geven), minstens €100,00 op het boek, minstens 2 minuten blijven staan, geen andere munt met dezelfde naam.
**Vergund** = beide beurzen hebben een MiCA-vergunning (ESMA-register), vaak via een EU-dochter die minder munten kan hebben dan de wereldwijde API die we meten (GOK). **Grijs** = minstens één beurs zonder vergunning (MEXC, Bitget, HTX, Poloniex, XT, Bitfinex, Binance). Zie README.md.
**Kraken-tarief:** Kraken rekent 0,80% taker op munt tegen EUR, USD, USDT of USDC (GEZIEN, kraken.com/pro/fees, laagste trede); de scanner rekende tot 19 nov met 0,40%. 399 opgeslagen kansen met Kraken uit die runs zijn hier **opnieuw doorgerekend met 0,80%** (GOK-benadering: 0,40% van de inzet aan de Kraken-kant extra op elk gemeten punt van het boek; het boek zelf is niet bewaard). 233 houden daarna nog winst op het boek. Dat ze met hogere kosten ook korter bleven staan, telt niet mee (dus eerder te gunstig).

## Hoeveel wordt er gecontroleerd? (GEZIEN, stand.jsonl)

Per ronde (mediaan over 274 metingen): 1100 kandidaten (verschil op de ticker groter dan de takerkosten), 120 met het orderboek gecontroleerd, 2 nog nooit gecontroleerd (0%).
Bijna alle kandidaten komen aan de beurt; de aantallen hieronder missen weinig.

## Trechter (GEZIEN, eigen metingen)

| Stap | Alle beurzen | Alleen MiCA-beurzen | Met minstens één grijze beurs |
|---|---|---|---|
| Verschillen met winst op het boek na alle kosten | 19571 | 2922 | 16649 |
| ...waarvan opnemen of storten dicht | 4448 | 450 | 3998 |
| ...waarvan status onbekend (beurs geeft het niet openbaar) | 11427 | 2075 | 9352 |
| Opnemen en storten open | 3696 | 397 | 3299 |
| ...en geen netwerk dat aan beide kanten open is: valt af | 98 | 3 | 95 |
| ...en opnamekosten onbekend: valt af | 0 | 0 | 0 |
| ...en minstens €100,00 op het boek | 1028 | 205 | 823 |
| ...en minstens 2 minuten blijven staan | 326 | 101 | 225 |
| ...en geen andere munt met dezelfde naam | 296 | 89 | 207 |
|    ...waarvan contractadres bekend en gelijk | 31 | 10 | 21 |
|    ...waarvan contractadres onbekend (telt mee, kan een andere munt zijn) | 265 | 79 | 186 |
|    ...waarvan netwerk gekoppeld en open | 185 | 34 | 151 |
|    ...waarvan netwerk niet te koppelen (telt mee) | 111 | 55 | 56 |
| **Echte kansen** (zelfde munt overlappend in de tijd samengevoegd, beste beurspaar telt) | 188 | 89 | 122 |
| Ter vergelijking: zelfde eisen, maar opnamestatus onbekend (niet meegeteld) | 670 | 159 | 576 |

## Echte kansen per dag (GEZIEN)

| Dag | Echt, alleen MiCA | Echt, met grijs | Mediane winst per kans bij €500 (MiCA / grijs) | Mediane duur |
|---|---|---|---|---|
| 2026-11-19 | 49 | 86 | €2,00 / €1,21 | 5.3 min |
| 2026-11-20 | 17 | 36 | €0,61 / €1,91 | 7.7 min |
| Totaal | 66 | 122 | €1,57 / €1,31 | 6.0 min |

## Beste munten (GEZIEN)

| | Soort | Kansen | Som winst bij €500 per kans |
|---|---|---|---|
| MERL-EUR | vergund | 16 | €180,26 |
| LUNC-USDT | grijs | 13 | €56,21 |
| MEME-USDT | grijs | 1 | €37,90 |
| USTC-USDT | grijs en vergund | 9 | €31,70 |
| SKY-USD | vergund | 2 | €21,52 |
| LAT-USDT | grijs | 3 | €17,59 |
| YB-USDT | grijs | 2 | €17,52 |
| GMT-EUR | vergund | 20 | €17,13 |
| WAN-USDT | grijs | 5 | €16,06 |
| VERONA-USDT | grijs | 9 | €13,96 |

## Beste beursparen (kopen op > verkopen op) (GEZIEN)

| | Soort | Kansen | Som winst bij €500 per kans |
|---|---|---|---|
| bitvavo > kraken | vergund | 51 | €222,93 |
| bitget > htx | grijs | 26 | €62,90 |
| kucoin > htx | grijs | 20 | €55,35 |
| kucoin > bitget | grijs | 12 | €35,86 |
| bitget > xt | grijs | 11 | €35,79 |
| bitget > gate | grijs | 7 | €24,32 |
| bitstamp > kraken | vergund | 2 | €21,52 |
| gate > kucoin | vergund | 9 | €19,60 |
| gate > xt | grijs | 2 | €19,11 |
| bitget > kucoin | grijs | 12 | €16,85 |

Beurzen die het vaakst meedoen (koop of verkoop): bitget (grijs) 74, kucoin 69, htx (grijs) 62, kraken 53, bitvavo 51, gate 34, xt (grijs) 24, poloniex (grijs) 7 (GEZIEN).

## Hoeveel kansen blijven staan terwijl je geld schuift? (GEZIEN, duur uit eigen metingen)

Wie geen voorraad op beide beurzen heeft, moet kopen, de munt opnemen, wachten tot hij binnen is en dan verkopen. Hoe lang dat duurt verschilt per munt en netwerk: een paar minuten (snelle ketens) tot een uur of meer (Bitcoin, beurzen die opnames met de hand keuren) (GOK, niet per munt gemeten).

| Overmaaktijd | Alle beurzen | Alleen MiCA-beurzen | Met minstens één grijze beurs |
|---|---|---|---|
| 5 min | 114 van 188 (61%) | 51 van 89 (57%) | 72 van 122 (59%) |
| 10 min | 70 van 188 (37%) | 32 van 89 (36%) | 44 van 122 (36%) |
| 30 min | 41 van 188 (22%) | 18 van 89 (20%) | 27 van 122 (22%) |
| 60 min | 17 van 188 (9%) | 9 van 89 (10%) | 11 van 122 (9%) |

## Wat zou het opleveren over 3 maanden? (GOK, doorgetrokken uit de metingen)

Gemeten over ±22.8 uur (GEZIEN), doorgetrokken naar 90 dagen (GOK: aanname dat de week die we maten gewoon is).

| Beurzen | Inleg | Model | Kansen per uur | Per kans (mediaan) | 3 maanden |
|---|---|---|---|---|---|
| Alleen MiCA | €2.000,00 | bovengrens: elke kans, geld overal tegelijk | 3.90 | €2,18 | €18.317,14 |
| Alleen MiCA | €2.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 2.23 | €2,53 | €34.565,17 |
| Alleen MiCA | €5.000,00 | bovengrens: elke kans, geld overal tegelijk | 3.90 | €2,29 | €19.311,42 |
| Alleen MiCA | €5.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 2.23 | €2,92 | €50.838,67 |
| Alle (met grijs) | €2.000,00 | bovengrens: elke kans, geld overal tegelijk | 8.23 | €1,59 | €28.252,36 |
| Alle (met grijs) | €2.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 2.23 | €2,53 | €34.565,17 |
| Alle (met grijs) | €5.000,00 | bovengrens: elke kans, geld overal tegelijk | 8.23 | €1,80 | €32.008,31 |
| Alle (met grijs) | €5.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 2.23 | €2,92 | €50.838,67 |

Bovengrens: elke kans met de helft van de inleg aan elke kant, alsof het geld op alle beurzen tegelijk staat (kan in het echt niet). Beste beurspaar: het paar is **achteraf** gekozen uit de metingen (vooraf kiezen levert minder op), en het model neemt aan dat je van elke munt al voorraad op de verkoopbeurs hebt.

Waarom dit te rooskleurig is (GOK): elke kans wordt maar één keer geteld met het mediane boek, maar andere bots pakken hem ook; de munt die je als voorraad aanhoudt kan dalen; na een paar kansen moet de voorraad terug (opnamekosten en tijd); minimale opname- en ordergroottes tellen niet mee; en een kans die we 2 minuten zagen staan, staat er niet per se nog als jouw order binnenkomt. Waarom het te somber kan zijn: niet alle kandidaten zijn gecontroleerd, en met voorraad op beide beurzen kun je dezelfde kans vaker pakken als het boek zich aanvult; dat telt hier niet mee.

## Wat houd je echt over? Voorraad op twee beurzen (simulatie)

Per beurspaar: geld en munten op beide beurzen, elke echte kans uitgevoerd tegen het boek zoals gemeten (niet meer dan de ruimte op het boek en niet meer dan de voorraad op die beurs), terugschuiven als een kant leeg dreigt te raken (met opnamekosten en tijd onderweg), en het koerseffect van de aangehouden munten apart. Netto = bruto min kosten terugschuiven plus koerseffect. **Gemeten** (GEZIEN): de kansen, het boek en de koersen; **de rest is een rekenmodel** (GOK, aannames onder de tabel). Geen advies.

**Met €150: netto €0,89 per dag op bitstamp - kraken (koerseffect erbovenop €-2,81), €0,07 per dag op bitvavo - kraken (koerseffect erbovenop €-1,28), €0,36 per dag op gate - kucoin (koerseffect erbovenop €0,07) (GOK: netto handel, rekenmodel op ±11.4 uur meting per dag, alleen MiCA).** "Per dag" is hier gemiddeld over 2 gemeten dagen achter elkaar; de eerste begint met een gelijk verdeelde voorraad; aan het eind staat de voorraad scheef, dus een volgende dag levert waarschijnlijk minder op, tenzij kansen de andere kant op hem terugbrengen (GOK).

### Alleen MiCA-beurzen (alle paren met echte kansen)

| Beurspaar | Inleg | Dag | Gemeten | Kansen | Gemist (geen voorraad) | Kleiner door voorraad | Bruto winst | Kosten terugschuiven | **Netto handel (bruto min kosten)** | Rendement handel | Koerseffect voorraad | Netto met koerseffect | Rendement met koerseffect |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| bitstamp - kraken | €100,00 | 2026-11-19 | 14.9 u | 2 | 1 | 1 | €1,18 | €0,00 (0x) | **€1,18** | 1.18% | €0,63 | €1,81 | 1.81% |
| bitstamp - kraken | €100,00 | 2026-11-20 | 7.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-4,38 | €-4,38 | -4.38% |
| bitstamp - kraken | €150,00 | 2026-11-19 | 14.9 u | 2 | 1 | 1 | €1,78 | €0,00 (0x) | **€1,78** | 1.18% | €0,94 | €2,72 | 1.81% |
| bitstamp - kraken | €150,00 | 2026-11-20 | 7.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-6,56 | €-6,56 | -4.38% |
| bitstamp - kraken | €200,00 | 2026-11-19 | 14.9 u | 2 | 1 | 1 | €2,37 | €0,00 (0x) | **€2,37** | 1.18% | €1,25 | €3,62 | 1.81% |
| bitstamp - kraken | €200,00 | 2026-11-20 | 7.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-8,75 | €-8,75 | -4.38% |
| bitstamp - kraken | €2.000,00 | 2026-11-19 | 14.9 u | 2 | 1 | 0 | €11,71 | €0,00 (0x) | **€11,71** | 0.59% | €12,53 | €24,24 | 1.21% |
| bitstamp - kraken | €2.000,00 | 2026-11-20 | 7.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-87,51 | €-87,51 | -4.38% |
| bitstamp - kraken | €5.000,00 | 2026-11-19 | 14.9 u | 2 | 1 | 0 | €11,71 | €0,00 (0x) | **€11,71** | 0.23% | €31,33 | €43,04 | 0.86% |
| bitstamp - kraken | €5.000,00 | 2026-11-20 | 7.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-218,78 | €-218,78 | -4.38% |
| bitvavo - kraken | €100,00 | 2026-11-19 | 14.9 u | 43 | 43 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,53 | €-0,53 | -0.53% |
| bitvavo - kraken | €100,00 | 2026-11-20 | 7.9 u | 8 | 8 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,18 | €-1,18 | -1.18% |
| bitvavo - kraken | €150,00 | 2026-11-19 | 14.9 u | 43 | 37 | 6 | €0,14 | €0,00 (0x) | **€0,14** | 0.09% | €-0,80 | €-0,66 | -0.44% |
| bitvavo - kraken | €150,00 | 2026-11-20 | 7.9 u | 8 | 8 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,77 | €-1,77 | -1.18% |
| bitvavo - kraken | €200,00 | 2026-11-19 | 14.9 u | 43 | 37 | 6 | €0,19 | €0,00 (0x) | **€0,19** | 0.09% | €-1,07 | €-0,88 | -0.44% |
| bitvavo - kraken | €200,00 | 2026-11-20 | 7.9 u | 8 | 8 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,36 | €-2,36 | -1.18% |
| bitvavo - kraken | €2.000,00 | 2026-11-19 | 14.9 u | 43 | 26 | 17 | €16,97 | €7,69 (18x) | **€9,28** | 0.46% | €-10,61 | €-1,33 | -0.07% |
| bitvavo - kraken | €2.000,00 | 2026-11-20 | 7.9 u | 8 | 7 | 1 | €2,59 | €0,32 (1x) | **€2,27** | 0.11% | €-23,42 | €-21,15 | -1.06% |
| bitvavo - kraken | €5.000,00 | 2026-11-19 | 14.9 u | 43 | 18 | 25 | €36,95 | €17,21 (27x) | **€19,74** | 0.39% | €-26,61 | €-6,86 | -0.14% |
| bitvavo - kraken | €5.000,00 | 2026-11-20 | 7.9 u | 8 | 1 | 7 | €9,71 | €8,22 (9x) | **€1,49** | 0.03% | €-58,65 | €-57,16 | -1.14% |
| gate - kucoin | €100,00 | 2026-11-19 | 14.9 u | 25 | 25 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,40 | €0,40 | 0.40% |
| gate - kucoin | €100,00 | 2026-11-20 | 7.9 u | 11 | 10 | 1 | €0,10 | €0,00 (1x) | **€0,10** | 0.10% | €-0,30 | €-0,20 | -0.20% |
| gate - kucoin | €150,00 | 2026-11-19 | 14.9 u | 25 | 17 | 8 | €0,22 | €0,00 (0x) | **€0,22** | 0.14% | €0,60 | €0,81 | 0.54% |
| gate - kucoin | €150,00 | 2026-11-20 | 7.9 u | 11 | 4 | 7 | €0,51 | €0,02 (2x) | **€0,50** | 0.33% | €-0,45 | €0,05 | 0.03% |
| gate - kucoin | €200,00 | 2026-11-19 | 14.9 u | 25 | 17 | 8 | €0,29 | €0,00 (0x) | **€0,29** | 0.14% | €0,79 | €1,08 | 0.54% |
| gate - kucoin | €200,00 | 2026-11-20 | 7.9 u | 11 | 4 | 7 | €0,68 | €0,02 (2x) | **€0,67** | 0.33% | €-0,60 | €0,07 | 0.03% |
| gate - kucoin | €2.000,00 | 2026-11-19 | 14.9 u | 25 | 6 | 19 | €6,15 | €4,85 (18x) | **€1,31** | 0.07% | €7,94 | €9,24 | 0.46% |
| gate - kucoin | €2.000,00 | 2026-11-20 | 7.9 u | 11 | 2 | 9 | €7,10 | €0,72 (6x) | **€6,39** | 0.32% | €-5,85 | €0,54 | 0.03% |
| gate - kucoin | €5.000,00 | 2026-11-19 | 14.9 u | 25 | 6 | 18 | €14,93 | €5,78 (20x) | **€9,15** | 0.18% | €19,89 | €29,04 | 0.58% |
| gate - kucoin | €5.000,00 | 2026-11-20 | 7.9 u | 11 | 2 | 9 | €14,97 | €2,45 (9x) | **€12,52** | 0.25% | €-14,70 | €-2,18 | -0.04% |

- bitstamp - kraken, €100,00: munten SKY; bruto zonder voorraadgrens zou €22,30 zijn, met voorraad €1,18 (GEZIEN boek, GOK model).
- bitstamp - kraken, €150,00: munten SKY; bruto zonder voorraadgrens zou €21,71 zijn, met voorraad €1,78 (GEZIEN boek, GOK model).
- bitstamp - kraken, €200,00: munten SKY; bruto zonder voorraadgrens zou €21,12 zijn, met voorraad €2,37 (GEZIEN boek, GOK model).
- bitstamp - kraken, €2.000,00: munten SKY; bruto zonder voorraadgrens zou €11,71 zijn, met voorraad €11,71 (GEZIEN boek, GOK model).
- bitstamp - kraken, €5.000,00: munten SKY; bruto zonder voorraadgrens zou €11,71 zijn, met voorraad €11,71 (GEZIEN boek, GOK model).
- bitvavo - kraken, €100,00: munten AVA, DYM, GMT, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €701,47 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitvavo - kraken, €150,00: munten AVA, DYM, GMT, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €701,06 zijn, met voorraad €0,14 (GEZIEN boek, GOK model).
- bitvavo - kraken, €200,00: munten AVA, DYM, GMT, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €700,93 zijn, met voorraad €0,19 (GEZIEN boek, GOK model).
- bitvavo - kraken, €2.000,00: munten AVA, DYM, GMT, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €681,23 zijn, met voorraad €19,57 (GEZIEN boek, GOK model).
- bitvavo - kraken, €5.000,00: munten AVA, DYM, GMT, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €647,72 zijn, met voorraad €46,66 (GEZIEN boek, GOK model).
- gate - kucoin, €100,00: munten ALKIMI, AVAIL, CHR, ERG, FTT, IKA, IR, LUNC, NIM, RARI, USTC, VERONA; bruto zonder voorraadgrens zou €111,24 zijn, met voorraad €0,10 (GEZIEN boek, GOK model).
- gate - kucoin, €150,00: munten ALKIMI, AVAIL, CHR, ERG, FTT, IKA, IR, LUNC, NIM, RARI, USTC, VERONA; bruto zonder voorraadgrens zou €111,21 zijn, met voorraad €0,73 (GEZIEN boek, GOK model).
- gate - kucoin, €200,00: munten ALKIMI, AVAIL, CHR, ERG, FTT, IKA, IR, LUNC, NIM, RARI, USTC, VERONA; bruto zonder voorraadgrens zou €111,19 zijn, met voorraad €0,97 (GEZIEN boek, GOK model).
- gate - kucoin, €2.000,00: munten ALKIMI, AVAIL, CHR, ERG, FTT, IKA, IR, LUNC, NIM, RARI, USTC, VERONA; bruto zonder voorraadgrens zou €109,20 zijn, met voorraad €13,26 (GEZIEN boek, GOK model).
- gate - kucoin, €5.000,00: munten ALKIMI, AVAIL, CHR, ERG, FTT, IKA, IR, LUNC, NIM, RARI, USTC, VERONA; bruto zonder voorraadgrens zou €106,78 zijn, met voorraad €29,90 (GEZIEN boek, GOK model).

### Met minstens één grijze beurs (de 5 paren met de meeste bruto winst)

| Beurspaar | Inleg | Dag | Gemeten | Kansen | Gemist (geen voorraad) | Kleiner door voorraad | Bruto winst | Kosten terugschuiven | **Netto handel (bruto min kosten)** | Rendement handel | Koerseffect voorraad | Netto met koerseffect | Rendement met koerseffect |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| htx - xt | €100,00 | 2026-11-19 | 14.9 u | 18 | 18 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,61 | €-0,61 | -0.61% |
| htx - xt | €100,00 | 2026-11-20 | 7.9 u | 6 | 6 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,94 | €-0,94 | -0.94% |
| htx - xt | €150,00 | 2026-11-19 | 14.9 u | 18 | 18 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,91 | €-0,91 | -0.61% |
| htx - xt | €150,00 | 2026-11-20 | 7.9 u | 6 | 6 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,41 | €-1,41 | -0.94% |
| htx - xt | €200,00 | 2026-11-19 | 14.9 u | 18 | 18 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,22 | €-1,22 | -0.61% |
| htx - xt | €200,00 | 2026-11-20 | 7.9 u | 6 | 6 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,88 | €-1,88 | -0.94% |
| htx - xt | €2.000,00 | 2026-11-19 | 14.9 u | 18 | 5 | 13 | €9,30 | €5,28 (12x) | **€4,01** | 0.20% | €-12,20 | €-8,19 | -0.41% |
| htx - xt | €2.000,00 | 2026-11-20 | 7.9 u | 6 | 0 | 6 | €13,80 | €1,18 (3x) | **€12,63** | 0.63% | €-18,58 | €-5,95 | -0.30% |
| htx - xt | €5.000,00 | 2026-11-19 | 14.9 u | 18 | 5 | 12 | €19,47 | €6,65 (13x) | **€12,82** | 0.26% | €-30,43 | €-17,61 | -0.35% |
| htx - xt | €5.000,00 | 2026-11-20 | 7.9 u | 6 | 0 | 6 | €33,24 | €2,11 (4x) | **€31,14** | 0.62% | €-46,83 | €-15,69 | -0.31% |
| kucoin - xt | €100,00 | 2026-11-19 | 14.9 u | 13 | 13 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,15 | €-0,15 | -0.15% |
| kucoin - xt | €100,00 | 2026-11-20 | 7.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,80 | €-0,80 | -0.80% |
| kucoin - xt | €150,00 | 2026-11-19 | 14.9 u | 13 | 10 | 3 | €0,35 | €0,00 (0x) | **€0,35** | 0.24% | €-0,22 | €0,13 | 0.09% |
| kucoin - xt | €150,00 | 2026-11-20 | 7.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,20 | €-1,20 | -0.80% |
| kucoin - xt | €200,00 | 2026-11-19 | 14.9 u | 13 | 10 | 3 | €0,47 | €0,00 (0x) | **€0,47** | 0.24% | €-0,30 | €0,18 | 0.09% |
| kucoin - xt | €200,00 | 2026-11-20 | 7.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,60 | €-1,60 | -0.80% |
| kucoin - xt | €2.000,00 | 2026-11-19 | 14.9 u | 13 | 3 | 10 | €16,57 | €6,42 (12x) | **€10,15** | 0.51% | €-2,95 | €7,20 | 0.36% |
| kucoin - xt | €2.000,00 | 2026-11-20 | 7.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-15,90 | €-15,90 | -0.79% |
| kucoin - xt | €5.000,00 | 2026-11-19 | 14.9 u | 13 | 2 | 10 | €34,70 | €5,17 (10x) | **€29,54** | 0.59% | €-7,39 | €22,14 | 0.44% |
| kucoin - xt | €5.000,00 | 2026-11-20 | 7.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-39,89 | €-39,89 | -0.80% |
| bitget - xt | €100,00 | 2026-11-19 | 14.9 u | 13 | 13 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €2,41 | €2,41 | 2.41% |
| bitget - xt | €100,00 | 2026-11-20 | 7.9 u | 2 | 2 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,69 | €-2,69 | -2.69% |
| bitget - xt | €150,00 | 2026-11-19 | 14.9 u | 13 | 13 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €3,61 | €3,61 | 2.41% |
| bitget - xt | €150,00 | 2026-11-20 | 7.9 u | 2 | 1 | 1 | €0,08 | €0,00 (0x) | **€0,08** | 0.05% | €-4,04 | €-3,97 | -2.64% |
| bitget - xt | €200,00 | 2026-11-19 | 14.9 u | 13 | 9 | 4 | €0,62 | €0,12 (4x) | **€0,50** | 0.25% | €4,81 | €5,31 | 2.66% |
| bitget - xt | €200,00 | 2026-11-20 | 7.9 u | 2 | 2 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-5,37 | €-5,37 | -2.69% |
| bitget - xt | €2.000,00 | 2026-11-19 | 14.9 u | 13 | 5 | 7 | €9,59 | €1,95 (10x) | **€7,64** | 0.38% | €48,12 | €55,76 | 2.79% |
| bitget - xt | €2.000,00 | 2026-11-20 | 7.9 u | 2 | 0 | 2 | €1,45 | €0,55 (2x) | **€0,90** | 0.04% | €-53,88 | €-52,98 | -2.65% |
| bitget - xt | €5.000,00 | 2026-11-19 | 14.9 u | 13 | 4 | 7 | €19,03 | €1,84 (9x) | **€17,19** | 0.34% | €120,30 | €137,49 | 2.75% |
| bitget - xt | €5.000,00 | 2026-11-20 | 7.9 u | 2 | 0 | 2 | €2,72 | €0,55 (2x) | **€2,16** | 0.04% | €-134,74 | €-132,58 | -2.65% |
| gate - htx | €100,00 | 2026-11-19 | 14.9 u | 19 | 19 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,97 | €-0,97 | -0.97% |
| gate - htx | €100,00 | 2026-11-20 | 7.9 u | 12 | 12 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,57 | €-1,57 | -1.57% |
| gate - htx | €150,00 | 2026-11-19 | 14.9 u | 19 | 19 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,46 | €-1,46 | -0.97% |
| gate - htx | €150,00 | 2026-11-20 | 7.9 u | 12 | 12 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,36 | €-2,36 | -1.57% |
| gate - htx | €200,00 | 2026-11-19 | 14.9 u | 19 | 19 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,95 | €-1,95 | -0.97% |
| gate - htx | €200,00 | 2026-11-20 | 7.9 u | 12 | 12 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,15 | €-3,15 | -1.57% |
| gate - htx | €2.000,00 | 2026-11-19 | 14.9 u | 19 | 6 | 13 | €6,88 | €4,51 (12x) | **€2,37** | 0.12% | €-19,49 | €-17,12 | -0.86% |
| gate - htx | €2.000,00 | 2026-11-20 | 7.9 u | 12 | 2 | 10 | €10,12 | €1,89 (8x) | **€8,23** | 0.41% | €-31,23 | €-23,00 | -1.15% |
| gate - htx | €5.000,00 | 2026-11-19 | 14.9 u | 19 | 6 | 10 | €15,55 | €5,59 (13x) | **€9,96** | 0.20% | €-48,72 | €-38,76 | -0.78% |
| gate - htx | €5.000,00 | 2026-11-20 | 7.9 u | 12 | 2 | 9 | €24,83 | €2,61 (9x) | **€22,22** | 0.44% | €-78,42 | €-56,20 | -1.12% |
| htx - kucoin | €100,00 | 2026-11-19 | 14.9 u | 16 | 16 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,76 | €-2,76 | -2.76% |
| htx - kucoin | €100,00 | 2026-11-20 | 7.9 u | 13 | 13 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,66 | €-1,66 | -1.66% |
| htx - kucoin | €150,00 | 2026-11-19 | 14.9 u | 16 | 16 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-4,14 | €-4,14 | -2.76% |
| htx - kucoin | €150,00 | 2026-11-20 | 7.9 u | 13 | 13 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,49 | €-2,49 | -1.66% |
| htx - kucoin | €200,00 | 2026-11-19 | 14.9 u | 16 | 16 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-5,51 | €-5,51 | -2.76% |
| htx - kucoin | €200,00 | 2026-11-20 | 7.9 u | 13 | 13 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,32 | €-3,32 | -1.66% |
| htx - kucoin | €2.000,00 | 2026-11-19 | 14.9 u | 16 | 7 | 9 | €3,96 | €1,18 (6x) | **€2,78** | 0.14% | €-55,07 | €-52,29 | -2.61% |
| htx - kucoin | €2.000,00 | 2026-11-20 | 7.9 u | 13 | 4 | 9 | €8,62 | €0,93 (5x) | **€7,69** | 0.38% | €-33,13 | €-25,45 | -1.27% |
| htx - kucoin | €5.000,00 | 2026-11-19 | 14.9 u | 16 | 3 | 13 | €12,30 | €4,43 (13x) | **€7,87** | 0.16% | €-137,77 | €-129,90 | -2.60% |
| htx - kucoin | €5.000,00 | 2026-11-20 | 7.9 u | 13 | 0 | 13 | €24,51 | €3,82 (11x) | **€20,69** | 0.41% | €-82,77 | €-62,07 | -1.24% |

- htx - xt, €100,00: munten BSV, CBK, LUNC, MEME, SEI, XCH, XDC; bruto zonder voorraadgrens zou €149,66 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - xt, €150,00: munten BSV, CBK, LUNC, MEME, SEI, XCH, XDC; bruto zonder voorraadgrens zou €149,66 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - xt, €200,00: munten BSV, CBK, LUNC, MEME, SEI, XCH, XDC; bruto zonder voorraadgrens zou €149,66 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - xt, €2.000,00: munten BSV, CBK, LUNC, MEME, SEI, XCH, XDC; bruto zonder voorraadgrens zou €147,37 zijn, met voorraad €23,10 (GEZIEN boek, GOK model).
- htx - xt, €5.000,00: munten BSV, CBK, LUNC, MEME, SEI, XCH, XDC; bruto zonder voorraadgrens zou €145,08 zijn, met voorraad €52,72 (GEZIEN boek, GOK model).
- kucoin - xt, €100,00: munten DAG, FIGHT, LUNC; bruto zonder voorraadgrens zou €549,84 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- kucoin - xt, €150,00: munten DAG, FIGHT, LUNC; bruto zonder voorraadgrens zou €549,84 zijn, met voorraad €0,35 (GEZIEN boek, GOK model).
- kucoin - xt, €200,00: munten DAG, FIGHT, LUNC; bruto zonder voorraadgrens zou €549,84 zijn, met voorraad €0,47 (GEZIEN boek, GOK model).
- kucoin - xt, €2.000,00: munten DAG, FIGHT, LUNC; bruto zonder voorraadgrens zou €544,29 zijn, met voorraad €16,57 (GEZIEN boek, GOK model).
- kucoin - xt, €5.000,00: munten DAG, FIGHT, LUNC; bruto zonder voorraadgrens zou €536,43 zijn, met voorraad €34,70 (GEZIEN boek, GOK model).
- bitget - xt, €100,00: munten KOR, KUB, LUNC, YB; bruto zonder voorraadgrens zou €594,29 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - xt, €150,00: munten KOR, KUB, LUNC, YB; bruto zonder voorraadgrens zou €594,29 zijn, met voorraad €0,08 (GEZIEN boek, GOK model).
- bitget - xt, €200,00: munten KOR, KUB, LUNC, YB; bruto zonder voorraadgrens zou €593,76 zijn, met voorraad €0,62 (GEZIEN boek, GOK model).
- bitget - xt, €2.000,00: munten KOR, KUB, LUNC, YB; bruto zonder voorraadgrens zou €587,79 zijn, met voorraad €11,04 (GEZIEN boek, GOK model).
- bitget - xt, €5.000,00: munten KOR, KUB, LUNC, YB; bruto zonder voorraadgrens zou €579,74 zijn, met voorraad €21,75 (GEZIEN boek, GOK model).
- gate - htx, €100,00: munten BSV, CBK, KAS, LAT, LUNC, MEME, MOVR, SEI, WARD, WLD; bruto zonder voorraadgrens zou €121,82 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- gate - htx, €150,00: munten BSV, CBK, KAS, LAT, LUNC, MEME, MOVR, SEI, WARD, WLD; bruto zonder voorraadgrens zou €121,82 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- gate - htx, €200,00: munten BSV, CBK, KAS, LAT, LUNC, MEME, MOVR, SEI, WARD, WLD; bruto zonder voorraadgrens zou €121,82 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- gate - htx, €2.000,00: munten BSV, CBK, KAS, LAT, LUNC, MEME, MOVR, SEI, WARD, WLD; bruto zonder voorraadgrens zou €118,41 zijn, met voorraad €17,00 (GEZIEN boek, GOK model).
- gate - htx, €5.000,00: munten BSV, CBK, KAS, LAT, LUNC, MEME, MOVR, SEI, WARD, WLD; bruto zonder voorraadgrens zou €113,91 zijn, met voorraad €40,38 (GEZIEN boek, GOK model).
- htx - kucoin, €100,00: munten BSV, CHIP, FET, LAT, LUNC, MEME, MOVR, ONE, SOMI, WAN, WARD, WLD, XCH, XEC; bruto zonder voorraadgrens zou €119,39 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - kucoin, €150,00: munten BSV, CHIP, FET, LAT, LUNC, MEME, MOVR, ONE, SOMI, WAN, WARD, WLD, XCH, XEC; bruto zonder voorraadgrens zou €119,39 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - kucoin, €200,00: munten BSV, CHIP, FET, LAT, LUNC, MEME, MOVR, ONE, SOMI, WAN, WARD, WLD, XCH, XEC; bruto zonder voorraadgrens zou €119,39 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - kucoin, €2.000,00: munten BSV, CHIP, FET, LAT, LUNC, MEME, MOVR, ONE, SOMI, WAN, WARD, WLD, XCH, XEC; bruto zonder voorraadgrens zou €118,45 zijn, met voorraad €12,58 (GEZIEN boek, GOK model).
- htx - kucoin, €5.000,00: munten BSV, CHIP, FET, LAT, LUNC, MEME, MOVR, ONE, SOMI, WAN, WARD, WLD, XCH, XEC; bruto zonder voorraadgrens zou €117,05 zijn, met voorraad €36,81 (GEZIEN boek, GOK model).

### Andere keuzes bij bitvavo - kraken (netto handel, alle dagen samen; GOK)

| Keuze | Inleg | Kansen | Gemist | Bruto winst | Kosten terugschuiven | Netto handel |
|---|---|---|---|---|---|---|
| standaard (schuifdrempel 25%, kostengrens 1%) | €150,00 | 51 | 45 | €0,14 | €0,00 | **€0,14** |
| standaard (schuifdrempel 25%, kostengrens 1%) | €2.000,00 | 51 | 33 | €19,57 | €8,01 | **€11,55** |
| schuifdrempel 10% | €150,00 | 51 | 45 | €0,14 | €0,00 | **€0,14** |
| schuifdrempel 10% | €2.000,00 | 51 | 36 | €15,70 | €6,09 | **€9,61** |
| schuifdrempel 40% | €150,00 | 51 | 45 | €0,14 | €0,00 | **€0,14** |
| schuifdrempel 40% | €2.000,00 | 51 | 33 | €16,76 | €8,69 | **€8,07** |
| kostengrens 2% (achteraf vergeleken) | €150,00 | 51 | 45 | €0,14 | €0,00 | **€0,14** |
| kostengrens 2% (achteraf vergeleken) | €2.000,00 | 51 | 20 | €20,75 | €24,42 | **€-3,67** |
| kostengrens 5% (achteraf vergeleken) | €150,00 | 51 | 42 | €0,18 | €2,48 | **€-2,31** |
| kostengrens 5% (achteraf vergeleken) | €2.000,00 | 51 | 20 | €20,75 | €24,42 | **€-3,67** |
| alleen MERL en GMT (meer voorraad per munt, achteraf gekozen) | €150,00 | 36 | 34 | €0,19 | €0,00 | **€0,19** |
| alleen MERL en GMT (meer voorraad per munt, achteraf gekozen) | €2.000,00 | 36 | 16 | €37,90 | €22,07 | **€15,83** |

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

- Opnamekosten bij de echte kansen: 77 van een netwerk dat aan beide kanten open is, 85 van de beurs zelf (laagste open netwerk), 26 geschat uit wat andere beurzen voor die munt vragen (GOK). Onbekende opnamekosten tellen niet als echte kans.
- Netwerk: KuCoin, Gate, Bitget, HTX, XT, Bitstamp, Bitvavo en Poloniex geven hun netwerken per munt. Als beide beurzen dat doen en de namen te koppelen zijn, moet er een netwerk zijn dat aan beide kanten open is. Anders is het netwerk "niet te koppelen" en telt de kans mee (staat apart in de trechter).
- De duur is gemeten in stappen van ±20 seconden; een kans kan een paar rondes eerder begonnen zijn dan we zagen.
- Takerkosten: uit de API waar die ze per paar geeft, anders het standaardtarief uit de README (deels GOK).
- Laatste run: 15 beurzen antwoordden, 2288 munt-quote-paren op minstens twee beurzen (GEZIEN).
