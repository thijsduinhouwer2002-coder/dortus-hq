# Rapport koersverschil-scanner

Gemaakt 2026-11-20 14:54 UTC uit 19 runs, samen ±29.3 uur gemeten (GEZIEN).
Echte kans = winst na alle kosten (opnamekosten bekend), opnemen en storten open (en een netwerk dat aan beide kanten open is, als de beurzen dat geven), minstens €100,00 op het boek, minstens 2 minuten blijven staan, geen andere munt met dezelfde naam.
**Vergund** = beide beurzen hebben een MiCA-vergunning (ESMA-register), vaak via een EU-dochter die minder munten kan hebben dan de wereldwijde API die we meten (GOK). **Grijs** = minstens één beurs zonder vergunning (MEXC, Bitget, HTX, Poloniex, XT, Bitfinex, Binance). Zie README.md.
**Kraken-tarief:** Kraken rekent 0,80% taker op munt tegen EUR, USD, USDT of USDC (GEZIEN, kraken.com/pro/fees, laagste trede); de scanner rekende tot 19 nov met 0,40%. 399 opgeslagen kansen met Kraken uit die runs zijn hier **opnieuw doorgerekend met 0,80%** (GOK-benadering: 0,40% van de inzet aan de Kraken-kant extra op elk gemeten punt van het boek; het boek zelf is niet bewaard). 233 houden daarna nog winst op het boek. Dat ze met hogere kosten ook korter bleven staan, telt niet mee (dus eerder te gunstig).

## Hoeveel wordt er gecontroleerd? (GEZIEN, stand.jsonl)

Per ronde (mediaan over 351 metingen): 1116 kandidaten (verschil op de ticker groter dan de takerkosten), 120 met het orderboek gecontroleerd, 2 nog nooit gecontroleerd (0%).
Bijna alle kandidaten komen aan de beurt; de aantallen hieronder missen weinig.

## Trechter (GEZIEN, eigen metingen)

| Stap | Alle beurzen | Alleen MiCA-beurzen | Met minstens één grijze beurs |
|---|---|---|---|
| Verschillen met winst op het boek na alle kosten | 24514 | 3665 | 20849 |
| ...waarvan opnemen of storten dicht | 5430 | 590 | 4840 |
| ...waarvan status onbekend (beurs geeft het niet openbaar) | 14409 | 2564 | 11845 |
| Opnemen en storten open | 4675 | 511 | 4164 |
| ...en geen netwerk dat aan beide kanten open is: valt af | 136 | 7 | 129 |
| ...en opnamekosten onbekend: valt af | 0 | 0 | 0 |
| ...en minstens €100,00 op het boek | 1364 | 271 | 1093 |
| ...en minstens 2 minuten blijven staan | 388 | 118 | 270 |
| ...en geen andere munt met dezelfde naam | 354 | 104 | 250 |
|    ...waarvan contractadres bekend en gelijk | 47 | 18 | 29 |
|    ...waarvan contractadres onbekend (telt mee, kan een andere munt zijn) | 307 | 86 | 221 |
|    ...waarvan netwerk gekoppeld en open | 229 | 46 | 183 |
|    ...waarvan netwerk niet te koppelen (telt mee) | 125 | 58 | 67 |
| **Echte kansen** (zelfde munt overlappend in de tijd samengevoegd, beste beurspaar telt) | 231 | 104 | 153 |
| Ter vergelijking: zelfde eisen, maar opnamestatus onbekend (niet meegeteld) | 879 | 221 | 742 |

## Echte kansen per dag (GEZIEN)

| Dag | Echt, alleen MiCA | Echt, met grijs | Mediane winst per kans bij €500 (MiCA / grijs) | Mediane duur |
|---|---|---|---|---|
| 2026-11-19 | 49 | 86 | €2,00 / €1,21 | 5.3 min |
| 2026-11-20 | 29 | 67 | €0,68 / €1,08 | 6.2 min |
| Totaal | 78 | 153 | €1,57 / €1,18 | 5.7 min |

## Beste munten (GEZIEN)

| | Soort | Kansen | Som winst bij €500 per kans |
|---|---|---|---|
| MERL-EUR | vergund | 17 | €201,75 |
| LUNC-USDT | grijs | 17 | €61,85 |
| KERNEL-EUR | vergund | 1 | €47,33 |
| MEME-USDT | grijs | 1 | €37,90 |
| USTC-USDT | grijs en vergund | 11 | €37,55 |
| KYO-USDT | vergund | 4 | €24,15 |
| SKY-USD | vergund | 2 | €21,52 |
| LAT-USDT | grijs | 3 | €17,59 |
| GMT-EUR | vergund | 21 | €17,57 |
| YB-USDT | grijs | 2 | €17,52 |

## Beste beursparen (kopen op > verkopen op) (GEZIEN)

| | Soort | Kansen | Som winst bij €500 per kans |
|---|---|---|---|
| bitvavo > kraken | vergund | 54 | €292,19 |
| bitget > htx | grijs | 32 | €69,92 |
| kucoin > htx | grijs | 21 | €56,60 |
| gate > kucoin | vergund | 16 | €49,02 |
| bitget > xt | grijs | 12 | €43,27 |
| kucoin > bitget | grijs | 17 | €41,50 |
| bitget > gate | grijs | 8 | €27,78 |
| gate > xt | grijs | 3 | €23,21 |
| bitstamp > kraken | vergund | 2 | €21,52 |
| bitget > kucoin | grijs | 16 | €17,77 |

Beurzen die het vaakst meedoen (koop of verkoop): bitget (grijs) 97, kucoin 91, htx (grijs) 75, kraken 60, bitvavo 54, gate 48, xt (grijs) 27, poloniex (grijs) 8 (GEZIEN).

## Hoeveel kansen blijven staan terwijl je geld schuift? (GEZIEN, duur uit eigen metingen)

Wie geen voorraad op beide beurzen heeft, moet kopen, de munt opnemen, wachten tot hij binnen is en dan verkopen. Hoe lang dat duurt verschilt per munt en netwerk: een paar minuten (snelle ketens) tot een uur of meer (Bitcoin, beurzen die opnames met de hand keuren) (GOK, niet per munt gemeten).

| Overmaaktijd | Alle beurzen | Alleen MiCA-beurzen | Met minstens één grijze beurs |
|---|---|---|---|
| 5 min | 134 van 231 (58%) | 59 van 104 (57%) | 87 van 153 (57%) |
| 10 min | 80 van 231 (35%) | 38 van 104 (37%) | 51 van 153 (33%) |
| 30 min | 48 van 231 (21%) | 23 van 104 (22%) | 31 van 153 (20%) |
| 60 min | 22 van 231 (10%) | 14 van 104 (13%) | 13 van 153 (8%) |

## Wat zou het opleveren over 3 maanden? (GOK, doorgetrokken uit de metingen)

Gemeten over ±29.3 uur (GEZIEN), doorgetrokken naar 90 dagen (GOK: aanname dat de week die we maten gewoon is).

| Beurzen | Inleg | Model | Kansen per uur | Per kans (mediaan) | 3 maanden |
|---|---|---|---|---|---|
| Alleen MiCA | €2.000,00 | bovengrens: elke kans, geld overal tegelijk | 3.56 | €1,79 | €13.740,53 |
| Alleen MiCA | €2.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 1.85 | €2,53 | €35.852,84 |
| Alleen MiCA | €5.000,00 | bovengrens: elke kans, geld overal tegelijk | 3.56 | €2,41 | €18.517,31 |
| Alleen MiCA | €5.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 1.85 | €3,12 | €50.788,67 |
| Alle (met grijs) | €2.000,00 | bovengrens: elke kans, geld overal tegelijk | 7.90 | €1,45 | €24.767,95 |
| Alle (met grijs) | €2.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 1.85 | €2,53 | €35.852,84 |
| Alle (met grijs) | €5.000,00 | bovengrens: elke kans, geld overal tegelijk | 7.90 | €1,59 | €27.176,51 |
| Alle (met grijs) | €5.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 1.85 | €3,12 | €50.788,67 |

Bovengrens: elke kans met de helft van de inleg aan elke kant, alsof het geld op alle beurzen tegelijk staat (kan in het echt niet). Beste beurspaar: het paar is **achteraf** gekozen uit de metingen (vooraf kiezen levert minder op), en het model neemt aan dat je van elke munt al voorraad op de verkoopbeurs hebt.

Waarom dit te rooskleurig is (GOK): elke kans wordt maar één keer geteld met het mediane boek, maar andere bots pakken hem ook; de munt die je als voorraad aanhoudt kan dalen; na een paar kansen moet de voorraad terug (opnamekosten en tijd); minimale opname- en ordergroottes tellen niet mee; en een kans die we 2 minuten zagen staan, staat er niet per se nog als jouw order binnenkomt. Waarom het te somber kan zijn: niet alle kandidaten zijn gecontroleerd, en met voorraad op beide beurzen kun je dezelfde kans vaker pakken als het boek zich aanvult; dat telt hier niet mee.

## Wat houd je echt over? Voorraad op twee beurzen (simulatie)

Per beurspaar: geld en munten op beide beurzen, elke echte kans uitgevoerd tegen het boek zoals gemeten (niet meer dan de ruimte op het boek en niet meer dan de voorraad op die beurs), terugschuiven als een kant leeg dreigt te raken (met opnamekosten en tijd onderweg), en het koerseffect van de aangehouden munten apart. Netto = bruto min kosten terugschuiven plus koerseffect. **Gemeten** (GEZIEN): de kansen, het boek en de koersen; **de rest is een rekenmodel** (GOK, aannames onder de tabel). Geen advies.

**Met €150: netto €0,89 per dag op bitstamp - kraken (koerseffect erbovenop €-1,48), €0,47 per dag op bitvavo - kraken (koerseffect erbovenop €0,31), €0,19 per dag op gate - kucoin (koerseffect erbovenop €1,03) (GOK: netto handel, rekenmodel op ±14.6 uur meting per dag, alleen MiCA).** "Per dag" is hier gemiddeld over 2 gemeten dagen achter elkaar; de eerste begint met een gelijk verdeelde voorraad; aan het eind staat de voorraad scheef, dus een volgende dag levert waarschijnlijk minder op, tenzij kansen de andere kant op hem terugbrengen (GOK).

### Alleen MiCA-beurzen (alle paren met echte kansen)

| Beurspaar | Inleg | Dag | Gemeten | Kansen | Gemist (geen voorraad) | Kleiner door voorraad | Bruto winst | Kosten terugschuiven | **Netto handel (bruto min kosten)** | Rendement handel | Koerseffect voorraad | Netto met koerseffect | Rendement met koerseffect |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| bitstamp - kraken | €100,00 | 2026-11-19 | 14.9 u | 2 | 1 | 1 | €1,18 | €0,00 (0x) | **€1,18** | 1.18% | €0,63 | €1,81 | 1.81% |
| bitstamp - kraken | €100,00 | 2026-11-20 | 14.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,60 | €-2,60 | -2.60% |
| bitstamp - kraken | €150,00 | 2026-11-19 | 14.9 u | 2 | 1 | 1 | €1,78 | €0,00 (0x) | **€1,78** | 1.18% | €0,94 | €2,72 | 1.81% |
| bitstamp - kraken | €150,00 | 2026-11-20 | 14.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,91 | €-3,91 | -2.60% |
| bitstamp - kraken | €200,00 | 2026-11-19 | 14.9 u | 2 | 1 | 1 | €2,37 | €0,00 (0x) | **€2,37** | 1.18% | €1,25 | €3,62 | 1.81% |
| bitstamp - kraken | €200,00 | 2026-11-20 | 14.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-5,21 | €-5,21 | -2.60% |
| bitstamp - kraken | €2.000,00 | 2026-11-19 | 14.9 u | 2 | 1 | 0 | €11,71 | €0,00 (0x) | **€11,71** | 0.59% | €12,53 | €24,24 | 1.21% |
| bitstamp - kraken | €2.000,00 | 2026-11-20 | 14.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-52,07 | €-52,07 | -2.60% |
| bitstamp - kraken | €5.000,00 | 2026-11-19 | 14.9 u | 2 | 1 | 0 | €11,71 | €0,00 (0x) | **€11,71** | 0.23% | €31,33 | €43,04 | 0.86% |
| bitstamp - kraken | €5.000,00 | 2026-11-20 | 14.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-130,19 | €-130,19 | -2.60% |
| bitvavo - kraken | €100,00 | 2026-11-19 | 14.9 u | 43 | 43 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,29 | €-0,29 | -0.29% |
| bitvavo - kraken | €100,00 | 2026-11-20 | 14.3 u | 11 | 11 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,70 | €0,70 | 0.70% |
| bitvavo - kraken | €150,00 | 2026-11-19 | 14.9 u | 43 | 38 | 5 | €0,08 | €0,00 (0x) | **€0,08** | 0.05% | €-0,43 | €-0,35 | -0.23% |
| bitvavo - kraken | €150,00 | 2026-11-20 | 14.3 u | 11 | 10 | 1 | €0,87 | €0,00 (0x) | **€0,87** | 0.58% | €1,05 | €1,92 | 1.28% |
| bitvavo - kraken | €200,00 | 2026-11-19 | 14.9 u | 43 | 37 | 6 | €0,16 | €0,00 (0x) | **€0,16** | 0.08% | €-0,58 | €-0,42 | -0.21% |
| bitvavo - kraken | €200,00 | 2026-11-20 | 14.3 u | 11 | 10 | 1 | €0,78 | €0,00 (0x) | **€0,78** | 0.39% | €1,40 | €2,17 | 1.09% |
| bitvavo - kraken | €2.000,00 | 2026-11-19 | 14.9 u | 43 | 28 | 15 | €11,33 | €6,07 (15x) | **€5,26** | 0.26% | €-5,71 | €-0,45 | -0.02% |
| bitvavo - kraken | €2.000,00 | 2026-11-20 | 14.3 u | 11 | 9 | 2 | €13,71 | €1,32 (2x) | **€12,39** | 0.62% | €14,21 | €26,60 | 1.33% |
| bitvavo - kraken | €5.000,00 | 2026-11-19 | 14.9 u | 43 | 23 | 20 | €29,68 | €14,63 (23x) | **€15,05** | 0.30% | €-14,32 | €0,74 | 0.01% |
| bitvavo - kraken | €5.000,00 | 2026-11-20 | 14.3 u | 11 | 2 | 9 | €36,60 | €9,38 (10x) | **€27,23** | 0.54% | €35,88 | €63,11 | 1.26% |
| gate - kucoin | €100,00 | 2026-11-19 | 14.9 u | 25 | 25 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,17 | €-0,17 | -0.17% |
| gate - kucoin | €100,00 | 2026-11-20 | 14.3 u | 23 | 21 | 2 | €0,13 | €0,00 (1x) | **€0,13** | 0.13% | €1,54 | €1,66 | 1.66% |
| gate - kucoin | €150,00 | 2026-11-19 | 14.9 u | 25 | 25 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,25 | €-0,25 | -0.17% |
| gate - kucoin | €150,00 | 2026-11-20 | 14.3 u | 23 | 19 | 4 | €0,41 | €0,02 (2x) | **€0,39** | 0.26% | €2,30 | €2,69 | 1.80% |
| gate - kucoin | €200,00 | 2026-11-19 | 14.9 u | 25 | 17 | 8 | €0,23 | €0,00 (0x) | **€0,23** | 0.12% | €-0,33 | €-0,10 | -0.05% |
| gate - kucoin | €200,00 | 2026-11-20 | 14.3 u | 23 | 12 | 11 | €0,91 | €0,02 (2x) | **€0,89** | 0.45% | €3,07 | €3,97 | 1.98% |
| gate - kucoin | €2.000,00 | 2026-11-19 | 14.9 u | 25 | 10 | 15 | €3,16 | €2,19 (12x) | **€0,97** | 0.05% | €-3,32 | €-2,35 | -0.12% |
| gate - kucoin | €2.000,00 | 2026-11-20 | 14.3 u | 23 | 7 | 16 | €9,66 | €1,35 (10x) | **€8,31** | 0.42% | €30,80 | €39,10 | 1.96% |
| gate - kucoin | €5.000,00 | 2026-11-19 | 14.9 u | 25 | 6 | 19 | €12,14 | €4,84 (19x) | **€7,30** | 0.15% | €-8,32 | €-1,02 | -0.02% |
| gate - kucoin | €5.000,00 | 2026-11-20 | 14.3 u | 23 | 5 | 18 | €23,91 | €5,74 (17x) | **€18,17** | 0.36% | €77,22 | €95,38 | 1.91% |

- bitstamp - kraken, €100,00: munten SKY; bruto zonder voorraadgrens zou €22,30 zijn, met voorraad €1,18 (GEZIEN boek, GOK model).
- bitstamp - kraken, €150,00: munten SKY; bruto zonder voorraadgrens zou €21,71 zijn, met voorraad €1,78 (GEZIEN boek, GOK model).
- bitstamp - kraken, €200,00: munten SKY; bruto zonder voorraadgrens zou €21,12 zijn, met voorraad €2,37 (GEZIEN boek, GOK model).
- bitstamp - kraken, €2.000,00: munten SKY; bruto zonder voorraadgrens zou €11,71 zijn, met voorraad €11,71 (GEZIEN boek, GOK model).
- bitstamp - kraken, €5.000,00: munten SKY; bruto zonder voorraadgrens zou €11,71 zijn, met voorraad €11,71 (GEZIEN boek, GOK model).
- bitvavo - kraken, €100,00: munten AVA, DYM, GMT, KERNEL, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €894,60 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitvavo - kraken, €150,00: munten AVA, DYM, GMT, KERNEL, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €894,60 zijn, met voorraad €0,95 (GEZIEN boek, GOK model).
- bitvavo - kraken, €200,00: munten AVA, DYM, GMT, KERNEL, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €894,14 zijn, met voorraad €0,94 (GEZIEN boek, GOK model).
- bitvavo - kraken, €2.000,00: munten AVA, DYM, GMT, KERNEL, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €870,91 zijn, met voorraad €25,04 (GEZIEN boek, GOK model).
- bitvavo - kraken, €5.000,00: munten AVA, DYM, GMT, KERNEL, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €835,68 zijn, met voorraad €66,29 (GEZIEN boek, GOK model).
- gate - kucoin, €100,00: munten ALKIMI, AVAIL, CHR, CYBER, ERG, FTT, IKA, IR, KYO, LUNC, NIM, OVR, RARI, USTC, VERONA; bruto zonder voorraadgrens zou €172,74 zijn, met voorraad €0,13 (GEZIEN boek, GOK model).
- gate - kucoin, €150,00: munten ALKIMI, AVAIL, CHR, CYBER, ERG, FTT, IKA, IR, KYO, LUNC, NIM, OVR, RARI, USTC, VERONA; bruto zonder voorraadgrens zou €172,60 zijn, met voorraad €0,41 (GEZIEN boek, GOK model).
- gate - kucoin, €200,00: munten ALKIMI, AVAIL, CHR, CYBER, ERG, FTT, IKA, IR, KYO, LUNC, NIM, OVR, RARI, USTC, VERONA; bruto zonder voorraadgrens zou €172,51 zijn, met voorraad €1,14 (GEZIEN boek, GOK model).
- gate - kucoin, €2.000,00: munten ALKIMI, AVAIL, CHR, CYBER, ERG, FTT, IKA, IR, KYO, LUNC, NIM, OVR, RARI, USTC, VERONA; bruto zonder voorraadgrens zou €170,15 zijn, met voorraad €12,82 (GEZIEN boek, GOK model).
- gate - kucoin, €5.000,00: munten ALKIMI, AVAIL, CHR, CYBER, ERG, FTT, IKA, IR, KYO, LUNC, NIM, OVR, RARI, USTC, VERONA; bruto zonder voorraadgrens zou €163,62 zijn, met voorraad €36,05 (GEZIEN boek, GOK model).

### Met minstens één grijze beurs (de 5 paren met de meeste bruto winst)

| Beurspaar | Inleg | Dag | Gemeten | Kansen | Gemist (geen voorraad) | Kleiner door voorraad | Bruto winst | Kosten terugschuiven | **Netto handel (bruto min kosten)** | Rendement handel | Koerseffect voorraad | Netto met koerseffect | Rendement met koerseffect |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| htx - xt | €100,00 | 2026-11-19 | 14.9 u | 18 | 18 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,59 | €-0,59 | -0.59% |
| htx - xt | €100,00 | 2026-11-20 | 14.3 u | 9 | 9 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,95 | €-0,95 | -0.95% |
| htx - xt | €150,00 | 2026-11-19 | 14.9 u | 18 | 18 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,89 | €-0,89 | -0.59% |
| htx - xt | €150,00 | 2026-11-20 | 14.3 u | 9 | 9 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,42 | €-1,42 | -0.95% |
| htx - xt | €200,00 | 2026-11-19 | 14.9 u | 18 | 18 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,18 | €-1,18 | -0.59% |
| htx - xt | €200,00 | 2026-11-20 | 14.3 u | 9 | 9 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,89 | €-1,89 | -0.95% |
| htx - xt | €2.000,00 | 2026-11-19 | 14.9 u | 18 | 5 | 13 | €8,12 | €5,28 (12x) | **€2,85** | 0.14% | €-11,88 | €-9,04 | -0.45% |
| htx - xt | €2.000,00 | 2026-11-20 | 14.3 u | 9 | 1 | 8 | €14,56 | €1,65 (5x) | **€12,91** | 0.65% | €-18,45 | €-5,54 | -0.28% |
| htx - xt | €5.000,00 | 2026-11-19 | 14.9 u | 18 | 5 | 12 | €17,69 | €7,10 (14x) | **€10,60** | 0.21% | €-29,63 | €-19,03 | -0.38% |
| htx - xt | €5.000,00 | 2026-11-20 | 14.3 u | 9 | 0 | 9 | €35,45 | €3,52 (7x) | **€31,93** | 0.64% | €-46,79 | €-14,86 | -0.30% |
| bitget - xt | €100,00 | 2026-11-19 | 14.9 u | 13 | 13 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €2,07 | €2,07 | 2.07% |
| bitget - xt | €100,00 | 2026-11-20 | 14.3 u | 4 | 4 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,59 | €-3,59 | -3.59% |
| bitget - xt | €150,00 | 2026-11-19 | 14.9 u | 13 | 13 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €3,11 | €3,11 | 2.07% |
| bitget - xt | €150,00 | 2026-11-20 | 14.3 u | 4 | 4 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-5,39 | €-5,39 | -3.59% |
| bitget - xt | €200,00 | 2026-11-19 | 14.9 u | 13 | 9 | 4 | €0,50 | €0,01 (3x) | **€0,50** | 0.25% | €4,15 | €4,64 | 2.32% |
| bitget - xt | €200,00 | 2026-11-20 | 14.3 u | 4 | 4 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-7,18 | €-7,18 | -3.59% |
| bitget - xt | €2.000,00 | 2026-11-19 | 14.9 u | 13 | 4 | 9 | €9,96 | €1,96 (11x) | **€8,00** | 0.40% | €41,46 | €49,46 | 2.47% |
| bitget - xt | €2.000,00 | 2026-11-20 | 14.3 u | 4 | 0 | 4 | €4,66 | €2,05 (5x) | **€2,61** | 0.13% | €-71,79 | €-69,19 | -3.46% |
| bitget - xt | €5.000,00 | 2026-11-19 | 14.9 u | 13 | 4 | 8 | €19,47 | €1,85 (10x) | **€17,62** | 0.35% | €103,65 | €121,27 | 2.43% |
| bitget - xt | €5.000,00 | 2026-11-20 | 14.3 u | 4 | 0 | 4 | €9,88 | €2,05 (5x) | **€7,82** | 0.16% | €-179,58 | €-171,75 | -3.44% |
| kucoin - xt | €100,00 | 2026-11-19 | 14.9 u | 13 | 13 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,07 | €0,07 | 0.07% |
| kucoin - xt | €100,00 | 2026-11-20 | 14.3 u | 2 | 2 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,87 | €-0,87 | -0.87% |
| kucoin - xt | €150,00 | 2026-11-19 | 14.9 u | 13 | 13 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,11 | €0,11 | 0.07% |
| kucoin - xt | €150,00 | 2026-11-20 | 14.3 u | 2 | 2 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,30 | €-1,30 | -0.87% |
| kucoin - xt | €200,00 | 2026-11-19 | 14.9 u | 13 | 10 | 3 | €0,35 | €0,00 (0x) | **€0,35** | 0.18% | €0,15 | €0,50 | 0.25% |
| kucoin - xt | €200,00 | 2026-11-20 | 14.3 u | 2 | 1 | 1 | €0,22 | €0,00 (0x) | **€0,22** | 0.11% | €-1,73 | €-1,51 | -0.75% |
| kucoin - xt | €2.000,00 | 2026-11-19 | 14.9 u | 13 | 3 | 10 | €13,20 | €5,51 (11x) | **€7,69** | 0.38% | €1,50 | €9,19 | 0.46% |
| kucoin - xt | €2.000,00 | 2026-11-20 | 14.3 u | 2 | 0 | 2 | €4,03 | €2,08 (3x) | **€1,95** | 0.10% | €-17,06 | €-15,11 | -0.76% |
| kucoin - xt | €5.000,00 | 2026-11-19 | 14.9 u | 13 | 3 | 8 | €28,07 | €5,51 (11x) | **€22,57** | 0.45% | €3,73 | €26,30 | 0.53% |
| kucoin - xt | €5.000,00 | 2026-11-20 | 14.3 u | 2 | 0 | 1 | €11,88 | €2,08 (3x) | **€9,80** | 0.20% | €-43,03 | €-33,23 | -0.66% |
| gate - htx | €100,00 | 2026-11-19 | 14.9 u | 19 | 19 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,78 | €-0,78 | -0.78% |
| gate - htx | €100,00 | 2026-11-20 | 14.3 u | 15 | 15 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,15 | €-2,15 | -2.15% |
| gate - htx | €150,00 | 2026-11-19 | 14.9 u | 19 | 19 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,17 | €-1,17 | -0.78% |
| gate - htx | €150,00 | 2026-11-20 | 14.3 u | 15 | 15 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,22 | €-3,22 | -2.15% |
| gate - htx | €200,00 | 2026-11-19 | 14.9 u | 19 | 19 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,56 | €-1,56 | -0.78% |
| gate - htx | €200,00 | 2026-11-20 | 14.3 u | 15 | 15 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-4,30 | €-4,30 | -2.15% |
| gate - htx | €2.000,00 | 2026-11-19 | 14.9 u | 19 | 7 | 12 | €5,99 | €3,58 (10x) | **€2,40** | 0.12% | €-15,69 | €-13,28 | -0.66% |
| gate - htx | €2.000,00 | 2026-11-20 | 14.3 u | 15 | 2 | 13 | €10,51 | €2,41 (10x) | **€8,09** | 0.40% | €-42,53 | €-34,44 | -1.72% |
| gate - htx | €5.000,00 | 2026-11-19 | 14.9 u | 19 | 6 | 11 | €14,83 | €5,58 (13x) | **€9,25** | 0.19% | €-39,16 | €-29,91 | -0.60% |
| gate - htx | €5.000,00 | 2026-11-20 | 14.3 u | 15 | 2 | 13 | €26,07 | €3,75 (12x) | **€22,32** | 0.45% | €-106,95 | €-84,63 | -1.69% |
| htx - kucoin | €100,00 | 2026-11-19 | 14.9 u | 16 | 16 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,61 | €-2,61 | -2.61% |
| htx - kucoin | €100,00 | 2026-11-20 | 14.3 u | 21 | 21 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,65 | €-2,65 | -2.65% |
| htx - kucoin | €150,00 | 2026-11-19 | 14.9 u | 16 | 16 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,92 | €-3,92 | -2.61% |
| htx - kucoin | €150,00 | 2026-11-20 | 14.3 u | 21 | 21 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,97 | €-3,97 | -2.65% |
| htx - kucoin | €200,00 | 2026-11-19 | 14.9 u | 16 | 16 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-5,22 | €-5,22 | -2.61% |
| htx - kucoin | €200,00 | 2026-11-20 | 14.3 u | 21 | 21 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-5,29 | €-5,29 | -2.65% |
| htx - kucoin | €2.000,00 | 2026-11-19 | 14.9 u | 16 | 7 | 9 | €3,70 | €0,86 (5x) | **€2,83** | 0.14% | €-52,17 | €-49,34 | -2.47% |
| htx - kucoin | €2.000,00 | 2026-11-20 | 14.3 u | 21 | 10 | 11 | €8,28 | €1,20 (6x) | **€7,08** | 0.35% | €-52,90 | €-45,82 | -2.29% |
| htx - kucoin | €5.000,00 | 2026-11-19 | 14.9 u | 16 | 3 | 13 | €11,48 | €4,43 (13x) | **€7,05** | 0.14% | €-130,52 | €-123,47 | -2.47% |
| htx - kucoin | €5.000,00 | 2026-11-20 | 14.3 u | 21 | 4 | 17 | €23,77 | €4,76 (14x) | **€19,01** | 0.38% | €-132,03 | €-113,02 | -2.26% |

- htx - xt, €100,00: munten BSV, CARV, CBK, LUNC, MEME, SEI, XCH, XDC; bruto zonder voorraadgrens zou €175,49 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - xt, €150,00: munten BSV, CARV, CBK, LUNC, MEME, SEI, XCH, XDC; bruto zonder voorraadgrens zou €175,49 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - xt, €200,00: munten BSV, CARV, CBK, LUNC, MEME, SEI, XCH, XDC; bruto zonder voorraadgrens zou €175,49 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - xt, €2.000,00: munten BSV, CARV, CBK, LUNC, MEME, SEI, XCH, XDC; bruto zonder voorraadgrens zou €173,48 zijn, met voorraad €22,69 (GEZIEN boek, GOK model).
- htx - xt, €5.000,00: munten BSV, CARV, CBK, LUNC, MEME, SEI, XCH, XDC; bruto zonder voorraadgrens zou €171,30 zijn, met voorraad €53,15 (GEZIEN boek, GOK model).
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
- htx - kucoin, €100,00: munten BSV, CHIP, FET, LAT, LUNC, MEME, MOVR, ONE, SOMI, WAN, WARD, WLD, XCH, XEC, XMR; bruto zonder voorraadgrens zou €128,45 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - kucoin, €150,00: munten BSV, CHIP, FET, LAT, LUNC, MEME, MOVR, ONE, SOMI, WAN, WARD, WLD, XCH, XEC, XMR; bruto zonder voorraadgrens zou €128,45 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - kucoin, €200,00: munten BSV, CHIP, FET, LAT, LUNC, MEME, MOVR, ONE, SOMI, WAN, WARD, WLD, XCH, XEC, XMR; bruto zonder voorraadgrens zou €128,45 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - kucoin, €2.000,00: munten BSV, CHIP, FET, LAT, LUNC, MEME, MOVR, ONE, SOMI, WAN, WARD, WLD, XCH, XEC, XMR; bruto zonder voorraadgrens zou €127,58 zijn, met voorraad €11,98 (GEZIEN boek, GOK model).
- htx - kucoin, €5.000,00: munten BSV, CHIP, FET, LAT, LUNC, MEME, MOVR, ONE, SOMI, WAN, WARD, WLD, XCH, XEC, XMR; bruto zonder voorraadgrens zou €126,27 zijn, met voorraad €35,24 (GEZIEN boek, GOK model).

### Andere keuzes bij bitvavo - kraken (netto handel, alle dagen samen; GOK)

| Keuze | Inleg | Kansen | Gemist | Bruto winst | Kosten terugschuiven | Netto handel |
|---|---|---|---|---|---|---|
| standaard (schuifdrempel 25%, kostengrens 1%) | €150,00 | 54 | 48 | €0,95 | €0,00 | **€0,95** |
| standaard (schuifdrempel 25%, kostengrens 1%) | €2.000,00 | 54 | 37 | €25,04 | €7,39 | **€17,65** |
| schuifdrempel 10% | €150,00 | 54 | 48 | €0,95 | €0,00 | **€0,95** |
| schuifdrempel 10% | €2.000,00 | 54 | 37 | €24,87 | €6,37 | **€18,50** |
| schuifdrempel 40% | €150,00 | 54 | 48 | €0,95 | €0,00 | **€0,95** |
| schuifdrempel 40% | €2.000,00 | 54 | 34 | €29,73 | €9,33 | **€20,41** |
| kostengrens 2% (achteraf vergeleken) | €150,00 | 54 | 48 | €0,95 | €0,00 | **€0,95** |
| kostengrens 2% (achteraf vergeleken) | €2.000,00 | 54 | 25 | €28,16 | €24,01 | **€4,15** |
| kostengrens 5% (achteraf vergeleken) | €150,00 | 54 | 48 | €0,95 | €1,00 | **€-0,05** |
| kostengrens 5% (achteraf vergeleken) | €2.000,00 | 54 | 25 | €28,16 | €24,01 | **€4,15** |
| alleen MERL en KERNEL (meer voorraad per munt, achteraf gekozen) | €150,00 | 18 | 16 | €2,05 | €0,00 | **€2,05** |
| alleen MERL en KERNEL (meer voorraad per munt, achteraf gekozen) | €2.000,00 | 18 | 9 | €73,99 | €8,75 | **€65,24** |

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

- Opnamekosten bij de echte kansen: 97 van een netwerk dat aan beide kanten open is, 90 van de beurs zelf (laagste open netwerk), 44 geschat uit wat andere beurzen voor die munt vragen (GOK). Onbekende opnamekosten tellen niet als echte kans.
- Netwerk: KuCoin, Gate, Bitget, HTX, XT, Bitstamp, Bitvavo en Poloniex geven hun netwerken per munt. Als beide beurzen dat doen en de namen te koppelen zijn, moet er een netwerk zijn dat aan beide kanten open is. Anders is het netwerk "niet te koppelen" en telt de kans mee (staat apart in de trechter).
- De duur is gemeten in stappen van ±20 seconden; een kans kan een paar rondes eerder begonnen zijn dan we zagen.
- Takerkosten: uit de API waar die ze per paar geeft, anders het standaardtarief uit de README (deels GOK).
- Laatste run: 15 beurzen antwoordden, 2288 munt-quote-paren op minstens twee beurzen (GEZIEN).
