# Rapport koersverschil-scanner

Gemaakt 2026-11-20 09:37 UTC uit 18 runs, samen ±24.0 uur gemeten (GEZIEN).
Echte kans = winst na alle kosten (opnamekosten bekend), opnemen en storten open (en een netwerk dat aan beide kanten open is, als de beurzen dat geven), minstens €100,00 op het boek, minstens 2 minuten blijven staan, geen andere munt met dezelfde naam.
**Vergund** = beide beurzen hebben een MiCA-vergunning (ESMA-register), vaak via een EU-dochter die minder munten kan hebben dan de wereldwijde API die we meten (GOK). **Grijs** = minstens één beurs zonder vergunning (MEXC, Bitget, HTX, Poloniex, XT, Bitfinex, Binance). Zie README.md.
**Kraken-tarief:** Kraken rekent 0,80% taker op munt tegen EUR, USD, USDT of USDC (GEZIEN, kraken.com/pro/fees, laagste trede); de scanner rekende tot 19 nov met 0,40%. 399 opgeslagen kansen met Kraken uit die runs zijn hier **opnieuw doorgerekend met 0,80%** (GOK-benadering: 0,40% van de inzet aan de Kraken-kant extra op elk gemeten punt van het boek; het boek zelf is niet bewaard). 233 houden daarna nog winst op het boek. Dat ze met hogere kosten ook korter bleven staan, telt niet mee (dus eerder te gunstig).

## Hoeveel wordt er gecontroleerd? (GEZIEN, stand.jsonl)

Per ronde (mediaan over 288 metingen): 1103 kandidaten (verschil op de ticker groter dan de takerkosten), 120 met het orderboek gecontroleerd, 2 nog nooit gecontroleerd (0%).
Bijna alle kandidaten komen aan de beurt; de aantallen hieronder missen weinig.

## Trechter (GEZIEN, eigen metingen)

| Stap | Alle beurzen | Alleen MiCA-beurzen | Met minstens één grijze beurs |
|---|---|---|---|
| Verschillen met winst op het boek na alle kosten | 20570 | 3042 | 17528 |
| ...waarvan opnemen of storten dicht | 4651 | 468 | 4183 |
| ...waarvan status onbekend (beurs geeft het niet openbaar) | 11992 | 2150 | 9842 |
| Opnemen en storten open | 3927 | 424 | 3503 |
| ...en geen netwerk dat aan beide kanten open is: valt af | 106 | 3 | 103 |
| ...en opnamekosten onbekend: valt af | 0 | 0 | 0 |
| ...en minstens €100,00 op het boek | 1097 | 219 | 878 |
| ...en minstens 2 minuten blijven staan | 342 | 107 | 235 |
| ...en geen andere munt met dezelfde naam | 310 | 94 | 216 |
|    ...waarvan contractadres bekend en gelijk | 33 | 12 | 21 |
|    ...waarvan contractadres onbekend (telt mee, kan een andere munt zijn) | 277 | 82 | 195 |
|    ...waarvan netwerk gekoppeld en open | 195 | 38 | 157 |
|    ...waarvan netwerk niet te koppelen (telt mee) | 115 | 56 | 59 |
| **Echte kansen** (zelfde munt overlappend in de tijd samengevoegd, beste beurspaar telt) | 192 | 94 | 124 |
| Ter vergelijking: zelfde eisen, maar opnamestatus onbekend (niet meegeteld) | 715 | 173 | 611 |

## Echte kansen per dag (GEZIEN)

| Dag | Echt, alleen MiCA | Echt, met grijs | Mediane winst per kans bij €500 (MiCA / grijs) | Mediane duur |
|---|---|---|---|---|
| 2026-11-19 | 49 | 86 | €2,00 / €1,21 | 5.3 min |
| 2026-11-20 | 19 | 38 | €0,61 / €1,91 | 8.3 min |
| Totaal | 68 | 124 | €1,65 / €1,31 | 6.3 min |

## Beste munten (GEZIEN)

| | Soort | Kansen | Som winst bij €500 per kans |
|---|---|---|---|
| MERL-EUR | vergund | 17 | €201,75 |
| LUNC-USDT | grijs | 11 | €59,26 |
| MEME-USDT | grijs | 1 | €37,90 |
| USTC-USDT | grijs | 9 | €35,32 |
| SKY-USD | vergund | 2 | €21,52 |
| LAT-USDT | grijs | 3 | €17,59 |
| YB-USDT | grijs | 2 | €17,52 |
| GMT-EUR | vergund | 20 | €17,13 |
| WAN-USDT | grijs | 5 | €16,06 |
| VERONA-USDT | grijs | 10 | €14,14 |

## Beste beursparen (kopen op > verkopen op) (GEZIEN)

| | Soort | Kansen | Som winst bij €500 per kans |
|---|---|---|---|
| bitvavo > kraken | vergund | 52 | €244,42 |
| bitget > htx | grijs | 28 | €64,00 |
| kucoin > htx | grijs | 20 | €55,35 |
| kucoin > bitget | grijs | 13 | €40,21 |
| bitget > xt | grijs | 11 | €35,79 |
| bitget > gate | grijs | 7 | €24,32 |
| gate > kucoin | vergund | 10 | €23,17 |
| bitstamp > kraken | vergund | 2 | €21,52 |
| gate > xt | grijs | 2 | €19,11 |
| bitget > kucoin | grijs | 13 | €17,02 |

Beurzen die het vaakst meedoen (koop of verkoop): bitget (grijs) 78, kucoin 69, htx (grijs) 62, kraken 54, bitvavo 52, gate 36, xt (grijs) 24, poloniex (grijs) 7 (GEZIEN).

## Hoeveel kansen blijven staan terwijl je geld schuift? (GEZIEN, duur uit eigen metingen)

Wie geen voorraad op beide beurzen heeft, moet kopen, de munt opnemen, wachten tot hij binnen is en dan verkopen. Hoe lang dat duurt verschilt per munt en netwerk: een paar minuten (snelle ketens) tot een uur of meer (Bitcoin, beurzen die opnames met de hand keuren) (GOK, niet per munt gemeten).

| Overmaaktijd | Alle beurzen | Alleen MiCA-beurzen | Met minstens één grijze beurs |
|---|---|---|---|
| 5 min | 118 van 192 (61%) | 56 van 94 (60%) | 74 van 124 (60%) |
| 10 min | 73 van 192 (38%) | 35 van 94 (37%) | 47 van 124 (38%) |
| 30 min | 44 van 192 (23%) | 21 van 94 (22%) | 29 van 124 (23%) |
| 60 min | 20 van 192 (10%) | 12 van 94 (13%) | 13 van 124 (10%) |

## Wat zou het opleveren over 3 maanden? (GOK, doorgetrokken uit de metingen)

Gemeten over ±24.0 uur (GEZIEN), doorgetrokken naar 90 dagen (GOK: aanname dat de week die we maten gewoon is).

| Beurzen | Inleg | Model | Kansen per uur | Per kans (mediaan) | 3 maanden |
|---|---|---|---|---|---|
| Alleen MiCA | €2.000,00 | bovengrens: elke kans, geld overal tegelijk | 3.92 | €2,19 | €18.493,76 |
| Alleen MiCA | €2.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 2.17 | €2,53 | €36.417,18 |
| Alleen MiCA | €5.000,00 | bovengrens: elke kans, geld overal tegelijk | 3.92 | €2,41 | €20.398,04 |
| Alleen MiCA | €5.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 2.17 | €3,01 | €54.461,78 |
| Alle (met grijs) | €2.000,00 | bovengrens: elke kans, geld overal tegelijk | 8.00 | €1,60 | €27.574,47 |
| Alle (met grijs) | €2.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 2.17 | €2,53 | €36.417,18 |
| Alle (met grijs) | €5.000,00 | bovengrens: elke kans, geld overal tegelijk | 8.00 | €1,87 | €32.238,18 |
| Alle (met grijs) | €5.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 2.17 | €3,01 | €54.461,78 |

Bovengrens: elke kans met de helft van de inleg aan elke kant, alsof het geld op alle beurzen tegelijk staat (kan in het echt niet). Beste beurspaar: het paar is **achteraf** gekozen uit de metingen (vooraf kiezen levert minder op), en het model neemt aan dat je van elke munt al voorraad op de verkoopbeurs hebt.

Waarom dit te rooskleurig is (GOK): elke kans wordt maar één keer geteld met het mediane boek, maar andere bots pakken hem ook; de munt die je als voorraad aanhoudt kan dalen; na een paar kansen moet de voorraad terug (opnamekosten en tijd); minimale opname- en ordergroottes tellen niet mee; en een kans die we 2 minuten zagen staan, staat er niet per se nog als jouw order binnenkomt. Waarom het te somber kan zijn: niet alle kandidaten zijn gecontroleerd, en met voorraad op beide beurzen kun je dezelfde kans vaker pakken als het boek zich aanvult; dat telt hier niet mee.

## Wat houd je echt over? Voorraad op twee beurzen (simulatie)

Per beurspaar: geld en munten op beide beurzen, elke echte kans uitgevoerd tegen het boek zoals gemeten (niet meer dan de ruimte op het boek en niet meer dan de voorraad op die beurs), terugschuiven als een kant leeg dreigt te raken (met opnamekosten en tijd onderweg), en het koerseffect van de aangehouden munten apart. Netto = bruto min kosten terugschuiven plus koerseffect. **Gemeten** (GEZIEN): de kansen, het boek en de koersen; **de rest is een rekenmodel** (GOK, aannames onder de tabel). Geen advies.

**Met €150: netto €0,89 per dag op bitstamp - kraken (koerseffect erbovenop €-2,51), €0,07 per dag op bitvavo - kraken (koerseffect erbovenop €-1,38), €0,36 per dag op gate - kucoin (koerseffect erbovenop €1,65) (GOK: netto handel, rekenmodel op ±12.0 uur meting per dag, alleen MiCA).** "Per dag" is hier gemiddeld over 2 gemeten dagen achter elkaar; de eerste begint met een gelijk verdeelde voorraad; aan het eind staat de voorraad scheef, dus een volgende dag levert waarschijnlijk minder op, tenzij kansen de andere kant op hem terugbrengen (GOK).

### Alleen MiCA-beurzen (alle paren met echte kansen)

| Beurspaar | Inleg | Dag | Gemeten | Kansen | Gemist (geen voorraad) | Kleiner door voorraad | Bruto winst | Kosten terugschuiven | **Netto handel (bruto min kosten)** | Rendement handel | Koerseffect voorraad | Netto met koerseffect | Rendement met koerseffect |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| bitstamp - kraken | €100,00 | 2026-11-19 | 14.9 u | 2 | 1 | 1 | €1,18 | €0,00 (0x) | **€1,18** | 1.18% | €0,63 | €1,81 | 1.81% |
| bitstamp - kraken | €100,00 | 2026-11-20 | 9.1 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,98 | €-3,98 | -3.98% |
| bitstamp - kraken | €150,00 | 2026-11-19 | 14.9 u | 2 | 1 | 1 | €1,78 | €0,00 (0x) | **€1,78** | 1.18% | €0,94 | €2,72 | 1.81% |
| bitstamp - kraken | €150,00 | 2026-11-20 | 9.1 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-5,96 | €-5,96 | -3.98% |
| bitstamp - kraken | €200,00 | 2026-11-19 | 14.9 u | 2 | 1 | 1 | €2,37 | €0,00 (0x) | **€2,37** | 1.18% | €1,25 | €3,62 | 1.81% |
| bitstamp - kraken | €200,00 | 2026-11-20 | 9.1 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-7,95 | €-7,95 | -3.98% |
| bitstamp - kraken | €2.000,00 | 2026-11-19 | 14.9 u | 2 | 1 | 0 | €11,71 | €0,00 (0x) | **€11,71** | 0.59% | €12,53 | €24,24 | 1.21% |
| bitstamp - kraken | €2.000,00 | 2026-11-20 | 9.1 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-79,52 | €-79,52 | -3.98% |
| bitstamp - kraken | €5.000,00 | 2026-11-19 | 14.9 u | 2 | 1 | 0 | €11,71 | €0,00 (0x) | **€11,71** | 0.23% | €31,33 | €43,04 | 0.86% |
| bitstamp - kraken | €5.000,00 | 2026-11-20 | 9.1 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-198,79 | €-198,79 | -3.98% |
| bitvavo - kraken | €100,00 | 2026-11-19 | 14.9 u | 43 | 43 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,53 | €-0,53 | -0.53% |
| bitvavo - kraken | €100,00 | 2026-11-20 | 9.1 u | 9 | 9 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,30 | €-1,30 | -1.30% |
| bitvavo - kraken | €150,00 | 2026-11-19 | 14.9 u | 43 | 37 | 6 | €0,14 | €0,00 (0x) | **€0,14** | 0.09% | €-0,80 | €-0,66 | -0.44% |
| bitvavo - kraken | €150,00 | 2026-11-20 | 9.1 u | 9 | 9 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,95 | €-1,95 | -1.30% |
| bitvavo - kraken | €200,00 | 2026-11-19 | 14.9 u | 43 | 37 | 6 | €0,19 | €0,00 (0x) | **€0,19** | 0.09% | €-1,07 | €-0,88 | -0.44% |
| bitvavo - kraken | €200,00 | 2026-11-20 | 9.1 u | 9 | 9 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,60 | €-2,60 | -1.30% |
| bitvavo - kraken | €2.000,00 | 2026-11-19 | 14.9 u | 43 | 26 | 17 | €16,97 | €7,68 (18x) | **€9,29** | 0.46% | €-10,61 | €-1,32 | -0.07% |
| bitvavo - kraken | €2.000,00 | 2026-11-20 | 9.1 u | 9 | 8 | 1 | €2,60 | €0,32 (1x) | **€2,27** | 0.11% | €-25,82 | €-23,55 | -1.18% |
| bitvavo - kraken | €5.000,00 | 2026-11-19 | 14.9 u | 43 | 18 | 25 | €36,95 | €17,20 (27x) | **€19,75** | 0.40% | €-26,61 | €-6,86 | -0.14% |
| bitvavo - kraken | €5.000,00 | 2026-11-20 | 9.1 u | 9 | 2 | 7 | €9,71 | €8,22 (9x) | **€1,50** | 0.03% | €-64,71 | €-63,21 | -1.26% |
| gate - kucoin | €100,00 | 2026-11-19 | 14.9 u | 25 | 25 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,37 | €0,37 | 0.37% |
| gate - kucoin | €100,00 | 2026-11-20 | 9.1 u | 15 | 13 | 2 | €0,17 | €0,00 (1x) | **€0,17** | 0.17% | €1,83 | €2,01 | 2.01% |
| gate - kucoin | €150,00 | 2026-11-19 | 14.9 u | 25 | 19 | 6 | €0,16 | €0,00 (0x) | **€0,16** | 0.11% | €0,55 | €0,71 | 0.47% |
| gate - kucoin | €150,00 | 2026-11-20 | 9.1 u | 15 | 8 | 7 | €0,58 | €0,02 (2x) | **€0,56** | 0.37% | €2,75 | €3,31 | 2.21% |
| gate - kucoin | €200,00 | 2026-11-19 | 14.9 u | 25 | 17 | 8 | €0,27 | €0,00 (0x) | **€0,27** | 0.13% | €0,73 | €1,00 | 0.50% |
| gate - kucoin | €200,00 | 2026-11-20 | 9.1 u | 15 | 7 | 8 | €0,78 | €0,02 (2x) | **€0,77** | 0.38% | €3,67 | €4,44 | 2.22% |
| gate - kucoin | €2.000,00 | 2026-11-19 | 14.9 u | 25 | 6 | 19 | €5,68 | €4,83 (18x) | **€0,85** | 0.04% | €7,33 | €8,17 | 0.41% |
| gate - kucoin | €2.000,00 | 2026-11-20 | 9.1 u | 15 | 3 | 12 | €8,83 | €1,23 (8x) | **€7,60** | 0.38% | €36,82 | €44,42 | 2.22% |
| gate - kucoin | €5.000,00 | 2026-11-19 | 14.9 u | 25 | 6 | 19 | €13,97 | €5,76 (20x) | **€8,21** | 0.16% | €18,36 | €26,57 | 0.53% |
| gate - kucoin | €5.000,00 | 2026-11-20 | 9.1 u | 15 | 2 | 13 | €20,31 | €4,80 (13x) | **€15,51** | 0.31% | €92,02 | €107,53 | 2.15% |

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
- gate - kucoin, €100,00: munten ALKIMI, AVAIL, CHR, CYBER, ERG, FTT, IKA, IR, LUNC, NIM, RARI, USTC, VERONA; bruto zonder voorraadgrens zou €131,21 zijn, met voorraad €0,17 (GEZIEN boek, GOK model).
- gate - kucoin, €150,00: munten ALKIMI, AVAIL, CHR, CYBER, ERG, FTT, IKA, IR, LUNC, NIM, RARI, USTC, VERONA; bruto zonder voorraadgrens zou €131,18 zijn, met voorraad €0,74 (GEZIEN boek, GOK model).
- gate - kucoin, €200,00: munten ALKIMI, AVAIL, CHR, CYBER, ERG, FTT, IKA, IR, LUNC, NIM, RARI, USTC, VERONA; bruto zonder voorraadgrens zou €131,17 zijn, met voorraad €1,05 (GEZIEN boek, GOK model).
- gate - kucoin, €2.000,00: munten ALKIMI, AVAIL, CHR, CYBER, ERG, FTT, IKA, IR, LUNC, NIM, RARI, USTC, VERONA; bruto zonder voorraadgrens zou €129,32 zijn, met voorraad €14,50 (GEZIEN boek, GOK model).
- gate - kucoin, €5.000,00: munten ALKIMI, AVAIL, CHR, CYBER, ERG, FTT, IKA, IR, LUNC, NIM, RARI, USTC, VERONA; bruto zonder voorraadgrens zou €127,05 zijn, met voorraad €34,28 (GEZIEN boek, GOK model).

### Met minstens één grijze beurs (de 5 paren met de meeste bruto winst)

| Beurspaar | Inleg | Dag | Gemeten | Kansen | Gemist (geen voorraad) | Kleiner door voorraad | Bruto winst | Kosten terugschuiven | **Netto handel (bruto min kosten)** | Rendement handel | Koerseffect voorraad | Netto met koerseffect | Rendement met koerseffect |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| htx - xt | €100,00 | 2026-11-19 | 14.9 u | 18 | 18 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,61 | €-0,61 | -0.61% |
| htx - xt | €100,00 | 2026-11-20 | 9.1 u | 7 | 7 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,06 | €-1,06 | -1.06% |
| htx - xt | €150,00 | 2026-11-19 | 14.9 u | 18 | 18 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,91 | €-0,91 | -0.61% |
| htx - xt | €150,00 | 2026-11-20 | 9.1 u | 7 | 7 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,58 | €-1,58 | -1.06% |
| htx - xt | €200,00 | 2026-11-19 | 14.9 u | 18 | 18 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,22 | €-1,22 | -0.61% |
| htx - xt | €200,00 | 2026-11-20 | 9.1 u | 7 | 7 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,11 | €-2,11 | -1.06% |
| htx - xt | €2.000,00 | 2026-11-19 | 14.9 u | 18 | 5 | 13 | €9,30 | €5,27 (12x) | **€4,03** | 0.20% | €-12,20 | €-8,18 | -0.41% |
| htx - xt | €2.000,00 | 2026-11-20 | 9.1 u | 7 | 0 | 7 | €14,98 | €1,56 (4x) | **€13,42** | 0.67% | €-20,80 | €-7,38 | -0.37% |
| htx - xt | €5.000,00 | 2026-11-19 | 14.9 u | 18 | 5 | 12 | €19,47 | €6,64 (13x) | **€12,83** | 0.26% | €-30,43 | €-17,60 | -0.35% |
| htx - xt | €5.000,00 | 2026-11-20 | 9.1 u | 7 | 0 | 7 | €35,93 | €2,50 (5x) | **€33,43** | 0.67% | €-52,43 | €-19,00 | -0.38% |
| kucoin - xt | €100,00 | 2026-11-19 | 14.9 u | 13 | 13 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,15 | €-0,15 | -0.15% |
| kucoin - xt | €100,00 | 2026-11-20 | 9.1 u | 1 | 1 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,01 | €-1,01 | -1.01% |
| kucoin - xt | €150,00 | 2026-11-19 | 14.9 u | 13 | 10 | 3 | €0,35 | €0,00 (0x) | **€0,35** | 0.24% | €-0,22 | €0,13 | 0.09% |
| kucoin - xt | €150,00 | 2026-11-20 | 9.1 u | 1 | 1 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,52 | €-1,52 | -1.01% |
| kucoin - xt | €200,00 | 2026-11-19 | 14.9 u | 13 | 10 | 3 | €0,47 | €0,00 (0x) | **€0,47** | 0.24% | €-0,30 | €0,18 | 0.09% |
| kucoin - xt | €200,00 | 2026-11-20 | 9.1 u | 1 | 1 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,02 | €-2,02 | -1.01% |
| kucoin - xt | €2.000,00 | 2026-11-19 | 14.9 u | 13 | 3 | 10 | €16,57 | €6,42 (12x) | **€10,15** | 0.51% | €-2,95 | €7,21 | 0.36% |
| kucoin - xt | €2.000,00 | 2026-11-20 | 9.1 u | 1 | 0 | 1 | €1,83 | €0,35 (1x) | **€1,48** | 0.07% | €-20,10 | €-18,61 | -0.93% |
| kucoin - xt | €5.000,00 | 2026-11-19 | 14.9 u | 13 | 2 | 10 | €34,70 | €5,17 (10x) | **€29,54** | 0.59% | €-7,39 | €22,14 | 0.44% |
| kucoin - xt | €5.000,00 | 2026-11-20 | 9.1 u | 1 | 0 | 1 | €4,51 | €1,26 (2x) | **€3,25** | 0.07% | €-50,45 | €-47,19 | -0.94% |
| bitget - xt | €100,00 | 2026-11-19 | 14.9 u | 13 | 13 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €2,41 | €2,41 | 2.41% |
| bitget - xt | €100,00 | 2026-11-20 | 9.1 u | 3 | 3 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,86 | €-1,86 | -1.86% |
| bitget - xt | €150,00 | 2026-11-19 | 14.9 u | 13 | 13 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €3,61 | €3,61 | 2.41% |
| bitget - xt | €150,00 | 2026-11-20 | 9.1 u | 3 | 2 | 1 | €0,08 | €0,00 (0x) | **€0,08** | 0.05% | €-2,79 | €-2,72 | -1.81% |
| bitget - xt | €200,00 | 2026-11-19 | 14.9 u | 13 | 9 | 4 | €0,62 | €0,12 (4x) | **€0,50** | 0.25% | €4,81 | €5,31 | 2.66% |
| bitget - xt | €200,00 | 2026-11-20 | 9.1 u | 3 | 3 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,71 | €-3,71 | -1.86% |
| bitget - xt | €2.000,00 | 2026-11-19 | 14.9 u | 13 | 5 | 7 | €9,59 | €1,95 (10x) | **€7,64** | 0.38% | €48,12 | €55,76 | 2.79% |
| bitget - xt | €2.000,00 | 2026-11-20 | 9.1 u | 3 | 0 | 3 | €3,05 | €1,46 (4x) | **€1,58** | 0.08% | €-37,20 | €-35,62 | -1.78% |
| bitget - xt | €5.000,00 | 2026-11-19 | 14.9 u | 13 | 4 | 7 | €19,03 | €1,84 (9x) | **€17,19** | 0.34% | €120,30 | €137,49 | 2.75% |
| bitget - xt | €5.000,00 | 2026-11-20 | 9.1 u | 3 | 0 | 3 | €5,87 | €1,46 (4x) | **€4,40** | 0.09% | €-93,04 | €-88,64 | -1.77% |
| gate - htx | €100,00 | 2026-11-19 | 14.9 u | 19 | 19 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,97 | €-0,97 | -0.97% |
| gate - htx | €100,00 | 2026-11-20 | 9.1 u | 13 | 13 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,86 | €-1,86 | -1.86% |
| gate - htx | €150,00 | 2026-11-19 | 14.9 u | 19 | 19 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,46 | €-1,46 | -0.97% |
| gate - htx | €150,00 | 2026-11-20 | 9.1 u | 13 | 13 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,79 | €-2,79 | -1.86% |
| gate - htx | €200,00 | 2026-11-19 | 14.9 u | 19 | 19 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,95 | €-1,95 | -0.97% |
| gate - htx | €200,00 | 2026-11-20 | 9.1 u | 13 | 13 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,72 | €-3,72 | -1.86% |
| gate - htx | €2.000,00 | 2026-11-19 | 14.9 u | 19 | 6 | 13 | €6,88 | €4,50 (12x) | **€2,38** | 0.12% | €-19,49 | €-17,11 | -0.86% |
| gate - htx | €2.000,00 | 2026-11-20 | 9.1 u | 13 | 2 | 11 | €10,94 | €2,28 (9x) | **€8,66** | 0.43% | €-36,92 | €-28,26 | -1.41% |
| gate - htx | €5.000,00 | 2026-11-19 | 14.9 u | 19 | 6 | 10 | €15,55 | €5,58 (13x) | **€9,97** | 0.20% | €-48,72 | €-38,75 | -0.78% |
| gate - htx | €5.000,00 | 2026-11-20 | 9.1 u | 13 | 2 | 10 | €26,85 | €3,00 (10x) | **€23,86** | 0.48% | €-92,70 | €-68,84 | -1.38% |
| htx - kucoin | €100,00 | 2026-11-19 | 14.9 u | 16 | 16 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,76 | €-2,76 | -2.76% |
| htx - kucoin | €100,00 | 2026-11-20 | 9.1 u | 13 | 13 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,70 | €-1,70 | -1.70% |
| htx - kucoin | €150,00 | 2026-11-19 | 14.9 u | 16 | 16 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-4,14 | €-4,14 | -2.76% |
| htx - kucoin | €150,00 | 2026-11-20 | 9.1 u | 13 | 13 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,55 | €-2,55 | -1.70% |
| htx - kucoin | €200,00 | 2026-11-19 | 14.9 u | 16 | 16 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-5,51 | €-5,51 | -2.76% |
| htx - kucoin | €200,00 | 2026-11-20 | 9.1 u | 13 | 13 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,40 | €-3,40 | -1.70% |
| htx - kucoin | €2.000,00 | 2026-11-19 | 14.9 u | 16 | 7 | 9 | €3,96 | €1,18 (6x) | **€2,78** | 0.14% | €-55,07 | €-52,29 | -2.61% |
| htx - kucoin | €2.000,00 | 2026-11-20 | 9.1 u | 13 | 4 | 9 | €8,62 | €0,93 (5x) | **€7,69** | 0.38% | €-34,02 | €-26,33 | -1.32% |
| htx - kucoin | €5.000,00 | 2026-11-19 | 14.9 u | 16 | 3 | 13 | €12,30 | €4,43 (13x) | **€7,87** | 0.16% | €-137,77 | €-129,90 | -2.60% |
| htx - kucoin | €5.000,00 | 2026-11-20 | 9.1 u | 13 | 0 | 13 | €24,51 | €3,82 (11x) | **€20,69** | 0.41% | €-84,89 | €-64,19 | -1.28% |

- htx - xt, €100,00: munten BSV, CBK, LUNC, MEME, SEI, XCH, XDC; bruto zonder voorraadgrens zou €167,63 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - xt, €150,00: munten BSV, CBK, LUNC, MEME, SEI, XCH, XDC; bruto zonder voorraadgrens zou €167,63 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - xt, €200,00: munten BSV, CBK, LUNC, MEME, SEI, XCH, XDC; bruto zonder voorraadgrens zou €167,63 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - xt, €2.000,00: munten BSV, CBK, LUNC, MEME, SEI, XCH, XDC; bruto zonder voorraadgrens zou €165,34 zijn, met voorraad €24,28 (GEZIEN boek, GOK model).
- htx - xt, €5.000,00: munten BSV, CBK, LUNC, MEME, SEI, XCH, XDC; bruto zonder voorraadgrens zou €163,06 zijn, met voorraad €55,40 (GEZIEN boek, GOK model).
- kucoin - xt, €100,00: munten DAG, FIGHT, LUNC; bruto zonder voorraadgrens zou €609,03 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- kucoin - xt, €150,00: munten DAG, FIGHT, LUNC; bruto zonder voorraadgrens zou €609,03 zijn, met voorraad €0,35 (GEZIEN boek, GOK model).
- kucoin - xt, €200,00: munten DAG, FIGHT, LUNC; bruto zonder voorraadgrens zou €609,03 zijn, met voorraad €0,47 (GEZIEN boek, GOK model).
- kucoin - xt, €2.000,00: munten DAG, FIGHT, LUNC; bruto zonder voorraadgrens zou €603,49 zijn, met voorraad €18,40 (GEZIEN boek, GOK model).
- kucoin - xt, €5.000,00: munten DAG, FIGHT, LUNC; bruto zonder voorraadgrens zou €595,63 zijn, met voorraad €39,21 (GEZIEN boek, GOK model).
- bitget - xt, €100,00: munten KOR, KUB, LUNC, YB; bruto zonder voorraadgrens zou €683,18 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - xt, €150,00: munten KOR, KUB, LUNC, YB; bruto zonder voorraadgrens zou €683,18 zijn, met voorraad €0,08 (GEZIEN boek, GOK model).
- bitget - xt, €200,00: munten KOR, KUB, LUNC, YB; bruto zonder voorraadgrens zou €682,65 zijn, met voorraad €0,62 (GEZIEN boek, GOK model).
- bitget - xt, €2.000,00: munten KOR, KUB, LUNC, YB; bruto zonder voorraadgrens zou €676,68 zijn, met voorraad €12,64 (GEZIEN boek, GOK model).
- bitget - xt, €5.000,00: munten KOR, KUB, LUNC, YB; bruto zonder voorraadgrens zou €668,63 zijn, met voorraad €24,90 (GEZIEN boek, GOK model).
- gate - htx, €100,00: munten BSV, CBK, KAS, LAT, LUNC, MEME, MOVR, SEI, WARD, WLD; bruto zonder voorraadgrens zou €134,05 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- gate - htx, €150,00: munten BSV, CBK, KAS, LAT, LUNC, MEME, MOVR, SEI, WARD, WLD; bruto zonder voorraadgrens zou €134,05 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- gate - htx, €200,00: munten BSV, CBK, KAS, LAT, LUNC, MEME, MOVR, SEI, WARD, WLD; bruto zonder voorraadgrens zou €134,05 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- gate - htx, €2.000,00: munten BSV, CBK, KAS, LAT, LUNC, MEME, MOVR, SEI, WARD, WLD; bruto zonder voorraadgrens zou €130,64 zijn, met voorraad €17,82 (GEZIEN boek, GOK model).
- gate - htx, €5.000,00: munten BSV, CBK, KAS, LAT, LUNC, MEME, MOVR, SEI, WARD, WLD; bruto zonder voorraadgrens zou €126,14 zijn, met voorraad €42,40 (GEZIEN boek, GOK model).
- htx - kucoin, €100,00: munten BSV, CHIP, FET, LAT, LUNC, MEME, MOVR, ONE, SOMI, WAN, WARD, WLD, XCH, XEC; bruto zonder voorraadgrens zou €119,39 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - kucoin, €150,00: munten BSV, CHIP, FET, LAT, LUNC, MEME, MOVR, ONE, SOMI, WAN, WARD, WLD, XCH, XEC; bruto zonder voorraadgrens zou €119,39 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - kucoin, €200,00: munten BSV, CHIP, FET, LAT, LUNC, MEME, MOVR, ONE, SOMI, WAN, WARD, WLD, XCH, XEC; bruto zonder voorraadgrens zou €119,39 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - kucoin, €2.000,00: munten BSV, CHIP, FET, LAT, LUNC, MEME, MOVR, ONE, SOMI, WAN, WARD, WLD, XCH, XEC; bruto zonder voorraadgrens zou €118,45 zijn, met voorraad €12,58 (GEZIEN boek, GOK model).
- htx - kucoin, €5.000,00: munten BSV, CHIP, FET, LAT, LUNC, MEME, MOVR, ONE, SOMI, WAN, WARD, WLD, XCH, XEC; bruto zonder voorraadgrens zou €117,05 zijn, met voorraad €36,81 (GEZIEN boek, GOK model).

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

- Opnamekosten bij de echte kansen: 80 van een netwerk dat aan beide kanten open is, 87 van de beurs zelf (laagste open netwerk), 25 geschat uit wat andere beurzen voor die munt vragen (GOK). Onbekende opnamekosten tellen niet als echte kans.
- Netwerk: KuCoin, Gate, Bitget, HTX, XT, Bitstamp, Bitvavo en Poloniex geven hun netwerken per munt. Als beide beurzen dat doen en de namen te koppelen zijn, moet er een netwerk zijn dat aan beide kanten open is. Anders is het netwerk "niet te koppelen" en telt de kans mee (staat apart in de trechter).
- De duur is gemeten in stappen van ±20 seconden; een kans kan een paar rondes eerder begonnen zijn dan we zagen.
- Takerkosten: uit de API waar die ze per paar geeft, anders het standaardtarief uit de README (deels GOK).
- Laatste run: 15 beurzen antwoordden, 2288 munt-quote-paren op minstens twee beurzen (GEZIEN).
