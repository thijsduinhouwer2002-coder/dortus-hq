# Rapport koersverschil-scanner

Gemaakt 2026-11-19 20:39 UTC uit 16 runs, samen ±11.8 uur gemeten (GEZIEN).
Echte kans = winst na alle kosten (opnamekosten bekend), opnemen en storten open (en een netwerk dat aan beide kanten open is, als de beurzen dat geven), minstens €100,00 op het boek, minstens 2 minuten blijven staan, geen andere munt met dezelfde naam.
**Vergund** = beide beurzen hebben een MiCA-vergunning (ESMA-register), vaak via een EU-dochter die minder munten kan hebben dan de wereldwijde API die we meten (GOK). **Grijs** = minstens één beurs zonder vergunning (MEXC, Bitget, HTX, Poloniex, XT, Bitfinex, Binance). Zie README.md.
**Kraken-tarief:** Kraken rekent 0,80% taker op munt tegen EUR, USD, USDT of USDC (GEZIEN, kraken.com/pro/fees, laagste trede); de scanner rekende tot 19 nov met 0,40%. 399 opgeslagen kansen met Kraken uit die runs zijn hier **opnieuw doorgerekend met 0,80%** (GOK-benadering: 0,40% van de inzet aan de Kraken-kant extra op elk gemeten punt van het boek; het boek zelf is niet bewaard). 233 houden daarna nog winst op het boek. Dat ze met hogere kosten ook korter bleven staan, telt niet mee (dus eerder te gunstig).

## Hoeveel wordt er gecontroleerd? (GEZIEN, stand.jsonl)

Per ronde (mediaan over 142 metingen): 1054 kandidaten (verschil op de ticker groter dan de takerkosten), 120 met het orderboek gecontroleerd, 3 nog nooit gecontroleerd (0%).
Bijna alle kandidaten komen aan de beurt; de aantallen hieronder missen weinig.

## Trechter (GEZIEN, eigen metingen)

| Stap | Alle beurzen | Alleen MiCA-beurzen | Met minstens één grijze beurs |
|---|---|---|---|
| Verschillen met winst op het boek na alle kosten | 11134 | 1514 | 9620 |
| ...waarvan opnemen of storten dicht | 2656 | 239 | 2417 |
| ...waarvan status onbekend (beurs geeft het niet openbaar) | 6458 | 1048 | 5410 |
| Opnemen en storten open | 2020 | 227 | 1793 |
| ...en geen netwerk dat aan beide kanten open is: valt af | 25 | 1 | 24 |
| ...en opnamekosten onbekend: valt af | 0 | 0 | 0 |
| ...en minstens €100,00 op het boek | 593 | 131 | 462 |
| ...en minstens 2 minuten blijven staan | 198 | 70 | 128 |
| ...en geen andere munt met dezelfde naam | 175 | 60 | 115 |
|    ...waarvan contractadres bekend en gelijk | 14 | 2 | 12 |
|    ...waarvan contractadres onbekend (telt mee, kan een andere munt zijn) | 161 | 58 | 103 |
|    ...waarvan netwerk gekoppeld en open | 102 | 18 | 84 |
|    ...waarvan netwerk niet te koppelen (telt mee) | 73 | 42 | 31 |
| **Echte kansen** (zelfde munt overlappend in de tijd samengevoegd, beste beurspaar telt) | 118 | 60 | 73 |
| Ter vergelijking: zelfde eisen, maar opnamestatus onbekend (niet meegeteld) | 340 | 83 | 289 |

## Echte kansen per dag (GEZIEN)

| Dag | Echt, alleen MiCA | Echt, met grijs | Mediane winst per kans bij €500 (MiCA / grijs) | Mediane duur |
|---|---|---|---|---|
| 2026-11-19 | 45 | 73 | €2,00 / €1,05 | 5.3 min |
| Totaal | 45 | 73 | €2,00 / €1,05 | 5.3 min |

## Beste munten (GEZIEN)

| | Soort | Kansen | Som winst bij €500 per kans |
|---|---|---|---|
| MERL-EUR | vergund | 13 | €135,36 |
| LUNC-USDT | grijs | 12 | €44,83 |
| USTC-USDT | grijs en vergund | 8 | €24,71 |
| SKY-USD | vergund | 2 | €21,52 |
| YB-USDT | grijs | 1 | €16,34 |
| WAN-USDT | grijs | 4 | €14,24 |
| GMT-EUR | vergund | 11 | €14,03 |
| VERONA-USDT | grijs | 8 | €13,53 |
| AVA-EUR | vergund | 4 | €11,22 |
| LUNA-EUR | vergund | 4 | €10,37 |

## Beste beursparen (kopen op > verkopen op) (GEZIEN)

| | Soort | Kansen | Som winst bij €500 per kans |
|---|---|---|---|
| bitvavo > kraken | vergund | 39 | €174,93 |
| kucoin > bitget | grijs | 9 | €24,65 |
| bitget > gate | grijs | 6 | €23,63 |
| kucoin > htx | grijs | 10 | €22,49 |
| bitstamp > kraken | vergund | 2 | €21,52 |
| gate > xt | grijs | 2 | €19,11 |
| bitget > xt | grijs | 4 | €13,09 |
| kucoin > xt | grijs | 3 | €10,44 |
| htx > xt | grijs | 4 | €10,41 |
| bitget > htx | grijs | 13 | €8,77 |

Beurzen die het vaakst meedoen (koop of verkoop): bitget (grijs) 42, kraken 41, bitvavo 39, kucoin 38, htx (grijs) 36, xt (grijs) 18, gate 17, poloniex (grijs) 3 (GEZIEN).

## Hoeveel kansen blijven staan terwijl je geld schuift? (GEZIEN, duur uit eigen metingen)

Wie geen voorraad op beide beurzen heeft, moet kopen, de munt opnemen, wachten tot hij binnen is en dan verkopen. Hoe lang dat duurt verschilt per munt en netwerk: een paar minuten (snelle ketens) tot een uur of meer (Bitcoin, beurzen die opnames met de hand keuren) (GOK, niet per munt gemeten).

| Overmaaktijd | Alle beurzen | Alleen MiCA-beurzen | Met minstens één grijze beurs |
|---|---|---|---|
| 5 min | 63 van 118 (53%) | 31 van 60 (52%) | 38 van 73 (52%) |
| 10 min | 32 van 118 (27%) | 19 van 60 (32%) | 17 van 73 (23%) |
| 30 min | 21 van 118 (18%) | 14 van 60 (23%) | 9 van 73 (12%) |
| 60 min | 7 van 118 (6%) | 5 van 60 (8%) | 3 van 73 (4%) |

## Wat zou het opleveren over 3 maanden? (GOK, doorgetrokken uit de metingen)

Gemeten over ±11.8 uur (GEZIEN), doorgetrokken naar 90 dagen (GOK: aanname dat de week die we maten gewoon is).

| Beurzen | Inleg | Model | Kansen per uur | Per kans (mediaan) | 3 maanden |
|---|---|---|---|---|---|
| Alleen MiCA | €2.000,00 | bovengrens: elke kans, geld overal tegelijk | 5.07 | €2,73 | €29.873,92 |
| Alleen MiCA | €2.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 3.30 | €3,10 | €51.120,36 |
| Alleen MiCA | €5.000,00 | bovengrens: elke kans, geld overal tegelijk | 5.07 | €3,05 | €33.437,66 |
| Alleen MiCA | €5.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 3.30 | €3,41 | €73.945,25 |
| Alle (met grijs) | €2.000,00 | bovengrens: elke kans, geld overal tegelijk | 9.97 | €1,58 | €34.081,68 |
| Alle (met grijs) | €2.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 3.30 | €3,10 | €51.120,36 |
| Alle (met grijs) | €5.000,00 | bovengrens: elke kans, geld overal tegelijk | 9.97 | €1,85 | €39.858,35 |
| Alle (met grijs) | €5.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 3.30 | €3,41 | €73.945,25 |

Bovengrens: elke kans met de helft van de inleg aan elke kant, alsof het geld op alle beurzen tegelijk staat (kan in het echt niet). Beste beurspaar: het paar is **achteraf** gekozen uit de metingen (vooraf kiezen levert minder op), en het model neemt aan dat je van elke munt al voorraad op de verkoopbeurs hebt.

Waarom dit te rooskleurig is (GOK): elke kans wordt maar één keer geteld met het mediane boek, maar andere bots pakken hem ook; de munt die je als voorraad aanhoudt kan dalen; na een paar kansen moet de voorraad terug (opnamekosten en tijd); minimale opname- en ordergroottes tellen niet mee; en een kans die we 2 minuten zagen staan, staat er niet per se nog als jouw order binnenkomt. Waarom het te somber kan zijn: niet alle kandidaten zijn gecontroleerd, en met voorraad op beide beurzen kun je dezelfde kans vaker pakken als het boek zich aanvult; dat telt hier niet mee.

## Wat houd je echt over? Voorraad op twee beurzen (simulatie)

Per beurspaar: geld en munten op beide beurzen, elke echte kans uitgevoerd tegen het boek zoals gemeten (niet meer dan de ruimte op het boek en niet meer dan de voorraad op die beurs), terugschuiven als een kant leeg dreigt te raken (met opnamekosten en tijd onderweg), en het koerseffect van de aangehouden munten apart. Netto = bruto min kosten terugschuiven plus koerseffect. **Gemeten** (GEZIEN): de kansen, het boek en de koersen; **de rest is een rekenmodel** (GOK, aannames onder de tabel). Geen advies.

**Met €150: netto €1,78 per dag op bitstamp - kraken (koerseffect erbovenop €1,20), €0,14 per dag op bitvavo - kraken (koerseffect erbovenop €-0,91), €0,39 per dag op gate - kucoin (koerseffect erbovenop €-1,89) (GOK: netto handel, rekenmodel op ±11.8 uur meting per dag, alleen MiCA).** "Per dag" is hier één gemeten dag die begint met een gelijk verdeelde voorraad; aan het eind staat de voorraad scheef, dus een volgende dag levert waarschijnlijk minder op, tenzij kansen de andere kant op hem terugbrengen (GOK).

### Alleen MiCA-beurzen (alle paren met echte kansen)

| Beurspaar | Inleg | Dag | Gemeten | Kansen | Gemist (geen voorraad) | Kleiner door voorraad | Bruto winst | Kosten terugschuiven | **Netto handel (bruto min kosten)** | Rendement handel | Koerseffect voorraad | Netto met koerseffect | Rendement met koerseffect |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| bitstamp - kraken | €100,00 | 2026-11-19 | 11.8 u | 2 | 1 | 1 | €1,18 | €0,00 (0x) | **€1,18** | 1.18% | €0,80 | €1,98 | 1.98% |
| bitstamp - kraken | €150,00 | 2026-11-19 | 11.8 u | 2 | 1 | 1 | €1,78 | €0,00 (0x) | **€1,78** | 1.18% | €1,20 | €2,97 | 1.98% |
| bitstamp - kraken | €200,00 | 2026-11-19 | 11.8 u | 2 | 1 | 1 | €2,37 | €0,00 (0x) | **€2,37** | 1.18% | €1,60 | €3,97 | 1.98% |
| bitstamp - kraken | €2.000,00 | 2026-11-19 | 11.8 u | 2 | 1 | 0 | €11,71 | €0,00 (0x) | **€11,71** | 0.59% | €15,99 | €27,70 | 1.38% |
| bitstamp - kraken | €5.000,00 | 2026-11-19 | 11.8 u | 2 | 1 | 0 | €11,71 | €0,00 (0x) | **€11,71** | 0.23% | €39,97 | €51,68 | 1.03% |
| bitvavo - kraken | €100,00 | 2026-11-19 | 11.8 u | 39 | 39 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,61 | €-0,61 | -0.61% |
| bitvavo - kraken | €150,00 | 2026-11-19 | 11.8 u | 39 | 33 | 6 | €0,14 | €0,00 (0x) | **€0,14** | 0.09% | €-0,91 | €-0,77 | -0.52% |
| bitvavo - kraken | €200,00 | 2026-11-19 | 11.8 u | 39 | 33 | 6 | €0,19 | €0,00 (0x) | **€0,19** | 0.09% | €-1,22 | €-1,03 | -0.52% |
| bitvavo - kraken | €2.000,00 | 2026-11-19 | 11.8 u | 39 | 24 | 15 | €12,21 | €7,04 (16x) | **€5,16** | 0.26% | €-12,12 | €-6,96 | -0.35% |
| bitvavo - kraken | €5.000,00 | 2026-11-19 | 11.8 u | 39 | 18 | 21 | €24,25 | €13,56 (22x) | **€10,69** | 0.21% | €-30,34 | €-19,64 | -0.39% |
| gate - kucoin | €100,00 | 2026-11-19 | 11.8 u | 19 | 12 | 7 | €0,26 | €0,00 (0x) | **€0,26** | 0.26% | €-1,26 | €-1,00 | -1.00% |
| gate - kucoin | €150,00 | 2026-11-19 | 11.8 u | 19 | 12 | 7 | €0,39 | €0,00 (0x) | **€0,39** | 0.26% | €-1,89 | €-1,50 | -1.00% |
| gate - kucoin | €200,00 | 2026-11-19 | 11.8 u | 19 | 12 | 7 | €0,52 | €0,00 (0x) | **€0,52** | 0.26% | €-2,52 | €-2,00 | -1.00% |
| gate - kucoin | €2.000,00 | 2026-11-19 | 11.8 u | 19 | 6 | 13 | €8,28 | €4,02 (14x) | **€4,26** | 0.21% | €-25,18 | €-20,93 | -1.05% |
| gate - kucoin | €5.000,00 | 2026-11-19 | 11.8 u | 19 | 4 | 10 | €17,16 | €3,65 (12x) | **€13,51** | 0.27% | €-63,00 | €-49,49 | -0.99% |

- bitstamp - kraken, €100,00: munten SKY; bruto zonder voorraadgrens zou €22,30 zijn, met voorraad €1,18 (GEZIEN boek, GOK model).
- bitstamp - kraken, €150,00: munten SKY; bruto zonder voorraadgrens zou €21,71 zijn, met voorraad €1,78 (GEZIEN boek, GOK model).
- bitstamp - kraken, €200,00: munten SKY; bruto zonder voorraadgrens zou €21,12 zijn, met voorraad €2,37 (GEZIEN boek, GOK model).
- bitstamp - kraken, €2.000,00: munten SKY; bruto zonder voorraadgrens zou €11,71 zijn, met voorraad €11,71 (GEZIEN boek, GOK model).
- bitstamp - kraken, €5.000,00: munten SKY; bruto zonder voorraadgrens zou €11,71 zijn, met voorraad €11,71 (GEZIEN boek, GOK model).
- bitvavo - kraken, €100,00: munten AVA, DYM, GMT, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €539,08 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitvavo - kraken, €150,00: munten AVA, DYM, GMT, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €538,68 zijn, met voorraad €0,14 (GEZIEN boek, GOK model).
- bitvavo - kraken, €200,00: munten AVA, DYM, GMT, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €538,54 zijn, met voorraad €0,19 (GEZIEN boek, GOK model).
- bitvavo - kraken, €2.000,00: munten AVA, DYM, GMT, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €518,85 zijn, met voorraad €12,21 (GEZIEN boek, GOK model).
- bitvavo - kraken, €5.000,00: munten AVA, DYM, GMT, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €485,85 zijn, met voorraad €24,25 (GEZIEN boek, GOK model).
- gate - kucoin, €100,00: munten ALKIMI, ERG, IR, LUNC, USTC, VERONA; bruto zonder voorraadgrens zou €63,54 zijn, met voorraad €0,26 (GEZIEN boek, GOK model).
- gate - kucoin, €150,00: munten ALKIMI, ERG, IR, LUNC, USTC, VERONA; bruto zonder voorraadgrens zou €63,54 zijn, met voorraad €0,39 (GEZIEN boek, GOK model).
- gate - kucoin, €200,00: munten ALKIMI, ERG, IR, LUNC, USTC, VERONA; bruto zonder voorraadgrens zou €63,54 zijn, met voorraad €0,52 (GEZIEN boek, GOK model).
- gate - kucoin, €2.000,00: munten ALKIMI, ERG, IR, LUNC, USTC, VERONA; bruto zonder voorraadgrens zou €61,49 zijn, met voorraad €8,28 (GEZIEN boek, GOK model).
- gate - kucoin, €5.000,00: munten ALKIMI, ERG, IR, LUNC, USTC, VERONA; bruto zonder voorraadgrens zou €59,30 zijn, met voorraad €17,16 (GEZIEN boek, GOK model).

### Met minstens één grijze beurs (de 5 paren met de meeste bruto winst)

| Beurspaar | Inleg | Dag | Gemeten | Kansen | Gemist (geen voorraad) | Kleiner door voorraad | Bruto winst | Kosten terugschuiven | **Netto handel (bruto min kosten)** | Rendement handel | Koerseffect voorraad | Netto met koerseffect | Rendement met koerseffect |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| kucoin - xt | €100,00 | 2026-11-19 | 11.8 u | 11 | 11 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,28 | €-0,28 | -0.28% |
| kucoin - xt | €150,00 | 2026-11-19 | 11.8 u | 11 | 8 | 3 | €0,35 | €0,00 (0x) | **€0,35** | 0.24% | €-0,42 | €-0,07 | -0.04% |
| kucoin - xt | €200,00 | 2026-11-19 | 11.8 u | 11 | 8 | 3 | €0,47 | €0,00 (0x) | **€0,47** | 0.24% | €-0,56 | €-0,09 | -0.04% |
| kucoin - xt | €2.000,00 | 2026-11-19 | 11.8 u | 11 | 3 | 8 | €12,75 | €4,81 (9x) | **€7,94** | 0.40% | €-5,59 | €2,34 | 0.12% |
| kucoin - xt | €5.000,00 | 2026-11-19 | 11.8 u | 11 | 2 | 8 | €25,26 | €4,47 (8x) | **€20,79** | 0.42% | €-14,03 | €6,76 | 0.14% |
| bitget - xt | €100,00 | 2026-11-19 | 11.8 u | 8 | 6 | 2 | €0,31 | €0,11 (2x) | **€0,20** | 0.20% | €1,77 | €1,97 | 1.97% |
| bitget - xt | €150,00 | 2026-11-19 | 11.8 u | 8 | 6 | 2 | €0,46 | €0,11 (2x) | **€0,35** | 0.24% | €2,66 | €3,01 | 2.01% |
| bitget - xt | €200,00 | 2026-11-19 | 11.8 u | 8 | 6 | 2 | €0,62 | €0,11 (2x) | **€0,51** | 0.25% | €3,55 | €4,06 | 2.03% |
| bitget - xt | €2.000,00 | 2026-11-19 | 11.8 u | 8 | 4 | 3 | €6,20 | €0,92 (3x) | **€5,29** | 0.26% | €35,47 | €40,75 | 2.04% |
| bitget - xt | €5.000,00 | 2026-11-19 | 11.8 u | 8 | 4 | 3 | €17,45 | €0,92 (4x) | **€16,54** | 0.33% | €88,67 | €105,21 | 2.10% |
| bitget - gate | €100,00 | 2026-11-19 | 11.8 u | 11 | 11 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,82 | €-0,82 | -0.82% |
| bitget - gate | €150,00 | 2026-11-19 | 11.8 u | 11 | 11 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,23 | €-1,23 | -0.82% |
| bitget - gate | €200,00 | 2026-11-19 | 11.8 u | 11 | 7 | 4 | €0,54 | €0,02 (2x) | **€0,52** | 0.26% | €-1,64 | €-1,11 | -0.56% |
| bitget - gate | €2.000,00 | 2026-11-19 | 11.8 u | 11 | 4 | 6 | €9,36 | €2,37 (9x) | **€6,99** | 0.35% | €-16,38 | €-9,39 | -0.47% |
| bitget - gate | €5.000,00 | 2026-11-19 | 11.8 u | 11 | 3 | 6 | €15,55 | €1,25 (6x) | **€14,30** | 0.29% | €-40,93 | €-26,63 | -0.53% |
| htx - xt | €100,00 | 2026-11-19 | 11.8 u | 16 | 16 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,17 | €-0,17 | -0.17% |
| htx - xt | €150,00 | 2026-11-19 | 11.8 u | 16 | 16 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,25 | €-0,25 | -0.17% |
| htx - xt | €200,00 | 2026-11-19 | 11.8 u | 16 | 12 | 4 | €0,42 | €0,00 (0x) | **€0,42** | 0.21% | €-0,34 | €0,08 | 0.04% |
| htx - xt | €2.000,00 | 2026-11-19 | 11.8 u | 16 | 5 | 10 | €11,99 | €6,31 (12x) | **€5,67** | 0.28% | €-3,41 | €2,26 | 0.11% |
| htx - xt | €5.000,00 | 2026-11-19 | 11.8 u | 16 | 5 | 10 | €22,72 | €5,86 (11x) | **€16,87** | 0.34% | €-8,51 | €8,36 | 0.17% |
| bitget - kucoin | €100,00 | 2026-11-19 | 11.8 u | 19 | 19 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,51 | €-1,51 | -1.51% |
| bitget - kucoin | €150,00 | 2026-11-19 | 11.8 u | 19 | 19 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,27 | €-2,27 | -1.51% |
| bitget - kucoin | €200,00 | 2026-11-19 | 11.8 u | 19 | 19 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,03 | €-3,03 | -1.51% |
| bitget - kucoin | €2.000,00 | 2026-11-19 | 11.8 u | 19 | 7 | 12 | €5,28 | €2,23 (11x) | **€3,05** | 0.15% | €-30,28 | €-27,24 | -1.36% |
| bitget - kucoin | €5.000,00 | 2026-11-19 | 11.8 u | 19 | 7 | 10 | €10,79 | €8,49 (18x) | **€2,30** | 0.05% | €-75,69 | €-73,39 | -1.47% |

- kucoin - xt, €100,00: munten DAG, FIGHT, LUNC; bruto zonder voorraadgrens zou €420,17 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- kucoin - xt, €150,00: munten DAG, FIGHT, LUNC; bruto zonder voorraadgrens zou €420,17 zijn, met voorraad €0,35 (GEZIEN boek, GOK model).
- kucoin - xt, €200,00: munten DAG, FIGHT, LUNC; bruto zonder voorraadgrens zou €420,17 zijn, met voorraad €0,47 (GEZIEN boek, GOK model).
- kucoin - xt, €2.000,00: munten DAG, FIGHT, LUNC; bruto zonder voorraadgrens zou €416,54 zijn, met voorraad €12,75 (GEZIEN boek, GOK model).
- kucoin - xt, €5.000,00: munten DAG, FIGHT, LUNC; bruto zonder voorraadgrens zou €411,23 zijn, met voorraad €25,26 (GEZIEN boek, GOK model).
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
- bitget - kucoin, €100,00: munten EGL1, KLV, LUNC, MTX, USDT, USTC, VERONA; bruto zonder voorraadgrens zou €48,21 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - kucoin, €150,00: munten EGL1, KLV, LUNC, MTX, USDT, USTC, VERONA; bruto zonder voorraadgrens zou €48,21 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - kucoin, €200,00: munten EGL1, KLV, LUNC, MTX, USDT, USTC, VERONA; bruto zonder voorraadgrens zou €48,21 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - kucoin, €2.000,00: munten EGL1, KLV, LUNC, MTX, USDT, USTC, VERONA; bruto zonder voorraadgrens zou €46,05 zijn, met voorraad €5,28 (GEZIEN boek, GOK model).
- bitget - kucoin, €5.000,00: munten EGL1, KLV, LUNC, MTX, USDT, USTC, VERONA; bruto zonder voorraadgrens zou €43,66 zijn, met voorraad €10,79 (GEZIEN boek, GOK model).

### Andere keuzes bij bitvavo - kraken (netto handel, alle dagen samen; GOK)

| Keuze | Inleg | Kansen | Gemist | Bruto winst | Kosten terugschuiven | Netto handel |
|---|---|---|---|---|---|---|
| standaard (schuifdrempel 25%, kostengrens 1%) | €150,00 | 39 | 33 | €0,14 | €0,00 | **€0,14** |
| standaard (schuifdrempel 25%, kostengrens 1%) | €2.000,00 | 39 | 24 | €12,21 | €7,04 | **€5,16** |
| schuifdrempel 10% | €150,00 | 39 | 33 | €0,14 | €0,00 | **€0,14** |
| schuifdrempel 10% | €2.000,00 | 39 | 27 | €8,32 | €5,12 | **€3,20** |
| schuifdrempel 40% | €150,00 | 39 | 33 | €0,14 | €0,00 | **€0,14** |
| schuifdrempel 40% | €2.000,00 | 39 | 24 | €9,55 | €6,72 | **€2,83** |
| kostengrens 2% (achteraf vergeleken) | €150,00 | 39 | 33 | €0,14 | €0,00 | **€0,14** |
| kostengrens 2% (achteraf vergeleken) | €2.000,00 | 39 | 19 | €11,73 | €13,56 | **€-1,83** |
| kostengrens 5% (achteraf vergeleken) | €150,00 | 39 | 30 | €0,18 | €2,48 | **€-2,31** |
| kostengrens 5% (achteraf vergeleken) | €2.000,00 | 39 | 19 | €11,73 | €13,56 | **€-1,83** |
| alleen MERL en GMT (meer voorraad per munt, achteraf gekozen) | €150,00 | 24 | 22 | €0,19 | €0,00 | **€0,19** |
| alleen MERL en GMT (meer voorraad per munt, achteraf gekozen) | €2.000,00 | 24 | 14 | €19,14 | €11,50 | **€7,64** |

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
- Geld terugschuiven per beurs: bitget EUR: 1 EUR, GOK (1 EUR, 24 uur; niet nagekeken); bitget USDT: 1 USDT, GOK (1 USDT, 30 min; niet nagekeken); bitstamp USD: 1 USD, GOK (1 USD, 24 uur; niet nagekeken); bitvavo EUR: 0 EUR, kosten GEZIEN (api.bitvavo.com/v2/assets: EUR withdrawalFee 0), tijd GOK (1 werkdag, SEPA), minimum 0 EUR (GEZIEN, api.bitvavo.com/v2/assets withdrawalMinAmount); gate USDT: 1 USDT, GOK (1 USDT, 30 min; niet nagekeken), minimum 1 USDT (GEZIEN, api.gateio.ws/api/v4/wallet/currency_chains withdraw_amount_min); htx USDT: 1 USDT, GOK (1 USDT, 30 min; niet nagekeken); kraken EUR: 1 EUR, kosten GEZIEN (support.kraken.com/articles/360000381846: Instant SEPA, Banking Circle, 1 EUR, near-instant), tijd GOK (1 uur tot het op de andere beurs staat), minimum 2 EUR (GEZIEN, support.kraken.com/articles/360000381846 Instant SEPA (Banking Circle)); kraken USD: 1 USD, GOK (1 USD, 24 uur; niet nagekeken); kucoin EUR: 1 EUR, GOK (1 EUR, 24 uur; niet nagekeken); kucoin USDT: 1 USDT, kosten GEZIEN (api.kucoin.com/api/v3/currencies/USDT: BEP20 1 USDT), tijd GOK, minimum 5 USDT (GEZIEN, api.kucoin.com/api/v3/currencies/USDT BEP20 withdrawalMinSize); xt USDT: 1 USDT, GOK (1 USDT, 30 min; niet nagekeken).

## Over de meting

- Opnamekosten bij de echte kansen: 46 van een netwerk dat aan beide kanten open is, 57 van de beurs zelf (laagste open netwerk), 15 geschat uit wat andere beurzen voor die munt vragen (GOK). Onbekende opnamekosten tellen niet als echte kans.
- Netwerk: KuCoin, Gate, Bitget, HTX, XT, Bitstamp, Bitvavo en Poloniex geven hun netwerken per munt. Als beide beurzen dat doen en de namen te koppelen zijn, moet er een netwerk zijn dat aan beide kanten open is. Anders is het netwerk "niet te koppelen" en telt de kans mee (staat apart in de trechter).
- De duur is gemeten in stappen van ±20 seconden; een kans kan een paar rondes eerder begonnen zijn dan we zagen.
- Takerkosten: uit de API waar die ze per paar geeft, anders het standaardtarief uit de README (deels GOK).
- Laatste run: 15 beurzen antwoordden, 2287 munt-quote-paren op minstens twee beurzen (GEZIEN).
