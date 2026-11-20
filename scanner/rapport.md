# Rapport koersverschil-scanner

Gemaakt 2026-11-20 22:16 UTC uit 21 runs, samen ±36.0 uur gemeten (GEZIEN).
Echte kans = winst na alle kosten (opnamekosten bekend), opnemen en storten open (en een netwerk dat aan beide kanten open is, als de beurzen dat geven), minstens €100,00 op het boek, minstens 2 minuten blijven staan, geen andere munt met dezelfde naam.
**Vergund** = beide beurzen hebben een MiCA-vergunning (ESMA-register), vaak via een EU-dochter die minder munten kan hebben dan de wereldwijde API die we meten (GOK). **Grijs** = minstens één beurs zonder vergunning (MEXC, Bitget, HTX, Poloniex, XT, Bitfinex, Binance). Zie README.md.
**Kraken-tarief:** Kraken rekent 0,80% taker op munt tegen EUR, USD, USDT of USDC (GEZIEN, kraken.com/pro/fees, laagste trede); de scanner rekende tot 19 nov met 0,40%. 399 opgeslagen kansen met Kraken uit die runs zijn hier **opnieuw doorgerekend met 0,80%** (GOK-benadering: 0,40% van de inzet aan de Kraken-kant extra op elk gemeten punt van het boek; het boek zelf is niet bewaard). 233 houden daarna nog winst op het boek. Dat ze met hogere kosten ook korter bleven staan, telt niet mee (dus eerder te gunstig).

## Hoeveel wordt er gecontroleerd? (GEZIEN, stand.jsonl)

Per ronde (mediaan over 432 metingen): 1144 kandidaten (verschil op de ticker groter dan de takerkosten), 120 met het orderboek gecontroleerd, 2 nog nooit gecontroleerd (0%).
Bijna alle kandidaten komen aan de beurt; de aantallen hieronder missen weinig.

## Trechter (GEZIEN, eigen metingen)

| Stap | Alle beurzen | Alleen MiCA-beurzen | Met minstens één grijze beurs |
|---|---|---|---|
| Verschillen met winst op het boek na alle kosten | 33354 | 4891 | 28463 |
| ...waarvan opnemen of storten dicht | 6675 | 726 | 5949 |
| ...waarvan status onbekend (beurs geeft het niet openbaar) | 19934 | 3488 | 16446 |
| Opnemen en storten open | 6745 | 677 | 6068 |
| ...en geen netwerk dat aan beide kanten open is: valt af | 156 | 12 | 144 |
| ...en opnamekosten onbekend: valt af | 0 | 0 | 0 |
| ...en minstens €100,00 op het boek | 1875 | 383 | 1492 |
| ...en minstens 2 minuten blijven staan | 523 | 155 | 368 |
| ...en geen andere munt met dezelfde naam | 484 | 138 | 346 |
|    ...waarvan contractadres bekend en gelijk | 65 | 26 | 39 |
|    ...waarvan contractadres onbekend (telt mee, kan een andere munt zijn) | 419 | 112 | 307 |
|    ...waarvan netwerk gekoppeld en open | 305 | 63 | 242 |
|    ...waarvan netwerk niet te koppelen (telt mee) | 179 | 75 | 104 |
| **Echte kansen** (zelfde munt overlappend in de tijd samengevoegd, beste beurspaar telt) | 312 | 137 | 216 |
| Ter vergelijking: zelfde eisen, maar opnamestatus onbekend (niet meegeteld) | 1117 | 268 | 946 |

## Echte kansen per dag (GEZIEN)

| Dag | Echt, alleen MiCA | Echt, met grijs | Mediane winst per kans bij €500 (MiCA / grijs) | Mediane duur |
|---|---|---|---|---|
| 2026-11-19 | 49 | 86 | €2,00 / €1,21 | 5.3 min |
| 2026-11-20 | 52 | 125 | €0,70 / €1,10 | 6.7 min |
| Totaal | 101 | 211 | €1,29 / €1,17 | 6.0 min |

## Beste munten (GEZIEN)

| | Soort | Kansen | Som winst bij €500 per kans |
|---|---|---|---|
| MERL-EUR | vergund | 19 | €287,01 |
| LUNC-USDT | grijs | 13 | €74,10 |
| KERNEL-EUR | vergund | 1 | €47,33 |
| USTC-USDT | grijs | 11 | €45,20 |
| MEME-USDT | grijs | 1 | €37,90 |
| BARD-USDT | grijs | 4 | €24,39 |
| KYO-USDT | vergund | 4 | €24,15 |
| SKY-USD | vergund | 2 | €21,52 |
| BSV-USDT | grijs | 15 | €19,45 |
| LAT-USDT | grijs | 3 | €17,59 |

## Beste beursparen (kopen op > verkopen op) (GEZIEN)

| | Soort | Kansen | Som winst bij €500 per kans |
|---|---|---|---|
| bitvavo > kraken | vergund | 57 | €380,22 |
| bitget > htx | grijs | 47 | €112,08 |
| kucoin > htx | grijs | 28 | €62,34 |
| gate > kucoin | vergund | 23 | €59,95 |
| kucoin > bitget | grijs | 20 | €51,91 |
| bitget > xt | grijs | 12 | €43,27 |
| bitget > kucoin | grijs | 19 | €33,49 |
| bitget > gate | grijs | 10 | €30,26 |
| gate > xt | grijs | 4 | €28,67 |
| kucoin > xt | grijs | 6 | €22,49 |

Beurzen die het vaakst meedoen (koop of verkoop): bitget (grijs) 132, kucoin 126, htx (grijs) 104, kraken 82, gate 72, bitvavo 57, xt (grijs) 35, poloniex (grijs) 14 (GEZIEN).

## Hoeveel kansen blijven staan terwijl je geld schuift? (GEZIEN, duur uit eigen metingen)

Wie geen voorraad op beide beurzen heeft, moet kopen, de munt opnemen, wachten tot hij binnen is en dan verkopen. Hoe lang dat duurt verschilt per munt en netwerk: een paar minuten (snelle ketens) tot een uur of meer (Bitcoin, beurzen die opnames met de hand keuren) (GOK, niet per munt gemeten).

| Overmaaktijd | Alle beurzen | Alleen MiCA-beurzen | Met minstens één grijze beurs |
|---|---|---|---|
| 5 min | 185 van 312 (59%) | 80 van 137 (58%) | 129 van 216 (60%) |
| 10 min | 114 van 312 (37%) | 51 van 137 (37%) | 81 van 216 (38%) |
| 30 min | 59 van 312 (19%) | 31 van 137 (23%) | 42 van 216 (19%) |
| 60 min | 30 van 312 (10%) | 20 van 137 (15%) | 21 van 216 (10%) |

## Wat zou het opleveren over 3 maanden? (GOK, doorgetrokken uit de metingen)

Gemeten over ±36.0 uur (GEZIEN), doorgetrokken naar 90 dagen (GOK: aanname dat de week die we maten gewoon is).

| Beurzen | Inleg | Model | Kansen per uur | Per kans (mediaan) | 3 maanden |
|---|---|---|---|---|---|
| Alleen MiCA | €2.000,00 | bovengrens: elke kans, geld overal tegelijk | 3.81 | €1,64 | €13.490,97 |
| Alleen MiCA | €2.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 1.58 | €2,92 | €39.445,27 |
| Alleen MiCA | €5.000,00 | bovengrens: elke kans, geld overal tegelijk | 3.81 | €2,18 | €17.883,56 |
| Alleen MiCA | €5.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 1.58 | €3,27 | €62.075,51 |
| Alle (met grijs) | €2.000,00 | bovengrens: elke kans, geld overal tegelijk | 8.67 | €1,48 | €27.688,62 |
| Alle (met grijs) | €2.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 1.58 | €2,92 | €39.445,27 |
| Alle (met grijs) | €5.000,00 | bovengrens: elke kans, geld overal tegelijk | 8.67 | €1,64 | €30.699,62 |
| Alle (met grijs) | €5.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 1.58 | €3,27 | €62.075,51 |

Bovengrens: elke kans met de helft van de inleg aan elke kant, alsof het geld op alle beurzen tegelijk staat (kan in het echt niet). Beste beurspaar: het paar is **achteraf** gekozen uit de metingen (vooraf kiezen levert minder op), en het model neemt aan dat je van elke munt al voorraad op de verkoopbeurs hebt.

Waarom dit te rooskleurig is (GOK): elke kans wordt maar één keer geteld met het mediane boek, maar andere bots pakken hem ook; de munt die je als voorraad aanhoudt kan dalen; na een paar kansen moet de voorraad terug (opnamekosten en tijd); minimale opname- en ordergroottes tellen niet mee; en een kans die we 2 minuten zagen staan, staat er niet per se nog als jouw order binnenkomt. Waarom het te somber kan zijn: niet alle kandidaten zijn gecontroleerd, en met voorraad op beide beurzen kun je dezelfde kans vaker pakken als het boek zich aanvult; dat telt hier niet mee.

## Wat houd je echt over? Voorraad op twee beurzen (simulatie)

Per beurspaar: geld en munten op beide beurzen, elke echte kans uitgevoerd tegen het boek zoals gemeten (niet meer dan de ruimte op het boek en niet meer dan de voorraad op die beurs), terugschuiven als een kant leeg dreigt te raken (met opnamekosten en tijd onderweg), en het koerseffect van de aangehouden munten apart. Netto = bruto min kosten terugschuiven plus koerseffect. **Gemeten** (GEZIEN): de kansen, het boek en de koersen; **de rest is een rekenmodel** (GOK, aannames onder de tabel). Geen advies.

**Met €150: netto €0,89 per dag op bitstamp - kraken (koerseffect erbovenop €-2,07), €-0,00 per dag op bitstamp - kucoin (koerseffect erbovenop €0,19), €0,38 per dag op bitvavo - kraken (koerseffect erbovenop €-1,78), €0,06 per dag op gate - kucoin (koerseffect erbovenop €-0,50), €0,02 per dag op kraken - kucoin (koerseffect erbovenop €0,20) (GOK: netto handel, rekenmodel op ±18.0 uur meting per dag, alleen MiCA).** "Per dag" is hier gemiddeld over 2 gemeten dagen achter elkaar; de eerste begint met een gelijk verdeelde voorraad; aan het eind staat de voorraad scheef, dus een volgende dag levert waarschijnlijk minder op, tenzij kansen de andere kant op hem terugbrengen (GOK).

### Alleen MiCA-beurzen (alle paren met echte kansen)

| Beurspaar | Inleg | Dag | Gemeten | Kansen | Gemist (geen voorraad) | Kleiner door voorraad | Bruto winst | Kosten terugschuiven | **Netto handel (bruto min kosten)** | Rendement handel | Koerseffect voorraad | Netto met koerseffect | Rendement met koerseffect |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| bitstamp - kraken | €100,00 | 2026-11-19 | 14.9 u | 2 | 1 | 1 | €1,18 | €0,00 (0x) | **€1,18** | 1.18% | €0,63 | €1,81 | 1.81% |
| bitstamp - kraken | €100,00 | 2026-11-20 | 21.1 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,38 | €-3,38 | -3.38% |
| bitstamp - kraken | €150,00 | 2026-11-19 | 14.9 u | 2 | 1 | 1 | €1,78 | €0,00 (0x) | **€1,78** | 1.18% | €0,94 | €2,72 | 1.81% |
| bitstamp - kraken | €150,00 | 2026-11-20 | 21.1 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-5,07 | €-5,07 | -3.38% |
| bitstamp - kraken | €200,00 | 2026-11-19 | 14.9 u | 2 | 1 | 1 | €2,37 | €0,00 (0x) | **€2,37** | 1.18% | €1,25 | €3,62 | 1.81% |
| bitstamp - kraken | €200,00 | 2026-11-20 | 21.1 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-6,76 | €-6,76 | -3.38% |
| bitstamp - kraken | €2.000,00 | 2026-11-19 | 14.9 u | 2 | 1 | 0 | €11,71 | €0,00 (0x) | **€11,71** | 0.59% | €12,53 | €24,24 | 1.21% |
| bitstamp - kraken | €2.000,00 | 2026-11-20 | 21.1 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-67,63 | €-67,63 | -3.38% |
| bitstamp - kraken | €5.000,00 | 2026-11-19 | 14.9 u | 2 | 1 | 0 | €11,71 | €0,00 (0x) | **€11,71** | 0.23% | €31,33 | €43,04 | 0.86% |
| bitstamp - kraken | €5.000,00 | 2026-11-20 | 21.1 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-169,08 | €-169,08 | -3.38% |
| bitstamp - kucoin | €100,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,14 | €0,14 | 0.14% |
| bitstamp - kucoin | €100,00 | 2026-11-20 | 21.1 u | 1 | 0 | 1 | €0,01 | €0,01 (1x) | **€-0,00** | -0.00% | €0,12 | €0,12 | 0.12% |
| bitstamp - kucoin | €150,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,21 | €0,21 | 0.14% |
| bitstamp - kucoin | €150,00 | 2026-11-20 | 21.1 u | 1 | 0 | 1 | €0,01 | €0,01 (1x) | **€-0,00** | -0.00% | €0,18 | €0,18 | 0.12% |
| bitstamp - kucoin | €200,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,27 | €0,27 | 0.14% |
| bitstamp - kucoin | €200,00 | 2026-11-20 | 21.1 u | 1 | 0 | 1 | €0,01 | €0,01 (1x) | **€0,00** | 0.00% | €0,24 | €0,24 | 0.12% |
| bitstamp - kucoin | €2.000,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €2,74 | €2,74 | 0.14% |
| bitstamp - kucoin | €2.000,00 | 2026-11-20 | 21.1 u | 1 | 0 | 1 | €0,10 | €1,01 (2x) | **€-0,91** | -0.05% | €2,42 | €1,51 | 0.08% |
| bitstamp - kucoin | €5.000,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €6,86 | €6,86 | 0.14% |
| bitstamp - kucoin | €5.000,00 | 2026-11-20 | 21.1 u | 1 | 0 | 1 | €0,25 | €1,01 (2x) | **€-0,76** | -0.02% | €6,04 | €5,28 | 0.11% |
| bitvavo - kraken | €100,00 | 2026-11-19 | 14.9 u | 43 | 43 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,62 | €-0,62 | -0.62% |
| bitvavo - kraken | €100,00 | 2026-11-20 | 21.1 u | 14 | 14 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,75 | €-1,75 | -1.75% |
| bitvavo - kraken | €150,00 | 2026-11-19 | 14.9 u | 43 | 43 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,93 | €-0,93 | -0.62% |
| bitvavo - kraken | €150,00 | 2026-11-20 | 21.1 u | 14 | 13 | 1 | €0,76 | €0,00 (0x) | **€0,76** | 0.51% | €-2,63 | €-1,87 | -1.25% |
| bitvavo - kraken | €200,00 | 2026-11-19 | 14.9 u | 43 | 37 | 6 | €0,14 | €0,00 (0x) | **€0,14** | 0.07% | €-1,24 | €-1,10 | -0.55% |
| bitvavo - kraken | €200,00 | 2026-11-20 | 21.1 u | 14 | 13 | 1 | €1,01 | €0,00 (0x) | **€1,01** | 0.51% | €-3,51 | €-2,49 | -1.25% |
| bitvavo - kraken | €2.000,00 | 2026-11-19 | 14.9 u | 43 | 27 | 16 | €11,14 | €6,39 (16x) | **€4,75** | 0.24% | €-12,32 | €-7,57 | -0.38% |
| bitvavo - kraken | €2.000,00 | 2026-11-20 | 21.1 u | 14 | 9 | 5 | €22,07 | €1,97 (4x) | **€20,11** | 1.01% | €-34,79 | €-14,69 | -0.73% |
| bitvavo - kraken | €5.000,00 | 2026-11-19 | 14.9 u | 43 | 22 | 21 | €28,08 | €14,95 (24x) | **€13,12** | 0.26% | €-30,85 | €-17,73 | -0.35% |
| bitvavo - kraken | €5.000,00 | 2026-11-20 | 21.1 u | 14 | 2 | 12 | €57,54 | €11,98 (14x) | **€45,56** | 0.91% | €-86,30 | €-40,74 | -0.81% |
| gate - kucoin | €100,00 | 2026-11-19 | 14.9 u | 25 | 25 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,80 | €-0,80 | -0.80% |
| gate - kucoin | €100,00 | 2026-11-20 | 21.1 u | 42 | 42 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,13 | €0,13 | 0.13% |
| gate - kucoin | €150,00 | 2026-11-19 | 14.9 u | 25 | 25 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,19 | €-1,19 | -0.80% |
| gate - kucoin | €150,00 | 2026-11-20 | 21.1 u | 42 | 40 | 2 | €0,12 | €0,00 (1x) | **€0,12** | 0.08% | €0,20 | €0,33 | 0.22% |
| gate - kucoin | €200,00 | 2026-11-19 | 14.9 u | 25 | 25 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,59 | €-1,59 | -0.80% |
| gate - kucoin | €200,00 | 2026-11-20 | 21.1 u | 42 | 39 | 3 | €0,25 | €0,00 (1x) | **€0,25** | 0.13% | €0,27 | €0,52 | 0.26% |
| gate - kucoin | €2.000,00 | 2026-11-19 | 14.9 u | 25 | 9 | 16 | €2,28 | €2,15 (12x) | **€0,13** | 0.01% | €-15,88 | €-15,75 | -0.79% |
| gate - kucoin | €2.000,00 | 2026-11-20 | 21.1 u | 42 | 13 | 29 | €10,74 | €2,00 (15x) | **€8,74** | 0.44% | €2,81 | €11,55 | 0.58% |
| gate - kucoin | €5.000,00 | 2026-11-19 | 14.9 u | 25 | 6 | 19 | €8,01 | €4,84 (19x) | **€3,17** | 0.06% | €-39,75 | €-36,58 | -0.73% |
| gate - kucoin | €5.000,00 | 2026-11-20 | 21.1 u | 42 | 7 | 35 | €29,33 | €7,24 (29x) | **€22,08** | 0.44% | €7,08 | €29,16 | 0.58% |
| kraken - kucoin | €100,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,11 | €0,11 | 0.11% |
| kraken - kucoin | €100,00 | 2026-11-20 | 21.1 u | 11 | 9 | 2 | €0,03 | €0,01 (1x) | **€0,02** | 0.02% | €0,16 | €0,18 | 0.18% |
| kraken - kucoin | €150,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,16 | €0,16 | 0.11% |
| kraken - kucoin | €150,00 | 2026-11-20 | 21.1 u | 11 | 9 | 2 | €0,05 | €0,01 (1x) | **€0,04** | 0.02% | €0,23 | €0,27 | 0.18% |
| kraken - kucoin | €200,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,22 | €0,22 | 0.11% |
| kraken - kucoin | €200,00 | 2026-11-20 | 21.1 u | 11 | 9 | 2 | €0,06 | €0,24 (2x) | **€-0,18** | -0.09% | €0,31 | €0,13 | 0.07% |
| kraken - kucoin | €2.000,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €2,19 | €2,19 | 0.11% |
| kraken - kucoin | €2.000,00 | 2026-11-20 | 21.1 u | 11 | 9 | 2 | €0,61 | €1,24 (3x) | **€-0,63** | -0.03% | €3,13 | €2,50 | 0.12% |
| kraken - kucoin | €5.000,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €5,49 | €5,49 | 0.11% |
| kraken - kucoin | €5.000,00 | 2026-11-20 | 21.1 u | 11 | 9 | 2 | €1,53 | €1,24 (3x) | **€0,28** | 0.01% | €7,81 | €8,10 | 0.16% |

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
- gate - kucoin, €100,00: munten ALKIMI, AVAIL, BARD, CCD, CHR, CWEB, CYBER, EDEN, ERG, FTT, HTR, IKA, IR, KYO, LUNC, NAKA, NIM, OVR, POKT, RARI, STREAM, USTC, VERONA; bruto zonder voorraadgrens zou €242,41 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- gate - kucoin, €150,00: munten ALKIMI, AVAIL, BARD, CCD, CHR, CWEB, CYBER, EDEN, ERG, FTT, HTR, IKA, IR, KYO, LUNC, NAKA, NIM, OVR, POKT, RARI, STREAM, USTC, VERONA; bruto zonder voorraadgrens zou €242,39 zijn, met voorraad €0,12 (GEZIEN boek, GOK model).
- gate - kucoin, €200,00: munten ALKIMI, AVAIL, BARD, CCD, CHR, CWEB, CYBER, EDEN, ERG, FTT, HTR, IKA, IR, KYO, LUNC, NAKA, NIM, OVR, POKT, RARI, STREAM, USTC, VERONA; bruto zonder voorraadgrens zou €242,38 zijn, met voorraad €0,25 (GEZIEN boek, GOK model).
- gate - kucoin, €2.000,00: munten ALKIMI, AVAIL, BARD, CCD, CHR, CWEB, CYBER, EDEN, ERG, FTT, HTR, IKA, IR, KYO, LUNC, NAKA, NIM, OVR, POKT, RARI, STREAM, USTC, VERONA; bruto zonder voorraadgrens zou €240,61 zijn, met voorraad €13,02 (GEZIEN boek, GOK model).
- gate - kucoin, €5.000,00: munten ALKIMI, AVAIL, BARD, CCD, CHR, CWEB, CYBER, EDEN, ERG, FTT, HTR, IKA, IR, KYO, LUNC, NAKA, NIM, OVR, POKT, RARI, STREAM, USTC, VERONA; bruto zonder voorraadgrens zou €236,21 zijn, met voorraad €37,33 (GEZIEN boek, GOK model).
- kraken - kucoin, €100,00: munten USDC, USDT; bruto zonder voorraadgrens zou €50,57 zijn, met voorraad €0,03 (GEZIEN boek, GOK model).
- kraken - kucoin, €150,00: munten USDC, USDT; bruto zonder voorraadgrens zou €50,56 zijn, met voorraad €0,05 (GEZIEN boek, GOK model).
- kraken - kucoin, €200,00: munten USDC, USDT; bruto zonder voorraadgrens zou €50,55 zijn, met voorraad €0,06 (GEZIEN boek, GOK model).
- kraken - kucoin, €2.000,00: munten USDC, USDT; bruto zonder voorraadgrens zou €50,27 zijn, met voorraad €0,61 (GEZIEN boek, GOK model).
- kraken - kucoin, €5.000,00: munten USDC, USDT; bruto zonder voorraadgrens zou €49,81 zijn, met voorraad €1,53 (GEZIEN boek, GOK model).

### Met minstens één grijze beurs (de 5 paren met de meeste bruto winst)

| Beurspaar | Inleg | Dag | Gemeten | Kansen | Gemist (geen voorraad) | Kleiner door voorraad | Bruto winst | Kosten terugschuiven | **Netto handel (bruto min kosten)** | Rendement handel | Koerseffect voorraad | Netto met koerseffect | Rendement met koerseffect |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| htx - xt | €100,00 | 2026-11-19 | 14.9 u | 18 | 18 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,68 | €-0,68 | -0.68% |
| htx - xt | €100,00 | 2026-11-20 | 21.1 u | 14 | 14 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,89 | €-2,89 | -2.89% |
| htx - xt | €150,00 | 2026-11-19 | 14.9 u | 18 | 18 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,02 | €-1,02 | -0.68% |
| htx - xt | €150,00 | 2026-11-20 | 21.1 u | 14 | 14 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-4,33 | €-4,33 | -2.89% |
| htx - xt | €200,00 | 2026-11-19 | 14.9 u | 18 | 18 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,36 | €-1,36 | -0.68% |
| htx - xt | €200,00 | 2026-11-20 | 21.1 u | 14 | 14 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-5,77 | €-5,77 | -2.89% |
| htx - xt | €2.000,00 | 2026-11-19 | 14.9 u | 18 | 5 | 13 | €5,87 | €3,89 (10x) | **€1,99** | 0.10% | €-13,69 | €-11,71 | -0.59% |
| htx - xt | €2.000,00 | 2026-11-20 | 21.1 u | 14 | 1 | 13 | €12,39 | €3,36 (9x) | **€9,02** | 0.45% | €-57,34 | €-48,32 | -2.42% |
| htx - xt | €5.000,00 | 2026-11-19 | 14.9 u | 18 | 5 | 13 | €14,23 | €6,17 (13x) | **€8,06** | 0.16% | €-34,14 | €-26,08 | -0.52% |
| htx - xt | €5.000,00 | 2026-11-20 | 21.1 u | 14 | 0 | 14 | €31,28 | €6,98 (13x) | **€24,30** | 0.49% | €-143,74 | €-119,43 | -2.39% |
| kucoin - xt | €100,00 | 2026-11-19 | 14.9 u | 13 | 13 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,05 | €-0,05 | -0.05% |
| kucoin - xt | €100,00 | 2026-11-20 | 21.1 u | 7 | 7 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,99 | €-0,99 | -0.99% |
| kucoin - xt | €150,00 | 2026-11-19 | 14.9 u | 13 | 13 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,07 | €-0,07 | -0.05% |
| kucoin - xt | €150,00 | 2026-11-20 | 21.1 u | 7 | 7 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,48 | €-1,48 | -0.99% |
| kucoin - xt | €200,00 | 2026-11-19 | 14.9 u | 13 | 13 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,09 | €-0,09 | -0.05% |
| kucoin - xt | €200,00 | 2026-11-20 | 21.1 u | 7 | 6 | 1 | €0,20 | €0,00 (1x) | **€0,20** | 0.10% | €-1,98 | €-1,78 | -0.89% |
| kucoin - xt | €2.000,00 | 2026-11-19 | 14.9 u | 13 | 4 | 9 | €8,70 | €3,65 (9x) | **€5,05** | 0.25% | €-0,98 | €4,07 | 0.20% |
| kucoin - xt | €2.000,00 | 2026-11-20 | 21.1 u | 7 | 1 | 6 | €6,93 | €2,76 (6x) | **€4,17** | 0.21% | €-19,57 | €-15,40 | -0.77% |
| kucoin - xt | €5.000,00 | 2026-11-19 | 14.9 u | 13 | 3 | 10 | €20,13 | €5,50 (11x) | **€14,64** | 0.29% | €-2,36 | €12,28 | 0.25% |
| kucoin - xt | €5.000,00 | 2026-11-20 | 21.1 u | 7 | 0 | 6 | €17,46 | €4,85 (7x) | **€12,61** | 0.25% | €-49,21 | €-36,60 | -0.73% |
| gate - htx | €100,00 | 2026-11-19 | 14.9 u | 19 | 19 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,89 | €-0,89 | -0.89% |
| gate - htx | €100,00 | 2026-11-20 | 21.1 u | 29 | 29 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,83 | €-2,83 | -2.83% |
| gate - htx | €150,00 | 2026-11-19 | 14.9 u | 19 | 19 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,34 | €-1,34 | -0.89% |
| gate - htx | €150,00 | 2026-11-20 | 21.1 u | 29 | 29 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-4,24 | €-4,24 | -2.83% |
| gate - htx | €200,00 | 2026-11-19 | 14.9 u | 19 | 19 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,78 | €-1,78 | -0.89% |
| gate - htx | €200,00 | 2026-11-20 | 21.1 u | 29 | 29 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-5,66 | €-5,66 | -2.83% |
| gate - htx | €2.000,00 | 2026-11-19 | 14.9 u | 19 | 14 | 5 | €1,09 | €0,17 (1x) | **€0,92** | 0.05% | €-17,82 | €-16,89 | -0.84% |
| gate - htx | €2.000,00 | 2026-11-20 | 21.1 u | 29 | 11 | 18 | €7,81 | €1,46 (8x) | **€6,35** | 0.32% | €-56,53 | €-50,19 | -2.51% |
| gate - htx | €5.000,00 | 2026-11-19 | 14.9 u | 19 | 6 | 13 | €9,08 | €4,50 (12x) | **€4,58** | 0.09% | €-44,56 | €-39,98 | -0.80% |
| gate - htx | €5.000,00 | 2026-11-20 | 21.1 u | 29 | 4 | 25 | €24,92 | €5,26 (19x) | **€19,66** | 0.39% | €-140,91 | €-121,26 | -2.43% |
| bitget - xt | €100,00 | 2026-11-19 | 14.9 u | 13 | 13 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €2,07 | €2,07 | 2.07% |
| bitget - xt | €100,00 | 2026-11-20 | 21.1 u | 6 | 6 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-4,04 | €-4,04 | -4.04% |
| bitget - xt | €150,00 | 2026-11-19 | 14.9 u | 13 | 13 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €3,11 | €3,11 | 2.07% |
| bitget - xt | €150,00 | 2026-11-20 | 21.1 u | 6 | 6 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-6,07 | €-6,07 | -4.04% |
| bitget - xt | €200,00 | 2026-11-19 | 14.9 u | 13 | 9 | 4 | €0,50 | €0,01 (3x) | **€0,50** | 0.25% | €4,15 | €4,64 | 2.32% |
| bitget - xt | €200,00 | 2026-11-20 | 21.1 u | 6 | 6 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-8,09 | €-8,09 | -4.04% |
| bitget - xt | €2.000,00 | 2026-11-19 | 14.9 u | 13 | 4 | 9 | €9,96 | €1,95 (11x) | **€8,00** | 0.40% | €41,46 | €49,46 | 2.47% |
| bitget - xt | €2.000,00 | 2026-11-20 | 21.1 u | 6 | 0 | 6 | €7,25 | €2,06 (7x) | **€5,19** | 0.26% | €-80,83 | €-75,64 | -3.78% |
| bitget - xt | €5.000,00 | 2026-11-19 | 14.9 u | 13 | 4 | 8 | €19,47 | €1,85 (10x) | **€17,62** | 0.35% | €103,65 | €121,27 | 2.43% |
| bitget - xt | €5.000,00 | 2026-11-20 | 21.1 u | 6 | 0 | 6 | €16,17 | €2,06 (7x) | **€14,11** | 0.28% | €-202,19 | €-188,08 | -3.76% |
| htx - kucoin | €100,00 | 2026-11-19 | 14.9 u | 16 | 16 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,17 | €-2,17 | -2.17% |
| htx - kucoin | €100,00 | 2026-11-20 | 21.1 u | 39 | 39 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,58 | €-3,58 | -3.58% |
| htx - kucoin | €150,00 | 2026-11-19 | 14.9 u | 16 | 16 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,26 | €-3,26 | -2.17% |
| htx - kucoin | €150,00 | 2026-11-20 | 21.1 u | 39 | 39 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-5,37 | €-5,37 | -3.58% |
| htx - kucoin | €200,00 | 2026-11-19 | 14.9 u | 16 | 16 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-4,34 | €-4,34 | -2.17% |
| htx - kucoin | €200,00 | 2026-11-20 | 21.1 u | 39 | 39 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-7,16 | €-7,16 | -3.58% |
| htx - kucoin | €2.000,00 | 2026-11-19 | 14.9 u | 16 | 9 | 7 | €1,40 | €0,00 (1x) | **€1,40** | 0.07% | €-43,43 | €-42,03 | -2.10% |
| htx - kucoin | €2.000,00 | 2026-11-20 | 21.1 u | 39 | 22 | 17 | €7,88 | €0,00 (1x) | **€7,88** | 0.39% | €-71,55 | €-63,67 | -3.18% |
| htx - kucoin | €5.000,00 | 2026-11-19 | 14.9 u | 16 | 3 | 13 | €7,48 | €3,83 (12x) | **€3,65** | 0.07% | €-108,48 | €-104,84 | -2.10% |
| htx - kucoin | €5.000,00 | 2026-11-20 | 21.1 u | 39 | 10 | 29 | €22,30 | €6,88 (21x) | **€15,41** | 0.31% | €-178,47 | €-163,05 | -3.26% |

- htx - xt, €100,00: munten BSV, CARV, CBK, HBAR, LUNC, MEME, RAIN, SEI, XCH, XDC, XMR; bruto zonder voorraadgrens zou €229,50 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - xt, €150,00: munten BSV, CARV, CBK, HBAR, LUNC, MEME, RAIN, SEI, XCH, XDC, XMR; bruto zonder voorraadgrens zou €229,50 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - xt, €200,00: munten BSV, CARV, CBK, HBAR, LUNC, MEME, RAIN, SEI, XCH, XDC, XMR; bruto zonder voorraadgrens zou €229,50 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - xt, €2.000,00: munten BSV, CARV, CBK, HBAR, LUNC, MEME, RAIN, SEI, XCH, XDC, XMR; bruto zonder voorraadgrens zou €228,05 zijn, met voorraad €18,26 (GEZIEN boek, GOK model).
- htx - xt, €5.000,00: munten BSV, CARV, CBK, HBAR, LUNC, MEME, RAIN, SEI, XCH, XDC, XMR; bruto zonder voorraadgrens zou €226,05 zijn, met voorraad €45,51 (GEZIEN boek, GOK model).
- kucoin - xt, €100,00: munten BARD, DAG, ENSO, FIGHT, LUNC, XMR; bruto zonder voorraadgrens zou €774,35 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- kucoin - xt, €150,00: munten BARD, DAG, ENSO, FIGHT, LUNC, XMR; bruto zonder voorraadgrens zou €774,35 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- kucoin - xt, €200,00: munten BARD, DAG, ENSO, FIGHT, LUNC, XMR; bruto zonder voorraadgrens zou €774,35 zijn, met voorraad €0,20 (GEZIEN boek, GOK model).
- kucoin - xt, €2.000,00: munten BARD, DAG, ENSO, FIGHT, LUNC, XMR; bruto zonder voorraadgrens zou €771,45 zijn, met voorraad €15,63 (GEZIEN boek, GOK model).
- kucoin - xt, €5.000,00: munten BARD, DAG, ENSO, FIGHT, LUNC, XMR; bruto zonder voorraadgrens zou €767,26 zijn, met voorraad €37,59 (GEZIEN boek, GOK model).
- gate - htx, €100,00: munten APEPE, BRISE, BSV, CBK, CRTS, ENJ, ENS, GOMINING, KAS, LAT, LUNC, MEME, MOVR, SEI, SSV, WARD, WLD, XCH, XCN; bruto zonder voorraadgrens zou €190,30 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- gate - htx, €150,00: munten APEPE, BRISE, BSV, CBK, CRTS, ENJ, ENS, GOMINING, KAS, LAT, LUNC, MEME, MOVR, SEI, SSV, WARD, WLD, XCH, XCN; bruto zonder voorraadgrens zou €190,30 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- gate - htx, €200,00: munten APEPE, BRISE, BSV, CBK, CRTS, ENJ, ENS, GOMINING, KAS, LAT, LUNC, MEME, MOVR, SEI, SSV, WARD, WLD, XCH, XCN; bruto zonder voorraadgrens zou €190,30 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- gate - htx, €2.000,00: munten APEPE, BRISE, BSV, CBK, CRTS, ENJ, ENS, GOMINING, KAS, LAT, LUNC, MEME, MOVR, SEI, SSV, WARD, WLD, XCH, XCN; bruto zonder voorraadgrens zou €189,64 zijn, met voorraad €8,90 (GEZIEN boek, GOK model).
- gate - htx, €5.000,00: munten APEPE, BRISE, BSV, CBK, CRTS, ENJ, ENS, GOMINING, KAS, LAT, LUNC, MEME, MOVR, SEI, SSV, WARD, WLD, XCH, XCN; bruto zonder voorraadgrens zou €185,45 zijn, met voorraad €34,00 (GEZIEN boek, GOK model).
- bitget - xt, €100,00: munten ENSO, KOR, KUB, LUNC, YB; bruto zonder voorraadgrens zou €885,90 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - xt, €150,00: munten ENSO, KOR, KUB, LUNC, YB; bruto zonder voorraadgrens zou €885,90 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - xt, €200,00: munten ENSO, KOR, KUB, LUNC, YB; bruto zonder voorraadgrens zou €885,47 zijn, met voorraad €0,50 (GEZIEN boek, GOK model).
- bitget - xt, €2.000,00: munten ENSO, KOR, KUB, LUNC, YB; bruto zonder voorraadgrens zou €880,51 zijn, met voorraad €17,21 (GEZIEN boek, GOK model).
- bitget - xt, €5.000,00: munten ENSO, KOR, KUB, LUNC, YB; bruto zonder voorraadgrens zou €873,91 zijn, met voorraad €35,64 (GEZIEN boek, GOK model).
- htx - kucoin, €100,00: munten ANIME, BSV, CFX, CHIP, ELA, ENJ, ENS, FET, JASMY, LAT, LUNC, MEME, MOVR, ONE, SOMI, SSV, WAN, WARD, WLD, XCH, XCN, XEC, XMR; bruto zonder voorraadgrens zou €194,58 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - kucoin, €150,00: munten ANIME, BSV, CFX, CHIP, ELA, ENJ, ENS, FET, JASMY, LAT, LUNC, MEME, MOVR, ONE, SOMI, SSV, WAN, WARD, WLD, XCH, XCN, XEC, XMR; bruto zonder voorraadgrens zou €194,58 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - kucoin, €200,00: munten ANIME, BSV, CFX, CHIP, ELA, ENJ, ENS, FET, JASMY, LAT, LUNC, MEME, MOVR, ONE, SOMI, SSV, WAN, WARD, WLD, XCH, XCN, XEC, XMR; bruto zonder voorraadgrens zou €194,58 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - kucoin, €2.000,00: munten ANIME, BSV, CFX, CHIP, ELA, ENJ, ENS, FET, JASMY, LAT, LUNC, MEME, MOVR, ONE, SOMI, SSV, WAN, WARD, WLD, XCH, XCN, XEC, XMR; bruto zonder voorraadgrens zou €194,01 zijn, met voorraad €9,28 (GEZIEN boek, GOK model).
- htx - kucoin, €5.000,00: munten ANIME, BSV, CFX, CHIP, ELA, ENJ, ENS, FET, JASMY, LAT, LUNC, MEME, MOVR, ONE, SOMI, SSV, WAN, WARD, WLD, XCH, XCN, XEC, XMR; bruto zonder voorraadgrens zou €193,16 zijn, met voorraad €29,77 (GEZIEN boek, GOK model).

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

- Opnamekosten bij de echte kansen: 130 van een netwerk dat aan beide kanten open is, 108 van de beurs zelf (laagste open netwerk), 74 geschat uit wat andere beurzen voor die munt vragen (GOK). Onbekende opnamekosten tellen niet als echte kans.
- Netwerk: KuCoin, Gate, Bitget, HTX, XT, Bitstamp, Bitvavo en Poloniex geven hun netwerken per munt. Als beide beurzen dat doen en de namen te koppelen zijn, moet er een netwerk zijn dat aan beide kanten open is. Anders is het netwerk "niet te koppelen" en telt de kans mee (staat apart in de trechter).
- De duur is gemeten in stappen van ±20 seconden; een kans kan een paar rondes eerder begonnen zijn dan we zagen.
- Takerkosten: uit de API waar die ze per paar geeft, anders het standaardtarief uit de README (deels GOK).
- Laatste run: 15 beurzen antwoordden, 2288 munt-quote-paren op minstens twee beurzen (GEZIEN).
