# Rapport koersverschil-scanner

Gemaakt 2026-11-19 17:06 UTC uit 16 runs, samen ±8.3 uur gemeten (GEZIEN).
Echte kans = winst na alle kosten (opnamekosten bekend), opnemen en storten open (en een netwerk dat aan beide kanten open is, als de beurzen dat geven), minstens €100,00 op het boek, minstens 2 minuten blijven staan, geen andere munt met dezelfde naam.
**Vergund** = beide beurzen hebben een MiCA-vergunning (ESMA-register), vaak via een EU-dochter die minder munten kan hebben dan de wereldwijde API die we meten (GOK). **Grijs** = minstens één beurs zonder vergunning (MEXC, Bitget, HTX, Poloniex, XT, Bitfinex, Binance). Zie README.md.
**Kraken-tarief:** Kraken rekent 0,80% taker op munt tegen EUR, USD, USDT of USDC (GEZIEN, kraken.com/pro/fees, laagste trede); de scanner rekende tot 19 nov met 0,40%. 399 opgeslagen kansen met Kraken uit die runs zijn hier **opnieuw doorgerekend met 0,80%** (GOK-benadering: 0,40% van de inzet aan de Kraken-kant extra op elk gemeten punt van het boek; het boek zelf is niet bewaard). 233 houden daarna nog winst op het boek. Dat ze met hogere kosten ook korter bleven staan, telt niet mee (dus eerder te gunstig).

## Hoeveel wordt er gecontroleerd? (GEZIEN, stand.jsonl)

Per ronde (mediaan over 99 metingen): 1054 kandidaten (verschil op de ticker groter dan de takerkosten), 120 met het orderboek gecontroleerd, 3 nog nooit gecontroleerd (0%).
Bijna alle kandidaten komen aan de beurt; de aantallen hieronder missen weinig.

## Trechter (GEZIEN, eigen metingen)

| Stap | Alle beurzen | Alleen MiCA-beurzen | Met minstens één grijze beurs |
|---|---|---|---|
| Verschillen met winst op het boek na alle kosten | 8431 | 1091 | 7340 |
| ...waarvan opnemen of storten dicht | 2034 | 186 | 1848 |
| ...waarvan status onbekend (beurs geeft het niet openbaar) | 4728 | 709 | 4019 |
| Opnemen en storten open | 1669 | 196 | 1473 |
| ...en geen netwerk dat aan beide kanten open is: valt af | 22 | 1 | 21 |
| ...en opnamekosten onbekend: valt af | 0 | 0 | 0 |
| ...en minstens €100,00 op het boek | 517 | 114 | 403 |
| ...en minstens 2 minuten blijven staan | 172 | 62 | 110 |
| ...en geen andere munt met dezelfde naam | 150 | 52 | 98 |
|    ...waarvan contractadres bekend en gelijk | 10 | 1 | 9 |
|    ...waarvan contractadres onbekend (telt mee, kan een andere munt zijn) | 140 | 51 | 89 |
|    ...waarvan netwerk gekoppeld en open | 83 | 15 | 68 |
|    ...waarvan netwerk niet te koppelen (telt mee) | 67 | 37 | 30 |
| **Echte kansen** (zelfde munt overlappend in de tijd samengevoegd, beste beurspaar telt) | 96 | 52 | 58 |
| Ter vergelijking: zelfde eisen, maar opnamestatus onbekend (niet meegeteld) | 244 | 60 | 207 |

## Echte kansen per dag (GEZIEN)

| Dag | Echt, alleen MiCA | Echt, met grijs | Mediane winst per kans bij €500 (MiCA / grijs) | Mediane duur |
|---|---|---|---|---|
| 2026-11-19 | 38 | 58 | €2,08 / €1,19 | 5.2 min |
| Totaal | 38 | 58 | €2,08 / €1,19 | 5.2 min |

## Beste munten (GEZIEN)

| | Soort | Kansen | Som winst bij €500 per kans |
|---|---|---|---|
| MERL-EUR | vergund | 13 | €135,36 |
| LUNC-USDT | grijs | 9 | €40,63 |
| USTC-USDT | grijs en vergund | 7 | €24,59 |
| YB-USDT | grijs | 1 | €16,34 |
| WAN-USDT | grijs | 4 | €14,24 |
| VERONA-USDT | grijs | 7 | €11,93 |
| GMT-EUR | vergund | 8 | €11,91 |
| AVA-EUR | vergund | 4 | €11,22 |
| LUNA-EUR | vergund | 4 | €10,37 |
| WARD-USDT | grijs | 4 | €7,24 |

## Beste beursparen (kopen op > verkopen op) (GEZIEN)

| | Soort | Kansen | Som winst bij €500 per kans |
|---|---|---|---|
| bitvavo > kraken | vergund | 36 | €172,81 |
| kucoin > bitget | grijs | 8 | €24,47 |
| bitget > gate | grijs | 6 | €23,63 |
| kucoin > htx | grijs | 10 | €22,49 |
| gate > xt | grijs | 1 | €16,34 |
| bitget > xt | grijs | 4 | €13,09 |
| bitget > htx | grijs | 10 | €7,00 |
| htx > xt | grijs | 2 | €6,80 |
| kucoin > xt | grijs | 1 | €6,56 |
| bitget > kucoin | grijs | 7 | €5,71 |

Beurzen die het vaakst meedoen (koop of verkoop): bitvavo 36, kraken 36, bitget (grijs) 35, kucoin 31, htx (grijs) 28, gate 12, xt (grijs) 12, poloniex (grijs) 2 (GEZIEN).

## Hoeveel kansen blijven staan terwijl je geld schuift? (GEZIEN, duur uit eigen metingen)

Wie geen voorraad op beide beurzen heeft, moet kopen, de munt opnemen, wachten tot hij binnen is en dan verkopen. Hoe lang dat duurt verschilt per munt en netwerk: een paar minuten (snelle ketens) tot een uur of meer (Bitcoin, beurzen die opnames met de hand keuren) (GOK, niet per munt gemeten).

| Overmaaktijd | Alle beurzen | Alleen MiCA-beurzen | Met minstens één grijze beurs |
|---|---|---|---|
| 5 min | 50 van 96 (52%) | 26 van 52 (50%) | 29 van 58 (50%) |
| 10 min | 24 van 96 (25%) | 15 van 52 (29%) | 12 van 58 (21%) |
| 30 min | 18 van 96 (19%) | 13 van 52 (25%) | 7 van 58 (12%) |
| 60 min | 5 van 96 (5%) | 4 van 52 (8%) | 2 van 58 (3%) |

## Wat zou het opleveren over 3 maanden? (GOK, doorgetrokken uit de metingen)

Gemeten over ±8.3 uur (GEZIEN), doorgetrokken naar 90 dagen (GOK: aanname dat de week die we maten gewoon is).

| Beurzen | Inleg | Model | Kansen per uur | Per kans (mediaan) | 3 maanden |
|---|---|---|---|---|---|
| Alleen MiCA | €2.000,00 | bovengrens: elke kans, geld overal tegelijk | 6.30 | €3,05 | €41.565,85 |
| Alleen MiCA | €2.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 4.36 | €3,24 | €72.067,92 |
| Alleen MiCA | €5.000,00 | bovengrens: elke kans, geld overal tegelijk | 6.30 | €3,12 | €42.544,02 |
| Alleen MiCA | €5.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 4.36 | €3,64 | €104.061,24 |
| Alle (met grijs) | €2.000,00 | bovengrens: elke kans, geld overal tegelijk | 11.64 | €1,98 | €49.685,55 |
| Alle (met grijs) | €2.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 4.36 | €3,24 | €72.067,92 |
| Alle (met grijs) | €5.000,00 | bovengrens: elke kans, geld overal tegelijk | 11.64 | €2,30 | €57.718,28 |
| Alle (met grijs) | €5.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 4.36 | €3,64 | €104.061,24 |

Bovengrens: elke kans met de helft van de inleg aan elke kant, alsof het geld op alle beurzen tegelijk staat (kan in het echt niet). Beste beurspaar: het paar is **achteraf** gekozen uit de metingen (vooraf kiezen levert minder op), en het model neemt aan dat je van elke munt al voorraad op de verkoopbeurs hebt.

Waarom dit te rooskleurig is (GOK): elke kans wordt maar één keer geteld met het mediane boek, maar andere bots pakken hem ook; de munt die je als voorraad aanhoudt kan dalen; na een paar kansen moet de voorraad terug (opnamekosten en tijd); minimale opname- en ordergroottes tellen niet mee; en een kans die we 2 minuten zagen staan, staat er niet per se nog als jouw order binnenkomt. Waarom het te somber kan zijn: niet alle kandidaten zijn gecontroleerd, en met voorraad op beide beurzen kun je dezelfde kans vaker pakken als het boek zich aanvult; dat telt hier niet mee.

## Wat houd je echt over? Voorraad op twee beurzen (simulatie)

Per beurspaar: geld en munten op beide beurzen, elke echte kans uitgevoerd tegen het boek zoals gemeten (niet meer dan de ruimte op het boek en niet meer dan de voorraad op die beurs), terugschuiven als een kant leeg dreigt te raken (met opnamekosten en tijd onderweg), en het koerseffect van de aangehouden munten apart. Netto = bruto min kosten terugschuiven plus koerseffect. **Gemeten** (GEZIEN): de kansen, het boek en de koersen; **de rest is een rekenmodel** (GOK, aannames onder de tabel). Geen advies.

**Met €150: netto €0,14 per dag op bitvavo - kraken (koerseffect erbovenop €-1,50), €0,40 per dag op gate - kucoin (koerseffect erbovenop €-0,35) (GOK: netto handel, rekenmodel op ±8.2 uur meting per dag, alleen MiCA).** "Per dag" is hier één gemeten dag die begint met een gelijk verdeelde voorraad; aan het eind staat de voorraad scheef, dus een volgende dag levert waarschijnlijk minder op, tenzij kansen de andere kant op hem terugbrengen (GOK).

### Alleen MiCA-beurzen (alle paren met echte kansen)

| Beurspaar | Inleg | Dag | Gemeten | Kansen | Gemist (geen voorraad) | Kleiner door voorraad | Bruto winst | Kosten terugschuiven | **Netto handel (bruto min kosten)** | Rendement handel | Koerseffect voorraad | Netto met koerseffect | Rendement met koerseffect |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| bitvavo - kraken | €100,00 | 2026-11-19 | 8.2 u | 36 | 36 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,00 | €-1,00 | -1.00% |
| bitvavo - kraken | €150,00 | 2026-11-19 | 8.2 u | 36 | 30 | 6 | €0,14 | €0,00 (0x) | **€0,14** | 0.09% | €-1,50 | €-1,36 | -0.90% |
| bitvavo - kraken | €200,00 | 2026-11-19 | 8.2 u | 36 | 30 | 6 | €0,19 | €0,00 (0x) | **€0,19** | 0.09% | €-2,00 | €-1,81 | -0.90% |
| bitvavo - kraken | €2.000,00 | 2026-11-19 | 8.2 u | 36 | 21 | 15 | €12,21 | €7,04 (16x) | **€5,16** | 0.26% | €-19,89 | €-14,72 | -0.74% |
| bitvavo - kraken | €5.000,00 | 2026-11-19 | 8.2 u | 36 | 18 | 18 | €22,09 | €10,65 (19x) | **€11,44** | 0.23% | €-49,75 | €-38,31 | -0.77% |
| gate - kucoin | €100,00 | 2026-11-19 | 8.2 u | 16 | 10 | 6 | €0,27 | €0,00 (0x) | **€0,27** | 0.27% | €-0,24 | €0,03 | 0.03% |
| gate - kucoin | €150,00 | 2026-11-19 | 8.2 u | 16 | 10 | 6 | €0,40 | €0,00 (0x) | **€0,40** | 0.27% | €-0,35 | €0,04 | 0.03% |
| gate - kucoin | €200,00 | 2026-11-19 | 8.2 u | 16 | 10 | 6 | €0,53 | €0,00 (0x) | **€0,53** | 0.27% | €-0,47 | €0,06 | 0.03% |
| gate - kucoin | €2.000,00 | 2026-11-19 | 8.2 u | 16 | 5 | 11 | €8,63 | €3,50 (11x) | **€5,13** | 0.26% | €-4,71 | €0,42 | 0.02% |
| gate - kucoin | €5.000,00 | 2026-11-19 | 8.2 u | 16 | 3 | 8 | €17,15 | €2,89 (9x) | **€14,26** | 0.29% | €-11,79 | €2,48 | 0.05% |

- bitvavo - kraken, €100,00: munten AVA, DYM, GMT, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €528,54 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitvavo - kraken, €150,00: munten AVA, DYM, GMT, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €528,13 zijn, met voorraad €0,14 (GEZIEN boek, GOK model).
- bitvavo - kraken, €200,00: munten AVA, DYM, GMT, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €527,99 zijn, met voorraad €0,19 (GEZIEN boek, GOK model).
- bitvavo - kraken, €2.000,00: munten AVA, DYM, GMT, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €508,30 zijn, met voorraad €12,21 (GEZIEN boek, GOK model).
- bitvavo - kraken, €5.000,00: munten AVA, DYM, GMT, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €475,30 zijn, met voorraad €22,09 (GEZIEN boek, GOK model).
- gate - kucoin, €100,00: munten ERG, IR, LUNC, USTC, VERONA; bruto zonder voorraadgrens zou €60,72 zijn, met voorraad €0,27 (GEZIEN boek, GOK model).
- gate - kucoin, €150,00: munten ERG, IR, LUNC, USTC, VERONA; bruto zonder voorraadgrens zou €60,72 zijn, met voorraad €0,40 (GEZIEN boek, GOK model).
- gate - kucoin, €200,00: munten ERG, IR, LUNC, USTC, VERONA; bruto zonder voorraadgrens zou €60,72 zijn, met voorraad €0,53 (GEZIEN boek, GOK model).
- gate - kucoin, €2.000,00: munten ERG, IR, LUNC, USTC, VERONA; bruto zonder voorraadgrens zou €58,26 zijn, met voorraad €8,63 (GEZIEN boek, GOK model).
- gate - kucoin, €5.000,00: munten ERG, IR, LUNC, USTC, VERONA; bruto zonder voorraadgrens zou €55,81 zijn, met voorraad €17,15 (GEZIEN boek, GOK model).

### Met minstens één grijze beurs (de 5 paren met de meeste bruto winst)

| Beurspaar | Inleg | Dag | Gemeten | Kansen | Gemist (geen voorraad) | Kleiner door voorraad | Bruto winst | Kosten terugschuiven | **Netto handel (bruto min kosten)** | Rendement handel | Koerseffect voorraad | Netto met koerseffect | Rendement met koerseffect |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| kucoin - xt | €100,00 | 2026-11-19 | 8.2 u | 9 | 7 | 2 | €0,22 | €0,00 (0x) | **€0,22** | 0.22% | €0,30 | €0,52 | 0.52% |
| kucoin - xt | €150,00 | 2026-11-19 | 8.2 u | 9 | 7 | 2 | €0,33 | €0,00 (0x) | **€0,33** | 0.22% | €0,45 | €0,78 | 0.52% |
| kucoin - xt | €200,00 | 2026-11-19 | 8.2 u | 9 | 7 | 2 | €0,44 | €0,00 (0x) | **€0,44** | 0.22% | €0,60 | €1,04 | 0.52% |
| kucoin - xt | €2.000,00 | 2026-11-19 | 8.2 u | 9 | 3 | 6 | €13,21 | €4,13 (7x) | **€9,08** | 0.45% | €6,05 | €15,12 | 0.76% |
| kucoin - xt | €5.000,00 | 2026-11-19 | 8.2 u | 9 | 3 | 5 | €30,40 | €3,21 (6x) | **€27,19** | 0.54% | €15,07 | €42,26 | 0.85% |
| bitget - xt | €100,00 | 2026-11-19 | 8.2 u | 8 | 6 | 2 | €0,31 | €0,11 (2x) | **€0,20** | 0.20% | €0,92 | €1,12 | 1.12% |
| bitget - xt | €150,00 | 2026-11-19 | 8.2 u | 8 | 6 | 2 | €0,46 | €0,11 (2x) | **€0,35** | 0.24% | €1,38 | €1,74 | 1.16% |
| bitget - xt | €200,00 | 2026-11-19 | 8.2 u | 8 | 6 | 2 | €0,62 | €0,11 (2x) | **€0,51** | 0.25% | €1,84 | €2,35 | 1.17% |
| bitget - xt | €2.000,00 | 2026-11-19 | 8.2 u | 8 | 4 | 3 | €6,20 | €0,92 (3x) | **€5,29** | 0.26% | €18,39 | €23,68 | 1.18% |
| bitget - xt | €5.000,00 | 2026-11-19 | 8.2 u | 8 | 4 | 3 | €17,45 | €0,92 (4x) | **€16,54** | 0.33% | €45,97 | €62,51 | 1.25% |
| bitget - gate | €100,00 | 2026-11-19 | 8.2 u | 11 | 11 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,36 | €-0,36 | -0.36% |
| bitget - gate | €150,00 | 2026-11-19 | 8.2 u | 11 | 11 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,53 | €-0,53 | -0.36% |
| bitget - gate | €200,00 | 2026-11-19 | 8.2 u | 11 | 7 | 4 | €0,54 | €0,02 (2x) | **€0,52** | 0.26% | €-0,71 | €-0,19 | -0.09% |
| bitget - gate | €2.000,00 | 2026-11-19 | 8.2 u | 11 | 4 | 6 | €9,36 | €2,37 (9x) | **€6,99** | 0.35% | €-7,12 | €-0,13 | -0.01% |
| bitget - gate | €5.000,00 | 2026-11-19 | 8.2 u | 11 | 3 | 6 | €15,55 | €1,25 (6x) | **€14,30** | 0.29% | €-17,80 | €-3,49 | -0.07% |
| htx - xt | €100,00 | 2026-11-19 | 8.2 u | 14 | 14 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,40 | €-0,40 | -0.40% |
| htx - xt | €150,00 | 2026-11-19 | 8.2 u | 14 | 14 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,60 | €-0,60 | -0.40% |
| htx - xt | €200,00 | 2026-11-19 | 8.2 u | 14 | 10 | 4 | €0,42 | €0,00 (0x) | **€0,42** | 0.21% | €-0,80 | €-0,38 | -0.19% |
| htx - xt | €2.000,00 | 2026-11-19 | 8.2 u | 14 | 5 | 8 | €9,65 | €5,53 (10x) | **€4,12** | 0.21% | €-8,00 | €-3,88 | -0.19% |
| htx - xt | €5.000,00 | 2026-11-19 | 8.2 u | 14 | 5 | 8 | €19,08 | €5,08 (9x) | **€14,01** | 0.28% | €-20,05 | €-6,04 | -0.12% |
| bitget - kucoin | €100,00 | 2026-11-19 | 8.2 u | 17 | 17 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,26 | €-2,26 | -2.26% |
| bitget - kucoin | €150,00 | 2026-11-19 | 8.2 u | 17 | 17 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,40 | €-3,40 | -2.26% |
| bitget - kucoin | €200,00 | 2026-11-19 | 8.2 u | 17 | 17 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-4,53 | €-4,53 | -2.26% |
| bitget - kucoin | €2.000,00 | 2026-11-19 | 8.2 u | 17 | 7 | 10 | €5,35 | €1,80 (9x) | **€3,55** | 0.18% | €-45,26 | €-41,71 | -2.09% |
| bitget - kucoin | €5.000,00 | 2026-11-19 | 8.2 u | 17 | 7 | 7 | €10,47 | €6,23 (14x) | **€4,23** | 0.08% | €-113,14 | €-108,91 | -2.18% |

- kucoin - xt, €100,00: munten FIGHT, LUNC; bruto zonder voorraadgrens zou €415,61 zijn, met voorraad €0,22 (GEZIEN boek, GOK model).
- kucoin - xt, €150,00: munten FIGHT, LUNC; bruto zonder voorraadgrens zou €415,61 zijn, met voorraad €0,33 (GEZIEN boek, GOK model).
- kucoin - xt, €200,00: munten FIGHT, LUNC; bruto zonder voorraadgrens zou €415,61 zijn, met voorraad €0,44 (GEZIEN boek, GOK model).
- kucoin - xt, €2.000,00: munten FIGHT, LUNC; bruto zonder voorraadgrens zou €409,97 zijn, met voorraad €13,21 (GEZIEN boek, GOK model).
- kucoin - xt, €5.000,00: munten FIGHT, LUNC; bruto zonder voorraadgrens zou €401,70 zijn, met voorraad €30,40 (GEZIEN boek, GOK model).
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
- htx - xt, €100,00: munten CBK, LUNC, SEI, XDC; bruto zonder voorraadgrens zou €50,50 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - xt, €150,00: munten CBK, LUNC, SEI, XDC; bruto zonder voorraadgrens zou €50,50 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - xt, €200,00: munten CBK, LUNC, SEI, XDC; bruto zonder voorraadgrens zou €50,36 zijn, met voorraad €0,42 (GEZIEN boek, GOK model).
- htx - xt, €2.000,00: munten CBK, LUNC, SEI, XDC; bruto zonder voorraadgrens zou €46,85 zijn, met voorraad €9,65 (GEZIEN boek, GOK model).
- htx - xt, €5.000,00: munten CBK, LUNC, SEI, XDC; bruto zonder voorraadgrens zou €43,61 zijn, met voorraad €19,08 (GEZIEN boek, GOK model).
- bitget - kucoin, €100,00: munten KLV, LUNC, MTX, USDT, USTC, VERONA; bruto zonder voorraadgrens zou €46,00 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - kucoin, €150,00: munten KLV, LUNC, MTX, USDT, USTC, VERONA; bruto zonder voorraadgrens zou €46,00 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - kucoin, €200,00: munten KLV, LUNC, MTX, USDT, USTC, VERONA; bruto zonder voorraadgrens zou €46,00 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - kucoin, €2.000,00: munten KLV, LUNC, MTX, USDT, USTC, VERONA; bruto zonder voorraadgrens zou €43,48 zijn, met voorraad €5,35 (GEZIEN boek, GOK model).
- bitget - kucoin, €5.000,00: munten KLV, LUNC, MTX, USDT, USTC, VERONA; bruto zonder voorraadgrens zou €40,96 zijn, met voorraad €10,47 (GEZIEN boek, GOK model).

### Andere keuzes bij bitvavo - kraken (netto handel, alle dagen samen; GOK)

| Keuze | Inleg | Kansen | Gemist | Bruto winst | Kosten terugschuiven | Netto handel |
|---|---|---|---|---|---|---|
| standaard (schuifdrempel 25%, kostengrens 1%) | €150,00 | 36 | 30 | €0,14 | €0,00 | **€0,14** |
| standaard (schuifdrempel 25%, kostengrens 1%) | €2.000,00 | 36 | 21 | €12,21 | €7,04 | **€5,16** |
| schuifdrempel 10% | €150,00 | 36 | 30 | €0,14 | €0,00 | **€0,14** |
| schuifdrempel 10% | €2.000,00 | 36 | 24 | €8,32 | €5,12 | **€3,20** |
| schuifdrempel 40% | €150,00 | 36 | 30 | €0,14 | €0,00 | **€0,14** |
| schuifdrempel 40% | €2.000,00 | 36 | 21 | €9,55 | €6,72 | **€2,83** |
| kostengrens 2% (achteraf vergeleken) | €150,00 | 36 | 30 | €0,14 | €0,00 | **€0,14** |
| kostengrens 2% (achteraf vergeleken) | €2.000,00 | 36 | 19 | €10,80 | €10,65 | **€0,15** |
| kostengrens 5% (achteraf vergeleken) | €150,00 | 36 | 27 | €0,18 | €2,48 | **€-2,31** |
| kostengrens 5% (achteraf vergeleken) | €2.000,00 | 36 | 19 | €10,80 | €10,65 | **€0,15** |
| alleen MERL en GMT (meer voorraad per munt, achteraf gekozen) | €150,00 | 21 | 19 | €0,19 | €0,00 | **€0,19** |
| alleen MERL en GMT (meer voorraad per munt, achteraf gekozen) | €2.000,00 | 21 | 13 | €17,72 | €8,56 | **€9,16** |

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

- Opnamekosten bij de echte kansen: 35 van een netwerk dat aan beide kanten open is, 54 van de beurs zelf (laagste open netwerk), 7 geschat uit wat andere beurzen voor die munt vragen (GOK). Onbekende opnamekosten tellen niet als echte kans.
- Netwerk: KuCoin, Gate, Bitget, HTX, XT, Bitstamp, Bitvavo en Poloniex geven hun netwerken per munt. Als beide beurzen dat doen en de namen te koppelen zijn, moet er een netwerk zijn dat aan beide kanten open is. Anders is het netwerk "niet te koppelen" en telt de kans mee (staat apart in de trechter).
- De duur is gemeten in stappen van ±20 seconden; een kans kan een paar rondes eerder begonnen zijn dan we zagen.
- Takerkosten: uit de API waar die ze per paar geeft, anders het standaardtarief uit de README (deels GOK).
- Laatste run: 15 beurzen antwoordden, 2287 munt-quote-paren op minstens twee beurzen (GEZIEN).
