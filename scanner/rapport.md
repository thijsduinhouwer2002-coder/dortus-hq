# Rapport koersverschil-scanner

Gemaakt 2026-11-21 05:58 UTC uit 22 runs, samen ±43.1 uur gemeten (GEZIEN).
Echte kans = winst na alle kosten (opnamekosten bekend), opnemen en storten open (en een netwerk dat aan beide kanten open is, als de beurzen dat geven), minstens €100,00 op het boek, minstens 2 minuten blijven staan, geen andere munt met dezelfde naam.
**Vergund** = beide beurzen hebben een MiCA-vergunning (ESMA-register), vaak via een EU-dochter die minder munten kan hebben dan de wereldwijde API die we meten (GOK). **Grijs** = minstens één beurs zonder vergunning (MEXC, Bitget, HTX, Poloniex, XT, Bitfinex, Binance). Zie README.md.
**Kraken-tarief:** Kraken rekent 0,80% taker op munt tegen EUR, USD, USDT of USDC (GEZIEN, kraken.com/pro/fees, laagste trede); de scanner rekende tot 19 nov met 0,40%. 399 opgeslagen kansen met Kraken uit die runs zijn hier **opnieuw doorgerekend met 0,80%** (GOK-benadering: 0,40% van de inzet aan de Kraken-kant extra op elk gemeten punt van het boek; het boek zelf is niet bewaard). 233 houden daarna nog winst op het boek. Dat ze met hogere kosten ook korter bleven staan, telt niet mee (dus eerder te gunstig).

## Hoeveel wordt er gecontroleerd? (GEZIEN, stand.jsonl)

Per ronde (mediaan over 517 metingen): 1153 kandidaten (verschil op de ticker groter dan de takerkosten), 120 met het orderboek gecontroleerd, 2 nog nooit gecontroleerd (0%).
Bijna alle kandidaten komen aan de beurt; de aantallen hieronder missen weinig.

## Trechter (GEZIEN, eigen metingen)

| Stap | Alle beurzen | Alleen MiCA-beurzen | Met minstens één grijze beurs |
|---|---|---|---|
| Verschillen met winst op het boek na alle kosten | 41412 | 5729 | 35683 |
| ...waarvan opnemen of storten dicht | 7579 | 832 | 6747 |
| ...waarvan status onbekend (beurs geeft het niet openbaar) | 25196 | 4078 | 21118 |
| Opnemen en storten open | 8637 | 819 | 7818 |
| ...en geen netwerk dat aan beide kanten open is: valt af | 178 | 18 | 160 |
| ...en opnamekosten onbekend: valt af | 2 | 2 | 0 |
| ...en minstens €100,00 op het boek | 2411 | 499 | 1912 |
| ...en minstens 2 minuten blijven staan | 696 | 193 | 503 |
| ...en geen andere munt met dezelfde naam | 653 | 174 | 479 |
|    ...waarvan contractadres bekend en gelijk | 83 | 32 | 51 |
|    ...waarvan contractadres onbekend (telt mee, kan een andere munt zijn) | 570 | 142 | 428 |
|    ...waarvan netwerk gekoppeld en open | 419 | 80 | 339 |
|    ...waarvan netwerk niet te koppelen (telt mee) | 234 | 94 | 140 |
| **Echte kansen** (zelfde munt overlappend in de tijd samengevoegd, beste beurspaar telt) | 394 | 171 | 286 |
| Ter vergelijking: zelfde eisen, maar opnamestatus onbekend (niet meegeteld) | 1481 | 323 | 1275 |

## Echte kansen per dag (GEZIEN)

| Dag | Echt, alleen MiCA | Echt, met grijs | Mediane winst per kans bij €500 (MiCA / grijs) | Mediane duur |
|---|---|---|---|---|
| 2026-11-19 | 49 | 86 | €2,00 / €1,21 | 5.3 min |
| 2026-11-20 | 53 | 138 | €1,01 / €1,13 | 6.7 min |
| 2026-11-21 | 17 | 51 | €6,72 / €1,18 | 6.3 min |
| Totaal | 119 | 275 | €1,58 / €1,18 | 6.0 min |

## Beste munten (GEZIEN)

| | Soort | Kansen | Som winst bij €500 per kans |
|---|---|---|---|
| MERL-EUR | vergund | 27 | €783,52 |
| LUNC-USDT | grijs | 15 | €84,35 |
| USTC-USDT | grijs en vergund | 15 | €56,65 |
| KERNEL-EUR | vergund | 1 | €47,33 |
| MEME-USDT | grijs | 1 | €37,90 |
| KYO-USDT | vergund | 5 | €30,94 |
| ENSO-USDT | grijs en vergund | 7 | €28,37 |
| BSV-USDT | grijs | 19 | €27,94 |
| BARD-USDT | grijs | 4 | €24,39 |
| SKY-USD | vergund | 2 | €21,52 |

## Beste beursparen (kopen op > verkopen op) (GEZIEN)

| | Soort | Kansen | Som winst bij €500 per kans |
|---|---|---|---|
| bitvavo > kraken | vergund | 65 | €876,73 |
| bitget > htx | grijs | 65 | €130,72 |
| gate > kucoin | vergund | 29 | €83,55 |
| kucoin > htx | grijs | 35 | €74,87 |
| kucoin > bitget | grijs | 22 | €62,32 |
| bitget > xt | grijs | 13 | €44,44 |
| gate > htx | grijs | 19 | €38,08 |
| bitget > kucoin | grijs | 22 | €34,65 |
| bitget > gate | grijs | 12 | €32,74 |
| gate > xt | grijs | 5 | €31,18 |

Beurzen die het vaakst meedoen (koop of verkoop): bitget (grijs) 169, kucoin 153, htx (grijs) 145, gate 94, kraken 94, bitvavo 65, xt (grijs) 44, poloniex (grijs) 20 (GEZIEN).

## Hoeveel kansen blijven staan terwijl je geld schuift? (GEZIEN, duur uit eigen metingen)

Wie geen voorraad op beide beurzen heeft, moet kopen, de munt opnemen, wachten tot hij binnen is en dan verkopen. Hoe lang dat duurt verschilt per munt en netwerk: een paar minuten (snelle ketens) tot een uur of meer (Bitcoin, beurzen die opnames met de hand keuren) (GOK, niet per munt gemeten).

| Overmaaktijd | Alle beurzen | Alleen MiCA-beurzen | Met minstens één grijze beurs |
|---|---|---|---|
| 5 min | 234 van 394 (59%) | 98 van 171 (57%) | 175 van 286 (61%) |
| 10 min | 144 van 394 (37%) | 64 van 171 (37%) | 108 van 286 (38%) |
| 30 min | 72 van 394 (18%) | 38 van 171 (22%) | 55 van 286 (19%) |
| 60 min | 39 van 394 (10%) | 27 van 171 (16%) | 30 van 286 (10%) |

## Wat zou het opleveren over 3 maanden? (GOK, doorgetrokken uit de metingen)

Gemeten over ±43.1 uur (GEZIEN), doorgetrokken naar 90 dagen (GOK: aanname dat de week die we maten gewoon is).

| Beurzen | Inleg | Model | Kansen per uur | Per kans (mediaan) | 3 maanden |
|---|---|---|---|---|---|
| Alleen MiCA | €2.000,00 | bovengrens: elke kans, geld overal tegelijk | 3.97 | €1,64 | €14.070,66 |
| Alleen MiCA | €2.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 1.51 | €3,58 | €79.148,96 |
| Alleen MiCA | €5.000,00 | bovengrens: elke kans, geld overal tegelijk | 3.97 | €2,20 | €18.830,32 |
| Alleen MiCA | €5.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 1.51 | €3,94 | €150.544,31 |
| Alle (met grijs) | €2.000,00 | bovengrens: elke kans, geld overal tegelijk | 9.14 | €1,57 | €30.973,24 |
| Alle (met grijs) | €2.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 1.51 | €3,58 | €79.148,96 |
| Alle (met grijs) | €5.000,00 | bovengrens: elke kans, geld overal tegelijk | 9.14 | €1,78 | €35.186,49 |
| Alle (met grijs) | €5.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 1.51 | €3,94 | €150.544,31 |

Bovengrens: elke kans met de helft van de inleg aan elke kant, alsof het geld op alle beurzen tegelijk staat (kan in het echt niet). Beste beurspaar: het paar is **achteraf** gekozen uit de metingen (vooraf kiezen levert minder op), en het model neemt aan dat je van elke munt al voorraad op de verkoopbeurs hebt.

Waarom dit te rooskleurig is (GOK): elke kans wordt maar één keer geteld met het mediane boek, maar andere bots pakken hem ook; de munt die je als voorraad aanhoudt kan dalen; na een paar kansen moet de voorraad terug (opnamekosten en tijd); minimale opname- en ordergroottes tellen niet mee; en een kans die we 2 minuten zagen staan, staat er niet per se nog als jouw order binnenkomt. Waarom het te somber kan zijn: niet alle kandidaten zijn gecontroleerd, en met voorraad op beide beurzen kun je dezelfde kans vaker pakken als het boek zich aanvult; dat telt hier niet mee.

## Wat houd je echt over? Voorraad op twee beurzen (simulatie)

Per beurspaar: geld en munten op beide beurzen, elke echte kans uitgevoerd tegen het boek zoals gemeten (niet meer dan de ruimte op het boek en niet meer dan de voorraad op die beurs), terugschuiven als een kant leeg dreigt te raken (met opnamekosten en tijd onderweg), en het koerseffect van de aangehouden munten apart. Netto = bruto min kosten terugschuiven plus koerseffect. **Gemeten** (GEZIEN): de kansen, het boek en de koersen; **de rest is een rekenmodel** (GOK, aannames onder de tabel). Geen advies.

**Met €150: netto €0,59 per dag op bitstamp - kraken (koerseffect erbovenop €-1,52), €0,01 per dag op bitstamp - kucoin (koerseffect erbovenop €0,18), €0,25 per dag op bitvavo - kraken (koerseffect erbovenop €-2,40), €0,03 per dag op bitvavo - kucoin (koerseffect erbovenop €0,18), €0,07 per dag op gate - kucoin (koerseffect erbovenop €-0,51), €0,01 per dag op kraken - kucoin (koerseffect erbovenop €0,18) (GOK: netto handel, rekenmodel op ±14.4 uur meting per dag, alleen MiCA).** "Per dag" is hier gemiddeld over 3 gemeten dagen achter elkaar; de eerste begint met een gelijk verdeelde voorraad; aan het eind staat de voorraad scheef, dus een volgende dag levert waarschijnlijk minder op, tenzij kansen de andere kant op hem terugbrengen (GOK).

### Alleen MiCA-beurzen (alle paren met echte kansen)

| Beurspaar | Inleg | Dag | Gemeten | Kansen | Gemist (geen voorraad) | Kleiner door voorraad | Bruto winst | Kosten terugschuiven | **Netto handel (bruto min kosten)** | Rendement handel | Koerseffect voorraad | Netto met koerseffect | Rendement met koerseffect |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| bitstamp - kraken | €100,00 | 2026-11-19 | 14.9 u | 2 | 1 | 1 | €1,18 | €0,00 (0x) | **€1,18** | 1.18% | €0,63 | €1,81 | 1.81% |
| bitstamp - kraken | €100,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,38 | €-3,38 | -3.38% |
| bitstamp - kraken | €100,00 | 2026-11-21 | 5.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,28 | €-0,28 | -0.28% |
| bitstamp - kraken | €150,00 | 2026-11-19 | 14.9 u | 2 | 1 | 1 | €1,78 | €0,00 (0x) | **€1,78** | 1.18% | €0,94 | €2,72 | 1.81% |
| bitstamp - kraken | €150,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-5,07 | €-5,07 | -3.38% |
| bitstamp - kraken | €150,00 | 2026-11-21 | 5.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,42 | €-0,42 | -0.28% |
| bitstamp - kraken | €200,00 | 2026-11-19 | 14.9 u | 2 | 1 | 1 | €2,37 | €0,00 (0x) | **€2,37** | 1.18% | €1,25 | €3,62 | 1.81% |
| bitstamp - kraken | €200,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-6,76 | €-6,76 | -3.38% |
| bitstamp - kraken | €200,00 | 2026-11-21 | 5.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,56 | €-0,56 | -0.28% |
| bitstamp - kraken | €2.000,00 | 2026-11-19 | 14.9 u | 2 | 1 | 0 | €11,71 | €0,00 (0x) | **€11,71** | 0.59% | €12,53 | €24,24 | 1.21% |
| bitstamp - kraken | €2.000,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-67,63 | €-67,63 | -3.38% |
| bitstamp - kraken | €2.000,00 | 2026-11-21 | 5.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-5,62 | €-5,62 | -0.28% |
| bitstamp - kraken | €5.000,00 | 2026-11-19 | 14.9 u | 2 | 1 | 0 | €11,71 | €0,00 (0x) | **€11,71** | 0.23% | €31,33 | €43,04 | 0.86% |
| bitstamp - kraken | €5.000,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-169,08 | €-169,08 | -3.38% |
| bitstamp - kraken | €5.000,00 | 2026-11-21 | 5.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-14,04 | €-14,04 | -0.28% |
| bitstamp - kucoin | €100,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,11 | €0,11 | 0.11% |
| bitstamp - kucoin | €100,00 | 2026-11-20 | 22.8 u | 1 | 0 | 1 | €0,00 | €0,01 (1x) | **€-0,01** | -0.01% | €0,11 | €0,10 | 0.10% |
| bitstamp - kucoin | €100,00 | 2026-11-21 | 5.3 u | 4 | 3 | 1 | €0,01 | €0,00 (0x) | **€0,01** | 0.01% | €0,15 | €0,16 | 0.16% |
| bitstamp - kucoin | €150,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,16 | €0,16 | 0.11% |
| bitstamp - kucoin | €150,00 | 2026-11-20 | 22.8 u | 1 | 0 | 1 | €0,00 | €0,01 (1x) | **€-0,01** | -0.00% | €0,16 | €0,16 | 0.11% |
| bitstamp - kucoin | €150,00 | 2026-11-21 | 5.3 u | 4 | 3 | 1 | €0,02 | €0,00 (0x) | **€0,02** | 0.01% | €0,22 | €0,24 | 0.16% |
| bitstamp - kucoin | €200,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,22 | €0,22 | 0.11% |
| bitstamp - kucoin | €200,00 | 2026-11-20 | 22.8 u | 1 | 0 | 1 | €0,01 | €0,01 (1x) | **€-0,00** | -0.00% | €0,22 | €0,22 | 0.11% |
| bitstamp - kucoin | €200,00 | 2026-11-21 | 5.3 u | 4 | 3 | 1 | €0,03 | €0,23 (1x) | **€-0,21** | -0.10% | €0,29 | €0,08 | 0.04% |
| bitstamp - kucoin | €2.000,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €2,19 | €2,19 | 0.11% |
| bitstamp - kucoin | €2.000,00 | 2026-11-20 | 22.8 u | 1 | 0 | 1 | €0,05 | €0,01 (1x) | **€0,04** | 0.00% | €2,19 | €2,24 | 0.11% |
| bitstamp - kucoin | €2.000,00 | 2026-11-21 | 5.3 u | 4 | 3 | 1 | €0,27 | €1,23 (2x) | **€-0,97** | -0.05% | €2,91 | €1,94 | 0.10% |
| bitstamp - kucoin | €5.000,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €5,49 | €5,49 | 0.11% |
| bitstamp - kucoin | €5.000,00 | 2026-11-20 | 22.8 u | 1 | 0 | 1 | €0,13 | €0,01 (1x) | **€0,12** | 0.00% | €5,48 | €5,60 | 0.11% |
| bitstamp - kucoin | €5.000,00 | 2026-11-21 | 5.3 u | 4 | 3 | 1 | €0,64 | €1,23 (2x) | **€-0,59** | -0.01% | €7,27 | €6,67 | 0.13% |
| bitvavo - kraken | €100,00 | 2026-11-19 | 14.9 u | 43 | 43 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,62 | €-0,62 | -0.62% |
| bitvavo - kraken | €100,00 | 2026-11-20 | 22.8 u | 15 | 15 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,69 | €-1,69 | -1.69% |
| bitvavo - kraken | €100,00 | 2026-11-21 | 5.3 u | 7 | 7 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,48 | €-2,48 | -2.48% |
| bitvavo - kraken | €150,00 | 2026-11-19 | 14.9 u | 43 | 43 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,93 | €-0,93 | -0.62% |
| bitvavo - kraken | €150,00 | 2026-11-20 | 22.8 u | 15 | 14 | 1 | €0,76 | €0,00 (0x) | **€0,76** | 0.51% | €-2,53 | €-1,77 | -1.18% |
| bitvavo - kraken | €150,00 | 2026-11-21 | 5.3 u | 7 | 7 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,72 | €-3,72 | -2.48% |
| bitvavo - kraken | €200,00 | 2026-11-19 | 14.9 u | 43 | 37 | 6 | €0,14 | €0,00 (0x) | **€0,14** | 0.07% | €-1,24 | €-1,10 | -0.55% |
| bitvavo - kraken | €200,00 | 2026-11-20 | 22.8 u | 15 | 14 | 1 | €1,01 | €0,00 (0x) | **€1,01** | 0.51% | €-3,38 | €-2,36 | -1.18% |
| bitvavo - kraken | €200,00 | 2026-11-21 | 5.3 u | 7 | 7 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-4,97 | €-4,97 | -2.48% |
| bitvavo - kraken | €2.000,00 | 2026-11-19 | 14.9 u | 43 | 27 | 16 | €11,14 | €6,40 (16x) | **€4,73** | 0.24% | €-12,31 | €-7,58 | -0.38% |
| bitvavo - kraken | €2.000,00 | 2026-11-20 | 22.8 u | 15 | 9 | 6 | €26,53 | €2,29 (5x) | **€24,24** | 1.21% | €-33,54 | €-9,31 | -0.47% |
| bitvavo - kraken | €2.000,00 | 2026-11-21 | 5.3 u | 7 | 4 | 3 | €20,10 | €0,97 (3x) | **€19,13** | 0.96% | €-49,24 | €-30,11 | -1.51% |
| bitvavo - kraken | €5.000,00 | 2026-11-19 | 14.9 u | 43 | 22 | 21 | €28,08 | €14,97 (24x) | **€13,11** | 0.26% | €-30,85 | €-17,74 | -0.35% |
| bitvavo - kraken | €5.000,00 | 2026-11-20 | 22.8 u | 15 | 2 | 13 | €68,91 | €12,31 (15x) | **€56,60** | 1.13% | €-83,17 | €-26,57 | -0.53% |
| bitvavo - kraken | €5.000,00 | 2026-11-21 | 5.3 u | 7 | 4 | 3 | €51,43 | €0,97 (3x) | **€50,45** | 1.01% | €-122,97 | €-72,52 | -1.45% |
| bitvavo - kucoin | €100,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,08 | €0,08 | 0.08% |
| bitvavo - kucoin | €100,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,13 | €0,13 | 0.13% |
| bitvavo - kucoin | €100,00 | 2026-11-21 | 5.3 u | 1 | 0 | 1 | €0,06 | €0,00 (0x) | **€0,06** | 0.06% | €0,15 | €0,21 | 0.21% |
| bitvavo - kucoin | €150,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,12 | €0,12 | 0.08% |
| bitvavo - kucoin | €150,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,20 | €0,20 | 0.13% |
| bitvavo - kucoin | €150,00 | 2026-11-21 | 5.3 u | 1 | 0 | 1 | €0,09 | €0,00 (0x) | **€0,09** | 0.06% | €0,22 | €0,32 | 0.21% |
| bitvavo - kucoin | €200,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,16 | €0,16 | 0.08% |
| bitvavo - kucoin | €200,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,26 | €0,26 | 0.13% |
| bitvavo - kucoin | €200,00 | 2026-11-21 | 5.3 u | 1 | 0 | 1 | €0,13 | €0,00 (0x) | **€0,13** | 0.06% | €0,30 | €0,42 | 0.21% |
| bitvavo - kucoin | €2.000,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €1,64 | €1,64 | 0.08% |
| bitvavo - kucoin | €2.000,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €2,63 | €2,63 | 0.13% |
| bitvavo - kucoin | €2.000,00 | 2026-11-21 | 5.3 u | 1 | 0 | 1 | €1,25 | €2,01 (2x) | **€-0,76** | -0.04% | €2,96 | €2,20 | 0.11% |
| bitvavo - kucoin | €5.000,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €4,11 | €4,11 | 0.08% |
| bitvavo - kucoin | €5.000,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €6,58 | €6,58 | 0.13% |
| bitvavo - kucoin | €5.000,00 | 2026-11-21 | 5.3 u | 1 | 0 | 1 | €2,87 | €2,01 (2x) | **€0,86** | 0.02% | €7,40 | €8,26 | 0.17% |
| gate - kucoin | €100,00 | 2026-11-19 | 14.9 u | 25 | 25 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,67 | €-0,67 | -0.67% |
| gate - kucoin | €100,00 | 2026-11-20 | 22.8 u | 46 | 46 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,27 | €-0,27 | -0.27% |
| gate - kucoin | €100,00 | 2026-11-21 | 5.3 u | 8 | 8 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,10 | €-0,10 | -0.10% |
| gate - kucoin | €150,00 | 2026-11-19 | 14.9 u | 25 | 25 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,00 | €-1,00 | -0.67% |
| gate - kucoin | €150,00 | 2026-11-20 | 22.8 u | 46 | 44 | 2 | €0,21 | €0,00 (1x) | **€0,21** | 0.14% | €-0,40 | €-0,19 | -0.12% |
| gate - kucoin | €150,00 | 2026-11-21 | 5.3 u | 8 | 8 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,14 | €-0,14 | -0.10% |
| gate - kucoin | €200,00 | 2026-11-19 | 14.9 u | 25 | 25 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,33 | €-1,33 | -0.67% |
| gate - kucoin | €200,00 | 2026-11-20 | 22.8 u | 46 | 43 | 3 | €0,22 | €0,00 (1x) | **€0,22** | 0.11% | €-0,53 | €-0,31 | -0.15% |
| gate - kucoin | €200,00 | 2026-11-21 | 5.3 u | 8 | 7 | 1 | €0,08 | €0,00 (0x) | **€0,08** | 0.04% | €-0,19 | €-0,11 | -0.06% |
| gate - kucoin | €2.000,00 | 2026-11-19 | 14.9 u | 25 | 11 | 14 | €1,73 | €1,28 (8x) | **€0,46** | 0.02% | €-13,30 | €-12,84 | -0.64% |
| gate - kucoin | €2.000,00 | 2026-11-20 | 22.8 u | 46 | 18 | 28 | €9,41 | €1,57 (13x) | **€7,83** | 0.39% | €-5,26 | €2,57 | 0.13% |
| gate - kucoin | €2.000,00 | 2026-11-21 | 5.3 u | 8 | 3 | 5 | €2,63 | €0,33 (2x) | **€2,30** | 0.12% | €-1,76 | €0,54 | 0.03% |
| gate - kucoin | €5.000,00 | 2026-11-19 | 14.9 u | 25 | 6 | 19 | €7,11 | €4,26 (18x) | **€2,84** | 0.06% | €-33,30 | €-30,45 | -0.61% |
| gate - kucoin | €5.000,00 | 2026-11-20 | 22.8 u | 46 | 9 | 37 | €27,66 | €6,42 (29x) | **€21,23** | 0.42% | €-13,08 | €8,16 | 0.16% |
| gate - kucoin | €5.000,00 | 2026-11-21 | 5.3 u | 8 | 0 | 8 | €6,78 | €0,89 (4x) | **€5,90** | 0.12% | €-4,23 | €1,66 | 0.03% |
| kraken - kucoin | €100,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,11 | €0,11 | 0.11% |
| kraken - kucoin | €100,00 | 2026-11-20 | 22.8 u | 15 | 13 | 2 | €0,03 | €0,01 (1x) | **€0,02** | 0.02% | €0,11 | €0,13 | 0.13% |
| kraken - kucoin | €100,00 | 2026-11-21 | 5.3 u | 7 | 7 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,15 | €0,15 | 0.15% |
| kraken - kucoin | €150,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,16 | €0,16 | 0.11% |
| kraken - kucoin | €150,00 | 2026-11-20 | 22.8 u | 15 | 13 | 2 | €0,05 | €0,01 (1x) | **€0,04** | 0.02% | €0,16 | €0,20 | 0.13% |
| kraken - kucoin | €150,00 | 2026-11-21 | 5.3 u | 7 | 7 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,22 | €0,22 | 0.15% |
| kraken - kucoin | €200,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,22 | €0,22 | 0.11% |
| kraken - kucoin | €200,00 | 2026-11-20 | 22.8 u | 15 | 13 | 2 | €0,06 | €0,24 (2x) | **€-0,18** | -0.09% | €0,22 | €0,04 | 0.02% |
| kraken - kucoin | €200,00 | 2026-11-21 | 5.3 u | 7 | 7 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,29 | €0,29 | 0.14% |
| kraken - kucoin | €2.000,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €2,19 | €2,19 | 0.11% |
| kraken - kucoin | €2.000,00 | 2026-11-20 | 22.8 u | 15 | 13 | 2 | €0,61 | €1,24 (3x) | **€-0,63** | -0.03% | €2,19 | €1,56 | 0.08% |
| kraken - kucoin | €2.000,00 | 2026-11-21 | 5.3 u | 7 | 7 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €2,91 | €2,91 | 0.15% |
| kraken - kucoin | €5.000,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €5,49 | €5,49 | 0.11% |
| kraken - kucoin | €5.000,00 | 2026-11-20 | 22.8 u | 15 | 13 | 2 | €1,53 | €1,24 (3x) | **€0,28** | 0.01% | €5,48 | €5,77 | 0.12% |
| kraken - kucoin | €5.000,00 | 2026-11-21 | 5.3 u | 7 | 7 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €7,27 | €7,27 | 0.15% |

- bitstamp - kraken, €100,00: munten SKY; bruto zonder voorraadgrens zou €22,30 zijn, met voorraad €1,18 (GEZIEN boek, GOK model).
- bitstamp - kraken, €150,00: munten SKY; bruto zonder voorraadgrens zou €21,71 zijn, met voorraad €1,78 (GEZIEN boek, GOK model).
- bitstamp - kraken, €200,00: munten SKY; bruto zonder voorraadgrens zou €21,12 zijn, met voorraad €2,37 (GEZIEN boek, GOK model).
- bitstamp - kraken, €2.000,00: munten SKY; bruto zonder voorraadgrens zou €11,71 zijn, met voorraad €11,71 (GEZIEN boek, GOK model).
- bitstamp - kraken, €5.000,00: munten SKY; bruto zonder voorraadgrens zou €11,71 zijn, met voorraad €11,71 (GEZIEN boek, GOK model).
- bitstamp - kucoin, €100,00: munten USDC, USDT; bruto zonder voorraadgrens zou €10,69 zijn, met voorraad €0,02 (GEZIEN boek, GOK model).
- bitstamp - kucoin, €150,00: munten USDC, USDT; bruto zonder voorraadgrens zou €10,69 zijn, met voorraad €0,02 (GEZIEN boek, GOK model).
- bitstamp - kucoin, €200,00: munten USDC, USDT; bruto zonder voorraadgrens zou €10,69 zijn, met voorraad €0,03 (GEZIEN boek, GOK model).
- bitstamp - kucoin, €2.000,00: munten USDC, USDT; bruto zonder voorraadgrens zou €10,69 zijn, met voorraad €0,32 (GEZIEN boek, GOK model).
- bitstamp - kucoin, €5.000,00: munten USDC, USDT; bruto zonder voorraadgrens zou €10,69 zijn, met voorraad €0,77 (GEZIEN boek, GOK model).
- bitvavo - kraken, €100,00: munten AVA, CVX, DYM, GMT, KERNEL, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €4.558,44 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitvavo - kraken, €150,00: munten AVA, CVX, DYM, GMT, KERNEL, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €4.558,44 zijn, met voorraad €0,76 (GEZIEN boek, GOK model).
- bitvavo - kraken, €200,00: munten AVA, CVX, DYM, GMT, KERNEL, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €4.558,03 zijn, met voorraad €1,15 (GEZIEN boek, GOK model).
- bitvavo - kraken, €2.000,00: munten AVA, CVX, DYM, GMT, KERNEL, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €4.501,15 zijn, met voorraad €57,77 (GEZIEN boek, GOK model).
- bitvavo - kraken, €5.000,00: munten AVA, CVX, DYM, GMT, KERNEL, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €4.414,06 zijn, met voorraad €148,41 (GEZIEN boek, GOK model).
- bitvavo - kucoin, €100,00: munten USDC; bruto zonder voorraadgrens zou €6,21 zijn, met voorraad €0,06 (GEZIEN boek, GOK model).
- bitvavo - kucoin, €150,00: munten USDC; bruto zonder voorraadgrens zou €6,21 zijn, met voorraad €0,09 (GEZIEN boek, GOK model).
- bitvavo - kucoin, €200,00: munten USDC; bruto zonder voorraadgrens zou €6,21 zijn, met voorraad €0,13 (GEZIEN boek, GOK model).
- bitvavo - kucoin, €2.000,00: munten USDC; bruto zonder voorraadgrens zou €6,21 zijn, met voorraad €1,25 (GEZIEN boek, GOK model).
- bitvavo - kucoin, €5.000,00: munten USDC; bruto zonder voorraadgrens zou €6,21 zijn, met voorraad €2,87 (GEZIEN boek, GOK model).
- gate - kucoin, €100,00: munten ALKIMI, AVAIL, BARD, CCD, CHR, CWEB, CYBER, EDEN, ENSO, ERG, FTT, HTR, IKA, IR, KYO, LUNC, NAKA, NIM, OVR, POKT, RARI, STREAM, SUPRA, USDS, USTC, VERONA; bruto zonder voorraadgrens zou €320,88 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- gate - kucoin, €150,00: munten ALKIMI, AVAIL, BARD, CCD, CHR, CWEB, CYBER, EDEN, ENSO, ERG, FTT, HTR, IKA, IR, KYO, LUNC, NAKA, NIM, OVR, POKT, RARI, STREAM, SUPRA, USDS, USTC, VERONA; bruto zonder voorraadgrens zou €320,88 zijn, met voorraad €0,21 (GEZIEN boek, GOK model).
- gate - kucoin, €200,00: munten ALKIMI, AVAIL, BARD, CCD, CHR, CWEB, CYBER, EDEN, ENSO, ERG, FTT, HTR, IKA, IR, KYO, LUNC, NAKA, NIM, OVR, POKT, RARI, STREAM, SUPRA, USDS, USTC, VERONA; bruto zonder voorraadgrens zou €320,85 zijn, met voorraad €0,30 (GEZIEN boek, GOK model).
- gate - kucoin, €2.000,00: munten ALKIMI, AVAIL, BARD, CCD, CHR, CWEB, CYBER, EDEN, ENSO, ERG, FTT, HTR, IKA, IR, KYO, LUNC, NAKA, NIM, OVR, POKT, RARI, STREAM, SUPRA, USDS, USTC, VERONA; bruto zonder voorraadgrens zou €319,28 zijn, met voorraad €13,77 (GEZIEN boek, GOK model).
- gate - kucoin, €5.000,00: munten ALKIMI, AVAIL, BARD, CCD, CHR, CWEB, CYBER, EDEN, ENSO, ERG, FTT, HTR, IKA, IR, KYO, LUNC, NAKA, NIM, OVR, POKT, RARI, STREAM, SUPRA, USDS, USTC, VERONA; bruto zonder voorraadgrens zou €315,11 zijn, met voorraad €41,54 (GEZIEN boek, GOK model).
- kraken - kucoin, €100,00: munten USDC, USDT; bruto zonder voorraadgrens zou €94,18 zijn, met voorraad €0,03 (GEZIEN boek, GOK model).
- kraken - kucoin, €150,00: munten USDC, USDT; bruto zonder voorraadgrens zou €94,17 zijn, met voorraad €0,05 (GEZIEN boek, GOK model).
- kraken - kucoin, €200,00: munten USDC, USDT; bruto zonder voorraadgrens zou €94,17 zijn, met voorraad €0,06 (GEZIEN boek, GOK model).
- kraken - kucoin, €2.000,00: munten USDC, USDT; bruto zonder voorraadgrens zou €93,89 zijn, met voorraad €0,61 (GEZIEN boek, GOK model).
- kraken - kucoin, €5.000,00: munten USDC, USDT; bruto zonder voorraadgrens zou €93,43 zijn, met voorraad €1,53 (GEZIEN boek, GOK model).

### Met minstens één grijze beurs (de 5 paren met de meeste bruto winst)

| Beurspaar | Inleg | Dag | Gemeten | Kansen | Gemist (geen voorraad) | Kleiner door voorraad | Bruto winst | Kosten terugschuiven | **Netto handel (bruto min kosten)** | Rendement handel | Koerseffect voorraad | Netto met koerseffect | Rendement met koerseffect |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| gate - htx | €100,00 | 2026-11-19 | 14.9 u | 19 | 19 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,14 | €-1,14 | -1.14% |
| gate - htx | €100,00 | 2026-11-20 | 22.8 u | 32 | 32 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,83 | €-2,83 | -2.83% |
| gate - htx | €100,00 | 2026-11-21 | 5.3 u | 15 | 15 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,10 | €-2,10 | -2.10% |
| gate - htx | €150,00 | 2026-11-19 | 14.9 u | 19 | 19 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,71 | €-1,71 | -1.14% |
| gate - htx | €150,00 | 2026-11-20 | 22.8 u | 32 | 32 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-4,25 | €-4,25 | -2.83% |
| gate - htx | €150,00 | 2026-11-21 | 5.3 u | 15 | 15 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,15 | €-3,15 | -2.10% |
| gate - htx | €200,00 | 2026-11-19 | 14.9 u | 19 | 19 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,28 | €-2,28 | -1.14% |
| gate - htx | €200,00 | 2026-11-20 | 22.8 u | 32 | 32 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-5,67 | €-5,67 | -2.83% |
| gate - htx | €200,00 | 2026-11-21 | 5.3 u | 15 | 15 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-4,19 | €-4,19 | -2.10% |
| gate - htx | €2.000,00 | 2026-11-19 | 14.9 u | 19 | 14 | 5 | €0,71 | €0,17 (1x) | **€0,55** | 0.03% | €-22,83 | €-22,29 | -1.11% |
| gate - htx | €2.000,00 | 2026-11-20 | 22.8 u | 32 | 12 | 20 | €5,31 | €0,66 (8x) | **€4,64** | 0.23% | €-56,68 | €-52,04 | -2.60% |
| gate - htx | €2.000,00 | 2026-11-21 | 5.3 u | 15 | 4 | 11 | €1,59 | €1,26 (5x) | **€0,33** | 0.02% | €-41,88 | €-41,55 | -2.08% |
| gate - htx | €5.000,00 | 2026-11-19 | 14.9 u | 19 | 7 | 12 | €5,67 | €3,57 (10x) | **€2,10** | 0.04% | €-57,12 | €-55,03 | -1.10% |
| gate - htx | €5.000,00 | 2026-11-20 | 22.8 u | 32 | 5 | 27 | €16,74 | €3,91 (17x) | **€12,83** | 0.26% | €-141,44 | €-128,61 | -2.57% |
| gate - htx | €5.000,00 | 2026-11-21 | 5.3 u | 15 | 3 | 12 | €4,28 | €1,34 (8x) | **€2,94** | 0.06% | €-104,25 | €-101,31 | -2.03% |
| kucoin - xt | €100,00 | 2026-11-19 | 14.9 u | 13 | 13 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,04 | €-0,04 | -0.04% |
| kucoin - xt | €100,00 | 2026-11-20 | 22.8 u | 10 | 10 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,34 | €-0,34 | -0.34% |
| kucoin - xt | €100,00 | 2026-11-21 | 5.3 u | 5 | 5 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,41 | €-0,41 | -0.41% |
| kucoin - xt | €150,00 | 2026-11-19 | 14.9 u | 13 | 13 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,06 | €-0,06 | -0.04% |
| kucoin - xt | €150,00 | 2026-11-20 | 22.8 u | 10 | 10 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,51 | €-0,51 | -0.34% |
| kucoin - xt | €150,00 | 2026-11-21 | 5.3 u | 5 | 5 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,61 | €-0,61 | -0.41% |
| kucoin - xt | €200,00 | 2026-11-19 | 14.9 u | 13 | 13 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,08 | €-0,08 | -0.04% |
| kucoin - xt | €200,00 | 2026-11-20 | 22.8 u | 10 | 10 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,67 | €-0,67 | -0.34% |
| kucoin - xt | €200,00 | 2026-11-21 | 5.3 u | 5 | 4 | 1 | €0,08 | €0,00 (0x) | **€0,08** | 0.04% | €-0,82 | €-0,74 | -0.37% |
| kucoin - xt | €2.000,00 | 2026-11-19 | 14.9 u | 13 | 4 | 9 | €7,46 | €3,65 (9x) | **€3,81** | 0.19% | €-0,84 | €2,97 | 0.15% |
| kucoin - xt | €2.000,00 | 2026-11-20 | 22.8 u | 10 | 2 | 8 | €6,79 | €2,29 (6x) | **€4,50** | 0.23% | €-6,61 | €-2,11 | -0.11% |
| kucoin - xt | €2.000,00 | 2026-11-21 | 5.3 u | 5 | 1 | 4 | €5,10 | €1,17 (2x) | **€3,93** | 0.20% | €-7,61 | €-3,68 | -0.18% |
| kucoin - xt | €5.000,00 | 2026-11-19 | 14.9 u | 13 | 3 | 10 | €17,66 | €5,50 (11x) | **€12,16** | 0.24% | €-2,02 | €10,14 | 0.20% |
| kucoin - xt | €5.000,00 | 2026-11-20 | 22.8 u | 10 | 1 | 8 | €16,90 | €6,03 (10x) | **€10,86** | 0.22% | €-16,83 | €-5,97 | -0.12% |
| kucoin - xt | €5.000,00 | 2026-11-21 | 5.3 u | 5 | 0 | 5 | €9,68 | €2,00 (3x) | **€7,68** | 0.15% | €-19,85 | €-12,16 | -0.24% |
| htx - xt | €100,00 | 2026-11-19 | 14.9 u | 18 | 18 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,84 | €-0,84 | -0.84% |
| htx - xt | €100,00 | 2026-11-20 | 22.8 u | 17 | 17 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,98 | €-2,98 | -2.98% |
| htx - xt | €100,00 | 2026-11-21 | 5.3 u | 5 | 5 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,50 | €-2,50 | -2.50% |
| htx - xt | €150,00 | 2026-11-19 | 14.9 u | 18 | 18 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,26 | €-1,26 | -0.84% |
| htx - xt | €150,00 | 2026-11-20 | 22.8 u | 17 | 17 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-4,47 | €-4,47 | -2.98% |
| htx - xt | €150,00 | 2026-11-21 | 5.3 u | 5 | 5 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,75 | €-3,75 | -2.50% |
| htx - xt | €200,00 | 2026-11-19 | 14.9 u | 18 | 18 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,68 | €-1,68 | -0.84% |
| htx - xt | €200,00 | 2026-11-20 | 22.8 u | 17 | 17 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-5,96 | €-5,96 | -2.98% |
| htx - xt | €200,00 | 2026-11-21 | 5.3 u | 5 | 5 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-5,00 | €-5,00 | -2.50% |
| htx - xt | €2.000,00 | 2026-11-19 | 14.9 u | 18 | 10 | 8 | €3,24 | €1,55 (4x) | **€1,68** | 0.08% | €-16,76 | €-15,08 | -0.75% |
| htx - xt | €2.000,00 | 2026-11-20 | 22.8 u | 17 | 8 | 9 | €8,17 | €0,51 (3x) | **€7,66** | 0.38% | €-59,52 | €-51,86 | -2.59% |
| htx - xt | €2.000,00 | 2026-11-21 | 5.3 u | 5 | 2 | 3 | €1,98 | €0,00 (0x) | **€1,98** | 0.10% | €-49,84 | €-47,86 | -2.39% |
| htx - xt | €5.000,00 | 2026-11-19 | 14.9 u | 18 | 5 | 13 | €12,56 | €6,17 (13x) | **€6,40** | 0.13% | €-41,94 | €-35,54 | -0.71% |
| htx - xt | €5.000,00 | 2026-11-20 | 22.8 u | 17 | 1 | 16 | €28,20 | €6,25 (13x) | **€21,94** | 0.44% | €-148,73 | €-126,79 | -2.54% |
| htx - xt | €5.000,00 | 2026-11-21 | 5.3 u | 5 | 2 | 3 | €3,39 | €0,00 (0x) | **€3,39** | 0.07% | €-124,18 | €-120,79 | -2.42% |
| htx - kucoin | €100,00 | 2026-11-19 | 14.9 u | 16 | 16 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,93 | €-1,93 | -1.93% |
| htx - kucoin | €100,00 | 2026-11-20 | 22.8 u | 42 | 42 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,44 | €-3,44 | -3.44% |
| htx - kucoin | €100,00 | 2026-11-21 | 5.3 u | 18 | 18 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,30 | €-2,30 | -2.30% |
| htx - kucoin | €150,00 | 2026-11-19 | 14.9 u | 16 | 16 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,89 | €-2,89 | -1.93% |
| htx - kucoin | €150,00 | 2026-11-20 | 22.8 u | 42 | 42 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-5,15 | €-5,15 | -3.44% |
| htx - kucoin | €150,00 | 2026-11-21 | 5.3 u | 18 | 18 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,45 | €-3,45 | -2.30% |
| htx - kucoin | €200,00 | 2026-11-19 | 14.9 u | 16 | 16 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,85 | €-3,85 | -1.93% |
| htx - kucoin | €200,00 | 2026-11-20 | 22.8 u | 42 | 42 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-6,87 | €-6,87 | -3.44% |
| htx - kucoin | €200,00 | 2026-11-21 | 5.3 u | 18 | 18 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-4,60 | €-4,60 | -2.30% |
| htx - kucoin | €2.000,00 | 2026-11-19 | 14.9 u | 16 | 9 | 7 | €0,95 | €0,00 (1x) | **€0,94** | 0.05% | €-38,55 | €-37,60 | -1.88% |
| htx - kucoin | €2.000,00 | 2026-11-20 | 22.8 u | 42 | 24 | 18 | €5,45 | €0,00 (1x) | **€5,45** | 0.27% | €-68,72 | €-63,27 | -3.16% |
| htx - kucoin | €2.000,00 | 2026-11-21 | 5.3 u | 18 | 8 | 10 | €1,10 | €0,00 (0x) | **€1,10** | 0.05% | €-45,99 | €-44,90 | -2.24% |
| htx - kucoin | €5.000,00 | 2026-11-19 | 14.9 u | 16 | 7 | 9 | €4,08 | €1,18 (6x) | **€2,90** | 0.06% | €-96,30 | €-93,40 | -1.87% |
| htx - kucoin | €5.000,00 | 2026-11-20 | 22.8 u | 42 | 15 | 27 | €14,45 | €3,82 (15x) | **€10,63** | 0.21% | €-171,68 | €-161,05 | -3.22% |
| htx - kucoin | €5.000,00 | 2026-11-21 | 5.3 u | 18 | 4 | 14 | €3,64 | €2,57 (8x) | **€1,07** | 0.02% | €-114,65 | €-113,58 | -2.27% |
| bitget - htx | €100,00 | 2026-11-19 | 14.9 u | 20 | 20 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €100,00 | 2026-11-20 | 22.8 u | 39 | 39 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €100,00 | 2026-11-21 | 5.3 u | 25 | 25 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €150,00 | 2026-11-19 | 14.9 u | 20 | 20 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €150,00 | 2026-11-20 | 22.8 u | 39 | 39 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €150,00 | 2026-11-21 | 5.3 u | 25 | 25 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €200,00 | 2026-11-19 | 14.9 u | 20 | 20 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €200,00 | 2026-11-20 | 22.8 u | 39 | 39 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €200,00 | 2026-11-21 | 5.3 u | 25 | 25 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €2.000,00 | 2026-11-19 | 14.9 u | 20 | 7 | 13 | €0,76 | €0,31 (7x) | **€0,45** | 0.02% | onbekend | onbekend* | onbekend* |
| bitget - htx | €2.000,00 | 2026-11-20 | 22.8 u | 39 | 11 | 28 | €3,94 | €1,28 (22x) | **€2,65** | 0.13% | onbekend | onbekend* | onbekend* |
| bitget - htx | €2.000,00 | 2026-11-21 | 5.3 u | 25 | 7 | 18 | €1,14 | €0,20 (12x) | **€0,94** | 0.05% | onbekend | onbekend* | onbekend* |
| bitget - htx | €5.000,00 | 2026-11-19 | 14.9 u | 20 | 6 | 14 | €1,95 | €0,70 (10x) | **€1,26** | 0.03% | onbekend | onbekend* | onbekend* |
| bitget - htx | €5.000,00 | 2026-11-20 | 22.8 u | 39 | 8 | 31 | €10,70 | €1,56 (27x) | **€9,14** | 0.18% | onbekend | onbekend* | onbekend* |
| bitget - htx | €5.000,00 | 2026-11-21 | 5.3 u | 25 | 3 | 22 | €3,90 | €0,56 (15x) | **€3,34** | 0.07% | onbekend | onbekend* | onbekend* |

- gate - htx, €100,00: munten APEPE, APT, ATOM, BRISE, BSV, CBK, CRTS, CVX, ENJ, ENS, GOMINING, KAS, LAT, LINK, LUNC, MBX, MEME, MOVR, NPC, PEOPLE, SEI, SHIB, SSV, VIRTUAL, WARD, WLD, XCH, XCN, XDC; bruto zonder voorraadgrens zou €283,07 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- gate - htx, €150,00: munten APEPE, APT, ATOM, BRISE, BSV, CBK, CRTS, CVX, ENJ, ENS, GOMINING, KAS, LAT, LINK, LUNC, MBX, MEME, MOVR, NPC, PEOPLE, SEI, SHIB, SSV, VIRTUAL, WARD, WLD, XCH, XCN, XDC; bruto zonder voorraadgrens zou €283,07 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- gate - htx, €200,00: munten APEPE, APT, ATOM, BRISE, BSV, CBK, CRTS, CVX, ENJ, ENS, GOMINING, KAS, LAT, LINK, LUNC, MBX, MEME, MOVR, NPC, PEOPLE, SEI, SHIB, SSV, VIRTUAL, WARD, WLD, XCH, XCN, XDC; bruto zonder voorraadgrens zou €283,07 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- gate - htx, €2.000,00: munten APEPE, APT, ATOM, BRISE, BSV, CBK, CRTS, CVX, ENJ, ENS, GOMINING, KAS, LAT, LINK, LUNC, MBX, MEME, MOVR, NPC, PEOPLE, SEI, SHIB, SSV, VIRTUAL, WARD, WLD, XCH, XCN, XDC; bruto zonder voorraadgrens zou €282,63 zijn, met voorraad €7,61 (GEZIEN boek, GOK model).
- gate - htx, €5.000,00: munten APEPE, APT, ATOM, BRISE, BSV, CBK, CRTS, CVX, ENJ, ENS, GOMINING, KAS, LAT, LINK, LUNC, MBX, MEME, MOVR, NPC, PEOPLE, SEI, SHIB, SSV, VIRTUAL, WARD, WLD, XCH, XCN, XDC; bruto zonder voorraadgrens zou €279,90 zijn, met voorraad €26,69 (GEZIEN boek, GOK model).
- kucoin - xt, €100,00: munten BARD, DAG, ENSO, FIGHT, LUNC, USDS, XMR; bruto zonder voorraadgrens zou €965,03 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- kucoin - xt, €150,00: munten BARD, DAG, ENSO, FIGHT, LUNC, USDS, XMR; bruto zonder voorraadgrens zou €965,03 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- kucoin - xt, €200,00: munten BARD, DAG, ENSO, FIGHT, LUNC, USDS, XMR; bruto zonder voorraadgrens zou €965,03 zijn, met voorraad €0,08 (GEZIEN boek, GOK model).
- kucoin - xt, €2.000,00: munten BARD, DAG, ENSO, FIGHT, LUNC, USDS, XMR; bruto zonder voorraadgrens zou €962,55 zijn, met voorraad €19,34 (GEZIEN boek, GOK model).
- kucoin - xt, €5.000,00: munten BARD, DAG, ENSO, FIGHT, LUNC, USDS, XMR; bruto zonder voorraadgrens zou €958,93 zijn, met voorraad €44,23 (GEZIEN boek, GOK model).
- htx - xt, €100,00: munten APT, BSV, CARV, CBK, HBAR, LUNC, MEME, PEOPLE, RAIN, SEI, XCH, XDC, XMR; bruto zonder voorraadgrens zou €327,30 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - xt, €150,00: munten APT, BSV, CARV, CBK, HBAR, LUNC, MEME, PEOPLE, RAIN, SEI, XCH, XDC, XMR; bruto zonder voorraadgrens zou €327,30 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - xt, €200,00: munten APT, BSV, CARV, CBK, HBAR, LUNC, MEME, PEOPLE, RAIN, SEI, XCH, XDC, XMR; bruto zonder voorraadgrens zou €327,30 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - xt, €2.000,00: munten APT, BSV, CARV, CBK, HBAR, LUNC, MEME, PEOPLE, RAIN, SEI, XCH, XDC, XMR; bruto zonder voorraadgrens zou €326,85 zijn, met voorraad €13,39 (GEZIEN boek, GOK model).
- htx - xt, €5.000,00: munten APT, BSV, CARV, CBK, HBAR, LUNC, MEME, PEOPLE, RAIN, SEI, XCH, XDC, XMR; bruto zonder voorraadgrens zou €324,21 zijn, met voorraad €44,15 (GEZIEN boek, GOK model).
- htx - kucoin, €100,00: munten ALGO, ANIME, APT, BONK, BSV, CFX, CHIP, CVX, DYDX, ELA, ENJ, ENS, FET, JASMY, LAT, LUNC, MEME, MOVR, NPC, ONE, PEOPLE, SHIB, SOMI, SSV, TRAC, VIRTUAL, WAN, WARD, WLD, XCH, XCN, XEC, XMR, XTZ; bruto zonder voorraadgrens zou €336,90 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - kucoin, €150,00: munten ALGO, ANIME, APT, BONK, BSV, CFX, CHIP, CVX, DYDX, ELA, ENJ, ENS, FET, JASMY, LAT, LUNC, MEME, MOVR, NPC, ONE, PEOPLE, SHIB, SOMI, SSV, TRAC, VIRTUAL, WAN, WARD, WLD, XCH, XCN, XEC, XMR, XTZ; bruto zonder voorraadgrens zou €336,90 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - kucoin, €200,00: munten ALGO, ANIME, APT, BONK, BSV, CFX, CHIP, CVX, DYDX, ELA, ENJ, ENS, FET, JASMY, LAT, LUNC, MEME, MOVR, NPC, ONE, PEOPLE, SHIB, SOMI, SSV, TRAC, VIRTUAL, WAN, WARD, WLD, XCH, XCN, XEC, XMR, XTZ; bruto zonder voorraadgrens zou €336,90 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - kucoin, €2.000,00: munten ALGO, ANIME, APT, BONK, BSV, CFX, CHIP, CVX, DYDX, ELA, ENJ, ENS, FET, JASMY, LAT, LUNC, MEME, MOVR, NPC, ONE, PEOPLE, SHIB, SOMI, SSV, TRAC, VIRTUAL, WAN, WARD, WLD, XCH, XCN, XEC, XMR, XTZ; bruto zonder voorraadgrens zou €336,37 zijn, met voorraad €7,50 (GEZIEN boek, GOK model).
- htx - kucoin, €5.000,00: munten ALGO, ANIME, APT, BONK, BSV, CFX, CHIP, CVX, DYDX, ELA, ENJ, ENS, FET, JASMY, LAT, LUNC, MEME, MOVR, NPC, ONE, PEOPLE, SHIB, SOMI, SSV, TRAC, VIRTUAL, WAN, WARD, WLD, XCH, XCN, XEC, XMR, XTZ; bruto zonder voorraadgrens zou €335,58 zijn, met voorraad €22,17 (GEZIEN boek, GOK model).
- bitget - htx, €100,00: munten AB, ACN, ALGO, ANIME, ATOM, BABY, BONK, BSV, CBK, CFX, CORE, DYDX, ENA, ENJ, ENS, HBAR, IOST, JASMY, KAS, LAT, LINK, LIT, LUNA, LUNC, MEME, MOVR, NPC, O, PEOPLE, RIVER, SHIB, SOMI, SSV, TAO, TIA, USTC, VIRTUAL, WARD, WLD, XDC, XTZ, ZEN; bruto zonder voorraadgrens zou €286,51 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - htx, €150,00: munten AB, ACN, ALGO, ANIME, ATOM, BABY, BONK, BSV, CBK, CFX, CORE, DYDX, ENA, ENJ, ENS, HBAR, IOST, JASMY, KAS, LAT, LINK, LIT, LUNA, LUNC, MEME, MOVR, NPC, O, PEOPLE, RIVER, SHIB, SOMI, SSV, TAO, TIA, USTC, VIRTUAL, WARD, WLD, XDC, XTZ, ZEN; bruto zonder voorraadgrens zou €286,51 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - htx, €200,00: munten AB, ACN, ALGO, ANIME, ATOM, BABY, BONK, BSV, CBK, CFX, CORE, DYDX, ENA, ENJ, ENS, HBAR, IOST, JASMY, KAS, LAT, LINK, LIT, LUNA, LUNC, MEME, MOVR, NPC, O, PEOPLE, RIVER, SHIB, SOMI, SSV, TAO, TIA, USTC, VIRTUAL, WARD, WLD, XDC, XTZ, ZEN; bruto zonder voorraadgrens zou €286,51 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - htx, €2.000,00: munten AB, ACN, ALGO, ANIME, ATOM, BABY, BONK, BSV, CBK, CFX, CORE, DYDX, ENA, ENJ, ENS, HBAR, IOST, JASMY, KAS, LAT, LINK, LIT, LUNA, LUNC, MEME, MOVR, NPC, O, PEOPLE, RIVER, SHIB, SOMI, SSV, TAO, TIA, USTC, VIRTUAL, WARD, WLD, XDC, XTZ, ZEN; bruto zonder voorraadgrens zou €286,26 zijn, met voorraad €5,83 (GEZIEN boek, GOK model).
- bitget - htx, €5.000,00: munten AB, ACN, ALGO, ANIME, ATOM, BABY, BONK, BSV, CBK, CFX, CORE, DYDX, ENA, ENJ, ENS, HBAR, IOST, JASMY, KAS, LAT, LINK, LIT, LUNA, LUNC, MEME, MOVR, NPC, O, PEOPLE, RIVER, SHIB, SOMI, SSV, TAO, TIA, USTC, VIRTUAL, WARD, WLD, XDC, XTZ, ZEN; bruto zonder voorraadgrens zou €285,83 zijn, met voorraad €16,55 (GEZIEN boek, GOK model).

### Andere keuzes bij bitvavo - kraken (netto handel, alle dagen samen; GOK)

| Keuze | Inleg | Kansen | Gemist | Bruto winst | Kosten terugschuiven | Netto handel |
|---|---|---|---|---|---|---|
| standaard (schuifdrempel 25%, kostengrens 1%) | €150,00 | 65 | 64 | €0,76 | €0,00 | **€0,76** |
| standaard (schuifdrempel 25%, kostengrens 1%) | €2.000,00 | 65 | 40 | €57,77 | €9,67 | **€48,10** |
| schuifdrempel 10% | €150,00 | 65 | 64 | €0,76 | €0,00 | **€0,76** |
| schuifdrempel 10% | €2.000,00 | 65 | 41 | €57,81 | €9,35 | **€48,45** |
| schuifdrempel 40% | €150,00 | 65 | 64 | €0,76 | €0,00 | **€0,76** |
| schuifdrempel 40% | €2.000,00 | 65 | 38 | €60,60 | €12,28 | **€48,32** |
| kostengrens 2% (achteraf vergeleken) | €150,00 | 65 | 64 | €0,76 | €0,00 | **€0,76** |
| kostengrens 2% (achteraf vergeleken) | €2.000,00 | 65 | 28 | €60,48 | €28,25 | **€32,23** |
| kostengrens 5% (achteraf vergeleken) | €150,00 | 65 | 64 | €0,76 | €0,00 | **€0,76** |
| kostengrens 5% (achteraf vergeleken) | €2.000,00 | 65 | 28 | €60,48 | €28,25 | **€32,23** |
| alleen MERL en KERNEL (meer voorraad per munt, achteraf gekozen) | €150,00 | 28 | 26 | €2,05 | €0,00 | **€2,05** |
| alleen MERL en KERNEL (meer voorraad per munt, achteraf gekozen) | €2.000,00 | 28 | 13 | €203,54 | €11,53 | **€192,01** |

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

- Opnamekosten bij de echte kansen: 169 van een netwerk dat aan beide kanten open is, 127 van de beurs zelf (laagste open netwerk), 98 geschat uit wat andere beurzen voor die munt vragen (GOK). Onbekende opnamekosten tellen niet als echte kans.
- Netwerk: KuCoin, Gate, Bitget, HTX, XT, Bitstamp, Bitvavo en Poloniex geven hun netwerken per munt. Als beide beurzen dat doen en de namen te koppelen zijn, moet er een netwerk zijn dat aan beide kanten open is. Anders is het netwerk "niet te koppelen" en telt de kans mee (staat apart in de trechter).
- De duur is gemeten in stappen van ±20 seconden; een kans kan een paar rondes eerder begonnen zijn dan we zagen.
- Takerkosten: uit de API waar die ze per paar geeft, anders het standaardtarief uit de README (deels GOK).
- Laatste run: 15 beurzen antwoordden, 2281 munt-quote-paren op minstens twee beurzen (GEZIEN).
