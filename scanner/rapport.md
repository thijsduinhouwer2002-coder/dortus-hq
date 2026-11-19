# Rapport koersverschil-scanner

Gemaakt 2026-11-19 19:38 UTC uit 16 runs, samen ±10.8 uur gemeten (GEZIEN).
Echte kans = winst na alle kosten (opnamekosten bekend), opnemen en storten open (en een netwerk dat aan beide kanten open is, als de beurzen dat geven), minstens €100,00 op het boek, minstens 2 minuten blijven staan, geen andere munt met dezelfde naam.
**Vergund** = beide beurzen hebben een MiCA-vergunning (ESMA-register), vaak via een EU-dochter die minder munten kan hebben dan de wereldwijde API die we meten (GOK). **Grijs** = minstens één beurs zonder vergunning (MEXC, Bitget, HTX, Poloniex, XT, Bitfinex, Binance). Zie README.md.
**Kraken-tarief:** Kraken rekent 0,80% taker op munt tegen EUR, USD, USDT of USDC (GEZIEN, kraken.com/pro/fees, laagste trede); de scanner rekende tot 19 nov met 0,40%. 399 opgeslagen kansen met Kraken uit die runs zijn hier **opnieuw doorgerekend met 0,80%** (GOK-benadering: 0,40% van de inzet aan de Kraken-kant extra op elk gemeten punt van het boek; het boek zelf is niet bewaard). 233 houden daarna nog winst op het boek. Dat ze met hogere kosten ook korter bleven staan, telt niet mee (dus eerder te gunstig).

## Hoeveel wordt er gecontroleerd? (GEZIEN, stand.jsonl)

Per ronde (mediaan over 130 metingen): 1054 kandidaten (verschil op de ticker groter dan de takerkosten), 120 met het orderboek gecontroleerd, 2 nog nooit gecontroleerd (0%).
Bijna alle kandidaten komen aan de beurt; de aantallen hieronder missen weinig.

## Trechter (GEZIEN, eigen metingen)

| Stap | Alle beurzen | Alleen MiCA-beurzen | Met minstens één grijze beurs |
|---|---|---|---|
| Verschillen met winst op het boek na alle kosten | 10278 | 1378 | 8900 |
| ...waarvan opnemen of storten dicht | 2436 | 223 | 2213 |
| ...waarvan status onbekend (beurs geeft het niet openbaar) | 5907 | 940 | 4967 |
| Opnemen en storten open | 1935 | 215 | 1720 |
| ...en geen netwerk dat aan beide kanten open is: valt af | 24 | 1 | 23 |
| ...en opnamekosten onbekend: valt af | 0 | 0 | 0 |
| ...en minstens €100,00 op het boek | 568 | 124 | 444 |
| ...en minstens 2 minuten blijven staan | 190 | 66 | 124 |
| ...en geen andere munt met dezelfde naam | 167 | 56 | 111 |
|    ...waarvan contractadres bekend en gelijk | 14 | 2 | 12 |
|    ...waarvan contractadres onbekend (telt mee, kan een andere munt zijn) | 153 | 54 | 99 |
|    ...waarvan netwerk gekoppeld en open | 98 | 18 | 80 |
|    ...waarvan netwerk niet te koppelen (telt mee) | 69 | 38 | 31 |
| **Echte kansen** (zelfde munt overlappend in de tijd samengevoegd, beste beurspaar telt) | 112 | 56 | 70 |
| Ter vergelijking: zelfde eisen, maar opnamestatus onbekend (niet meegeteld) | 307 | 72 | 260 |

## Echte kansen per dag (GEZIEN)

| Dag | Echt, alleen MiCA | Echt, met grijs | Mediane winst per kans bij €500 (MiCA / grijs) | Mediane duur |
|---|---|---|---|---|
| 2026-11-19 | 42 | 70 | €1,86 / €1,04 | 5.3 min |
| Totaal | 42 | 70 | €1,86 / €1,04 | 5.3 min |

## Beste munten (GEZIEN)

| | Soort | Kansen | Som winst bij €500 per kans |
|---|---|---|---|
| MERL-EUR | vergund | 13 | €135,36 |
| LUNC-USDT | grijs | 12 | €44,83 |
| USTC-USDT | grijs en vergund | 8 | €24,71 |
| YB-USDT | grijs | 1 | €16,34 |
| WAN-USDT | grijs | 4 | €14,24 |
| GMT-EUR | vergund | 9 | €13,20 |
| VERONA-USDT | grijs en vergund | 8 | €12,47 |
| AVA-EUR | vergund | 4 | €11,22 |
| LUNA-EUR | vergund | 4 | €10,37 |
| WARD-USDT | grijs | 8 | €9,53 |

## Beste beursparen (kopen op > verkopen op) (GEZIEN)

| | Soort | Kansen | Som winst bij €500 per kans |
|---|---|---|---|
| bitvavo > kraken | vergund | 37 | €174,10 |
| kucoin > bitget | grijs | 9 | €24,65 |
| bitget > gate | grijs | 6 | €23,63 |
| kucoin > htx | grijs | 10 | €22,49 |
| gate > xt | grijs | 2 | €19,11 |
| bitget > xt | grijs | 4 | €13,09 |
| htx > xt | grijs | 4 | €10,41 |
| bitget > htx | grijs | 12 | €8,17 |
| kucoin > xt | grijs | 2 | €7,99 |
| bitget > kucoin | grijs | 7 | €5,71 |

Beurzen die het vaakst meedoen (koop of verkoop): bitget (grijs) 40, bitvavo 37, kraken 37, kucoin 36, htx (grijs) 36, gate 19, xt (grijs) 17, poloniex (grijs) 2 (GEZIEN).

## Hoeveel kansen blijven staan terwijl je geld schuift? (GEZIEN, duur uit eigen metingen)

Wie geen voorraad op beide beurzen heeft, moet kopen, de munt opnemen, wachten tot hij binnen is en dan verkopen. Hoe lang dat duurt verschilt per munt en netwerk: een paar minuten (snelle ketens) tot een uur of meer (Bitcoin, beurzen die opnames met de hand keuren) (GOK, niet per munt gemeten).

| Overmaaktijd | Alle beurzen | Alleen MiCA-beurzen | Met minstens één grijze beurs |
|---|---|---|---|
| 5 min | 59 van 112 (53%) | 29 van 56 (52%) | 35 van 70 (50%) |
| 10 min | 30 van 112 (27%) | 18 van 56 (32%) | 15 van 70 (21%) |
| 30 min | 20 van 112 (18%) | 14 van 56 (25%) | 8 van 70 (11%) |
| 60 min | 6 van 112 (5%) | 5 van 56 (9%) | 2 van 70 (3%) |

## Wat zou het opleveren over 3 maanden? (GOK, doorgetrokken uit de metingen)

Gemeten over ±10.8 uur (GEZIEN), doorgetrokken naar 90 dagen (GOK: aanname dat de week die we maten gewoon is).

| Beurzen | Inleg | Model | Kansen per uur | Per kans (mediaan) | 3 maanden |
|---|---|---|---|---|---|
| Alleen MiCA | €2.000,00 | bovengrens: elke kans, geld overal tegelijk | 5.17 | €2,73 | €30.456,02 |
| Alleen MiCA | €2.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 3.42 | €3,15 | €55.388,46 |
| Alleen MiCA | €5.000,00 | bovengrens: elke kans, geld overal tegelijk | 5.17 | €3,05 | €34.089,19 |
| Alleen MiCA | €5.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 3.42 | €3,52 | €79.948,13 |
| Alle (met grijs) | €2.000,00 | bovengrens: elke kans, geld overal tegelijk | 10.34 | €1,54 | €34.476,07 |
| Alle (met grijs) | €2.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 3.42 | €3,15 | €55.388,46 |
| Alle (met grijs) | €5.000,00 | bovengrens: elke kans, geld overal tegelijk | 10.34 | €1,71 | €38.223,12 |
| Alle (met grijs) | €5.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 3.42 | €3,52 | €79.948,13 |

Bovengrens: elke kans met de helft van de inleg aan elke kant, alsof het geld op alle beurzen tegelijk staat (kan in het echt niet). Beste beurspaar: het paar is **achteraf** gekozen uit de metingen (vooraf kiezen levert minder op), en het model neemt aan dat je van elke munt al voorraad op de verkoopbeurs hebt.

Waarom dit te rooskleurig is (GOK): elke kans wordt maar één keer geteld met het mediane boek, maar andere bots pakken hem ook; de munt die je als voorraad aanhoudt kan dalen; na een paar kansen moet de voorraad terug (opnamekosten en tijd); minimale opname- en ordergroottes tellen niet mee; en een kans die we 2 minuten zagen staan, staat er niet per se nog als jouw order binnenkomt. Waarom het te somber kan zijn: niet alle kandidaten zijn gecontroleerd, en met voorraad op beide beurzen kun je dezelfde kans vaker pakken als het boek zich aanvult; dat telt hier niet mee.

## Wat houd je echt over? Voorraad op twee beurzen (simulatie)

Per beurspaar: geld en munten op beide beurzen, elke echte kans uitgevoerd tegen het boek zoals gemeten (niet meer dan de ruimte op het boek en niet meer dan de voorraad op die beurs), terugschuiven als een kant leeg dreigt te raken (met opnamekosten en tijd onderweg), en het koerseffect van de aangehouden munten apart. Netto = bruto min kosten terugschuiven plus koerseffect. **Gemeten** (GEZIEN): de kansen, het boek en de koersen; **de rest is een rekenmodel** (GOK, aannames onder de tabel). Geen advies.

**Met €150: netto €0,14 per dag op bitvavo - kraken (koerseffect erbovenop €-0,66), €0,39 per dag op gate - kucoin (koerseffect erbovenop €-1,74) (GOK: netto handel, rekenmodel op ±10.8 uur meting per dag, alleen MiCA).** "Per dag" is hier één gemeten dag die begint met een gelijk verdeelde voorraad; aan het eind staat de voorraad scheef, dus een volgende dag levert waarschijnlijk minder op, tenzij kansen de andere kant op hem terugbrengen (GOK).

### Alleen MiCA-beurzen (alle paren met echte kansen)

| Beurspaar | Inleg | Dag | Gemeten | Kansen | Gemist (geen voorraad) | Kleiner door voorraad | Bruto winst | Kosten terugschuiven | **Netto handel (bruto min kosten)** | Rendement handel | Koerseffect voorraad | Netto met koerseffect | Rendement met koerseffect |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| bitvavo - kraken | €100,00 | 2026-11-19 | 10.8 u | 37 | 37 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,44 | €-0,44 | -0.44% |
| bitvavo - kraken | €150,00 | 2026-11-19 | 10.8 u | 37 | 31 | 6 | €0,14 | €0,00 (0x) | **€0,14** | 0.09% | €-0,66 | €-0,52 | -0.35% |
| bitvavo - kraken | €200,00 | 2026-11-19 | 10.8 u | 37 | 31 | 6 | €0,19 | €0,00 (0x) | **€0,19** | 0.09% | €-0,88 | €-0,69 | -0.35% |
| bitvavo - kraken | €2.000,00 | 2026-11-19 | 10.8 u | 37 | 22 | 15 | €12,21 | €7,04 (16x) | **€5,16** | 0.26% | €-8,72 | €-3,55 | -0.18% |
| bitvavo - kraken | €5.000,00 | 2026-11-19 | 10.8 u | 37 | 18 | 19 | €23,05 | €11,62 (20x) | **€11,43** | 0.23% | €-21,85 | €-10,42 | -0.21% |
| gate - kucoin | €100,00 | 2026-11-19 | 10.8 u | 19 | 12 | 7 | €0,26 | €0,00 (0x) | **€0,26** | 0.26% | €-1,16 | €-0,90 | -0.90% |
| gate - kucoin | €150,00 | 2026-11-19 | 10.8 u | 19 | 12 | 7 | €0,39 | €0,00 (0x) | **€0,39** | 0.26% | €-1,74 | €-1,35 | -0.90% |
| gate - kucoin | €200,00 | 2026-11-19 | 10.8 u | 19 | 12 | 7 | €0,52 | €0,00 (0x) | **€0,52** | 0.26% | €-2,32 | €-1,80 | -0.90% |
| gate - kucoin | €2.000,00 | 2026-11-19 | 10.8 u | 19 | 6 | 13 | €8,28 | €4,02 (14x) | **€4,26** | 0.21% | €-23,19 | €-18,93 | -0.95% |
| gate - kucoin | €5.000,00 | 2026-11-19 | 10.8 u | 19 | 4 | 10 | €17,16 | €3,65 (12x) | **€13,51** | 0.27% | €-57,98 | €-44,47 | -0.89% |

- bitvavo - kraken, €100,00: munten AVA, DYM, GMT, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €533,03 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitvavo - kraken, €150,00: munten AVA, DYM, GMT, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €532,62 zijn, met voorraad €0,14 (GEZIEN boek, GOK model).
- bitvavo - kraken, €200,00: munten AVA, DYM, GMT, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €532,48 zijn, met voorraad €0,19 (GEZIEN boek, GOK model).
- bitvavo - kraken, €2.000,00: munten AVA, DYM, GMT, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €512,79 zijn, met voorraad €12,21 (GEZIEN boek, GOK model).
- bitvavo - kraken, €5.000,00: munten AVA, DYM, GMT, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €479,79 zijn, met voorraad €23,05 (GEZIEN boek, GOK model).
- gate - kucoin, €100,00: munten ALKIMI, ERG, IR, LUNC, USTC, VERONA; bruto zonder voorraadgrens zou €63,54 zijn, met voorraad €0,26 (GEZIEN boek, GOK model).
- gate - kucoin, €150,00: munten ALKIMI, ERG, IR, LUNC, USTC, VERONA; bruto zonder voorraadgrens zou €63,54 zijn, met voorraad €0,39 (GEZIEN boek, GOK model).
- gate - kucoin, €200,00: munten ALKIMI, ERG, IR, LUNC, USTC, VERONA; bruto zonder voorraadgrens zou €63,54 zijn, met voorraad €0,52 (GEZIEN boek, GOK model).
- gate - kucoin, €2.000,00: munten ALKIMI, ERG, IR, LUNC, USTC, VERONA; bruto zonder voorraadgrens zou €61,49 zijn, met voorraad €8,28 (GEZIEN boek, GOK model).
- gate - kucoin, €5.000,00: munten ALKIMI, ERG, IR, LUNC, USTC, VERONA; bruto zonder voorraadgrens zou €59,30 zijn, met voorraad €17,16 (GEZIEN boek, GOK model).

### Met minstens één grijze beurs (de 5 paren met de meeste bruto winst)

| Beurspaar | Inleg | Dag | Gemeten | Kansen | Gemist (geen voorraad) | Kleiner door voorraad | Bruto winst | Kosten terugschuiven | **Netto handel (bruto min kosten)** | Rendement handel | Koerseffect voorraad | Netto met koerseffect | Rendement met koerseffect |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| kucoin - xt | €100,00 | 2026-11-19 | 10.8 u | 10 | 10 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,09 | €0,09 | 0.09% |
| kucoin - xt | €150,00 | 2026-11-19 | 10.8 u | 10 | 7 | 3 | €0,35 | €0,00 (0x) | **€0,35** | 0.24% | €0,14 | €0,49 | 0.33% |
| kucoin - xt | €200,00 | 2026-11-19 | 10.8 u | 10 | 7 | 3 | €0,47 | €0,00 (0x) | **€0,47** | 0.24% | €0,19 | €0,66 | 0.33% |
| kucoin - xt | €2.000,00 | 2026-11-19 | 10.8 u | 10 | 3 | 7 | €10,48 | €4,47 (8x) | **€6,01** | 0.30% | €1,88 | €7,89 | 0.39% |
| kucoin - xt | €5.000,00 | 2026-11-19 | 10.8 u | 10 | 2 | 7 | €23,08 | €4,13 (7x) | **€18,94** | 0.38% | €4,69 | €23,63 | 0.47% |
| bitget - xt | €100,00 | 2026-11-19 | 10.8 u | 8 | 6 | 2 | €0,31 | €0,11 (2x) | **€0,20** | 0.20% | €2,54 | €2,74 | 2.74% |
| bitget - xt | €150,00 | 2026-11-19 | 10.8 u | 8 | 6 | 2 | €0,46 | €0,11 (2x) | **€0,35** | 0.24% | €3,81 | €4,16 | 2.77% |
| bitget - xt | €200,00 | 2026-11-19 | 10.8 u | 8 | 6 | 2 | €0,62 | €0,11 (2x) | **€0,51** | 0.25% | €5,08 | €5,59 | 2.79% |
| bitget - xt | €2.000,00 | 2026-11-19 | 10.8 u | 8 | 4 | 3 | €6,20 | €0,92 (3x) | **€5,29** | 0.26% | €50,81 | €56,10 | 2.80% |
| bitget - xt | €5.000,00 | 2026-11-19 | 10.8 u | 8 | 4 | 3 | €17,45 | €0,92 (4x) | **€16,54** | 0.33% | €127,02 | €143,56 | 2.87% |
| bitget - gate | €100,00 | 2026-11-19 | 10.8 u | 11 | 11 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,50 | €-0,50 | -0.50% |
| bitget - gate | €150,00 | 2026-11-19 | 10.8 u | 11 | 11 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,75 | €-0,75 | -0.50% |
| bitget - gate | €200,00 | 2026-11-19 | 10.8 u | 11 | 7 | 4 | €0,54 | €0,02 (2x) | **€0,52** | 0.26% | €-0,99 | €-0,47 | -0.24% |
| bitget - gate | €2.000,00 | 2026-11-19 | 10.8 u | 11 | 4 | 6 | €9,36 | €2,37 (9x) | **€6,99** | 0.35% | €-9,96 | €-2,97 | -0.15% |
| bitget - gate | €5.000,00 | 2026-11-19 | 10.8 u | 11 | 3 | 6 | €15,55 | €1,25 (6x) | **€14,30** | 0.29% | €-24,89 | €-10,58 | -0.21% |
| htx - xt | €100,00 | 2026-11-19 | 10.8 u | 16 | 16 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,07 | €0,07 | 0.07% |
| htx - xt | €150,00 | 2026-11-19 | 10.8 u | 16 | 16 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,10 | €0,10 | 0.07% |
| htx - xt | €200,00 | 2026-11-19 | 10.8 u | 16 | 12 | 4 | €0,42 | €0,00 (0x) | **€0,42** | 0.21% | €0,13 | €0,55 | 0.28% |
| htx - xt | €2.000,00 | 2026-11-19 | 10.8 u | 16 | 5 | 10 | €11,99 | €6,31 (12x) | **€5,67** | 0.28% | €1,28 | €6,95 | 0.35% |
| htx - xt | €5.000,00 | 2026-11-19 | 10.8 u | 16 | 5 | 10 | €22,72 | €5,86 (11x) | **€16,87** | 0.34% | €3,25 | €20,12 | 0.40% |
| bitget - kucoin | €100,00 | 2026-11-19 | 10.8 u | 18 | 18 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,47 | €-1,47 | -1.47% |
| bitget - kucoin | €150,00 | 2026-11-19 | 10.8 u | 18 | 18 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,20 | €-2,20 | -1.47% |
| bitget - kucoin | €200,00 | 2026-11-19 | 10.8 u | 18 | 18 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,93 | €-2,93 | -1.47% |
| bitget - kucoin | €2.000,00 | 2026-11-19 | 10.8 u | 18 | 7 | 11 | €4,76 | €2,05 (10x) | **€2,71** | 0.14% | €-29,32 | €-26,61 | -1.33% |
| bitget - kucoin | €5.000,00 | 2026-11-19 | 10.8 u | 18 | 7 | 9 | €9,84 | €8,30 (17x) | **€1,54** | 0.03% | €-73,27 | €-71,73 | -1.43% |

- kucoin - xt, €100,00: munten DAG, FIGHT, LUNC; bruto zonder voorraadgrens zou €417,39 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- kucoin - xt, €150,00: munten DAG, FIGHT, LUNC; bruto zonder voorraadgrens zou €417,39 zijn, met voorraad €0,35 (GEZIEN boek, GOK model).
- kucoin - xt, €200,00: munten DAG, FIGHT, LUNC; bruto zonder voorraadgrens zou €417,39 zijn, met voorraad €0,47 (GEZIEN boek, GOK model).
- kucoin - xt, €2.000,00: munten DAG, FIGHT, LUNC; bruto zonder voorraadgrens zou €413,75 zijn, met voorraad €10,48 (GEZIEN boek, GOK model).
- kucoin - xt, €5.000,00: munten DAG, FIGHT, LUNC; bruto zonder voorraadgrens zou €408,45 zijn, met voorraad €23,08 (GEZIEN boek, GOK model).
- bitget - xt, €100,00: munten KOR, LUNC; bruto zonder voorraadgrens zou €388,15 zijn, met voorraad €0,31 (GEZIEN boek, GOK model).
- bitget - xt, €150,00: munten KOR, LUNC; bruto zonder voorraadgrens zou €388,10 zijn, met voorraad €0,46 (GEZIEN boek, GOK model).
- bitget - xt, €200,00: munten KOR, LUNC; bruto zonder voorraadgrens zou €388,05 zijn, met voorraad €0,62 (GEZIEN boek, GOK model).
- bitget - xt, €2.000,00: munten KOR, LUNC; bruto zonder voorraadgrens zou €383,10 zijn, met voorraad €6,20 (GEZIEN boek, GOK model).
- bitget - xt, €5.000,00: munten KOR, LUNC; bruto zonder voorraadgrens zou €372,45 zijn, met voorraad €17,45 (GEZIEN boek, GOK model).
- bitget - gate, €100,00: munten BABYSHARK, IR, LUNC, VERONA; bruto zonder voorraadgrens zou €63,45 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - gate, €150,00: munten BABYSHARK, IR, LUNC, VERONA; bruto zonder voorraadgrens zou €63,45 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - gate, €200,00: munten BABYSHARK, IR, LUNC, VERONA; bruto zonder voorraadgrens zou €63,34 zijn, met voorraad €0,54 (GEZIEN boek, GOK model).
- bitget - gate, €2.000,00: munten BABYSHARK, IR, LUNC, VERONA; bruto zonder voorraadgrens zou €59,54 zijn, met voorraad €9,36 (GEZIEN boek, GOK model).
- bitget - gate, €5.000,00: munten BABYSHARK, IR, LUNC, VERONA; bruto zonder voorraadgrens zou €60,33 zijn, met voorraad €15,55 (GEZIEN boek, GOK model).
- htx - xt, €100,00: munten CBK, LUNC, SEI, XDC; bruto zonder voorraadgrens zou €54,94 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - xt, €150,00: munten CBK, LUNC, SEI, XDC; bruto zonder voorraadgrens zou €54,94 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - xt, €200,00: munten CBK, LUNC, SEI, XDC; bruto zonder voorraadgrens zou €54,80 zijn, met voorraad €0,42 (GEZIEN boek, GOK model).
- htx - xt, €2.000,00: munten CBK, LUNC, SEI, XDC; bruto zonder voorraadgrens zou €51,29 zijn, met voorraad €11,99 (GEZIEN boek, GOK model).
- htx - xt, €5.000,00: munten CBK, LUNC, SEI, XDC; bruto zonder voorraadgrens zou €48,05 zijn, met voorraad €22,72 (GEZIEN boek, GOK model).
- bitget - kucoin, €100,00: munten EGL1, KLV, LUNC, MTX, USDT, USTC, VERONA; bruto zonder voorraadgrens zou €46,42 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - kucoin, €150,00: munten EGL1, KLV, LUNC, MTX, USDT, USTC, VERONA; bruto zonder voorraadgrens zou €46,42 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - kucoin, €200,00: munten EGL1, KLV, LUNC, MTX, USDT, USTC, VERONA; bruto zonder voorraadgrens zou €46,42 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - kucoin, €2.000,00: munten EGL1, KLV, LUNC, MTX, USDT, USTC, VERONA; bruto zonder voorraadgrens zou €44,27 zijn, met voorraad €4,76 (GEZIEN boek, GOK model).
- bitget - kucoin, €5.000,00: munten EGL1, KLV, LUNC, MTX, USDT, USTC, VERONA; bruto zonder voorraadgrens zou €41,88 zijn, met voorraad €9,84 (GEZIEN boek, GOK model).

### Andere keuzes bij bitvavo - kraken (netto handel, alle dagen samen; GOK)

| Keuze | Inleg | Kansen | Gemist | Bruto winst | Kosten terugschuiven | Netto handel |
|---|---|---|---|---|---|---|
| standaard (schuifdrempel 25%, kostengrens 1%) | €150,00 | 37 | 31 | €0,14 | €0,00 | **€0,14** |
| standaard (schuifdrempel 25%, kostengrens 1%) | €2.000,00 | 37 | 22 | €12,21 | €7,04 | **€5,16** |
| schuifdrempel 10% | €150,00 | 37 | 31 | €0,14 | €0,00 | **€0,14** |
| schuifdrempel 10% | €2.000,00 | 37 | 25 | €8,32 | €5,12 | **€3,20** |
| schuifdrempel 40% | €150,00 | 37 | 31 | €0,14 | €0,00 | **€0,14** |
| schuifdrempel 40% | €2.000,00 | 37 | 22 | €9,55 | €6,72 | **€2,83** |
| kostengrens 2% (achteraf vergeleken) | €150,00 | 37 | 31 | €0,14 | €0,00 | **€0,14** |
| kostengrens 2% (achteraf vergeleken) | €2.000,00 | 37 | 19 | €11,21 | €11,62 | **€-0,41** |
| kostengrens 5% (achteraf vergeleken) | €150,00 | 37 | 28 | €0,18 | €2,48 | **€-2,31** |
| kostengrens 5% (achteraf vergeleken) | €2.000,00 | 37 | 19 | €11,21 | €11,62 | **€-0,41** |
| alleen MERL en GMT (meer voorraad per munt, achteraf gekozen) | €150,00 | 22 | 20 | €0,19 | €0,00 | **€0,19** |
| alleen MERL en GMT (meer voorraad per munt, achteraf gekozen) | €2.000,00 | 22 | 14 | €17,72 | €8,56 | **€9,16** |

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
- Geld terugschuiven per beurs: bitget EUR: 1 EUR, GOK (1 EUR, 24 uur; niet nagekeken); bitget USDT: 1 USDT, GOK (1 USDT, 30 min; niet nagekeken); bitvavo EUR: 0 EUR, kosten GEZIEN (api.bitvavo.com/v2/assets: EUR withdrawalFee 0), tijd GOK (1 werkdag, SEPA), minimum 0 EUR (GEZIEN, api.bitvavo.com/v2/assets withdrawalMinAmount); gate USDT: 1 USDT, GOK (1 USDT, 30 min; niet nagekeken), minimum 1 USDT (GEZIEN, api.gateio.ws/api/v4/wallet/currency_chains withdraw_amount_min); htx USDT: 1 USDT, GOK (1 USDT, 30 min; niet nagekeken); kraken EUR: 1 EUR, kosten GEZIEN (support.kraken.com/articles/360000381846: Instant SEPA, Banking Circle, 1 EUR, near-instant), tijd GOK (1 uur tot het op de andere beurs staat), minimum 2 EUR (GEZIEN, support.kraken.com/articles/360000381846 Instant SEPA (Banking Circle)); kucoin EUR: 1 EUR, GOK (1 EUR, 24 uur; niet nagekeken); kucoin USDT: 1 USDT, kosten GEZIEN (api.kucoin.com/api/v3/currencies/USDT: BEP20 1 USDT), tijd GOK, minimum 5 USDT (GEZIEN, api.kucoin.com/api/v3/currencies/USDT BEP20 withdrawalMinSize); xt USDT: 1 USDT, GOK (1 USDT, 30 min; niet nagekeken).

## Over de meting

- Opnamekosten bij de echte kansen: 42 van een netwerk dat aan beide kanten open is, 55 van de beurs zelf (laagste open netwerk), 15 geschat uit wat andere beurzen voor die munt vragen (GOK). Onbekende opnamekosten tellen niet als echte kans.
- Netwerk: KuCoin, Gate, Bitget, HTX, XT, Bitstamp, Bitvavo en Poloniex geven hun netwerken per munt. Als beide beurzen dat doen en de namen te koppelen zijn, moet er een netwerk zijn dat aan beide kanten open is. Anders is het netwerk "niet te koppelen" en telt de kans mee (staat apart in de trechter).
- De duur is gemeten in stappen van ±20 seconden; een kans kan een paar rondes eerder begonnen zijn dan we zagen.
- Takerkosten: uit de API waar die ze per paar geeft, anders het standaardtarief uit de README (deels GOK).
- Laatste run: 15 beurzen antwoordden, 2287 munt-quote-paren op minstens twee beurzen (GEZIEN).
