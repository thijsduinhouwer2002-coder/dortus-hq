# Rapport koersverschil-scanner

Gemaakt 2026-11-20 15:09 UTC uit 19 runs, samen ±29.4 uur gemeten (GEZIEN).
Echte kans = winst na alle kosten (opnamekosten bekend), opnemen en storten open (en een netwerk dat aan beide kanten open is, als de beurzen dat geven), minstens €100,00 op het boek, minstens 2 minuten blijven staan, geen andere munt met dezelfde naam.
**Vergund** = beide beurzen hebben een MiCA-vergunning (ESMA-register), vaak via een EU-dochter die minder munten kan hebben dan de wereldwijde API die we meten (GOK). **Grijs** = minstens één beurs zonder vergunning (MEXC, Bitget, HTX, Poloniex, XT, Bitfinex, Binance). Zie README.md.
**Kraken-tarief:** Kraken rekent 0,80% taker op munt tegen EUR, USD, USDT of USDC (GEZIEN, kraken.com/pro/fees, laagste trede); de scanner rekende tot 19 nov met 0,40%. 399 opgeslagen kansen met Kraken uit die runs zijn hier **opnieuw doorgerekend met 0,80%** (GOK-benadering: 0,40% van de inzet aan de Kraken-kant extra op elk gemeten punt van het boek; het boek zelf is niet bewaard). 233 houden daarna nog winst op het boek. Dat ze met hogere kosten ook korter bleven staan, telt niet mee (dus eerder te gunstig).

## Hoeveel wordt er gecontroleerd? (GEZIEN, stand.jsonl)

Per ronde (mediaan over 353 metingen): 1115 kandidaten (verschil op de ticker groter dan de takerkosten), 120 met het orderboek gecontroleerd, 2 nog nooit gecontroleerd (0%).
Bijna alle kandidaten komen aan de beurt; de aantallen hieronder missen weinig.

## Trechter (GEZIEN, eigen metingen)

| Stap | Alle beurzen | Alleen MiCA-beurzen | Met minstens één grijze beurs |
|---|---|---|---|
| Verschillen met winst op het boek na alle kosten | 24754 | 3696 | 21058 |
| ...waarvan opnemen of storten dicht | 5481 | 593 | 4888 |
| ...waarvan status onbekend (beurs geeft het niet openbaar) | 14538 | 2585 | 11953 |
| Opnemen en storten open | 4735 | 518 | 4217 |
| ...en geen netwerk dat aan beide kanten open is: valt af | 136 | 7 | 129 |
| ...en opnamekosten onbekend: valt af | 0 | 0 | 0 |
| ...en minstens €100,00 op het boek | 1386 | 276 | 1110 |
| ...en minstens 2 minuten blijven staan | 401 | 120 | 281 |
| ...en geen andere munt met dezelfde naam | 367 | 106 | 261 |
|    ...waarvan contractadres bekend en gelijk | 47 | 18 | 29 |
|    ...waarvan contractadres onbekend (telt mee, kan een andere munt zijn) | 320 | 88 | 232 |
|    ...waarvan netwerk gekoppeld en open | 235 | 47 | 188 |
|    ...waarvan netwerk niet te koppelen (telt mee) | 132 | 59 | 73 |
| **Echte kansen** (zelfde munt overlappend in de tijd samengevoegd, beste beurspaar telt) | 228 | 106 | 151 |
| Ter vergelijking: zelfde eisen, maar opnamestatus onbekend (niet meegeteld) | 893 | 225 | 753 |

## Echte kansen per dag (GEZIEN)

| Dag | Echt, alleen MiCA | Echt, met grijs | Mediane winst per kans bij €500 (MiCA / grijs) | Mediane duur |
|---|---|---|---|---|
| 2026-11-19 | 49 | 86 | €2,00 / €1,21 | 5.3 min |
| 2026-11-20 | 28 | 65 | €0,86 / €1,27 | 7.3 min |
| Totaal | 77 | 151 | €1,58 / €1,21 | 5.8 min |

## Beste munten (GEZIEN)

| | Soort | Kansen | Som winst bij €500 per kans |
|---|---|---|---|
| MERL-EUR | vergund | 18 | €234,30 |
| LUNC-USDT | grijs | 12 | €66,95 |
| KERNEL-EUR | vergund | 1 | €47,33 |
| USTC-USDT | grijs | 10 | €39,46 |
| MEME-USDT | grijs | 1 | €37,90 |
| KYO-USDT | vergund | 4 | €24,15 |
| SKY-USD | vergund | 2 | €21,52 |
| LAT-USDT | grijs | 3 | €17,59 |
| GMT-EUR | vergund | 21 | €17,57 |
| YB-USDT | grijs | 2 | €17,52 |

## Beste beursparen (kopen op > verkopen op) (GEZIEN)

| | Soort | Kansen | Som winst bij €500 per kans |
|---|---|---|---|
| bitvavo > kraken | vergund | 55 | €324,74 |
| bitget > htx | grijs | 32 | €69,92 |
| kucoin > htx | grijs | 21 | €56,11 |
| gate > kucoin | vergund | 16 | €49,02 |
| kucoin > bitget | grijs | 18 | €45,64 |
| bitget > xt | grijs | 12 | €43,27 |
| bitget > gate | grijs | 8 | €27,78 |
| gate > xt | grijs | 3 | €23,21 |
| bitstamp > kraken | vergund | 2 | €21,52 |
| htx > xt | grijs | 3 | €19,34 |

Beurzen die het vaakst meedoen (koop of verkoop): bitget (grijs) 99, kucoin 86, htx (grijs) 70, kraken 61, bitvavo 55, gate 46, xt (grijs) 29, poloniex (grijs) 8 (GEZIEN).

## Hoeveel kansen blijven staan terwijl je geld schuift? (GEZIEN, duur uit eigen metingen)

Wie geen voorraad op beide beurzen heeft, moet kopen, de munt opnemen, wachten tot hij binnen is en dan verkopen. Hoe lang dat duurt verschilt per munt en netwerk: een paar minuten (snelle ketens) tot een uur of meer (Bitcoin, beurzen die opnames met de hand keuren) (GOK, niet per munt gemeten).

| Overmaaktijd | Alle beurzen | Alleen MiCA-beurzen | Met minstens één grijze beurs |
|---|---|---|---|
| 5 min | 135 van 228 (59%) | 61 van 106 (58%) | 89 van 151 (59%) |
| 10 min | 83 van 228 (36%) | 40 van 106 (38%) | 55 van 151 (36%) |
| 30 min | 51 van 228 (22%) | 25 van 106 (24%) | 34 van 151 (23%) |
| 60 min | 25 van 228 (11%) | 16 van 106 (15%) | 16 van 151 (11%) |

## Wat zou het opleveren over 3 maanden? (GOK, doorgetrokken uit de metingen)

Gemeten over ±29.4 uur (GEZIEN), doorgetrokken naar 90 dagen (GOK: aanname dat de week die we maten gewoon is).

| Beurzen | Inleg | Model | Kansen per uur | Per kans (mediaan) | 3 maanden |
|---|---|---|---|---|---|
| Alleen MiCA | €2.000,00 | bovengrens: elke kans, geld overal tegelijk | 3.60 | €1,98 | €15.447,02 |
| Alleen MiCA | €2.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 1.87 | €2,54 | €40.285,62 |
| Alleen MiCA | €5.000,00 | bovengrens: elke kans, geld overal tegelijk | 3.60 | €2,55 | €19.811,75 |
| Alleen MiCA | €5.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 1.87 | €3,15 | €58.900,14 |
| Alle (met grijs) | €2.000,00 | bovengrens: elke kans, geld overal tegelijk | 7.75 | €1,55 | €26.014,52 |
| Alle (met grijs) | €2.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 1.87 | €2,54 | €40.285,62 |
| Alle (met grijs) | €5.000,00 | bovengrens: elke kans, geld overal tegelijk | 7.75 | €1,78 | €29.821,40 |
| Alle (met grijs) | €5.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 1.87 | €3,15 | €58.900,14 |

Bovengrens: elke kans met de helft van de inleg aan elke kant, alsof het geld op alle beurzen tegelijk staat (kan in het echt niet). Beste beurspaar: het paar is **achteraf** gekozen uit de metingen (vooraf kiezen levert minder op), en het model neemt aan dat je van elke munt al voorraad op de verkoopbeurs hebt.

Waarom dit te rooskleurig is (GOK): elke kans wordt maar één keer geteld met het mediane boek, maar andere bots pakken hem ook; de munt die je als voorraad aanhoudt kan dalen; na een paar kansen moet de voorraad terug (opnamekosten en tijd); minimale opname- en ordergroottes tellen niet mee; en een kans die we 2 minuten zagen staan, staat er niet per se nog als jouw order binnenkomt. Waarom het te somber kan zijn: niet alle kandidaten zijn gecontroleerd, en met voorraad op beide beurzen kun je dezelfde kans vaker pakken als het boek zich aanvult; dat telt hier niet mee.

## Wat houd je echt over? Voorraad op twee beurzen (simulatie)

Per beurspaar: geld en munten op beide beurzen, elke echte kans uitgevoerd tegen het boek zoals gemeten (niet meer dan de ruimte op het boek en niet meer dan de voorraad op die beurs), terugschuiven als een kant leeg dreigt te raken (met opnamekosten en tijd onderweg), en het koerseffect van de aangehouden munten apart. Netto = bruto min kosten terugschuiven plus koerseffect. **Gemeten** (GEZIEN): de kansen, het boek en de koersen; **de rest is een rekenmodel** (GOK, aannames onder de tabel). Geen advies.

**Met €150: netto €0,89 per dag op bitstamp - kraken (koerseffect erbovenop €-1,68), €0,47 per dag op bitvavo - kraken (koerseffect erbovenop €0,27), €0,19 per dag op gate - kucoin (koerseffect erbovenop €0,83) (GOK: netto handel, rekenmodel op ±14.7 uur meting per dag, alleen MiCA).** "Per dag" is hier gemiddeld over 2 gemeten dagen achter elkaar; de eerste begint met een gelijk verdeelde voorraad; aan het eind staat de voorraad scheef, dus een volgende dag levert waarschijnlijk minder op, tenzij kansen de andere kant op hem terugbrengen (GOK).

### Alleen MiCA-beurzen (alle paren met echte kansen)

| Beurspaar | Inleg | Dag | Gemeten | Kansen | Gemist (geen voorraad) | Kleiner door voorraad | Bruto winst | Kosten terugschuiven | **Netto handel (bruto min kosten)** | Rendement handel | Koerseffect voorraad | Netto met koerseffect | Rendement met koerseffect |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| bitstamp - kraken | €100,00 | 2026-11-19 | 14.9 u | 2 | 1 | 1 | €1,18 | €0,00 (0x) | **€1,18** | 1.18% | €0,63 | €1,81 | 1.81% |
| bitstamp - kraken | €100,00 | 2026-11-20 | 14.5 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,86 | €-2,86 | -2.86% |
| bitstamp - kraken | €150,00 | 2026-11-19 | 14.9 u | 2 | 1 | 1 | €1,78 | €0,00 (0x) | **€1,78** | 1.18% | €0,94 | €2,72 | 1.81% |
| bitstamp - kraken | €150,00 | 2026-11-20 | 14.5 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-4,29 | €-4,29 | -2.86% |
| bitstamp - kraken | €200,00 | 2026-11-19 | 14.9 u | 2 | 1 | 1 | €2,37 | €0,00 (0x) | **€2,37** | 1.18% | €1,25 | €3,62 | 1.81% |
| bitstamp - kraken | €200,00 | 2026-11-20 | 14.5 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-5,73 | €-5,73 | -2.86% |
| bitstamp - kraken | €2.000,00 | 2026-11-19 | 14.9 u | 2 | 1 | 0 | €11,71 | €0,00 (0x) | **€11,71** | 0.59% | €12,53 | €24,24 | 1.21% |
| bitstamp - kraken | €2.000,00 | 2026-11-20 | 14.5 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-57,26 | €-57,26 | -2.86% |
| bitstamp - kraken | €5.000,00 | 2026-11-19 | 14.9 u | 2 | 1 | 0 | €11,71 | €0,00 (0x) | **€11,71** | 0.23% | €31,33 | €43,04 | 0.86% |
| bitstamp - kraken | €5.000,00 | 2026-11-20 | 14.5 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-143,15 | €-143,15 | -2.86% |
| bitvavo - kraken | €100,00 | 2026-11-19 | 14.9 u | 43 | 43 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,29 | €-0,29 | -0.29% |
| bitvavo - kraken | €100,00 | 2026-11-20 | 14.5 u | 12 | 12 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,65 | €0,65 | 0.65% |
| bitvavo - kraken | €150,00 | 2026-11-19 | 14.9 u | 43 | 39 | 4 | €0,07 | €0,00 (0x) | **€0,07** | 0.05% | €-0,43 | €-0,36 | -0.24% |
| bitvavo - kraken | €150,00 | 2026-11-20 | 14.5 u | 12 | 11 | 1 | €0,87 | €0,00 (0x) | **€0,87** | 0.58% | €0,98 | €1,85 | 1.23% |
| bitvavo - kraken | €200,00 | 2026-11-19 | 14.9 u | 43 | 37 | 6 | €0,16 | €0,00 (0x) | **€0,16** | 0.08% | €-0,58 | €-0,42 | -0.21% |
| bitvavo - kraken | €200,00 | 2026-11-20 | 14.5 u | 12 | 11 | 1 | €0,78 | €0,00 (0x) | **€0,78** | 0.39% | €1,31 | €2,09 | 1.04% |
| bitvavo - kraken | €2.000,00 | 2026-11-19 | 14.9 u | 43 | 28 | 15 | €11,33 | €6,07 (15x) | **€5,26** | 0.26% | €-5,71 | €-0,45 | -0.02% |
| bitvavo - kraken | €2.000,00 | 2026-11-20 | 14.5 u | 12 | 9 | 3 | €17,98 | €1,64 (3x) | **€16,34** | 0.82% | €13,33 | €29,67 | 1.48% |
| bitvavo - kraken | €5.000,00 | 2026-11-19 | 14.9 u | 43 | 23 | 20 | €29,68 | €14,63 (23x) | **€15,05** | 0.30% | €-14,32 | €0,74 | 0.01% |
| bitvavo - kraken | €5.000,00 | 2026-11-20 | 14.5 u | 12 | 2 | 10 | €47,42 | €10,70 (12x) | **€36,72** | 0.73% | €33,59 | €70,30 | 1.41% |
| gate - kucoin | €100,00 | 2026-11-19 | 14.9 u | 25 | 25 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,17 | €-0,17 | -0.17% |
| gate - kucoin | €100,00 | 2026-11-20 | 14.5 u | 24 | 22 | 2 | €0,13 | €0,00 (1x) | **€0,13** | 0.13% | €1,27 | €1,40 | 1.40% |
| gate - kucoin | €150,00 | 2026-11-19 | 14.9 u | 25 | 25 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,25 | €-0,25 | -0.17% |
| gate - kucoin | €150,00 | 2026-11-20 | 14.5 u | 24 | 20 | 4 | €0,41 | €0,02 (2x) | **€0,39** | 0.26% | €1,91 | €2,30 | 1.53% |
| gate - kucoin | €200,00 | 2026-11-19 | 14.9 u | 25 | 17 | 8 | €0,23 | €0,00 (0x) | **€0,23** | 0.12% | €-0,33 | €-0,10 | -0.05% |
| gate - kucoin | €200,00 | 2026-11-20 | 14.5 u | 24 | 13 | 11 | €0,91 | €0,02 (2x) | **€0,89** | 0.45% | €2,54 | €3,43 | 1.72% |
| gate - kucoin | €2.000,00 | 2026-11-19 | 14.9 u | 25 | 10 | 15 | €3,16 | €2,19 (12x) | **€0,97** | 0.05% | €-3,32 | €-2,35 | -0.12% |
| gate - kucoin | €2.000,00 | 2026-11-20 | 14.5 u | 24 | 8 | 16 | €9,66 | €1,35 (10x) | **€8,31** | 0.42% | €25,49 | €33,80 | 1.69% |
| gate - kucoin | €5.000,00 | 2026-11-19 | 14.9 u | 25 | 6 | 19 | €12,14 | €4,84 (19x) | **€7,30** | 0.15% | €-8,32 | €-1,02 | -0.02% |
| gate - kucoin | €5.000,00 | 2026-11-20 | 14.5 u | 24 | 5 | 19 | €24,84 | €6,09 (18x) | **€18,76** | 0.38% | €63,97 | €82,73 | 1.65% |

- bitstamp - kraken, €100,00: munten SKY; bruto zonder voorraadgrens zou €22,30 zijn, met voorraad €1,18 (GEZIEN boek, GOK model).
- bitstamp - kraken, €150,00: munten SKY; bruto zonder voorraadgrens zou €21,71 zijn, met voorraad €1,78 (GEZIEN boek, GOK model).
- bitstamp - kraken, €200,00: munten SKY; bruto zonder voorraadgrens zou €21,12 zijn, met voorraad €2,37 (GEZIEN boek, GOK model).
- bitstamp - kraken, €2.000,00: munten SKY; bruto zonder voorraadgrens zou €11,71 zijn, met voorraad €11,71 (GEZIEN boek, GOK model).
- bitstamp - kraken, €5.000,00: munten SKY; bruto zonder voorraadgrens zou €11,71 zijn, met voorraad €11,71 (GEZIEN boek, GOK model).
- bitvavo - kraken, €100,00: munten AVA, DYM, GMT, KERNEL, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €1.083,83 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitvavo - kraken, €150,00: munten AVA, DYM, GMT, KERNEL, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €1.083,83 zijn, met voorraad €0,94 (GEZIEN boek, GOK model).
- bitvavo - kraken, €200,00: munten AVA, DYM, GMT, KERNEL, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €1.083,36 zijn, met voorraad €0,94 (GEZIEN boek, GOK model).
- bitvavo - kraken, €2.000,00: munten AVA, DYM, GMT, KERNEL, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €1.060,13 zijn, met voorraad €29,31 (GEZIEN boek, GOK model).
- bitvavo - kraken, €5.000,00: munten AVA, DYM, GMT, KERNEL, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €1.024,91 zijn, met voorraad €77,10 (GEZIEN boek, GOK model).
- gate - kucoin, €100,00: munten ALKIMI, AVAIL, CHR, CYBER, ERG, FTT, IKA, IR, KYO, LUNC, NIM, OVR, RARI, USTC, VERONA; bruto zonder voorraadgrens zou €182,45 zijn, met voorraad €0,13 (GEZIEN boek, GOK model).
- gate - kucoin, €150,00: munten ALKIMI, AVAIL, CHR, CYBER, ERG, FTT, IKA, IR, KYO, LUNC, NIM, OVR, RARI, USTC, VERONA; bruto zonder voorraadgrens zou €182,30 zijn, met voorraad €0,41 (GEZIEN boek, GOK model).
- gate - kucoin, €200,00: munten ALKIMI, AVAIL, CHR, CYBER, ERG, FTT, IKA, IR, KYO, LUNC, NIM, OVR, RARI, USTC, VERONA; bruto zonder voorraadgrens zou €182,21 zijn, met voorraad €1,14 (GEZIEN boek, GOK model).
- gate - kucoin, €2.000,00: munten ALKIMI, AVAIL, CHR, CYBER, ERG, FTT, IKA, IR, KYO, LUNC, NIM, OVR, RARI, USTC, VERONA; bruto zonder voorraadgrens zou €179,85 zijn, met voorraad €12,82 (GEZIEN boek, GOK model).
- gate - kucoin, €5.000,00: munten ALKIMI, AVAIL, CHR, CYBER, ERG, FTT, IKA, IR, KYO, LUNC, NIM, OVR, RARI, USTC, VERONA; bruto zonder voorraadgrens zou €173,32 zijn, met voorraad €36,98 (GEZIEN boek, GOK model).

### Met minstens één grijze beurs (de 5 paren met de meeste bruto winst)

| Beurspaar | Inleg | Dag | Gemeten | Kansen | Gemist (geen voorraad) | Kleiner door voorraad | Bruto winst | Kosten terugschuiven | **Netto handel (bruto min kosten)** | Rendement handel | Koerseffect voorraad | Netto met koerseffect | Rendement met koerseffect |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| htx - xt | €100,00 | 2026-11-19 | 14.9 u | 18 | 18 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,59 | €-0,59 | -0.59% |
| htx - xt | €100,00 | 2026-11-20 | 14.5 u | 11 | 11 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,30 | €-1,30 | -1.30% |
| htx - xt | €150,00 | 2026-11-19 | 14.9 u | 18 | 18 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,89 | €-0,89 | -0.59% |
| htx - xt | €150,00 | 2026-11-20 | 14.5 u | 11 | 11 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,94 | €-1,94 | -1.30% |
| htx - xt | €200,00 | 2026-11-19 | 14.9 u | 18 | 18 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,18 | €-1,18 | -0.59% |
| htx - xt | €200,00 | 2026-11-20 | 14.5 u | 11 | 11 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,59 | €-2,59 | -1.30% |
| htx - xt | €2.000,00 | 2026-11-19 | 14.9 u | 18 | 5 | 13 | €7,21 | €5,27 (12x) | **€1,93** | 0.10% | €-11,86 | €-9,93 | -0.50% |
| htx - xt | €2.000,00 | 2026-11-20 | 14.5 u | 11 | 1 | 10 | €13,98 | €2,04 (6x) | **€11,93** | 0.60% | €-25,44 | €-13,51 | -0.68% |
| htx - xt | €5.000,00 | 2026-11-19 | 14.9 u | 18 | 5 | 12 | €16,31 | €7,10 (14x) | **€9,22** | 0.18% | €-29,58 | €-20,36 | -0.41% |
| htx - xt | €5.000,00 | 2026-11-20 | 14.5 u | 11 | 0 | 11 | €34,48 | €4,75 (9x) | **€29,73** | 0.59% | €-64,25 | €-34,52 | -0.69% |
| kucoin - xt | €100,00 | 2026-11-19 | 14.9 u | 13 | 13 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,06 | €-0,06 | -0.06% |
| kucoin - xt | €100,00 | 2026-11-20 | 14.5 u | 4 | 4 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,40 | €-1,40 | -1.40% |
| kucoin - xt | €150,00 | 2026-11-19 | 14.9 u | 13 | 13 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,09 | €-0,09 | -0.06% |
| kucoin - xt | €150,00 | 2026-11-20 | 14.5 u | 4 | 4 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,11 | €-2,11 | -1.40% |
| kucoin - xt | €200,00 | 2026-11-19 | 14.9 u | 13 | 11 | 2 | €0,17 | €0,00 (0x) | **€0,17** | 0.09% | €-0,11 | €0,06 | 0.03% |
| kucoin - xt | €200,00 | 2026-11-20 | 14.5 u | 4 | 3 | 1 | €0,18 | €0,00 (0x) | **€0,18** | 0.09% | €-2,81 | €-2,63 | -1.32% |
| kucoin - xt | €2.000,00 | 2026-11-19 | 14.9 u | 13 | 3 | 10 | €11,08 | €5,50 (11x) | **€5,58** | 0.28% | €-1,12 | €4,46 | 0.22% |
| kucoin - xt | €2.000,00 | 2026-11-20 | 14.5 u | 4 | 0 | 4 | €4,66 | €2,41 (4x) | **€2,25** | 0.11% | €-27,84 | €-25,59 | -1.28% |
| kucoin - xt | €5.000,00 | 2026-11-19 | 14.9 u | 13 | 3 | 9 | €23,53 | €5,50 (11x) | **€18,04** | 0.36% | €-2,83 | €15,21 | 0.30% |
| kucoin - xt | €5.000,00 | 2026-11-20 | 14.5 u | 4 | 0 | 4 | €13,61 | €3,46 (5x) | **€10,16** | 0.20% | €-69,95 | €-59,79 | -1.20% |
| bitget - xt | €100,00 | 2026-11-19 | 14.9 u | 13 | 13 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €2,07 | €2,07 | 2.07% |
| bitget - xt | €100,00 | 2026-11-20 | 14.5 u | 5 | 5 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,46 | €-3,46 | -3.46% |
| bitget - xt | €150,00 | 2026-11-19 | 14.9 u | 13 | 13 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €3,11 | €3,11 | 2.07% |
| bitget - xt | €150,00 | 2026-11-20 | 14.5 u | 5 | 5 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-5,19 | €-5,19 | -3.46% |
| bitget - xt | €200,00 | 2026-11-19 | 14.9 u | 13 | 9 | 4 | €0,50 | €0,01 (3x) | **€0,50** | 0.25% | €4,15 | €4,64 | 2.32% |
| bitget - xt | €200,00 | 2026-11-20 | 14.5 u | 5 | 5 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-6,92 | €-6,92 | -3.46% |
| bitget - xt | €2.000,00 | 2026-11-19 | 14.9 u | 13 | 4 | 9 | €9,96 | €1,96 (11x) | **€8,00** | 0.40% | €41,46 | €49,46 | 2.47% |
| bitget - xt | €2.000,00 | 2026-11-20 | 14.5 u | 5 | 0 | 5 | €5,94 | €2,06 (6x) | **€3,88** | 0.19% | €-69,13 | €-65,24 | -3.26% |
| bitget - xt | €5.000,00 | 2026-11-19 | 14.9 u | 13 | 4 | 8 | €19,47 | €1,85 (10x) | **€17,62** | 0.35% | €103,65 | €121,27 | 2.43% |
| bitget - xt | €5.000,00 | 2026-11-20 | 14.5 u | 5 | 0 | 5 | €12,98 | €2,06 (6x) | **€10,93** | 0.22% | €-172,90 | €-161,97 | -3.24% |
| gate - htx | €100,00 | 2026-11-19 | 14.9 u | 19 | 19 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,78 | €-0,78 | -0.78% |
| gate - htx | €100,00 | 2026-11-20 | 14.5 u | 16 | 16 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,07 | €-2,07 | -2.07% |
| gate - htx | €150,00 | 2026-11-19 | 14.9 u | 19 | 19 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,17 | €-1,17 | -0.78% |
| gate - htx | €150,00 | 2026-11-20 | 14.5 u | 16 | 16 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,11 | €-3,11 | -2.07% |
| gate - htx | €200,00 | 2026-11-19 | 14.9 u | 19 | 19 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,56 | €-1,56 | -0.78% |
| gate - htx | €200,00 | 2026-11-20 | 14.5 u | 16 | 16 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-4,15 | €-4,15 | -2.07% |
| gate - htx | €2.000,00 | 2026-11-19 | 14.9 u | 19 | 7 | 12 | €5,99 | €3,58 (10x) | **€2,40** | 0.12% | €-15,69 | €-13,28 | -0.66% |
| gate - htx | €2.000,00 | 2026-11-20 | 14.5 u | 16 | 2 | 14 | €11,25 | €2,80 (11x) | **€8,45** | 0.42% | €-41,04 | €-32,59 | -1.63% |
| gate - htx | €5.000,00 | 2026-11-19 | 14.9 u | 19 | 6 | 11 | €14,83 | €5,58 (13x) | **€9,25** | 0.19% | €-39,16 | €-29,91 | -0.60% |
| gate - htx | €5.000,00 | 2026-11-20 | 14.5 u | 16 | 2 | 14 | €27,99 | €4,14 (13x) | **€23,84** | 0.48% | €-103,21 | €-79,37 | -1.59% |
| htx - kucoin | €100,00 | 2026-11-19 | 14.9 u | 16 | 16 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,61 | €-2,61 | -2.61% |
| htx - kucoin | €100,00 | 2026-11-20 | 14.5 u | 22 | 22 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,49 | €-2,49 | -2.49% |
| htx - kucoin | €150,00 | 2026-11-19 | 14.9 u | 16 | 16 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,92 | €-3,92 | -2.61% |
| htx - kucoin | €150,00 | 2026-11-20 | 14.5 u | 22 | 22 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,74 | €-3,74 | -2.49% |
| htx - kucoin | €200,00 | 2026-11-19 | 14.9 u | 16 | 16 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-5,22 | €-5,22 | -2.61% |
| htx - kucoin | €200,00 | 2026-11-20 | 14.5 u | 22 | 22 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-4,98 | €-4,98 | -2.49% |
| htx - kucoin | €2.000,00 | 2026-11-19 | 14.9 u | 16 | 7 | 9 | €3,70 | €0,86 (5x) | **€2,83** | 0.14% | €-52,17 | €-49,34 | -2.47% |
| htx - kucoin | €2.000,00 | 2026-11-20 | 14.5 u | 22 | 11 | 11 | €8,28 | €1,20 (6x) | **€7,08** | 0.35% | €-49,80 | €-42,72 | -2.14% |
| htx - kucoin | €5.000,00 | 2026-11-19 | 14.9 u | 16 | 3 | 13 | €11,48 | €4,43 (13x) | **€7,05** | 0.14% | €-130,52 | €-123,47 | -2.47% |
| htx - kucoin | €5.000,00 | 2026-11-20 | 14.5 u | 22 | 5 | 17 | €23,77 | €4,76 (14x) | **€19,01** | 0.38% | €-124,29 | €-105,28 | -2.11% |

- htx - xt, €100,00: munten BSV, CARV, CBK, LUNC, MEME, SEI, XCH, XDC, XMR; bruto zonder voorraadgrens zou €203,52 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - xt, €150,00: munten BSV, CARV, CBK, LUNC, MEME, SEI, XCH, XDC, XMR; bruto zonder voorraadgrens zou €203,52 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - xt, €200,00: munten BSV, CARV, CBK, LUNC, MEME, SEI, XCH, XDC, XMR; bruto zonder voorraadgrens zou €203,52 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - xt, €2.000,00: munten BSV, CARV, CBK, LUNC, MEME, SEI, XCH, XDC, XMR; bruto zonder voorraadgrens zou €201,74 zijn, met voorraad €21,18 (GEZIEN boek, GOK model).
- htx - xt, €5.000,00: munten BSV, CARV, CBK, LUNC, MEME, SEI, XCH, XDC, XMR; bruto zonder voorraadgrens zou €199,63 zijn, met voorraad €50,79 (GEZIEN boek, GOK model).
- kucoin - xt, €100,00: munten DAG, ENSO, FIGHT, LUNC, XMR; bruto zonder voorraadgrens zou €677,33 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- kucoin - xt, €150,00: munten DAG, ENSO, FIGHT, LUNC, XMR; bruto zonder voorraadgrens zou €677,33 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- kucoin - xt, €200,00: munten DAG, ENSO, FIGHT, LUNC, XMR; bruto zonder voorraadgrens zou €677,33 zijn, met voorraad €0,35 (GEZIEN boek, GOK model).
- kucoin - xt, €2.000,00: munten DAG, ENSO, FIGHT, LUNC, XMR; bruto zonder voorraadgrens zou €673,85 zijn, met voorraad €15,74 (GEZIEN boek, GOK model).
- kucoin - xt, €5.000,00: munten DAG, ENSO, FIGHT, LUNC, XMR; bruto zonder voorraadgrens zou €668,85 zijn, met voorraad €37,15 (GEZIEN boek, GOK model).
- bitget - xt, €100,00: munten ENSO, KOR, KUB, LUNC, YB; bruto zonder voorraadgrens zou €788,49 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - xt, €150,00: munten ENSO, KOR, KUB, LUNC, YB; bruto zonder voorraadgrens zou €788,49 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - xt, €200,00: munten ENSO, KOR, KUB, LUNC, YB; bruto zonder voorraadgrens zou €788,06 zijn, met voorraad €0,50 (GEZIEN boek, GOK model).
- bitget - xt, €2.000,00: munten ENSO, KOR, KUB, LUNC, YB; bruto zonder voorraadgrens zou €783,09 zijn, met voorraad €15,90 (GEZIEN boek, GOK model).
- bitget - xt, €5.000,00: munten ENSO, KOR, KUB, LUNC, YB; bruto zonder voorraadgrens zou €776,50 zijn, met voorraad €32,45 (GEZIEN boek, GOK model).
- gate - htx, €100,00: munten BSV, CBK, CRTS, KAS, LAT, LUNC, MEME, MOVR, SEI, WARD, WLD; bruto zonder voorraadgrens zou €150,84 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- gate - htx, €150,00: munten BSV, CBK, CRTS, KAS, LAT, LUNC, MEME, MOVR, SEI, WARD, WLD; bruto zonder voorraadgrens zou €150,84 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- gate - htx, €200,00: munten BSV, CBK, CRTS, KAS, LAT, LUNC, MEME, MOVR, SEI, WARD, WLD; bruto zonder voorraadgrens zou €150,84 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- gate - htx, €2.000,00: munten BSV, CBK, CRTS, KAS, LAT, LUNC, MEME, MOVR, SEI, WARD, WLD; bruto zonder voorraadgrens zou €147,74 zijn, met voorraad €17,24 (GEZIEN boek, GOK model).
- gate - htx, €5.000,00: munten BSV, CBK, CRTS, KAS, LAT, LUNC, MEME, MOVR, SEI, WARD, WLD; bruto zonder voorraadgrens zou €143,41 zijn, met voorraad €42,82 (GEZIEN boek, GOK model).
- htx - kucoin, €100,00: munten BSV, CHIP, FET, LAT, LUNC, MEME, MOVR, ONE, SOMI, WAN, WARD, WLD, XCH, XEC, XMR; bruto zonder voorraadgrens zou €135,76 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - kucoin, €150,00: munten BSV, CHIP, FET, LAT, LUNC, MEME, MOVR, ONE, SOMI, WAN, WARD, WLD, XCH, XEC, XMR; bruto zonder voorraadgrens zou €135,76 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - kucoin, €200,00: munten BSV, CHIP, FET, LAT, LUNC, MEME, MOVR, ONE, SOMI, WAN, WARD, WLD, XCH, XEC, XMR; bruto zonder voorraadgrens zou €135,76 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - kucoin, €2.000,00: munten BSV, CHIP, FET, LAT, LUNC, MEME, MOVR, ONE, SOMI, WAN, WARD, WLD, XCH, XEC, XMR; bruto zonder voorraadgrens zou €134,89 zijn, met voorraad €11,98 (GEZIEN boek, GOK model).
- htx - kucoin, €5.000,00: munten BSV, CHIP, FET, LAT, LUNC, MEME, MOVR, ONE, SOMI, WAN, WARD, WLD, XCH, XEC, XMR; bruto zonder voorraadgrens zou €133,58 zijn, met voorraad €35,24 (GEZIEN boek, GOK model).

### Andere keuzes bij bitvavo - kraken (netto handel, alle dagen samen; GOK)

| Keuze | Inleg | Kansen | Gemist | Bruto winst | Kosten terugschuiven | Netto handel |
|---|---|---|---|---|---|---|
| standaard (schuifdrempel 25%, kostengrens 1%) | €150,00 | 55 | 50 | €0,94 | €0,00 | **€0,94** |
| standaard (schuifdrempel 25%, kostengrens 1%) | €2.000,00 | 55 | 37 | €29,31 | €7,71 | **€21,60** |
| schuifdrempel 10% | €150,00 | 55 | 50 | €0,94 | €0,00 | **€0,94** |
| schuifdrempel 10% | €2.000,00 | 55 | 37 | €29,14 | €6,69 | **€22,45** |
| schuifdrempel 40% | €150,00 | 55 | 50 | €0,94 | €0,00 | **€0,94** |
| schuifdrempel 40% | €2.000,00 | 55 | 34 | €33,99 | €9,65 | **€24,34** |
| kostengrens 2% (achteraf vergeleken) | €150,00 | 55 | 50 | €0,94 | €0,00 | **€0,94** |
| kostengrens 2% (achteraf vergeleken) | €2.000,00 | 55 | 25 | €32,43 | €25,33 | **€7,10** |
| kostengrens 5% (achteraf vergeleken) | €150,00 | 55 | 50 | €0,94 | €1,00 | **€-0,06** |
| kostengrens 5% (achteraf vergeleken) | €2.000,00 | 55 | 25 | €32,43 | €25,33 | **€7,10** |
| alleen MERL en KERNEL (meer voorraad per munt, achteraf gekozen) | €150,00 | 19 | 17 | €2,05 | €0,00 | **€2,05** |
| alleen MERL en KERNEL (meer voorraad per munt, achteraf gekozen) | €2.000,00 | 19 | 9 | €78,49 | €7,90 | **€70,59** |

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

- Opnamekosten bij de echte kansen: 96 van een netwerk dat aan beide kanten open is, 93 van de beurs zelf (laagste open netwerk), 39 geschat uit wat andere beurzen voor die munt vragen (GOK). Onbekende opnamekosten tellen niet als echte kans.
- Netwerk: KuCoin, Gate, Bitget, HTX, XT, Bitstamp, Bitvavo en Poloniex geven hun netwerken per munt. Als beide beurzen dat doen en de namen te koppelen zijn, moet er een netwerk zijn dat aan beide kanten open is. Anders is het netwerk "niet te koppelen" en telt de kans mee (staat apart in de trechter).
- De duur is gemeten in stappen van ±20 seconden; een kans kan een paar rondes eerder begonnen zijn dan we zagen.
- Takerkosten: uit de API waar die ze per paar geeft, anders het standaardtarief uit de README (deels GOK).
- Laatste run: 15 beurzen antwoordden, 2289 munt-quote-paren op minstens twee beurzen (GEZIEN).
