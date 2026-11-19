# Rapport koersverschil-scanner

Gemaakt 2026-11-19 15:38 UTC uit 9 runs, samen ±6.6 uur gemeten (GEZIEN).
Echte kans = winst na alle kosten (opnamekosten bekend), opnemen en storten open (en een netwerk dat aan beide kanten open is, als de beurzen dat geven), minstens €100,00 op het boek, minstens 2 minuten blijven staan, geen andere munt met dezelfde naam.
**Vergund** = beide beurzen hebben een MiCA-vergunning (ESMA-register), vaak via een EU-dochter die minder munten kan hebben dan de wereldwijde API die we meten (GOK). **Grijs** = minstens één beurs zonder vergunning (MEXC, Bitget, HTX, Poloniex, XT, Bitfinex, Binance). Zie README.md.

## Hoeveel wordt er gecontroleerd? (GEZIEN, stand.jsonl)

Per ronde (mediaan over 79 metingen): 1044 kandidaten (verschil op de ticker groter dan de takerkosten), 120 met het orderboek gecontroleerd, 3 nog nooit gecontroleerd (0%).
Bijna alle kandidaten komen aan de beurt; de aantallen hieronder missen weinig.

## Trechter (GEZIEN, eigen metingen)

| Stap | Alle beurzen | Alleen MiCA-beurzen | Met minstens één grijze beurs |
|---|---|---|---|
| Verschillen met winst op het boek na alle kosten | 5850 | 839 | 5011 |
| ...waarvan opnemen of storten dicht | 1217 | 104 | 1113 |
| ...waarvan status onbekend (beurs geeft het niet openbaar) | 3288 | 492 | 2796 |
| Opnemen en storten open | 1345 | 243 | 1102 |
| ...en geen netwerk dat aan beide kanten open is: valt af | 20 | 1 | 19 |
| ...en opnamekosten onbekend: valt af | 0 | 0 | 0 |
| ...en minstens €100,00 op het boek | 465 | 183 | 282 |
| ...en minstens 2 minuten blijven staan | 138 | 63 | 75 |
| ...en geen andere munt met dezelfde naam | 124 | 57 | 67 |
|    ...waarvan contractadres bekend en gelijk | 7 | 1 | 6 |
|    ...waarvan contractadres onbekend (telt mee, kan een andere munt zijn) | 117 | 56 | 61 |
|    ...waarvan netwerk gekoppeld en open | 55 | 10 | 45 |
|    ...waarvan netwerk niet te koppelen (telt mee) | 69 | 47 | 22 |
| **Echte kansen** (zelfde munt overlappend in de tijd samengevoegd, beste beurspaar telt) | 86 | 57 | 39 |
| Ter vergelijking: zelfde eisen, maar opnamestatus onbekend (niet meegeteld) | 192 | 53 | 158 |

## Echte kansen per dag (GEZIEN)

| Dag | Echt, alleen MiCA | Echt, met grijs | Mediane winst per kans bij €500 (MiCA / grijs) | Mediane duur |
|---|---|---|---|---|
| 2026-11-19 | 47 | 39 | €1,99 / €1,02 | 4.8 min |
| Totaal | 47 | 39 | €1,99 / €1,02 | 4.8 min |

## Beste munten (GEZIEN)

| | Soort | Kansen | Som winst bij €500 per kans |
|---|---|---|---|
| MERL-EUR | vergund | 9 | €91,52 |
| LUNC-USDT | grijs | 5 | €26,38 |
| DYM-EUR | vergund | 20 | €22,57 |
| LUNA-EUR | vergund | 6 | €20,65 |
| GMT-EUR | vergund | 7 | €18,44 |
| YB-USDT | grijs | 1 | €16,34 |
| USTC-USDT | grijs | 4 | €15,61 |
| WAN-USDT | grijs | 3 | €12,65 |
| VERONA-USDT | grijs | 7 | €11,93 |
| AVA-EUR | vergund | 3 | €7,30 |

## Beste beursparen (kopen op > verkopen op) (GEZIEN)

| | Soort | Kansen | Som winst bij €500 per kans |
|---|---|---|---|
| bitvavo > kraken | vergund | 46 | €160,20 |
| bitget > gate | grijs | 5 | €18,41 |
| gate > xt | grijs | 1 | €16,34 |
| kucoin > bitget | grijs | 6 | €16,14 |
| kucoin > htx | grijs | 5 | €13,65 |
| bitget > xt | grijs | 3 | €8,35 |
| kucoin > xt | grijs | 1 | €6,56 |
| htx > xt | grijs | 1 | €5,83 |
| bitget > htx | grijs | 5 | €3,98 |
| bitget > kucoin | grijs | 6 | €3,67 |

Beurzen die het vaakst meedoen (koop of verkoop): bitvavo 46, kraken 46, bitget (grijs) 25, kucoin 20, htx (grijs) 16, gate 9, xt (grijs) 8, poloniex (grijs) 2 (GEZIEN).

## Hoeveel kansen blijven staan terwijl je geld schuift? (GEZIEN, duur uit eigen metingen)

Wie geen voorraad op beide beurzen heeft, moet kopen, de munt opnemen, wachten tot hij binnen is en dan verkopen. Hoe lang dat duurt verschilt per munt en netwerk: een paar minuten (snelle ketens) tot een uur of meer (Bitcoin, beurzen die opnames met de hand keuren) (GOK, niet per munt gemeten).

| Overmaaktijd | Alle beurzen | Alleen MiCA-beurzen | Met minstens één grijze beurs |
|---|---|---|---|
| 5 min | 43 van 86 (50%) | 24 van 57 (42%) | 23 van 39 (59%) |
| 10 min | 19 van 86 (22%) | 13 van 57 (23%) | 8 van 39 (21%) |
| 30 min | 14 van 86 (16%) | 10 van 57 (18%) | 5 van 39 (13%) |
| 60 min | 5 van 86 (6%) | 4 van 57 (7%) | 2 van 39 (5%) |

## Wat zou het opleveren over 3 maanden? (GOK, doorgetrokken uit de metingen)

Gemeten over ±6.6 uur (GEZIEN), doorgetrokken naar 90 dagen (GOK: aanname dat de week die we maten gewoon is).

| Beurzen | Inleg | Model | Kansen per uur | Per kans (mediaan) | 3 maanden |
|---|---|---|---|---|---|
| Alleen MiCA | €2.000,00 | bovengrens: elke kans, geld overal tegelijk | 8.66 | €3,01 | €56.235,73 |
| Alleen MiCA | €2.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 6.99 | €3,76 | €88.246,92 |
| Alleen MiCA | €5.000,00 | bovengrens: elke kans, geld overal tegelijk | 8.66 | €4,84 | €90.544,55 |
| Alleen MiCA | €5.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 6.99 | €5,20 | €137.057,24 |
| Alle (met grijs) | €2.000,00 | bovengrens: elke kans, geld overal tegelijk | 13.06 | €2,44 | €68.755,58 |
| Alle (met grijs) | €2.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 6.99 | €3,76 | €88.246,92 |
| Alle (met grijs) | €5.000,00 | bovengrens: elke kans, geld overal tegelijk | 13.06 | €3,52 | €99.418,79 |
| Alle (met grijs) | €5.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 6.99 | €5,20 | €137.057,24 |

Bovengrens: elke kans met de helft van de inleg aan elke kant, alsof het geld op alle beurzen tegelijk staat (kan in het echt niet). Beste beurspaar: het paar is **achteraf** gekozen uit de metingen (vooraf kiezen levert minder op), en het model neemt aan dat je van elke munt al voorraad op de verkoopbeurs hebt.

Waarom dit te rooskleurig is (GOK): elke kans wordt maar één keer geteld met het mediane boek, maar andere bots pakken hem ook; de munt die je als voorraad aanhoudt kan dalen; na een paar kansen moet de voorraad terug (opnamekosten en tijd); minimale opname- en ordergroottes tellen niet mee; en een kans die we 2 minuten zagen staan, staat er niet per se nog als jouw order binnenkomt. Waarom het te somber kan zijn: niet alle kandidaten zijn gecontroleerd, en met voorraad op beide beurzen kun je dezelfde kans vaker pakken als het boek zich aanvult; dat telt hier niet mee.

## Wat houd je echt over? Voorraad op twee beurzen (simulatie)

Per beurspaar: geld en munten op beide beurzen, elke echte kans uitgevoerd tegen het boek zoals gemeten (niet meer dan de ruimte op het boek en niet meer dan de voorraad op die beurs), terugschuiven als een kant leeg dreigt te raken (met opnamekosten en tijd onderweg), en het koerseffect van de aangehouden munten apart. Netto = bruto min kosten terugschuiven plus koerseffect. **Gemeten** (GEZIEN): de kansen, het boek en de koersen; **de rest is een rekenmodel** (GOK, aannames onder de tabel). Geen advies.

**Met €150: netto €0,20 per dag op bitvavo - kraken (koerseffect erbovenop €0,30), €0,40 per dag op gate - kucoin (koerseffect erbovenop €-0,68) (GOK: netto handel, rekenmodel op ±6.6 uur meting per dag, alleen MiCA).**

### Alleen MiCA-beurzen (alle paren met echte kansen)

| Beurspaar | Inleg | Dag | Gemeten | Kansen | Gemist (geen voorraad) | Kleiner door voorraad | Bruto winst | Kosten terugschuiven | **Netto handel (bruto min kosten)** | Rendement handel | Koerseffect voorraad | Netto met koerseffect | Rendement met koerseffect |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| bitvavo - kraken | €100,00 | 2026-11-19 | 6.6 u | 46 | 46 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,20 | €0,20 | 0.20% |
| bitvavo - kraken | €150,00 | 2026-11-19 | 6.6 u | 46 | 40 | 6 | €0,20 | €0,00 (0x) | **€0,20** | 0.13% | €0,30 | €0,50 | 0.33% |
| bitvavo - kraken | €200,00 | 2026-11-19 | 6.6 u | 46 | 40 | 6 | €0,26 | €0,00 (0x) | **€0,26** | 0.13% | €0,40 | €0,67 | 0.33% |
| bitvavo - kraken | €2.000,00 | 2026-11-19 | 6.6 u | 46 | 26 | 20 | €15,85 | €7,94 (19x) | **€7,91** | 0.40% | €4,01 | €11,92 | 0.60% |
| bitvavo - kraken | €5.000,00 | 2026-11-19 | 6.6 u | 46 | 24 | 22 | €33,76 | €13,48 (24x) | **€20,28** | 0.41% | €10,05 | €30,34 | 0.61% |
| gate - kucoin | €100,00 | 2026-11-19 | 6.6 u | 11 | 5 | 6 | €0,27 | €0,00 (0x) | **€0,27** | 0.27% | €-0,46 | €-0,19 | -0.19% |
| gate - kucoin | €150,00 | 2026-11-19 | 6.6 u | 11 | 5 | 6 | €0,40 | €0,00 (0x) | **€0,40** | 0.27% | €-0,68 | €-0,29 | -0.19% |
| gate - kucoin | €200,00 | 2026-11-19 | 6.6 u | 11 | 5 | 6 | €0,53 | €0,00 (0x) | **€0,53** | 0.27% | €-0,91 | €-0,38 | -0.19% |
| gate - kucoin | €2.000,00 | 2026-11-19 | 6.6 u | 11 | 3 | 8 | €6,52 | €2,81 (8x) | **€3,71** | 0.19% | €-9,11 | €-5,40 | -0.27% |
| gate - kucoin | €5.000,00 | 2026-11-19 | 6.6 u | 11 | 2 | 5 | €12,75 | €2,19 (6x) | **€10,55** | 0.21% | €-22,81 | €-12,26 | -0.25% |

- bitvavo - kraken, €100,00: munten AVA, DYM, GMT, LUNA, MERL, SSV; bruto zonder voorraadgrens zou €540,76 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitvavo - kraken, €150,00: munten AVA, DYM, GMT, LUNA, MERL, SSV; bruto zonder voorraadgrens zou €540,14 zijn, met voorraad €0,20 (GEZIEN boek, GOK model).
- bitvavo - kraken, €200,00: munten AVA, DYM, GMT, LUNA, MERL, SSV; bruto zonder voorraadgrens zou €539,94 zijn, met voorraad €0,26 (GEZIEN boek, GOK model).
- bitvavo - kraken, €2.000,00: munten AVA, DYM, GMT, LUNA, MERL, SSV; bruto zonder voorraadgrens zou €511,63 zijn, met voorraad €15,85 (GEZIEN boek, GOK model).
- bitvavo - kraken, €5.000,00: munten AVA, DYM, GMT, LUNA, MERL, SSV; bruto zonder voorraadgrens zou €470,66 zijn, met voorraad €33,76 (GEZIEN boek, GOK model).
- gate - kucoin, €100,00: munten ERG, IR, LUNC, USTC, VERONA; bruto zonder voorraadgrens zou €40,69 zijn, met voorraad €0,27 (GEZIEN boek, GOK model).
- gate - kucoin, €150,00: munten ERG, IR, LUNC, USTC, VERONA; bruto zonder voorraadgrens zou €40,69 zijn, met voorraad €0,40 (GEZIEN boek, GOK model).
- gate - kucoin, €200,00: munten ERG, IR, LUNC, USTC, VERONA; bruto zonder voorraadgrens zou €40,69 zijn, met voorraad €0,53 (GEZIEN boek, GOK model).
- gate - kucoin, €2.000,00: munten ERG, IR, LUNC, USTC, VERONA; bruto zonder voorraadgrens zou €38,23 zijn, met voorraad €6,52 (GEZIEN boek, GOK model).
- gate - kucoin, €5.000,00: munten ERG, IR, LUNC, USTC, VERONA; bruto zonder voorraadgrens zou €35,77 zijn, met voorraad €12,75 (GEZIEN boek, GOK model).

### Met minstens één grijze beurs (de 5 paren met de meeste bruto winst)

| Beurspaar | Inleg | Dag | Gemeten | Kansen | Gemist (geen voorraad) | Kleiner door voorraad | Bruto winst | Kosten terugschuiven | **Netto handel (bruto min kosten)** | Rendement handel | Koerseffect voorraad | Netto met koerseffect | Rendement met koerseffect |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| kucoin - xt | €100,00 | 2026-11-19 | 6.6 u | 5 | 4 | 1 | €0,22 | €0,00 (0x) | **€0,22** | 0.22% | €1,38 | €1,60 | 1.60% |
| kucoin - xt | €150,00 | 2026-11-19 | 6.6 u | 5 | 4 | 1 | €0,33 | €0,34 (1x) | **€-0,02** | -0.01% | €2,07 | €2,06 | 1.37% |
| kucoin - xt | €200,00 | 2026-11-19 | 6.6 u | 5 | 4 | 1 | €0,43 | €0,34 (1x) | **€0,09** | 0.05% | €2,77 | €2,86 | 1.43% |
| kucoin - xt | €2.000,00 | 2026-11-19 | 6.6 u | 5 | 2 | 3 | €15,97 | €3,76 (6x) | **€12,21** | 0.61% | €27,63 | €39,84 | 1.99% |
| kucoin - xt | €5.000,00 | 2026-11-19 | 6.6 u | 5 | 2 | 3 | €38,66 | €3,76 (6x) | **€34,90** | 0.70% | €69,10 | €104,00 | 2.08% |
| bitget - xt | €100,00 | 2026-11-19 | 6.6 u | 6 | 4 | 2 | €0,31 | €0,11 (2x) | **€0,20** | 0.20% | €1,43 | €1,63 | 1.63% |
| bitget - xt | €150,00 | 2026-11-19 | 6.6 u | 6 | 4 | 2 | €0,46 | €0,11 (2x) | **€0,35** | 0.24% | €2,14 | €2,50 | 1.67% |
| bitget - xt | €200,00 | 2026-11-19 | 6.6 u | 6 | 4 | 2 | €0,62 | €0,11 (2x) | **€0,51** | 0.25% | €2,86 | €3,37 | 1.68% |
| bitget - xt | €2.000,00 | 2026-11-19 | 6.6 u | 6 | 3 | 2 | €5,10 | €0,91 (2x) | **€4,19** | 0.21% | €28,56 | €32,75 | 1.64% |
| bitget - xt | €5.000,00 | 2026-11-19 | 6.6 u | 6 | 3 | 2 | €11,48 | €0,92 (3x) | **€10,57** | 0.21% | €71,40 | €81,96 | 1.64% |
| bitget - gate | €100,00 | 2026-11-19 | 6.6 u | 9 | 9 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,90 | €-0,90 | -0.90% |
| bitget - gate | €150,00 | 2026-11-19 | 6.6 u | 9 | 9 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,34 | €-1,34 | -0.90% |
| bitget - gate | €200,00 | 2026-11-19 | 6.6 u | 9 | 5 | 4 | €0,54 | €0,02 (2x) | **€0,52** | 0.26% | €-1,79 | €-1,27 | -0.63% |
| bitget - gate | €2.000,00 | 2026-11-19 | 6.6 u | 9 | 3 | 5 | €7,94 | €1,45 (7x) | **€6,48** | 0.32% | €-17,91 | €-11,42 | -0.57% |
| bitget - gate | €5.000,00 | 2026-11-19 | 6.6 u | 9 | 2 | 5 | €12,17 | €1,25 (5x) | **€10,92** | 0.22% | €-44,77 | €-33,84 | -0.68% |
| htx - xt | €100,00 | 2026-11-19 | 6.6 u | 10 | 10 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,19 | €0,19 | 0.19% |
| htx - xt | €150,00 | 2026-11-19 | 6.6 u | 10 | 10 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,28 | €0,28 | 0.19% |
| htx - xt | €200,00 | 2026-11-19 | 6.6 u | 10 | 6 | 4 | €0,42 | €0,00 (0x) | **€0,42** | 0.21% | €0,37 | €0,79 | 0.40% |
| htx - xt | €2.000,00 | 2026-11-19 | 6.6 u | 10 | 3 | 6 | €7,42 | €3,83 (7x) | **€3,59** | 0.18% | €3,71 | €7,30 | 0.37% |
| htx - xt | €5.000,00 | 2026-11-19 | 6.6 u | 10 | 3 | 6 | €14,61 | €3,38 (6x) | **€11,23** | 0.22% | €9,32 | €20,55 | 0.41% |
| gate - xt | €100,00 | 2026-11-19 | 6.6 u | 1 | 0 | 1 | €0,87 | €0,00 (0x) | **€0,87** | 0.87% | €22,66 | €23,53 | 23.53% |
| gate - xt | €150,00 | 2026-11-19 | 6.6 u | 1 | 0 | 1 | €1,30 | €0,00 (0x) | **€1,30** | 0.87% | €33,99 | €35,29 | 23.53% |
| gate - xt | €200,00 | 2026-11-19 | 6.6 u | 1 | 0 | 1 | €1,74 | €0,00 (0x) | **€1,74** | 0.87% | €45,31 | €47,05 | 23.53% |
| gate - xt | €2.000,00 | 2026-11-19 | 6.6 u | 1 | 0 | 1 | €17,18 | €1,75 (2x) | **€15,43** | 0.77% | €453,02 | €468,45 | 23.42% |
| gate - xt | €5.000,00 | 2026-11-19 | 6.6 u | 1 | 0 | 1 | €33,84 | €1,75 (2x) | **€32,08** | 0.64% | €1.132,74 | €1.164,82 | 23.30% |

- kucoin - xt, €100,00: munten LUNC; bruto zonder voorraadgrens zou €306,53 zijn, met voorraad €0,22 (GEZIEN boek, GOK model).
- kucoin - xt, €150,00: munten LUNC; bruto zonder voorraadgrens zou €306,53 zijn, met voorraad €0,33 (GEZIEN boek, GOK model).
- kucoin - xt, €200,00: munten LUNC; bruto zonder voorraadgrens zou €306,53 zijn, met voorraad €0,43 (GEZIEN boek, GOK model).
- kucoin - xt, €2.000,00: munten LUNC; bruto zonder voorraadgrens zou €295,31 zijn, met voorraad €15,97 (GEZIEN boek, GOK model).
- kucoin - xt, €5.000,00: munten LUNC; bruto zonder voorraadgrens zou €279,54 zijn, met voorraad €38,66 (GEZIEN boek, GOK model).
- bitget - xt, €100,00: munten KOR, LUNC; bruto zonder voorraadgrens zou €280,38 zijn, met voorraad €0,31 (GEZIEN boek, GOK model).
- bitget - xt, €150,00: munten KOR, LUNC; bruto zonder voorraadgrens zou €280,33 zijn, met voorraad €0,46 (GEZIEN boek, GOK model).
- bitget - xt, €200,00: munten KOR, LUNC; bruto zonder voorraadgrens zou €280,28 zijn, met voorraad €0,62 (GEZIEN boek, GOK model).
- bitget - xt, €2.000,00: munten KOR, LUNC; bruto zonder voorraadgrens zou €275,33 zijn, met voorraad €5,10 (GEZIEN boek, GOK model).
- bitget - xt, €5.000,00: munten KOR, LUNC; bruto zonder voorraadgrens zou €264,69 zijn, met voorraad €11,48 (GEZIEN boek, GOK model).
- bitget - gate, €100,00: munten BABYSHARK, IR, LUNC, VERONA; bruto zonder voorraadgrens zou €46,36 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - gate, €150,00: munten BABYSHARK, IR, LUNC, VERONA; bruto zonder voorraadgrens zou €46,36 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - gate, €200,00: munten BABYSHARK, IR, LUNC, VERONA; bruto zonder voorraadgrens zou €46,24 zijn, met voorraad €0,54 (GEZIEN boek, GOK model).
- bitget - gate, €2.000,00: munten BABYSHARK, IR, LUNC, VERONA; bruto zonder voorraadgrens zou €42,45 zijn, met voorraad €7,94 (GEZIEN boek, GOK model).
- bitget - gate, €5.000,00: munten BABYSHARK, IR, LUNC, VERONA; bruto zonder voorraadgrens zou €43,24 zijn, met voorraad €12,17 (GEZIEN boek, GOK model).
- htx - xt, €100,00: munten CBK, LUNC, SEI, XDC; bruto zonder voorraadgrens zou €38,12 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - xt, €150,00: munten CBK, LUNC, SEI, XDC; bruto zonder voorraadgrens zou €38,12 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - xt, €200,00: munten CBK, LUNC, SEI, XDC; bruto zonder voorraadgrens zou €37,97 zijn, met voorraad €0,42 (GEZIEN boek, GOK model).
- htx - xt, €2.000,00: munten CBK, LUNC, SEI, XDC; bruto zonder voorraadgrens zou €34,47 zijn, met voorraad €7,42 (GEZIEN boek, GOK model).
- htx - xt, €5.000,00: munten CBK, LUNC, SEI, XDC; bruto zonder voorraadgrens zou €31,22 zijn, met voorraad €14,61 (GEZIEN boek, GOK model).
- gate - xt, €100,00: munten YB; bruto zonder voorraadgrens zou €42,96 zijn, met voorraad €0,87 (GEZIEN boek, GOK model).
- gate - xt, €150,00: munten YB; bruto zonder voorraadgrens zou €42,96 zijn, met voorraad €1,30 (GEZIEN boek, GOK model).
- gate - xt, €200,00: munten YB; bruto zonder voorraadgrens zou €42,96 zijn, met voorraad €1,74 (GEZIEN boek, GOK model).
- gate - xt, €2.000,00: munten YB; bruto zonder voorraadgrens zou €42,96 zijn, met voorraad €17,18 (GEZIEN boek, GOK model).
- gate - xt, €5.000,00: munten YB; bruto zonder voorraadgrens zou €42,96 zijn, met voorraad €33,84 (GEZIEN boek, GOK model).

### Andere keuzes bij bitvavo - kraken (netto handel, alle dagen samen; GOK)

| Keuze | Inleg | Kansen | Gemist | Bruto winst | Kosten terugschuiven | Netto handel |
|---|---|---|---|---|---|---|
| schuifdrempel 10% | €150,00 | 46 | 40 | €0,20 | €0,00 | **€0,20** |
| schuifdrempel 10% | €2.000,00 | 46 | 30 | €10,42 | €5,99 | **€4,43** |
| schuifdrempel 25% (standaard) | €150,00 | 46 | 40 | €0,20 | €0,00 | **€0,20** |
| schuifdrempel 25% (standaard) | €2.000,00 | 46 | 26 | €15,85 | €7,94 | **€7,91** |
| schuifdrempel 40% | €150,00 | 46 | 40 | €0,20 | €0,00 | **€0,20** |
| schuifdrempel 40% | €2.000,00 | 46 | 28 | €12,44 | €8,60 | **€3,83** |
| alleen MERL en DYM (meer voorraad per munt, achteraf gekozen) | €150,00 | 29 | 27 | €0,23 | €0,00 | **€0,23** |
| alleen MERL en DYM (meer voorraad per munt, achteraf gekozen) | €2.000,00 | 29 | 21 | €20,45 | €6,47 | **€13,98** |

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
- Geld terugschuiven per beurs: bitget USDT: 1 USDT, GOK (1 USDT, 30 min; niet nagekeken); bitvavo EUR: 0 EUR, kosten GEZIEN (api.bitvavo.com/v2/assets: EUR withdrawalFee 0), tijd GOK (1 werkdag, SEPA), minimum 0 EUR (GEZIEN, api.bitvavo.com/v2/assets withdrawalMinAmount); gate USDT: 1 USDT, GOK (1 USDT, 30 min; niet nagekeken), minimum 1 USDT (GEZIEN, api.gateio.ws/api/v4/wallet/currency_chains withdraw_amount_min); htx USDT: 1 USDT, GOK (1 USDT, 30 min; niet nagekeken); kraken EUR: 1 EUR, kosten GEZIEN (support.kraken.com/articles/360000381846: Instant SEPA, Banking Circle, 1 EUR, near-instant), tijd GOK (1 uur tot het op de andere beurs staat), minimum 2 EUR (GEZIEN, support.kraken.com/articles/360000381846 Instant SEPA (Banking Circle)); kucoin USDT: 1 USDT, kosten GEZIEN (api.kucoin.com/api/v3/currencies/USDT: BEP20 1 USDT), tijd GOK, minimum 5 USDT (GEZIEN, api.kucoin.com/api/v3/currencies/USDT BEP20 withdrawalMinSize); xt USDT: 1 USDT, GOK (1 USDT, 30 min; niet nagekeken).

## Over de meting

- Opnamekosten bij de echte kansen: 21 van een netwerk dat aan beide kanten open is, 60 van de beurs zelf (laagste open netwerk), 5 geschat uit wat andere beurzen voor die munt vragen (GOK). Onbekende opnamekosten tellen niet als echte kans.
- Netwerk: KuCoin, Gate, Bitget, HTX, XT, Bitstamp, Bitvavo en Poloniex geven hun netwerken per munt. Als beide beurzen dat doen en de namen te koppelen zijn, moet er een netwerk zijn dat aan beide kanten open is. Anders is het netwerk "niet te koppelen" en telt de kans mee (staat apart in de trechter).
- De duur is gemeten in stappen van ±20 seconden; een kans kan een paar rondes eerder begonnen zijn dan we zagen.
- Takerkosten: uit de API waar die ze per paar geeft, anders het standaardtarief uit de README (deels GOK).
- Laatste run: 15 beurzen antwoordden, 2286 munt-quote-paren op minstens twee beurzen (GEZIEN).
