# Rapport koersverschil-scanner

Gemaakt 2026-11-21 00:25 UTC uit 21 runs, samen ±38.2 uur gemeten (GEZIEN).
Echte kans = winst na alle kosten (opnamekosten bekend), opnemen en storten open (en een netwerk dat aan beide kanten open is, als de beurzen dat geven), minstens €100,00 op het boek, minstens 2 minuten blijven staan, geen andere munt met dezelfde naam.
**Vergund** = beide beurzen hebben een MiCA-vergunning (ESMA-register), vaak via een EU-dochter die minder munten kan hebben dan de wereldwijde API die we meten (GOK). **Grijs** = minstens één beurs zonder vergunning (MEXC, Bitget, HTX, Poloniex, XT, Bitfinex, Binance). Zie README.md.
**Kraken-tarief:** Kraken rekent 0,80% taker op munt tegen EUR, USD, USDT of USDC (GEZIEN, kraken.com/pro/fees, laagste trede); de scanner rekende tot 19 nov met 0,40%. 399 opgeslagen kansen met Kraken uit die runs zijn hier **opnieuw doorgerekend met 0,80%** (GOK-benadering: 0,40% van de inzet aan de Kraken-kant extra op elk gemeten punt van het boek; het boek zelf is niet bewaard). 233 houden daarna nog winst op het boek. Dat ze met hogere kosten ook korter bleven staan, telt niet mee (dus eerder te gunstig).

## Hoeveel wordt er gecontroleerd? (GEZIEN, stand.jsonl)

Per ronde (mediaan over 458 metingen): 1143 kandidaten (verschil op de ticker groter dan de takerkosten), 120 met het orderboek gecontroleerd, 2 nog nooit gecontroleerd (0%).
Bijna alle kandidaten komen aan de beurt; de aantallen hieronder missen weinig.

## Trechter (GEZIEN, eigen metingen)

| Stap | Alle beurzen | Alleen MiCA-beurzen | Met minstens één grijze beurs |
|---|---|---|---|
| Verschillen met winst op het boek na alle kosten | 35519 | 5152 | 30367 |
| ...waarvan opnemen of storten dicht | 6894 | 750 | 6144 |
| ...waarvan status onbekend (beurs geeft het niet openbaar) | 21353 | 3695 | 17658 |
| Opnemen en storten open | 7272 | 707 | 6565 |
| ...en geen netwerk dat aan beide kanten open is: valt af | 164 | 14 | 150 |
| ...en opnamekosten onbekend: valt af | 0 | 0 | 0 |
| ...en minstens €100,00 op het boek | 1967 | 405 | 1562 |
| ...en minstens 2 minuten blijven staan | 546 | 163 | 383 |
| ...en geen andere munt met dezelfde naam | 507 | 146 | 361 |
|    ...waarvan contractadres bekend en gelijk | 69 | 28 | 41 |
|    ...waarvan contractadres onbekend (telt mee, kan een andere munt zijn) | 438 | 118 | 320 |
|    ...waarvan netwerk gekoppeld en open | 316 | 67 | 249 |
|    ...waarvan netwerk niet te koppelen (telt mee) | 191 | 79 | 112 |
| **Echte kansen** (zelfde munt overlappend in de tijd samengevoegd, beste beurspaar telt) | 331 | 145 | 228 |
| Ter vergelijking: zelfde eisen, maar opnamestatus onbekend (niet meegeteld) | 1244 | 283 | 1062 |

## Echte kansen per dag (GEZIEN)

| Dag | Echt, alleen MiCA | Echt, met grijs | Mediane winst per kans bij €500 (MiCA / grijs) | Mediane duur |
|---|---|---|---|---|
| 2026-11-19 | 49 | 86 | €2,00 / €1,21 | 5.3 min |
| 2026-11-20 | 59 | 136 | €0,68 / €1,03 | 6.3 min |
| 2026-11-21 | 0 | 1 | geen / €3,09 | 3.0 min |
| Totaal | 108 | 223 | €1,23 / €1,16 | 5.7 min |

## Beste munten (GEZIEN)

| | Soort | Kansen | Som winst bij €500 per kans |
|---|---|---|---|
| MERL-EUR | vergund | 19 | €287,01 |
| LUNC-USDT | grijs en vergund | 15 | €79,13 |
| USTC-USDT | grijs | 13 | €51,00 |
| KERNEL-EUR | vergund | 1 | €47,33 |
| MEME-USDT | grijs | 1 | €37,90 |
| KYO-USDT | vergund | 5 | €30,94 |
| BARD-USDT | grijs | 4 | €24,39 |
| SKY-USD | vergund | 2 | €21,52 |
| BSV-USDT | grijs | 16 | €19,85 |
| LAT-USDT | grijs | 3 | €17,59 |

## Beste beursparen (kopen op > verkopen op) (GEZIEN)

| | Soort | Kansen | Som winst bij €500 per kans |
|---|---|---|---|
| bitvavo > kraken | vergund | 57 | €380,22 |
| bitget > htx | grijs | 47 | €112,08 |
| gate > kucoin | vergund | 25 | €68,85 |
| kucoin > htx | grijs | 29 | €62,74 |
| kucoin > bitget | grijs | 21 | €57,68 |
| bitget > xt | grijs | 12 | €43,27 |
| bitget > kucoin | grijs | 19 | €33,49 |
| bitget > gate | grijs | 12 | €32,74 |
| gate > xt | grijs | 4 | €28,67 |
| kucoin > xt | grijs | 6 | €22,49 |

Beurzen die het vaakst meedoen (koop of verkoop): bitget (grijs) 138, kucoin 137, htx (grijs) 111, kraken 86, gate 79, bitvavo 57, xt (grijs) 38, poloniex (grijs) 14 (GEZIEN).

## Hoeveel kansen blijven staan terwijl je geld schuift? (GEZIEN, duur uit eigen metingen)

Wie geen voorraad op beide beurzen heeft, moet kopen, de munt opnemen, wachten tot hij binnen is en dan verkopen. Hoe lang dat duurt verschilt per munt en netwerk: een paar minuten (snelle ketens) tot een uur of meer (Bitcoin, beurzen die opnames met de hand keuren) (GOK, niet per munt gemeten).

| Overmaaktijd | Alle beurzen | Alleen MiCA-beurzen | Met minstens één grijze beurs |
|---|---|---|---|
| 5 min | 193 van 331 (58%) | 85 van 145 (59%) | 133 van 228 (58%) |
| 10 min | 117 van 331 (35%) | 54 van 145 (37%) | 82 van 228 (36%) |
| 30 min | 61 van 331 (18%) | 33 van 145 (23%) | 43 van 228 (19%) |
| 60 min | 32 van 331 (10%) | 22 van 145 (15%) | 22 van 228 (10%) |

## Wat zou het opleveren over 3 maanden? (GOK, doorgetrokken uit de metingen)

Gemeten over ±38.2 uur (GEZIEN), doorgetrokken naar 90 dagen (GOK: aanname dat de week die we maten gewoon is).

| Beurzen | Inleg | Model | Kansen per uur | Per kans (mediaan) | 3 maanden |
|---|---|---|---|---|---|
| Alleen MiCA | €2.000,00 | bovengrens: elke kans, geld overal tegelijk | 3.80 | €1,64 | €13.468,20 |
| Alleen MiCA | €2.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 1.49 | €2,92 | €37.206,10 |
| Alleen MiCA | €5.000,00 | bovengrens: elke kans, geld overal tegelijk | 3.80 | €2,18 | €17.853,39 |
| Alleen MiCA | €5.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 1.49 | €3,27 | €58.551,70 |
| Alle (met grijs) | €2.000,00 | bovengrens: elke kans, geld overal tegelijk | 8.67 | €1,45 | €27.198,71 |
| Alle (met grijs) | €2.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 1.49 | €2,92 | €37.206,10 |
| Alle (met grijs) | €5.000,00 | bovengrens: elke kans, geld overal tegelijk | 8.67 | €1,64 | €30.744,66 |
| Alle (met grijs) | €5.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 1.49 | €3,27 | €58.551,70 |

Bovengrens: elke kans met de helft van de inleg aan elke kant, alsof het geld op alle beurzen tegelijk staat (kan in het echt niet). Beste beurspaar: het paar is **achteraf** gekozen uit de metingen (vooraf kiezen levert minder op), en het model neemt aan dat je van elke munt al voorraad op de verkoopbeurs hebt.

Waarom dit te rooskleurig is (GOK): elke kans wordt maar één keer geteld met het mediane boek, maar andere bots pakken hem ook; de munt die je als voorraad aanhoudt kan dalen; na een paar kansen moet de voorraad terug (opnamekosten en tijd); minimale opname- en ordergroottes tellen niet mee; en een kans die we 2 minuten zagen staan, staat er niet per se nog als jouw order binnenkomt. Waarom het te somber kan zijn: niet alle kandidaten zijn gecontroleerd, en met voorraad op beide beurzen kun je dezelfde kans vaker pakken als het boek zich aanvult; dat telt hier niet mee.

## Wat houd je echt over? Voorraad op twee beurzen (simulatie)

Per beurspaar: geld en munten op beide beurzen, elke echte kans uitgevoerd tegen het boek zoals gemeten (niet meer dan de ruimte op het boek en niet meer dan de voorraad op die beurs), terugschuiven als een kant leeg dreigt te raken (met opnamekosten en tijd onderweg), en het koerseffect van de aangehouden munten apart. Netto = bruto min kosten terugschuiven plus koerseffect. **Gemeten** (GEZIEN): de kansen, het boek en de koersen; **de rest is een rekenmodel** (GOK, aannames onder de tabel). Geen advies.

**Met €150: netto €0,59 per dag op bitstamp - kraken (koerseffect erbovenop €-1,24), €-0,00 per dag op bitstamp - kucoin (koerseffect erbovenop €0,09), €0,25 per dag op bitvavo - kraken (koerseffect erbovenop €-1,10), €0,04 per dag op gate - kucoin (koerseffect erbovenop €-0,43), €0,01 per dag op kraken - kucoin (koerseffect erbovenop €0,11) (GOK: netto handel, rekenmodel op ±12.7 uur meting per dag, alleen MiCA).** "Per dag" is hier gemiddeld over 3 gemeten dagen achter elkaar; de eerste begint met een gelijk verdeelde voorraad; aan het eind staat de voorraad scheef, dus een volgende dag levert waarschijnlijk minder op, tenzij kansen de andere kant op hem terugbrengen (GOK).

### Alleen MiCA-beurzen (alle paren met echte kansen)

| Beurspaar | Inleg | Dag | Gemeten | Kansen | Gemist (geen voorraad) | Kleiner door voorraad | Bruto winst | Kosten terugschuiven | **Netto handel (bruto min kosten)** | Rendement handel | Koerseffect voorraad | Netto met koerseffect | Rendement met koerseffect |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| bitstamp - kraken | €100,00 | 2026-11-19 | 14.9 u | 2 | 1 | 1 | €1,18 | €0,00 (0x) | **€1,18** | 1.18% | €0,63 | €1,81 | 1.81% |
| bitstamp - kraken | €100,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,38 | €-3,38 | -3.38% |
| bitstamp - kraken | €100,00 | 2026-11-21 | 0.4 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,27 | €0,27 | 0.27% |
| bitstamp - kraken | €150,00 | 2026-11-19 | 14.9 u | 2 | 1 | 1 | €1,78 | €0,00 (0x) | **€1,78** | 1.18% | €0,94 | €2,72 | 1.81% |
| bitstamp - kraken | €150,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-5,07 | €-5,07 | -3.38% |
| bitstamp - kraken | €150,00 | 2026-11-21 | 0.4 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,41 | €0,41 | 0.27% |
| bitstamp - kraken | €200,00 | 2026-11-19 | 14.9 u | 2 | 1 | 1 | €2,37 | €0,00 (0x) | **€2,37** | 1.18% | €1,25 | €3,62 | 1.81% |
| bitstamp - kraken | €200,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-6,76 | €-6,76 | -3.38% |
| bitstamp - kraken | €200,00 | 2026-11-21 | 0.4 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,54 | €0,54 | 0.27% |
| bitstamp - kraken | €2.000,00 | 2026-11-19 | 14.9 u | 2 | 1 | 0 | €11,71 | €0,00 (0x) | **€11,71** | 0.59% | €12,53 | €24,24 | 1.21% |
| bitstamp - kraken | €2.000,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-67,63 | €-67,63 | -3.38% |
| bitstamp - kraken | €2.000,00 | 2026-11-21 | 0.4 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €5,40 | €5,40 | 0.27% |
| bitstamp - kraken | €5.000,00 | 2026-11-19 | 14.9 u | 2 | 1 | 0 | €11,71 | €0,00 (0x) | **€11,71** | 0.23% | €31,33 | €43,04 | 0.86% |
| bitstamp - kraken | €5.000,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-169,08 | €-169,08 | -3.38% |
| bitstamp - kraken | €5.000,00 | 2026-11-21 | 0.4 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €13,50 | €13,50 | 0.27% |
| bitstamp - kucoin | €100,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,14 | €0,14 | 0.14% |
| bitstamp - kucoin | €100,00 | 2026-11-20 | 22.8 u | 1 | 0 | 1 | €0,01 | €0,01 (1x) | **€-0,00** | -0.00% | €0,09 | €0,08 | 0.08% |
| bitstamp - kucoin | €100,00 | 2026-11-21 | 0.4 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,04 | €-0,04 | -0.04% |
| bitstamp - kucoin | €150,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,21 | €0,21 | 0.14% |
| bitstamp - kucoin | €150,00 | 2026-11-20 | 22.8 u | 1 | 0 | 1 | €0,01 | €0,01 (1x) | **€-0,00** | -0.00% | €0,13 | €0,13 | 0.09% |
| bitstamp - kucoin | €150,00 | 2026-11-21 | 0.4 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,06 | €-0,06 | -0.04% |
| bitstamp - kucoin | €200,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,27 | €0,27 | 0.14% |
| bitstamp - kucoin | €200,00 | 2026-11-20 | 22.8 u | 1 | 0 | 1 | €0,01 | €0,01 (1x) | **€0,00** | 0.00% | €0,18 | €0,18 | 0.09% |
| bitstamp - kucoin | €200,00 | 2026-11-21 | 0.4 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,08 | €-0,08 | -0.04% |
| bitstamp - kucoin | €2.000,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €2,74 | €2,74 | 0.14% |
| bitstamp - kucoin | €2.000,00 | 2026-11-20 | 22.8 u | 1 | 0 | 1 | €0,10 | €1,01 (2x) | **€-0,91** | -0.05% | €1,76 | €0,85 | 0.04% |
| bitstamp - kucoin | €2.000,00 | 2026-11-21 | 0.4 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,77 | €-0,77 | -0.04% |
| bitstamp - kucoin | €5.000,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €6,86 | €6,86 | 0.14% |
| bitstamp - kucoin | €5.000,00 | 2026-11-20 | 22.8 u | 1 | 0 | 1 | €0,25 | €1,01 (2x) | **€-0,76** | -0.02% | €4,39 | €3,63 | 0.07% |
| bitstamp - kucoin | €5.000,00 | 2026-11-21 | 0.4 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,92 | €-1,92 | -0.04% |
| bitvavo - kraken | €100,00 | 2026-11-19 | 14.9 u | 43 | 43 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,62 | €-0,62 | -0.62% |
| bitvavo - kraken | €100,00 | 2026-11-20 | 22.8 u | 14 | 14 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,69 | €-1,69 | -1.69% |
| bitvavo - kraken | €100,00 | 2026-11-21 | 0.4 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,11 | €0,11 | 0.11% |
| bitvavo - kraken | €150,00 | 2026-11-19 | 14.9 u | 43 | 43 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,93 | €-0,93 | -0.62% |
| bitvavo - kraken | €150,00 | 2026-11-20 | 22.8 u | 14 | 13 | 1 | €0,76 | €0,00 (0x) | **€0,76** | 0.51% | €-2,53 | €-1,77 | -1.18% |
| bitvavo - kraken | €150,00 | 2026-11-21 | 0.4 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,16 | €0,16 | 0.11% |
| bitvavo - kraken | €200,00 | 2026-11-19 | 14.9 u | 43 | 37 | 6 | €0,14 | €0,00 (0x) | **€0,14** | 0.07% | €-1,24 | €-1,10 | -0.55% |
| bitvavo - kraken | €200,00 | 2026-11-20 | 22.8 u | 14 | 13 | 1 | €1,01 | €0,00 (0x) | **€1,01** | 0.51% | €-3,38 | €-2,36 | -1.18% |
| bitvavo - kraken | €200,00 | 2026-11-21 | 0.4 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,21 | €0,21 | 0.11% |
| bitvavo - kraken | €2.000,00 | 2026-11-19 | 14.9 u | 43 | 27 | 16 | €11,14 | €6,39 (16x) | **€4,75** | 0.24% | €-12,32 | €-7,57 | -0.38% |
| bitvavo - kraken | €2.000,00 | 2026-11-20 | 22.8 u | 14 | 9 | 5 | €22,07 | €1,97 (4x) | **€20,11** | 1.01% | €-33,53 | €-13,43 | -0.67% |
| bitvavo - kraken | €2.000,00 | 2026-11-21 | 0.4 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €2,22 | €2,22 | 0.11% |
| bitvavo - kraken | €5.000,00 | 2026-11-19 | 14.9 u | 43 | 22 | 21 | €28,08 | €14,95 (24x) | **€13,12** | 0.26% | €-30,85 | €-17,73 | -0.35% |
| bitvavo - kraken | €5.000,00 | 2026-11-20 | 22.8 u | 14 | 2 | 12 | €57,54 | €11,98 (14x) | **€45,56** | 0.91% | €-83,16 | €-37,61 | -0.75% |
| bitvavo - kraken | €5.000,00 | 2026-11-21 | 0.4 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €5,51 | €5,51 | 0.11% |
| gate - kucoin | €100,00 | 2026-11-19 | 14.9 u | 25 | 25 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,80 | €-0,80 | -0.80% |
| gate - kucoin | €100,00 | 2026-11-20 | 22.8 u | 46 | 46 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,09 | €-0,09 | -0.09% |
| gate - kucoin | €100,00 | 2026-11-21 | 0.4 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,03 | €0,03 | 0.03% |
| gate - kucoin | €150,00 | 2026-11-19 | 14.9 u | 25 | 25 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,19 | €-1,19 | -0.80% |
| gate - kucoin | €150,00 | 2026-11-20 | 22.8 u | 46 | 44 | 2 | €0,12 | €0,00 (1x) | **€0,12** | 0.08% | €-0,14 | €-0,01 | -0.01% |
| gate - kucoin | €150,00 | 2026-11-21 | 0.4 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,05 | €0,05 | 0.03% |
| gate - kucoin | €200,00 | 2026-11-19 | 14.9 u | 25 | 25 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,59 | €-1,59 | -0.80% |
| gate - kucoin | €200,00 | 2026-11-20 | 22.8 u | 46 | 43 | 3 | €0,25 | €0,00 (1x) | **€0,25** | 0.13% | €-0,18 | €0,07 | 0.03% |
| gate - kucoin | €200,00 | 2026-11-21 | 0.4 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,07 | €0,07 | 0.03% |
| gate - kucoin | €2.000,00 | 2026-11-19 | 14.9 u | 25 | 9 | 16 | €2,28 | €2,14 (12x) | **€0,14** | 0.01% | €-15,88 | €-15,75 | -0.79% |
| gate - kucoin | €2.000,00 | 2026-11-20 | 22.8 u | 46 | 16 | 30 | €10,91 | €2,16 (16x) | **€8,74** | 0.44% | €-1,78 | €6,96 | 0.35% |
| gate - kucoin | €2.000,00 | 2026-11-21 | 0.4 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,69 | €0,69 | 0.03% |
| gate - kucoin | €5.000,00 | 2026-11-19 | 14.9 u | 25 | 6 | 19 | €8,01 | €4,83 (19x) | **€3,18** | 0.06% | €-39,75 | €-36,57 | -0.73% |
| gate - kucoin | €5.000,00 | 2026-11-20 | 22.8 u | 46 | 8 | 38 | €31,05 | €7,98 (32x) | **€23,07** | 0.46% | €-4,41 | €18,67 | 0.37% |
| gate - kucoin | €5.000,00 | 2026-11-21 | 0.4 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €1,70 | €1,70 | 0.03% |
| kraken - kucoin | €100,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,11 | €0,11 | 0.11% |
| kraken - kucoin | €100,00 | 2026-11-20 | 22.8 u | 15 | 13 | 2 | €0,03 | €0,01 (1x) | **€0,02** | 0.02% | €0,11 | €0,13 | 0.13% |
| kraken - kucoin | €100,00 | 2026-11-21 | 0.4 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,00 | €-0,00 | -0.00% |
| kraken - kucoin | €150,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,16 | €0,16 | 0.11% |
| kraken - kucoin | €150,00 | 2026-11-20 | 22.8 u | 15 | 13 | 2 | €0,05 | €0,01 (1x) | **€0,04** | 0.02% | €0,16 | €0,20 | 0.13% |
| kraken - kucoin | €150,00 | 2026-11-21 | 0.4 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,00 | €-0,00 | -0.00% |
| kraken - kucoin | €200,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,22 | €0,22 | 0.11% |
| kraken - kucoin | €200,00 | 2026-11-20 | 22.8 u | 15 | 13 | 2 | €0,06 | €0,24 (2x) | **€-0,18** | -0.09% | €0,22 | €0,04 | 0.02% |
| kraken - kucoin | €200,00 | 2026-11-21 | 0.4 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,00 | €-0,00 | -0.00% |
| kraken - kucoin | €2.000,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €2,19 | €2,19 | 0.11% |
| kraken - kucoin | €2.000,00 | 2026-11-20 | 22.8 u | 15 | 13 | 2 | €0,61 | €1,24 (3x) | **€-0,63** | -0.03% | €2,19 | €1,56 | 0.08% |
| kraken - kucoin | €2.000,00 | 2026-11-21 | 0.4 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,00 | €-0,00 | -0.00% |
| kraken - kucoin | €5.000,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €5,49 | €5,49 | 0.11% |
| kraken - kucoin | €5.000,00 | 2026-11-20 | 22.8 u | 15 | 13 | 2 | €1,53 | €1,24 (3x) | **€0,28** | 0.01% | €5,48 | €5,77 | 0.12% |
| kraken - kucoin | €5.000,00 | 2026-11-21 | 0.4 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,00 | €-0,00 | -0.00% |

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
| htx - xt | €100,00 | 2026-11-19 | 14.9 u | 18 | 18 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,68 | €-0,68 | -0.68% |
| htx - xt | €100,00 | 2026-11-20 | 22.8 u | 16 | 16 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,81 | €-2,81 | -2.81% |
| htx - xt | €100,00 | 2026-11-21 | 0.4 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,08 | €-0,08 | -0.08% |
| htx - xt | €150,00 | 2026-11-19 | 14.9 u | 18 | 18 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,02 | €-1,02 | -0.68% |
| htx - xt | €150,00 | 2026-11-20 | 22.8 u | 16 | 16 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-4,22 | €-4,22 | -2.81% |
| htx - xt | €150,00 | 2026-11-21 | 0.4 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,13 | €-0,13 | -0.08% |
| htx - xt | €200,00 | 2026-11-19 | 14.9 u | 18 | 18 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,36 | €-1,36 | -0.68% |
| htx - xt | €200,00 | 2026-11-20 | 22.8 u | 16 | 16 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-5,62 | €-5,62 | -2.81% |
| htx - xt | €200,00 | 2026-11-21 | 0.4 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,17 | €-0,17 | -0.08% |
| htx - xt | €2.000,00 | 2026-11-19 | 14.9 u | 18 | 5 | 13 | €5,87 | €3,89 (10x) | **€1,99** | 0.10% | €-13,69 | €-11,71 | -0.59% |
| htx - xt | €2.000,00 | 2026-11-20 | 22.8 u | 16 | 2 | 14 | €12,42 | €3,36 (9x) | **€9,05** | 0.45% | €-55,93 | €-46,87 | -2.34% |
| htx - xt | €2.000,00 | 2026-11-21 | 0.4 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,58 | €-1,58 | -0.08% |
| htx - xt | €5.000,00 | 2026-11-19 | 14.9 u | 18 | 5 | 13 | €14,23 | €6,17 (13x) | **€8,06** | 0.16% | €-34,14 | €-26,08 | -0.52% |
| htx - xt | €5.000,00 | 2026-11-20 | 22.8 u | 16 | 0 | 16 | €31,74 | €8,64 (15x) | **€23,10** | 0.46% | €-140,09 | €-116,99 | -2.34% |
| htx - xt | €5.000,00 | 2026-11-21 | 0.4 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-4,07 | €-4,07 | -0.08% |
| kucoin - xt | €100,00 | 2026-11-19 | 14.9 u | 13 | 13 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,05 | €-0,05 | -0.05% |
| kucoin - xt | €100,00 | 2026-11-20 | 22.8 u | 9 | 9 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,37 | €-0,37 | -0.37% |
| kucoin - xt | €100,00 | 2026-11-21 | 0.4 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,05 | €0,05 | 0.05% |
| kucoin - xt | €150,00 | 2026-11-19 | 14.9 u | 13 | 13 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,07 | €-0,07 | -0.05% |
| kucoin - xt | €150,00 | 2026-11-20 | 22.8 u | 9 | 9 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,56 | €-0,56 | -0.37% |
| kucoin - xt | €150,00 | 2026-11-21 | 0.4 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,07 | €0,07 | 0.05% |
| kucoin - xt | €200,00 | 2026-11-19 | 14.9 u | 13 | 13 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,09 | €-0,09 | -0.05% |
| kucoin - xt | €200,00 | 2026-11-20 | 22.8 u | 9 | 8 | 1 | €0,20 | €0,00 (1x) | **€0,20** | 0.10% | €-0,75 | €-0,55 | -0.27% |
| kucoin - xt | €200,00 | 2026-11-21 | 0.4 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,09 | €0,09 | 0.05% |
| kucoin - xt | €2.000,00 | 2026-11-19 | 14.9 u | 13 | 4 | 9 | €8,70 | €3,65 (9x) | **€5,05** | 0.25% | €-0,98 | €4,07 | 0.20% |
| kucoin - xt | €2.000,00 | 2026-11-20 | 22.8 u | 9 | 2 | 7 | €7,12 | €2,76 (6x) | **€4,36** | 0.22% | €-7,31 | €-2,95 | -0.15% |
| kucoin - xt | €2.000,00 | 2026-11-21 | 0.4 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,98 | €0,98 | 0.05% |
| kucoin - xt | €5.000,00 | 2026-11-19 | 14.9 u | 13 | 3 | 10 | €20,13 | €5,50 (11x) | **€14,64** | 0.29% | €-2,36 | €12,28 | 0.25% |
| kucoin - xt | €5.000,00 | 2026-11-20 | 22.8 u | 9 | 1 | 7 | €17,69 | €5,68 (8x) | **€12,01** | 0.24% | €-18,58 | €-6,57 | -0.13% |
| kucoin - xt | €5.000,00 | 2026-11-21 | 0.4 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €2,40 | €2,40 | 0.05% |
| gate - htx | €100,00 | 2026-11-19 | 14.9 u | 19 | 19 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,99 | €-0,99 | -0.99% |
| gate - htx | €100,00 | 2026-11-20 | 22.8 u | 30 | 30 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,66 | €-2,66 | -2.66% |
| gate - htx | €100,00 | 2026-11-21 | 0.4 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,17 | €-0,17 | -0.17% |
| gate - htx | €150,00 | 2026-11-19 | 14.9 u | 19 | 19 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,49 | €-1,49 | -0.99% |
| gate - htx | €150,00 | 2026-11-20 | 22.8 u | 30 | 30 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,99 | €-3,99 | -2.66% |
| gate - htx | €150,00 | 2026-11-21 | 0.4 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,26 | €-0,26 | -0.17% |
| gate - htx | €200,00 | 2026-11-19 | 14.9 u | 19 | 19 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,99 | €-1,99 | -0.99% |
| gate - htx | €200,00 | 2026-11-20 | 22.8 u | 30 | 30 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-5,32 | €-5,32 | -2.66% |
| gate - htx | €200,00 | 2026-11-21 | 0.4 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,34 | €-0,34 | -0.17% |
| gate - htx | €2.000,00 | 2026-11-19 | 14.9 u | 19 | 14 | 5 | €1,04 | €0,17 (1x) | **€0,87** | 0.04% | €-19,86 | €-18,99 | -0.95% |
| gate - htx | €2.000,00 | 2026-11-20 | 22.8 u | 30 | 11 | 19 | €7,62 | €1,46 (8x) | **€6,16** | 0.31% | €-53,18 | €-47,02 | -2.35% |
| gate - htx | €2.000,00 | 2026-11-21 | 0.4 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,42 | €-3,42 | -0.17% |
| gate - htx | €5.000,00 | 2026-11-19 | 14.9 u | 19 | 6 | 13 | €8,62 | €4,50 (12x) | **€4,13** | 0.08% | €-49,68 | €-45,55 | -0.91% |
| gate - htx | €5.000,00 | 2026-11-20 | 22.8 u | 30 | 4 | 26 | €24,16 | €5,26 (19x) | **€18,90** | 0.38% | €-132,62 | €-113,73 | -2.27% |
| gate - htx | €5.000,00 | 2026-11-21 | 0.4 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-8,45 | €-8,45 | -0.17% |
| htx - kucoin | €100,00 | 2026-11-19 | 14.9 u | 16 | 16 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,20 | €-2,20 | -2.20% |
| htx - kucoin | €100,00 | 2026-11-20 | 22.8 u | 42 | 42 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,31 | €-3,31 | -3.31% |
| htx - kucoin | €100,00 | 2026-11-21 | 0.4 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,22 | €-0,22 | -0.22% |
| htx - kucoin | €150,00 | 2026-11-19 | 14.9 u | 16 | 16 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,31 | €-3,31 | -2.20% |
| htx - kucoin | €150,00 | 2026-11-20 | 22.8 u | 42 | 42 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-4,96 | €-4,96 | -3.31% |
| htx - kucoin | €150,00 | 2026-11-21 | 0.4 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,34 | €-0,34 | -0.22% |
| htx - kucoin | €200,00 | 2026-11-19 | 14.9 u | 16 | 16 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-4,41 | €-4,41 | -2.20% |
| htx - kucoin | €200,00 | 2026-11-20 | 22.8 u | 42 | 42 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-6,62 | €-6,62 | -3.31% |
| htx - kucoin | €200,00 | 2026-11-21 | 0.4 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,45 | €-0,45 | -0.22% |
| htx - kucoin | €2.000,00 | 2026-11-19 | 14.9 u | 16 | 9 | 7 | €1,34 | €0,00 (1x) | **€1,34** | 0.07% | €-44,07 | €-42,73 | -2.14% |
| htx - kucoin | €2.000,00 | 2026-11-20 | 22.8 u | 42 | 24 | 18 | €7,71 | €0,00 (1x) | **€7,71** | 0.39% | €-66,20 | €-58,49 | -2.92% |
| htx - kucoin | €2.000,00 | 2026-11-21 | 0.4 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-4,50 | €-4,50 | -0.22% |
| htx - kucoin | €5.000,00 | 2026-11-19 | 14.9 u | 16 | 3 | 13 | €7,16 | €3,83 (12x) | **€3,33** | 0.07% | €-110,07 | €-106,74 | -2.13% |
| htx - kucoin | €5.000,00 | 2026-11-20 | 22.8 u | 42 | 10 | 32 | €22,01 | €7,50 (23x) | **€14,51** | 0.29% | €-165,10 | €-150,59 | -3.01% |
| htx - kucoin | €5.000,00 | 2026-11-21 | 0.4 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-11,17 | €-11,17 | -0.22% |
| bitget - xt | €100,00 | 2026-11-19 | 14.9 u | 13 | 13 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €2,07 | €2,07 | 2.07% |
| bitget - xt | €100,00 | 2026-11-20 | 22.8 u | 6 | 6 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-4,23 | €-4,23 | -4.23% |
| bitget - xt | €100,00 | 2026-11-21 | 0.4 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,01 | €0,01 | 0.01% |
| bitget - xt | €150,00 | 2026-11-19 | 14.9 u | 13 | 13 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €3,11 | €3,11 | 2.07% |
| bitget - xt | €150,00 | 2026-11-20 | 22.8 u | 6 | 6 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-6,35 | €-6,35 | -4.23% |
| bitget - xt | €150,00 | 2026-11-21 | 0.4 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,01 | €0,01 | 0.01% |
| bitget - xt | €200,00 | 2026-11-19 | 14.9 u | 13 | 9 | 4 | €0,50 | €0,01 (3x) | **€0,50** | 0.25% | €4,15 | €4,64 | 2.32% |
| bitget - xt | €200,00 | 2026-11-20 | 22.8 u | 6 | 6 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-8,47 | €-8,47 | -4.23% |
| bitget - xt | €200,00 | 2026-11-21 | 0.4 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,01 | €0,01 | 0.01% |
| bitget - xt | €2.000,00 | 2026-11-19 | 14.9 u | 13 | 4 | 9 | €9,96 | €1,95 (11x) | **€8,00** | 0.40% | €41,46 | €49,46 | 2.47% |
| bitget - xt | €2.000,00 | 2026-11-20 | 22.8 u | 6 | 0 | 6 | €7,25 | €2,06 (7x) | **€5,19** | 0.26% | €-84,59 | €-79,40 | -3.97% |
| bitget - xt | €2.000,00 | 2026-11-21 | 0.4 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,12 | €0,12 | 0.01% |
| bitget - xt | €5.000,00 | 2026-11-19 | 14.9 u | 13 | 4 | 8 | €19,47 | €1,85 (10x) | **€17,62** | 0.35% | €103,65 | €121,27 | 2.43% |
| bitget - xt | €5.000,00 | 2026-11-20 | 22.8 u | 6 | 0 | 6 | €16,17 | €2,06 (7x) | **€14,11** | 0.28% | €-211,60 | €-197,49 | -3.95% |
| bitget - xt | €5.000,00 | 2026-11-21 | 0.4 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,30 | €0,30 | 0.01% |

- htx - xt, €100,00: munten BSV, CARV, CBK, HBAR, LUNC, MEME, RAIN, SEI, XCH, XDC, XMR; bruto zonder voorraadgrens zou €270,54 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - xt, €150,00: munten BSV, CARV, CBK, HBAR, LUNC, MEME, RAIN, SEI, XCH, XDC, XMR; bruto zonder voorraadgrens zou €270,54 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - xt, €200,00: munten BSV, CARV, CBK, HBAR, LUNC, MEME, RAIN, SEI, XCH, XDC, XMR; bruto zonder voorraadgrens zou €270,54 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - xt, €2.000,00: munten BSV, CARV, CBK, HBAR, LUNC, MEME, RAIN, SEI, XCH, XDC, XMR; bruto zonder voorraadgrens zou €269,09 zijn, met voorraad €18,29 (GEZIEN boek, GOK model).
- htx - xt, €5.000,00: munten BSV, CARV, CBK, HBAR, LUNC, MEME, RAIN, SEI, XCH, XDC, XMR; bruto zonder voorraadgrens zou €267,09 zijn, met voorraad €45,97 (GEZIEN boek, GOK model).
- kucoin - xt, €100,00: munten BARD, DAG, ENSO, FIGHT, LUNC, XMR; bruto zonder voorraadgrens zou €806,05 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- kucoin - xt, €150,00: munten BARD, DAG, ENSO, FIGHT, LUNC, XMR; bruto zonder voorraadgrens zou €806,05 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- kucoin - xt, €200,00: munten BARD, DAG, ENSO, FIGHT, LUNC, XMR; bruto zonder voorraadgrens zou €806,05 zijn, met voorraad €0,20 (GEZIEN boek, GOK model).
- kucoin - xt, €2.000,00: munten BARD, DAG, ENSO, FIGHT, LUNC, XMR; bruto zonder voorraadgrens zou €803,15 zijn, met voorraad €15,82 (GEZIEN boek, GOK model).
- kucoin - xt, €5.000,00: munten BARD, DAG, ENSO, FIGHT, LUNC, XMR; bruto zonder voorraadgrens zou €798,96 zijn, met voorraad €37,82 (GEZIEN boek, GOK model).
- gate - htx, €100,00: munten APEPE, BRISE, BSV, CBK, CRTS, CVX, ENJ, ENS, GOMINING, KAS, LAT, LUNC, MEME, MOVR, SEI, SSV, WARD, WLD, XCH, XCN; bruto zonder voorraadgrens zou €196,83 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- gate - htx, €150,00: munten APEPE, BRISE, BSV, CBK, CRTS, CVX, ENJ, ENS, GOMINING, KAS, LAT, LUNC, MEME, MOVR, SEI, SSV, WARD, WLD, XCH, XCN; bruto zonder voorraadgrens zou €196,83 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- gate - htx, €200,00: munten APEPE, BRISE, BSV, CBK, CRTS, CVX, ENJ, ENS, GOMINING, KAS, LAT, LUNC, MEME, MOVR, SEI, SSV, WARD, WLD, XCH, XCN; bruto zonder voorraadgrens zou €196,83 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- gate - htx, €2.000,00: munten APEPE, BRISE, BSV, CBK, CRTS, CVX, ENJ, ENS, GOMINING, KAS, LAT, LUNC, MEME, MOVR, SEI, SSV, WARD, WLD, XCH, XCN; bruto zonder voorraadgrens zou €196,19 zijn, met voorraad €8,65 (GEZIEN boek, GOK model).
- gate - htx, €5.000,00: munten APEPE, BRISE, BSV, CBK, CRTS, CVX, ENJ, ENS, GOMINING, KAS, LAT, LUNC, MEME, MOVR, SEI, SSV, WARD, WLD, XCH, XCN; bruto zonder voorraadgrens zou €192,21 zijn, met voorraad €32,78 (GEZIEN boek, GOK model).
- htx - kucoin, €100,00: munten ANIME, BSV, CFX, CHIP, CVX, ELA, ENJ, ENS, FET, JASMY, LAT, LUNC, MEME, MOVR, ONE, SOMI, SSV, WAN, WARD, WLD, XCH, XCN, XEC, XMR; bruto zonder voorraadgrens zou €211,91 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - kucoin, €150,00: munten ANIME, BSV, CFX, CHIP, CVX, ELA, ENJ, ENS, FET, JASMY, LAT, LUNC, MEME, MOVR, ONE, SOMI, SSV, WAN, WARD, WLD, XCH, XCN, XEC, XMR; bruto zonder voorraadgrens zou €211,91 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - kucoin, €200,00: munten ANIME, BSV, CFX, CHIP, CVX, ELA, ENJ, ENS, FET, JASMY, LAT, LUNC, MEME, MOVR, ONE, SOMI, SSV, WAN, WARD, WLD, XCH, XCN, XEC, XMR; bruto zonder voorraadgrens zou €211,91 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - kucoin, €2.000,00: munten ANIME, BSV, CFX, CHIP, CVX, ELA, ENJ, ENS, FET, JASMY, LAT, LUNC, MEME, MOVR, ONE, SOMI, SSV, WAN, WARD, WLD, XCH, XCN, XEC, XMR; bruto zonder voorraadgrens zou €211,37 zijn, met voorraad €9,06 (GEZIEN boek, GOK model).
- htx - kucoin, €5.000,00: munten ANIME, BSV, CFX, CHIP, CVX, ELA, ENJ, ENS, FET, JASMY, LAT, LUNC, MEME, MOVR, ONE, SOMI, SSV, WAN, WARD, WLD, XCH, XCN, XEC, XMR; bruto zonder voorraadgrens zou €210,55 zijn, met voorraad €29,17 (GEZIEN boek, GOK model).
- bitget - xt, €100,00: munten ENSO, KOR, KUB, LUNC, YB; bruto zonder voorraadgrens zou €885,90 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - xt, €150,00: munten ENSO, KOR, KUB, LUNC, YB; bruto zonder voorraadgrens zou €885,90 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - xt, €200,00: munten ENSO, KOR, KUB, LUNC, YB; bruto zonder voorraadgrens zou €885,47 zijn, met voorraad €0,50 (GEZIEN boek, GOK model).
- bitget - xt, €2.000,00: munten ENSO, KOR, KUB, LUNC, YB; bruto zonder voorraadgrens zou €880,51 zijn, met voorraad €17,21 (GEZIEN boek, GOK model).
- bitget - xt, €5.000,00: munten ENSO, KOR, KUB, LUNC, YB; bruto zonder voorraadgrens zou €873,91 zijn, met voorraad €35,64 (GEZIEN boek, GOK model).

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

- Opnamekosten bij de echte kansen: 134 van een netwerk dat aan beide kanten open is, 113 van de beurs zelf (laagste open netwerk), 84 geschat uit wat andere beurzen voor die munt vragen (GOK). Onbekende opnamekosten tellen niet als echte kans.
- Netwerk: KuCoin, Gate, Bitget, HTX, XT, Bitstamp, Bitvavo en Poloniex geven hun netwerken per munt. Als beide beurzen dat doen en de namen te koppelen zijn, moet er een netwerk zijn dat aan beide kanten open is. Anders is het netwerk "niet te koppelen" en telt de kans mee (staat apart in de trechter).
- De duur is gemeten in stappen van ±20 seconden; een kans kan een paar rondes eerder begonnen zijn dan we zagen.
- Takerkosten: uit de API waar die ze per paar geeft, anders het standaardtarief uit de README (deels GOK).
- Laatste run: 15 beurzen antwoordden, 2288 munt-quote-paren op minstens twee beurzen (GEZIEN).
