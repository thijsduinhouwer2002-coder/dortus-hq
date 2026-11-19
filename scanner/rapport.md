# Rapport koersverschil-scanner

Gemaakt 2026-11-19 16:29 UTC uit 15 runs, samen ±7.6 uur gemeten (GEZIEN).
Echte kans = winst na alle kosten (opnamekosten bekend), opnemen en storten open (en een netwerk dat aan beide kanten open is, als de beurzen dat geven), minstens €100,00 op het boek, minstens 2 minuten blijven staan, geen andere munt met dezelfde naam.
**Vergund** = beide beurzen hebben een MiCA-vergunning (ESMA-register), vaak via een EU-dochter die minder munten kan hebben dan de wereldwijde API die we meten (GOK). **Grijs** = minstens één beurs zonder vergunning (MEXC, Bitget, HTX, Poloniex, XT, Bitfinex, Binance). Zie README.md.
**Kraken-tarief:** Kraken rekent 0,80% taker op munt tegen EUR, USD, USDT of USDC (GEZIEN, kraken.com/pro/fees, laagste trede); de scanner rekende tot 19 nov met 0,40%. 399 opgeslagen kansen met Kraken uit die runs zijn hier **opnieuw doorgerekend met 0,80%** (GOK-benadering: 0,40% van de inzet aan de Kraken-kant extra op elk gemeten punt van het boek; het boek zelf is niet bewaard). 233 houden daarna nog winst op het boek. Dat ze met hogere kosten ook korter bleven staan, telt niet mee (dus eerder te gunstig).

## Hoeveel wordt er gecontroleerd? (GEZIEN, stand.jsonl)

Per ronde (mediaan over 91 metingen): 1048 kandidaten (verschil op de ticker groter dan de takerkosten), 120 met het orderboek gecontroleerd, 3 nog nooit gecontroleerd (0%).
Bijna alle kandidaten komen aan de beurt; de aantallen hieronder missen weinig.

## Trechter (GEZIEN, eigen metingen)

| Stap | Alle beurzen | Alleen MiCA-beurzen | Met minstens één grijze beurs |
|---|---|---|---|
| Verschillen met winst op het boek na alle kosten | 7475 | 971 | 6504 |
| ...waarvan opnemen of storten dicht | 1760 | 160 | 1600 |
| ...waarvan status onbekend (beurs geeft het niet openbaar) | 4165 | 629 | 3536 |
| Opnemen en storten open | 1550 | 182 | 1368 |
| ...en geen netwerk dat aan beide kanten open is: valt af | 22 | 1 | 21 |
| ...en opnamekosten onbekend: valt af | 0 | 0 | 0 |
| ...en minstens €100,00 op het boek | 479 | 107 | 372 |
| ...en minstens 2 minuten blijven staan | 156 | 57 | 99 |
| ...en geen andere munt met dezelfde naam | 136 | 48 | 88 |
|    ...waarvan contractadres bekend en gelijk | 9 | 1 | 8 |
|    ...waarvan contractadres onbekend (telt mee, kan een andere munt zijn) | 127 | 47 | 80 |
|    ...waarvan netwerk gekoppeld en open | 75 | 13 | 62 |
|    ...waarvan netwerk niet te koppelen (telt mee) | 61 | 35 | 26 |
| **Echte kansen** (zelfde munt overlappend in de tijd samengevoegd, beste beurspaar telt) | 89 | 48 | 53 |
| Ter vergelijking: zelfde eisen, maar opnamestatus onbekend (niet meegeteld) | 202 | 52 | 169 |

## Echte kansen per dag (GEZIEN)

| Dag | Echt, alleen MiCA | Echt, met grijs | Mediane winst per kans bij €500 (MiCA / grijs) | Mediane duur |
|---|---|---|---|---|
| 2026-11-19 | 36 | 53 | €2,01 / €1,21 | 5.0 min |
| Totaal | 36 | 53 | €2,01 / €1,21 | 5.0 min |

## Beste munten (GEZIEN)

| | Soort | Kansen | Som winst bij €500 per kans |
|---|---|---|---|
| MERL-EUR | vergund | 12 | €120,76 |
| LUNC-USDT | grijs | 8 | €38,25 |
| USTC-USDT | grijs en vergund | 6 | €20,14 |
| YB-USDT | grijs | 1 | €16,34 |
| WAN-USDT | grijs | 4 | €14,24 |
| VERONA-USDT | grijs | 7 | €11,93 |
| AVA-EUR | vergund | 4 | €11,22 |
| LUNA-EUR | vergund | 4 | €10,37 |
| GMT-EUR | vergund | 7 | €9,70 |
| WARD-USDT | grijs | 3 | €6,81 |

## Beste beursparen (kopen op > verkopen op) (GEZIEN)

| | Soort | Kansen | Som winst bij €500 per kans |
|---|---|---|---|
| bitvavo > kraken | vergund | 34 | €156,00 |
| kucoin > htx | grijs | 9 | €22,05 |
| kucoin > bitget | grijs | 7 | €20,42 |
| bitget > gate | grijs | 5 | €18,41 |
| gate > xt | grijs | 1 | €16,34 |
| bitget > xt | grijs | 4 | €13,09 |
| htx > xt | grijs | 2 | €9,65 |
| bitget > htx | grijs | 9 | €6,64 |
| kucoin > xt | grijs | 1 | €6,56 |
| bitget > kucoin | grijs | 7 | €5,71 |

Beurzen die het vaakst meedoen (koop of verkoop): bitvavo 34, kraken 34, bitget (grijs) 32, kucoin 28, htx (grijs) 26, gate 11, xt (grijs) 11, poloniex (grijs) 2 (GEZIEN).

## Hoeveel kansen blijven staan terwijl je geld schuift? (GEZIEN, duur uit eigen metingen)

Wie geen voorraad op beide beurzen heeft, moet kopen, de munt opnemen, wachten tot hij binnen is en dan verkopen. Hoe lang dat duurt verschilt per munt en netwerk: een paar minuten (snelle ketens) tot een uur of meer (Bitcoin, beurzen die opnames met de hand keuren) (GOK, niet per munt gemeten).

| Overmaaktijd | Alle beurzen | Alleen MiCA-beurzen | Met minstens één grijze beurs |
|---|---|---|---|
| 5 min | 46 van 89 (52%) | 22 van 48 (46%) | 28 van 53 (53%) |
| 10 min | 20 van 89 (22%) | 12 van 48 (25%) | 10 van 53 (19%) |
| 30 min | 14 van 89 (16%) | 10 van 48 (21%) | 5 van 53 (9%) |
| 60 min | 5 van 89 (6%) | 4 van 48 (8%) | 2 van 53 (4%) |

## Wat zou het opleveren over 3 maanden? (GOK, doorgetrokken uit de metingen)

Gemeten over ±7.6 uur (GEZIEN), doorgetrokken naar 90 dagen (GOK: aanname dat de week die we maten gewoon is).

| Beurzen | Inleg | Model | Kansen per uur | Per kans (mediaan) | 3 maanden |
|---|---|---|---|---|---|
| Alleen MiCA | €2.000,00 | bovengrens: elke kans, geld overal tegelijk | 6.33 | €2,96 | €40.516,43 |
| Alleen MiCA | €2.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 4.48 | €3,12 | €70.732,23 |
| Alleen MiCA | €5.000,00 | bovengrens: elke kans, geld overal tegelijk | 6.33 | €3,05 | €41.741,41 |
| Alleen MiCA | €5.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 4.48 | €3,28 | €101.816,30 |
| Alle (met grijs) | €2.000,00 | bovengrens: elke kans, geld overal tegelijk | 11.74 | €2,04 | €51.644,33 |
| Alle (met grijs) | €2.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 4.48 | €3,12 | €70.732,23 |
| Alle (met grijs) | €5.000,00 | bovengrens: elke kans, geld overal tegelijk | 11.74 | €2,40 | €60.747,30 |
| Alle (met grijs) | €5.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 4.48 | €3,28 | €101.816,30 |

Bovengrens: elke kans met de helft van de inleg aan elke kant, alsof het geld op alle beurzen tegelijk staat (kan in het echt niet). Beste beurspaar: het paar is **achteraf** gekozen uit de metingen (vooraf kiezen levert minder op), en het model neemt aan dat je van elke munt al voorraad op de verkoopbeurs hebt.

Waarom dit te rooskleurig is (GOK): elke kans wordt maar één keer geteld met het mediane boek, maar andere bots pakken hem ook; de munt die je als voorraad aanhoudt kan dalen; na een paar kansen moet de voorraad terug (opnamekosten en tijd); minimale opname- en ordergroottes tellen niet mee; en een kans die we 2 minuten zagen staan, staat er niet per se nog als jouw order binnenkomt. Waarom het te somber kan zijn: niet alle kandidaten zijn gecontroleerd, en met voorraad op beide beurzen kun je dezelfde kans vaker pakken als het boek zich aanvult; dat telt hier niet mee.

## Wat houd je echt over? Voorraad op twee beurzen (simulatie)

Per beurspaar: geld en munten op beide beurzen, elke echte kans uitgevoerd tegen het boek zoals gemeten (niet meer dan de ruimte op het boek en niet meer dan de voorraad op die beurs), terugschuiven als een kant leeg dreigt te raken (met opnamekosten en tijd onderweg), en het koerseffect van de aangehouden munten apart. Netto = bruto min kosten terugschuiven plus koerseffect. **Gemeten** (GEZIEN): de kansen, het boek en de koersen; **de rest is een rekenmodel** (GOK, aannames onder de tabel). Geen advies.

**Met €150: netto €0,14 per dag op bitvavo - kraken (koerseffect erbovenop €-0,73), €0,40 per dag op gate - kucoin (koerseffect erbovenop €-0,29) (GOK: netto handel, rekenmodel op ±7.6 uur meting per dag, alleen MiCA).** "Per dag" is hier één gemeten dag die begint met een gelijk verdeelde voorraad; aan het eind staat de voorraad scheef, dus een volgende dag levert waarschijnlijk minder op, tenzij kansen de andere kant op hem terugbrengen (GOK).

### Alleen MiCA-beurzen (alle paren met echte kansen)

| Beurspaar | Inleg | Dag | Gemeten | Kansen | Gemist (geen voorraad) | Kleiner door voorraad | Bruto winst | Kosten terugschuiven | **Netto handel (bruto min kosten)** | Rendement handel | Koerseffect voorraad | Netto met koerseffect | Rendement met koerseffect |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| bitvavo - kraken | €100,00 | 2026-11-19 | 7.6 u | 34 | 34 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,49 | €-0,49 | -0.49% |
| bitvavo - kraken | €150,00 | 2026-11-19 | 7.6 u | 34 | 28 | 6 | €0,14 | €0,00 (0x) | **€0,14** | 0.09% | €-0,73 | €-0,59 | -0.40% |
| bitvavo - kraken | €200,00 | 2026-11-19 | 7.6 u | 34 | 28 | 6 | €0,19 | €0,00 (0x) | **€0,19** | 0.09% | €-0,98 | €-0,79 | -0.40% |
| bitvavo - kraken | €2.000,00 | 2026-11-19 | 7.6 u | 34 | 19 | 15 | €12,21 | €7,05 (16x) | **€5,16** | 0.26% | €-9,76 | €-4,60 | -0.23% |
| bitvavo - kraken | €5.000,00 | 2026-11-19 | 7.6 u | 34 | 17 | 17 | €21,57 | €10,65 (19x) | **€10,92** | 0.22% | €-24,37 | €-13,45 | -0.27% |
| gate - kucoin | €100,00 | 2026-11-19 | 7.6 u | 14 | 8 | 6 | €0,27 | €0,00 (0x) | **€0,27** | 0.27% | €-0,19 | €0,07 | 0.07% |
| gate - kucoin | €150,00 | 2026-11-19 | 7.6 u | 14 | 8 | 6 | €0,40 | €0,00 (0x) | **€0,40** | 0.27% | €-0,29 | €0,11 | 0.07% |
| gate - kucoin | €200,00 | 2026-11-19 | 7.6 u | 14 | 8 | 6 | €0,53 | €0,00 (0x) | **€0,53** | 0.27% | €-0,39 | €0,14 | 0.07% |
| gate - kucoin | €2.000,00 | 2026-11-19 | 7.6 u | 14 | 5 | 9 | €7,05 | €2,98 (9x) | **€4,07** | 0.20% | €-3,87 | €0,19 | 0.01% |
| gate - kucoin | €5.000,00 | 2026-11-19 | 7.6 u | 14 | 3 | 6 | €13,65 | €2,37 (7x) | **€11,28** | 0.23% | €-9,69 | €1,59 | 0.03% |

- bitvavo - kraken, €100,00: munten AVA, DYM, GMT, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €483,37 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitvavo - kraken, €150,00: munten AVA, DYM, GMT, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €482,97 zijn, met voorraad €0,14 (GEZIEN boek, GOK model).
- bitvavo - kraken, €200,00: munten AVA, DYM, GMT, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €482,83 zijn, met voorraad €0,19 (GEZIEN boek, GOK model).
- bitvavo - kraken, €2.000,00: munten AVA, DYM, GMT, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €463,14 zijn, met voorraad €12,21 (GEZIEN boek, GOK model).
- bitvavo - kraken, €5.000,00: munten AVA, DYM, GMT, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €430,14 zijn, met voorraad €21,57 (GEZIEN boek, GOK model).
- gate - kucoin, €100,00: munten ERG, IR, LUNC, USTC, VERONA; bruto zonder voorraadgrens zou €48,48 zijn, met voorraad €0,27 (GEZIEN boek, GOK model).
- gate - kucoin, €150,00: munten ERG, IR, LUNC, USTC, VERONA; bruto zonder voorraadgrens zou €48,48 zijn, met voorraad €0,40 (GEZIEN boek, GOK model).
- gate - kucoin, €200,00: munten ERG, IR, LUNC, USTC, VERONA; bruto zonder voorraadgrens zou €48,48 zijn, met voorraad €0,53 (GEZIEN boek, GOK model).
- gate - kucoin, €2.000,00: munten ERG, IR, LUNC, USTC, VERONA; bruto zonder voorraadgrens zou €46,02 zijn, met voorraad €7,05 (GEZIEN boek, GOK model).
- gate - kucoin, €5.000,00: munten ERG, IR, LUNC, USTC, VERONA; bruto zonder voorraadgrens zou €43,56 zijn, met voorraad €13,65 (GEZIEN boek, GOK model).

### Met minstens één grijze beurs (de 5 paren met de meeste bruto winst)

| Beurspaar | Inleg | Dag | Gemeten | Kansen | Gemist (geen voorraad) | Kleiner door voorraad | Bruto winst | Kosten terugschuiven | **Netto handel (bruto min kosten)** | Rendement handel | Koerseffect voorraad | Netto met koerseffect | Rendement met koerseffect |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| kucoin - xt | €100,00 | 2026-11-19 | 7.6 u | 7 | 5 | 2 | €0,22 | €0,00 (0x) | **€0,22** | 0.22% | €0,45 | €0,67 | 0.67% |
| kucoin - xt | €150,00 | 2026-11-19 | 7.6 u | 7 | 5 | 2 | €0,33 | €0,00 (0x) | **€0,33** | 0.22% | €0,68 | €1,00 | 0.67% |
| kucoin - xt | €200,00 | 2026-11-19 | 7.6 u | 7 | 5 | 2 | €0,44 | €0,00 (0x) | **€0,44** | 0.22% | €0,90 | €1,34 | 0.67% |
| kucoin - xt | €2.000,00 | 2026-11-19 | 7.6 u | 7 | 3 | 4 | €9,41 | €2,86 (5x) | **€6,55** | 0.33% | €9,03 | €15,57 | 0.78% |
| kucoin - xt | €5.000,00 | 2026-11-19 | 7.6 u | 7 | 3 | 4 | €22,06 | €2,86 (5x) | **€19,20** | 0.38% | €22,55 | €41,75 | 0.83% |
| bitget - xt | €100,00 | 2026-11-19 | 7.6 u | 7 | 5 | 2 | €0,31 | €0,11 (2x) | **€0,20** | 0.20% | €0,43 | €0,63 | 0.63% |
| bitget - xt | €150,00 | 2026-11-19 | 7.6 u | 7 | 5 | 2 | €0,46 | €0,11 (2x) | **€0,35** | 0.24% | €0,65 | €1,00 | 0.67% |
| bitget - xt | €200,00 | 2026-11-19 | 7.6 u | 7 | 5 | 2 | €0,62 | €0,11 (2x) | **€0,51** | 0.25% | €0,86 | €1,37 | 0.69% |
| bitget - xt | €2.000,00 | 2026-11-19 | 7.6 u | 7 | 4 | 2 | €5,10 | €0,91 (2x) | **€4,19** | 0.21% | €8,59 | €12,78 | 0.64% |
| bitget - xt | €5.000,00 | 2026-11-19 | 7.6 u | 7 | 4 | 2 | €11,48 | €0,92 (3x) | **€10,57** | 0.21% | €21,47 | €32,03 | 0.64% |
| bitget - gate | €100,00 | 2026-11-19 | 7.6 u | 10 | 10 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,38 | €-0,38 | -0.38% |
| bitget - gate | €150,00 | 2026-11-19 | 7.6 u | 10 | 10 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,57 | €-0,57 | -0.38% |
| bitget - gate | €200,00 | 2026-11-19 | 7.6 u | 10 | 6 | 4 | €0,54 | €0,02 (2x) | **€0,52** | 0.26% | €-0,76 | €-0,23 | -0.12% |
| bitget - gate | €2.000,00 | 2026-11-19 | 7.6 u | 10 | 4 | 5 | €7,94 | €1,45 (7x) | **€6,48** | 0.32% | €-7,57 | €-1,09 | -0.05% |
| bitget - gate | €5.000,00 | 2026-11-19 | 7.6 u | 10 | 3 | 5 | €12,17 | €1,25 (5x) | **€10,92** | 0.22% | €-18,93 | €-8,01 | -0.16% |
| htx - xt | €100,00 | 2026-11-19 | 7.6 u | 13 | 13 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,21 | €-0,21 | -0.21% |
| htx - xt | €150,00 | 2026-11-19 | 7.6 u | 13 | 13 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,32 | €-0,32 | -0.21% |
| htx - xt | €200,00 | 2026-11-19 | 7.6 u | 13 | 9 | 4 | €0,42 | €0,00 (0x) | **€0,42** | 0.21% | €-0,42 | €-0,00 | -0.00% |
| htx - xt | €2.000,00 | 2026-11-19 | 7.6 u | 13 | 5 | 7 | €9,13 | €4,24 (8x) | **€4,89** | 0.24% | €-4,22 | €0,68 | 0.03% |
| htx - xt | €5.000,00 | 2026-11-19 | 7.6 u | 13 | 5 | 7 | €17,95 | €3,78 (7x) | **€14,17** | 0.28% | €-10,57 | €3,60 | 0.07% |
| bitget - kucoin | €100,00 | 2026-11-19 | 7.6 u | 16 | 16 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,74 | €-0,74 | -0.74% |
| bitget - kucoin | €150,00 | 2026-11-19 | 7.6 u | 16 | 16 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,11 | €-1,11 | -0.74% |
| bitget - kucoin | €200,00 | 2026-11-19 | 7.6 u | 16 | 16 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,49 | €-1,49 | -0.74% |
| bitget - kucoin | €2.000,00 | 2026-11-19 | 7.6 u | 16 | 7 | 9 | €4,49 | €1,62 (8x) | **€2,87** | 0.14% | €-14,86 | €-11,99 | -0.60% |
| bitget - kucoin | €5.000,00 | 2026-11-19 | 7.6 u | 16 | 7 | 6 | €7,35 | €6,84 (13x) | **€0,50** | 0.01% | €-37,11 | €-36,61 | -0.73% |

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
- htx - xt, €100,00: munten CBK, LUNC, SEI, XDC; bruto zonder voorraadgrens zou €49,15 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - xt, €150,00: munten CBK, LUNC, SEI, XDC; bruto zonder voorraadgrens zou €49,15 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - xt, €200,00: munten CBK, LUNC, SEI, XDC; bruto zonder voorraadgrens zou €49,00 zijn, met voorraad €0,42 (GEZIEN boek, GOK model).
- htx - xt, €2.000,00: munten CBK, LUNC, SEI, XDC; bruto zonder voorraadgrens zou €45,50 zijn, met voorraad €9,13 (GEZIEN boek, GOK model).
- htx - xt, €5.000,00: munten CBK, LUNC, SEI, XDC; bruto zonder voorraadgrens zou €42,25 zijn, met voorraad €17,95 (GEZIEN boek, GOK model).
- bitget - kucoin, €100,00: munten KLV, LUNC, MTX, USDT, USTC, VERONA; bruto zonder voorraadgrens zou €40,36 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - kucoin, €150,00: munten KLV, LUNC, MTX, USDT, USTC, VERONA; bruto zonder voorraadgrens zou €40,36 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - kucoin, €200,00: munten KLV, LUNC, MTX, USDT, USTC, VERONA; bruto zonder voorraadgrens zou €40,36 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - kucoin, €2.000,00: munten KLV, LUNC, MTX, USDT, USTC, VERONA; bruto zonder voorraadgrens zou €37,84 zijn, met voorraad €4,49 (GEZIEN boek, GOK model).
- bitget - kucoin, €5.000,00: munten KLV, LUNC, MTX, USDT, USTC, VERONA; bruto zonder voorraadgrens zou €35,32 zijn, met voorraad €7,35 (GEZIEN boek, GOK model).

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

- Opnamekosten bij de echte kansen: 32 van een netwerk dat aan beide kanten open is, 50 van de beurs zelf (laagste open netwerk), 7 geschat uit wat andere beurzen voor die munt vragen (GOK). Onbekende opnamekosten tellen niet als echte kans.
- Netwerk: KuCoin, Gate, Bitget, HTX, XT, Bitstamp, Bitvavo en Poloniex geven hun netwerken per munt. Als beide beurzen dat doen en de namen te koppelen zijn, moet er een netwerk zijn dat aan beide kanten open is. Anders is het netwerk "niet te koppelen" en telt de kans mee (staat apart in de trechter).
- De duur is gemeten in stappen van ±20 seconden; een kans kan een paar rondes eerder begonnen zijn dan we zagen.
- Takerkosten: uit de API waar die ze per paar geeft, anders het standaardtarief uit de README (deels GOK).
- Laatste run: 15 beurzen antwoordden, 2286 munt-quote-paren op minstens twee beurzen (GEZIEN).
