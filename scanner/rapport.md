# Rapport koersverschil-scanner

Gemaakt 2026-11-19 15:45 UTC uit 10 runs, samen ±6.8 uur gemeten (GEZIEN).
Echte kans = winst na alle kosten (opnamekosten bekend), opnemen en storten open (en een netwerk dat aan beide kanten open is, als de beurzen dat geven), minstens €100,00 op het boek, minstens 2 minuten blijven staan, geen andere munt met dezelfde naam.
**Vergund** = beide beurzen hebben een MiCA-vergunning (ESMA-register), vaak via een EU-dochter die minder munten kan hebben dan de wereldwijde API die we meten (GOK). **Grijs** = minstens één beurs zonder vergunning (MEXC, Bitget, HTX, Poloniex, XT, Bitfinex, Binance). Zie README.md.

## Hoeveel wordt er gecontroleerd? (GEZIEN, stand.jsonl)

Per ronde (mediaan over 81 metingen): 1045 kandidaten (verschil op de ticker groter dan de takerkosten), 120 met het orderboek gecontroleerd, 3 nog nooit gecontroleerd (0%).
Bijna alle kandidaten komen aan de beurt; de aantallen hieronder missen weinig.

## Trechter (GEZIEN, eigen metingen)

| Stap | Alle beurzen | Alleen MiCA-beurzen | Met minstens één grijze beurs |
|---|---|---|---|
| Verschillen met winst op het boek na alle kosten | 6178 | 896 | 5282 |
| ...waarvan opnemen of storten dicht | 1310 | 113 | 1197 |
| ...waarvan status onbekend (beurs geeft het niet openbaar) | 3449 | 528 | 2921 |
| Opnemen en storten open | 1419 | 255 | 1164 |
| ...en geen netwerk dat aan beide kanten open is: valt af | 22 | 1 | 21 |
| ...en opnamekosten onbekend: valt af | 0 | 0 | 0 |
| ...en minstens €100,00 op het boek | 491 | 190 | 301 |
| ...en minstens 2 minuten blijven staan | 156 | 70 | 86 |
| ...en geen andere munt met dezelfde naam | 140 | 63 | 77 |
|    ...waarvan contractadres bekend en gelijk | 8 | 1 | 7 |
|    ...waarvan contractadres onbekend (telt mee, kan een andere munt zijn) | 132 | 62 | 70 |
|    ...waarvan netwerk gekoppeld en open | 64 | 12 | 52 |
|    ...waarvan netwerk niet te koppelen (telt mee) | 76 | 51 | 25 |
| **Echte kansen** (zelfde munt overlappend in de tijd samengevoegd, beste beurspaar telt) | 96 | 63 | 45 |
| Ter vergelijking: zelfde eisen, maar opnamestatus onbekend (niet meegeteld) | 192 | 53 | 158 |

## Echte kansen per dag (GEZIEN)

| Dag | Echt, alleen MiCA | Echt, met grijs | Mediane winst per kans bij €500 (MiCA / grijs) | Mediane duur |
|---|---|---|---|---|
| 2026-11-19 | 51 | 45 | €2,27 / €1,18 | 4.7 min |
| Totaal | 51 | 45 | €2,27 / €1,18 | 4.7 min |

## Beste munten (GEZIEN)

| | Soort | Kansen | Som winst bij €500 per kans |
|---|---|---|---|
| MERL-EUR | vergund | 10 | €109,03 |
| LUNC-USDT | grijs | 6 | €31,12 |
| DYM-EUR | vergund | 21 | €24,84 |
| GMT-EUR | vergund | 8 | €22,46 |
| LUNA-EUR | vergund | 6 | €20,65 |
| USTC-USDT | grijs | 5 | €19,89 |
| YB-USDT | grijs | 1 | €16,34 |
| AVA-EUR | vergund | 4 | €13,86 |
| WAN-USDT | grijs | 3 | €12,65 |
| VERONA-USDT | grijs | 7 | €11,93 |

## Beste beursparen (kopen op > verkopen op) (GEZIEN)

| | Soort | Kansen | Som winst bij €500 per kans |
|---|---|---|---|
| bitvavo > kraken | vergund | 50 | €190,55 |
| kucoin > bitget | grijs | 7 | €20,42 |
| bitget > gate | grijs | 5 | €18,41 |
| kucoin > htx | grijs | 6 | €16,78 |
| gate > xt | grijs | 1 | €16,34 |
| bitget > xt | grijs | 4 | €13,09 |
| kucoin > xt | grijs | 1 | €6,56 |
| htx > xt | grijs | 1 | €5,83 |
| bitget > htx | grijs | 7 | €5,51 |
| bitget > kucoin | grijs | 6 | €3,67 |

Beurzen die het vaakst meedoen (koop of verkoop): bitvavo 50, kraken 50, bitget (grijs) 29, kucoin 23, htx (grijs) 19, xt (grijs) 10, gate 9, poloniex (grijs) 2 (GEZIEN).

## Hoeveel kansen blijven staan terwijl je geld schuift? (GEZIEN, duur uit eigen metingen)

Wie geen voorraad op beide beurzen heeft, moet kopen, de munt opnemen, wachten tot hij binnen is en dan verkopen. Hoe lang dat duurt verschilt per munt en netwerk: een paar minuten (snelle ketens) tot een uur of meer (Bitcoin, beurzen die opnames met de hand keuren) (GOK, niet per munt gemeten).

| Overmaaktijd | Alle beurzen | Alleen MiCA-beurzen | Met minstens één grijze beurs |
|---|---|---|---|
| 5 min | 47 van 96 (49%) | 27 van 63 (43%) | 24 van 45 (53%) |
| 10 min | 19 van 96 (20%) | 13 van 63 (21%) | 8 van 45 (18%) |
| 30 min | 14 van 96 (15%) | 10 van 63 (16%) | 5 van 45 (11%) |
| 60 min | 5 van 96 (5%) | 4 van 63 (6%) | 2 van 45 (4%) |

## Wat zou het opleveren over 3 maanden? (GOK, doorgetrokken uit de metingen)

Gemeten over ±6.8 uur (GEZIEN), doorgetrokken naar 90 dagen (GOK: aanname dat de week die we maten gewoon is).

| Beurzen | Inleg | Model | Kansen per uur | Per kans (mediaan) | 3 maanden |
|---|---|---|---|---|---|
| Alleen MiCA | €2.000,00 | bovengrens: elke kans, geld overal tegelijk | 9.33 | €3,92 | €79.078,38 |
| Alleen MiCA | €2.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 7.41 | €4,34 | €103.355,78 |
| Alleen MiCA | €5.000,00 | bovengrens: elke kans, geld overal tegelijk | 9.33 | €4,99 | €100.590,23 |
| Alleen MiCA | €5.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 7.41 | €5,99 | €165.030,17 |
| Alle (met grijs) | €2.000,00 | bovengrens: elke kans, geld overal tegelijk | 14.22 | €2,95 | €90.491,25 |
| Alle (met grijs) | €2.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 7.41 | €4,34 | €103.355,78 |
| Alle (met grijs) | €5.000,00 | bovengrens: elke kans, geld overal tegelijk | 14.22 | €3,70 | €113.528,77 |
| Alle (met grijs) | €5.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 7.41 | €5,99 | €165.030,17 |

Bovengrens: elke kans met de helft van de inleg aan elke kant, alsof het geld op alle beurzen tegelijk staat (kan in het echt niet). Beste beurspaar: het paar is **achteraf** gekozen uit de metingen (vooraf kiezen levert minder op), en het model neemt aan dat je van elke munt al voorraad op de verkoopbeurs hebt.

Waarom dit te rooskleurig is (GOK): elke kans wordt maar één keer geteld met het mediane boek, maar andere bots pakken hem ook; de munt die je als voorraad aanhoudt kan dalen; na een paar kansen moet de voorraad terug (opnamekosten en tijd); minimale opname- en ordergroottes tellen niet mee; en een kans die we 2 minuten zagen staan, staat er niet per se nog als jouw order binnenkomt. Waarom het te somber kan zijn: niet alle kandidaten zijn gecontroleerd, en met voorraad op beide beurzen kun je dezelfde kans vaker pakken als het boek zich aanvult; dat telt hier niet mee.

## Wat houd je echt over? Voorraad op twee beurzen (simulatie)

Per beurspaar: geld en munten op beide beurzen, elke echte kans uitgevoerd tegen het boek zoals gemeten (niet meer dan de ruimte op het boek en niet meer dan de voorraad op die beurs), terugschuiven als een kant leeg dreigt te raken (met opnamekosten en tijd onderweg), en het koerseffect van de aangehouden munten apart. Netto = bruto min kosten terugschuiven plus koerseffect. **Gemeten** (GEZIEN): de kansen, het boek en de koersen; **de rest is een rekenmodel** (GOK, aannames onder de tabel). Geen advies.

**Met €150: netto €0,20 per dag op bitvavo - kraken (koerseffect erbovenop €0,30), €0,40 per dag op gate - kucoin (koerseffect erbovenop €-0,68) (GOK: netto handel, rekenmodel op ±6.7 uur meting per dag, alleen MiCA).**

### Alleen MiCA-beurzen (alle paren met echte kansen)

| Beurspaar | Inleg | Dag | Gemeten | Kansen | Gemist (geen voorraad) | Kleiner door voorraad | Bruto winst | Kosten terugschuiven | **Netto handel (bruto min kosten)** | Rendement handel | Koerseffect voorraad | Netto met koerseffect | Rendement met koerseffect |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| bitvavo - kraken | €100,00 | 2026-11-19 | 6.7 u | 50 | 50 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,20 | €0,20 | 0.20% |
| bitvavo - kraken | €150,00 | 2026-11-19 | 6.7 u | 50 | 44 | 6 | €0,20 | €0,00 (0x) | **€0,20** | 0.13% | €0,30 | €0,50 | 0.33% |
| bitvavo - kraken | €200,00 | 2026-11-19 | 6.7 u | 50 | 44 | 6 | €0,26 | €0,00 (0x) | **€0,26** | 0.13% | €0,40 | €0,67 | 0.33% |
| bitvavo - kraken | €2.000,00 | 2026-11-19 | 6.7 u | 50 | 30 | 20 | €15,85 | €7,94 (19x) | **€7,91** | 0.40% | €4,01 | €11,92 | 0.60% |
| bitvavo - kraken | €5.000,00 | 2026-11-19 | 6.7 u | 50 | 28 | 22 | €33,76 | €13,48 (24x) | **€20,28** | 0.41% | €10,05 | €30,34 | 0.61% |
| gate - kucoin | €100,00 | 2026-11-19 | 6.7 u | 13 | 7 | 6 | €0,27 | €0,00 (0x) | **€0,27** | 0.27% | €-0,46 | €-0,19 | -0.19% |
| gate - kucoin | €150,00 | 2026-11-19 | 6.7 u | 13 | 7 | 6 | €0,40 | €0,00 (0x) | **€0,40** | 0.27% | €-0,68 | €-0,29 | -0.19% |
| gate - kucoin | €200,00 | 2026-11-19 | 6.7 u | 13 | 7 | 6 | €0,53 | €0,00 (0x) | **€0,53** | 0.27% | €-0,91 | €-0,38 | -0.19% |
| gate - kucoin | €2.000,00 | 2026-11-19 | 6.7 u | 13 | 4 | 9 | €7,05 | €2,98 (9x) | **€4,07** | 0.20% | €-9,11 | €-5,04 | -0.25% |
| gate - kucoin | €5.000,00 | 2026-11-19 | 6.7 u | 13 | 3 | 5 | €13,52 | €2,37 (7x) | **€11,15** | 0.22% | €-22,81 | €-11,66 | -0.23% |

- bitvavo - kraken, €100,00: munten AVA, DYM, GMT, LUNA, MERL, SSV; bruto zonder voorraadgrens zou €717,99 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitvavo - kraken, €150,00: munten AVA, DYM, GMT, LUNA, MERL, SSV; bruto zonder voorraadgrens zou €717,28 zijn, met voorraad €0,20 (GEZIEN boek, GOK model).
- bitvavo - kraken, €200,00: munten AVA, DYM, GMT, LUNA, MERL, SSV; bruto zonder voorraadgrens zou €717,04 zijn, met voorraad €0,26 (GEZIEN boek, GOK model).
- bitvavo - kraken, €2.000,00: munten AVA, DYM, GMT, LUNA, MERL, SSV; bruto zonder voorraadgrens zou €684,57 zijn, met voorraad €15,85 (GEZIEN boek, GOK model).
- bitvavo - kraken, €5.000,00: munten AVA, DYM, GMT, LUNA, MERL, SSV; bruto zonder voorraadgrens zou €637,54 zijn, met voorraad €33,76 (GEZIEN boek, GOK model).
- gate - kucoin, €100,00: munten ERG, IR, LUNC, USTC, VERONA; bruto zonder voorraadgrens zou €48,05 zijn, met voorraad €0,27 (GEZIEN boek, GOK model).
- gate - kucoin, €150,00: munten ERG, IR, LUNC, USTC, VERONA; bruto zonder voorraadgrens zou €48,05 zijn, met voorraad €0,40 (GEZIEN boek, GOK model).
- gate - kucoin, €200,00: munten ERG, IR, LUNC, USTC, VERONA; bruto zonder voorraadgrens zou €48,05 zijn, met voorraad €0,53 (GEZIEN boek, GOK model).
- gate - kucoin, €2.000,00: munten ERG, IR, LUNC, USTC, VERONA; bruto zonder voorraadgrens zou €45,59 zijn, met voorraad €7,05 (GEZIEN boek, GOK model).
- gate - kucoin, €5.000,00: munten ERG, IR, LUNC, USTC, VERONA; bruto zonder voorraadgrens zou €43,13 zijn, met voorraad €13,52 (GEZIEN boek, GOK model).

### Met minstens één grijze beurs (de 5 paren met de meeste bruto winst)

| Beurspaar | Inleg | Dag | Gemeten | Kansen | Gemist (geen voorraad) | Kleiner door voorraad | Bruto winst | Kosten terugschuiven | **Netto handel (bruto min kosten)** | Rendement handel | Koerseffect voorraad | Netto met koerseffect | Rendement met koerseffect |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| kucoin - xt | €100,00 | 2026-11-19 | 6.7 u | 7 | 5 | 2 | €0,22 | €0,00 (0x) | **€0,22** | 0.22% | €0,97 | €1,18 | 1.18% |
| kucoin - xt | €150,00 | 2026-11-19 | 6.7 u | 7 | 5 | 2 | €0,33 | €0,00 (0x) | **€0,33** | 0.22% | €1,45 | €1,78 | 1.18% |
| kucoin - xt | €200,00 | 2026-11-19 | 6.7 u | 7 | 5 | 2 | €0,44 | €0,00 (0x) | **€0,44** | 0.22% | €1,93 | €2,37 | 1.18% |
| kucoin - xt | €2.000,00 | 2026-11-19 | 6.7 u | 7 | 3 | 4 | €9,41 | €2,86 (5x) | **€6,55** | 0.33% | €19,32 | €25,86 | 1.29% |
| kucoin - xt | €5.000,00 | 2026-11-19 | 6.7 u | 7 | 3 | 4 | €22,06 | €2,86 (5x) | **€19,20** | 0.38% | €48,31 | €67,50 | 1.35% |
| bitget - xt | €100,00 | 2026-11-19 | 6.7 u | 7 | 5 | 2 | €0,31 | €0,11 (2x) | **€0,20** | 0.20% | €1,43 | €1,63 | 1.63% |
| bitget - xt | €150,00 | 2026-11-19 | 6.7 u | 7 | 5 | 2 | €0,46 | €0,11 (2x) | **€0,35** | 0.24% | €2,14 | €2,50 | 1.67% |
| bitget - xt | €200,00 | 2026-11-19 | 6.7 u | 7 | 5 | 2 | €0,62 | €0,11 (2x) | **€0,51** | 0.25% | €2,86 | €3,37 | 1.68% |
| bitget - xt | €2.000,00 | 2026-11-19 | 6.7 u | 7 | 4 | 2 | €5,10 | €0,91 (2x) | **€4,19** | 0.21% | €28,56 | €32,75 | 1.64% |
| bitget - xt | €5.000,00 | 2026-11-19 | 6.7 u | 7 | 4 | 2 | €11,48 | €0,92 (3x) | **€10,57** | 0.21% | €71,40 | €81,97 | 1.64% |
| bitget - gate | €100,00 | 2026-11-19 | 6.7 u | 10 | 10 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,90 | €-0,90 | -0.90% |
| bitget - gate | €150,00 | 2026-11-19 | 6.7 u | 10 | 10 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,34 | €-1,34 | -0.90% |
| bitget - gate | €200,00 | 2026-11-19 | 6.7 u | 10 | 6 | 4 | €0,54 | €0,02 (2x) | **€0,52** | 0.26% | €-1,79 | €-1,27 | -0.63% |
| bitget - gate | €2.000,00 | 2026-11-19 | 6.7 u | 10 | 4 | 5 | €7,94 | €1,45 (7x) | **€6,48** | 0.32% | €-17,91 | €-11,42 | -0.57% |
| bitget - gate | €5.000,00 | 2026-11-19 | 6.7 u | 10 | 3 | 5 | €12,17 | €1,25 (5x) | **€10,92** | 0.22% | €-44,77 | €-33,84 | -0.68% |
| htx - xt | €100,00 | 2026-11-19 | 6.7 u | 11 | 11 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,19 | €0,19 | 0.19% |
| htx - xt | €150,00 | 2026-11-19 | 6.7 u | 11 | 11 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,28 | €0,28 | 0.19% |
| htx - xt | €200,00 | 2026-11-19 | 6.7 u | 11 | 7 | 4 | €0,42 | €0,00 (0x) | **€0,42** | 0.21% | €0,37 | €0,79 | 0.40% |
| htx - xt | €2.000,00 | 2026-11-19 | 6.7 u | 11 | 4 | 6 | €7,42 | €3,85 (7x) | **€3,58** | 0.18% | €3,71 | €7,29 | 0.36% |
| htx - xt | €5.000,00 | 2026-11-19 | 6.7 u | 11 | 4 | 6 | €14,61 | €3,39 (6x) | **€11,22** | 0.22% | €9,32 | €20,54 | 0.41% |
| bitget - kucoin | €100,00 | 2026-11-19 | 6.7 u | 15 | 15 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,54 | €-0,54 | -0.54% |
| bitget - kucoin | €150,00 | 2026-11-19 | 6.7 u | 15 | 15 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,81 | €-0,81 | -0.54% |
| bitget - kucoin | €200,00 | 2026-11-19 | 6.7 u | 15 | 15 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,08 | €-1,08 | -0.54% |
| bitget - kucoin | €2.000,00 | 2026-11-19 | 6.7 u | 15 | 7 | 8 | €3,60 | €1,50 (7x) | **€2,10** | 0.10% | €-10,77 | €-8,67 | -0.43% |
| bitget - kucoin | €5.000,00 | 2026-11-19 | 6.7 u | 15 | 7 | 5 | €6,84 | €5,93 (12x) | **€0,91** | 0.02% | €-26,89 | €-25,97 | -0.52% |

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
- htx - xt, €100,00: munten CBK, LUNC, SEI, XDC; bruto zonder voorraadgrens zou €41,14 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - xt, €150,00: munten CBK, LUNC, SEI, XDC; bruto zonder voorraadgrens zou €41,14 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - xt, €200,00: munten CBK, LUNC, SEI, XDC; bruto zonder voorraadgrens zou €40,99 zijn, met voorraad €0,42 (GEZIEN boek, GOK model).
- htx - xt, €2.000,00: munten CBK, LUNC, SEI, XDC; bruto zonder voorraadgrens zou €37,49 zijn, met voorraad €7,42 (GEZIEN boek, GOK model).
- htx - xt, €5.000,00: munten CBK, LUNC, SEI, XDC; bruto zonder voorraadgrens zou €34,24 zijn, met voorraad €14,61 (GEZIEN boek, GOK model).
- bitget - kucoin, €100,00: munten KLV, LUNC, MTX, USDT, USTC, VERONA; bruto zonder voorraadgrens zou €38,22 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - kucoin, €150,00: munten KLV, LUNC, MTX, USDT, USTC, VERONA; bruto zonder voorraadgrens zou €38,22 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - kucoin, €200,00: munten KLV, LUNC, MTX, USDT, USTC, VERONA; bruto zonder voorraadgrens zou €38,22 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - kucoin, €2.000,00: munten KLV, LUNC, MTX, USDT, USTC, VERONA; bruto zonder voorraadgrens zou €35,71 zijn, met voorraad €3,60 (GEZIEN boek, GOK model).
- bitget - kucoin, €5.000,00: munten KLV, LUNC, MTX, USDT, USTC, VERONA; bruto zonder voorraadgrens zou €33,18 zijn, met voorraad €6,84 (GEZIEN boek, GOK model).

### Andere keuzes bij bitvavo - kraken (netto handel, alle dagen samen; GOK)

| Keuze | Inleg | Kansen | Gemist | Bruto winst | Kosten terugschuiven | Netto handel |
|---|---|---|---|---|---|---|
| schuifdrempel 10% | €150,00 | 50 | 44 | €0,20 | €0,00 | **€0,20** |
| schuifdrempel 10% | €2.000,00 | 50 | 34 | €10,42 | €5,99 | **€4,43** |
| schuifdrempel 25% (standaard) | €150,00 | 50 | 44 | €0,20 | €0,00 | **€0,20** |
| schuifdrempel 25% (standaard) | €2.000,00 | 50 | 30 | €15,85 | €7,94 | **€7,91** |
| schuifdrempel 40% | €150,00 | 50 | 44 | €0,20 | €0,00 | **€0,20** |
| schuifdrempel 40% | €2.000,00 | 50 | 32 | €12,44 | €8,60 | **€3,83** |
| alleen MERL en DYM (meer voorraad per munt, achteraf gekozen) | €150,00 | 31 | 29 | €0,23 | €0,00 | **€0,23** |
| alleen MERL en DYM (meer voorraad per munt, achteraf gekozen) | €2.000,00 | 31 | 23 | €20,45 | €6,47 | **€13,98** |

Bij "alleen ..." tellen de kansen in andere munten niet mee (je hebt die munten dan niet).

Dag en Gemeten: de kansen komen alleen uit de uren dat de scanner mat (GEZIEN); het koerseffect loopt door over de hele tijd van de eerste tot de laatste meting. Rendement = netto gedeeld door de inleg, voor die dag. * = koers niet op te halen, koerseffect onbekend (niet als 0 bedoeld). **Het koerseffect is het risico van de voorraad, geen opbrengst van de methode:** bij één munt over een paar uur is het vooral toeval. Kijk voor wat de methode oplevert naar Netto handel.

**Aannames:**

- Winst per kans: de mediaan van wat de scanner op het boek mat bij €100, €500, €1.000, €2.500 en de volle ruimte (GEZIEN), lineair daartussen (GOK). Uitgevoerd 2 minuten na het begin (dan pas weet je dat hij meetelt), één keer per kans; gaat dezelfde kans binnen 5 minuten weer open, dan is het deel van het boek dat je al gebruikte op (GOK).
- Inleg: de helft geld (de quote van de kansen), de helft munten, verdeeld over de munten die op dat paar echte kansen hadden, en alles half op elke beurs (GOK). Die munten zijn **achteraf** gekozen; vooraf weet je dat niet.
- Terugschuiven zodra een kant onder 25% van zijn beginvoorraad komt: de helft van het verschil gaat terug, alleen als de opnamekosten hooguit 1% van het bedrag zijn (GOK, eigen regel).
- Opnamekosten van de munt: wat de scanner bij die beurs zag (GEZIEN uit de API van de beurs; bij Kraken en Gate geschat uit andere beurzen, GOK). Geld: zie de tabel hieronder.
- Een munt is na 30 minuten op de andere beurs (GOK). Zolang iets onderweg is, telt het niet als voorraad; kansen die daardoor niet of kleiner konden, staan als gemist of beperkt.
- Minimale order (in euro en in munten) en minimale opname van de munt per beurs en munt: uit de openbare API van Bitvavo, Kraken, KuCoin en Gate (GEZIEN, opgehaald bij het maken van het rapport). Een kans onder het minimum telt als gemist; een terugschuif onder het opnameminimum wordt opgehoogd tot het minimum. Andere beurzen of geen antwoord: minimale order 10 euro (GOK). Kraken geeft zijn opnameminimum niet openbaar: daar geen minimum (GOK). USDT telt tegen de koers van het moment van de kans; de koers USDT-EUR zelf beweegt niet mee (GOK).
- Koerseffect: slotkoers per 15 minuten (of per uur) uit de openbare candles van Bitvavo, Kraken, KuCoin of Gate (GEZIEN), over alle aangehouden munten, ook als de scanner tussen twee runs even niet mat.
- Niet meegeteld: andere bots die dezelfde kans pakken, dat het boek zich na jouw order aanvult (dan kan het vaker), belasting, en dat de EU-versie van een beurs minder munten kan hebben dan de API die we meten.
- Geld terugschuiven per beurs: bitget EUR: 1 EUR, GOK (1 EUR, 24 uur; niet nagekeken); bitget USDT: 1 USDT, GOK (1 USDT, 30 min; niet nagekeken); bitvavo EUR: 0 EUR, kosten GEZIEN (api.bitvavo.com/v2/assets: EUR withdrawalFee 0), tijd GOK (1 werkdag, SEPA), minimum 0 EUR (GEZIEN, api.bitvavo.com/v2/assets withdrawalMinAmount); gate USDT: 1 USDT, GOK (1 USDT, 30 min; niet nagekeken), minimum 1 USDT (GEZIEN, api.gateio.ws/api/v4/wallet/currency_chains withdraw_amount_min); htx USDT: 1 USDT, GOK (1 USDT, 30 min; niet nagekeken); kraken EUR: 1 EUR, kosten GEZIEN (support.kraken.com/articles/360000381846: Instant SEPA, Banking Circle, 1 EUR, near-instant), tijd GOK (1 uur tot het op de andere beurs staat), minimum 2 EUR (GEZIEN, support.kraken.com/articles/360000381846 Instant SEPA (Banking Circle)); kucoin EUR: 1 EUR, GOK (1 EUR, 24 uur; niet nagekeken); kucoin USDT: 1 USDT, kosten GEZIEN (api.kucoin.com/api/v3/currencies/USDT: BEP20 1 USDT), tijd GOK, minimum 5 USDT (GEZIEN, api.kucoin.com/api/v3/currencies/USDT BEP20 withdrawalMinSize); xt USDT: 1 USDT, GOK (1 USDT, 30 min; niet nagekeken).

## Over de meting

- Opnamekosten bij de echte kansen: 25 van een netwerk dat aan beide kanten open is, 66 van de beurs zelf (laagste open netwerk), 5 geschat uit wat andere beurzen voor die munt vragen (GOK). Onbekende opnamekosten tellen niet als echte kans.
- Netwerk: KuCoin, Gate, Bitget, HTX, XT, Bitstamp, Bitvavo en Poloniex geven hun netwerken per munt. Als beide beurzen dat doen en de namen te koppelen zijn, moet er een netwerk zijn dat aan beide kanten open is. Anders is het netwerk "niet te koppelen" en telt de kans mee (staat apart in de trechter).
- De duur is gemeten in stappen van ±20 seconden; een kans kan een paar rondes eerder begonnen zijn dan we zagen.
- Takerkosten: uit de API waar die ze per paar geeft, anders het standaardtarief uit de README (deels GOK).
- Laatste run: 15 beurzen antwoordden, 2287 munt-quote-paren op minstens twee beurzen (GEZIEN).
