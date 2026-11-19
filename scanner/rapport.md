# Rapport koersverschil-scanner

Gemaakt 2026-11-19 15:58 UTC uit 14 runs, samen ±7.1 uur gemeten (GEZIEN).
Echte kans = winst na alle kosten (opnamekosten bekend), opnemen en storten open (en een netwerk dat aan beide kanten open is, als de beurzen dat geven), minstens €100,00 op het boek, minstens 2 minuten blijven staan, geen andere munt met dezelfde naam.
**Vergund** = beide beurzen hebben een MiCA-vergunning (ESMA-register), vaak via een EU-dochter die minder munten kan hebben dan de wereldwijde API die we meten (GOK). **Grijs** = minstens één beurs zonder vergunning (MEXC, Bitget, HTX, Poloniex, XT, Bitfinex, Binance). Zie README.md.
**Kraken-tarief:** Kraken rekent 0,80% taker op munt tegen EUR, USD, USDT of USDC (GEZIEN, kraken.com/pro/fees, laagste trede); de scanner rekende tot 19 nov met 0,40%. 399 opgeslagen kansen met Kraken uit die runs zijn hier **opnieuw doorgerekend met 0,80%** (GOK-benadering: 0,40% van de inzet aan de Kraken-kant extra op elk gemeten punt van het boek; het boek zelf is niet bewaard). 233 houden daarna nog winst op het boek. Dat ze met hogere kosten ook korter bleven staan, telt niet mee (dus eerder te gunstig).

## Hoeveel wordt er gecontroleerd? (GEZIEN, stand.jsonl)

Per ronde (mediaan over 85 metingen): 1047 kandidaten (verschil op de ticker groter dan de takerkosten), 120 met het orderboek gecontroleerd, 3 nog nooit gecontroleerd (0%).
Bijna alle kandidaten komen aan de beurt; de aantallen hieronder missen weinig.

## Trechter (GEZIEN, eigen metingen)

| Stap | Alle beurzen | Alleen MiCA-beurzen | Met minstens één grijze beurs |
|---|---|---|---|
| Verschillen met winst op het boek na alle kosten | 6895 | 879 | 6016 |
| ...waarvan opnemen of storten dicht | 1624 | 147 | 1477 |
| ...waarvan status onbekend (beurs geeft het niet openbaar) | 3789 | 558 | 3231 |
| Opnemen en storten open | 1482 | 174 | 1308 |
| ...en geen netwerk dat aan beide kanten open is: valt af | 22 | 1 | 21 |
| ...en opnamekosten onbekend: valt af | 0 | 0 | 0 |
| ...en minstens €100,00 op het boek | 447 | 101 | 346 |
| ...en minstens 2 minuten blijven staan | 147 | 56 | 91 |
| ...en geen andere munt met dezelfde naam | 127 | 47 | 80 |
|    ...waarvan contractadres bekend en gelijk | 8 | 1 | 7 |
|    ...waarvan contractadres onbekend (telt mee, kan een andere munt zijn) | 119 | 46 | 73 |
|    ...waarvan netwerk gekoppeld en open | 67 | 12 | 55 |
|    ...waarvan netwerk niet te koppelen (telt mee) | 60 | 35 | 25 |
| **Echte kansen** (zelfde munt overlappend in de tijd samengevoegd, beste beurspaar telt) | 82 | 47 | 47 |
| Ter vergelijking: zelfde eisen, maar opnamestatus onbekend (niet meegeteld) | 188 | 49 | 158 |

## Echte kansen per dag (GEZIEN)

| Dag | Echt, alleen MiCA | Echt, met grijs | Mediane winst per kans bij €500 (MiCA / grijs) | Mediane duur |
|---|---|---|---|---|
| 2026-11-19 | 35 | 47 | €2,02 / €1,20 | 5.0 min |
| Totaal | 35 | 47 | €2,02 / €1,20 | 5.0 min |

## Beste munten (GEZIEN)

| | Soort | Kansen | Som winst bij €500 per kans |
|---|---|---|---|
| MERL-EUR | vergund | 12 | €120,76 |
| LUNC-USDT | grijs | 7 | €34,44 |
| USTC-USDT | grijs | 5 | €19,89 |
| YB-USDT | grijs | 1 | €16,34 |
| WAN-USDT | grijs | 3 | €12,65 |
| VERONA-USDT | grijs | 7 | €11,93 |
| AVA-EUR | vergund | 4 | €11,22 |
| LUNA-EUR | vergund | 4 | €10,37 |
| GMT-EUR | vergund | 7 | €9,70 |
| WARD-USDT | grijs | 2 | €5,46 |

## Beste beursparen (kopen op > verkopen op) (GEZIEN)

| | Soort | Kansen | Som winst bij €500 per kans |
|---|---|---|---|
| bitvavo > kraken | vergund | 34 | €156,00 |
| kucoin > bitget | grijs | 7 | €20,42 |
| kucoin > htx | grijs | 7 | €19,11 |
| bitget > gate | grijs | 5 | €18,41 |
| gate > xt | grijs | 1 | €16,34 |
| bitget > xt | grijs | 4 | €13,09 |
| kucoin > xt | grijs | 1 | €6,56 |
| htx > xt | grijs | 1 | €5,83 |
| bitget > htx | grijs | 7 | €5,51 |
| bitget > kucoin | grijs | 6 | €3,67 |

Beurzen die het vaakst meedoen (koop of verkoop): bitvavo 34, kraken 34, bitget (grijs) 29, kucoin 24, htx (grijs) 21, gate 10, xt (grijs) 10, poloniex (grijs) 2 (GEZIEN).

## Hoeveel kansen blijven staan terwijl je geld schuift? (GEZIEN, duur uit eigen metingen)

Wie geen voorraad op beide beurzen heeft, moet kopen, de munt opnemen, wachten tot hij binnen is en dan verkopen. Hoe lang dat duurt verschilt per munt en netwerk: een paar minuten (snelle ketens) tot een uur of meer (Bitcoin, beurzen die opnames met de hand keuren) (GOK, niet per munt gemeten).

| Overmaaktijd | Alle beurzen | Alleen MiCA-beurzen | Met minstens één grijze beurs |
|---|---|---|---|
| 5 min | 42 van 82 (51%) | 22 van 47 (47%) | 24 van 47 (51%) |
| 10 min | 18 van 82 (22%) | 12 van 47 (26%) | 8 van 47 (17%) |
| 30 min | 14 van 82 (17%) | 10 van 47 (21%) | 5 van 47 (11%) |
| 60 min | 5 van 82 (6%) | 4 van 47 (9%) | 2 van 47 (4%) |

## Wat zou het opleveren over 3 maanden? (GOK, doorgetrokken uit de metingen)

Gemeten over ±7.1 uur (GEZIEN), doorgetrokken naar 90 dagen (GOK: aanname dat de week die we maten gewoon is).

| Beurzen | Inleg | Model | Kansen per uur | Per kans (mediaan) | 3 maanden |
|---|---|---|---|---|---|
| Alleen MiCA | €2.000,00 | bovengrens: elke kans, geld overal tegelijk | 6.64 | €3,01 | €43.096,77 |
| Alleen MiCA | €2.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 4.80 | €3,12 | €75.724,90 |
| Alleen MiCA | €5.000,00 | bovengrens: elke kans, geld overal tegelijk | 6.64 | €3,10 | €44.416,72 |
| Alleen MiCA | €5.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 4.80 | €3,28 | €109.003,05 |
| Alle (met grijs) | €2.000,00 | bovengrens: elke kans, geld overal tegelijk | 11.58 | €2,30 | €57.443,39 |
| Alle (met grijs) | €2.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 4.80 | €3,12 | €75.724,90 |
| Alle (met grijs) | €5.000,00 | bovengrens: elke kans, geld overal tegelijk | 11.58 | €2,85 | €71.319,47 |
| Alle (met grijs) | €5.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 4.80 | €3,28 | €109.003,05 |

Bovengrens: elke kans met de helft van de inleg aan elke kant, alsof het geld op alle beurzen tegelijk staat (kan in het echt niet). Beste beurspaar: het paar is **achteraf** gekozen uit de metingen (vooraf kiezen levert minder op), en het model neemt aan dat je van elke munt al voorraad op de verkoopbeurs hebt.

Waarom dit te rooskleurig is (GOK): elke kans wordt maar één keer geteld met het mediane boek, maar andere bots pakken hem ook; de munt die je als voorraad aanhoudt kan dalen; na een paar kansen moet de voorraad terug (opnamekosten en tijd); minimale opname- en ordergroottes tellen niet mee; en een kans die we 2 minuten zagen staan, staat er niet per se nog als jouw order binnenkomt. Waarom het te somber kan zijn: niet alle kandidaten zijn gecontroleerd, en met voorraad op beide beurzen kun je dezelfde kans vaker pakken als het boek zich aanvult; dat telt hier niet mee.

## Wat houd je echt over? Voorraad op twee beurzen (simulatie)

Per beurspaar: geld en munten op beide beurzen, elke echte kans uitgevoerd tegen het boek zoals gemeten (niet meer dan de ruimte op het boek en niet meer dan de voorraad op die beurs), terugschuiven als een kant leeg dreigt te raken (met opnamekosten en tijd onderweg), en het koerseffect van de aangehouden munten apart. Netto = bruto min kosten terugschuiven plus koerseffect. **Gemeten** (GEZIEN): de kansen, het boek en de koersen; **de rest is een rekenmodel** (GOK, aannames onder de tabel). Geen advies.

**Met €150: netto €0,14 per dag op bitvavo - kraken (koerseffect erbovenop €-0,56), €0,40 per dag op gate - kucoin (koerseffect erbovenop €-0,35) (GOK: netto handel, rekenmodel op ±7.1 uur meting per dag, alleen MiCA).** "Per dag" is hier één gemeten dag die begint met een gelijk verdeelde voorraad; aan het eind staat de voorraad scheef, dus een volgende dag levert waarschijnlijk minder op, tenzij kansen de andere kant op hem terugbrengen (GOK).

### Alleen MiCA-beurzen (alle paren met echte kansen)

| Beurspaar | Inleg | Dag | Gemeten | Kansen | Gemist (geen voorraad) | Kleiner door voorraad | Bruto winst | Kosten terugschuiven | **Netto handel (bruto min kosten)** | Rendement handel | Koerseffect voorraad | Netto met koerseffect | Rendement met koerseffect |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| bitvavo - kraken | €100,00 | 2026-11-19 | 7.1 u | 34 | 34 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,37 | €-0,37 | -0.37% |
| bitvavo - kraken | €150,00 | 2026-11-19 | 7.1 u | 34 | 28 | 6 | €0,14 | €0,00 (0x) | **€0,14** | 0.09% | €-0,56 | €-0,42 | -0.28% |
| bitvavo - kraken | €200,00 | 2026-11-19 | 7.1 u | 34 | 28 | 6 | €0,19 | €0,00 (0x) | **€0,19** | 0.09% | €-0,74 | €-0,56 | -0.28% |
| bitvavo - kraken | €2.000,00 | 2026-11-19 | 7.1 u | 34 | 19 | 15 | €12,21 | €7,05 (16x) | **€5,16** | 0.26% | €-7,46 | €-2,30 | -0.11% |
| bitvavo - kraken | €5.000,00 | 2026-11-19 | 7.1 u | 34 | 17 | 17 | €21,57 | €10,65 (19x) | **€10,92** | 0.22% | €-18,58 | €-7,66 | -0.15% |
| gate - kucoin | €100,00 | 2026-11-19 | 7.1 u | 13 | 7 | 6 | €0,27 | €0,00 (0x) | **€0,27** | 0.27% | €-0,23 | €0,03 | 0.03% |
| gate - kucoin | €150,00 | 2026-11-19 | 7.1 u | 13 | 7 | 6 | €0,40 | €0,00 (0x) | **€0,40** | 0.27% | €-0,35 | €0,05 | 0.03% |
| gate - kucoin | €200,00 | 2026-11-19 | 7.1 u | 13 | 7 | 6 | €0,53 | €0,00 (0x) | **€0,53** | 0.27% | €-0,47 | €0,06 | 0.03% |
| gate - kucoin | €2.000,00 | 2026-11-19 | 7.1 u | 13 | 4 | 9 | €7,05 | €2,98 (9x) | **€4,07** | 0.20% | €-4,67 | €-0,60 | -0.03% |
| gate - kucoin | €5.000,00 | 2026-11-19 | 7.1 u | 13 | 3 | 5 | €13,52 | €2,37 (7x) | **€11,15** | 0.22% | €-11,69 | €-0,54 | -0.01% |

- bitvavo - kraken, €100,00: munten AVA, DYM, GMT, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €483,37 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitvavo - kraken, €150,00: munten AVA, DYM, GMT, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €482,97 zijn, met voorraad €0,14 (GEZIEN boek, GOK model).
- bitvavo - kraken, €200,00: munten AVA, DYM, GMT, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €482,83 zijn, met voorraad €0,19 (GEZIEN boek, GOK model).
- bitvavo - kraken, €2.000,00: munten AVA, DYM, GMT, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €463,14 zijn, met voorraad €12,21 (GEZIEN boek, GOK model).
- bitvavo - kraken, €5.000,00: munten AVA, DYM, GMT, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €430,14 zijn, met voorraad €21,57 (GEZIEN boek, GOK model).
- gate - kucoin, €100,00: munten ERG, IR, LUNC, USTC, VERONA; bruto zonder voorraadgrens zou €48,05 zijn, met voorraad €0,27 (GEZIEN boek, GOK model).
- gate - kucoin, €150,00: munten ERG, IR, LUNC, USTC, VERONA; bruto zonder voorraadgrens zou €48,05 zijn, met voorraad €0,40 (GEZIEN boek, GOK model).
- gate - kucoin, €200,00: munten ERG, IR, LUNC, USTC, VERONA; bruto zonder voorraadgrens zou €48,05 zijn, met voorraad €0,53 (GEZIEN boek, GOK model).
- gate - kucoin, €2.000,00: munten ERG, IR, LUNC, USTC, VERONA; bruto zonder voorraadgrens zou €45,59 zijn, met voorraad €7,05 (GEZIEN boek, GOK model).
- gate - kucoin, €5.000,00: munten ERG, IR, LUNC, USTC, VERONA; bruto zonder voorraadgrens zou €43,13 zijn, met voorraad €13,52 (GEZIEN boek, GOK model).

### Met minstens één grijze beurs (de 5 paren met de meeste bruto winst)

| Beurspaar | Inleg | Dag | Gemeten | Kansen | Gemist (geen voorraad) | Kleiner door voorraad | Bruto winst | Kosten terugschuiven | **Netto handel (bruto min kosten)** | Rendement handel | Koerseffect voorraad | Netto met koerseffect | Rendement met koerseffect |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| kucoin - xt | €100,00 | 2026-11-19 | 7.1 u | 7 | 5 | 2 | €0,22 | €0,00 (0x) | **€0,22** | 0.22% | €1,37 | €1,59 | 1.59% |
| kucoin - xt | €150,00 | 2026-11-19 | 7.1 u | 7 | 5 | 2 | €0,33 | €0,00 (0x) | **€0,33** | 0.22% | €2,06 | €2,39 | 1.59% |
| kucoin - xt | €200,00 | 2026-11-19 | 7.1 u | 7 | 5 | 2 | €0,44 | €0,00 (0x) | **€0,44** | 0.22% | €2,75 | €3,18 | 1.59% |
| kucoin - xt | €2.000,00 | 2026-11-19 | 7.1 u | 7 | 3 | 4 | €9,41 | €2,86 (5x) | **€6,55** | 0.33% | €27,45 | €33,99 | 1.70% |
| kucoin - xt | €5.000,00 | 2026-11-19 | 7.1 u | 7 | 3 | 4 | €22,06 | €2,86 (5x) | **€19,20** | 0.38% | €68,66 | €87,85 | 1.76% |
| bitget - xt | €100,00 | 2026-11-19 | 7.1 u | 7 | 5 | 2 | €0,31 | €0,11 (2x) | **€0,20** | 0.20% | €0,76 | €0,96 | 0.96% |
| bitget - xt | €150,00 | 2026-11-19 | 7.1 u | 7 | 5 | 2 | €0,46 | €0,11 (2x) | **€0,35** | 0.24% | €1,14 | €1,49 | 0.99% |
| bitget - xt | €200,00 | 2026-11-19 | 7.1 u | 7 | 5 | 2 | €0,62 | €0,11 (2x) | **€0,51** | 0.25% | €1,51 | €2,02 | 1.01% |
| bitget - xt | €2.000,00 | 2026-11-19 | 7.1 u | 7 | 4 | 2 | €5,10 | €0,91 (2x) | **€4,19** | 0.21% | €15,08 | €19,27 | 0.96% |
| bitget - xt | €5.000,00 | 2026-11-19 | 7.1 u | 7 | 4 | 2 | €11,48 | €0,92 (3x) | **€10,57** | 0.21% | €37,70 | €48,27 | 0.97% |
| bitget - gate | €100,00 | 2026-11-19 | 7.1 u | 10 | 10 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,60 | €-0,60 | -0.60% |
| bitget - gate | €150,00 | 2026-11-19 | 7.1 u | 10 | 10 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,90 | €-0,90 | -0.60% |
| bitget - gate | €200,00 | 2026-11-19 | 7.1 u | 10 | 6 | 4 | €0,54 | €0,02 (2x) | **€0,52** | 0.26% | €-1,20 | €-0,68 | -0.34% |
| bitget - gate | €2.000,00 | 2026-11-19 | 7.1 u | 10 | 4 | 5 | €7,94 | €1,45 (7x) | **€6,48** | 0.32% | €-12,01 | €-5,53 | -0.28% |
| bitget - gate | €5.000,00 | 2026-11-19 | 7.1 u | 10 | 3 | 5 | €12,17 | €1,25 (5x) | **€10,92** | 0.22% | €-30,02 | €-19,10 | -0.38% |
| htx - xt | €100,00 | 2026-11-19 | 7.1 u | 12 | 12 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,14 | €-0,14 | -0.14% |
| htx - xt | €150,00 | 2026-11-19 | 7.1 u | 12 | 12 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,22 | €-0,22 | -0.14% |
| htx - xt | €200,00 | 2026-11-19 | 7.1 u | 12 | 8 | 4 | €0,42 | €0,00 (0x) | **€0,42** | 0.21% | €-0,29 | €0,13 | 0.07% |
| htx - xt | €2.000,00 | 2026-11-19 | 7.1 u | 12 | 5 | 6 | €7,42 | €3,84 (7x) | **€3,58** | 0.18% | €-2,89 | €0,70 | 0.03% |
| htx - xt | €5.000,00 | 2026-11-19 | 7.1 u | 12 | 5 | 6 | €14,61 | €3,38 (6x) | **€11,23** | 0.22% | €-7,21 | €4,01 | 0.08% |
| bitget - kucoin | €100,00 | 2026-11-19 | 7.1 u | 15 | 15 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,17 | €-0,17 | -0.17% |
| bitget - kucoin | €150,00 | 2026-11-19 | 7.1 u | 15 | 15 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,25 | €-0,25 | -0.17% |
| bitget - kucoin | €200,00 | 2026-11-19 | 7.1 u | 15 | 15 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,33 | €-0,33 | -0.17% |
| bitget - kucoin | €2.000,00 | 2026-11-19 | 7.1 u | 15 | 7 | 8 | €3,60 | €1,50 (7x) | **€2,10** | 0.10% | €-3,36 | €-1,26 | -0.06% |
| bitget - kucoin | €5.000,00 | 2026-11-19 | 7.1 u | 15 | 7 | 5 | €6,84 | €5,93 (12x) | **€0,91** | 0.02% | €-8,36 | €-7,45 | -0.15% |

- kucoin - xt, €100,00: munten FIGHT, LUNC; bruto zonder voorraadgrens zou €358,76 zijn, met voorraad €0,22 (GEZIEN boek, GOK model).
- kucoin - xt, €150,00: munten FIGHT, LUNC; bruto zonder voorraadgrens zou €358,76 zijn, met voorraad €0,33 (GEZIEN boek, GOK model).
- kucoin - xt, €200,00: munten FIGHT, LUNC; bruto zonder voorraadgrens zou €358,76 zijn, met voorraad €0,44 (GEZIEN boek, GOK model).
- kucoin - xt, €2.000,00: munten FIGHT, LUNC; bruto zonder voorraadgrens zou €353,11 zijn, met voorraad €9,41 (GEZIEN boek, GOK model).
- kucoin - xt, €5.000,00: munten FIGHT, LUNC; bruto zonder voorraadgrens zou €344,85 zijn, met voorraad €22,06 (GEZIEN boek, GOK model).
- bitget - xt, €100,00: munten KOR, LUNC; bruto zonder voorraadgrens zou €336,66 zijn, met voorraad €0,31 (GEZIEN boek, GOK model).
- bitget - xt, €150,00: munten KOR, LUNC; bruto zonder voorraadgrens zou €336,61 zijn, met voorraad €0,46 (GEZIEN boek, GOK model).
- bitget - xt, €200,00: munten KOR, LUNC; bruto zonder voorraadgrens zou €336,56 zijn, met voorraad €0,62 (GEZIEN boek, GOK model).
- bitget - xt, €2.000,00: munten KOR, LUNC; bruto zonder voorraadgrens zou €331,61 zijn, met voorraad €5,10 (GEZIEN boek, GOK model).
- bitget - xt, €5.000,00: munten KOR, LUNC; bruto zonder voorraadgrens zou €320,96 zijn, met voorraad €11,48 (GEZIEN boek, GOK model).
- bitget - gate, €100,00: munten BABYSHARK, IR, LUNC, VERONA; bruto zonder voorraadgrens zou €52,89 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - gate, €150,00: munten BABYSHARK, IR, LUNC, VERONA; bruto zonder voorraadgrens zou €52,89 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - gate, €200,00: munten BABYSHARK, IR, LUNC, VERONA; bruto zonder voorraadgrens zou €52,78 zijn, met voorraad €0,54 (GEZIEN boek, GOK model).
- bitget - gate, €2.000,00: munten BABYSHARK, IR, LUNC, VERONA; bruto zonder voorraadgrens zou €48,98 zijn, met voorraad €7,94 (GEZIEN boek, GOK model).
- bitget - gate, €5.000,00: munten BABYSHARK, IR, LUNC, VERONA; bruto zonder voorraadgrens zou €49,77 zijn, met voorraad €12,17 (GEZIEN boek, GOK model).
- htx - xt, €100,00: munten CBK, LUNC, SEI, XDC; bruto zonder voorraadgrens zou €44,94 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - xt, €150,00: munten CBK, LUNC, SEI, XDC; bruto zonder voorraadgrens zou €44,94 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - xt, €200,00: munten CBK, LUNC, SEI, XDC; bruto zonder voorraadgrens zou €44,80 zijn, met voorraad €0,42 (GEZIEN boek, GOK model).
- htx - xt, €2.000,00: munten CBK, LUNC, SEI, XDC; bruto zonder voorraadgrens zou €41,29 zijn, met voorraad €7,42 (GEZIEN boek, GOK model).
- htx - xt, €5.000,00: munten CBK, LUNC, SEI, XDC; bruto zonder voorraadgrens zou €38,05 zijn, met voorraad €14,61 (GEZIEN boek, GOK model).
- bitget - kucoin, €100,00: munten KLV, LUNC, MTX, USDT, USTC, VERONA; bruto zonder voorraadgrens zou €38,22 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - kucoin, €150,00: munten KLV, LUNC, MTX, USDT, USTC, VERONA; bruto zonder voorraadgrens zou €38,22 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - kucoin, €200,00: munten KLV, LUNC, MTX, USDT, USTC, VERONA; bruto zonder voorraadgrens zou €38,22 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - kucoin, €2.000,00: munten KLV, LUNC, MTX, USDT, USTC, VERONA; bruto zonder voorraadgrens zou €35,71 zijn, met voorraad €3,60 (GEZIEN boek, GOK model).
- bitget - kucoin, €5.000,00: munten KLV, LUNC, MTX, USDT, USTC, VERONA; bruto zonder voorraadgrens zou €33,18 zijn, met voorraad €6,84 (GEZIEN boek, GOK model).

### Andere keuzes bij bitvavo - kraken (netto handel, alle dagen samen; GOK)

| Keuze | Inleg | Kansen | Gemist | Bruto winst | Kosten terugschuiven | Netto handel |
|---|---|---|---|---|---|---|
| standaard (schuifdrempel 25%, kostengrens 1%) | €150,00 | 34 | 28 | €0,14 | €0,00 | **€0,14** |
| standaard (schuifdrempel 25%, kostengrens 1%) | €2.000,00 | 34 | 19 | €12,21 | €7,05 | **€5,16** |
| schuifdrempel 10% | €150,00 | 34 | 28 | €0,14 | €0,00 | **€0,14** |
| schuifdrempel 10% | €2.000,00 | 34 | 22 | €8,32 | €5,12 | **€3,20** |
| schuifdrempel 40% | €150,00 | 34 | 28 | €0,14 | €0,00 | **€0,14** |
| schuifdrempel 40% | €2.000,00 | 34 | 19 | €9,55 | €6,72 | **€2,83** |
| kostengrens 2% (achteraf vergeleken) | €150,00 | 34 | 28 | €0,14 | €0,00 | **€0,14** |
| kostengrens 2% (achteraf vergeleken) | €2.000,00 | 34 | 18 | €10,54 | €10,65 | **€-0,10** |
| kostengrens 5% (achteraf vergeleken) | €150,00 | 34 | 25 | €0,18 | €2,48 | **€-2,31** |
| kostengrens 5% (achteraf vergeleken) | €2.000,00 | 34 | 18 | €10,54 | €10,65 | **€-0,10** |
| alleen MERL en AVA (meer voorraad per munt, achteraf gekozen) | €150,00 | 16 | 14 | €0,19 | €0,00 | **€0,19** |
| alleen MERL en AVA (meer voorraad per munt, achteraf gekozen) | €2.000,00 | 16 | 10 | €13,48 | €5,60 | **€7,88** |

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

- Opnamekosten bij de echte kansen: 26 van een netwerk dat aan beide kanten open is, 50 van de beurs zelf (laagste open netwerk), 6 geschat uit wat andere beurzen voor die munt vragen (GOK). Onbekende opnamekosten tellen niet als echte kans.
- Netwerk: KuCoin, Gate, Bitget, HTX, XT, Bitstamp, Bitvavo en Poloniex geven hun netwerken per munt. Als beide beurzen dat doen en de namen te koppelen zijn, moet er een netwerk zijn dat aan beide kanten open is. Anders is het netwerk "niet te koppelen" en telt de kans mee (staat apart in de trechter).
- De duur is gemeten in stappen van ±20 seconden; een kans kan een paar rondes eerder begonnen zijn dan we zagen.
- Takerkosten: uit de API waar die ze per paar geeft, anders het standaardtarief uit de README (deels GOK).
- Laatste run: 15 beurzen antwoordden, 2287 munt-quote-paren op minstens twee beurzen (GEZIEN).
