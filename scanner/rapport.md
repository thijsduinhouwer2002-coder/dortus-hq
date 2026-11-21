# Rapport koersverschil-scanner

Gemaakt 2026-11-21 02:01 UTC uit 21 runs, samen ±39.8 uur gemeten (GEZIEN).
Echte kans = winst na alle kosten (opnamekosten bekend), opnemen en storten open (en een netwerk dat aan beide kanten open is, als de beurzen dat geven), minstens €100,00 op het boek, minstens 2 minuten blijven staan, geen andere munt met dezelfde naam.
**Vergund** = beide beurzen hebben een MiCA-vergunning (ESMA-register), vaak via een EU-dochter die minder munten kan hebben dan de wereldwijde API die we meten (GOK). **Grijs** = minstens één beurs zonder vergunning (MEXC, Bitget, HTX, Poloniex, XT, Bitfinex, Binance). Zie README.md.
**Kraken-tarief:** Kraken rekent 0,80% taker op munt tegen EUR, USD, USDT of USDC (GEZIEN, kraken.com/pro/fees, laagste trede); de scanner rekende tot 19 nov met 0,40%. 399 opgeslagen kansen met Kraken uit die runs zijn hier **opnieuw doorgerekend met 0,80%** (GOK-benadering: 0,40% van de inzet aan de Kraken-kant extra op elk gemeten punt van het boek; het boek zelf is niet bewaard). 233 houden daarna nog winst op het boek. Dat ze met hogere kosten ook korter bleven staan, telt niet mee (dus eerder te gunstig).

## Hoeveel wordt er gecontroleerd? (GEZIEN, stand.jsonl)

Per ronde (mediaan over 477 metingen): 1142 kandidaten (verschil op de ticker groter dan de takerkosten), 120 met het orderboek gecontroleerd, 2 nog nooit gecontroleerd (0%).
Bijna alle kandidaten komen aan de beurt; de aantallen hieronder missen weinig.

## Trechter (GEZIEN, eigen metingen)

| Stap | Alle beurzen | Alleen MiCA-beurzen | Met minstens één grijze beurs |
|---|---|---|---|
| Verschillen met winst op het boek na alle kosten | 37221 | 5280 | 31941 |
| ...waarvan opnemen of storten dicht | 7018 | 772 | 6246 |
| ...waarvan status onbekend (beurs geeft het niet openbaar) | 22472 | 3789 | 18683 |
| Opnemen en storten open | 7731 | 719 | 7012 |
| ...en geen netwerk dat aan beide kanten open is: valt af | 170 | 16 | 154 |
| ...en opnamekosten onbekend: valt af | 2 | 2 | 0 |
| ...en minstens €100,00 op het boek | 2029 | 409 | 1620 |
| ...en minstens 2 minuten blijven staan | 560 | 163 | 397 |
| ...en geen andere munt met dezelfde naam | 521 | 146 | 375 |
|    ...waarvan contractadres bekend en gelijk | 71 | 28 | 43 |
|    ...waarvan contractadres onbekend (telt mee, kan een andere munt zijn) | 450 | 118 | 332 |
|    ...waarvan netwerk gekoppeld en open | 328 | 67 | 261 |
|    ...waarvan netwerk niet te koppelen (telt mee) | 193 | 79 | 114 |
| **Echte kansen** (zelfde munt overlappend in de tijd samengevoegd, beste beurspaar telt) | 336 | 145 | 234 |
| Ter vergelijking: zelfde eisen, maar opnamestatus onbekend (niet meegeteld) | 1331 | 297 | 1138 |

## Echte kansen per dag (GEZIEN)

| Dag | Echt, alleen MiCA | Echt, met grijs | Mediane winst per kans bij €500 (MiCA / grijs) | Mediane duur |
|---|---|---|---|---|
| 2026-11-19 | 49 | 86 | €2,00 / €1,21 | 5.3 min |
| 2026-11-20 | 58 | 136 | €0,68 / €1,13 | 6.3 min |
| 2026-11-21 | 0 | 7 | geen / €1,18 | 7.0 min |
| Totaal | 107 | 229 | €1,16 / €1,18 | 6.0 min |

## Beste munten (GEZIEN)

| | Soort | Kansen | Som winst bij €500 per kans |
|---|---|---|---|
| MERL-EUR | vergund | 19 | €287,01 |
| LUNC-USDT | grijs | 14 | €81,45 |
| USTC-USDT | grijs | 13 | €51,00 |
| KERNEL-EUR | vergund | 1 | €47,33 |
| MEME-USDT | grijs | 1 | €37,90 |
| KYO-USDT | vergund | 5 | €30,94 |
| BARD-USDT | grijs | 4 | €24,39 |
| SKY-USD | vergund | 2 | €21,52 |
| BSV-USDT | grijs | 16 | €20,97 |
| LAT-USDT | grijs | 3 | €17,59 |

## Beste beursparen (kopen op > verkopen op) (GEZIEN)

| | Soort | Kansen | Som winst bij €500 per kans |
|---|---|---|---|
| bitvavo > kraken | vergund | 57 | €380,22 |
| bitget > htx | grijs | 49 | €113,76 |
| gate > kucoin | vergund | 25 | €68,85 |
| kucoin > htx | grijs | 29 | €63,91 |
| kucoin > bitget | grijs | 21 | €57,68 |
| bitget > xt | grijs | 13 | €44,44 |
| bitget > kucoin | grijs | 19 | €33,49 |
| bitget > gate | grijs | 12 | €32,74 |
| gate > xt | grijs | 4 | €28,67 |
| htx > xt | grijs | 5 | €23,18 |

Beurzen die het vaakst meedoen (koop of verkoop): bitget (grijs) 142, kucoin 136, htx (grijs) 114, kraken 86, gate 79, bitvavo 58, xt (grijs) 41, poloniex (grijs) 14 (GEZIEN).

## Hoeveel kansen blijven staan terwijl je geld schuift? (GEZIEN, duur uit eigen metingen)

Wie geen voorraad op beide beurzen heeft, moet kopen, de munt opnemen, wachten tot hij binnen is en dan verkopen. Hoe lang dat duurt verschilt per munt en netwerk: een paar minuten (snelle ketens) tot een uur of meer (Bitcoin, beurzen die opnames met de hand keuren) (GOK, niet per munt gemeten).

| Overmaaktijd | Alle beurzen | Alleen MiCA-beurzen | Met minstens één grijze beurs |
|---|---|---|---|
| 5 min | 197 van 336 (59%) | 85 van 145 (59%) | 138 van 234 (59%) |
| 10 min | 120 van 336 (36%) | 54 van 145 (37%) | 86 van 234 (37%) |
| 30 min | 63 van 336 (19%) | 33 van 145 (23%) | 46 van 234 (20%) |
| 60 min | 32 van 336 (10%) | 22 van 145 (15%) | 23 van 234 (10%) |

## Wat zou het opleveren over 3 maanden? (GOK, doorgetrokken uit de metingen)

Gemeten over ±39.8 uur (GEZIEN), doorgetrokken naar 90 dagen (GOK: aanname dat de week die we maten gewoon is).

| Beurzen | Inleg | Model | Kansen per uur | Per kans (mediaan) | 3 maanden |
|---|---|---|---|---|---|
| Alleen MiCA | €2.000,00 | bovengrens: elke kans, geld overal tegelijk | 3.65 | €1,64 | €12.931,75 |
| Alleen MiCA | €2.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 1.43 | €2,92 | €35.724,15 |
| Alleen MiCA | €5.000,00 | bovengrens: elke kans, geld overal tegelijk | 3.65 | €2,18 | €17.142,28 |
| Alleen MiCA | €5.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 1.43 | €3,27 | €56.219,53 |
| Alle (met grijs) | €2.000,00 | bovengrens: elke kans, geld overal tegelijk | 8.45 | €1,48 | €27.005,54 |
| Alle (met grijs) | €2.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 1.43 | €2,92 | €35.724,15 |
| Alle (met grijs) | €5.000,00 | bovengrens: elke kans, geld overal tegelijk | 8.45 | €1,66 | €30.244,42 |
| Alle (met grijs) | €5.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 1.43 | €3,27 | €56.219,53 |

Bovengrens: elke kans met de helft van de inleg aan elke kant, alsof het geld op alle beurzen tegelijk staat (kan in het echt niet). Beste beurspaar: het paar is **achteraf** gekozen uit de metingen (vooraf kiezen levert minder op), en het model neemt aan dat je van elke munt al voorraad op de verkoopbeurs hebt.

Waarom dit te rooskleurig is (GOK): elke kans wordt maar één keer geteld met het mediane boek, maar andere bots pakken hem ook; de munt die je als voorraad aanhoudt kan dalen; na een paar kansen moet de voorraad terug (opnamekosten en tijd); minimale opname- en ordergroottes tellen niet mee; en een kans die we 2 minuten zagen staan, staat er niet per se nog als jouw order binnenkomt. Waarom het te somber kan zijn: niet alle kandidaten zijn gecontroleerd, en met voorraad op beide beurzen kun je dezelfde kans vaker pakken als het boek zich aanvult; dat telt hier niet mee.

## Wat houd je echt over? Voorraad op twee beurzen (simulatie)

Per beurspaar: geld en munten op beide beurzen, elke echte kans uitgevoerd tegen het boek zoals gemeten (niet meer dan de ruimte op het boek en niet meer dan de voorraad op die beurs), terugschuiven als een kant leeg dreigt te raken (met opnamekosten en tijd onderweg), en het koerseffect van de aangehouden munten apart. Netto = bruto min kosten terugschuiven plus koerseffect. **Gemeten** (GEZIEN): de kansen, het boek en de koersen; **de rest is een rekenmodel** (GOK, aannames onder de tabel). Geen advies.

**Met €150: netto €0,59 per dag op bitstamp - kraken (koerseffect erbovenop €-1,15), €-0,00 per dag op bitstamp - kucoin (koerseffect erbovenop €0,10), €0,25 per dag op bitvavo - kraken (koerseffect erbovenop €-1,36), €0,04 per dag op gate - kucoin (koerseffect erbovenop €-0,47), €0,01 per dag op kraken - kucoin (koerseffect erbovenop €0,11) (GOK: netto handel, rekenmodel op ±13.2 uur meting per dag, alleen MiCA).** "Per dag" is hier gemiddeld over 3 gemeten dagen achter elkaar; de eerste begint met een gelijk verdeelde voorraad; aan het eind staat de voorraad scheef, dus een volgende dag levert waarschijnlijk minder op, tenzij kansen de andere kant op hem terugbrengen (GOK).

### Alleen MiCA-beurzen (alle paren met echte kansen)

| Beurspaar | Inleg | Dag | Gemeten | Kansen | Gemist (geen voorraad) | Kleiner door voorraad | Bruto winst | Kosten terugschuiven | **Netto handel (bruto min kosten)** | Rendement handel | Koerseffect voorraad | Netto met koerseffect | Rendement met koerseffect |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| bitstamp - kraken | €100,00 | 2026-11-19 | 14.9 u | 2 | 1 | 1 | €1,18 | €0,00 (0x) | **€1,18** | 1.18% | €0,63 | €1,81 | 1.81% |
| bitstamp - kraken | €100,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,38 | €-3,38 | -3.38% |
| bitstamp - kraken | €100,00 | 2026-11-21 | 2.0 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,46 | €0,46 | 0.46% |
| bitstamp - kraken | €150,00 | 2026-11-19 | 14.9 u | 2 | 1 | 1 | €1,78 | €0,00 (0x) | **€1,78** | 1.18% | €0,94 | €2,72 | 1.81% |
| bitstamp - kraken | €150,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-5,07 | €-5,07 | -3.38% |
| bitstamp - kraken | €150,00 | 2026-11-21 | 2.0 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,70 | €0,70 | 0.46% |
| bitstamp - kraken | €200,00 | 2026-11-19 | 14.9 u | 2 | 1 | 1 | €2,37 | €0,00 (0x) | **€2,37** | 1.18% | €1,25 | €3,62 | 1.81% |
| bitstamp - kraken | €200,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-6,76 | €-6,76 | -3.38% |
| bitstamp - kraken | €200,00 | 2026-11-21 | 2.0 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,93 | €0,93 | 0.46% |
| bitstamp - kraken | €2.000,00 | 2026-11-19 | 14.9 u | 2 | 1 | 0 | €11,71 | €0,00 (0x) | **€11,71** | 0.59% | €12,53 | €24,24 | 1.21% |
| bitstamp - kraken | €2.000,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-67,63 | €-67,63 | -3.38% |
| bitstamp - kraken | €2.000,00 | 2026-11-21 | 2.0 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €9,29 | €9,29 | 0.46% |
| bitstamp - kraken | €5.000,00 | 2026-11-19 | 14.9 u | 2 | 1 | 0 | €11,71 | €0,00 (0x) | **€11,71** | 0.23% | €31,33 | €43,04 | 0.86% |
| bitstamp - kraken | €5.000,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-169,08 | €-169,08 | -3.38% |
| bitstamp - kraken | €5.000,00 | 2026-11-21 | 2.0 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €23,23 | €23,23 | 0.46% |
| bitstamp - kucoin | €100,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,14 | €0,14 | 0.14% |
| bitstamp - kucoin | €100,00 | 2026-11-20 | 22.8 u | 1 | 0 | 1 | €0,01 | €0,01 (1x) | **€-0,00** | -0.00% | €0,09 | €0,08 | 0.08% |
| bitstamp - kucoin | €100,00 | 2026-11-21 | 2.0 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,02 | €-0,02 | -0.02% |
| bitstamp - kucoin | €150,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,21 | €0,21 | 0.14% |
| bitstamp - kucoin | €150,00 | 2026-11-20 | 22.8 u | 1 | 0 | 1 | €0,01 | €0,01 (1x) | **€-0,00** | -0.00% | €0,13 | €0,13 | 0.09% |
| bitstamp - kucoin | €150,00 | 2026-11-21 | 2.0 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,02 | €-0,02 | -0.02% |
| bitstamp - kucoin | €200,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,27 | €0,27 | 0.14% |
| bitstamp - kucoin | €200,00 | 2026-11-20 | 22.8 u | 1 | 0 | 1 | €0,01 | €0,01 (1x) | **€0,00** | 0.00% | €0,18 | €0,18 | 0.09% |
| bitstamp - kucoin | €200,00 | 2026-11-21 | 2.0 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,03 | €-0,03 | -0.02% |
| bitstamp - kucoin | €2.000,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €2,74 | €2,74 | 0.14% |
| bitstamp - kucoin | €2.000,00 | 2026-11-20 | 22.8 u | 1 | 0 | 1 | €0,10 | €1,01 (2x) | **€-0,91** | -0.05% | €1,76 | €0,85 | 0.04% |
| bitstamp - kucoin | €2.000,00 | 2026-11-21 | 2.0 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,33 | €-0,33 | -0.02% |
| bitstamp - kucoin | €5.000,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €6,86 | €6,86 | 0.14% |
| bitstamp - kucoin | €5.000,00 | 2026-11-20 | 22.8 u | 1 | 0 | 1 | €0,25 | €1,01 (2x) | **€-0,76** | -0.02% | €4,39 | €3,63 | 0.07% |
| bitstamp - kucoin | €5.000,00 | 2026-11-21 | 2.0 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,82 | €-0,82 | -0.02% |
| bitvavo - kraken | €100,00 | 2026-11-19 | 14.9 u | 43 | 43 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,62 | €-0,62 | -0.62% |
| bitvavo - kraken | €100,00 | 2026-11-20 | 22.8 u | 14 | 14 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,69 | €-1,69 | -1.69% |
| bitvavo - kraken | €100,00 | 2026-11-21 | 2.0 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,41 | €-0,41 | -0.41% |
| bitvavo - kraken | €150,00 | 2026-11-19 | 14.9 u | 43 | 43 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,93 | €-0,93 | -0.62% |
| bitvavo - kraken | €150,00 | 2026-11-20 | 22.8 u | 14 | 13 | 1 | €0,76 | €0,00 (0x) | **€0,76** | 0.51% | €-2,53 | €-1,77 | -1.18% |
| bitvavo - kraken | €150,00 | 2026-11-21 | 2.0 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,62 | €-0,62 | -0.41% |
| bitvavo - kraken | €200,00 | 2026-11-19 | 14.9 u | 43 | 37 | 6 | €0,14 | €0,00 (0x) | **€0,14** | 0.07% | €-1,24 | €-1,10 | -0.55% |
| bitvavo - kraken | €200,00 | 2026-11-20 | 22.8 u | 14 | 13 | 1 | €1,01 | €0,00 (0x) | **€1,01** | 0.51% | €-3,38 | €-2,36 | -1.18% |
| bitvavo - kraken | €200,00 | 2026-11-21 | 2.0 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,82 | €-0,82 | -0.41% |
| bitvavo - kraken | €2.000,00 | 2026-11-19 | 14.9 u | 43 | 27 | 16 | €11,14 | €6,39 (16x) | **€4,75** | 0.24% | €-12,32 | €-7,57 | -0.38% |
| bitvavo - kraken | €2.000,00 | 2026-11-20 | 22.8 u | 14 | 9 | 5 | €22,07 | €1,97 (4x) | **€20,11** | 1.01% | €-33,53 | €-13,43 | -0.67% |
| bitvavo - kraken | €2.000,00 | 2026-11-21 | 2.0 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-8,02 | €-8,02 | -0.40% |
| bitvavo - kraken | €5.000,00 | 2026-11-19 | 14.9 u | 43 | 22 | 21 | €28,08 | €14,95 (24x) | **€13,12** | 0.26% | €-30,85 | €-17,73 | -0.35% |
| bitvavo - kraken | €5.000,00 | 2026-11-20 | 22.8 u | 14 | 2 | 12 | €57,54 | €11,98 (14x) | **€45,56** | 0.91% | €-83,16 | €-37,61 | -0.75% |
| bitvavo - kraken | €5.000,00 | 2026-11-21 | 2.0 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-20,32 | €-20,32 | -0.41% |
| gate - kucoin | €100,00 | 2026-11-19 | 14.9 u | 25 | 25 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,80 | €-0,80 | -0.80% |
| gate - kucoin | €100,00 | 2026-11-20 | 22.8 u | 46 | 46 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,09 | €-0,09 | -0.09% |
| gate - kucoin | €100,00 | 2026-11-21 | 2.0 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,04 | €-0,04 | -0.04% |
| gate - kucoin | €150,00 | 2026-11-19 | 14.9 u | 25 | 25 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,19 | €-1,19 | -0.80% |
| gate - kucoin | €150,00 | 2026-11-20 | 22.8 u | 46 | 44 | 2 | €0,12 | €0,00 (1x) | **€0,12** | 0.08% | €-0,14 | €-0,01 | -0.01% |
| gate - kucoin | €150,00 | 2026-11-21 | 2.0 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,06 | €-0,06 | -0.04% |
| gate - kucoin | €200,00 | 2026-11-19 | 14.9 u | 25 | 25 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,59 | €-1,59 | -0.80% |
| gate - kucoin | €200,00 | 2026-11-20 | 22.8 u | 46 | 43 | 3 | €0,25 | €0,00 (1x) | **€0,25** | 0.13% | €-0,18 | €0,07 | 0.03% |
| gate - kucoin | €200,00 | 2026-11-21 | 2.0 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,09 | €-0,09 | -0.04% |
| gate - kucoin | €2.000,00 | 2026-11-19 | 14.9 u | 25 | 9 | 16 | €2,28 | €2,14 (12x) | **€0,14** | 0.01% | €-15,88 | €-15,75 | -0.79% |
| gate - kucoin | €2.000,00 | 2026-11-20 | 22.8 u | 46 | 16 | 30 | €10,91 | €2,16 (16x) | **€8,74** | 0.44% | €-1,78 | €6,96 | 0.35% |
| gate - kucoin | €2.000,00 | 2026-11-21 | 2.0 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,80 | €-0,80 | -0.04% |
| gate - kucoin | €5.000,00 | 2026-11-19 | 14.9 u | 25 | 6 | 19 | €8,01 | €4,83 (19x) | **€3,18** | 0.06% | €-39,75 | €-36,57 | -0.73% |
| gate - kucoin | €5.000,00 | 2026-11-20 | 22.8 u | 46 | 8 | 38 | €31,05 | €7,98 (32x) | **€23,07** | 0.46% | €-4,41 | €18,67 | 0.37% |
| gate - kucoin | €5.000,00 | 2026-11-21 | 2.0 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,88 | €-1,88 | -0.04% |
| kraken - kucoin | €100,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,11 | €0,11 | 0.11% |
| kraken - kucoin | €100,00 | 2026-11-20 | 22.8 u | 15 | 13 | 2 | €0,03 | €0,01 (1x) | **€0,02** | 0.02% | €0,11 | €0,13 | 0.13% |
| kraken - kucoin | €100,00 | 2026-11-21 | 2.0 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,01 | €0,01 | 0.01% |
| kraken - kucoin | €150,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,16 | €0,16 | 0.11% |
| kraken - kucoin | €150,00 | 2026-11-20 | 22.8 u | 15 | 13 | 2 | €0,05 | €0,01 (1x) | **€0,04** | 0.02% | €0,16 | €0,20 | 0.13% |
| kraken - kucoin | €150,00 | 2026-11-21 | 2.0 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,01 | €0,01 | 0.01% |
| kraken - kucoin | €200,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,22 | €0,22 | 0.11% |
| kraken - kucoin | €200,00 | 2026-11-20 | 22.8 u | 15 | 13 | 2 | €0,06 | €0,24 (2x) | **€-0,18** | -0.09% | €0,22 | €0,04 | 0.02% |
| kraken - kucoin | €200,00 | 2026-11-21 | 2.0 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,02 | €0,02 | 0.01% |
| kraken - kucoin | €2.000,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €2,19 | €2,19 | 0.11% |
| kraken - kucoin | €2.000,00 | 2026-11-20 | 22.8 u | 15 | 13 | 2 | €0,61 | €1,24 (3x) | **€-0,63** | -0.03% | €2,19 | €1,56 | 0.08% |
| kraken - kucoin | €2.000,00 | 2026-11-21 | 2.0 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,16 | €0,16 | 0.01% |
| kraken - kucoin | €5.000,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €5,49 | €5,49 | 0.11% |
| kraken - kucoin | €5.000,00 | 2026-11-20 | 22.8 u | 15 | 13 | 2 | €1,53 | €1,24 (3x) | **€0,28** | 0.01% | €5,48 | €5,77 | 0.12% |
| kraken - kucoin | €5.000,00 | 2026-11-21 | 2.0 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,41 | €0,41 | 0.01% |

- bitstamp - kraken, €100,00: munten SKY; bruto zonder voorraadgrens zou €22,30 zijn, met voorraad €1,18 (GEZIEN boek, GOK model).
- bitstamp - kraken, €150,00: munten SKY; bruto zonder voorraadgrens zou €21,71 zijn, met voorraad €1,78 (GEZIEN boek, GOK model).
- bitstamp - kraken, €200,00: munten SKY; bruto zonder voorraadgrens zou €21,12 zijn, met voorraad €2,37 (GEZIEN boek, GOK model).
- bitstamp - kraken, €2.000,00: munten SKY; bruto zonder voorraadgrens zou €11,71 zijn, met voorraad €11,71 (GEZIEN boek, GOK model).
- bitstamp - kraken, €5.000,00: munten SKY; bruto zonder voorraadgrens zou €11,71 zijn, met voorraad €11,71 (GEZIEN boek, GOK model).
- bitstamp - kucoin, €100,00: munten USDT; bruto zonder voorraadgrens zou €1,20 zijn, met voorraad €0,01 (GEZIEN boek, GOK model).
- bitstamp - kucoin, €150,00: munten USDT; bruto zonder voorraadgrens zou €1,20 zijn, met voorraad €0,01 (GEZIEN boek, GOK model).
- bitstamp - kucoin, €200,00: munten USDT; bruto zonder voorraadgrens zou €1,20 zijn, met voorraad €0,01 (GEZIEN boek, GOK model).
- bitstamp - kucoin, €2.000,00: munten USDT; bruto zonder voorraadgrens zou €1,20 zijn, met voorraad €0,10 (GEZIEN boek, GOK model).
- bitstamp - kucoin, €5.000,00: munten USDT; bruto zonder voorraadgrens zou €1,20 zijn, met voorraad €0,25 (GEZIEN boek, GOK model).
- bitvavo - kraken, €100,00: munten AVA, CVX, DYM, GMT, KERNEL, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €1.486,10 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitvavo - kraken, €150,00: munten AVA, CVX, DYM, GMT, KERNEL, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €1.486,10 zijn, met voorraad €0,76 (GEZIEN boek, GOK model).
- bitvavo - kraken, €200,00: munten AVA, CVX, DYM, GMT, KERNEL, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €1.485,69 zijn, met voorraad €1,15 (GEZIEN boek, GOK model).
- bitvavo - kraken, €2.000,00: munten AVA, CVX, DYM, GMT, KERNEL, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €1.463,94 zijn, met voorraad €33,21 (GEZIEN boek, GOK model).
- bitvavo - kraken, €5.000,00: munten AVA, CVX, DYM, GMT, KERNEL, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €1.431,52 zijn, met voorraad €85,61 (GEZIEN boek, GOK model).
- gate - kucoin, €100,00: munten ALKIMI, AVAIL, BARD, CCD, CHR, CWEB, CYBER, EDEN, ERG, FTT, HTR, IKA, IR, KYO, LUNC, NAKA, NIM, OVR, POKT, RARI, STREAM, USTC, VERONA; bruto zonder voorraadgrens zou €261,55 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- gate - kucoin, €150,00: munten ALKIMI, AVAIL, BARD, CCD, CHR, CWEB, CYBER, EDEN, ERG, FTT, HTR, IKA, IR, KYO, LUNC, NAKA, NIM, OVR, POKT, RARI, STREAM, USTC, VERONA; bruto zonder voorraadgrens zou €261,53 zijn, met voorraad €0,12 (GEZIEN boek, GOK model).
- gate - kucoin, €200,00: munten ALKIMI, AVAIL, BARD, CCD, CHR, CWEB, CYBER, EDEN, ERG, FTT, HTR, IKA, IR, KYO, LUNC, NAKA, NIM, OVR, POKT, RARI, STREAM, USTC, VERONA; bruto zonder voorraadgrens zou €261,52 zijn, met voorraad €0,25 (GEZIEN boek, GOK model).
- gate - kucoin, €2.000,00: munten ALKIMI, AVAIL, BARD, CCD, CHR, CWEB, CYBER, EDEN, ERG, FTT, HTR, IKA, IR, KYO, LUNC, NAKA, NIM, OVR, POKT, RARI, STREAM, USTC, VERONA; bruto zonder voorraadgrens zou €259,75 zijn, met voorraad €13,19 (GEZIEN boek, GOK model).
- gate - kucoin, €5.000,00: munten ALKIMI, AVAIL, BARD, CCD, CHR, CWEB, CYBER, EDEN, ERG, FTT, HTR, IKA, IR, KYO, LUNC, NAKA, NIM, OVR, POKT, RARI, STREAM, USTC, VERONA; bruto zonder voorraadgrens zou €255,35 zijn, met voorraad €39,06 (GEZIEN boek, GOK model).
- kraken - kucoin, €100,00: munten USDC, USDT; bruto zonder voorraadgrens zou €62,49 zijn, met voorraad €0,03 (GEZIEN boek, GOK model).
- kraken - kucoin, €150,00: munten USDC, USDT; bruto zonder voorraadgrens zou €62,48 zijn, met voorraad €0,05 (GEZIEN boek, GOK model).
- kraken - kucoin, €200,00: munten USDC, USDT; bruto zonder voorraadgrens zou €62,48 zijn, met voorraad €0,06 (GEZIEN boek, GOK model).
- kraken - kucoin, €2.000,00: munten USDC, USDT; bruto zonder voorraadgrens zou €62,20 zijn, met voorraad €0,61 (GEZIEN boek, GOK model).
- kraken - kucoin, €5.000,00: munten USDC, USDT; bruto zonder voorraadgrens zou €61,74 zijn, met voorraad €1,53 (GEZIEN boek, GOK model).

### Met minstens één grijze beurs (de 5 paren met de meeste bruto winst)

| Beurspaar | Inleg | Dag | Gemeten | Kansen | Gemist (geen voorraad) | Kleiner door voorraad | Bruto winst | Kosten terugschuiven | **Netto handel (bruto min kosten)** | Rendement handel | Koerseffect voorraad | Netto met koerseffect | Rendement met koerseffect |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| htx - xt | €100,00 | 2026-11-19 | 14.9 u | 18 | 18 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,84 | €-0,84 | -0.84% |
| htx - xt | €100,00 | 2026-11-20 | 22.8 u | 16 | 16 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,97 | €-2,97 | -2.97% |
| htx - xt | €100,00 | 2026-11-21 | 2.0 u | 2 | 2 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,67 | €-0,67 | -0.67% |
| htx - xt | €150,00 | 2026-11-19 | 14.9 u | 18 | 18 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,26 | €-1,26 | -0.84% |
| htx - xt | €150,00 | 2026-11-20 | 22.8 u | 16 | 16 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-4,46 | €-4,46 | -2.97% |
| htx - xt | €150,00 | 2026-11-21 | 2.0 u | 2 | 2 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,00 | €-1,00 | -0.67% |
| htx - xt | €200,00 | 2026-11-19 | 14.9 u | 18 | 18 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,67 | €-1,67 | -0.84% |
| htx - xt | €200,00 | 2026-11-20 | 22.8 u | 16 | 16 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-5,95 | €-5,95 | -2.97% |
| htx - xt | €200,00 | 2026-11-21 | 2.0 u | 2 | 2 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,34 | €-1,34 | -0.67% |
| htx - xt | €2.000,00 | 2026-11-19 | 14.9 u | 18 | 5 | 13 | €5,38 | €3,89 (10x) | **€1,49** | 0.07% | €-16,81 | €-15,32 | -0.77% |
| htx - xt | €2.000,00 | 2026-11-20 | 22.8 u | 16 | 4 | 12 | €10,17 | €2,20 (6x) | **€7,97** | 0.40% | €-59,17 | €-51,20 | -2.56% |
| htx - xt | €2.000,00 | 2026-11-21 | 2.0 u | 2 | 0 | 2 | €1,66 | €0,00 (0x) | **€1,66** | 0.08% | €-12,93 | €-11,27 | -0.56% |
| htx - xt | €5.000,00 | 2026-11-19 | 14.9 u | 18 | 5 | 13 | €13,40 | €6,17 (13x) | **€7,24** | 0.14% | €-41,92 | €-34,68 | -0.69% |
| htx - xt | €5.000,00 | 2026-11-20 | 22.8 u | 16 | 0 | 16 | €29,35 | €8,64 (15x) | **€20,70** | 0.41% | €-148,23 | €-127,53 | -2.55% |
| htx - xt | €5.000,00 | 2026-11-21 | 2.0 u | 2 | 0 | 2 | €2,47 | €0,00 (0x) | **€2,47** | 0.05% | €-32,85 | €-30,38 | -0.61% |
| kucoin - xt | €100,00 | 2026-11-19 | 14.9 u | 13 | 13 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,05 | €-0,05 | -0.05% |
| kucoin - xt | €100,00 | 2026-11-20 | 22.8 u | 10 | 10 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,37 | €-0,37 | -0.37% |
| kucoin - xt | €100,00 | 2026-11-21 | 2.0 u | 1 | 1 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,19 | €0,19 | 0.19% |
| kucoin - xt | €150,00 | 2026-11-19 | 14.9 u | 13 | 13 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,07 | €-0,07 | -0.05% |
| kucoin - xt | €150,00 | 2026-11-20 | 22.8 u | 10 | 10 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,56 | €-0,56 | -0.37% |
| kucoin - xt | €150,00 | 2026-11-21 | 2.0 u | 1 | 1 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,28 | €0,28 | 0.19% |
| kucoin - xt | €200,00 | 2026-11-19 | 14.9 u | 13 | 13 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,09 | €-0,09 | -0.05% |
| kucoin - xt | €200,00 | 2026-11-20 | 22.8 u | 10 | 9 | 1 | €0,20 | €0,00 (1x) | **€0,20** | 0.10% | €-0,75 | €-0,55 | -0.27% |
| kucoin - xt | €200,00 | 2026-11-21 | 2.0 u | 1 | 1 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,38 | €0,38 | 0.19% |
| kucoin - xt | €2.000,00 | 2026-11-19 | 14.9 u | 13 | 4 | 9 | €8,70 | €3,65 (9x) | **€5,05** | 0.25% | €-0,98 | €4,08 | 0.20% |
| kucoin - xt | €2.000,00 | 2026-11-20 | 22.8 u | 10 | 2 | 8 | €7,87 | €3,11 (7x) | **€4,76** | 0.24% | €-7,33 | €-2,57 | -0.13% |
| kucoin - xt | €2.000,00 | 2026-11-21 | 2.0 u | 1 | 0 | 1 | €0,29 | €0,83 (1x) | **€-0,54** | -0.03% | €3,99 | €3,44 | 0.17% |
| kucoin - xt | €5.000,00 | 2026-11-19 | 14.9 u | 13 | 3 | 10 | €20,13 | €5,49 (11x) | **€14,64** | 0.29% | €-2,36 | €12,28 | 0.25% |
| kucoin - xt | €5.000,00 | 2026-11-20 | 22.8 u | 10 | 1 | 8 | €19,55 | €6,03 (9x) | **€13,52** | 0.27% | €-18,60 | €-5,08 | -0.10% |
| kucoin - xt | €5.000,00 | 2026-11-21 | 2.0 u | 1 | 0 | 1 | €0,58 | €0,83 (1x) | **€-0,25** | -0.00% | €9,61 | €9,36 | 0.19% |
| gate - htx | €100,00 | 2026-11-19 | 14.9 u | 19 | 19 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,07 | €-1,07 | -1.07% |
| gate - htx | €100,00 | 2026-11-20 | 22.8 u | 32 | 32 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,76 | €-2,76 | -2.76% |
| gate - htx | €100,00 | 2026-11-21 | 2.0 u | 1 | 1 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,42 | €-0,42 | -0.42% |
| gate - htx | €150,00 | 2026-11-19 | 14.9 u | 19 | 19 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,60 | €-1,60 | -1.07% |
| gate - htx | €150,00 | 2026-11-20 | 22.8 u | 32 | 32 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-4,14 | €-4,14 | -2.76% |
| gate - htx | €150,00 | 2026-11-21 | 2.0 u | 1 | 1 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,63 | €-0,63 | -0.42% |
| gate - htx | €200,00 | 2026-11-19 | 14.9 u | 19 | 19 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,13 | €-2,13 | -1.07% |
| gate - htx | €200,00 | 2026-11-20 | 22.8 u | 32 | 32 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-5,52 | €-5,52 | -2.76% |
| gate - htx | €200,00 | 2026-11-21 | 2.0 u | 1 | 1 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,84 | €-0,84 | -0.42% |
| gate - htx | €2.000,00 | 2026-11-19 | 14.9 u | 19 | 14 | 5 | €0,99 | €0,17 (1x) | **€0,82** | 0.04% | €-21,34 | €-20,52 | -1.03% |
| gate - htx | €2.000,00 | 2026-11-20 | 22.8 u | 32 | 12 | 20 | €7,31 | €1,60 (9x) | **€5,72** | 0.29% | €-55,19 | €-49,47 | -2.47% |
| gate - htx | €2.000,00 | 2026-11-21 | 2.0 u | 1 | 0 | 1 | €0,26 | €0,09 (1x) | **€0,18** | 0.01% | €-8,35 | €-8,17 | -0.41% |
| gate - htx | €5.000,00 | 2026-11-19 | 14.9 u | 19 | 6 | 13 | €8,21 | €4,50 (12x) | **€3,71** | 0.07% | €-53,38 | €-49,67 | -0.99% |
| gate - htx | €5.000,00 | 2026-11-20 | 22.8 u | 32 | 4 | 28 | €24,11 | €5,17 (20x) | **€18,95** | 0.38% | €-137,67 | €-118,72 | -2.37% |
| gate - htx | €5.000,00 | 2026-11-21 | 2.0 u | 1 | 0 | 1 | €0,66 | €0,09 (1x) | **€0,58** | 0.01% | €-20,32 | €-19,74 | -0.39% |
| htx - kucoin | €100,00 | 2026-11-19 | 14.9 u | 16 | 16 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,22 | €-2,22 | -2.22% |
| htx - kucoin | €100,00 | 2026-11-20 | 22.8 u | 42 | 42 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,37 | €-3,37 | -3.37% |
| htx - kucoin | €100,00 | 2026-11-21 | 2.0 u | 1 | 1 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,51 | €-0,51 | -0.51% |
| htx - kucoin | €150,00 | 2026-11-19 | 14.9 u | 16 | 16 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,33 | €-3,33 | -2.22% |
| htx - kucoin | €150,00 | 2026-11-20 | 22.8 u | 42 | 42 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-5,05 | €-5,05 | -3.37% |
| htx - kucoin | €150,00 | 2026-11-21 | 2.0 u | 1 | 1 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,77 | €-0,77 | -0.51% |
| htx - kucoin | €200,00 | 2026-11-19 | 14.9 u | 16 | 16 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-4,43 | €-4,43 | -2.22% |
| htx - kucoin | €200,00 | 2026-11-20 | 22.8 u | 42 | 42 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-6,74 | €-6,74 | -3.37% |
| htx - kucoin | €200,00 | 2026-11-21 | 2.0 u | 1 | 1 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,03 | €-1,03 | -0.51% |
| htx - kucoin | €2.000,00 | 2026-11-19 | 14.9 u | 16 | 9 | 7 | €1,29 | €0,00 (1x) | **€1,28** | 0.06% | €-44,34 | €-43,06 | -2.15% |
| htx - kucoin | €2.000,00 | 2026-11-20 | 22.8 u | 42 | 24 | 18 | €7,40 | €0,00 (1x) | **€7,40** | 0.37% | €-67,36 | €-59,96 | -3.00% |
| htx - kucoin | €2.000,00 | 2026-11-21 | 2.0 u | 1 | 0 | 1 | €0,24 | €0,00 (0x) | **€0,24** | 0.01% | €-10,27 | €-10,04 | -0.50% |
| htx - kucoin | €5.000,00 | 2026-11-19 | 14.9 u | 16 | 3 | 13 | €6,88 | €3,83 (12x) | **€3,04** | 0.06% | €-110,77 | €-107,72 | -2.15% |
| htx - kucoin | €5.000,00 | 2026-11-20 | 22.8 u | 42 | 10 | 32 | €21,13 | €7,50 (23x) | **€13,62** | 0.27% | €-168,01 | €-154,38 | -3.09% |
| htx - kucoin | €5.000,00 | 2026-11-21 | 2.0 u | 1 | 0 | 1 | €0,59 | €0,17 (1x) | **€0,42** | 0.01% | €-25,37 | €-24,96 | -0.50% |
| bitget - xt | €100,00 | 2026-11-19 | 14.9 u | 13 | 13 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €2,07 | €2,07 | 2.07% |
| bitget - xt | €100,00 | 2026-11-20 | 22.8 u | 6 | 6 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-4,23 | €-4,23 | -4.23% |
| bitget - xt | €100,00 | 2026-11-21 | 2.0 u | 1 | 1 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,45 | €-0,45 | -0.45% |
| bitget - xt | €150,00 | 2026-11-19 | 14.9 u | 13 | 13 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €3,11 | €3,11 | 2.07% |
| bitget - xt | €150,00 | 2026-11-20 | 22.8 u | 6 | 6 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-6,35 | €-6,35 | -4.23% |
| bitget - xt | €150,00 | 2026-11-21 | 2.0 u | 1 | 1 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,68 | €-0,68 | -0.45% |
| bitget - xt | €200,00 | 2026-11-19 | 14.9 u | 13 | 9 | 4 | €0,50 | €0,01 (3x) | **€0,50** | 0.25% | €4,15 | €4,64 | 2.32% |
| bitget - xt | €200,00 | 2026-11-20 | 22.8 u | 6 | 6 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-8,47 | €-8,47 | -4.23% |
| bitget - xt | €200,00 | 2026-11-21 | 2.0 u | 1 | 1 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,91 | €-0,91 | -0.45% |
| bitget - xt | €2.000,00 | 2026-11-19 | 14.9 u | 13 | 4 | 9 | €9,96 | €1,96 (11x) | **€8,00** | 0.40% | €41,46 | €49,46 | 2.47% |
| bitget - xt | €2.000,00 | 2026-11-20 | 22.8 u | 6 | 0 | 6 | €7,25 | €2,27 (7x) | **€4,98** | 0.25% | €-84,59 | €-79,61 | -3.98% |
| bitget - xt | €2.000,00 | 2026-11-21 | 2.0 u | 1 | 0 | 1 | €0,51 | €1,71 (2x) | **€-1,20** | -0.06% | €-9,14 | €-10,34 | -0.52% |
| bitget - xt | €5.000,00 | 2026-11-19 | 14.9 u | 13 | 4 | 8 | €19,47 | €1,85 (10x) | **€17,62** | 0.35% | €103,65 | €121,27 | 2.43% |
| bitget - xt | €5.000,00 | 2026-11-20 | 22.8 u | 6 | 0 | 6 | €16,17 | €2,27 (7x) | **€13,90** | 0.28% | €-211,60 | €-197,70 | -3.95% |
| bitget - xt | €5.000,00 | 2026-11-21 | 2.0 u | 1 | 0 | 1 | €1,13 | €0,80 (1x) | **€0,34** | 0.01% | €-22,78 | €-22,44 | -0.45% |

- htx - xt, €100,00: munten APT, BSV, CARV, CBK, HBAR, LUNC, MEME, RAIN, SEI, XCH, XDC, XMR; bruto zonder voorraadgrens zou €276,24 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - xt, €150,00: munten APT, BSV, CARV, CBK, HBAR, LUNC, MEME, RAIN, SEI, XCH, XDC, XMR; bruto zonder voorraadgrens zou €276,24 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - xt, €200,00: munten APT, BSV, CARV, CBK, HBAR, LUNC, MEME, RAIN, SEI, XCH, XDC, XMR; bruto zonder voorraadgrens zou €276,24 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - xt, €2.000,00: munten APT, BSV, CARV, CBK, HBAR, LUNC, MEME, RAIN, SEI, XCH, XDC, XMR; bruto zonder voorraadgrens zou €274,91 zijn, met voorraad €17,21 (GEZIEN boek, GOK model).
- htx - xt, €5.000,00: munten APT, BSV, CARV, CBK, HBAR, LUNC, MEME, RAIN, SEI, XCH, XDC, XMR; bruto zonder voorraadgrens zou €272,96 zijn, met voorraad €45,22 (GEZIEN boek, GOK model).
- kucoin - xt, €100,00: munten BARD, DAG, ENSO, FIGHT, LUNC, XMR; bruto zonder voorraadgrens zou €841,24 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- kucoin - xt, €150,00: munten BARD, DAG, ENSO, FIGHT, LUNC, XMR; bruto zonder voorraadgrens zou €841,24 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- kucoin - xt, €200,00: munten BARD, DAG, ENSO, FIGHT, LUNC, XMR; bruto zonder voorraadgrens zou €841,24 zijn, met voorraad €0,20 (GEZIEN boek, GOK model).
- kucoin - xt, €2.000,00: munten BARD, DAG, ENSO, FIGHT, LUNC, XMR; bruto zonder voorraadgrens zou €838,35 zijn, met voorraad €16,86 (GEZIEN boek, GOK model).
- kucoin - xt, €5.000,00: munten BARD, DAG, ENSO, FIGHT, LUNC, XMR; bruto zonder voorraadgrens zou €834,15 zijn, met voorraad €40,26 (GEZIEN boek, GOK model).
- gate - htx, €100,00: munten APEPE, APT, BRISE, BSV, CBK, CRTS, CVX, ENJ, ENS, GOMINING, KAS, LAT, LUNC, MEME, MOVR, SEI, SSV, WARD, WLD, XCH, XCN; bruto zonder voorraadgrens zou €209,53 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- gate - htx, €150,00: munten APEPE, APT, BRISE, BSV, CBK, CRTS, CVX, ENJ, ENS, GOMINING, KAS, LAT, LUNC, MEME, MOVR, SEI, SSV, WARD, WLD, XCH, XCN; bruto zonder voorraadgrens zou €209,53 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- gate - htx, €200,00: munten APEPE, APT, BRISE, BSV, CBK, CRTS, CVX, ENJ, ENS, GOMINING, KAS, LAT, LUNC, MEME, MOVR, SEI, SSV, WARD, WLD, XCH, XCN; bruto zonder voorraadgrens zou €209,53 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- gate - htx, €2.000,00: munten APEPE, APT, BRISE, BSV, CBK, CRTS, CVX, ENJ, ENS, GOMINING, KAS, LAT, LUNC, MEME, MOVR, SEI, SSV, WARD, WLD, XCH, XCN; bruto zonder voorraadgrens zou €208,92 zijn, met voorraad €8,56 (GEZIEN boek, GOK model).
- gate - htx, €5.000,00: munten APEPE, APT, BRISE, BSV, CBK, CRTS, CVX, ENJ, ENS, GOMINING, KAS, LAT, LUNC, MEME, MOVR, SEI, SSV, WARD, WLD, XCH, XCN; bruto zonder voorraadgrens zou €205,14 zijn, met voorraad €32,98 (GEZIEN boek, GOK model).
- htx - kucoin, €100,00: munten ANIME, APT, BSV, CFX, CHIP, CVX, ELA, ENJ, ENS, FET, JASMY, LAT, LUNC, MEME, MOVR, ONE, SOMI, SSV, WAN, WARD, WLD, XCH, XCN, XEC, XMR; bruto zonder voorraadgrens zou €213,65 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - kucoin, €150,00: munten ANIME, APT, BSV, CFX, CHIP, CVX, ELA, ENJ, ENS, FET, JASMY, LAT, LUNC, MEME, MOVR, ONE, SOMI, SSV, WAN, WARD, WLD, XCH, XCN, XEC, XMR; bruto zonder voorraadgrens zou €213,65 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - kucoin, €200,00: munten ANIME, APT, BSV, CFX, CHIP, CVX, ELA, ENJ, ENS, FET, JASMY, LAT, LUNC, MEME, MOVR, ONE, SOMI, SSV, WAN, WARD, WLD, XCH, XCN, XEC, XMR; bruto zonder voorraadgrens zou €213,65 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - kucoin, €2.000,00: munten ANIME, APT, BSV, CFX, CHIP, CVX, ELA, ENJ, ENS, FET, JASMY, LAT, LUNC, MEME, MOVR, ONE, SOMI, SSV, WAN, WARD, WLD, XCH, XCN, XEC, XMR; bruto zonder voorraadgrens zou €213,13 zijn, met voorraad €8,93 (GEZIEN boek, GOK model).
- htx - kucoin, €5.000,00: munten ANIME, APT, BSV, CFX, CHIP, CVX, ELA, ENJ, ENS, FET, JASMY, LAT, LUNC, MEME, MOVR, ONE, SOMI, SSV, WAN, WARD, WLD, XCH, XCN, XEC, XMR; bruto zonder voorraadgrens zou €212,34 zijn, met voorraad €28,59 (GEZIEN boek, GOK model).
- bitget - xt, €100,00: munten ENSO, KOR, KUB, LUNC, YB; bruto zonder voorraadgrens zou €892,11 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - xt, €150,00: munten ENSO, KOR, KUB, LUNC, YB; bruto zonder voorraadgrens zou €892,11 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - xt, €200,00: munten ENSO, KOR, KUB, LUNC, YB; bruto zonder voorraadgrens zou €891,68 zijn, met voorraad €0,50 (GEZIEN boek, GOK model).
- bitget - xt, €2.000,00: munten ENSO, KOR, KUB, LUNC, YB; bruto zonder voorraadgrens zou €886,71 zijn, met voorraad €17,72 (GEZIEN boek, GOK model).
- bitget - xt, €5.000,00: munten ENSO, KOR, KUB, LUNC, YB; bruto zonder voorraadgrens zou €880,12 zijn, met voorraad €36,77 (GEZIEN boek, GOK model).

### Andere keuzes bij bitvavo - kraken (netto handel, alle dagen samen; GOK)

| Keuze | Inleg | Kansen | Gemist | Bruto winst | Kosten terugschuiven | Netto handel |
|---|---|---|---|---|---|---|
| standaard (schuifdrempel 25%, kostengrens 1%) | €150,00 | 57 | 56 | €0,76 | €0,00 | **€0,76** |
| standaard (schuifdrempel 25%, kostengrens 1%) | €2.000,00 | 57 | 36 | €33,21 | €8,35 | **€24,85** |
| schuifdrempel 10% | €150,00 | 57 | 56 | €0,76 | €0,00 | **€0,76** |
| schuifdrempel 10% | €2.000,00 | 57 | 37 | €33,25 | €7,04 | **€26,20** |
| schuifdrempel 40% | €150,00 | 57 | 56 | €0,76 | €0,00 | **€0,76** |
| schuifdrempel 40% | €2.000,00 | 57 | 34 | €36,11 | €9,97 | **€26,14** |
| kostengrens 2% (achteraf vergeleken) | €150,00 | 57 | 56 | €0,76 | €0,00 | **€0,76** |
| kostengrens 2% (achteraf vergeleken) | €2.000,00 | 57 | 24 | €35,91 | €25,93 | **€9,98** |
| kostengrens 5% (achteraf vergeleken) | €150,00 | 57 | 56 | €0,76 | €0,00 | **€0,76** |
| kostengrens 5% (achteraf vergeleken) | €2.000,00 | 57 | 24 | €35,91 | €25,93 | **€9,98** |
| alleen MERL en KERNEL (meer voorraad per munt, achteraf gekozen) | €150,00 | 20 | 18 | €2,05 | €0,00 | **€2,05** |
| alleen MERL en KERNEL (meer voorraad per munt, achteraf gekozen) | €2.000,00 | 20 | 9 | €102,46 | €8,22 | **€94,24** |

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
- Geld terugschuiven per beurs: bitget USDT: 1 USDT, GOK (1 USDT, 30 min; niet nagekeken); bitstamp EUR: 1 EUR, GOK (1 EUR, 24 uur; niet nagekeken); bitstamp USD: 1 USD, GOK (1 USD, 24 uur; niet nagekeken); bitvavo EUR: 0 EUR, kosten GEZIEN (api.bitvavo.com/v2/assets: EUR withdrawalFee 0), tijd GOK (1 werkdag, SEPA), minimum 0 EUR (GEZIEN, api.bitvavo.com/v2/assets withdrawalMinAmount); gate USDT: 1 USDT, GOK (1 USDT, 30 min; niet nagekeken), minimum 1 USDT (GEZIEN, api.gateio.ws/api/v4/wallet/currency_chains withdraw_amount_min); htx USDT: 1 USDT, GOK (1 USDT, 30 min; niet nagekeken); kraken EUR: 1 EUR, kosten GEZIEN (support.kraken.com/articles/360000381846: Instant SEPA, Banking Circle, 1 EUR, near-instant), tijd GOK (1 uur tot het op de andere beurs staat), minimum 2 EUR (GEZIEN, support.kraken.com/articles/360000381846 Instant SEPA (Banking Circle)); kraken USD: 1 USD, GOK (1 USD, 24 uur; niet nagekeken); kucoin EUR: 1 EUR, GOK (1 EUR, 24 uur; niet nagekeken); kucoin USDT: 1 USDT, kosten GEZIEN (api.kucoin.com/api/v3/currencies/USDT: BEP20 1 USDT), tijd GOK, minimum 5 USDT (GEZIEN, api.kucoin.com/api/v3/currencies/USDT BEP20 withdrawalMinSize); xt USDT: 1 USDT, GOK (1 USDT, 30 min; niet nagekeken).

## Over de meting

- Opnamekosten bij de echte kansen: 140 van een netwerk dat aan beide kanten open is, 112 van de beurs zelf (laagste open netwerk), 84 geschat uit wat andere beurzen voor die munt vragen (GOK). Onbekende opnamekosten tellen niet als echte kans.
- Netwerk: KuCoin, Gate, Bitget, HTX, XT, Bitstamp, Bitvavo en Poloniex geven hun netwerken per munt. Als beide beurzen dat doen en de namen te koppelen zijn, moet er een netwerk zijn dat aan beide kanten open is. Anders is het netwerk "niet te koppelen" en telt de kans mee (staat apart in de trechter).
- De duur is gemeten in stappen van ±20 seconden; een kans kan een paar rondes eerder begonnen zijn dan we zagen.
- Takerkosten: uit de API waar die ze per paar geeft, anders het standaardtarief uit de README (deels GOK).
- Laatste run: 15 beurzen antwoordden, 2281 munt-quote-paren op minstens twee beurzen (GEZIEN).
