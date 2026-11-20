# Rapport koersverschil-scanner

Gemaakt 2026-11-20 07:18 UTC uit 18 runs, samen ±21.8 uur gemeten (GEZIEN).
Echte kans = winst na alle kosten (opnamekosten bekend), opnemen en storten open (en een netwerk dat aan beide kanten open is, als de beurzen dat geven), minstens €100,00 op het boek, minstens 2 minuten blijven staan, geen andere munt met dezelfde naam.
**Vergund** = beide beurzen hebben een MiCA-vergunning (ESMA-register), vaak via een EU-dochter die minder munten kan hebben dan de wereldwijde API die we meten (GOK). **Grijs** = minstens één beurs zonder vergunning (MEXC, Bitget, HTX, Poloniex, XT, Bitfinex, Binance). Zie README.md.
**Kraken-tarief:** Kraken rekent 0,80% taker op munt tegen EUR, USD, USDT of USDC (GEZIEN, kraken.com/pro/fees, laagste trede); de scanner rekende tot 19 nov met 0,40%. 399 opgeslagen kansen met Kraken uit die runs zijn hier **opnieuw doorgerekend met 0,80%** (GOK-benadering: 0,40% van de inzet aan de Kraken-kant extra op elk gemeten punt van het boek; het boek zelf is niet bewaard). 233 houden daarna nog winst op het boek. Dat ze met hogere kosten ook korter bleven staan, telt niet mee (dus eerder te gunstig).

## Hoeveel wordt er gecontroleerd? (GEZIEN, stand.jsonl)

Per ronde (mediaan over 261 metingen): 1095 kandidaten (verschil op de ticker groter dan de takerkosten), 120 met het orderboek gecontroleerd, 2 nog nooit gecontroleerd (0%).
Bijna alle kandidaten komen aan de beurt; de aantallen hieronder missen weinig.

## Trechter (GEZIEN, eigen metingen)

| Stap | Alle beurzen | Alleen MiCA-beurzen | Met minstens één grijze beurs |
|---|---|---|---|
| Verschillen met winst op het boek na alle kosten | 18859 | 2847 | 16012 |
| ...waarvan opnemen of storten dicht | 4298 | 437 | 3861 |
| ...waarvan status onbekend (beurs geeft het niet openbaar) | 11092 | 2038 | 9054 |
| Opnemen en storten open | 3469 | 372 | 3097 |
| ...en geen netwerk dat aan beide kanten open is: valt af | 70 | 3 | 67 |
| ...en opnamekosten onbekend: valt af | 0 | 0 | 0 |
| ...en minstens €100,00 op het boek | 993 | 198 | 795 |
| ...en minstens 2 minuten blijven staan | 318 | 100 | 218 |
| ...en geen andere munt met dezelfde naam | 288 | 88 | 200 |
|    ...waarvan contractadres bekend en gelijk | 30 | 9 | 21 |
|    ...waarvan contractadres onbekend (telt mee, kan een andere munt zijn) | 258 | 79 | 179 |
|    ...waarvan netwerk gekoppeld en open | 177 | 33 | 144 |
|    ...waarvan netwerk niet te koppelen (telt mee) | 111 | 55 | 56 |
| **Echte kansen** (zelfde munt overlappend in de tijd samengevoegd, beste beurspaar telt) | 183 | 88 | 118 |
| Ter vergelijking: zelfde eisen, maar opnamestatus onbekend (niet meegeteld) | 649 | 152 | 559 |

## Echte kansen per dag (GEZIEN)

| Dag | Echt, alleen MiCA | Echt, met grijs | Mediane winst per kans bij €500 (MiCA / grijs) | Mediane duur |
|---|---|---|---|---|
| 2026-11-19 | 49 | 86 | €2,00 / €1,21 | 5.3 min |
| 2026-11-20 | 16 | 32 | €0,65 / €2,05 | 8.0 min |
| Totaal | 65 | 118 | €1,58 / €1,31 | 6.0 min |

## Beste munten (GEZIEN)

| | Soort | Kansen | Som winst bij €500 per kans |
|---|---|---|---|
| MERL-EUR | vergund | 16 | €180,26 |
| LUNC-USDT | grijs | 13 | €56,21 |
| USTC-USDT | grijs en vergund | 9 | €31,70 |
| SKY-USD | vergund | 2 | €21,52 |
| LAT-USDT | grijs | 3 | €17,59 |
| YB-USDT | grijs | 2 | €17,52 |
| GMT-EUR | vergund | 20 | €17,13 |
| WAN-USDT | grijs | 4 | €14,24 |
| VERONA-USDT | grijs | 9 | €13,96 |
| BSV-USDT | grijs | 6 | €11,48 |

## Beste beursparen (kopen op > verkopen op) (GEZIEN)

| | Soort | Kansen | Som winst bij €500 per kans |
|---|---|---|---|
| bitvavo > kraken | vergund | 51 | €222,93 |
| kucoin > htx | grijs | 19 | €55,17 |
| kucoin > bitget | grijs | 12 | €35,86 |
| bitget > xt | grijs | 11 | €35,79 |
| bitget > htx | grijs | 24 | €24,46 |
| bitget > gate | grijs | 7 | €24,32 |
| bitstamp > kraken | vergund | 2 | €21,52 |
| gate > kucoin | vergund | 9 | €19,60 |
| gate > xt | grijs | 2 | €19,11 |
| bitget > kucoin | grijs | 12 | €16,85 |

Beurzen die het vaakst meedoen (koop of verkoop): bitget (grijs) 72, kucoin 66, htx (grijs) 58, kraken 53, bitvavo 51, gate 33, xt (grijs) 24, poloniex (grijs) 7 (GEZIEN).

## Hoeveel kansen blijven staan terwijl je geld schuift? (GEZIEN, duur uit eigen metingen)

Wie geen voorraad op beide beurzen heeft, moet kopen, de munt opnemen, wachten tot hij binnen is en dan verkopen. Hoe lang dat duurt verschilt per munt en netwerk: een paar minuten (snelle ketens) tot een uur of meer (Bitcoin, beurzen die opnames met de hand keuren) (GOK, niet per munt gemeten).

| Overmaaktijd | Alle beurzen | Alleen MiCA-beurzen | Met minstens één grijze beurs |
|---|---|---|---|
| 5 min | 111 van 183 (61%) | 50 van 88 (57%) | 70 van 118 (59%) |
| 10 min | 68 van 183 (37%) | 31 van 88 (35%) | 43 van 118 (36%) |
| 30 min | 40 van 183 (22%) | 18 van 88 (20%) | 26 van 118 (22%) |
| 60 min | 17 van 183 (9%) | 9 van 88 (10%) | 11 van 118 (9%) |

## Wat zou het opleveren over 3 maanden? (GOK, doorgetrokken uit de metingen)

Gemeten over ±21.8 uur (GEZIEN), doorgetrokken naar 90 dagen (GOK: aanname dat de week die we maten gewoon is).

| Beurzen | Inleg | Model | Kansen per uur | Per kans (mediaan) | 3 maanden |
|---|---|---|---|---|---|
| Alleen MiCA | €2.000,00 | bovengrens: elke kans, geld overal tegelijk | 4.05 | €2,19 | €19.104,27 |
| Alleen MiCA | €2.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 2.34 | €2,53 | €36.286,74 |
| Alleen MiCA | €5.000,00 | bovengrens: elke kans, geld overal tegelijk | 4.05 | €2,41 | €21.071,42 |
| Alleen MiCA | €5.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 2.34 | €2,92 | €53.370,77 |
| Alle (met grijs) | €2.000,00 | bovengrens: elke kans, geld overal tegelijk | 8.41 | €1,59 | €28.953,38 |
| Alle (met grijs) | €2.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 2.34 | €2,53 | €36.286,74 |
| Alle (met grijs) | €5.000,00 | bovengrens: elke kans, geld overal tegelijk | 8.41 | €1,92 | €34.826,92 |
| Alle (met grijs) | €5.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 2.34 | €2,92 | €53.370,77 |

Bovengrens: elke kans met de helft van de inleg aan elke kant, alsof het geld op alle beurzen tegelijk staat (kan in het echt niet). Beste beurspaar: het paar is **achteraf** gekozen uit de metingen (vooraf kiezen levert minder op), en het model neemt aan dat je van elke munt al voorraad op de verkoopbeurs hebt.

Waarom dit te rooskleurig is (GOK): elke kans wordt maar één keer geteld met het mediane boek, maar andere bots pakken hem ook; de munt die je als voorraad aanhoudt kan dalen; na een paar kansen moet de voorraad terug (opnamekosten en tijd); minimale opname- en ordergroottes tellen niet mee; en een kans die we 2 minuten zagen staan, staat er niet per se nog als jouw order binnenkomt. Waarom het te somber kan zijn: niet alle kandidaten zijn gecontroleerd, en met voorraad op beide beurzen kun je dezelfde kans vaker pakken als het boek zich aanvult; dat telt hier niet mee.

## Wat houd je echt over? Voorraad op twee beurzen (simulatie)

Per beurspaar: geld en munten op beide beurzen, elke echte kans uitgevoerd tegen het boek zoals gemeten (niet meer dan de ruimte op het boek en niet meer dan de voorraad op die beurs), terugschuiven als een kant leeg dreigt te raken (met opnamekosten en tijd onderweg), en het koerseffect van de aangehouden munten apart. Netto = bruto min kosten terugschuiven plus koerseffect. **Gemeten** (GEZIEN): de kansen, het boek en de koersen; **de rest is een rekenmodel** (GOK, aannames onder de tabel). Geen advies.

**Met €150: netto €0,89 per dag op bitstamp - kraken (koerseffect erbovenop €-1,73), €0,07 per dag op bitvavo - kraken (koerseffect erbovenop €-1,16), €0,36 per dag op gate - kucoin (koerseffect erbovenop €0,94) (GOK: netto handel, rekenmodel op ±10.9 uur meting per dag, alleen MiCA).** "Per dag" is hier gemiddeld over 2 gemeten dagen achter elkaar; de eerste begint met een gelijk verdeelde voorraad; aan het eind staat de voorraad scheef, dus een volgende dag levert waarschijnlijk minder op, tenzij kansen de andere kant op hem terugbrengen (GOK).

### Alleen MiCA-beurzen (alle paren met echte kansen)

| Beurspaar | Inleg | Dag | Gemeten | Kansen | Gemist (geen voorraad) | Kleiner door voorraad | Bruto winst | Kosten terugschuiven | **Netto handel (bruto min kosten)** | Rendement handel | Koerseffect voorraad | Netto met koerseffect | Rendement met koerseffect |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| bitstamp - kraken | €100,00 | 2026-11-19 | 14.9 u | 2 | 1 | 1 | €1,18 | €0,00 (0x) | **€1,18** | 1.18% | €0,63 | €1,81 | 1.81% |
| bitstamp - kraken | €100,00 | 2026-11-20 | 6.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,94 | €-2,94 | -2.94% |
| bitstamp - kraken | €150,00 | 2026-11-19 | 14.9 u | 2 | 1 | 1 | €1,78 | €0,00 (0x) | **€1,78** | 1.18% | €0,94 | €2,72 | 1.81% |
| bitstamp - kraken | €150,00 | 2026-11-20 | 6.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-4,41 | €-4,41 | -2.94% |
| bitstamp - kraken | €200,00 | 2026-11-19 | 14.9 u | 2 | 1 | 1 | €2,37 | €0,00 (0x) | **€2,37** | 1.18% | €1,25 | €3,62 | 1.81% |
| bitstamp - kraken | €200,00 | 2026-11-20 | 6.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-5,88 | €-5,88 | -2.94% |
| bitstamp - kraken | €2.000,00 | 2026-11-19 | 14.9 u | 2 | 1 | 0 | €11,71 | €0,00 (0x) | **€11,71** | 0.59% | €12,53 | €24,24 | 1.21% |
| bitstamp - kraken | €2.000,00 | 2026-11-20 | 6.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-58,77 | €-58,77 | -2.94% |
| bitstamp - kraken | €5.000,00 | 2026-11-19 | 14.9 u | 2 | 1 | 0 | €11,71 | €0,00 (0x) | **€11,71** | 0.23% | €31,33 | €43,04 | 0.86% |
| bitstamp - kraken | €5.000,00 | 2026-11-20 | 6.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-146,93 | €-146,93 | -2.94% |
| bitvavo - kraken | €100,00 | 2026-11-19 | 14.9 u | 43 | 43 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,53 | €-0,53 | -0.53% |
| bitvavo - kraken | €100,00 | 2026-11-20 | 6.8 u | 8 | 8 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,01 | €-1,01 | -1.01% |
| bitvavo - kraken | €150,00 | 2026-11-19 | 14.9 u | 43 | 37 | 6 | €0,14 | €0,00 (0x) | **€0,14** | 0.09% | €-0,80 | €-0,66 | -0.44% |
| bitvavo - kraken | €150,00 | 2026-11-20 | 6.8 u | 8 | 8 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,51 | €-1,51 | -1.01% |
| bitvavo - kraken | €200,00 | 2026-11-19 | 14.9 u | 43 | 37 | 6 | €0,19 | €0,00 (0x) | **€0,19** | 0.09% | €-1,07 | €-0,88 | -0.44% |
| bitvavo - kraken | €200,00 | 2026-11-20 | 6.8 u | 8 | 8 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,02 | €-2,02 | -1.01% |
| bitvavo - kraken | €2.000,00 | 2026-11-19 | 14.9 u | 43 | 26 | 17 | €16,97 | €7,69 (18x) | **€9,28** | 0.46% | €-10,61 | €-1,33 | -0.07% |
| bitvavo - kraken | €2.000,00 | 2026-11-20 | 6.8 u | 8 | 7 | 1 | €2,59 | €0,32 (1x) | **€2,27** | 0.11% | €-20,00 | €-17,73 | -0.89% |
| bitvavo - kraken | €5.000,00 | 2026-11-19 | 14.9 u | 43 | 18 | 25 | €36,95 | €17,21 (27x) | **€19,74** | 0.39% | €-26,61 | €-6,86 | -0.14% |
| bitvavo - kraken | €5.000,00 | 2026-11-20 | 6.8 u | 8 | 1 | 7 | €9,71 | €8,22 (9x) | **€1,49** | 0.03% | €-50,14 | €-48,65 | -0.97% |
| gate - kucoin | €100,00 | 2026-11-19 | 14.9 u | 25 | 25 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,40 | €0,40 | 0.40% |
| gate - kucoin | €100,00 | 2026-11-20 | 6.8 u | 10 | 9 | 1 | €0,10 | €0,00 (1x) | **€0,10** | 0.10% | €0,86 | €0,96 | 0.96% |
| gate - kucoin | €150,00 | 2026-11-19 | 14.9 u | 25 | 17 | 8 | €0,22 | €0,00 (0x) | **€0,22** | 0.14% | €0,60 | €0,81 | 0.54% |
| gate - kucoin | €150,00 | 2026-11-20 | 6.8 u | 10 | 3 | 7 | €0,51 | €0,02 (2x) | **€0,50** | 0.33% | €1,29 | €1,78 | 1.19% |
| gate - kucoin | €200,00 | 2026-11-19 | 14.9 u | 25 | 17 | 8 | €0,29 | €0,00 (0x) | **€0,29** | 0.14% | €0,79 | €1,08 | 0.54% |
| gate - kucoin | €200,00 | 2026-11-20 | 6.8 u | 10 | 3 | 7 | €0,68 | €0,02 (2x) | **€0,67** | 0.33% | €1,71 | €2,38 | 1.19% |
| gate - kucoin | €2.000,00 | 2026-11-19 | 14.9 u | 25 | 6 | 19 | €6,15 | €4,85 (18x) | **€1,31** | 0.07% | €7,94 | €9,24 | 0.46% |
| gate - kucoin | €2.000,00 | 2026-11-20 | 6.8 u | 10 | 1 | 9 | €7,10 | €0,72 (6x) | **€6,39** | 0.32% | €17,27 | €23,66 | 1.18% |
| gate - kucoin | €5.000,00 | 2026-11-19 | 14.9 u | 25 | 6 | 18 | €14,93 | €5,78 (20x) | **€9,15** | 0.18% | €19,89 | €29,04 | 0.58% |
| gate - kucoin | €5.000,00 | 2026-11-20 | 6.8 u | 10 | 1 | 9 | €14,97 | €2,45 (9x) | **€12,52** | 0.25% | €43,11 | €55,63 | 1.11% |

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
- gate - kucoin, €100,00: munten ALKIMI, AVAIL, CHR, ERG, FTT, IKA, IR, LUNC, NIM, RARI, USTC, VERONA; bruto zonder voorraadgrens zou €110,37 zijn, met voorraad €0,10 (GEZIEN boek, GOK model).
- gate - kucoin, €150,00: munten ALKIMI, AVAIL, CHR, ERG, FTT, IKA, IR, LUNC, NIM, RARI, USTC, VERONA; bruto zonder voorraadgrens zou €110,37 zijn, met voorraad €0,73 (GEZIEN boek, GOK model).
- gate - kucoin, €200,00: munten ALKIMI, AVAIL, CHR, ERG, FTT, IKA, IR, LUNC, NIM, RARI, USTC, VERONA; bruto zonder voorraadgrens zou €110,37 zijn, met voorraad €0,97 (GEZIEN boek, GOK model).
- gate - kucoin, €2.000,00: munten ALKIMI, AVAIL, CHR, ERG, FTT, IKA, IR, LUNC, NIM, RARI, USTC, VERONA; bruto zonder voorraadgrens zou €108,82 zijn, met voorraad €13,26 (GEZIEN boek, GOK model).
- gate - kucoin, €5.000,00: munten ALKIMI, AVAIL, CHR, ERG, FTT, IKA, IR, LUNC, NIM, RARI, USTC, VERONA; bruto zonder voorraadgrens zou €106,54 zijn, met voorraad €29,90 (GEZIEN boek, GOK model).

### Met minstens één grijze beurs (de 5 paren met de meeste bruto winst)

| Beurspaar | Inleg | Dag | Gemeten | Kansen | Gemist (geen voorraad) | Kleiner door voorraad | Bruto winst | Kosten terugschuiven | **Netto handel (bruto min kosten)** | Rendement handel | Koerseffect voorraad | Netto met koerseffect | Rendement met koerseffect |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| kucoin - xt | €100,00 | 2026-11-19 | 14.9 u | 13 | 13 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,15 | €-0,15 | -0.15% |
| kucoin - xt | €100,00 | 2026-11-20 | 6.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,70 | €-0,70 | -0.70% |
| kucoin - xt | €150,00 | 2026-11-19 | 14.9 u | 13 | 10 | 3 | €0,35 | €0,00 (0x) | **€0,35** | 0.24% | €-0,22 | €0,13 | 0.09% |
| kucoin - xt | €150,00 | 2026-11-20 | 6.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,05 | €-1,05 | -0.70% |
| kucoin - xt | €200,00 | 2026-11-19 | 14.9 u | 13 | 10 | 3 | €0,47 | €0,00 (0x) | **€0,47** | 0.24% | €-0,30 | €0,18 | 0.09% |
| kucoin - xt | €200,00 | 2026-11-20 | 6.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,40 | €-1,40 | -0.70% |
| kucoin - xt | €2.000,00 | 2026-11-19 | 14.9 u | 13 | 3 | 10 | €16,57 | €6,42 (12x) | **€10,15** | 0.51% | €-2,95 | €7,20 | 0.36% |
| kucoin - xt | €2.000,00 | 2026-11-20 | 6.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-13,88 | €-13,88 | -0.69% |
| kucoin - xt | €5.000,00 | 2026-11-19 | 14.9 u | 13 | 2 | 10 | €34,70 | €5,17 (10x) | **€29,54** | 0.59% | €-7,39 | €22,14 | 0.44% |
| kucoin - xt | €5.000,00 | 2026-11-20 | 6.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-34,81 | €-34,81 | -0.70% |
| bitget - xt | €100,00 | 2026-11-19 | 14.9 u | 13 | 13 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €2,41 | €2,41 | 2.41% |
| bitget - xt | €100,00 | 2026-11-20 | 6.8 u | 2 | 2 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,81 | €-0,81 | -0.81% |
| bitget - xt | €150,00 | 2026-11-19 | 14.9 u | 13 | 13 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €3,61 | €3,61 | 2.41% |
| bitget - xt | €150,00 | 2026-11-20 | 6.8 u | 2 | 1 | 1 | €0,08 | €0,00 (0x) | **€0,08** | 0.05% | €-1,21 | €-1,14 | -0.76% |
| bitget - xt | €200,00 | 2026-11-19 | 14.9 u | 13 | 9 | 4 | €0,62 | €0,12 (4x) | **€0,50** | 0.25% | €4,81 | €5,31 | 2.66% |
| bitget - xt | €200,00 | 2026-11-20 | 6.8 u | 2 | 2 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,60 | €-1,60 | -0.80% |
| bitget - xt | €2.000,00 | 2026-11-19 | 14.9 u | 13 | 5 | 7 | €9,59 | €1,95 (10x) | **€7,64** | 0.38% | €48,12 | €55,76 | 2.79% |
| bitget - xt | €2.000,00 | 2026-11-20 | 6.8 u | 2 | 0 | 2 | €1,45 | €0,55 (2x) | **€0,90** | 0.04% | €-16,15 | €-15,26 | -0.76% |
| bitget - xt | €5.000,00 | 2026-11-19 | 14.9 u | 13 | 4 | 7 | €19,03 | €1,84 (9x) | **€17,19** | 0.34% | €120,30 | €137,49 | 2.75% |
| bitget - xt | €5.000,00 | 2026-11-20 | 6.8 u | 2 | 0 | 2 | €2,72 | €0,55 (2x) | **€2,16** | 0.04% | €-40,36 | €-38,20 | -0.76% |
| htx - xt | €100,00 | 2026-11-19 | 14.9 u | 18 | 18 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,42 | €-0,42 | -0.42% |
| htx - xt | €100,00 | 2026-11-20 | 6.8 u | 5 | 5 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,88 | €-0,88 | -0.88% |
| htx - xt | €150,00 | 2026-11-19 | 14.9 u | 18 | 18 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,64 | €-0,64 | -0.42% |
| htx - xt | €150,00 | 2026-11-20 | 6.8 u | 5 | 5 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,33 | €-1,33 | -0.88% |
| htx - xt | €200,00 | 2026-11-19 | 14.9 u | 18 | 18 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,85 | €-0,85 | -0.42% |
| htx - xt | €200,00 | 2026-11-20 | 6.8 u | 5 | 5 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,77 | €-1,77 | -0.88% |
| htx - xt | €2.000,00 | 2026-11-19 | 14.9 u | 18 | 5 | 13 | €10,87 | €5,28 (12x) | **€5,58** | 0.28% | €-8,52 | €-2,93 | -0.15% |
| htx - xt | €2.000,00 | 2026-11-20 | 6.8 u | 5 | 0 | 5 | €4,84 | €2,08 (4x) | **€2,75** | 0.14% | €-17,48 | €-14,73 | -0.74% |
| htx - xt | €5.000,00 | 2026-11-19 | 14.9 u | 18 | 5 | 12 | €21,84 | €6,65 (13x) | **€15,19** | 0.30% | €-21,22 | €-6,03 | -0.12% |
| htx - xt | €5.000,00 | 2026-11-20 | 6.8 u | 5 | 0 | 5 | €10,37 | €4,90 (6x) | **€5,47** | 0.11% | €-43,99 | €-38,52 | -0.77% |
| bitget - gate | €100,00 | 2026-11-19 | 14.9 u | 15 | 15 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,32 | €0,32 | 0.32% |
| bitget - gate | €100,00 | 2026-11-20 | 6.8 u | 2 | 2 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,26 | €-1,26 | -1.26% |
| bitget - gate | €150,00 | 2026-11-19 | 14.9 u | 15 | 15 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,48 | €0,48 | 0.32% |
| bitget - gate | €150,00 | 2026-11-20 | 6.8 u | 2 | 2 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,89 | €-1,89 | -1.26% |
| bitget - gate | €200,00 | 2026-11-19 | 14.9 u | 15 | 15 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,64 | €0,64 | 0.32% |
| bitget - gate | €200,00 | 2026-11-20 | 6.8 u | 2 | 2 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,51 | €-2,51 | -1.26% |
| bitget - gate | €2.000,00 | 2026-11-19 | 14.9 u | 15 | 4 | 11 | €10,17 | €2,20 (11x) | **€7,97** | 0.40% | €6,44 | €14,41 | 0.72% |
| bitget - gate | €2.000,00 | 2026-11-20 | 6.8 u | 2 | 0 | 2 | €1,76 | €0,58 (2x) | **€1,18** | 0.06% | €-25,05 | €-23,88 | -1.19% |
| bitget - gate | €5.000,00 | 2026-11-19 | 14.9 u | 15 | 4 | 9 | €20,82 | €3,69 (11x) | **€17,13** | 0.34% | €16,02 | €33,15 | 0.66% |
| bitget - gate | €5.000,00 | 2026-11-20 | 6.8 u | 2 | 0 | 1 | €3,82 | €0,57 (1x) | **€3,25** | 0.07% | €-62,76 | €-59,50 | -1.19% |
| gate - htx | €100,00 | 2026-11-19 | 14.9 u | 19 | 19 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,89 | €-0,89 | -0.89% |
| gate - htx | €100,00 | 2026-11-20 | 6.8 u | 11 | 11 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,71 | €-1,71 | -1.71% |
| gate - htx | €150,00 | 2026-11-19 | 14.9 u | 19 | 19 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,34 | €-1,34 | -0.89% |
| gate - htx | €150,00 | 2026-11-20 | 6.8 u | 11 | 11 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,57 | €-2,57 | -1.71% |
| gate - htx | €200,00 | 2026-11-19 | 14.9 u | 19 | 19 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,78 | €-1,78 | -0.89% |
| gate - htx | €200,00 | 2026-11-20 | 6.8 u | 11 | 11 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,42 | €-3,42 | -1.71% |
| gate - htx | €2.000,00 | 2026-11-19 | 14.9 u | 19 | 6 | 13 | €7,65 | €4,51 (12x) | **€3,15** | 0.16% | €-17,84 | €-14,70 | -0.73% |
| gate - htx | €2.000,00 | 2026-11-20 | 6.8 u | 11 | 2 | 9 | €3,85 | €1,89 (8x) | **€1,96** | 0.10% | €-34,03 | €-32,07 | -1.60% |
| gate - htx | €5.000,00 | 2026-11-19 | 14.9 u | 19 | 6 | 10 | €16,33 | €5,59 (13x) | **€10,74** | 0.21% | €-44,61 | €-33,87 | -0.68% |
| gate - htx | €5.000,00 | 2026-11-20 | 6.8 u | 11 | 2 | 8 | €8,75 | €2,61 (9x) | **€6,14** | 0.12% | €-85,32 | €-79,18 | -1.58% |

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
- htx - xt, €100,00: munten BSV, CBK, LUNC, SEI, XCH, XDC; bruto zonder voorraadgrens zou €111,79 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - xt, €150,00: munten BSV, CBK, LUNC, SEI, XCH, XDC; bruto zonder voorraadgrens zou €111,79 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - xt, €200,00: munten BSV, CBK, LUNC, SEI, XCH, XDC; bruto zonder voorraadgrens zou €111,79 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - xt, €2.000,00: munten BSV, CBK, LUNC, SEI, XCH, XDC; bruto zonder voorraadgrens zou €109,11 zijn, met voorraad €15,70 (GEZIEN boek, GOK model).
- htx - xt, €5.000,00: munten BSV, CBK, LUNC, SEI, XCH, XDC; bruto zonder voorraadgrens zou €106,70 zijn, met voorraad €32,22 (GEZIEN boek, GOK model).
- bitget - gate, €100,00: munten BABYSHARK, IR, IRYS, LUNC, RARE, SNEK, VERONA; bruto zonder voorraadgrens zou €101,13 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - gate, €150,00: munten BABYSHARK, IR, IRYS, LUNC, RARE, SNEK, VERONA; bruto zonder voorraadgrens zou €101,13 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - gate, €200,00: munten BABYSHARK, IR, IRYS, LUNC, RARE, SNEK, VERONA; bruto zonder voorraadgrens zou €101,13 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - gate, €2.000,00: munten BABYSHARK, IR, IRYS, LUNC, RARE, SNEK, VERONA; bruto zonder voorraadgrens zou €97,82 zijn, met voorraad €11,93 (GEZIEN boek, GOK model).
- bitget - gate, €5.000,00: munten BABYSHARK, IR, IRYS, LUNC, RARE, SNEK, VERONA; bruto zonder voorraadgrens zou €94,00 zijn, met voorraad €24,64 (GEZIEN boek, GOK model).
- gate - htx, €100,00: munten BSV, CBK, KAS, LAT, LUNC, MOVR, SEI, WARD, WLD; bruto zonder voorraadgrens zou €84,42 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- gate - htx, €150,00: munten BSV, CBK, KAS, LAT, LUNC, MOVR, SEI, WARD, WLD; bruto zonder voorraadgrens zou €84,42 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- gate - htx, €200,00: munten BSV, CBK, KAS, LAT, LUNC, MOVR, SEI, WARD, WLD; bruto zonder voorraadgrens zou €84,42 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- gate - htx, €2.000,00: munten BSV, CBK, KAS, LAT, LUNC, MOVR, SEI, WARD, WLD; bruto zonder voorraadgrens zou €80,62 zijn, met voorraad €11,51 (GEZIEN boek, GOK model).
- gate - htx, €5.000,00: munten BSV, CBK, KAS, LAT, LUNC, MOVR, SEI, WARD, WLD; bruto zonder voorraadgrens zou €75,99 zijn, met voorraad €25,08 (GEZIEN boek, GOK model).

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

- Opnamekosten bij de echte kansen: 72 van een netwerk dat aan beide kanten open is, 85 van de beurs zelf (laagste open netwerk), 26 geschat uit wat andere beurzen voor die munt vragen (GOK). Onbekende opnamekosten tellen niet als echte kans.
- Netwerk: KuCoin, Gate, Bitget, HTX, XT, Bitstamp, Bitvavo en Poloniex geven hun netwerken per munt. Als beide beurzen dat doen en de namen te koppelen zijn, moet er een netwerk zijn dat aan beide kanten open is. Anders is het netwerk "niet te koppelen" en telt de kans mee (staat apart in de trechter).
- De duur is gemeten in stappen van ±20 seconden; een kans kan een paar rondes eerder begonnen zijn dan we zagen.
- Takerkosten: uit de API waar die ze per paar geeft, anders het standaardtarief uit de README (deels GOK).
- Laatste run: 15 beurzen antwoordden, 2288 munt-quote-paren op minstens twee beurzen (GEZIEN).
