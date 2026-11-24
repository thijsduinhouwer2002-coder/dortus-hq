# Rapport koersverschil-scanner

Gemaakt 2026-11-24 01:57 UTC uit 35 runs, samen ±103.8 uur gemeten (GEZIEN).
Echte kans = winst na alle kosten (opnamekosten bekend), opnemen en storten open (en een netwerk dat aan beide kanten open is, als de beurzen dat geven), minstens €100,00 op het boek, minstens 2 minuten blijven staan, geen andere munt met dezelfde naam.
**Vergund** = beide beurzen hebben een MiCA-vergunning (ESMA-register), vaak via een EU-dochter die minder munten kan hebben dan de wereldwijde API die we meten (GOK). **Grijs** = minstens één beurs zonder vergunning (MEXC, Bitget, HTX, Poloniex, XT, Bitfinex, Binance). Zie README.md.
**Kraken-tarief:** Kraken rekent 0,80% taker op munt tegen EUR, USD, USDT of USDC (GEZIEN, kraken.com/pro/fees, laagste trede); de scanner rekende tot 19 nov met 0,40%. 399 opgeslagen kansen met Kraken uit die runs zijn hier **opnieuw doorgerekend met 0,80%** (GOK-benadering: 0,40% van de inzet aan de Kraken-kant extra op elk gemeten punt van het boek; het boek zelf is niet bewaard). 233 houden daarna nog winst op het boek. Dat ze met hogere kosten ook korter bleven staan, telt niet mee (dus eerder te gunstig).

## Hoeveel wordt er gecontroleerd? (GEZIEN, stand.jsonl)

Per ronde (mediaan over 1245 metingen): 1070 kandidaten (verschil op de ticker groter dan de takerkosten), 120 met het orderboek gecontroleerd, 3 nog nooit gecontroleerd (0%).
Bijna alle kandidaten komen aan de beurt; de aantallen hieronder missen weinig.

## Trechter (GEZIEN, eigen metingen)

| Stap | Alle beurzen | Alleen MiCA-beurzen | Met minstens één grijze beurs |
|---|---|---|---|
| Verschillen met winst op het boek na alle kosten | 88129 | 12576 | 75553 |
| ...waarvan opnemen of storten dicht | 15946 | 1749 | 14197 |
| ...waarvan status onbekend (beurs geeft het niet openbaar) | 53397 | 9046 | 44351 |
| Opnemen en storten open | 18786 | 1781 | 17005 |
| ...en geen netwerk dat aan beide kanten open is: valt af | 787 | 64 | 723 |
| ...en opnamekosten onbekend: valt af | 5 | 5 | 0 |
| ...en minstens €100,00 op het boek | 5779 | 1052 | 4727 |
| ...en minstens 2 minuten blijven staan | 1598 | 408 | 1190 |
| ...en geen andere munt met dezelfde naam | 1530 | 373 | 1157 |
|    ...waarvan contractadres bekend en gelijk | 248 | 75 | 173 |
|    ...waarvan contractadres onbekend (telt mee, kan een andere munt zijn) | 1282 | 298 | 984 |
|    ...waarvan netwerk gekoppeld en open | 993 | 183 | 810 |
|    ...waarvan netwerk niet te koppelen (telt mee) | 537 | 190 | 347 |
| **Echte kansen** (zelfde munt overlappend in de tijd samengevoegd, beste beurspaar telt) | 956 | 363 | 701 |
| Ter vergelijking: zelfde eisen, maar opnamestatus onbekend (niet meegeteld) | 3759 | 986 | 3136 |

## Echte kansen per dag (GEZIEN)

| Dag | Echt, alleen MiCA | Echt, met grijs | Mediane winst per kans bij €500 (MiCA / grijs) | Mediane duur |
|---|---|---|---|---|
| 2026-11-19 | 49 | 86 | €2,00 / €1,21 | 5.3 min |
| 2026-11-20 | 53 | 138 | €1,01 / €1,13 | 6.7 min |
| 2026-11-21 | 61 | 176 | €1,13 / €0,88 | 6.7 min |
| 2026-11-22 | 60 | 165 | €1,74 / €0,93 | 9.3 min |
| 2026-11-23 | 53 | 113 | €1,10 / €1,00 | 6.8 min |
| 2026-11-24 | 0 | 2 | geen / €1,56 | 2.6 min |
| Totaal | 276 | 680 | €1,33 / €0,98 | 6.7 min |

## Beste munten (GEZIEN)

| | Soort | Kansen | Som winst bij €500 per kans |
|---|---|---|---|
| MERL-EUR | vergund | 71 | €1.012,65 |
| AI-USDT | grijs | 24 | €246,23 |
| LUNC-USDT | grijs | 34 | €149,07 |
| PYR-USDT | grijs | 11 | €138,01 |
| USTC-USDT | grijs en vergund | 43 | €107,95 |
| NES-USDT | grijs en vergund | 8 | €95,21 |
| XMR-USDT | grijs | 65 | €85,01 |
| DCR-USDT | grijs en vergund | 2 | €52,11 |
| ENSO-USDT | grijs en vergund | 15 | €48,21 |
| KERNEL-EUR | vergund | 1 | €47,33 |

## Beste beursparen (kopen op > verkopen op) (GEZIEN)

| | Soort | Kansen | Som winst bij €500 per kans |
|---|---|---|---|
| bitvavo > kraken | vergund | 152 | €1.134,91 |
| htx > kucoin | grijs | 36 | €254,33 |
| htx > gate | grijs | 35 | €209,03 |
| bitget > htx | grijs | 96 | €193,74 |
| gate > kucoin | vergund | 54 | €166,12 |
| kucoin > bitget | grijs | 79 | €119,46 |
| bitget > kucoin | grijs | 63 | €113,35 |
| kucoin > htx | grijs | 48 | €106,71 |
| bitget > xt | grijs | 30 | €93,12 |
| gate > htx | grijs | 36 | €91,10 |

Beurzen die het vaakst meedoen (koop of verkoop): kucoin 413, bitget (grijs) 391, htx (grijs) 327, gate 234, kraken 191, bitvavo 167, poloniex (grijs) 103, xt (grijs) 83 (GEZIEN).

## Hoeveel kansen blijven staan terwijl je geld schuift? (GEZIEN, duur uit eigen metingen)

Wie geen voorraad op beide beurzen heeft, moet kopen, de munt opnemen, wachten tot hij binnen is en dan verkopen. Hoe lang dat duurt verschilt per munt en netwerk: een paar minuten (snelle ketens) tot een uur of meer (Bitcoin, beurzen die opnames met de hand keuren) (GOK, niet per munt gemeten).

| Overmaaktijd | Alle beurzen | Alleen MiCA-beurzen | Met minstens één grijze beurs |
|---|---|---|---|
| 5 min | 575 van 956 (60%) | 221 van 363 (61%) | 424 van 701 (60%) |
| 10 min | 385 van 956 (40%) | 154 van 363 (42%) | 284 van 701 (41%) |
| 30 min | 194 van 956 (20%) | 76 van 363 (21%) | 151 van 701 (22%) |
| 60 min | 111 van 956 (12%) | 50 van 363 (14%) | 87 van 701 (12%) |

## Wat zou het opleveren over 3 maanden? (GOK, doorgetrokken uit de metingen)

Gemeten over ±103.8 uur (GEZIEN), doorgetrokken naar 90 dagen (GOK: aanname dat de week die we maten gewoon is).

| Beurzen | Inleg | Model | Kansen per uur | Per kans (mediaan) | 3 maanden |
|---|---|---|---|---|---|
| Alleen MiCA | €2.000,00 | bovengrens: elke kans, geld overal tegelijk | 3.50 | €1,62 | €12.213,12 |
| Alleen MiCA | €2.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 1.47 | €3,12 | €42.516,78 |
| Alleen MiCA | €5.000,00 | bovengrens: elke kans, geld overal tegelijk | 3.50 | €1,90 | €14.370,69 |
| Alleen MiCA | €5.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 1.47 | €3,66 | €78.679,49 |
| Alle (met grijs) | €2.000,00 | bovengrens: elke kans, geld overal tegelijk | 9.21 | €1,38 | €27.471,54 |
| Alle (met grijs) | €2.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 1.47 | €3,12 | €42.516,78 |
| Alle (met grijs) | €5.000,00 | bovengrens: elke kans, geld overal tegelijk | 9.21 | €1,62 | €32.217,32 |
| Alle (met grijs) | €5.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 1.47 | €3,66 | €78.679,49 |

Bovengrens: elke kans met de helft van de inleg aan elke kant, alsof het geld op alle beurzen tegelijk staat (kan in het echt niet). Beste beurspaar: het paar is **achteraf** gekozen uit de metingen (vooraf kiezen levert minder op), en het model neemt aan dat je van elke munt al voorraad op de verkoopbeurs hebt.

Waarom dit te rooskleurig is (GOK): elke kans wordt maar één keer geteld met het mediane boek, maar andere bots pakken hem ook; de munt die je als voorraad aanhoudt kan dalen; na een paar kansen moet de voorraad terug (opnamekosten en tijd); minimale opname- en ordergroottes tellen niet mee; en een kans die we 2 minuten zagen staan, staat er niet per se nog als jouw order binnenkomt. Waarom het te somber kan zijn: niet alle kandidaten zijn gecontroleerd, en met voorraad op beide beurzen kun je dezelfde kans vaker pakken als het boek zich aanvult; dat telt hier niet mee.

## Wat houd je echt over? Voorraad op twee beurzen (simulatie)

Per beurspaar: geld en munten op beide beurzen, elke echte kans uitgevoerd tegen het boek zoals gemeten (niet meer dan de ruimte op het boek en niet meer dan de voorraad op die beurs), terugschuiven als een kant leeg dreigt te raken (met opnamekosten en tijd onderweg), en het koerseffect van de aangehouden munten apart. Netto = bruto min kosten terugschuiven plus koerseffect. **Gemeten** (GEZIEN): de kansen, het boek en de koersen; **de rest is een rekenmodel** (GOK, aannames onder de tabel). Geen advies.

**Met €150: netto €0,26 per dag op bitstamp - kraken (koerseffect erbovenop €-1,26), €0,00 per dag op bitstamp - kucoin (koerseffect erbovenop €0,08), €0,00 per dag op bitvavo - kraken (koerseffect erbovenop €-0,51), €0,01 per dag op bitvavo - kucoin (koerseffect erbovenop €-0,22), €0,00 per dag op gate - kucoin (koerseffect erbovenop €-1,26), €0,01 per dag op kraken - kucoin (koerseffect erbovenop €0,08) (GOK: netto handel, rekenmodel op ±17.3 uur meting per dag, alleen MiCA).** "Per dag" is hier gemiddeld over 6 gemeten dagen achter elkaar; de eerste begint met een gelijk verdeelde voorraad; aan het eind staat de voorraad scheef, dus een volgende dag levert waarschijnlijk minder op, tenzij kansen de andere kant op hem terugbrengen (GOK).

### Alleen MiCA-beurzen (alle paren met echte kansen)

| Beurspaar | Inleg | Dag | Gemeten | Kansen | Gemist (geen voorraad) | Kleiner door voorraad | Bruto winst | Kosten terugschuiven | **Netto handel (bruto min kosten)** | Rendement handel | Koerseffect voorraad | Netto met koerseffect | Rendement met koerseffect |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| bitstamp - kraken | €100,00 | 2026-11-19 | 14.9 u | 2 | 1 | 1 | €0,59 | €0,00 (0x) | **€0,59** | 0.59% | €-0,02 | €0,57 | 0.57% |
| bitstamp - kraken | €100,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,95 | €-2,95 | -2.95% |
| bitstamp - kraken | €100,00 | 2026-11-21 | 22.9 u | 1 | 0 | 1 | €0,45 | €0,00 (0x) | **€0,45** | 0.45% | €-0,70 | €-0,25 | -0.25% |
| bitstamp - kraken | €100,00 | 2026-11-22 | 22.1 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,42 | €-1,42 | -1.42% |
| bitstamp - kraken | €100,00 | 2026-11-23 | 19.7 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,23 | €-0,23 | -0.23% |
| bitstamp - kraken | €100,00 | 2026-11-24 | 1.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,30 | €0,30 | 0.30% |
| bitstamp - kraken | €150,00 | 2026-11-19 | 14.9 u | 2 | 1 | 1 | €0,89 | €0,00 (0x) | **€0,89** | 0.59% | €-0,03 | €0,85 | 0.57% |
| bitstamp - kraken | €150,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-4,43 | €-4,43 | -2.95% |
| bitstamp - kraken | €150,00 | 2026-11-21 | 22.9 u | 1 | 0 | 1 | €0,67 | €0,00 (0x) | **€0,67** | 0.45% | €-1,05 | €-0,38 | -0.25% |
| bitstamp - kraken | €150,00 | 2026-11-22 | 22.1 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,13 | €-2,13 | -1.42% |
| bitstamp - kraken | €150,00 | 2026-11-23 | 19.7 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,34 | €-0,34 | -0.23% |
| bitstamp - kraken | €150,00 | 2026-11-24 | 1.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,46 | €0,46 | 0.30% |
| bitstamp - kraken | €200,00 | 2026-11-19 | 14.9 u | 2 | 1 | 1 | €1,18 | €0,00 (0x) | **€1,18** | 0.59% | €-0,04 | €1,14 | 0.57% |
| bitstamp - kraken | €200,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-5,91 | €-5,91 | -2.95% |
| bitstamp - kraken | €200,00 | 2026-11-21 | 22.9 u | 1 | 0 | 1 | €0,89 | €0,00 (0x) | **€0,89** | 0.45% | €-1,40 | €-0,51 | -0.25% |
| bitstamp - kraken | €200,00 | 2026-11-22 | 22.1 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,85 | €-2,85 | -1.42% |
| bitstamp - kraken | €200,00 | 2026-11-23 | 19.7 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,46 | €-0,46 | -0.23% |
| bitstamp - kraken | €200,00 | 2026-11-24 | 1.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,61 | €0,61 | 0.30% |
| bitstamp - kraken | €2.000,00 | 2026-11-19 | 14.9 u | 2 | 1 | 0 | €11,71 | €0,98 (1x) | **€10,73** | 0.54% | €-0,46 | €10,27 | 0.51% |
| bitstamp - kraken | €2.000,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-59,03 | €-59,03 | -2.95% |
| bitstamp - kraken | €2.000,00 | 2026-11-21 | 22.9 u | 1 | 0 | 0 | €5,30 | €0,00 (0x) | **€5,30** | 0.26% | €-14,01 | €-8,71 | -0.44% |
| bitstamp - kraken | €2.000,00 | 2026-11-22 | 22.1 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-28,41 | €-28,41 | -1.42% |
| bitstamp - kraken | €2.000,00 | 2026-11-23 | 19.7 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-4,54 | €-4,54 | -0.23% |
| bitstamp - kraken | €2.000,00 | 2026-11-24 | 1.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €6,08 | €6,08 | 0.30% |
| bitstamp - kraken | €5.000,00 | 2026-11-19 | 14.9 u | 2 | 1 | 0 | €11,71 | €0,00 (0x) | **€11,71** | 0.23% | €-1,10 | €10,60 | 0.21% |
| bitstamp - kraken | €5.000,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-147,75 | €-147,75 | -2.95% |
| bitstamp - kraken | €5.000,00 | 2026-11-21 | 22.9 u | 1 | 0 | 0 | €5,30 | €0,00 (0x) | **€5,30** | 0.11% | €-35,01 | €-29,71 | -0.59% |
| bitstamp - kraken | €5.000,00 | 2026-11-22 | 22.1 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-71,15 | €-71,15 | -1.42% |
| bitstamp - kraken | €5.000,00 | 2026-11-23 | 19.7 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-11,41 | €-11,41 | -0.23% |
| bitstamp - kraken | €5.000,00 | 2026-11-24 | 1.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €15,18 | €15,18 | 0.30% |
| bitstamp - kucoin | €100,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,11 | €0,11 | 0.11% |
| bitstamp - kucoin | €100,00 | 2026-11-20 | 22.8 u | 1 | 0 | 1 | €0,00 | €0,01 (1x) | **€-0,01** | -0.01% | €0,11 | €0,10 | 0.10% |
| bitstamp - kucoin | €100,00 | 2026-11-21 | 22.9 u | 6 | 5 | 1 | €0,01 | €0,00 (0x) | **€0,01** | 0.01% | €-0,16 | €-0,15 | -0.15% |
| bitstamp - kucoin | €100,00 | 2026-11-22 | 22.1 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,08 | €-0,08 | -0.08% |
| bitstamp - kucoin | €100,00 | 2026-11-23 | 19.7 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,29 | €0,29 | 0.29% |
| bitstamp - kucoin | €100,00 | 2026-11-24 | 1.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,04 | €0,04 | 0.04% |
| bitstamp - kucoin | €150,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,16 | €0,16 | 0.11% |
| bitstamp - kucoin | €150,00 | 2026-11-20 | 22.8 u | 1 | 0 | 1 | €0,00 | €0,01 (1x) | **€-0,01** | -0.00% | €0,16 | €0,16 | 0.11% |
| bitstamp - kucoin | €150,00 | 2026-11-21 | 22.9 u | 6 | 5 | 1 | €0,02 | €0,00 (0x) | **€0,02** | 0.01% | €-0,24 | €-0,22 | -0.15% |
| bitstamp - kucoin | €150,00 | 2026-11-22 | 22.1 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,12 | €-0,12 | -0.08% |
| bitstamp - kucoin | €150,00 | 2026-11-23 | 19.7 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,44 | €0,44 | 0.29% |
| bitstamp - kucoin | €150,00 | 2026-11-24 | 1.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,05 | €0,05 | 0.04% |
| bitstamp - kucoin | €200,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,22 | €0,22 | 0.11% |
| bitstamp - kucoin | €200,00 | 2026-11-20 | 22.8 u | 1 | 0 | 1 | €0,01 | €0,01 (1x) | **€-0,00** | -0.00% | €0,22 | €0,22 | 0.11% |
| bitstamp - kucoin | €200,00 | 2026-11-21 | 22.9 u | 6 | 5 | 1 | €0,03 | €0,23 (1x) | **€-0,21** | -0.10% | €-0,32 | €-0,53 | -0.26% |
| bitstamp - kucoin | €200,00 | 2026-11-22 | 22.1 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,16 | €-0,16 | -0.08% |
| bitstamp - kucoin | €200,00 | 2026-11-23 | 19.7 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,58 | €0,58 | 0.29% |
| bitstamp - kucoin | €200,00 | 2026-11-24 | 1.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,07 | €0,07 | 0.04% |
| bitstamp - kucoin | €2.000,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €2,19 | €2,19 | 0.11% |
| bitstamp - kucoin | €2.000,00 | 2026-11-20 | 22.8 u | 1 | 0 | 1 | €0,05 | €0,01 (1x) | **€0,04** | 0.00% | €2,19 | €2,24 | 0.11% |
| bitstamp - kucoin | €2.000,00 | 2026-11-21 | 22.9 u | 6 | 5 | 1 | €0,27 | €1,23 (2x) | **€-0,97** | -0.05% | €-3,24 | €-4,20 | -0.21% |
| bitstamp - kucoin | €2.000,00 | 2026-11-22 | 22.1 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,59 | €-1,59 | -0.08% |
| bitstamp - kucoin | €2.000,00 | 2026-11-23 | 19.7 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €5,81 | €5,81 | 0.29% |
| bitstamp - kucoin | €2.000,00 | 2026-11-24 | 1.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,71 | €0,71 | 0.04% |
| bitstamp - kucoin | €5.000,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €5,49 | €5,49 | 0.11% |
| bitstamp - kucoin | €5.000,00 | 2026-11-20 | 22.8 u | 1 | 0 | 1 | €0,13 | €0,01 (1x) | **€0,12** | 0.00% | €5,48 | €5,60 | 0.11% |
| bitstamp - kucoin | €5.000,00 | 2026-11-21 | 22.9 u | 6 | 5 | 1 | €0,64 | €1,23 (2x) | **€-0,59** | -0.01% | €-8,09 | €-8,68 | -0.17% |
| bitstamp - kucoin | €5.000,00 | 2026-11-22 | 22.1 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,98 | €-3,98 | -0.08% |
| bitstamp - kucoin | €5.000,00 | 2026-11-23 | 19.7 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €14,53 | €14,53 | 0.29% |
| bitstamp - kucoin | €5.000,00 | 2026-11-24 | 1.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €1,78 | €1,78 | 0.04% |
| bitvavo - kraken | €100,00 | 2026-11-19 | 14.9 u | 43 | 43 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,87 | €-0,87 | -0.87% |
| bitvavo - kraken | €100,00 | 2026-11-20 | 22.8 u | 15 | 15 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,51 | €-1,51 | -1.51% |
| bitvavo - kraken | €100,00 | 2026-11-21 | 22.9 u | 26 | 26 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,57 | €-0,57 | -0.57% |
| bitvavo - kraken | €100,00 | 2026-11-22 | 22.1 u | 40 | 40 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,04 | €-0,04 | -0.04% |
| bitvavo - kraken | €100,00 | 2026-11-23 | 19.7 u | 28 | 28 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,64 | €0,64 | 0.64% |
| bitvavo - kraken | €100,00 | 2026-11-24 | 1.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,30 | €0,30 | 0.30% |
| bitvavo - kraken | €150,00 | 2026-11-19 | 14.9 u | 43 | 43 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,30 | €-1,30 | -0.87% |
| bitvavo - kraken | €150,00 | 2026-11-20 | 22.8 u | 15 | 15 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,27 | €-2,27 | -1.51% |
| bitvavo - kraken | €150,00 | 2026-11-21 | 22.9 u | 26 | 26 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,86 | €-0,86 | -0.57% |
| bitvavo - kraken | €150,00 | 2026-11-22 | 22.1 u | 40 | 40 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,06 | €-0,06 | -0.04% |
| bitvavo - kraken | €150,00 | 2026-11-23 | 19.7 u | 28 | 28 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,96 | €0,96 | 0.64% |
| bitvavo - kraken | €150,00 | 2026-11-24 | 1.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,45 | €0,45 | 0.30% |
| bitvavo - kraken | €200,00 | 2026-11-19 | 14.9 u | 43 | 43 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,74 | €-1,74 | -0.87% |
| bitvavo - kraken | €200,00 | 2026-11-20 | 22.8 u | 15 | 15 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,03 | €-3,03 | -1.51% |
| bitvavo - kraken | €200,00 | 2026-11-21 | 22.9 u | 26 | 26 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,14 | €-1,14 | -0.57% |
| bitvavo - kraken | €200,00 | 2026-11-22 | 22.1 u | 40 | 40 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,08 | €-0,08 | -0.04% |
| bitvavo - kraken | €200,00 | 2026-11-23 | 19.7 u | 28 | 28 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €1,28 | €1,28 | 0.64% |
| bitvavo - kraken | €200,00 | 2026-11-24 | 1.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,60 | €0,60 | 0.30% |
| bitvavo - kraken | €2.000,00 | 2026-11-19 | 14.9 u | 43 | 25 | 18 | €9,30 | €6,00 (17x) | **€3,31** | 0.17% | €-17,30 | €-14,00 | -0.70% |
| bitvavo - kraken | €2.000,00 | 2026-11-20 | 22.8 u | 15 | 9 | 6 | €17,49 | €2,29 (5x) | **€15,21** | 0.76% | €-30,01 | €-14,80 | -0.74% |
| bitvavo - kraken | €2.000,00 | 2026-11-21 | 22.9 u | 26 | 16 | 10 | €18,54 | €3,25 (8x) | **€15,29** | 0.76% | €-11,56 | €3,73 | 0.19% |
| bitvavo - kraken | €2.000,00 | 2026-11-22 | 22.1 u | 40 | 21 | 19 | €8,20 | €7,11 (20x) | **€1,10** | 0.05% | €-0,81 | €0,29 | 0.01% |
| bitvavo - kraken | €2.000,00 | 2026-11-23 | 19.7 u | 28 | 20 | 8 | €2,06 | €3,55 (9x) | **€-1,49** | -0.07% | €12,74 | €11,25 | 0.56% |
| bitvavo - kraken | €2.000,00 | 2026-11-24 | 1.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €5,93 | €5,93 | 0.30% |
| bitvavo - kraken | €5.000,00 | 2026-11-19 | 14.9 u | 43 | 17 | 26 | €26,11 | €16,86 (28x) | **€9,25** | 0.18% | €-43,33 | €-34,08 | -0.68% |
| bitvavo - kraken | €5.000,00 | 2026-11-20 | 22.8 u | 15 | 8 | 7 | €44,31 | €3,46 (6x) | **€40,84** | 0.82% | €-74,61 | €-33,77 | -0.68% |
| bitvavo - kraken | €5.000,00 | 2026-11-21 | 22.9 u | 26 | 14 | 12 | €49,08 | €7,52 (13x) | **€41,57** | 0.83% | €-28,54 | €13,03 | 0.26% |
| bitvavo - kraken | €5.000,00 | 2026-11-22 | 22.1 u | 40 | 20 | 20 | €22,44 | €9,07 (22x) | **€13,36** | 0.27% | €-1,76 | €11,61 | 0.23% |
| bitvavo - kraken | €5.000,00 | 2026-11-23 | 19.7 u | 28 | 14 | 14 | €6,89 | €6,12 (15x) | **€0,77** | 0.02% | €31,56 | €32,32 | 0.65% |
| bitvavo - kraken | €5.000,00 | 2026-11-24 | 1.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €14,71 | €14,71 | 0.29% |
| bitvavo - kucoin | €100,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,52 | €-0,52 | -0.52% |
| bitvavo - kucoin | €100,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,80 | €-1,80 | -1.80% |
| bitvavo - kucoin | €100,00 | 2026-11-21 | 22.9 u | 7 | 5 | 2 | €0,04 | €0,00 (0x) | **€0,04** | 0.04% | €0,78 | €0,82 | 0.82% |
| bitvavo - kucoin | €100,00 | 2026-11-22 | 22.1 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,45 | €0,45 | 0.45% |
| bitvavo - kucoin | €100,00 | 2026-11-23 | 19.7 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,05 | €0,05 | 0.05% |
| bitvavo - kucoin | €100,00 | 2026-11-24 | 1.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,16 | €0,16 | 0.16% |
| bitvavo - kucoin | €150,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,78 | €-0,78 | -0.52% |
| bitvavo - kucoin | €150,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,71 | €-2,71 | -1.80% |
| bitvavo - kucoin | €150,00 | 2026-11-21 | 22.9 u | 7 | 5 | 2 | €0,07 | €0,00 (0x) | **€0,07** | 0.04% | €1,17 | €1,23 | 0.82% |
| bitvavo - kucoin | €150,00 | 2026-11-22 | 22.1 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,68 | €0,68 | 0.45% |
| bitvavo - kucoin | €150,00 | 2026-11-23 | 19.7 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,08 | €0,08 | 0.05% |
| bitvavo - kucoin | €150,00 | 2026-11-24 | 1.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,24 | €0,24 | 0.16% |
| bitvavo - kucoin | €200,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,04 | €-1,04 | -0.52% |
| bitvavo - kucoin | €200,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,61 | €-3,61 | -1.80% |
| bitvavo - kucoin | €200,00 | 2026-11-21 | 22.9 u | 7 | 5 | 2 | €0,09 | €0,00 (0x) | **€0,09** | 0.04% | €1,56 | €1,65 | 0.82% |
| bitvavo - kucoin | €200,00 | 2026-11-22 | 22.1 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,91 | €0,91 | 0.45% |
| bitvavo - kucoin | €200,00 | 2026-11-23 | 19.7 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,10 | €0,10 | 0.05% |
| bitvavo - kucoin | €200,00 | 2026-11-24 | 1.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,32 | €0,32 | 0.16% |
| bitvavo - kucoin | €2.000,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-10,39 | €-10,39 | -0.52% |
| bitvavo - kucoin | €2.000,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-36,07 | €-36,07 | -1.80% |
| bitvavo - kucoin | €2.000,00 | 2026-11-21 | 22.9 u | 7 | 4 | 3 | €0,91 | €2,73 (3x) | **€-1,82** | -0.09% | €15,55 | €13,72 | 0.69% |
| bitvavo - kucoin | €2.000,00 | 2026-11-22 | 22.1 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €9,04 | €9,04 | 0.45% |
| bitvavo - kucoin | €2.000,00 | 2026-11-23 | 19.7 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €1,02 | €1,02 | 0.05% |
| bitvavo - kucoin | €2.000,00 | 2026-11-24 | 1.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €3,17 | €3,17 | 0.16% |
| bitvavo - kucoin | €5.000,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-25,99 | €-25,99 | -0.52% |
| bitvavo - kucoin | €5.000,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-90,18 | €-90,18 | -1.80% |
| bitvavo - kucoin | €5.000,00 | 2026-11-21 | 22.9 u | 7 | 4 | 3 | €2,24 | €2,73 (3x) | **€-0,49** | -0.01% | €38,94 | €38,45 | 0.77% |
| bitvavo - kucoin | €5.000,00 | 2026-11-22 | 22.1 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €22,63 | €22,63 | 0.45% |
| bitvavo - kucoin | €5.000,00 | 2026-11-23 | 19.7 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €2,55 | €2,55 | 0.05% |
| bitvavo - kucoin | €5.000,00 | 2026-11-24 | 1.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €7,94 | €7,94 | 0.16% |
| gate - kucoin | €100,00 | 2026-11-19 | 14.9 u | 25 | 25 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,34 | €-0,34 | -0.34% |
| gate - kucoin | €100,00 | 2026-11-20 | 22.8 u | 46 | 46 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,66 | €-0,66 | -0.66% |
| gate - kucoin | €100,00 | 2026-11-21 | 22.9 u | 46 | 46 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,91 | €-1,91 | -1.91% |
| gate - kucoin | €100,00 | 2026-11-22 | 22.1 u | 28 | 28 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,98 | €-1,98 | -1.98% |
| gate - kucoin | €100,00 | 2026-11-23 | 19.7 u | 32 | 32 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,32 | €-0,32 | -0.32% |
| gate - kucoin | €100,00 | 2026-11-24 | 1.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,14 | €0,14 | 0.14% |
| gate - kucoin | €150,00 | 2026-11-19 | 14.9 u | 25 | 25 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,51 | €-0,51 | -0.34% |
| gate - kucoin | €150,00 | 2026-11-20 | 22.8 u | 46 | 46 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,99 | €-0,99 | -0.66% |
| gate - kucoin | €150,00 | 2026-11-21 | 22.9 u | 46 | 46 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,86 | €-2,86 | -1.91% |
| gate - kucoin | €150,00 | 2026-11-22 | 22.1 u | 28 | 28 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,96 | €-2,96 | -1.98% |
| gate - kucoin | €150,00 | 2026-11-23 | 19.7 u | 32 | 32 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,48 | €-0,48 | -0.32% |
| gate - kucoin | €150,00 | 2026-11-24 | 1.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,21 | €0,21 | 0.14% |
| gate - kucoin | €200,00 | 2026-11-19 | 14.9 u | 25 | 25 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,68 | €-0,68 | -0.34% |
| gate - kucoin | €200,00 | 2026-11-20 | 22.8 u | 46 | 45 | 1 | €0,12 | €0,00 (0x) | **€0,12** | 0.06% | €-1,32 | €-1,20 | -0.60% |
| gate - kucoin | €200,00 | 2026-11-21 | 22.9 u | 46 | 46 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,81 | €-3,81 | -1.91% |
| gate - kucoin | €200,00 | 2026-11-22 | 22.1 u | 28 | 28 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,95 | €-3,95 | -1.98% |
| gate - kucoin | €200,00 | 2026-11-23 | 19.7 u | 32 | 32 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,64 | €-0,64 | -0.32% |
| gate - kucoin | €200,00 | 2026-11-24 | 1.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,28 | €0,28 | 0.14% |
| gate - kucoin | €2.000,00 | 2026-11-19 | 14.9 u | 25 | 17 | 8 | €0,85 | €0,00 (0x) | **€0,85** | 0.04% | €-6,77 | €-5,92 | -0.30% |
| gate - kucoin | €2.000,00 | 2026-11-20 | 22.8 u | 46 | 25 | 21 | €5,84 | €0,05 (3x) | **€5,79** | 0.29% | €-13,15 | €-7,37 | -0.37% |
| gate - kucoin | €2.000,00 | 2026-11-21 | 22.9 u | 46 | 34 | 12 | €3,11 | €0,01 (1x) | **€3,10** | 0.16% | €-38,13 | €-35,03 | -1.75% |
| gate - kucoin | €2.000,00 | 2026-11-22 | 22.1 u | 28 | 21 | 7 | €0,67 | €0,01 (2x) | **€0,66** | 0.03% | €-39,51 | €-38,85 | -1.94% |
| gate - kucoin | €2.000,00 | 2026-11-23 | 19.7 u | 32 | 26 | 6 | €0,93 | €0,10 (1x) | **€0,83** | 0.04% | €-6,37 | €-5,53 | -0.28% |
| gate - kucoin | €2.000,00 | 2026-11-24 | 1.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €2,77 | €2,77 | 0.14% |
| gate - kucoin | €5.000,00 | 2026-11-19 | 14.9 u | 25 | 10 | 15 | €2,89 | €2,10 (12x) | **€0,78** | 0.02% | €-16,91 | €-16,12 | -0.32% |
| gate - kucoin | €5.000,00 | 2026-11-20 | 22.8 u | 46 | 15 | 31 | €15,48 | €2,80 (19x) | **€12,68** | 0.25% | €-32,85 | €-20,17 | -0.40% |
| gate - kucoin | €5.000,00 | 2026-11-21 | 22.9 u | 46 | 15 | 31 | €10,72 | €3,48 (22x) | **€7,24** | 0.14% | €-95,34 | €-88,10 | -1.76% |
| gate - kucoin | €5.000,00 | 2026-11-22 | 22.1 u | 28 | 6 | 22 | €3,78 | €2,35 (17x) | **€1,43** | 0.03% | €-98,65 | €-97,23 | -1.94% |
| gate - kucoin | €5.000,00 | 2026-11-23 | 19.7 u | 32 | 13 | 19 | €4,52 | €2,18 (16x) | **€2,34** | 0.05% | €-16,16 | €-13,82 | -0.28% |
| gate - kucoin | €5.000,00 | 2026-11-24 | 1.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €6,89 | €6,89 | 0.14% |
| kraken - kucoin | €100,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,11 | €0,11 | 0.11% |
| kraken - kucoin | €100,00 | 2026-11-20 | 22.8 u | 15 | 13 | 2 | €0,03 | €0,01 (1x) | **€0,02** | 0.02% | €0,11 | €0,13 | 0.13% |
| kraken - kucoin | €100,00 | 2026-11-21 | 22.9 u | 12 | 12 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,16 | €-0,16 | -0.16% |
| kraken - kucoin | €100,00 | 2026-11-22 | 22.1 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,08 | €-0,08 | -0.08% |
| kraken - kucoin | €100,00 | 2026-11-23 | 19.7 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,29 | €0,29 | 0.29% |
| kraken - kucoin | €100,00 | 2026-11-24 | 1.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,04 | €0,04 | 0.04% |
| kraken - kucoin | €150,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,16 | €0,16 | 0.11% |
| kraken - kucoin | €150,00 | 2026-11-20 | 22.8 u | 15 | 13 | 2 | €0,05 | €0,01 (1x) | **€0,04** | 0.02% | €0,16 | €0,20 | 0.13% |
| kraken - kucoin | €150,00 | 2026-11-21 | 22.9 u | 12 | 12 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,24 | €-0,24 | -0.16% |
| kraken - kucoin | €150,00 | 2026-11-22 | 22.1 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,12 | €-0,12 | -0.08% |
| kraken - kucoin | €150,00 | 2026-11-23 | 19.7 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,44 | €0,44 | 0.29% |
| kraken - kucoin | €150,00 | 2026-11-24 | 1.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,05 | €0,05 | 0.04% |
| kraken - kucoin | €200,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,22 | €0,22 | 0.11% |
| kraken - kucoin | €200,00 | 2026-11-20 | 22.8 u | 15 | 13 | 2 | €0,06 | €0,24 (2x) | **€-0,18** | -0.09% | €0,22 | €0,04 | 0.02% |
| kraken - kucoin | €200,00 | 2026-11-21 | 22.9 u | 12 | 12 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,32 | €-0,32 | -0.16% |
| kraken - kucoin | €200,00 | 2026-11-22 | 22.1 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,16 | €-0,16 | -0.08% |
| kraken - kucoin | €200,00 | 2026-11-23 | 19.7 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,58 | €0,58 | 0.29% |
| kraken - kucoin | €200,00 | 2026-11-24 | 1.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,07 | €0,07 | 0.04% |
| kraken - kucoin | €2.000,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €2,19 | €2,19 | 0.11% |
| kraken - kucoin | €2.000,00 | 2026-11-20 | 22.8 u | 15 | 13 | 2 | €0,61 | €1,24 (3x) | **€-0,63** | -0.03% | €2,19 | €1,56 | 0.08% |
| kraken - kucoin | €2.000,00 | 2026-11-21 | 22.9 u | 12 | 12 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,24 | €-3,24 | -0.16% |
| kraken - kucoin | €2.000,00 | 2026-11-22 | 22.1 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,59 | €-1,59 | -0.08% |
| kraken - kucoin | €2.000,00 | 2026-11-23 | 19.7 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €5,81 | €5,81 | 0.29% |
| kraken - kucoin | €2.000,00 | 2026-11-24 | 1.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,71 | €0,71 | 0.04% |
| kraken - kucoin | €5.000,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €5,49 | €5,49 | 0.11% |
| kraken - kucoin | €5.000,00 | 2026-11-20 | 22.8 u | 15 | 13 | 2 | €1,53 | €1,24 (3x) | **€0,28** | 0.01% | €5,48 | €5,77 | 0.12% |
| kraken - kucoin | €5.000,00 | 2026-11-21 | 22.9 u | 12 | 12 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-8,09 | €-8,09 | -0.16% |
| kraken - kucoin | €5.000,00 | 2026-11-22 | 22.1 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,98 | €-3,98 | -0.08% |
| kraken - kucoin | €5.000,00 | 2026-11-23 | 19.7 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €14,53 | €14,53 | 0.29% |
| kraken - kucoin | €5.000,00 | 2026-11-24 | 1.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €1,78 | €1,78 | 0.04% |

- bitstamp - kraken, €100,00: munten IMX, SKY; bruto zonder voorraadgrens zou €28,19 zijn, met voorraad €1,04 (GEZIEN boek, GOK model).
- bitstamp - kraken, €150,00: munten IMX, SKY; bruto zonder voorraadgrens zou €27,89 zijn, met voorraad €1,56 (GEZIEN boek, GOK model).
- bitstamp - kraken, €200,00: munten IMX, SKY; bruto zonder voorraadgrens zou €27,60 zijn, met voorraad €2,08 (GEZIEN boek, GOK model).
- bitstamp - kraken, €2.000,00: munten IMX, SKY; bruto zonder voorraadgrens zou €17,01 zijn, met voorraad €17,01 (GEZIEN boek, GOK model).
- bitstamp - kraken, €5.000,00: munten IMX, SKY; bruto zonder voorraadgrens zou €17,01 zijn, met voorraad €17,01 (GEZIEN boek, GOK model).
- bitstamp - kucoin, €100,00: munten USDC, USDT; bruto zonder voorraadgrens zou €13,16 zijn, met voorraad €0,02 (GEZIEN boek, GOK model).
- bitstamp - kucoin, €150,00: munten USDC, USDT; bruto zonder voorraadgrens zou €13,16 zijn, met voorraad €0,02 (GEZIEN boek, GOK model).
- bitstamp - kucoin, €200,00: munten USDC, USDT; bruto zonder voorraadgrens zou €13,16 zijn, met voorraad €0,03 (GEZIEN boek, GOK model).
- bitstamp - kucoin, €2.000,00: munten USDC, USDT; bruto zonder voorraadgrens zou €13,16 zijn, met voorraad €0,32 (GEZIEN boek, GOK model).
- bitstamp - kucoin, €5.000,00: munten USDC, USDT; bruto zonder voorraadgrens zou €13,16 zijn, met voorraad €0,77 (GEZIEN boek, GOK model).
- bitvavo - kraken, €100,00: munten AERO, AVA, CVX, CYBER, DYM, GMT, KERNEL, LUNA, MERL, MLN, PROMPT, VELO; bruto zonder voorraadgrens zou €5.472,88 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitvavo - kraken, €150,00: munten AERO, AVA, CVX, CYBER, DYM, GMT, KERNEL, LUNA, MERL, MLN, PROMPT, VELO; bruto zonder voorraadgrens zou €5.472,88 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitvavo - kraken, €200,00: munten AERO, AVA, CVX, CYBER, DYM, GMT, KERNEL, LUNA, MERL, MLN, PROMPT, VELO; bruto zonder voorraadgrens zou €5.472,88 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitvavo - kraken, €2.000,00: munten AERO, AVA, CVX, CYBER, DYM, GMT, KERNEL, LUNA, MERL, MLN, PROMPT, VELO; bruto zonder voorraadgrens zou €5.426,23 zijn, met voorraad €55,60 (GEZIEN boek, GOK model).
- bitvavo - kraken, €5.000,00: munten AERO, AVA, CVX, CYBER, DYM, GMT, KERNEL, LUNA, MERL, MLN, PROMPT, VELO; bruto zonder voorraadgrens zou €5.359,42 zijn, met voorraad €148,83 (GEZIEN boek, GOK model).
- bitvavo - kucoin, €100,00: munten ETH, USDC; bruto zonder voorraadgrens zou €19,28 zijn, met voorraad €0,04 (GEZIEN boek, GOK model).
- bitvavo - kucoin, €150,00: munten ETH, USDC; bruto zonder voorraadgrens zou €19,28 zijn, met voorraad €0,07 (GEZIEN boek, GOK model).
- bitvavo - kucoin, €200,00: munten ETH, USDC; bruto zonder voorraadgrens zou €19,28 zijn, met voorraad €0,09 (GEZIEN boek, GOK model).
- bitvavo - kucoin, €2.000,00: munten ETH, USDC; bruto zonder voorraadgrens zou €19,28 zijn, met voorraad €0,91 (GEZIEN boek, GOK model).
- bitvavo - kucoin, €5.000,00: munten ETH, USDC; bruto zonder voorraadgrens zou €19,28 zijn, met voorraad €2,24 (GEZIEN boek, GOK model).
- gate - kucoin, €100,00: munten ALKIMI, AVAIL, BARD, CAMP, CCD, CHR, CWEB, CYBER, DCR, DMTR, EDEN, ENSO, EPIC, ERG, ESPORTS, EVAA, FTT, HIGH, HTR, IKA, IR, JST, KAVA, KYO, LSK, LUNC, NAKA, NES, NIM, OVR, POKT, POND, RARI, SD, SOUL, STREAM, SUPRA, USDS, USTC, VERONA, XU3O8; bruto zonder voorraadgrens zou €593,81 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- gate - kucoin, €150,00: munten ALKIMI, AVAIL, BARD, CAMP, CCD, CHR, CWEB, CYBER, DCR, DMTR, EDEN, ENSO, EPIC, ERG, ESPORTS, EVAA, FTT, HIGH, HTR, IKA, IR, JST, KAVA, KYO, LSK, LUNC, NAKA, NES, NIM, OVR, POKT, POND, RARI, SD, SOUL, STREAM, SUPRA, USDS, USTC, VERONA, XU3O8; bruto zonder voorraadgrens zou €593,81 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- gate - kucoin, €200,00: munten ALKIMI, AVAIL, BARD, CAMP, CCD, CHR, CWEB, CYBER, DCR, DMTR, EDEN, ENSO, EPIC, ERG, ESPORTS, EVAA, FTT, HIGH, HTR, IKA, IR, JST, KAVA, KYO, LSK, LUNC, NAKA, NES, NIM, OVR, POKT, POND, RARI, SD, SOUL, STREAM, SUPRA, USDS, USTC, VERONA, XU3O8; bruto zonder voorraadgrens zou €593,81 zijn, met voorraad €0,12 (GEZIEN boek, GOK model).
- gate - kucoin, €2.000,00: munten ALKIMI, AVAIL, BARD, CAMP, CCD, CHR, CWEB, CYBER, DCR, DMTR, EDEN, ENSO, EPIC, ERG, ESPORTS, EVAA, FTT, HIGH, HTR, IKA, IR, JST, KAVA, KYO, LSK, LUNC, NAKA, NES, NIM, OVR, POKT, POND, RARI, SD, SOUL, STREAM, SUPRA, USDS, USTC, VERONA, XU3O8; bruto zonder voorraadgrens zou €592,78 zijn, met voorraad €11,41 (GEZIEN boek, GOK model).
- gate - kucoin, €5.000,00: munten ALKIMI, AVAIL, BARD, CAMP, CCD, CHR, CWEB, CYBER, DCR, DMTR, EDEN, ENSO, EPIC, ERG, ESPORTS, EVAA, FTT, HIGH, HTR, IKA, IR, JST, KAVA, KYO, LSK, LUNC, NAKA, NES, NIM, OVR, POKT, POND, RARI, SD, SOUL, STREAM, SUPRA, USDS, USTC, VERONA, XU3O8; bruto zonder voorraadgrens zou €590,96 zijn, met voorraad €37,39 (GEZIEN boek, GOK model).
- kraken - kucoin, €100,00: munten USDC, USDT; bruto zonder voorraadgrens zou €120,83 zijn, met voorraad €0,03 (GEZIEN boek, GOK model).
- kraken - kucoin, €150,00: munten USDC, USDT; bruto zonder voorraadgrens zou €120,83 zijn, met voorraad €0,05 (GEZIEN boek, GOK model).
- kraken - kucoin, €200,00: munten USDC, USDT; bruto zonder voorraadgrens zou €120,82 zijn, met voorraad €0,06 (GEZIEN boek, GOK model).
- kraken - kucoin, €2.000,00: munten USDC, USDT; bruto zonder voorraadgrens zou €120,54 zijn, met voorraad €0,61 (GEZIEN boek, GOK model).
- kraken - kucoin, €5.000,00: munten USDC, USDT; bruto zonder voorraadgrens zou €120,08 zijn, met voorraad €1,53 (GEZIEN boek, GOK model).

### Met minstens één grijze beurs (de 5 paren met de meeste bruto winst)

| Beurspaar | Inleg | Dag | Gemeten | Kansen | Gemist (geen voorraad) | Kleiner door voorraad | Bruto winst | Kosten terugschuiven | **Netto handel (bruto min kosten)** | Rendement handel | Koerseffect voorraad | Netto met koerseffect | Rendement met koerseffect |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| htx - kucoin | €100,00 | 2026-11-19 | 14.9 u | 16 | 16 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,05 | €-1,05 | -1.05% |
| htx - kucoin | €100,00 | 2026-11-20 | 22.8 u | 42 | 42 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,92 | €-2,92 | -2.92% |
| htx - kucoin | €100,00 | 2026-11-21 | 22.9 u | 32 | 32 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,20 | €0,20 | 0.20% |
| htx - kucoin | €100,00 | 2026-11-22 | 22.1 u | 40 | 40 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,26 | €-0,26 | -0.26% |
| htx - kucoin | €100,00 | 2026-11-23 | 19.7 u | 15 | 15 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,60 | €0,60 | 0.60% |
| htx - kucoin | €100,00 | 2026-11-24 | 1.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,41 | €0,41 | 0.41% |
| htx - kucoin | €150,00 | 2026-11-19 | 14.9 u | 16 | 16 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,57 | €-1,57 | -1.05% |
| htx - kucoin | €150,00 | 2026-11-20 | 22.8 u | 42 | 42 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-4,38 | €-4,38 | -2.92% |
| htx - kucoin | €150,00 | 2026-11-21 | 22.9 u | 32 | 32 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,30 | €0,30 | 0.20% |
| htx - kucoin | €150,00 | 2026-11-22 | 22.1 u | 40 | 40 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,39 | €-0,39 | -0.26% |
| htx - kucoin | €150,00 | 2026-11-23 | 19.7 u | 15 | 15 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,89 | €0,89 | 0.60% |
| htx - kucoin | €150,00 | 2026-11-24 | 1.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,62 | €0,62 | 0.41% |
| htx - kucoin | €200,00 | 2026-11-19 | 14.9 u | 16 | 16 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,09 | €-2,09 | -1.05% |
| htx - kucoin | €200,00 | 2026-11-20 | 22.8 u | 42 | 42 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-5,84 | €-5,84 | -2.92% |
| htx - kucoin | €200,00 | 2026-11-21 | 22.9 u | 32 | 32 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,40 | €0,40 | 0.20% |
| htx - kucoin | €200,00 | 2026-11-22 | 22.1 u | 40 | 40 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,52 | €-0,52 | -0.26% |
| htx - kucoin | €200,00 | 2026-11-23 | 19.7 u | 15 | 15 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €1,19 | €1,19 | 0.60% |
| htx - kucoin | €200,00 | 2026-11-24 | 1.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,82 | €0,82 | 0.41% |
| htx - kucoin | €2.000,00 | 2026-11-19 | 14.9 u | 16 | 16 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-20,94 | €-20,94 | -1.05% |
| htx - kucoin | €2.000,00 | 2026-11-20 | 22.8 u | 42 | 42 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-58,41 | €-58,41 | -2.92% |
| htx - kucoin | €2.000,00 | 2026-11-21 | 22.9 u | 32 | 32 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €4,04 | €4,04 | 0.20% |
| htx - kucoin | €2.000,00 | 2026-11-22 | 22.1 u | 40 | 39 | 1 | €0,17 | €0,00 (0x) | **€0,17** | 0.01% | €-5,20 | €-5,03 | -0.25% |
| htx - kucoin | €2.000,00 | 2026-11-23 | 19.7 u | 15 | 13 | 2 | €2,53 | €0,10 (1x) | **€2,43** | 0.12% | €11,94 | €14,38 | 0.72% |
| htx - kucoin | €2.000,00 | 2026-11-24 | 1.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €8,23 | €8,23 | 0.41% |
| htx - kucoin | €5.000,00 | 2026-11-19 | 14.9 u | 16 | 9 | 7 | €1,39 | €0,00 (1x) | **€1,38** | 0.03% | €-52,35 | €-50,97 | -1.02% |
| htx - kucoin | €5.000,00 | 2026-11-20 | 22.8 u | 42 | 24 | 18 | €7,98 | €0,00 (1x) | **€7,98** | 0.16% | €-146,03 | €-138,05 | -2.76% |
| htx - kucoin | €5.000,00 | 2026-11-21 | 22.9 u | 32 | 13 | 19 | €2,70 | €0,27 (5x) | **€2,43** | 0.05% | €10,09 | €12,52 | 0.25% |
| htx - kucoin | €5.000,00 | 2026-11-22 | 22.1 u | 40 | 26 | 14 | €7,56 | €0,33 (4x) | **€7,24** | 0.14% | €-13,01 | €-5,78 | -0.12% |
| htx - kucoin | €5.000,00 | 2026-11-23 | 19.7 u | 15 | 8 | 7 | €2,10 | €0,31 (2x) | **€1,79** | 0.04% | €29,77 | €31,56 | 0.63% |
| htx - kucoin | €5.000,00 | 2026-11-24 | 1.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €20,57 | €20,57 | 0.41% |
| gate - htx | €100,00 | 2026-11-19 | 14.9 u | 19 | 19 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,85 | €-0,85 | -0.85% |
| gate - htx | €100,00 | 2026-11-20 | 22.8 u | 32 | 32 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,61 | €-2,61 | -2.61% |
| gate - htx | €100,00 | 2026-11-21 | 22.9 u | 36 | 36 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,17 | €0,17 | 0.17% |
| gate - htx | €100,00 | 2026-11-22 | 22.1 u | 35 | 35 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,79 | €-0,79 | -0.79% |
| gate - htx | €100,00 | 2026-11-23 | 19.7 u | 25 | 25 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,44 | €0,44 | 0.44% |
| gate - htx | €100,00 | 2026-11-24 | 1.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,41 | €0,41 | 0.41% |
| gate - htx | €150,00 | 2026-11-19 | 14.9 u | 19 | 19 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,27 | €-1,27 | -0.85% |
| gate - htx | €150,00 | 2026-11-20 | 22.8 u | 32 | 32 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,92 | €-3,92 | -2.61% |
| gate - htx | €150,00 | 2026-11-21 | 22.9 u | 36 | 36 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,25 | €0,25 | 0.17% |
| gate - htx | €150,00 | 2026-11-22 | 22.1 u | 35 | 35 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,19 | €-1,19 | -0.79% |
| gate - htx | €150,00 | 2026-11-23 | 19.7 u | 25 | 25 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,67 | €0,67 | 0.44% |
| gate - htx | €150,00 | 2026-11-24 | 1.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,61 | €0,61 | 0.41% |
| gate - htx | €200,00 | 2026-11-19 | 14.9 u | 19 | 19 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,70 | €-1,70 | -0.85% |
| gate - htx | €200,00 | 2026-11-20 | 22.8 u | 32 | 32 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-5,22 | €-5,22 | -2.61% |
| gate - htx | €200,00 | 2026-11-21 | 22.9 u | 36 | 36 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,34 | €0,34 | 0.17% |
| gate - htx | €200,00 | 2026-11-22 | 22.1 u | 35 | 35 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,59 | €-1,59 | -0.79% |
| gate - htx | €200,00 | 2026-11-23 | 19.7 u | 25 | 25 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,89 | €0,89 | 0.44% |
| gate - htx | €200,00 | 2026-11-24 | 1.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,81 | €0,81 | 0.41% |
| gate - htx | €2.000,00 | 2026-11-19 | 14.9 u | 19 | 19 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-16,97 | €-16,97 | -0.85% |
| gate - htx | €2.000,00 | 2026-11-20 | 22.8 u | 32 | 32 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-52,24 | €-52,24 | -2.61% |
| gate - htx | €2.000,00 | 2026-11-21 | 22.9 u | 36 | 36 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €3,39 | €3,39 | 0.17% |
| gate - htx | €2.000,00 | 2026-11-22 | 22.1 u | 35 | 33 | 2 | €0,23 | €0,05 (1x) | **€0,18** | 0.01% | €-15,85 | €-15,67 | -0.78% |
| gate - htx | €2.000,00 | 2026-11-23 | 19.7 u | 25 | 25 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €8,89 | €8,89 | 0.44% |
| gate - htx | €2.000,00 | 2026-11-24 | 1.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €8,10 | €8,10 | 0.41% |
| gate - htx | €5.000,00 | 2026-11-19 | 14.9 u | 19 | 14 | 5 | €0,99 | €0,17 (1x) | **€0,82** | 0.02% | €-42,41 | €-41,59 | -0.83% |
| gate - htx | €5.000,00 | 2026-11-20 | 22.8 u | 32 | 12 | 20 | €7,39 | €0,66 (8x) | **€6,73** | 0.13% | €-130,59 | €-123,87 | -2.48% |
| gate - htx | €5.000,00 | 2026-11-21 | 22.9 u | 36 | 13 | 23 | €5,03 | €1,00 (14x) | **€4,03** | 0.08% | €8,46 | €12,49 | 0.25% |
| gate - htx | €5.000,00 | 2026-11-22 | 22.1 u | 35 | 10 | 25 | €7,01 | €2,52 (22x) | **€4,49** | 0.09% | €-39,64 | €-35,15 | -0.70% |
| gate - htx | €5.000,00 | 2026-11-23 | 19.7 u | 25 | 16 | 9 | €3,39 | €0,40 (5x) | **€2,99** | 0.06% | €22,12 | €25,12 | 0.50% |
| gate - htx | €5.000,00 | 2026-11-24 | 1.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €20,23 | €20,23 | 0.40% |
| bitget - htx | €100,00 | 2026-11-19 | 14.9 u | 20 | 20 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €100,00 | 2026-11-20 | 22.8 u | 39 | 39 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €100,00 | 2026-11-21 | 22.9 u | 47 | 47 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €100,00 | 2026-11-22 | 22.1 u | 39 | 39 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €100,00 | 2026-11-23 | 19.7 u | 27 | 27 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €100,00 | 2026-11-24 | 1.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €150,00 | 2026-11-19 | 14.9 u | 20 | 20 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €150,00 | 2026-11-20 | 22.8 u | 39 | 39 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €150,00 | 2026-11-21 | 22.9 u | 47 | 47 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €150,00 | 2026-11-22 | 22.1 u | 39 | 39 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €150,00 | 2026-11-23 | 19.7 u | 27 | 27 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €150,00 | 2026-11-24 | 1.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €200,00 | 2026-11-19 | 14.9 u | 20 | 20 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €200,00 | 2026-11-20 | 22.8 u | 39 | 39 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €200,00 | 2026-11-21 | 22.9 u | 47 | 47 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €200,00 | 2026-11-22 | 22.1 u | 39 | 39 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €200,00 | 2026-11-23 | 19.7 u | 27 | 27 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €200,00 | 2026-11-24 | 1.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €2.000,00 | 2026-11-19 | 14.9 u | 20 | 20 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €2.000,00 | 2026-11-20 | 22.8 u | 39 | 39 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €2.000,00 | 2026-11-21 | 22.9 u | 47 | 47 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €2.000,00 | 2026-11-22 | 22.1 u | 39 | 38 | 1 | €0,19 | €0,00 (0x) | **€0,19** | 0.01% | onbekend | onbekend* | onbekend* |
| bitget - htx | €2.000,00 | 2026-11-23 | 19.7 u | 27 | 26 | 1 | €1,35 | €0,00 (0x) | **€1,35** | 0.07% | onbekend | onbekend* | onbekend* |
| bitget - htx | €2.000,00 | 2026-11-24 | 1.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €5.000,00 | 2026-11-19 | 14.9 u | 20 | 6 | 14 | €1,37 | €0,70 (10x) | **€0,67** | 0.01% | onbekend | onbekend* | onbekend* |
| bitget - htx | €5.000,00 | 2026-11-20 | 22.8 u | 39 | 8 | 31 | €7,47 | €0,64 (26x) | **€6,83** | 0.14% | onbekend | onbekend* | onbekend* |
| bitget - htx | €5.000,00 | 2026-11-21 | 22.9 u | 47 | 8 | 39 | €4,21 | €1,59 (31x) | **€2,61** | 0.05% | onbekend | onbekend* | onbekend* |
| bitget - htx | €5.000,00 | 2026-11-22 | 22.1 u | 39 | 17 | 22 | €5,01 | €0,86 (17x) | **€4,14** | 0.08% | onbekend | onbekend* | onbekend* |
| bitget - htx | €5.000,00 | 2026-11-23 | 19.7 u | 27 | 9 | 18 | €2,34 | €0,84 (15x) | **€1,51** | 0.03% | onbekend | onbekend* | onbekend* |
| bitget - htx | €5.000,00 | 2026-11-24 | 1.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| htx - xt | €100,00 | 2026-11-19 | 14.9 u | 18 | 18 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,14 | €-1,14 | -1.14% |
| htx - xt | €100,00 | 2026-11-20 | 22.8 u | 17 | 17 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,67 | €-2,67 | -2.67% |
| htx - xt | €100,00 | 2026-11-21 | 22.9 u | 15 | 15 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,04 | €0,04 | 0.04% |
| htx - xt | €100,00 | 2026-11-22 | 22.1 u | 15 | 15 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,55 | €-0,55 | -0.55% |
| htx - xt | €100,00 | 2026-11-23 | 19.7 u | 9 | 9 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,71 | €0,71 | 0.71% |
| htx - xt | €100,00 | 2026-11-24 | 1.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,43 | €0,43 | 0.43% |
| htx - xt | €150,00 | 2026-11-19 | 14.9 u | 18 | 18 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,71 | €-1,71 | -1.14% |
| htx - xt | €150,00 | 2026-11-20 | 22.8 u | 17 | 17 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-4,01 | €-4,01 | -2.67% |
| htx - xt | €150,00 | 2026-11-21 | 22.9 u | 15 | 15 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,07 | €0,07 | 0.04% |
| htx - xt | €150,00 | 2026-11-22 | 22.1 u | 15 | 15 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,83 | €-0,83 | -0.55% |
| htx - xt | €150,00 | 2026-11-23 | 19.7 u | 9 | 9 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €1,06 | €1,06 | 0.71% |
| htx - xt | €150,00 | 2026-11-24 | 1.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,64 | €0,64 | 0.43% |
| htx - xt | €200,00 | 2026-11-19 | 14.9 u | 18 | 18 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,27 | €-2,27 | -1.14% |
| htx - xt | €200,00 | 2026-11-20 | 22.8 u | 17 | 17 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-5,35 | €-5,35 | -2.67% |
| htx - xt | €200,00 | 2026-11-21 | 22.9 u | 15 | 15 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,09 | €0,09 | 0.04% |
| htx - xt | €200,00 | 2026-11-22 | 22.1 u | 15 | 15 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,10 | €-1,10 | -0.55% |
| htx - xt | €200,00 | 2026-11-23 | 19.7 u | 9 | 9 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €1,41 | €1,41 | 0.71% |
| htx - xt | €200,00 | 2026-11-24 | 1.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,85 | €0,85 | 0.43% |
| htx - xt | €2.000,00 | 2026-11-19 | 14.9 u | 18 | 14 | 4 | €0,65 | €0,00 (0x) | **€0,65** | 0.03% | €-22,74 | €-22,10 | -1.10% |
| htx - xt | €2.000,00 | 2026-11-20 | 22.8 u | 17 | 9 | 8 | €3,85 | €0,12 (2x) | **€3,73** | 0.19% | €-53,46 | €-49,73 | -2.49% |
| htx - xt | €2.000,00 | 2026-11-21 | 22.9 u | 15 | 7 | 8 | €3,02 | €0,01 (1x) | **€3,01** | 0.15% | €0,89 | €3,90 | 0.19% |
| htx - xt | €2.000,00 | 2026-11-22 | 22.1 u | 15 | 10 | 5 | €1,52 | €0,11 (1x) | **€1,41** | 0.07% | €-11,04 | €-9,63 | -0.48% |
| htx - xt | €2.000,00 | 2026-11-23 | 19.7 u | 9 | 6 | 3 | €0,53 | €0,00 (0x) | **€0,53** | 0.03% | €14,11 | €14,63 | 0.73% |
| htx - xt | €2.000,00 | 2026-11-24 | 1.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €8,51 | €8,51 | 0.43% |
| htx - xt | €5.000,00 | 2026-11-19 | 14.9 u | 18 | 5 | 13 | €6,22 | €4,29 (11x) | **€1,93** | 0.04% | €-56,90 | €-54,97 | -1.10% |
| htx - xt | €5.000,00 | 2026-11-20 | 22.8 u | 17 | 2 | 15 | €13,80 | €2,81 (9x) | **€11,00** | 0.22% | €-133,36 | €-122,37 | -2.45% |
| htx - xt | €5.000,00 | 2026-11-21 | 22.9 u | 15 | 2 | 13 | €9,71 | €1,54 (5x) | **€8,17** | 0.16% | €2,89 | €11,06 | 0.22% |
| htx - xt | €5.000,00 | 2026-11-22 | 22.1 u | 15 | 10 | 5 | €3,81 | €0,11 (1x) | **€3,70** | 0.07% | €-27,49 | €-23,79 | -0.48% |
| htx - xt | €5.000,00 | 2026-11-23 | 19.7 u | 9 | 6 | 3 | €1,32 | €0,65 (2x) | **€0,67** | 0.01% | €34,66 | €35,33 | 0.71% |
| htx - xt | €5.000,00 | 2026-11-24 | 1.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €21,23 | €21,23 | 0.42% |
| bitget - kucoin | €100,00 | 2026-11-19 | 14.9 u | 21 | 21 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,34 | €-0,34 | -0.34% |
| bitget - kucoin | €100,00 | 2026-11-20 | 22.8 u | 24 | 24 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,53 | €-1,53 | -1.53% |
| bitget - kucoin | €100,00 | 2026-11-21 | 22.9 u | 39 | 39 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,26 | €-0,26 | -0.26% |
| bitget - kucoin | €100,00 | 2026-11-22 | 22.1 u | 49 | 49 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,89 | €-1,89 | -1.89% |
| bitget - kucoin | €100,00 | 2026-11-23 | 19.7 u | 46 | 46 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,67 | €-0,67 | -0.67% |
| bitget - kucoin | €100,00 | 2026-11-24 | 1.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,25 | €0,25 | 0.25% |
| bitget - kucoin | €150,00 | 2026-11-19 | 14.9 u | 21 | 21 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,52 | €-0,52 | -0.34% |
| bitget - kucoin | €150,00 | 2026-11-20 | 22.8 u | 24 | 24 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,29 | €-2,29 | -1.53% |
| bitget - kucoin | €150,00 | 2026-11-21 | 22.9 u | 39 | 39 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,40 | €-0,40 | -0.26% |
| bitget - kucoin | €150,00 | 2026-11-22 | 22.1 u | 49 | 49 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,84 | €-2,84 | -1.89% |
| bitget - kucoin | €150,00 | 2026-11-23 | 19.7 u | 46 | 46 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,00 | €-1,00 | -0.67% |
| bitget - kucoin | €150,00 | 2026-11-24 | 1.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,37 | €0,37 | 0.25% |
| bitget - kucoin | €200,00 | 2026-11-19 | 14.9 u | 21 | 21 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,69 | €-0,69 | -0.34% |
| bitget - kucoin | €200,00 | 2026-11-20 | 22.8 u | 24 | 24 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,06 | €-3,06 | -1.53% |
| bitget - kucoin | €200,00 | 2026-11-21 | 22.9 u | 39 | 39 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,53 | €-0,53 | -0.26% |
| bitget - kucoin | €200,00 | 2026-11-22 | 22.1 u | 49 | 49 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,79 | €-3,79 | -1.89% |
| bitget - kucoin | €200,00 | 2026-11-23 | 19.7 u | 46 | 46 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,33 | €-1,33 | -0.67% |
| bitget - kucoin | €200,00 | 2026-11-24 | 1.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,50 | €0,50 | 0.25% |
| bitget - kucoin | €2.000,00 | 2026-11-19 | 14.9 u | 21 | 14 | 7 | €0,70 | €0,29 (2x) | **€0,41** | 0.02% | €-6,87 | €-6,46 | -0.32% |
| bitget - kucoin | €2.000,00 | 2026-11-20 | 22.8 u | 24 | 14 | 10 | €1,92 | €0,00 (2x) | **€1,92** | 0.10% | €-30,57 | €-28,65 | -1.43% |
| bitget - kucoin | €2.000,00 | 2026-11-21 | 22.9 u | 39 | 23 | 16 | €0,63 | €0,58 (10x) | **€0,05** | 0.00% | €-5,30 | €-5,25 | -0.26% |
| bitget - kucoin | €2.000,00 | 2026-11-22 | 22.1 u | 49 | 39 | 10 | €0,58 | €1,46 (8x) | **€-0,88** | -0.04% | €-37,88 | €-38,76 | -1.94% |
| bitget - kucoin | €2.000,00 | 2026-11-23 | 19.7 u | 46 | 46 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-13,28 | €-13,28 | -0.66% |
| bitget - kucoin | €2.000,00 | 2026-11-24 | 1.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €4,98 | €4,98 | 0.25% |
| bitget - kucoin | €5.000,00 | 2026-11-19 | 14.9 u | 21 | 8 | 13 | €3,69 | €2,26 (12x) | **€1,43** | 0.03% | €-17,19 | €-15,75 | -0.32% |
| bitget - kucoin | €5.000,00 | 2026-11-20 | 22.8 u | 24 | 6 | 18 | €7,50 | €2,20 (13x) | **€5,29** | 0.11% | €-76,31 | €-71,02 | -1.42% |
| bitget - kucoin | €5.000,00 | 2026-11-21 | 22.9 u | 39 | 12 | 27 | €5,25 | €4,44 (23x) | **€0,82** | 0.02% | €-13,04 | €-12,22 | -0.24% |
| bitget - kucoin | €5.000,00 | 2026-11-22 | 22.1 u | 49 | 42 | 7 | €1,97 | €0,01 (2x) | **€1,95** | 0.04% | €-94,59 | €-92,64 | -1.85% |
| bitget - kucoin | €5.000,00 | 2026-11-23 | 19.7 u | 46 | 33 | 13 | €2,28 | €1,19 (8x) | **€1,10** | 0.02% | €-33,17 | €-32,08 | -0.64% |
| bitget - kucoin | €5.000,00 | 2026-11-24 | 1.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €12,48 | €12,48 | 0.25% |

- htx - kucoin, €100,00: munten ACN, AI, ALGO, ANIME, APT, ATOM, BIO, BONK, BRISE, BSV, BTT, CAP, CELO, CFX, CHIP, CVX, DCR, DYDX, ELA, ENJ, ENS, ENSO, FET, JASMY, JST, KSM, LAT, LTC, LUNC, MAPO, MEME, MINA, MOVR, NES, NIGHT, NPC, ONE, PEOPLE, PUMP, QNT, RUNE, SAND, SD, SHIB, SOMI, SSV, TAO, TRAC, VIRTUAL, WAN, WARD, WIN, WLD, XCH, XCN, XEC, XMR, XTZ; bruto zonder voorraadgrens zou €854,58 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - kucoin, €150,00: munten ACN, AI, ALGO, ANIME, APT, ATOM, BIO, BONK, BRISE, BSV, BTT, CAP, CELO, CFX, CHIP, CVX, DCR, DYDX, ELA, ENJ, ENS, ENSO, FET, JASMY, JST, KSM, LAT, LTC, LUNC, MAPO, MEME, MINA, MOVR, NES, NIGHT, NPC, ONE, PEOPLE, PUMP, QNT, RUNE, SAND, SD, SHIB, SOMI, SSV, TAO, TRAC, VIRTUAL, WAN, WARD, WIN, WLD, XCH, XCN, XEC, XMR, XTZ; bruto zonder voorraadgrens zou €854,58 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - kucoin, €200,00: munten ACN, AI, ALGO, ANIME, APT, ATOM, BIO, BONK, BRISE, BSV, BTT, CAP, CELO, CFX, CHIP, CVX, DCR, DYDX, ELA, ENJ, ENS, ENSO, FET, JASMY, JST, KSM, LAT, LTC, LUNC, MAPO, MEME, MINA, MOVR, NES, NIGHT, NPC, ONE, PEOPLE, PUMP, QNT, RUNE, SAND, SD, SHIB, SOMI, SSV, TAO, TRAC, VIRTUAL, WAN, WARD, WIN, WLD, XCH, XCN, XEC, XMR, XTZ; bruto zonder voorraadgrens zou €854,58 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - kucoin, €2.000,00: munten ACN, AI, ALGO, ANIME, APT, ATOM, BIO, BONK, BRISE, BSV, BTT, CAP, CELO, CFX, CHIP, CVX, DCR, DYDX, ELA, ENJ, ENS, ENSO, FET, JASMY, JST, KSM, LAT, LTC, LUNC, MAPO, MEME, MINA, MOVR, NES, NIGHT, NPC, ONE, PEOPLE, PUMP, QNT, RUNE, SAND, SD, SHIB, SOMI, SSV, TAO, TRAC, VIRTUAL, WAN, WARD, WIN, WLD, XCH, XCN, XEC, XMR, XTZ; bruto zonder voorraadgrens zou €854,58 zijn, met voorraad €2,70 (GEZIEN boek, GOK model).
- htx - kucoin, €5.000,00: munten ACN, AI, ALGO, ANIME, APT, ATOM, BIO, BONK, BRISE, BSV, BTT, CAP, CELO, CFX, CHIP, CVX, DCR, DYDX, ELA, ENJ, ENS, ENSO, FET, JASMY, JST, KSM, LAT, LTC, LUNC, MAPO, MEME, MINA, MOVR, NES, NIGHT, NPC, ONE, PEOPLE, PUMP, QNT, RUNE, SAND, SD, SHIB, SOMI, SSV, TAO, TRAC, VIRTUAL, WAN, WARD, WIN, WLD, XCH, XCN, XEC, XMR, XTZ; bruto zonder voorraadgrens zou €853,80 zijn, met voorraad €21,73 (GEZIEN boek, GOK model).
- gate - htx, €100,00: munten AKT, ALGO, APEPE, APT, ATOM, BIO, BRISE, BSV, BTT, CBK, CELO, CORE, CRTS, CVX, ENJ, ENS, ENSO, GOMINING, GT, HBAR, HIVE, KAS, KCT, KSM, LAT, LINK, LUNC, M, MBX, MEGA, MEME, MOVR, NES, NPC, PENGU, PEOPLE, PYR, QNT, SAND, SC, SD, SEI, SHIB, SOMI, SSV, ULTIMA, VIRTUAL, WARD, WLD, XCH, XCN, XDC; bruto zonder voorraadgrens zou €761,90 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- gate - htx, €150,00: munten AKT, ALGO, APEPE, APT, ATOM, BIO, BRISE, BSV, BTT, CBK, CELO, CORE, CRTS, CVX, ENJ, ENS, ENSO, GOMINING, GT, HBAR, HIVE, KAS, KCT, KSM, LAT, LINK, LUNC, M, MBX, MEGA, MEME, MOVR, NES, NPC, PENGU, PEOPLE, PYR, QNT, SAND, SC, SD, SEI, SHIB, SOMI, SSV, ULTIMA, VIRTUAL, WARD, WLD, XCH, XCN, XDC; bruto zonder voorraadgrens zou €761,90 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- gate - htx, €200,00: munten AKT, ALGO, APEPE, APT, ATOM, BIO, BRISE, BSV, BTT, CBK, CELO, CORE, CRTS, CVX, ENJ, ENS, ENSO, GOMINING, GT, HBAR, HIVE, KAS, KCT, KSM, LAT, LINK, LUNC, M, MBX, MEGA, MEME, MOVR, NES, NPC, PENGU, PEOPLE, PYR, QNT, SAND, SC, SD, SEI, SHIB, SOMI, SSV, ULTIMA, VIRTUAL, WARD, WLD, XCH, XCN, XDC; bruto zonder voorraadgrens zou €761,90 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- gate - htx, €2.000,00: munten AKT, ALGO, APEPE, APT, ATOM, BIO, BRISE, BSV, BTT, CBK, CELO, CORE, CRTS, CVX, ENJ, ENS, ENSO, GOMINING, GT, HBAR, HIVE, KAS, KCT, KSM, LAT, LINK, LUNC, M, MBX, MEGA, MEME, MOVR, NES, NPC, PENGU, PEOPLE, PYR, QNT, SAND, SC, SD, SEI, SHIB, SOMI, SSV, ULTIMA, VIRTUAL, WARD, WLD, XCH, XCN, XDC; bruto zonder voorraadgrens zou €761,90 zijn, met voorraad €0,23 (GEZIEN boek, GOK model).
- gate - htx, €5.000,00: munten AKT, ALGO, APEPE, APT, ATOM, BIO, BRISE, BSV, BTT, CBK, CELO, CORE, CRTS, CVX, ENJ, ENS, ENSO, GOMINING, GT, HBAR, HIVE, KAS, KCT, KSM, LAT, LINK, LUNC, M, MBX, MEGA, MEME, MOVR, NES, NPC, PENGU, PEOPLE, PYR, QNT, SAND, SC, SD, SEI, SHIB, SOMI, SSV, ULTIMA, VIRTUAL, WARD, WLD, XCH, XCN, XDC; bruto zonder voorraadgrens zou €761,18 zijn, met voorraad €23,82 (GEZIEN boek, GOK model).
- bitget - htx, €100,00: munten AB, ACN, AI, ALGO, ANIME, ATOM, BABY, BIO, BONK, BSV, BTT, CBK, CFX, CORE, DYDX, ENA, ENJ, ENS, ENSO, HBAR, HIVE, IOST, JASMY, KAITO, KAS, KSM, LAT, LINK, LIT, LUNA, LUNC, M, MAPO, MEME, MINA, MOVR, NES, NPC, O, PCI, PEOPLE, PUMP, QNT, RIVER, S, SAND, SHIB, SNEK, SOMI, SSV, TAO, TIA, TLOS, USTC, VIRTUAL, WARD, WLD, XDC, XTZ, ZEN; bruto zonder voorraadgrens zou €809,15 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - htx, €150,00: munten AB, ACN, AI, ALGO, ANIME, ATOM, BABY, BIO, BONK, BSV, BTT, CBK, CFX, CORE, DYDX, ENA, ENJ, ENS, ENSO, HBAR, HIVE, IOST, JASMY, KAITO, KAS, KSM, LAT, LINK, LIT, LUNA, LUNC, M, MAPO, MEME, MINA, MOVR, NES, NPC, O, PCI, PEOPLE, PUMP, QNT, RIVER, S, SAND, SHIB, SNEK, SOMI, SSV, TAO, TIA, TLOS, USTC, VIRTUAL, WARD, WLD, XDC, XTZ, ZEN; bruto zonder voorraadgrens zou €809,15 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - htx, €200,00: munten AB, ACN, AI, ALGO, ANIME, ATOM, BABY, BIO, BONK, BSV, BTT, CBK, CFX, CORE, DYDX, ENA, ENJ, ENS, ENSO, HBAR, HIVE, IOST, JASMY, KAITO, KAS, KSM, LAT, LINK, LIT, LUNA, LUNC, M, MAPO, MEME, MINA, MOVR, NES, NPC, O, PCI, PEOPLE, PUMP, QNT, RIVER, S, SAND, SHIB, SNEK, SOMI, SSV, TAO, TIA, TLOS, USTC, VIRTUAL, WARD, WLD, XDC, XTZ, ZEN; bruto zonder voorraadgrens zou €809,15 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - htx, €2.000,00: munten AB, ACN, AI, ALGO, ANIME, ATOM, BABY, BIO, BONK, BSV, BTT, CBK, CFX, CORE, DYDX, ENA, ENJ, ENS, ENSO, HBAR, HIVE, IOST, JASMY, KAITO, KAS, KSM, LAT, LINK, LIT, LUNA, LUNC, M, MAPO, MEME, MINA, MOVR, NES, NPC, O, PCI, PEOPLE, PUMP, QNT, RIVER, S, SAND, SHIB, SNEK, SOMI, SSV, TAO, TIA, TLOS, USTC, VIRTUAL, WARD, WLD, XDC, XTZ, ZEN; bruto zonder voorraadgrens zou €809,15 zijn, met voorraad €1,53 (GEZIEN boek, GOK model).
- bitget - htx, €5.000,00: munten AB, ACN, AI, ALGO, ANIME, ATOM, BABY, BIO, BONK, BSV, BTT, CBK, CFX, CORE, DYDX, ENA, ENJ, ENS, ENSO, HBAR, HIVE, IOST, JASMY, KAITO, KAS, KSM, LAT, LINK, LIT, LUNA, LUNC, M, MAPO, MEME, MINA, MOVR, NES, NPC, O, PCI, PEOPLE, PUMP, QNT, RIVER, S, SAND, SHIB, SNEK, SOMI, SSV, TAO, TIA, TLOS, USTC, VIRTUAL, WARD, WLD, XDC, XTZ, ZEN; bruto zonder voorraadgrens zou €808,46 zijn, met voorraad €20,40 (GEZIEN boek, GOK model).
- htx - xt, €100,00: munten ALGO, APEPE, APT, BIO, BSV, CARV, CBK, CELO, CFX, GT, HBAR, KSM, LUNC, MEME, MINA, PENGU, PEOPLE, RAIN, SC, SEI, SHIB, SOMI, TLOS, XCH, XDC, XMR; bruto zonder voorraadgrens zou €848,26 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - xt, €150,00: munten ALGO, APEPE, APT, BIO, BSV, CARV, CBK, CELO, CFX, GT, HBAR, KSM, LUNC, MEME, MINA, PENGU, PEOPLE, RAIN, SC, SEI, SHIB, SOMI, TLOS, XCH, XDC, XMR; bruto zonder voorraadgrens zou €848,26 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - xt, €200,00: munten ALGO, APEPE, APT, BIO, BSV, CARV, CBK, CELO, CFX, GT, HBAR, KSM, LUNC, MEME, MINA, PENGU, PEOPLE, RAIN, SC, SEI, SHIB, SOMI, TLOS, XCH, XDC, XMR; bruto zonder voorraadgrens zou €848,26 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - xt, €2.000,00: munten ALGO, APEPE, APT, BIO, BSV, CARV, CBK, CELO, CFX, GT, HBAR, KSM, LUNC, MEME, MINA, PENGU, PEOPLE, RAIN, SC, SEI, SHIB, SOMI, TLOS, XCH, XDC, XMR; bruto zonder voorraadgrens zou €848,04 zijn, met voorraad €9,57 (GEZIEN boek, GOK model).
- htx - xt, €5.000,00: munten ALGO, APEPE, APT, BIO, BSV, CARV, CBK, CELO, CFX, GT, HBAR, KSM, LUNC, MEME, MINA, PENGU, PEOPLE, RAIN, SC, SEI, SHIB, SOMI, TLOS, XCH, XDC, XMR; bruto zonder voorraadgrens zou €846,73 zijn, met voorraad €34,87 (GEZIEN boek, GOK model).
- bitget - kucoin, €100,00: munten ACE, BARD, BTC, CARV, CHR, DMC, EDEN, EGL1, ENJ, ENSO, ETH, HYPER, IR, JST, KAVA, KLV, KNC, LAT, LUNC, MASK, MHA, MTX, NES, NOM, PROVE, TAC, USDC, USDT, USTC, VERONA; bruto zonder voorraadgrens zou €511,41 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - kucoin, €150,00: munten ACE, BARD, BTC, CARV, CHR, DMC, EDEN, EGL1, ENJ, ENSO, ETH, HYPER, IR, JST, KAVA, KLV, KNC, LAT, LUNC, MASK, MHA, MTX, NES, NOM, PROVE, TAC, USDC, USDT, USTC, VERONA; bruto zonder voorraadgrens zou €511,41 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - kucoin, €200,00: munten ACE, BARD, BTC, CARV, CHR, DMC, EDEN, EGL1, ENJ, ENSO, ETH, HYPER, IR, JST, KAVA, KLV, KNC, LAT, LUNC, MASK, MHA, MTX, NES, NOM, PROVE, TAC, USDC, USDT, USTC, VERONA; bruto zonder voorraadgrens zou €511,41 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - kucoin, €2.000,00: munten ACE, BARD, BTC, CARV, CHR, DMC, EDEN, EGL1, ENJ, ENSO, ETH, HYPER, IR, JST, KAVA, KLV, KNC, LAT, LUNC, MASK, MHA, MTX, NES, NOM, PROVE, TAC, USDC, USDT, USTC, VERONA; bruto zonder voorraadgrens zou €511,05 zijn, met voorraad €3,83 (GEZIEN boek, GOK model).
- bitget - kucoin, €5.000,00: munten ACE, BARD, BTC, CARV, CHR, DMC, EDEN, EGL1, ENJ, ENSO, ETH, HYPER, IR, JST, KAVA, KLV, KNC, LAT, LUNC, MASK, MHA, MTX, NES, NOM, PROVE, TAC, USDC, USDT, USTC, VERONA; bruto zonder voorraadgrens zou €509,23 zijn, met voorraad €20,69 (GEZIEN boek, GOK model).

### Andere keuzes bij bitvavo - kraken (netto handel, alle dagen samen; GOK)

| Keuze | Inleg | Kansen | Gemist | Bruto winst | Kosten terugschuiven | Netto handel |
|---|---|---|---|---|---|---|
| standaard (schuifdrempel 25%, kostengrens 1%) | €150,00 | 152 | 152 | €0,00 | €0,00 | **€0,00** |
| standaard (schuifdrempel 25%, kostengrens 1%) | €2.000,00 | 152 | 91 | €55,60 | €22,19 | **€33,41** |
| schuifdrempel 10% | €150,00 | 152 | 152 | €0,00 | €0,00 | **€0,00** |
| schuifdrempel 10% | €2.000,00 | 152 | 91 | €55,60 | €21,19 | **€34,41** |
| schuifdrempel 40% | €150,00 | 152 | 152 | €0,00 | €0,00 | **€0,00** |
| schuifdrempel 40% | €2.000,00 | 152 | 91 | €55,28 | €23,19 | **€32,09** |
| kostengrens 2% (achteraf vergeleken) | €150,00 | 152 | 152 | €0,00 | €0,00 | **€0,00** |
| kostengrens 2% (achteraf vergeleken) | €2.000,00 | 152 | 86 | €55,85 | €25,39 | **€30,46** |
| kostengrens 5% (achteraf vergeleken) | €150,00 | 152 | 152 | €0,00 | €0,00 | **€0,00** |
| kostengrens 5% (achteraf vergeleken) | €2.000,00 | 152 | 42 | €59,91 | €76,59 | **€-16,69** |
| alleen MERL en GMT (meer voorraad per munt, achteraf gekozen) | €150,00 | 123 | 121 | €0,19 | €0,00 | **€0,19** |
| alleen MERL en GMT (meer voorraad per munt, achteraf gekozen) | €2.000,00 | 123 | 41 | €261,06 | €75,13 | **€185,93** |

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
- Geld terugschuiven per beurs: bitget EUR: 1 EUR, GOK (1 EUR, 24 uur; niet nagekeken); bitget USDT: 1 USDT, GOK (1 USDT, 30 min; niet nagekeken); bitstamp EUR: 1 EUR, GOK (1 EUR, 24 uur; niet nagekeken); bitstamp USD: 1 USD, GOK (1 USD, 24 uur; niet nagekeken); bitvavo EUR: 0 EUR, kosten GEZIEN (api.bitvavo.com/v2/assets: EUR withdrawalFee 0), tijd GOK (1 werkdag, SEPA), minimum 0 EUR (GEZIEN, api.bitvavo.com/v2/assets withdrawalMinAmount); gate USDT: 1 USDT, GOK (1 USDT, 30 min; niet nagekeken), minimum 1 USDT (GEZIEN, api.gateio.ws/api/v4/wallet/currency_chains withdraw_amount_min); htx USDT: 1 USDT, GOK (1 USDT, 30 min; niet nagekeken); kraken EUR: 1 EUR, kosten GEZIEN (support.kraken.com/articles/360000381846: Instant SEPA, Banking Circle, 1 EUR, near-instant), tijd GOK (1 uur tot het op de andere beurs staat), minimum 2 EUR (GEZIEN, support.kraken.com/articles/360000381846 Instant SEPA (Banking Circle)); kraken USD: 1 USD, GOK (1 USD, 24 uur; niet nagekeken); kucoin EUR: 1 EUR, GOK (1 EUR, 24 uur; niet nagekeken); kucoin USDT: 1 USDT, kosten GEZIEN (api.kucoin.com/api/v3/currencies/USDT: BEP20 1 USDT), tijd GOK, minimum 5 USDT (GEZIEN, api.kucoin.com/api/v3/currencies/USDT BEP20 withdrawalMinSize); xt USDT: 1 USDT, GOK (1 USDT, 30 min; niet nagekeken).

## Over de meting

- Opnamekosten bij de echte kansen: 468 van een netwerk dat aan beide kanten open is, 316 van de beurs zelf (laagste open netwerk), 172 geschat uit wat andere beurzen voor die munt vragen (GOK). Onbekende opnamekosten tellen niet als echte kans.
- Netwerk: KuCoin, Gate, Bitget, HTX, XT, Bitstamp, Bitvavo en Poloniex geven hun netwerken per munt. Als beide beurzen dat doen en de namen te koppelen zijn, moet er een netwerk zijn dat aan beide kanten open is. Anders is het netwerk "niet te koppelen" en telt de kans mee (staat apart in de trechter).
- De duur is gemeten in stappen van ±20 seconden; een kans kan een paar rondes eerder begonnen zijn dan we zagen.
- Takerkosten: uit de API waar die ze per paar geeft, anders het standaardtarief uit de README (deels GOK).
- Laatste run: 15 beurzen antwoordden, 2275 munt-quote-paren op minstens twee beurzen (GEZIEN).
