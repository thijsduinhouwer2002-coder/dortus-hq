# Rapport koersverschil-scanner

Gemaakt 2026-11-20 02:52 UTC uit 17 runs, samen ±17.8 uur gemeten (GEZIEN).
Echte kans = winst na alle kosten (opnamekosten bekend), opnemen en storten open (en een netwerk dat aan beide kanten open is, als de beurzen dat geven), minstens €100,00 op het boek, minstens 2 minuten blijven staan, geen andere munt met dezelfde naam.
**Vergund** = beide beurzen hebben een MiCA-vergunning (ESMA-register), vaak via een EU-dochter die minder munten kan hebben dan de wereldwijde API die we meten (GOK). **Grijs** = minstens één beurs zonder vergunning (MEXC, Bitget, HTX, Poloniex, XT, Bitfinex, Binance). Zie README.md.
**Kraken-tarief:** Kraken rekent 0,80% taker op munt tegen EUR, USD, USDT of USDC (GEZIEN, kraken.com/pro/fees, laagste trede); de scanner rekende tot 19 nov met 0,40%. 399 opgeslagen kansen met Kraken uit die runs zijn hier **opnieuw doorgerekend met 0,80%** (GOK-benadering: 0,40% van de inzet aan de Kraken-kant extra op elk gemeten punt van het boek; het boek zelf is niet bewaard). 233 houden daarna nog winst op het boek. Dat ze met hogere kosten ook korter bleven staan, telt niet mee (dus eerder te gunstig).

## Hoeveel wordt er gecontroleerd? (GEZIEN, stand.jsonl)

Per ronde (mediaan over 214 metingen): 1066 kandidaten (verschil op de ticker groter dan de takerkosten), 120 met het orderboek gecontroleerd, 2 nog nooit gecontroleerd (0%).
Bijna alle kandidaten komen aan de beurt; de aantallen hieronder missen weinig.

## Trechter (GEZIEN, eigen metingen)

| Stap | Alle beurzen | Alleen MiCA-beurzen | Met minstens één grijze beurs |
|---|---|---|---|
| Verschillen met winst op het boek na alle kosten | 16018 | 2380 | 13638 |
| ...waarvan opnemen of storten dicht | 3659 | 366 | 3293 |
| ...waarvan status onbekend (beurs geeft het niet openbaar) | 9545 | 1711 | 7834 |
| Opnemen en storten open | 2814 | 303 | 2511 |
| ...en geen netwerk dat aan beide kanten open is: valt af | 40 | 3 | 37 |
| ...en opnamekosten onbekend: valt af | 0 | 0 | 0 |
| ...en minstens €100,00 op het boek | 808 | 164 | 644 |
| ...en minstens 2 minuten blijven staan | 258 | 83 | 175 |
| ...en geen andere munt met dezelfde naam | 232 | 72 | 160 |
|    ...waarvan contractadres bekend en gelijk | 19 | 5 | 14 |
|    ...waarvan contractadres onbekend (telt mee, kan een andere munt zijn) | 213 | 67 | 146 |
|    ...waarvan netwerk gekoppeld en open | 139 | 24 | 115 |
|    ...waarvan netwerk niet te koppelen (telt mee) | 93 | 48 | 45 |
| **Echte kansen** (zelfde munt overlappend in de tijd samengevoegd, beste beurspaar telt) | 150 | 72 | 97 |
| Ter vergelijking: zelfde eisen, maar opnamestatus onbekend (niet meegeteld) | 541 | 125 | 468 |

## Echte kansen per dag (GEZIEN)

| Dag | Echt, alleen MiCA | Echt, met grijs | Mediane winst per kans bij €500 (MiCA / grijs) | Mediane duur |
|---|---|---|---|---|
| 2026-11-19 | 49 | 85 | €1,72 / €1,20 | 5.3 min |
| 2026-11-20 | 4 | 12 | €1,25 / €2,60 | 7.2 min |
| Totaal | 53 | 97 | €1,72 / €1,23 | 5.7 min |

## Beste munten (GEZIEN)

| | Soort | Kansen | Som winst bij €500 per kans |
|---|---|---|---|
| MERL-EUR | vergund | 14 | €149,78 |
| LUNC-USDT | grijs | 12 | €56,70 |
| USTC-USDT | grijs en vergund | 8 | €27,88 |
| SKY-USD | vergund | 2 | €21,52 |
| YB-USDT | grijs | 1 | €16,34 |
| LAT-USDT | grijs | 3 | €16,01 |
| GMT-EUR | vergund | 15 | €15,51 |
| WAN-USDT | grijs | 4 | €14,24 |
| VERONA-USDT | grijs | 8 | €13,53 |
| AVA-EUR | vergund | 4 | €11,22 |

## Beste beursparen (kopen op > verkopen op) (GEZIEN)

| | Soort | Kansen | Som winst bij €500 per kans |
|---|---|---|---|
| bitvavo > kraken | vergund | 44 | €190,83 |
| kucoin > htx | grijs | 15 | €36,10 |
| kucoin > bitget | grijs | 10 | €28,27 |
| bitget > xt | grijs | 9 | €27,04 |
| bitget > gate | grijs | 7 | €24,32 |
| bitstamp > kraken | vergund | 2 | €21,52 |
| gate > xt | grijs | 2 | €19,11 |
| bitget > htx | grijs | 19 | €18,16 |
| htx > xt | grijs | 3 | €14,18 |
| bitget > kucoin | grijs | 9 | €12,44 |

Beurzen die het vaakst meedoen (koop of verkoop): bitget (grijs) 58, kucoin 49, htx (grijs) 49, kraken 46, bitvavo 44, gate 26, xt (grijs) 22, poloniex (grijs) 4 (GEZIEN).

## Hoeveel kansen blijven staan terwijl je geld schuift? (GEZIEN, duur uit eigen metingen)

Wie geen voorraad op beide beurzen heeft, moet kopen, de munt opnemen, wachten tot hij binnen is en dan verkopen. Hoe lang dat duurt verschilt per munt en netwerk: een paar minuten (snelle ketens) tot een uur of meer (Bitcoin, beurzen die opnames met de hand keuren) (GOK, niet per munt gemeten).

| Overmaaktijd | Alle beurzen | Alleen MiCA-beurzen | Met minstens één grijze beurs |
|---|---|---|---|
| 5 min | 83 van 150 (55%) | 37 van 72 (51%) | 54 van 97 (56%) |
| 10 min | 50 van 150 (33%) | 23 van 72 (32%) | 32 van 97 (33%) |
| 30 min | 33 van 150 (22%) | 16 van 72 (22%) | 20 van 97 (21%) |
| 60 min | 13 van 150 (9%) | 7 van 72 (10%) | 8 van 97 (8%) |

## Wat zou het opleveren over 3 maanden? (GOK, doorgetrokken uit de metingen)

Gemeten over ±17.8 uur (GEZIEN), doorgetrokken naar 90 dagen (GOK: aanname dat de week die we maten gewoon is).

| Beurzen | Inleg | Model | Kansen per uur | Per kans (mediaan) | 3 maanden |
|---|---|---|---|---|---|
| Alleen MiCA | €2.000,00 | bovengrens: elke kans, geld overal tegelijk | 4.04 | €2,25 | €19.578,78 |
| Alleen MiCA | €2.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 2.47 | €2,73 | €37.198,20 |
| Alleen MiCA | €5.000,00 | bovengrens: elke kans, geld overal tegelijk | 4.04 | €2,58 | €22.466,56 |
| Alleen MiCA | €5.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 2.47 | €3,12 | €53.986,38 |
| Alle (met grijs) | €2.000,00 | bovengrens: elke kans, geld overal tegelijk | 8.41 | €1,60 | €28.991,95 |
| Alle (met grijs) | €2.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 2.47 | €2,73 | €37.198,20 |
| Alle (met grijs) | €5.000,00 | bovengrens: elke kans, geld overal tegelijk | 8.41 | €1,98 | €35.914,74 |
| Alle (met grijs) | €5.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 2.47 | €3,12 | €53.986,38 |

Bovengrens: elke kans met de helft van de inleg aan elke kant, alsof het geld op alle beurzen tegelijk staat (kan in het echt niet). Beste beurspaar: het paar is **achteraf** gekozen uit de metingen (vooraf kiezen levert minder op), en het model neemt aan dat je van elke munt al voorraad op de verkoopbeurs hebt.

Waarom dit te rooskleurig is (GOK): elke kans wordt maar één keer geteld met het mediane boek, maar andere bots pakken hem ook; de munt die je als voorraad aanhoudt kan dalen; na een paar kansen moet de voorraad terug (opnamekosten en tijd); minimale opname- en ordergroottes tellen niet mee; en een kans die we 2 minuten zagen staan, staat er niet per se nog als jouw order binnenkomt. Waarom het te somber kan zijn: niet alle kandidaten zijn gecontroleerd, en met voorraad op beide beurzen kun je dezelfde kans vaker pakken als het boek zich aanvult; dat telt hier niet mee.

## Wat houd je echt over? Voorraad op twee beurzen (simulatie)

Per beurspaar: geld en munten op beide beurzen, elke echte kans uitgevoerd tegen het boek zoals gemeten (niet meer dan de ruimte op het boek en niet meer dan de voorraad op die beurs), terugschuiven als een kant leeg dreigt te raken (met opnamekosten en tijd onderweg), en het koerseffect van de aangehouden munten apart. Netto = bruto min kosten terugschuiven plus koerseffect. **Gemeten** (GEZIEN): de kansen, het boek en de koersen; **de rest is een rekenmodel** (GOK, aannames onder de tabel). Geen advies.

**Met €150: netto €0,89 per dag op bitstamp - kraken (koerseffect erbovenop €-0,85), €0,07 per dag op bitvavo - kraken (koerseffect erbovenop €-0,77), €0,21 per dag op gate - kucoin (koerseffect erbovenop €-2,26) (GOK: netto handel, rekenmodel op ±8.9 uur meting per dag, alleen MiCA).** "Per dag" is hier gemiddeld over 2 gemeten dagen achter elkaar; de eerste begint met een gelijk verdeelde voorraad; aan het eind staat de voorraad scheef, dus een volgende dag levert waarschijnlijk minder op, tenzij kansen de andere kant op hem terugbrengen (GOK).

### Alleen MiCA-beurzen (alle paren met echte kansen)

| Beurspaar | Inleg | Dag | Gemeten | Kansen | Gemist (geen voorraad) | Kleiner door voorraad | Bruto winst | Kosten terugschuiven | **Netto handel (bruto min kosten)** | Rendement handel | Koerseffect voorraad | Netto met koerseffect | Rendement met koerseffect |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| bitstamp - kraken | €100,00 | 2026-11-19 | 14.9 u | 2 | 1 | 1 | €1,18 | €0,00 (0x) | **€1,18** | 1.18% | €0,63 | €1,81 | 1.81% |
| bitstamp - kraken | €100,00 | 2026-11-20 | 2.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,76 | €-1,76 | -1.76% |
| bitstamp - kraken | €150,00 | 2026-11-19 | 14.9 u | 2 | 1 | 1 | €1,78 | €0,00 (0x) | **€1,78** | 1.18% | €0,94 | €2,72 | 1.81% |
| bitstamp - kraken | €150,00 | 2026-11-20 | 2.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,64 | €-2,64 | -1.76% |
| bitstamp - kraken | €200,00 | 2026-11-19 | 14.9 u | 2 | 1 | 1 | €2,37 | €0,00 (0x) | **€2,37** | 1.18% | €1,25 | €3,62 | 1.81% |
| bitstamp - kraken | €200,00 | 2026-11-20 | 2.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,52 | €-3,52 | -1.76% |
| bitstamp - kraken | €2.000,00 | 2026-11-19 | 14.9 u | 2 | 1 | 0 | €11,71 | €0,00 (0x) | **€11,71** | 0.59% | €12,53 | €24,24 | 1.21% |
| bitstamp - kraken | €2.000,00 | 2026-11-20 | 2.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-35,22 | €-35,22 | -1.76% |
| bitstamp - kraken | €5.000,00 | 2026-11-19 | 14.9 u | 2 | 1 | 0 | €11,71 | €0,00 (0x) | **€11,71** | 0.23% | €31,33 | €43,04 | 0.86% |
| bitstamp - kraken | €5.000,00 | 2026-11-20 | 2.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-88,05 | €-88,05 | -1.76% |
| bitvavo - kraken | €100,00 | 2026-11-19 | 14.9 u | 42 | 42 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,53 | €-0,53 | -0.53% |
| bitvavo - kraken | €100,00 | 2026-11-20 | 2.9 u | 2 | 2 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,50 | €-0,50 | -0.50% |
| bitvavo - kraken | €150,00 | 2026-11-19 | 14.9 u | 42 | 36 | 6 | €0,14 | €0,00 (0x) | **€0,14** | 0.09% | €-0,80 | €-0,66 | -0.44% |
| bitvavo - kraken | €150,00 | 2026-11-20 | 2.9 u | 2 | 2 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,74 | €-0,74 | -0.50% |
| bitvavo - kraken | €200,00 | 2026-11-19 | 14.9 u | 42 | 36 | 6 | €0,19 | €0,00 (0x) | **€0,19** | 0.09% | €-1,07 | €-0,88 | -0.44% |
| bitvavo - kraken | €200,00 | 2026-11-20 | 2.9 u | 2 | 2 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,99 | €-0,99 | -0.50% |
| bitvavo - kraken | €2.000,00 | 2026-11-19 | 14.9 u | 42 | 26 | 16 | €14,65 | €7,37 (17x) | **€7,28** | 0.36% | €-10,61 | €-3,33 | -0.17% |
| bitvavo - kraken | €2.000,00 | 2026-11-20 | 2.9 u | 2 | 2 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-9,84 | €-9,84 | -0.49% |
| bitvavo - kraken | €5.000,00 | 2026-11-19 | 14.9 u | 42 | 18 | 24 | €31,16 | €16,84 (26x) | **€14,32** | 0.29% | €-26,61 | €-12,29 | -0.25% |
| bitvavo - kraken | €5.000,00 | 2026-11-20 | 2.9 u | 2 | 0 | 2 | €1,00 | €1,95 (2x) | **€-0,95** | -0.02% | €-24,53 | €-25,48 | -0.51% |
| gate - kucoin | €100,00 | 2026-11-19 | 14.9 u | 24 | 16 | 8 | €0,22 | €0,00 (0x) | **€0,22** | 0.22% | €-0,87 | €-0,66 | -0.66% |
| gate - kucoin | €100,00 | 2026-11-20 | 2.9 u | 2 | 1 | 1 | €0,06 | €0,00 (0x) | **€0,06** | 0.06% | €-2,14 | €-2,08 | -2.08% |
| gate - kucoin | €150,00 | 2026-11-19 | 14.9 u | 24 | 16 | 8 | €0,33 | €0,00 (0x) | **€0,33** | 0.22% | €-1,31 | €-0,99 | -0.66% |
| gate - kucoin | €150,00 | 2026-11-20 | 2.9 u | 2 | 1 | 1 | €0,09 | €0,00 (0x) | **€0,09** | 0.06% | €-3,22 | €-3,12 | -2.08% |
| gate - kucoin | €200,00 | 2026-11-19 | 14.9 u | 24 | 16 | 8 | €0,43 | €0,00 (0x) | **€0,43** | 0.22% | €-1,75 | €-1,31 | -0.66% |
| gate - kucoin | €200,00 | 2026-11-20 | 2.9 u | 2 | 1 | 1 | €0,12 | €0,00 (0x) | **€0,12** | 0.06% | €-4,29 | €-4,16 | -2.08% |
| gate - kucoin | €2.000,00 | 2026-11-19 | 14.9 u | 24 | 6 | 18 | €8,35 | €5,42 (19x) | **€2,94** | 0.15% | €-17,47 | €-14,53 | -0.73% |
| gate - kucoin | €2.000,00 | 2026-11-20 | 2.9 u | 2 | 1 | 1 | €1,23 | €0,00 (0x) | **€1,23** | 0.06% | €-42,78 | €-41,55 | -2.08% |
| gate - kucoin | €5.000,00 | 2026-11-19 | 14.9 u | 24 | 5 | 16 | €17,02 | €5,05 (17x) | **€11,97** | 0.24% | €-43,71 | €-31,74 | -0.63% |
| gate - kucoin | €5.000,00 | 2026-11-20 | 2.9 u | 2 | 1 | 1 | €2,38 | €0,63 (1x) | **€1,75** | 0.04% | €-106,99 | €-105,24 | -2.10% |

- bitstamp - kraken, €100,00: munten SKY; bruto zonder voorraadgrens zou €22,30 zijn, met voorraad €1,18 (GEZIEN boek, GOK model).
- bitstamp - kraken, €150,00: munten SKY; bruto zonder voorraadgrens zou €21,71 zijn, met voorraad €1,78 (GEZIEN boek, GOK model).
- bitstamp - kraken, €200,00: munten SKY; bruto zonder voorraadgrens zou €21,12 zijn, met voorraad €2,37 (GEZIEN boek, GOK model).
- bitstamp - kraken, €2.000,00: munten SKY; bruto zonder voorraadgrens zou €11,71 zijn, met voorraad €11,71 (GEZIEN boek, GOK model).
- bitstamp - kraken, €5.000,00: munten SKY; bruto zonder voorraadgrens zou €11,71 zijn, met voorraad €11,71 (GEZIEN boek, GOK model).
- bitvavo - kraken, €100,00: munten AVA, DYM, GMT, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €587,29 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitvavo - kraken, €150,00: munten AVA, DYM, GMT, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €586,88 zijn, met voorraad €0,14 (GEZIEN boek, GOK model).
- bitvavo - kraken, €200,00: munten AVA, DYM, GMT, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €586,75 zijn, met voorraad €0,19 (GEZIEN boek, GOK model).
- bitvavo - kraken, €2.000,00: munten AVA, DYM, GMT, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €567,05 zijn, met voorraad €14,65 (GEZIEN boek, GOK model).
- bitvavo - kraken, €5.000,00: munten AVA, DYM, GMT, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €533,54 zijn, met voorraad €32,16 (GEZIEN boek, GOK model).
- gate - kucoin, €100,00: munten ALKIMI, ERG, FTT, IR, LUNC, RARI, USTC, VERONA; bruto zonder voorraadgrens zou €81,90 zijn, met voorraad €0,28 (GEZIEN boek, GOK model).
- gate - kucoin, €150,00: munten ALKIMI, ERG, FTT, IR, LUNC, RARI, USTC, VERONA; bruto zonder voorraadgrens zou €81,90 zijn, met voorraad €0,42 (GEZIEN boek, GOK model).
- gate - kucoin, €200,00: munten ALKIMI, ERG, FTT, IR, LUNC, RARI, USTC, VERONA; bruto zonder voorraadgrens zou €81,90 zijn, met voorraad €0,56 (GEZIEN boek, GOK model).
- gate - kucoin, €2.000,00: munten ALKIMI, ERG, FTT, IR, LUNC, RARI, USTC, VERONA; bruto zonder voorraadgrens zou €79,58 zijn, met voorraad €9,59 (GEZIEN boek, GOK model).
- gate - kucoin, €5.000,00: munten ALKIMI, ERG, FTT, IR, LUNC, RARI, USTC, VERONA; bruto zonder voorraadgrens zou €76,72 zijn, met voorraad €19,40 (GEZIEN boek, GOK model).

### Met minstens één grijze beurs (de 5 paren met de meeste bruto winst)

| Beurspaar | Inleg | Dag | Gemeten | Kansen | Gemist (geen voorraad) | Kleiner door voorraad | Bruto winst | Kosten terugschuiven | **Netto handel (bruto min kosten)** | Rendement handel | Koerseffect voorraad | Netto met koerseffect | Rendement met koerseffect |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| kucoin - xt | €100,00 | 2026-11-19 | 14.9 u | 12 | 12 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,15 | €-0,15 | -0.15% |
| kucoin - xt | €100,00 | 2026-11-20 | 2.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,94 | €-0,94 | -0.94% |
| kucoin - xt | €150,00 | 2026-11-19 | 14.9 u | 12 | 9 | 3 | €0,35 | €0,00 (0x) | **€0,35** | 0.24% | €-0,22 | €0,13 | 0.09% |
| kucoin - xt | €150,00 | 2026-11-20 | 2.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,42 | €-1,42 | -0.94% |
| kucoin - xt | €200,00 | 2026-11-19 | 14.9 u | 12 | 9 | 3 | €0,47 | €0,00 (0x) | **€0,47** | 0.24% | €-0,30 | €0,18 | 0.09% |
| kucoin - xt | €200,00 | 2026-11-20 | 2.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,89 | €-1,89 | -0.94% |
| kucoin - xt | €2.000,00 | 2026-11-19 | 14.9 u | 12 | 3 | 9 | €14,56 | €5,16 (10x) | **€9,39** | 0.47% | €-2,94 | €6,45 | 0.32% |
| kucoin - xt | €2.000,00 | 2026-11-20 | 2.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-18,80 | €-18,80 | -0.94% |
| kucoin - xt | €5.000,00 | 2026-11-19 | 14.9 u | 12 | 2 | 9 | €29,75 | €4,82 (9x) | **€24,93** | 0.50% | €-7,39 | €17,55 | 0.35% |
| kucoin - xt | €5.000,00 | 2026-11-20 | 2.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-47,13 | €-47,13 | -0.94% |
| bitget - xt | €100,00 | 2026-11-19 | 14.9 u | 12 | 12 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €1,32 | €1,32 | 1.32% |
| bitget - xt | €100,00 | 2026-11-20 | 2.9 u | 1 | 1 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €1,39 | €1,39 | 1.39% |
| bitget - xt | €150,00 | 2026-11-19 | 14.9 u | 12 | 9 | 3 | €0,49 | €0,11 (3x) | **€0,38** | 0.25% | €1,98 | €2,36 | 1.57% |
| bitget - xt | €150,00 | 2026-11-20 | 2.9 u | 1 | 1 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €2,08 | €2,08 | 1.38% |
| bitget - xt | €200,00 | 2026-11-19 | 14.9 u | 12 | 9 | 3 | €0,65 | €0,11 (3x) | **€0,54** | 0.27% | €2,65 | €3,19 | 1.59% |
| bitget - xt | €200,00 | 2026-11-20 | 2.9 u | 1 | 1 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €2,77 | €2,77 | 1.39% |
| bitget - xt | €2.000,00 | 2026-11-19 | 14.9 u | 12 | 4 | 7 | €11,59 | €1,85 (9x) | **€9,74** | 0.49% | €26,48 | €36,22 | 1.81% |
| bitget - xt | €2.000,00 | 2026-11-20 | 2.9 u | 1 | 0 | 1 | €0,80 | €0,92 (2x) | **€-0,12** | -0.01% | €27,83 | €27,71 | 1.39% |
| bitget - xt | €5.000,00 | 2026-11-19 | 14.9 u | 12 | 4 | 6 | €21,85 | €1,84 (8x) | **€20,00** | 0.40% | €66,19 | €86,20 | 1.72% |
| bitget - xt | €5.000,00 | 2026-11-20 | 2.9 u | 1 | 0 | 1 | €1,77 | €0,92 (2x) | **€0,85** | 0.02% | €69,58 | €70,43 | 1.41% |
| htx - xt | €100,00 | 2026-11-19 | 14.9 u | 18 | 18 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,08 | €-0,08 | -0.08% |
| htx - xt | €100,00 | 2026-11-20 | 2.9 u | 2 | 2 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,88 | €-0,88 | -0.88% |
| htx - xt | €150,00 | 2026-11-19 | 14.9 u | 18 | 18 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,12 | €-0,12 | -0.08% |
| htx - xt | €150,00 | 2026-11-20 | 2.9 u | 2 | 2 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,33 | €-1,33 | -0.88% |
| htx - xt | €200,00 | 2026-11-19 | 14.9 u | 18 | 14 | 4 | €0,42 | €0,00 (0x) | **€0,42** | 0.21% | €-0,16 | €0,25 | 0.13% |
| htx - xt | €200,00 | 2026-11-20 | 2.9 u | 2 | 2 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,77 | €-1,77 | -0.88% |
| htx - xt | €2.000,00 | 2026-11-19 | 14.9 u | 18 | 5 | 12 | €15,21 | €8,02 (15x) | **€7,19** | 0.36% | €-1,68 | €5,50 | 0.28% |
| htx - xt | €2.000,00 | 2026-11-20 | 2.9 u | 2 | 0 | 2 | €2,46 | €0,78 (2x) | **€1,68** | 0.08% | €-17,55 | €-15,87 | -0.79% |
| htx - xt | €5.000,00 | 2026-11-19 | 14.9 u | 18 | 5 | 12 | €30,14 | €7,56 (14x) | **€22,58** | 0.45% | €-4,16 | €18,42 | 0.37% |
| htx - xt | €5.000,00 | 2026-11-20 | 2.9 u | 2 | 0 | 2 | €4,91 | €0,78 (2x) | **€4,12** | 0.08% | €-44,10 | €-39,98 | -0.80% |
| bitget - gate | €100,00 | 2026-11-19 | 14.9 u | 14 | 14 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,32 | €0,32 | 0.32% |
| bitget - gate | €100,00 | 2026-11-20 | 2.9 u | 1 | 1 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,18 | €-0,18 | -0.18% |
| bitget - gate | €150,00 | 2026-11-19 | 14.9 u | 14 | 14 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,48 | €0,48 | 0.32% |
| bitget - gate | €150,00 | 2026-11-20 | 2.9 u | 1 | 1 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,27 | €-0,27 | -0.18% |
| bitget - gate | €200,00 | 2026-11-19 | 14.9 u | 14 | 14 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,64 | €0,64 | 0.32% |
| bitget - gate | €200,00 | 2026-11-20 | 2.9 u | 1 | 1 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,36 | €-0,36 | -0.18% |
| bitget - gate | €2.000,00 | 2026-11-19 | 14.9 u | 14 | 4 | 10 | €8,99 | €2,20 (10x) | **€6,79** | 0.34% | €6,44 | €13,23 | 0.66% |
| bitget - gate | €2.000,00 | 2026-11-20 | 2.9 u | 1 | 0 | 1 | €0,41 | €0,57 (1x) | **€-0,15** | -0.01% | €-3,59 | €-3,74 | -0.19% |
| bitget - gate | €5.000,00 | 2026-11-19 | 14.9 u | 14 | 4 | 8 | €18,05 | €3,69 (10x) | **€14,36** | 0.29% | €16,02 | €30,38 | 0.61% |
| bitget - gate | €5.000,00 | 2026-11-20 | 2.9 u | 1 | 0 | 1 | €0,81 | €0,57 (1x) | **€0,24** | 0.00% | €-9,08 | €-8,84 | -0.18% |
| gate - htx | €100,00 | 2026-11-19 | 14.9 u | 19 | 19 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,79 | €-0,79 | -0.79% |
| gate - htx | €100,00 | 2026-11-20 | 2.9 u | 8 | 8 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,43 | €-2,43 | -2.43% |
| gate - htx | €150,00 | 2026-11-19 | 14.9 u | 19 | 19 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,19 | €-1,19 | -0.79% |
| gate - htx | €150,00 | 2026-11-20 | 2.9 u | 8 | 8 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,65 | €-3,65 | -2.43% |
| gate - htx | €200,00 | 2026-11-19 | 14.9 u | 19 | 19 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,59 | €-1,59 | -0.79% |
| gate - htx | €200,00 | 2026-11-20 | 2.9 u | 8 | 8 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-4,87 | €-4,87 | -2.43% |
| gate - htx | €2.000,00 | 2026-11-19 | 14.9 u | 19 | 6 | 13 | €8,62 | €4,51 (12x) | **€4,12** | 0.21% | €-15,88 | €-11,77 | -0.59% |
| gate - htx | €2.000,00 | 2026-11-20 | 2.9 u | 8 | 2 | 6 | €3,22 | €1,23 (5x) | **€2,00** | 0.10% | €-48,57 | €-46,57 | -2.33% |
| gate - htx | €5.000,00 | 2026-11-19 | 14.9 u | 19 | 6 | 11 | €16,92 | €5,13 (12x) | **€11,79** | 0.24% | €-39,72 | €-27,93 | -0.56% |
| gate - htx | €5.000,00 | 2026-11-20 | 2.9 u | 8 | 2 | 5 | €6,80 | €1,23 (5x) | **€5,57** | 0.11% | €-121,60 | €-116,03 | -2.32% |

- kucoin - xt, €100,00: munten DAG, FIGHT, LUNC; bruto zonder voorraadgrens zou €483,41 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- kucoin - xt, €150,00: munten DAG, FIGHT, LUNC; bruto zonder voorraadgrens zou €483,41 zijn, met voorraad €0,35 (GEZIEN boek, GOK model).
- kucoin - xt, €200,00: munten DAG, FIGHT, LUNC; bruto zonder voorraadgrens zou €483,41 zijn, met voorraad €0,47 (GEZIEN boek, GOK model).
- kucoin - xt, €2.000,00: munten DAG, FIGHT, LUNC; bruto zonder voorraadgrens zou €477,87 zijn, met voorraad €14,56 (GEZIEN boek, GOK model).
- kucoin - xt, €5.000,00: munten DAG, FIGHT, LUNC; bruto zonder voorraadgrens zou €470,01 zijn, met voorraad €29,75 (GEZIEN boek, GOK model).
- bitget - xt, €100,00: munten KOR, KUB, LUNC; bruto zonder voorraadgrens zou €466,32 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - xt, €150,00: munten KOR, KUB, LUNC; bruto zonder voorraadgrens zou €465,95 zijn, met voorraad €0,49 (GEZIEN boek, GOK model).
- bitget - xt, €200,00: munten KOR, KUB, LUNC; bruto zonder voorraadgrens zou €465,82 zijn, met voorraad €0,65 (GEZIEN boek, GOK model).
- bitget - xt, €2.000,00: munten KOR, KUB, LUNC; bruto zonder voorraadgrens zou €458,02 zijn, met voorraad €12,38 (GEZIEN boek, GOK model).
- bitget - xt, €5.000,00: munten KOR, KUB, LUNC; bruto zonder voorraadgrens zou €447,63 zijn, met voorraad €23,61 (GEZIEN boek, GOK model).
- htx - xt, €100,00: munten CBK, LUNC, SEI, XDC; bruto zonder voorraadgrens zou €95,70 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - xt, €150,00: munten CBK, LUNC, SEI, XDC; bruto zonder voorraadgrens zou €95,70 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - xt, €200,00: munten CBK, LUNC, SEI, XDC; bruto zonder voorraadgrens zou €95,56 zijn, met voorraad €0,42 (GEZIEN boek, GOK model).
- htx - xt, €2.000,00: munten CBK, LUNC, SEI, XDC; bruto zonder voorraadgrens zou €92,05 zijn, met voorraad €17,67 (GEZIEN boek, GOK model).
- htx - xt, €5.000,00: munten CBK, LUNC, SEI, XDC; bruto zonder voorraadgrens zou €88,81 zijn, met voorraad €35,05 (GEZIEN boek, GOK model).
- bitget - gate, €100,00: munten BABYSHARK, IR, IRYS, LUNC, RARE, SNEK, VERONA; bruto zonder voorraadgrens zou €82,29 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - gate, €150,00: munten BABYSHARK, IR, IRYS, LUNC, RARE, SNEK, VERONA; bruto zonder voorraadgrens zou €82,29 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - gate, €200,00: munten BABYSHARK, IR, IRYS, LUNC, RARE, SNEK, VERONA; bruto zonder voorraadgrens zou €82,29 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - gate, €2.000,00: munten BABYSHARK, IR, IRYS, LUNC, RARE, SNEK, VERONA; bruto zonder voorraadgrens zou €78,97 zijn, met voorraad €9,41 (GEZIEN boek, GOK model).
- bitget - gate, €5.000,00: munten BABYSHARK, IR, IRYS, LUNC, RARE, SNEK, VERONA; bruto zonder voorraadgrens zou €75,15 zijn, met voorraad €18,86 (GEZIEN boek, GOK model).
- gate - htx, €100,00: munten CBK, KAS, LAT, LUNC, MOVR, SEI, WARD, WLD; bruto zonder voorraadgrens zou €77,60 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- gate - htx, €150,00: munten CBK, KAS, LAT, LUNC, MOVR, SEI, WARD, WLD; bruto zonder voorraadgrens zou €77,60 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- gate - htx, €200,00: munten CBK, KAS, LAT, LUNC, MOVR, SEI, WARD, WLD; bruto zonder voorraadgrens zou €77,60 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- gate - htx, €2.000,00: munten CBK, KAS, LAT, LUNC, MOVR, SEI, WARD, WLD; bruto zonder voorraadgrens zou €73,32 zijn, met voorraad €11,85 (GEZIEN boek, GOK model).
- gate - htx, €5.000,00: munten CBK, KAS, LAT, LUNC, MOVR, SEI, WARD, WLD; bruto zonder voorraadgrens zou €68,52 zijn, met voorraad €23,72 (GEZIEN boek, GOK model).

### Andere keuzes bij bitvavo - kraken (netto handel, alle dagen samen; GOK)

| Keuze | Inleg | Kansen | Gemist | Bruto winst | Kosten terugschuiven | Netto handel |
|---|---|---|---|---|---|---|
| standaard (schuifdrempel 25%, kostengrens 1%) | €150,00 | 44 | 38 | €0,14 | €0,00 | **€0,14** |
| standaard (schuifdrempel 25%, kostengrens 1%) | €2.000,00 | 44 | 28 | €14,65 | €7,37 | **€7,28** |
| schuifdrempel 10% | €150,00 | 44 | 38 | €0,14 | €0,00 | **€0,14** |
| schuifdrempel 10% | €2.000,00 | 44 | 31 | €10,77 | €5,44 | **€5,32** |
| schuifdrempel 40% | €150,00 | 44 | 38 | €0,14 | €0,00 | **€0,14** |
| schuifdrempel 40% | €2.000,00 | 44 | 28 | €11,83 | €7,04 | **€4,78** |
| kostengrens 2% (achteraf vergeleken) | €150,00 | 44 | 38 | €0,14 | €0,00 | **€0,14** |
| kostengrens 2% (achteraf vergeleken) | €2.000,00 | 44 | 19 | €14,94 | €18,79 | **€-3,85** |
| kostengrens 5% (achteraf vergeleken) | €150,00 | 44 | 35 | €0,18 | €2,48 | **€-2,31** |
| kostengrens 5% (achteraf vergeleken) | €2.000,00 | 44 | 19 | €14,94 | €18,79 | **€-3,85** |
| alleen MERL en GMT (meer voorraad per munt, achteraf gekozen) | €150,00 | 29 | 27 | €0,19 | €0,00 | **€0,19** |
| alleen MERL en GMT (meer voorraad per munt, achteraf gekozen) | €2.000,00 | 29 | 15 | €21,35 | €15,43 | **€5,92** |

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

- Opnamekosten bij de echte kansen: 54 van een netwerk dat aan beide kanten open is, 74 van de beurs zelf (laagste open netwerk), 22 geschat uit wat andere beurzen voor die munt vragen (GOK). Onbekende opnamekosten tellen niet als echte kans.
- Netwerk: KuCoin, Gate, Bitget, HTX, XT, Bitstamp, Bitvavo en Poloniex geven hun netwerken per munt. Als beide beurzen dat doen en de namen te koppelen zijn, moet er een netwerk zijn dat aan beide kanten open is. Anders is het netwerk "niet te koppelen" en telt de kans mee (staat apart in de trechter).
- De duur is gemeten in stappen van ±20 seconden; een kans kan een paar rondes eerder begonnen zijn dan we zagen.
- Takerkosten: uit de API waar die ze per paar geeft, anders het standaardtarief uit de README (deels GOK).
- Laatste run: 15 beurzen antwoordden, 2288 munt-quote-paren op minstens twee beurzen (GEZIEN).
