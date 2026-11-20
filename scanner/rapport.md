# Rapport koersverschil-scanner

Gemaakt 2026-11-20 11:47 UTC uit 19 runs, samen ±26.1 uur gemeten (GEZIEN).
Echte kans = winst na alle kosten (opnamekosten bekend), opnemen en storten open (en een netwerk dat aan beide kanten open is, als de beurzen dat geven), minstens €100,00 op het boek, minstens 2 minuten blijven staan, geen andere munt met dezelfde naam.
**Vergund** = beide beurzen hebben een MiCA-vergunning (ESMA-register), vaak via een EU-dochter die minder munten kan hebben dan de wereldwijde API die we meten (GOK). **Grijs** = minstens één beurs zonder vergunning (MEXC, Bitget, HTX, Poloniex, XT, Bitfinex, Binance). Zie README.md.
**Kraken-tarief:** Kraken rekent 0,80% taker op munt tegen EUR, USD, USDT of USDC (GEZIEN, kraken.com/pro/fees, laagste trede); de scanner rekende tot 19 nov met 0,40%. 399 opgeslagen kansen met Kraken uit die runs zijn hier **opnieuw doorgerekend met 0,80%** (GOK-benadering: 0,40% van de inzet aan de Kraken-kant extra op elk gemeten punt van het boek; het boek zelf is niet bewaard). 233 houden daarna nog winst op het boek. Dat ze met hogere kosten ook korter bleven staan, telt niet mee (dus eerder te gunstig).

## Hoeveel wordt er gecontroleerd? (GEZIEN, stand.jsonl)

Per ronde (mediaan over 313 metingen): 1106 kandidaten (verschil op de ticker groter dan de takerkosten), 120 met het orderboek gecontroleerd, 2 nog nooit gecontroleerd (0%).
Bijna alle kandidaten komen aan de beurt; de aantallen hieronder missen weinig.

## Trechter (GEZIEN, eigen metingen)

| Stap | Alle beurzen | Alleen MiCA-beurzen | Met minstens één grijze beurs |
|---|---|---|---|
| Verschillen met winst op het boek na alle kosten | 21860 | 3225 | 18635 |
| ...waarvan opnemen of storten dicht | 4930 | 502 | 4428 |
| ...waarvan status onbekend (beurs geeft het niet openbaar) | 12750 | 2269 | 10481 |
| Opnemen en storten open | 4180 | 454 | 3726 |
| ...en geen netwerk dat aan beide kanten open is: valt af | 121 | 4 | 117 |
| ...en opnamekosten onbekend: valt af | 0 | 0 | 0 |
| ...en minstens €100,00 op het boek | 1191 | 234 | 957 |
| ...en minstens 2 minuten blijven staan | 361 | 111 | 250 |
| ...en geen andere munt met dezelfde naam | 329 | 98 | 231 |
|    ...waarvan contractadres bekend en gelijk | 42 | 15 | 27 |
|    ...waarvan contractadres onbekend (telt mee, kan een andere munt zijn) | 287 | 83 | 204 |
|    ...waarvan netwerk gekoppeld en open | 212 | 42 | 170 |
|    ...waarvan netwerk niet te koppelen (telt mee) | 117 | 56 | 61 |
| **Echte kansen** (zelfde munt overlappend in de tijd samengevoegd, beste beurspaar telt) | 207 | 98 | 135 |
| Ter vergelijking: zelfde eisen, maar opnamestatus onbekend (niet meegeteld) | 765 | 182 | 654 |

## Echte kansen per dag (GEZIEN)

| Dag | Echt, alleen MiCA | Echt, met grijs | Mediane winst per kans bij €500 (MiCA / grijs) | Mediane duur |
|---|---|---|---|---|
| 2026-11-19 | 49 | 86 | €2,00 / €1,21 | 5.3 min |
| 2026-11-20 | 23 | 49 | €0,68 / €1,32 | 7.7 min |
| Totaal | 72 | 135 | €1,72 / €1,23 | 6.0 min |

## Beste munten (GEZIEN)

| | Soort | Kansen | Som winst bij €500 per kans |
|---|---|---|---|
| MERL-EUR | vergund | 17 | €201,75 |
| LUNC-USDT | grijs | 11 | €59,26 |
| MEME-USDT | grijs | 1 | €37,90 |
| USTC-USDT | grijs en vergund | 10 | €37,04 |
| KYO-USDT | vergund | 2 | €22,38 |
| SKY-USD | vergund | 2 | €21,52 |
| LAT-USDT | grijs | 3 | €17,59 |
| YB-USDT | grijs | 2 | €17,52 |
| GMT-EUR | vergund | 20 | €17,13 |
| WAN-USDT | grijs | 5 | €16,06 |

## Beste beursparen (kopen op > verkopen op) (GEZIEN)

| | Soort | Kansen | Som winst bij €500 per kans |
|---|---|---|---|
| bitvavo > kraken | vergund | 52 | €244,42 |
| bitget > htx | grijs | 30 | €66,01 |
| kucoin > htx | grijs | 20 | €55,35 |
| gate > kucoin | vergund | 13 | €46,21 |
| bitget > xt | grijs | 12 | €43,27 |
| kucoin > bitget | grijs | 16 | €40,81 |
| bitget > gate | grijs | 8 | €27,78 |
| bitstamp > kraken | vergund | 2 | €21,52 |
| gate > xt | grijs | 2 | €19,11 |
| bitget > kucoin | grijs | 15 | €17,13 |

Beurzen die het vaakst meedoen (koop of verkoop): bitget (grijs) 88, kucoin 78, htx (grijs) 65, kraken 54, bitvavo 52, gate 42, xt (grijs) 25, poloniex (grijs) 8 (GEZIEN).

## Hoeveel kansen blijven staan terwijl je geld schuift? (GEZIEN, duur uit eigen metingen)

Wie geen voorraad op beide beurzen heeft, moet kopen, de munt opnemen, wachten tot hij binnen is en dan verkopen. Hoe lang dat duurt verschilt per munt en netwerk: een paar minuten (snelle ketens) tot een uur of meer (Bitcoin, beurzen die opnames met de hand keuren) (GOK, niet per munt gemeten).

| Overmaaktijd | Alle beurzen | Alleen MiCA-beurzen | Met minstens één grijze beurs |
|---|---|---|---|
| 5 min | 124 van 207 (60%) | 57 van 98 (58%) | 79 van 135 (59%) |
| 10 min | 77 van 207 (37%) | 36 van 98 (37%) | 50 van 135 (37%) |
| 30 min | 47 van 207 (23%) | 22 van 98 (22%) | 31 van 135 (23%) |
| 60 min | 21 van 207 (10%) | 13 van 98 (13%) | 13 van 135 (10%) |

## Wat zou het opleveren over 3 maanden? (GOK, doorgetrokken uit de metingen)

Gemeten over ±26.1 uur (GEZIEN), doorgetrokken naar 90 dagen (GOK: aanname dat de week die we maten gewoon is).

| Beurzen | Inleg | Model | Kansen per uur | Per kans (mediaan) | 3 maanden |
|---|---|---|---|---|---|
| Alleen MiCA | €2.000,00 | bovengrens: elke kans, geld overal tegelijk | 3.76 | €2,19 | €17.740,79 |
| Alleen MiCA | €2.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 1.99 | €2,53 | €33.508,55 |
| Alleen MiCA | €5.000,00 | bovengrens: elke kans, geld overal tegelijk | 3.76 | €2,41 | €19.567,53 |
| Alleen MiCA | €5.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 1.99 | €3,01 | €50.111,94 |
| Alle (met grijs) | €2.000,00 | bovengrens: elke kans, geld overal tegelijk | 7.94 | €1,58 | €27.153,74 |
| Alle (met grijs) | €2.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 1.99 | €2,53 | €33.508,55 |
| Alle (met grijs) | €5.000,00 | bovengrens: elke kans, geld overal tegelijk | 7.94 | €1,78 | €30.477,47 |
| Alle (met grijs) | €5.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 1.99 | €3,01 | €50.111,94 |

Bovengrens: elke kans met de helft van de inleg aan elke kant, alsof het geld op alle beurzen tegelijk staat (kan in het echt niet). Beste beurspaar: het paar is **achteraf** gekozen uit de metingen (vooraf kiezen levert minder op), en het model neemt aan dat je van elke munt al voorraad op de verkoopbeurs hebt.

Waarom dit te rooskleurig is (GOK): elke kans wordt maar één keer geteld met het mediane boek, maar andere bots pakken hem ook; de munt die je als voorraad aanhoudt kan dalen; na een paar kansen moet de voorraad terug (opnamekosten en tijd); minimale opname- en ordergroottes tellen niet mee; en een kans die we 2 minuten zagen staan, staat er niet per se nog als jouw order binnenkomt. Waarom het te somber kan zijn: niet alle kandidaten zijn gecontroleerd, en met voorraad op beide beurzen kun je dezelfde kans vaker pakken als het boek zich aanvult; dat telt hier niet mee.

## Wat houd je echt over? Voorraad op twee beurzen (simulatie)

Per beurspaar: geld en munten op beide beurzen, elke echte kans uitgevoerd tegen het boek zoals gemeten (niet meer dan de ruimte op het boek en niet meer dan de voorraad op die beurs), terugschuiven als een kant leeg dreigt te raken (met opnamekosten en tijd onderweg), en het koerseffect van de aangehouden munten apart. Netto = bruto min kosten terugschuiven plus koerseffect. **Gemeten** (GEZIEN): de kansen, het boek en de koersen; **de rest is een rekenmodel** (GOK, aannames onder de tabel). Geen advies.

**Met €150: netto €0,89 per dag op bitstamp - kraken (koerseffect erbovenop €-2,80), €0,07 per dag op bitvavo - kraken (koerseffect erbovenop €-1,59), €0,24 per dag op gate - kucoin (koerseffect erbovenop €0,63) (GOK: netto handel, rekenmodel op ±13.0 uur meting per dag, alleen MiCA).** "Per dag" is hier gemiddeld over 2 gemeten dagen achter elkaar; de eerste begint met een gelijk verdeelde voorraad; aan het eind staat de voorraad scheef, dus een volgende dag levert waarschijnlijk minder op, tenzij kansen de andere kant op hem terugbrengen (GOK).

### Alleen MiCA-beurzen (alle paren met echte kansen)

| Beurspaar | Inleg | Dag | Gemeten | Kansen | Gemist (geen voorraad) | Kleiner door voorraad | Bruto winst | Kosten terugschuiven | **Netto handel (bruto min kosten)** | Rendement handel | Koerseffect voorraad | Netto met koerseffect | Rendement met koerseffect |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| bitstamp - kraken | €100,00 | 2026-11-19 | 14.9 u | 2 | 1 | 1 | €1,18 | €0,00 (0x) | **€1,18** | 1.18% | €0,63 | €1,81 | 1.81% |
| bitstamp - kraken | €100,00 | 2026-11-20 | 11.2 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-4,35 | €-4,35 | -4.35% |
| bitstamp - kraken | €150,00 | 2026-11-19 | 14.9 u | 2 | 1 | 1 | €1,78 | €0,00 (0x) | **€1,78** | 1.18% | €0,94 | €2,72 | 1.81% |
| bitstamp - kraken | €150,00 | 2026-11-20 | 11.2 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-6,53 | €-6,53 | -4.35% |
| bitstamp - kraken | €200,00 | 2026-11-19 | 14.9 u | 2 | 1 | 1 | €2,37 | €0,00 (0x) | **€2,37** | 1.18% | €1,25 | €3,62 | 1.81% |
| bitstamp - kraken | €200,00 | 2026-11-20 | 11.2 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-8,71 | €-8,71 | -4.35% |
| bitstamp - kraken | €2.000,00 | 2026-11-19 | 14.9 u | 2 | 1 | 0 | €11,71 | €0,00 (0x) | **€11,71** | 0.59% | €12,53 | €24,24 | 1.21% |
| bitstamp - kraken | €2.000,00 | 2026-11-20 | 11.2 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-87,08 | €-87,08 | -4.35% |
| bitstamp - kraken | €5.000,00 | 2026-11-19 | 14.9 u | 2 | 1 | 0 | €11,71 | €0,00 (0x) | **€11,71** | 0.23% | €31,33 | €43,04 | 0.86% |
| bitstamp - kraken | €5.000,00 | 2026-11-20 | 11.2 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-217,70 | €-217,70 | -4.35% |
| bitvavo - kraken | €100,00 | 2026-11-19 | 14.9 u | 43 | 43 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,53 | €-0,53 | -0.53% |
| bitvavo - kraken | €100,00 | 2026-11-20 | 11.2 u | 9 | 9 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,58 | €-1,58 | -1.58% |
| bitvavo - kraken | €150,00 | 2026-11-19 | 14.9 u | 43 | 37 | 6 | €0,14 | €0,00 (0x) | **€0,14** | 0.09% | €-0,80 | €-0,66 | -0.44% |
| bitvavo - kraken | €150,00 | 2026-11-20 | 11.2 u | 9 | 9 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,37 | €-2,37 | -1.58% |
| bitvavo - kraken | €200,00 | 2026-11-19 | 14.9 u | 43 | 37 | 6 | €0,19 | €0,00 (0x) | **€0,19** | 0.09% | €-1,07 | €-0,88 | -0.44% |
| bitvavo - kraken | €200,00 | 2026-11-20 | 11.2 u | 9 | 9 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,16 | €-3,16 | -1.58% |
| bitvavo - kraken | €2.000,00 | 2026-11-19 | 14.9 u | 43 | 26 | 17 | €16,97 | €7,68 (18x) | **€9,29** | 0.46% | €-10,61 | €-1,32 | -0.07% |
| bitvavo - kraken | €2.000,00 | 2026-11-20 | 11.2 u | 9 | 8 | 1 | €2,60 | €0,32 (1x) | **€2,27** | 0.11% | €-31,39 | €-29,12 | -1.46% |
| bitvavo - kraken | €5.000,00 | 2026-11-19 | 14.9 u | 43 | 18 | 25 | €36,95 | €17,20 (27x) | **€19,75** | 0.40% | €-26,61 | €-6,86 | -0.14% |
| bitvavo - kraken | €5.000,00 | 2026-11-20 | 11.2 u | 9 | 2 | 7 | €9,71 | €8,22 (9x) | **€1,50** | 0.03% | €-78,57 | €-77,07 | -1.54% |
| gate - kucoin | €100,00 | 2026-11-19 | 14.9 u | 25 | 25 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,07 | €-0,07 | -0.07% |
| gate - kucoin | €100,00 | 2026-11-20 | 11.2 u | 19 | 18 | 1 | €0,09 | €0,00 (1x) | **€0,09** | 0.09% | €0,92 | €1,01 | 1.01% |
| gate - kucoin | €150,00 | 2026-11-19 | 14.9 u | 25 | 22 | 3 | €0,05 | €0,00 (0x) | **€0,05** | 0.04% | €-0,11 | €-0,06 | -0.04% |
| gate - kucoin | €150,00 | 2026-11-20 | 11.2 u | 19 | 15 | 4 | €0,43 | €0,02 (2x) | **€0,42** | 0.28% | €1,38 | €1,80 | 1.20% |
| gate - kucoin | €200,00 | 2026-11-19 | 14.9 u | 25 | 17 | 8 | €0,25 | €0,00 (0x) | **€0,25** | 0.12% | €-0,15 | €0,10 | 0.05% |
| gate - kucoin | €200,00 | 2026-11-20 | 11.2 u | 19 | 9 | 10 | €0,95 | €0,02 (2x) | **€0,93** | 0.47% | €1,84 | €2,77 | 1.39% |
| gate - kucoin | €2.000,00 | 2026-11-19 | 14.9 u | 25 | 6 | 19 | €5,27 | €3,91 (17x) | **€1,36** | 0.07% | €-1,50 | €-0,13 | -0.01% |
| gate - kucoin | €2.000,00 | 2026-11-20 | 11.2 u | 19 | 4 | 15 | €10,40 | €1,18 (9x) | **€9,21** | 0.46% | €18,54 | €27,75 | 1.39% |
| gate - kucoin | €5.000,00 | 2026-11-19 | 14.9 u | 25 | 6 | 19 | €12,99 | €4,84 (19x) | **€8,15** | 0.16% | €-3,69 | €4,46 | 0.09% |
| gate - kucoin | €5.000,00 | 2026-11-20 | 11.2 u | 19 | 3 | 16 | €24,51 | €5,09 (15x) | **€19,42** | 0.39% | €46,50 | €65,92 | 1.32% |

- bitstamp - kraken, €100,00: munten SKY; bruto zonder voorraadgrens zou €22,30 zijn, met voorraad €1,18 (GEZIEN boek, GOK model).
- bitstamp - kraken, €150,00: munten SKY; bruto zonder voorraadgrens zou €21,71 zijn, met voorraad €1,78 (GEZIEN boek, GOK model).
- bitstamp - kraken, €200,00: munten SKY; bruto zonder voorraadgrens zou €21,12 zijn, met voorraad €2,37 (GEZIEN boek, GOK model).
- bitstamp - kraken, €2.000,00: munten SKY; bruto zonder voorraadgrens zou €11,71 zijn, met voorraad €11,71 (GEZIEN boek, GOK model).
- bitstamp - kraken, €5.000,00: munten SKY; bruto zonder voorraadgrens zou €11,71 zijn, met voorraad €11,71 (GEZIEN boek, GOK model).
- bitvavo - kraken, €100,00: munten AVA, DYM, GMT, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €809,78 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitvavo - kraken, €150,00: munten AVA, DYM, GMT, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €809,38 zijn, met voorraad €0,14 (GEZIEN boek, GOK model).
- bitvavo - kraken, €200,00: munten AVA, DYM, GMT, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €809,24 zijn, met voorraad €0,19 (GEZIEN boek, GOK model).
- bitvavo - kraken, €2.000,00: munten AVA, DYM, GMT, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €785,92 zijn, met voorraad €19,57 (GEZIEN boek, GOK model).
- bitvavo - kraken, €5.000,00: munten AVA, DYM, GMT, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €747,25 zijn, met voorraad €46,66 (GEZIEN boek, GOK model).
- gate - kucoin, €100,00: munten ALKIMI, AVAIL, CHR, CYBER, ERG, FTT, IKA, IR, KYO, LUNC, NIM, RARI, USTC, VERONA; bruto zonder voorraadgrens zou €160,41 zijn, met voorraad €0,09 (GEZIEN boek, GOK model).
- gate - kucoin, €150,00: munten ALKIMI, AVAIL, CHR, CYBER, ERG, FTT, IKA, IR, KYO, LUNC, NIM, RARI, USTC, VERONA; bruto zonder voorraadgrens zou €160,23 zijn, met voorraad €0,49 (GEZIEN boek, GOK model).
- gate - kucoin, €200,00: munten ALKIMI, AVAIL, CHR, CYBER, ERG, FTT, IKA, IR, KYO, LUNC, NIM, RARI, USTC, VERONA; bruto zonder voorraadgrens zou €160,13 zijn, met voorraad €1,20 (GEZIEN boek, GOK model).
- gate - kucoin, €2.000,00: munten ALKIMI, AVAIL, CHR, CYBER, ERG, FTT, IKA, IR, KYO, LUNC, NIM, RARI, USTC, VERONA; bruto zonder voorraadgrens zou €156,28 zijn, met voorraad €15,66 (GEZIEN boek, GOK model).
- gate - kucoin, €5.000,00: munten ALKIMI, AVAIL, CHR, CYBER, ERG, FTT, IKA, IR, KYO, LUNC, NIM, RARI, USTC, VERONA; bruto zonder voorraadgrens zou €150,64 zijn, met voorraad €37,51 (GEZIEN boek, GOK model).

### Met minstens één grijze beurs (de 5 paren met de meeste bruto winst)

| Beurspaar | Inleg | Dag | Gemeten | Kansen | Gemist (geen voorraad) | Kleiner door voorraad | Bruto winst | Kosten terugschuiven | **Netto handel (bruto min kosten)** | Rendement handel | Koerseffect voorraad | Netto met koerseffect | Rendement met koerseffect |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| htx - xt | €100,00 | 2026-11-19 | 14.9 u | 18 | 18 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,61 | €-0,61 | -0.61% |
| htx - xt | €100,00 | 2026-11-20 | 11.2 u | 8 | 8 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,97 | €-0,97 | -0.97% |
| htx - xt | €150,00 | 2026-11-19 | 14.9 u | 18 | 18 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,91 | €-0,91 | -0.61% |
| htx - xt | €150,00 | 2026-11-20 | 11.2 u | 8 | 8 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,45 | €-1,45 | -0.97% |
| htx - xt | €200,00 | 2026-11-19 | 14.9 u | 18 | 18 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,22 | €-1,22 | -0.61% |
| htx - xt | €200,00 | 2026-11-20 | 11.2 u | 8 | 8 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,94 | €-1,94 | -0.97% |
| htx - xt | €2.000,00 | 2026-11-19 | 14.9 u | 18 | 5 | 13 | €9,30 | €5,27 (12x) | **€4,02** | 0.20% | €-12,20 | €-8,18 | -0.41% |
| htx - xt | €2.000,00 | 2026-11-20 | 11.2 u | 8 | 1 | 7 | €14,98 | €1,56 (4x) | **€13,42** | 0.67% | €-19,00 | €-5,58 | -0.28% |
| htx - xt | €5.000,00 | 2026-11-19 | 14.9 u | 18 | 5 | 12 | €19,47 | €6,64 (13x) | **€12,83** | 0.26% | €-30,43 | €-17,60 | -0.35% |
| htx - xt | €5.000,00 | 2026-11-20 | 11.2 u | 8 | 0 | 8 | €36,62 | €3,43 (6x) | **€33,19** | 0.66% | €-48,01 | €-14,82 | -0.30% |
| bitget - xt | €100,00 | 2026-11-19 | 14.9 u | 13 | 13 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €2,07 | €2,07 | 2.07% |
| bitget - xt | €100,00 | 2026-11-20 | 11.2 u | 4 | 4 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,79 | €-0,79 | -0.79% |
| bitget - xt | €150,00 | 2026-11-19 | 14.9 u | 13 | 13 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €3,11 | €3,11 | 2.07% |
| bitget - xt | €150,00 | 2026-11-20 | 11.2 u | 4 | 4 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,18 | €-1,18 | -0.79% |
| bitget - xt | €200,00 | 2026-11-19 | 14.9 u | 13 | 9 | 4 | €0,50 | €0,01 (3x) | **€0,50** | 0.25% | €4,15 | €4,64 | 2.32% |
| bitget - xt | €200,00 | 2026-11-20 | 11.2 u | 4 | 4 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,57 | €-1,57 | -0.78% |
| bitget - xt | €2.000,00 | 2026-11-19 | 14.9 u | 13 | 4 | 9 | €9,96 | €1,96 (11x) | **€8,00** | 0.40% | €41,46 | €49,46 | 2.47% |
| bitget - xt | €2.000,00 | 2026-11-20 | 11.2 u | 4 | 0 | 4 | €4,66 | €2,05 (5x) | **€2,61** | 0.13% | €-15,72 | €-13,11 | -0.66% |
| bitget - xt | €5.000,00 | 2026-11-19 | 14.9 u | 13 | 4 | 8 | €19,47 | €1,85 (10x) | **€17,62** | 0.35% | €103,65 | €121,27 | 2.43% |
| bitget - xt | €5.000,00 | 2026-11-20 | 11.2 u | 4 | 0 | 4 | €9,88 | €2,05 (5x) | **€7,82** | 0.16% | €-39,28 | €-31,46 | -0.63% |
| kucoin - xt | €100,00 | 2026-11-19 | 14.9 u | 13 | 13 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,07 | €0,07 | 0.07% |
| kucoin - xt | €100,00 | 2026-11-20 | 11.2 u | 2 | 2 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,22 | €0,22 | 0.22% |
| kucoin - xt | €150,00 | 2026-11-19 | 14.9 u | 13 | 13 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,11 | €0,11 | 0.07% |
| kucoin - xt | €150,00 | 2026-11-20 | 11.2 u | 2 | 2 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,33 | €0,33 | 0.22% |
| kucoin - xt | €200,00 | 2026-11-19 | 14.9 u | 13 | 10 | 3 | €0,35 | €0,00 (0x) | **€0,35** | 0.18% | €0,15 | €0,50 | 0.25% |
| kucoin - xt | €200,00 | 2026-11-20 | 11.2 u | 2 | 1 | 1 | €0,22 | €0,00 (0x) | **€0,22** | 0.11% | €0,44 | €0,66 | 0.33% |
| kucoin - xt | €2.000,00 | 2026-11-19 | 14.9 u | 13 | 3 | 10 | €13,20 | €5,51 (11x) | **€7,69** | 0.38% | €1,50 | €9,19 | 0.46% |
| kucoin - xt | €2.000,00 | 2026-11-20 | 11.2 u | 2 | 0 | 2 | €4,03 | €2,08 (3x) | **€1,95** | 0.10% | €4,53 | €6,48 | 0.32% |
| kucoin - xt | €5.000,00 | 2026-11-19 | 14.9 u | 13 | 3 | 8 | €28,07 | €5,51 (11x) | **€22,57** | 0.45% | €3,73 | €26,30 | 0.53% |
| kucoin - xt | €5.000,00 | 2026-11-20 | 11.2 u | 2 | 0 | 1 | €11,88 | €2,08 (3x) | **€9,80** | 0.20% | €11,15 | €20,96 | 0.42% |
| gate - htx | €100,00 | 2026-11-19 | 14.9 u | 19 | 19 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,78 | €-0,78 | -0.78% |
| gate - htx | €100,00 | 2026-11-20 | 11.2 u | 15 | 15 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,78 | €-1,78 | -1.78% |
| gate - htx | €150,00 | 2026-11-19 | 14.9 u | 19 | 19 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,17 | €-1,17 | -0.78% |
| gate - htx | €150,00 | 2026-11-20 | 11.2 u | 15 | 15 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,66 | €-2,66 | -1.78% |
| gate - htx | €200,00 | 2026-11-19 | 14.9 u | 19 | 19 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,56 | €-1,56 | -0.78% |
| gate - htx | €200,00 | 2026-11-20 | 11.2 u | 15 | 15 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,55 | €-3,55 | -1.78% |
| gate - htx | €2.000,00 | 2026-11-19 | 14.9 u | 19 | 7 | 12 | €5,99 | €3,58 (10x) | **€2,40** | 0.12% | €-15,69 | €-13,28 | -0.66% |
| gate - htx | €2.000,00 | 2026-11-20 | 11.2 u | 15 | 2 | 13 | €10,51 | €2,41 (10x) | **€8,09** | 0.40% | €-35,21 | €-27,12 | -1.36% |
| gate - htx | €5.000,00 | 2026-11-19 | 14.9 u | 19 | 6 | 11 | €14,83 | €5,58 (13x) | **€9,25** | 0.19% | €-39,16 | €-29,91 | -0.60% |
| gate - htx | €5.000,00 | 2026-11-20 | 11.2 u | 15 | 2 | 13 | €26,07 | €3,75 (12x) | **€22,32** | 0.45% | €-88,48 | €-66,17 | -1.32% |
| htx - kucoin | €100,00 | 2026-11-19 | 14.9 u | 16 | 16 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,76 | €-2,76 | -2.76% |
| htx - kucoin | €100,00 | 2026-11-20 | 11.2 u | 14 | 14 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,58 | €-1,58 | -1.58% |
| htx - kucoin | €150,00 | 2026-11-19 | 14.9 u | 16 | 16 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-4,14 | €-4,14 | -2.76% |
| htx - kucoin | €150,00 | 2026-11-20 | 11.2 u | 14 | 14 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,36 | €-2,36 | -1.58% |
| htx - kucoin | €200,00 | 2026-11-19 | 14.9 u | 16 | 16 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-5,51 | €-5,51 | -2.76% |
| htx - kucoin | €200,00 | 2026-11-20 | 11.2 u | 14 | 14 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,15 | €-3,15 | -1.58% |
| htx - kucoin | €2.000,00 | 2026-11-19 | 14.9 u | 16 | 7 | 9 | €3,96 | €1,18 (6x) | **€2,78** | 0.14% | €-55,07 | €-52,29 | -2.61% |
| htx - kucoin | €2.000,00 | 2026-11-20 | 11.2 u | 14 | 4 | 10 | €8,71 | €1,20 (6x) | **€7,51** | 0.38% | €-31,53 | €-24,01 | -1.20% |
| htx - kucoin | €5.000,00 | 2026-11-19 | 14.9 u | 16 | 3 | 13 | €12,30 | €4,43 (13x) | **€7,87** | 0.16% | €-137,77 | €-129,90 | -2.60% |
| htx - kucoin | €5.000,00 | 2026-11-20 | 11.2 u | 14 | 0 | 14 | €24,74 | €4,08 (12x) | **€20,66** | 0.41% | €-78,75 | €-58,09 | -1.16% |

- htx - xt, €100,00: munten BSV, CBK, LUNC, MEME, SEI, XCH, XDC; bruto zonder voorraadgrens zou €169,58 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - xt, €150,00: munten BSV, CBK, LUNC, MEME, SEI, XCH, XDC; bruto zonder voorraadgrens zou €169,58 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - xt, €200,00: munten BSV, CBK, LUNC, MEME, SEI, XCH, XDC; bruto zonder voorraadgrens zou €169,58 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - xt, €2.000,00: munten BSV, CBK, LUNC, MEME, SEI, XCH, XDC; bruto zonder voorraadgrens zou €167,29 zijn, met voorraad €24,28 (GEZIEN boek, GOK model).
- htx - xt, €5.000,00: munten BSV, CBK, LUNC, MEME, SEI, XCH, XDC; bruto zonder voorraadgrens zou €165,01 zijn, met voorraad €56,10 (GEZIEN boek, GOK model).
- bitget - xt, €100,00: munten ENSO, KOR, KUB, LUNC, YB; bruto zonder voorraadgrens zou €696,80 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - xt, €150,00: munten ENSO, KOR, KUB, LUNC, YB; bruto zonder voorraadgrens zou €696,80 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - xt, €200,00: munten ENSO, KOR, KUB, LUNC, YB; bruto zonder voorraadgrens zou €696,38 zijn, met voorraad €0,50 (GEZIEN boek, GOK model).
- bitget - xt, €2.000,00: munten ENSO, KOR, KUB, LUNC, YB; bruto zonder voorraadgrens zou €691,41 zijn, met voorraad €14,62 (GEZIEN boek, GOK model).
- bitget - xt, €5.000,00: munten ENSO, KOR, KUB, LUNC, YB; bruto zonder voorraadgrens zou €684,82 zijn, met voorraad €29,35 (GEZIEN boek, GOK model).
- kucoin - xt, €100,00: munten DAG, ENSO, FIGHT, LUNC; bruto zonder voorraadgrens zou €617,52 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- kucoin - xt, €150,00: munten DAG, ENSO, FIGHT, LUNC; bruto zonder voorraadgrens zou €617,52 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- kucoin - xt, €200,00: munten DAG, ENSO, FIGHT, LUNC; bruto zonder voorraadgrens zou €617,52 zijn, met voorraad €0,58 (GEZIEN boek, GOK model).
- kucoin - xt, €2.000,00: munten DAG, ENSO, FIGHT, LUNC; bruto zonder voorraadgrens zou €613,21 zijn, met voorraad €17,23 (GEZIEN boek, GOK model).
- kucoin - xt, €5.000,00: munten DAG, ENSO, FIGHT, LUNC; bruto zonder voorraadgrens zou €606,95 zijn, met voorraad €39,95 (GEZIEN boek, GOK model).
- gate - htx, €100,00: munten BSV, CBK, CRTS, KAS, LAT, LUNC, MEME, MOVR, SEI, WARD, WLD; bruto zonder voorraadgrens zou €136,87 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- gate - htx, €150,00: munten BSV, CBK, CRTS, KAS, LAT, LUNC, MEME, MOVR, SEI, WARD, WLD; bruto zonder voorraadgrens zou €136,87 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- gate - htx, €200,00: munten BSV, CBK, CRTS, KAS, LAT, LUNC, MEME, MOVR, SEI, WARD, WLD; bruto zonder voorraadgrens zou €136,87 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- gate - htx, €2.000,00: munten BSV, CBK, CRTS, KAS, LAT, LUNC, MEME, MOVR, SEI, WARD, WLD; bruto zonder voorraadgrens zou €133,76 zijn, met voorraad €16,49 (GEZIEN boek, GOK model).
- gate - htx, €5.000,00: munten BSV, CBK, CRTS, KAS, LAT, LUNC, MEME, MOVR, SEI, WARD, WLD; bruto zonder voorraadgrens zou €129,43 zijn, met voorraad €40,90 (GEZIEN boek, GOK model).
- htx - kucoin, €100,00: munten BSV, CHIP, FET, LAT, LUNC, MEME, MOVR, ONE, SOMI, WAN, WARD, WLD, XCH, XEC; bruto zonder voorraadgrens zou €120,43 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - kucoin, €150,00: munten BSV, CHIP, FET, LAT, LUNC, MEME, MOVR, ONE, SOMI, WAN, WARD, WLD, XCH, XEC; bruto zonder voorraadgrens zou €120,43 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - kucoin, €200,00: munten BSV, CHIP, FET, LAT, LUNC, MEME, MOVR, ONE, SOMI, WAN, WARD, WLD, XCH, XEC; bruto zonder voorraadgrens zou €120,43 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - kucoin, €2.000,00: munten BSV, CHIP, FET, LAT, LUNC, MEME, MOVR, ONE, SOMI, WAN, WARD, WLD, XCH, XEC; bruto zonder voorraadgrens zou €119,49 zijn, met voorraad €12,67 (GEZIEN boek, GOK model).
- htx - kucoin, €5.000,00: munten BSV, CHIP, FET, LAT, LUNC, MEME, MOVR, ONE, SOMI, WAN, WARD, WLD, XCH, XEC; bruto zonder voorraadgrens zou €118,09 zijn, met voorraad €37,04 (GEZIEN boek, GOK model).

### Andere keuzes bij bitvavo - kraken (netto handel, alle dagen samen; GOK)

| Keuze | Inleg | Kansen | Gemist | Bruto winst | Kosten terugschuiven | Netto handel |
|---|---|---|---|---|---|---|
| standaard (schuifdrempel 25%, kostengrens 1%) | €150,00 | 52 | 46 | €0,14 | €0,00 | **€0,14** |
| standaard (schuifdrempel 25%, kostengrens 1%) | €2.000,00 | 52 | 34 | €19,57 | €8,00 | **€11,57** |
| schuifdrempel 10% | €150,00 | 52 | 46 | €0,14 | €0,00 | **€0,14** |
| schuifdrempel 10% | €2.000,00 | 52 | 37 | €15,70 | €6,08 | **€9,62** |
| schuifdrempel 40% | €150,00 | 52 | 46 | €0,14 | €0,00 | **€0,14** |
| schuifdrempel 40% | €2.000,00 | 52 | 34 | €16,76 | €8,68 | **€8,08** |
| kostengrens 2% (achteraf vergeleken) | €150,00 | 52 | 46 | €0,14 | €0,00 | **€0,14** |
| kostengrens 2% (achteraf vergeleken) | €2.000,00 | 52 | 21 | €20,75 | €24,41 | **€-3,66** |
| kostengrens 5% (achteraf vergeleken) | €150,00 | 52 | 43 | €0,18 | €2,48 | **€-2,31** |
| kostengrens 5% (achteraf vergeleken) | €2.000,00 | 52 | 21 | €20,75 | €24,41 | **€-3,66** |
| alleen MERL en GMT (meer voorraad per munt, achteraf gekozen) | €150,00 | 37 | 35 | €0,19 | €0,00 | **€0,19** |
| alleen MERL en GMT (meer voorraad per munt, achteraf gekozen) | €2.000,00 | 37 | 17 | €37,90 | €22,06 | **€15,84** |

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

- Opnamekosten bij de echte kansen: 90 van een netwerk dat aan beide kanten open is, 88 van de beurs zelf (laagste open netwerk), 29 geschat uit wat andere beurzen voor die munt vragen (GOK). Onbekende opnamekosten tellen niet als echte kans.
- Netwerk: KuCoin, Gate, Bitget, HTX, XT, Bitstamp, Bitvavo en Poloniex geven hun netwerken per munt. Als beide beurzen dat doen en de namen te koppelen zijn, moet er een netwerk zijn dat aan beide kanten open is. Anders is het netwerk "niet te koppelen" en telt de kans mee (staat apart in de trechter).
- De duur is gemeten in stappen van ±20 seconden; een kans kan een paar rondes eerder begonnen zijn dan we zagen.
- Takerkosten: uit de API waar die ze per paar geeft, anders het standaardtarief uit de README (deels GOK).
- Laatste run: 15 beurzen antwoordden, 2288 munt-quote-paren op minstens twee beurzen (GEZIEN).
