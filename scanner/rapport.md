# Rapport koersverschil-scanner

Gemaakt 2026-11-20 04:41 UTC uit 18 runs, samen ±19.2 uur gemeten (GEZIEN).
Echte kans = winst na alle kosten (opnamekosten bekend), opnemen en storten open (en een netwerk dat aan beide kanten open is, als de beurzen dat geven), minstens €100,00 op het boek, minstens 2 minuten blijven staan, geen andere munt met dezelfde naam.
**Vergund** = beide beurzen hebben een MiCA-vergunning (ESMA-register), vaak via een EU-dochter die minder munten kan hebben dan de wereldwijde API die we meten (GOK). **Grijs** = minstens één beurs zonder vergunning (MEXC, Bitget, HTX, Poloniex, XT, Bitfinex, Binance). Zie README.md.
**Kraken-tarief:** Kraken rekent 0,80% taker op munt tegen EUR, USD, USDT of USDC (GEZIEN, kraken.com/pro/fees, laagste trede); de scanner rekende tot 19 nov met 0,40%. 399 opgeslagen kansen met Kraken uit die runs zijn hier **opnieuw doorgerekend met 0,80%** (GOK-benadering: 0,40% van de inzet aan de Kraken-kant extra op elk gemeten punt van het boek; het boek zelf is niet bewaard). 233 houden daarna nog winst op het boek. Dat ze met hogere kosten ook korter bleven staan, telt niet mee (dus eerder te gunstig).

## Hoeveel wordt er gecontroleerd? (GEZIEN, stand.jsonl)

Per ronde (mediaan over 230 metingen): 1072 kandidaten (verschil op de ticker groter dan de takerkosten), 120 met het orderboek gecontroleerd, 2 nog nooit gecontroleerd (0%).
Bijna alle kandidaten komen aan de beurt; de aantallen hieronder missen weinig.

## Trechter (GEZIEN, eigen metingen)

| Stap | Alle beurzen | Alleen MiCA-beurzen | Met minstens één grijze beurs |
|---|---|---|---|
| Verschillen met winst op het boek na alle kosten | 17173 | 2574 | 14599 |
| ...waarvan opnemen of storten dicht | 3957 | 405 | 3552 |
| ...waarvan status onbekend (beurs geeft het niet openbaar) | 10125 | 1839 | 8286 |
| Opnemen en storten open | 3091 | 330 | 2761 |
| ...en geen netwerk dat aan beide kanten open is: valt af | 50 | 3 | 47 |
| ...en opnamekosten onbekend: valt af | 0 | 0 | 0 |
| ...en minstens €100,00 op het boek | 891 | 179 | 712 |
| ...en minstens 2 minuten blijven staan | 290 | 94 | 196 |
| ...en geen andere munt met dezelfde naam | 261 | 82 | 179 |
|    ...waarvan contractadres bekend en gelijk | 25 | 7 | 18 |
|    ...waarvan contractadres onbekend (telt mee, kan een andere munt zijn) | 236 | 75 | 161 |
|    ...waarvan netwerk gekoppeld en open | 155 | 29 | 126 |
|    ...waarvan netwerk niet te koppelen (telt mee) | 106 | 53 | 53 |
| **Echte kansen** (zelfde munt overlappend in de tijd samengevoegd, beste beurspaar telt) | 163 | 82 | 104 |
| Ter vergelijking: zelfde eisen, maar opnamestatus onbekend (niet meegeteld) | 579 | 134 | 501 |

## Echte kansen per dag (GEZIEN)

| Dag | Echt, alleen MiCA | Echt, met grijs | Mediane winst per kans bij €500 (MiCA / grijs) | Mediane duur |
|---|---|---|---|---|
| 2026-11-19 | 49 | 86 | €2,00 / €1,21 | 5.3 min |
| 2026-11-20 | 10 | 18 | €0,34 / €2,15 | 7.5 min |
| Totaal | 59 | 104 | €1,72 / €1,31 | 5.7 min |

## Beste munten (GEZIEN)

| | Soort | Kansen | Som winst bij €500 per kans |
|---|---|---|---|
| MERL-EUR | vergund | 16 | €180,26 |
| LUNC-USDT | grijs | 10 | €52,69 |
| USTC-USDT | grijs | 8 | €30,97 |
| SKY-USD | vergund | 2 | €21,52 |
| LAT-USDT | grijs | 3 | €17,59 |
| YB-USDT | grijs | 1 | €16,34 |
| GMT-EUR | vergund | 18 | €15,84 |
| WAN-USDT | grijs | 4 | €14,24 |
| VERONA-USDT | grijs | 8 | €13,53 |
| AVA-EUR | vergund | 4 | €11,22 |

## Beste beursparen (kopen op > verkopen op) (GEZIEN)

| | Soort | Kansen | Som winst bij €500 per kans |
|---|---|---|---|
| bitvavo > kraken | vergund | 49 | €221,63 |
| kucoin > htx | grijs | 17 | €39,95 |
| kucoin > bitget | grijs | 12 | €35,86 |
| bitget > xt | grijs | 10 | €34,61 |
| bitget > gate | grijs | 7 | €24,32 |
| bitstamp > kraken | vergund | 2 | €21,52 |
| gate > xt | grijs | 2 | €19,11 |
| bitget > htx | grijs | 20 | €18,29 |
| bitget > kucoin | grijs | 10 | €15,69 |
| gate > kucoin | vergund | 7 | €13,33 |

Beurzen die het vaakst meedoen (koop of verkoop): bitget (grijs) 64, kucoin 55, kraken 51, bitvavo 49, htx (grijs) 49, gate 28, xt (grijs) 22, poloniex (grijs) 6 (GEZIEN).

## Hoeveel kansen blijven staan terwijl je geld schuift? (GEZIEN, duur uit eigen metingen)

Wie geen voorraad op beide beurzen heeft, moet kopen, de munt opnemen, wachten tot hij binnen is en dan verkopen. Hoe lang dat duurt verschilt per munt en netwerk: een paar minuten (snelle ketens) tot een uur of meer (Bitcoin, beurzen die opnames met de hand keuren) (GOK, niet per munt gemeten).

| Overmaaktijd | Alle beurzen | Alleen MiCA-beurzen | Met minstens één grijze beurs |
|---|---|---|---|
| 5 min | 93 van 163 (57%) | 44 van 82 (54%) | 58 van 104 (56%) |
| 10 min | 57 van 163 (35%) | 27 van 82 (33%) | 36 van 104 (35%) |
| 30 min | 35 van 163 (21%) | 18 van 82 (22%) | 21 van 104 (20%) |
| 60 min | 16 van 163 (10%) | 9 van 82 (11%) | 10 van 104 (10%) |

## Wat zou het opleveren over 3 maanden? (GOK, doorgetrokken uit de metingen)

Gemeten over ±19.2 uur (GEZIEN), doorgetrokken naar 90 dagen (GOK: aanname dat de week die we maten gewoon is).

| Beurzen | Inleg | Model | Kansen per uur | Per kans (mediaan) | 3 maanden |
|---|---|---|---|---|---|
| Alleen MiCA | €2.000,00 | bovengrens: elke kans, geld overal tegelijk | 4.28 | €2,25 | €20.746,93 |
| Alleen MiCA | €2.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 2.56 | €2,54 | €40.928,34 |
| Alleen MiCA | €5.000,00 | bovengrens: elke kans, geld overal tegelijk | 4.28 | €2,58 | €23.807,01 |
| Alleen MiCA | €5.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 2.56 | €3,10 | €60.276,94 |
| Alle (met grijs) | €2.000,00 | bovengrens: elke kans, geld overal tegelijk | 8.50 | €1,60 | €29.360,78 |
| Alle (met grijs) | €2.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 2.56 | €2,54 | €40.928,34 |
| Alle (met grijs) | €5.000,00 | bovengrens: elke kans, geld overal tegelijk | 8.50 | €2,04 | €37.422,88 |
| Alle (met grijs) | €5.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 2.56 | €3,10 | €60.276,94 |

Bovengrens: elke kans met de helft van de inleg aan elke kant, alsof het geld op alle beurzen tegelijk staat (kan in het echt niet). Beste beurspaar: het paar is **achteraf** gekozen uit de metingen (vooraf kiezen levert minder op), en het model neemt aan dat je van elke munt al voorraad op de verkoopbeurs hebt.

Waarom dit te rooskleurig is (GOK): elke kans wordt maar één keer geteld met het mediane boek, maar andere bots pakken hem ook; de munt die je als voorraad aanhoudt kan dalen; na een paar kansen moet de voorraad terug (opnamekosten en tijd); minimale opname- en ordergroottes tellen niet mee; en een kans die we 2 minuten zagen staan, staat er niet per se nog als jouw order binnenkomt. Waarom het te somber kan zijn: niet alle kandidaten zijn gecontroleerd, en met voorraad op beide beurzen kun je dezelfde kans vaker pakken als het boek zich aanvult; dat telt hier niet mee.

## Wat houd je echt over? Voorraad op twee beurzen (simulatie)

Per beurspaar: geld en munten op beide beurzen, elke echte kans uitgevoerd tegen het boek zoals gemeten (niet meer dan de ruimte op het boek en niet meer dan de voorraad op die beurs), terugschuiven als een kant leeg dreigt te raken (met opnamekosten en tijd onderweg), en het koerseffect van de aangehouden munten apart. Netto = bruto min kosten terugschuiven plus koerseffect. **Gemeten** (GEZIEN): de kansen, het boek en de koersen; **de rest is een rekenmodel** (GOK, aannames onder de tabel). Geen advies.

**Met €150: netto €0,89 per dag op bitstamp - kraken (koerseffect erbovenop €-1,22), €0,07 per dag op bitvavo - kraken (koerseffect erbovenop €-1,32), €0,29 per dag op gate - kucoin (koerseffect erbovenop €-1,88) (GOK: netto handel, rekenmodel op ±9.6 uur meting per dag, alleen MiCA).** "Per dag" is hier gemiddeld over 2 gemeten dagen achter elkaar; de eerste begint met een gelijk verdeelde voorraad; aan het eind staat de voorraad scheef, dus een volgende dag levert waarschijnlijk minder op, tenzij kansen de andere kant op hem terugbrengen (GOK).

### Alleen MiCA-beurzen (alle paren met echte kansen)

| Beurspaar | Inleg | Dag | Gemeten | Kansen | Gemist (geen voorraad) | Kleiner door voorraad | Bruto winst | Kosten terugschuiven | **Netto handel (bruto min kosten)** | Rendement handel | Koerseffect voorraad | Netto met koerseffect | Rendement met koerseffect |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| bitstamp - kraken | €100,00 | 2026-11-19 | 14.9 u | 2 | 1 | 1 | €1,18 | €0,00 (0x) | **€1,18** | 1.18% | €0,63 | €1,81 | 1.81% |
| bitstamp - kraken | €100,00 | 2026-11-20 | 4.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,25 | €-2,25 | -2.25% |
| bitstamp - kraken | €150,00 | 2026-11-19 | 14.9 u | 2 | 1 | 1 | €1,78 | €0,00 (0x) | **€1,78** | 1.18% | €0,94 | €2,72 | 1.81% |
| bitstamp - kraken | €150,00 | 2026-11-20 | 4.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,37 | €-3,37 | -2.25% |
| bitstamp - kraken | €200,00 | 2026-11-19 | 14.9 u | 2 | 1 | 1 | €2,37 | €0,00 (0x) | **€2,37** | 1.18% | €1,25 | €3,62 | 1.81% |
| bitstamp - kraken | €200,00 | 2026-11-20 | 4.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-4,49 | €-4,49 | -2.25% |
| bitstamp - kraken | €2.000,00 | 2026-11-19 | 14.9 u | 2 | 1 | 0 | €11,71 | €0,00 (0x) | **€11,71** | 0.59% | €12,53 | €24,24 | 1.21% |
| bitstamp - kraken | €2.000,00 | 2026-11-20 | 4.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-44,94 | €-44,94 | -2.25% |
| bitstamp - kraken | €5.000,00 | 2026-11-19 | 14.9 u | 2 | 1 | 0 | €11,71 | €0,00 (0x) | **€11,71** | 0.23% | €31,33 | €43,04 | 0.86% |
| bitstamp - kraken | €5.000,00 | 2026-11-20 | 4.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-112,36 | €-112,36 | -2.25% |
| bitvavo - kraken | €100,00 | 2026-11-19 | 14.9 u | 43 | 43 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,53 | €-0,53 | -0.53% |
| bitvavo - kraken | €100,00 | 2026-11-20 | 4.3 u | 6 | 6 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,23 | €-1,23 | -1.23% |
| bitvavo - kraken | €150,00 | 2026-11-19 | 14.9 u | 43 | 37 | 6 | €0,14 | €0,00 (0x) | **€0,14** | 0.09% | €-0,80 | €-0,66 | -0.44% |
| bitvavo - kraken | €150,00 | 2026-11-20 | 4.3 u | 6 | 6 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,84 | €-1,84 | -1.23% |
| bitvavo - kraken | €200,00 | 2026-11-19 | 14.9 u | 43 | 37 | 6 | €0,19 | €0,00 (0x) | **€0,19** | 0.09% | €-1,07 | €-0,88 | -0.44% |
| bitvavo - kraken | €200,00 | 2026-11-20 | 4.3 u | 6 | 6 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,45 | €-2,45 | -1.23% |
| bitvavo - kraken | €2.000,00 | 2026-11-19 | 14.9 u | 43 | 26 | 17 | €16,97 | €7,69 (18x) | **€9,28** | 0.46% | €-10,61 | €-1,33 | -0.07% |
| bitvavo - kraken | €2.000,00 | 2026-11-20 | 4.3 u | 6 | 5 | 1 | €2,59 | €0,32 (1x) | **€2,27** | 0.11% | €-24,36 | €-22,09 | -1.10% |
| bitvavo - kraken | €5.000,00 | 2026-11-19 | 14.9 u | 43 | 18 | 25 | €36,95 | €17,19 (27x) | **€19,76** | 0.40% | €-26,61 | €-6,85 | -0.14% |
| bitvavo - kraken | €5.000,00 | 2026-11-20 | 4.3 u | 6 | 1 | 5 | €8,36 | €5,24 (6x) | **€3,11** | 0.06% | €-60,93 | €-57,81 | -1.16% |
| gate - kucoin | €100,00 | 2026-11-19 | 14.9 u | 25 | 25 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,73 | €-0,73 | -0.73% |
| gate - kucoin | €100,00 | 2026-11-20 | 4.3 u | 6 | 6 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,78 | €-1,78 | -1.78% |
| gate - kucoin | €150,00 | 2026-11-19 | 14.9 u | 25 | 17 | 8 | €0,26 | €0,00 (0x) | **€0,26** | 0.17% | €-1,10 | €-0,84 | -0.56% |
| gate - kucoin | €150,00 | 2026-11-20 | 4.3 u | 6 | 2 | 4 | €0,31 | €0,00 (0x) | **€0,31** | 0.21% | €-2,67 | €-2,36 | -1.57% |
| gate - kucoin | €200,00 | 2026-11-19 | 14.9 u | 25 | 17 | 8 | €0,35 | €0,00 (0x) | **€0,35** | 0.17% | €-1,46 | €-1,12 | -0.56% |
| gate - kucoin | €200,00 | 2026-11-20 | 4.3 u | 6 | 2 | 4 | €0,41 | €0,00 (0x) | **€0,41** | 0.21% | €-3,56 | €-3,15 | -1.57% |
| gate - kucoin | €2.000,00 | 2026-11-19 | 14.9 u | 25 | 6 | 19 | €7,39 | €5,26 (19x) | **€2,12** | 0.11% | €-14,62 | €-12,50 | -0.62% |
| gate - kucoin | €2.000,00 | 2026-11-20 | 4.3 u | 6 | 1 | 5 | €4,25 | €0,53 (3x) | **€3,72** | 0.19% | €-35,47 | €-31,75 | -1.59% |
| gate - kucoin | €5.000,00 | 2026-11-19 | 14.9 u | 25 | 6 | 17 | €17,01 | €5,78 (20x) | **€11,23** | 0.22% | €-36,56 | €-25,33 | -0.51% |
| gate - kucoin | €5.000,00 | 2026-11-20 | 4.3 u | 6 | 1 | 4 | €9,29 | €1,77 (5x) | **€7,52** | 0.15% | €-88,75 | €-81,23 | -1.62% |

- bitstamp - kraken, €100,00: munten SKY; bruto zonder voorraadgrens zou €22,30 zijn, met voorraad €1,18 (GEZIEN boek, GOK model).
- bitstamp - kraken, €150,00: munten SKY; bruto zonder voorraadgrens zou €21,71 zijn, met voorraad €1,78 (GEZIEN boek, GOK model).
- bitstamp - kraken, €200,00: munten SKY; bruto zonder voorraadgrens zou €21,12 zijn, met voorraad €2,37 (GEZIEN boek, GOK model).
- bitstamp - kraken, €2.000,00: munten SKY; bruto zonder voorraadgrens zou €11,71 zijn, met voorraad €11,71 (GEZIEN boek, GOK model).
- bitstamp - kraken, €5.000,00: munten SKY; bruto zonder voorraadgrens zou €11,71 zijn, met voorraad €11,71 (GEZIEN boek, GOK model).
- bitvavo - kraken, €100,00: munten AVA, DYM, GMT, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €696,91 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitvavo - kraken, €150,00: munten AVA, DYM, GMT, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €696,50 zijn, met voorraad €0,14 (GEZIEN boek, GOK model).
- bitvavo - kraken, €200,00: munten AVA, DYM, GMT, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €696,36 zijn, met voorraad €0,19 (GEZIEN boek, GOK model).
- bitvavo - kraken, €2.000,00: munten AVA, DYM, GMT, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €676,67 zijn, met voorraad €19,57 (GEZIEN boek, GOK model).
- bitvavo - kraken, €5.000,00: munten AVA, DYM, GMT, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €643,16 zijn, met voorraad €45,31 (GEZIEN boek, GOK model).
- gate - kucoin, €100,00: munten ALKIMI, CHR, ERG, FTT, IR, LUNC, NIM, RARI, USTC, VERONA; bruto zonder voorraadgrens zou €102,63 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- gate - kucoin, €150,00: munten ALKIMI, CHR, ERG, FTT, IR, LUNC, NIM, RARI, USTC, VERONA; bruto zonder voorraadgrens zou €102,63 zijn, met voorraad €0,57 (GEZIEN boek, GOK model).
- gate - kucoin, €200,00: munten ALKIMI, CHR, ERG, FTT, IR, LUNC, NIM, RARI, USTC, VERONA; bruto zonder voorraadgrens zou €102,63 zijn, met voorraad €0,76 (GEZIEN boek, GOK model).
- gate - kucoin, €2.000,00: munten ALKIMI, CHR, ERG, FTT, IR, LUNC, NIM, RARI, USTC, VERONA; bruto zonder voorraadgrens zou €100,77 zijn, met voorraad €11,64 (GEZIEN boek, GOK model).
- gate - kucoin, €5.000,00: munten ALKIMI, CHR, ERG, FTT, IR, LUNC, NIM, RARI, USTC, VERONA; bruto zonder voorraadgrens zou €98,25 zijn, met voorraad €26,30 (GEZIEN boek, GOK model).

### Met minstens één grijze beurs (de 5 paren met de meeste bruto winst)

| Beurspaar | Inleg | Dag | Gemeten | Kansen | Gemist (geen voorraad) | Kleiner door voorraad | Bruto winst | Kosten terugschuiven | **Netto handel (bruto min kosten)** | Rendement handel | Koerseffect voorraad | Netto met koerseffect | Rendement met koerseffect |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| kucoin - xt | €100,00 | 2026-11-19 | 14.9 u | 13 | 13 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,15 | €-0,15 | -0.15% |
| kucoin - xt | €100,00 | 2026-11-20 | 4.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,14 | €-1,14 | -1.14% |
| kucoin - xt | €150,00 | 2026-11-19 | 14.9 u | 13 | 10 | 3 | €0,35 | €0,00 (0x) | **€0,35** | 0.24% | €-0,22 | €0,13 | 0.09% |
| kucoin - xt | €150,00 | 2026-11-20 | 4.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,71 | €-1,71 | -1.14% |
| kucoin - xt | €200,00 | 2026-11-19 | 14.9 u | 13 | 10 | 3 | €0,47 | €0,00 (0x) | **€0,47** | 0.24% | €-0,30 | €0,18 | 0.09% |
| kucoin - xt | €200,00 | 2026-11-20 | 4.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,27 | €-2,27 | -1.14% |
| kucoin - xt | €2.000,00 | 2026-11-19 | 14.9 u | 13 | 3 | 10 | €16,57 | €6,42 (12x) | **€10,15** | 0.51% | €-2,95 | €7,20 | 0.36% |
| kucoin - xt | €2.000,00 | 2026-11-20 | 4.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-22,61 | €-22,61 | -1.13% |
| kucoin - xt | €5.000,00 | 2026-11-19 | 14.9 u | 13 | 2 | 10 | €34,70 | €5,17 (10x) | **€29,54** | 0.59% | €-7,39 | €22,14 | 0.44% |
| kucoin - xt | €5.000,00 | 2026-11-20 | 4.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-56,74 | €-56,74 | -1.13% |
| bitget - xt | €100,00 | 2026-11-19 | 14.9 u | 13 | 13 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €1,32 | €1,32 | 1.32% |
| bitget - xt | €100,00 | 2026-11-20 | 4.3 u | 1 | 1 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,40 | €-1,40 | -1.40% |
| bitget - xt | €150,00 | 2026-11-19 | 14.9 u | 13 | 10 | 3 | €0,49 | €0,11 (3x) | **€0,38** | 0.25% | €1,98 | €2,36 | 1.57% |
| bitget - xt | €150,00 | 2026-11-20 | 4.3 u | 1 | 1 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,10 | €-2,10 | -1.40% |
| bitget - xt | €200,00 | 2026-11-19 | 14.9 u | 13 | 10 | 3 | €0,65 | €0,11 (3x) | **€0,54** | 0.27% | €2,65 | €3,19 | 1.59% |
| bitget - xt | €200,00 | 2026-11-20 | 4.3 u | 1 | 1 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,81 | €-2,81 | -1.40% |
| bitget - xt | €2.000,00 | 2026-11-19 | 14.9 u | 13 | 4 | 8 | €14,18 | €2,76 (11x) | **€11,42** | 0.57% | €26,48 | €37,90 | 1.90% |
| bitget - xt | €2.000,00 | 2026-11-20 | 4.3 u | 1 | 0 | 1 | €0,80 | €0,00 (1x) | **€0,79** | 0.04% | €-28,08 | €-27,28 | -1.36% |
| bitget - xt | €5.000,00 | 2026-11-19 | 14.9 u | 13 | 4 | 7 | €28,24 | €2,76 (10x) | **€25,48** | 0.51% | €66,19 | €91,68 | 1.83% |
| bitget - xt | €5.000,00 | 2026-11-20 | 4.3 u | 1 | 0 | 1 | €1,77 | €0,00 (1x) | **€1,76** | 0.04% | €-70,19 | €-68,43 | -1.37% |
| bitget - gate | €100,00 | 2026-11-19 | 14.9 u | 15 | 15 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,32 | €0,32 | 0.32% |
| bitget - gate | €100,00 | 2026-11-20 | 4.3 u | 2 | 2 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,95 | €-0,95 | -0.95% |
| bitget - gate | €150,00 | 2026-11-19 | 14.9 u | 15 | 15 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,48 | €0,48 | 0.32% |
| bitget - gate | €150,00 | 2026-11-20 | 4.3 u | 2 | 2 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,43 | €-1,43 | -0.95% |
| bitget - gate | €200,00 | 2026-11-19 | 14.9 u | 15 | 15 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,64 | €0,64 | 0.32% |
| bitget - gate | €200,00 | 2026-11-20 | 4.3 u | 2 | 2 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,91 | €-1,91 | -0.95% |
| bitget - gate | €2.000,00 | 2026-11-19 | 14.9 u | 15 | 4 | 11 | €10,17 | €2,20 (11x) | **€7,97** | 0.40% | €6,44 | €14,41 | 0.72% |
| bitget - gate | €2.000,00 | 2026-11-20 | 4.3 u | 2 | 0 | 2 | €1,76 | €0,58 (2x) | **€1,18** | 0.06% | €-18,99 | €-17,81 | -0.89% |
| bitget - gate | €5.000,00 | 2026-11-19 | 14.9 u | 15 | 4 | 9 | €20,82 | €3,69 (11x) | **€17,13** | 0.34% | €16,02 | €33,15 | 0.66% |
| bitget - gate | €5.000,00 | 2026-11-20 | 4.3 u | 2 | 0 | 1 | €3,82 | €0,57 (1x) | **€3,25** | 0.07% | €-47,66 | €-44,41 | -0.89% |
| htx - xt | €100,00 | 2026-11-19 | 14.9 u | 18 | 18 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,08 | €-0,08 | -0.08% |
| htx - xt | €100,00 | 2026-11-20 | 4.3 u | 3 | 3 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,38 | €-1,38 | -1.38% |
| htx - xt | €150,00 | 2026-11-19 | 14.9 u | 18 | 18 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,12 | €-0,12 | -0.08% |
| htx - xt | €150,00 | 2026-11-20 | 4.3 u | 3 | 3 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,07 | €-2,07 | -1.38% |
| htx - xt | €200,00 | 2026-11-19 | 14.9 u | 18 | 14 | 4 | €0,42 | €0,00 (0x) | **€0,42** | 0.21% | €-0,16 | €0,25 | 0.13% |
| htx - xt | €200,00 | 2026-11-20 | 4.3 u | 3 | 3 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,76 | €-2,76 | -1.38% |
| htx - xt | €2.000,00 | 2026-11-19 | 14.9 u | 18 | 5 | 12 | €15,21 | €8,02 (15x) | **€7,19** | 0.36% | €-1,68 | €5,50 | 0.28% |
| htx - xt | €2.000,00 | 2026-11-20 | 4.3 u | 3 | 0 | 3 | €3,34 | €1,18 (3x) | **€2,16** | 0.11% | €-27,30 | €-25,14 | -1.26% |
| htx - xt | €5.000,00 | 2026-11-19 | 14.9 u | 18 | 5 | 12 | €30,14 | €7,56 (14x) | **€22,58** | 0.45% | €-4,16 | €18,42 | 0.37% |
| htx - xt | €5.000,00 | 2026-11-20 | 4.3 u | 3 | 0 | 2 | €6,50 | €2,09 (4x) | **€4,41** | 0.09% | €-68,71 | €-64,30 | -1.29% |
| gate - htx | €100,00 | 2026-11-19 | 14.9 u | 19 | 19 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,89 | €-0,89 | -0.89% |
| gate - htx | €100,00 | 2026-11-20 | 4.3 u | 10 | 10 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,89 | €-1,89 | -1.89% |
| gate - htx | €150,00 | 2026-11-19 | 14.9 u | 19 | 19 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,34 | €-1,34 | -0.89% |
| gate - htx | €150,00 | 2026-11-20 | 4.3 u | 10 | 10 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,83 | €-2,83 | -1.89% |
| gate - htx | €200,00 | 2026-11-19 | 14.9 u | 19 | 19 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,78 | €-1,78 | -0.89% |
| gate - htx | €200,00 | 2026-11-20 | 4.3 u | 10 | 10 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,77 | €-3,77 | -1.89% |
| gate - htx | €2.000,00 | 2026-11-19 | 14.9 u | 19 | 6 | 13 | €7,65 | €4,51 (12x) | **€3,15** | 0.16% | €-17,85 | €-14,70 | -0.74% |
| gate - htx | €2.000,00 | 2026-11-20 | 4.3 u | 10 | 2 | 8 | €3,59 | €1,75 (7x) | **€1,84** | 0.09% | €-37,45 | €-35,61 | -1.78% |
| gate - htx | €5.000,00 | 2026-11-19 | 14.9 u | 19 | 6 | 10 | €16,33 | €5,59 (13x) | **€10,74** | 0.21% | €-44,63 | €-33,89 | -0.68% |
| gate - htx | €5.000,00 | 2026-11-20 | 4.3 u | 10 | 2 | 7 | €8,14 | €2,47 (8x) | **€5,67** | 0.11% | €-93,98 | €-88,31 | -1.77% |

- kucoin - xt, €100,00: munten DAG, FIGHT, LUNC; bruto zonder voorraadgrens zou €549,84 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- kucoin - xt, €150,00: munten DAG, FIGHT, LUNC; bruto zonder voorraadgrens zou €549,84 zijn, met voorraad €0,35 (GEZIEN boek, GOK model).
- kucoin - xt, €200,00: munten DAG, FIGHT, LUNC; bruto zonder voorraadgrens zou €549,84 zijn, met voorraad €0,47 (GEZIEN boek, GOK model).
- kucoin - xt, €2.000,00: munten DAG, FIGHT, LUNC; bruto zonder voorraadgrens zou €544,29 zijn, met voorraad €16,57 (GEZIEN boek, GOK model).
- kucoin - xt, €5.000,00: munten DAG, FIGHT, LUNC; bruto zonder voorraadgrens zou €536,43 zijn, met voorraad €34,70 (GEZIEN boek, GOK model).
- bitget - xt, €100,00: munten KOR, KUB, LUNC; bruto zonder voorraadgrens zou €592,23 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - xt, €150,00: munten KOR, KUB, LUNC; bruto zonder voorraadgrens zou €591,85 zijn, met voorraad €0,49 (GEZIEN boek, GOK model).
- bitget - xt, €200,00: munten KOR, KUB, LUNC; bruto zonder voorraadgrens zou €591,73 zijn, met voorraad €0,65 (GEZIEN boek, GOK model).
- bitget - xt, €2.000,00: munten KOR, KUB, LUNC; bruto zonder voorraadgrens zou €583,92 zijn, met voorraad €14,98 (GEZIEN boek, GOK model).
- bitget - xt, €5.000,00: munten KOR, KUB, LUNC; bruto zonder voorraadgrens zou €573,54 zijn, met voorraad €30,01 (GEZIEN boek, GOK model).
- bitget - gate, €100,00: munten BABYSHARK, IR, IRYS, LUNC, RARE, SNEK, VERONA; bruto zonder voorraadgrens zou €101,13 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - gate, €150,00: munten BABYSHARK, IR, IRYS, LUNC, RARE, SNEK, VERONA; bruto zonder voorraadgrens zou €101,13 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - gate, €200,00: munten BABYSHARK, IR, IRYS, LUNC, RARE, SNEK, VERONA; bruto zonder voorraadgrens zou €101,13 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - gate, €2.000,00: munten BABYSHARK, IR, IRYS, LUNC, RARE, SNEK, VERONA; bruto zonder voorraadgrens zou €97,82 zijn, met voorraad €11,93 (GEZIEN boek, GOK model).
- bitget - gate, €5.000,00: munten BABYSHARK, IR, IRYS, LUNC, RARE, SNEK, VERONA; bruto zonder voorraadgrens zou €94,00 zijn, met voorraad €24,64 (GEZIEN boek, GOK model).
- htx - xt, €100,00: munten CBK, LUNC, SEI, XDC; bruto zonder voorraadgrens zou €97,29 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - xt, €150,00: munten CBK, LUNC, SEI, XDC; bruto zonder voorraadgrens zou €97,29 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - xt, €200,00: munten CBK, LUNC, SEI, XDC; bruto zonder voorraadgrens zou €97,15 zijn, met voorraad €0,42 (GEZIEN boek, GOK model).
- htx - xt, €2.000,00: munten CBK, LUNC, SEI, XDC; bruto zonder voorraadgrens zou €93,65 zijn, met voorraad €18,54 (GEZIEN boek, GOK model).
- htx - xt, €5.000,00: munten CBK, LUNC, SEI, XDC; bruto zonder voorraadgrens zou €90,40 zijn, met voorraad €36,64 (GEZIEN boek, GOK model).
- gate - htx, €100,00: munten BSV, CBK, KAS, LAT, LUNC, MOVR, SEI, WARD, WLD; bruto zonder voorraadgrens zou €82,00 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- gate - htx, €150,00: munten BSV, CBK, KAS, LAT, LUNC, MOVR, SEI, WARD, WLD; bruto zonder voorraadgrens zou €82,00 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- gate - htx, €200,00: munten BSV, CBK, KAS, LAT, LUNC, MOVR, SEI, WARD, WLD; bruto zonder voorraadgrens zou €82,00 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- gate - htx, €2.000,00: munten BSV, CBK, KAS, LAT, LUNC, MOVR, SEI, WARD, WLD; bruto zonder voorraadgrens zou €78,21 zijn, met voorraad €11,25 (GEZIEN boek, GOK model).
- gate - htx, €5.000,00: munten BSV, CBK, KAS, LAT, LUNC, MOVR, SEI, WARD, WLD; bruto zonder voorraadgrens zou €73,57 zijn, met voorraad €24,46 (GEZIEN boek, GOK model).

### Andere keuzes bij bitvavo - kraken (netto handel, alle dagen samen; GOK)

| Keuze | Inleg | Kansen | Gemist | Bruto winst | Kosten terugschuiven | Netto handel |
|---|---|---|---|---|---|---|
| standaard (schuifdrempel 25%, kostengrens 1%) | €150,00 | 49 | 43 | €0,14 | €0,00 | **€0,14** |
| standaard (schuifdrempel 25%, kostengrens 1%) | €2.000,00 | 49 | 31 | €19,57 | €8,01 | **€11,55** |
| schuifdrempel 10% | €150,00 | 49 | 43 | €0,14 | €0,00 | **€0,14** |
| schuifdrempel 10% | €2.000,00 | 49 | 34 | €15,70 | €6,09 | **€9,61** |
| schuifdrempel 40% | €150,00 | 49 | 43 | €0,14 | €0,00 | **€0,14** |
| schuifdrempel 40% | €2.000,00 | 49 | 31 | €16,76 | €8,69 | **€8,07** |
| kostengrens 2% (achteraf vergeleken) | €150,00 | 49 | 43 | €0,14 | €0,00 | **€0,14** |
| kostengrens 2% (achteraf vergeleken) | €2.000,00 | 49 | 20 | €20,20 | €22,44 | **€-2,23** |
| kostengrens 5% (achteraf vergeleken) | €150,00 | 49 | 40 | €0,18 | €2,48 | **€-2,31** |
| kostengrens 5% (achteraf vergeleken) | €2.000,00 | 49 | 20 | €20,20 | €22,44 | **€-2,23** |
| alleen MERL en GMT (meer voorraad per munt, achteraf gekozen) | €150,00 | 34 | 32 | €0,19 | €0,00 | **€0,19** |
| alleen MERL en GMT (meer voorraad per munt, achteraf gekozen) | €2.000,00 | 34 | 16 | €36,39 | €19,09 | **€17,30** |

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

- Opnamekosten bij de echte kansen: 59 van een netwerk dat aan beide kanten open is, 83 van de beurs zelf (laagste open netwerk), 21 geschat uit wat andere beurzen voor die munt vragen (GOK). Onbekende opnamekosten tellen niet als echte kans.
- Netwerk: KuCoin, Gate, Bitget, HTX, XT, Bitstamp, Bitvavo en Poloniex geven hun netwerken per munt. Als beide beurzen dat doen en de namen te koppelen zijn, moet er een netwerk zijn dat aan beide kanten open is. Anders is het netwerk "niet te koppelen" en telt de kans mee (staat apart in de trechter).
- De duur is gemeten in stappen van ±20 seconden; een kans kan een paar rondes eerder begonnen zijn dan we zagen.
- Takerkosten: uit de API waar die ze per paar geeft, anders het standaardtarief uit de README (deels GOK).
- Laatste run: 15 beurzen antwoordden, 2288 munt-quote-paren op minstens twee beurzen (GEZIEN).
