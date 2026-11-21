# Rapport koersverschil-scanner

Gemaakt 2026-11-21 16:05 UTC uit 24 runs, samen ±52.8 uur gemeten (GEZIEN).
Echte kans = winst na alle kosten (opnamekosten bekend), opnemen en storten open (en een netwerk dat aan beide kanten open is, als de beurzen dat geven), minstens €100,00 op het boek, minstens 2 minuten blijven staan, geen andere munt met dezelfde naam.
**Vergund** = beide beurzen hebben een MiCA-vergunning (ESMA-register), vaak via een EU-dochter die minder munten kan hebben dan de wereldwijde API die we meten (GOK). **Grijs** = minstens één beurs zonder vergunning (MEXC, Bitget, HTX, Poloniex, XT, Bitfinex, Binance). Zie README.md.
**Kraken-tarief:** Kraken rekent 0,80% taker op munt tegen EUR, USD, USDT of USDC (GEZIEN, kraken.com/pro/fees, laagste trede); de scanner rekende tot 19 nov met 0,40%. 399 opgeslagen kansen met Kraken uit die runs zijn hier **opnieuw doorgerekend met 0,80%** (GOK-benadering: 0,40% van de inzet aan de Kraken-kant extra op elk gemeten punt van het boek; het boek zelf is niet bewaard). 233 houden daarna nog winst op het boek. Dat ze met hogere kosten ook korter bleven staan, telt niet mee (dus eerder te gunstig).

## Hoeveel wordt er gecontroleerd? (GEZIEN, stand.jsonl)

Per ronde (mediaan over 634 metingen): 1149 kandidaten (verschil op de ticker groter dan de takerkosten), 120 met het orderboek gecontroleerd, 2 nog nooit gecontroleerd (0%).
Bijna alle kandidaten komen aan de beurt; de aantallen hieronder missen weinig.

## Trechter (GEZIEN, eigen metingen)

| Stap | Alle beurzen | Alleen MiCA-beurzen | Met minstens één grijze beurs |
|---|---|---|---|
| Verschillen met winst op het boek na alle kosten | 51429 | 6946 | 44483 |
| ...waarvan opnemen of storten dicht | 8856 | 971 | 7885 |
| ...waarvan status onbekend (beurs geeft het niet openbaar) | 31901 | 4969 | 26932 |
| Opnemen en storten open | 10672 | 1006 | 9666 |
| ...en geen netwerk dat aan beide kanten open is: valt af | 216 | 19 | 197 |
| ...en opnamekosten onbekend: valt af | 5 | 5 | 0 |
| ...en minstens €100,00 op het boek | 3167 | 639 | 2528 |
| ...en minstens 2 minuten blijven staan | 882 | 245 | 637 |
| ...en geen andere munt met dezelfde naam | 833 | 222 | 611 |
|    ...waarvan contractadres bekend en gelijk | 115 | 44 | 71 |
|    ...waarvan contractadres onbekend (telt mee, kan een andere munt zijn) | 718 | 178 | 540 |
|    ...waarvan netwerk gekoppeld en open | 555 | 116 | 439 |
|    ...waarvan netwerk niet te koppelen (telt mee) | 278 | 106 | 172 |
| **Echte kansen** (zelfde munt overlappend in de tijd samengevoegd, beste beurspaar telt) | 494 | 212 | 364 |
| Ter vergelijking: zelfde eisen, maar opnamestatus onbekend (niet meegeteld) | 2024 | 435 | 1736 |

## Echte kansen per dag (GEZIEN)

| Dag | Echt, alleen MiCA | Echt, met grijs | Mediane winst per kans bij €500 (MiCA / grijs) | Mediane duur |
|---|---|---|---|---|
| 2026-11-19 | 49 | 86 | €2,00 / €1,21 | 5.3 min |
| 2026-11-20 | 53 | 138 | €1,01 / €1,13 | 6.7 min |
| 2026-11-21 | 44 | 124 | €1,64 / €0,95 | 5.6 min |
| Totaal | 146 | 348 | €1,55 / €1,09 | 6.0 min |

## Beste munten (GEZIEN)

| | Soort | Kansen | Som winst bij €500 per kans |
|---|---|---|---|
| MERL-EUR | vergund | 30 | €830,34 |
| LUNC-USDT | grijs | 16 | €94,30 |
| USTC-USDT | grijs en vergund | 18 | €67,44 |
| KERNEL-EUR | vergund | 1 | €47,33 |
| MEME-USDT | grijs | 1 | €37,90 |
| ENSO-USDT | grijs en vergund | 10 | €37,15 |
| BSV-USDT | grijs | 23 | €34,83 |
| KYO-USDT | vergund | 5 | €30,94 |
| BARD-USDT | grijs | 4 | €24,39 |
| SHIB-USDT | grijs | 8 | €22,78 |

## Beste beursparen (kopen op > verkopen op) (GEZIEN)

| | Soort | Kansen | Som winst bij €500 per kans |
|---|---|---|---|
| bitvavo > kraken | vergund | 70 | €930,60 |
| bitget > htx | grijs | 76 | €148,79 |
| gate > kucoin | vergund | 36 | €95,95 |
| kucoin > htx | grijs | 38 | €88,52 |
| kucoin > bitget | grijs | 29 | €75,32 |
| bitget > xt | grijs | 17 | €58,36 |
| bitget > gate | grijs | 17 | €42,95 |
| bitget > kucoin | grijs | 26 | €41,09 |
| gate > htx | grijs | 22 | €40,65 |
| htx > gate | grijs | 6 | €38,21 |

Beurzen die het vaakst meedoen (koop of verkoop): bitget (grijs) 214, kucoin 200, htx (grijs) 180, gate 121, kraken 105, bitvavo 77, xt (grijs) 49, poloniex (grijs) 39 (GEZIEN).

## Hoeveel kansen blijven staan terwijl je geld schuift? (GEZIEN, duur uit eigen metingen)

Wie geen voorraad op beide beurzen heeft, moet kopen, de munt opnemen, wachten tot hij binnen is en dan verkopen. Hoe lang dat duurt verschilt per munt en netwerk: een paar minuten (snelle ketens) tot een uur of meer (Bitcoin, beurzen die opnames met de hand keuren) (GOK, niet per munt gemeten).

| Overmaaktijd | Alle beurzen | Alleen MiCA-beurzen | Met minstens één grijze beurs |
|---|---|---|---|
| 5 min | 284 van 494 (57%) | 118 van 212 (56%) | 219 van 364 (60%) |
| 10 min | 176 van 494 (36%) | 79 van 212 (37%) | 137 van 364 (38%) |
| 30 min | 90 van 494 (18%) | 45 van 212 (21%) | 71 van 364 (20%) |
| 60 min | 54 van 494 (11%) | 34 van 212 (16%) | 42 van 364 (12%) |

## Wat zou het opleveren over 3 maanden? (GOK, doorgetrokken uit de metingen)

Gemeten over ±52.8 uur (GEZIEN), doorgetrokken naar 90 dagen (GOK: aanname dat de week die we maten gewoon is).

| Beurzen | Inleg | Model | Kansen per uur | Per kans (mediaan) | 3 maanden |
|---|---|---|---|---|---|
| Alleen MiCA | €2.000,00 | bovengrens: elke kans, geld overal tegelijk | 4.01 | €1,55 | €13.468,06 |
| Alleen MiCA | €2.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 1.32 | €4,08 | €68.750,05 |
| Alleen MiCA | €5.000,00 | bovengrens: elke kans, geld overal tegelijk | 4.01 | €1,94 | €16.839,95 |
| Alleen MiCA | €5.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 1.32 | €5,49 | €132.306,51 |
| Alle (met grijs) | €2.000,00 | bovengrens: elke kans, geld overal tegelijk | 9.35 | €1,51 | €30.488,44 |
| Alle (met grijs) | €2.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 1.32 | €4,08 | €68.750,05 |
| Alle (met grijs) | €5.000,00 | bovengrens: elke kans, geld overal tegelijk | 9.35 | €1,75 | €35.442,45 |
| Alle (met grijs) | €5.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 1.32 | €5,49 | €132.306,51 |

Bovengrens: elke kans met de helft van de inleg aan elke kant, alsof het geld op alle beurzen tegelijk staat (kan in het echt niet). Beste beurspaar: het paar is **achteraf** gekozen uit de metingen (vooraf kiezen levert minder op), en het model neemt aan dat je van elke munt al voorraad op de verkoopbeurs hebt.

Waarom dit te rooskleurig is (GOK): elke kans wordt maar één keer geteld met het mediane boek, maar andere bots pakken hem ook; de munt die je als voorraad aanhoudt kan dalen; na een paar kansen moet de voorraad terug (opnamekosten en tijd); minimale opname- en ordergroottes tellen niet mee; en een kans die we 2 minuten zagen staan, staat er niet per se nog als jouw order binnenkomt. Waarom het te somber kan zijn: niet alle kandidaten zijn gecontroleerd, en met voorraad op beide beurzen kun je dezelfde kans vaker pakken als het boek zich aanvult; dat telt hier niet mee.

## Wat houd je echt over? Voorraad op twee beurzen (simulatie)

Per beurspaar: geld en munten op beide beurzen, elke echte kans uitgevoerd tegen het boek zoals gemeten (niet meer dan de ruimte op het boek en niet meer dan de voorraad op die beurs), terugschuiven als een kant leeg dreigt te raken (met opnamekosten en tijd onderweg), en het koerseffect van de aangehouden munten apart. Netto = bruto min kosten terugschuiven plus koerseffect. **Gemeten** (GEZIEN): de kansen, het boek en de koersen; **de rest is een rekenmodel** (GOK, aannames onder de tabel). Geen advies.

**Met €150: netto €0,52 per dag op bitstamp - kraken (koerseffect erbovenop €-1,63), €0,01 per dag op bitstamp - kucoin (koerseffect erbovenop €0,03), €0,00 per dag op bitvavo - kraken (koerseffect erbovenop €-2,15), €0,02 per dag op bitvavo - kucoin (koerseffect erbovenop €-0,77), €0,04 per dag op gate - kucoin (koerseffect erbovenop €-1,64), €0,01 per dag op kraken - kucoin (koerseffect erbovenop €0,03) (GOK: netto handel, rekenmodel op ±17.6 uur meting per dag, alleen MiCA).** "Per dag" is hier gemiddeld over 3 gemeten dagen achter elkaar; de eerste begint met een gelijk verdeelde voorraad; aan het eind staat de voorraad scheef, dus een volgende dag levert waarschijnlijk minder op, tenzij kansen de andere kant op hem terugbrengen (GOK).

### Alleen MiCA-beurzen (alle paren met echte kansen)

| Beurspaar | Inleg | Dag | Gemeten | Kansen | Gemist (geen voorraad) | Kleiner door voorraad | Bruto winst | Kosten terugschuiven | **Netto handel (bruto min kosten)** | Rendement handel | Koerseffect voorraad | Netto met koerseffect | Rendement met koerseffect |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| bitstamp - kraken | €100,00 | 2026-11-19 | 14.9 u | 2 | 1 | 1 | €0,59 | €0,00 (0x) | **€0,59** | 0.59% | €-0,02 | €0,57 | 0.57% |
| bitstamp - kraken | €100,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,95 | €-2,95 | -2.95% |
| bitstamp - kraken | €100,00 | 2026-11-21 | 15.1 u | 1 | 0 | 1 | €0,45 | €0,00 (0x) | **€0,45** | 0.45% | €-0,28 | €0,17 | 0.17% |
| bitstamp - kraken | €150,00 | 2026-11-19 | 14.9 u | 2 | 1 | 1 | €0,89 | €0,00 (0x) | **€0,89** | 0.59% | €-0,03 | €0,85 | 0.57% |
| bitstamp - kraken | €150,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-4,43 | €-4,43 | -2.95% |
| bitstamp - kraken | €150,00 | 2026-11-21 | 15.1 u | 1 | 0 | 1 | €0,67 | €0,00 (0x) | **€0,67** | 0.45% | €-0,41 | €0,26 | 0.17% |
| bitstamp - kraken | €200,00 | 2026-11-19 | 14.9 u | 2 | 1 | 1 | €1,18 | €0,00 (0x) | **€1,18** | 0.59% | €-0,04 | €1,14 | 0.57% |
| bitstamp - kraken | €200,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-5,91 | €-5,91 | -2.95% |
| bitstamp - kraken | €200,00 | 2026-11-21 | 15.1 u | 1 | 0 | 1 | €0,89 | €0,00 (0x) | **€0,89** | 0.45% | €-0,55 | €0,34 | 0.17% |
| bitstamp - kraken | €2.000,00 | 2026-11-19 | 14.9 u | 2 | 1 | 0 | €11,71 | €0,98 (1x) | **€10,73** | 0.54% | €-0,46 | €10,27 | 0.51% |
| bitstamp - kraken | €2.000,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-59,03 | €-59,03 | -2.95% |
| bitstamp - kraken | €2.000,00 | 2026-11-21 | 15.1 u | 1 | 0 | 0 | €5,30 | €0,00 (0x) | **€5,30** | 0.26% | €-5,54 | €-0,24 | -0.01% |
| bitstamp - kraken | €5.000,00 | 2026-11-19 | 14.9 u | 2 | 1 | 0 | €11,71 | €0,00 (0x) | **€11,71** | 0.23% | €-1,10 | €10,60 | 0.21% |
| bitstamp - kraken | €5.000,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-147,75 | €-147,75 | -2.95% |
| bitstamp - kraken | €5.000,00 | 2026-11-21 | 15.1 u | 1 | 0 | 0 | €5,30 | €0,00 (0x) | **€5,30** | 0.11% | €-13,83 | €-8,53 | -0.17% |
| bitstamp - kucoin | €100,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,11 | €0,11 | 0.11% |
| bitstamp - kucoin | €100,00 | 2026-11-20 | 22.8 u | 1 | 0 | 1 | €0,00 | €0,01 (1x) | **€-0,01** | -0.01% | €0,11 | €0,10 | 0.10% |
| bitstamp - kucoin | €100,00 | 2026-11-21 | 15.1 u | 6 | 5 | 1 | €0,01 | €0,00 (0x) | **€0,01** | 0.01% | €-0,16 | €-0,14 | -0.14% |
| bitstamp - kucoin | €150,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,16 | €0,16 | 0.11% |
| bitstamp - kucoin | €150,00 | 2026-11-20 | 22.8 u | 1 | 0 | 1 | €0,00 | €0,01 (1x) | **€-0,01** | -0.00% | €0,16 | €0,16 | 0.11% |
| bitstamp - kucoin | €150,00 | 2026-11-21 | 15.1 u | 6 | 5 | 1 | €0,02 | €0,00 (0x) | **€0,02** | 0.01% | €-0,23 | €-0,21 | -0.14% |
| bitstamp - kucoin | €200,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,22 | €0,22 | 0.11% |
| bitstamp - kucoin | €200,00 | 2026-11-20 | 22.8 u | 1 | 0 | 1 | €0,01 | €0,01 (1x) | **€-0,00** | -0.00% | €0,22 | €0,22 | 0.11% |
| bitstamp - kucoin | €200,00 | 2026-11-21 | 15.1 u | 6 | 5 | 1 | €0,03 | €0,23 (1x) | **€-0,21** | -0.10% | €-0,31 | €-0,52 | -0.26% |
| bitstamp - kucoin | €2.000,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €2,19 | €2,19 | 0.11% |
| bitstamp - kucoin | €2.000,00 | 2026-11-20 | 22.8 u | 1 | 0 | 1 | €0,05 | €0,01 (1x) | **€0,04** | 0.00% | €2,19 | €2,24 | 0.11% |
| bitstamp - kucoin | €2.000,00 | 2026-11-21 | 15.1 u | 6 | 5 | 1 | €0,27 | €1,23 (2x) | **€-0,97** | -0.05% | €-3,13 | €-4,09 | -0.20% |
| bitstamp - kucoin | €5.000,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €5,49 | €5,49 | 0.11% |
| bitstamp - kucoin | €5.000,00 | 2026-11-20 | 22.8 u | 1 | 0 | 1 | €0,13 | €0,01 (1x) | **€0,12** | 0.00% | €5,48 | €5,60 | 0.11% |
| bitstamp - kucoin | €5.000,00 | 2026-11-21 | 15.1 u | 6 | 5 | 1 | €0,64 | €1,23 (2x) | **€-0,59** | -0.01% | €-7,82 | €-8,41 | -0.17% |
| bitvavo - kraken | €100,00 | 2026-11-19 | 14.9 u | 43 | 43 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,83 | €-0,83 | -0.83% |
| bitvavo - kraken | €100,00 | 2026-11-20 | 22.8 u | 15 | 15 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,35 | €-2,35 | -2.35% |
| bitvavo - kraken | €100,00 | 2026-11-21 | 15.1 u | 12 | 12 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,13 | €-1,13 | -1.13% |
| bitvavo - kraken | €150,00 | 2026-11-19 | 14.9 u | 43 | 43 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,25 | €-1,25 | -0.83% |
| bitvavo - kraken | €150,00 | 2026-11-20 | 22.8 u | 15 | 15 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,52 | €-3,52 | -2.35% |
| bitvavo - kraken | €150,00 | 2026-11-21 | 15.1 u | 12 | 12 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,69 | €-1,69 | -1.13% |
| bitvavo - kraken | €200,00 | 2026-11-19 | 14.9 u | 43 | 38 | 5 | €0,12 | €0,00 (0x) | **€0,12** | 0.06% | €-1,67 | €-1,55 | -0.77% |
| bitvavo - kraken | €200,00 | 2026-11-20 | 22.8 u | 15 | 14 | 1 | €0,90 | €0,00 (0x) | **€0,90** | 0.45% | €-4,70 | €-3,80 | -1.90% |
| bitvavo - kraken | €200,00 | 2026-11-21 | 15.1 u | 12 | 12 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,25 | €-2,25 | -1.13% |
| bitvavo - kraken | €2.000,00 | 2026-11-19 | 14.9 u | 43 | 25 | 18 | €12,03 | €7,02 (18x) | **€5,02** | 0.25% | €-16,59 | €-11,57 | -0.58% |
| bitvavo - kraken | €2.000,00 | 2026-11-20 | 22.8 u | 15 | 9 | 6 | €23,49 | €2,29 (5x) | **€21,19** | 1.06% | €-46,68 | €-25,49 | -1.27% |
| bitvavo - kraken | €2.000,00 | 2026-11-21 | 15.1 u | 12 | 5 | 7 | €22,55 | €3,35 (8x) | **€19,20** | 0.96% | €-22,53 | €-3,33 | -0.17% |
| bitvavo - kraken | €5.000,00 | 2026-11-19 | 14.9 u | 43 | 20 | 23 | €26,34 | €16,24 (26x) | **€10,10** | 0.20% | €-41,54 | €-31,43 | -0.63% |
| bitvavo - kraken | €5.000,00 | 2026-11-20 | 22.8 u | 15 | 2 | 13 | €61,31 | €12,31 (15x) | **€49,00** | 0.98% | €-116,07 | €-67,08 | -1.34% |
| bitvavo - kraken | €5.000,00 | 2026-11-21 | 15.1 u | 12 | 5 | 7 | €58,01 | €2,35 (7x) | **€55,65** | 1.11% | €-56,21 | €-0,56 | -0.01% |
| bitvavo - kucoin | €100,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,52 | €-0,52 | -0.52% |
| bitvavo - kucoin | €100,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,80 | €-1,80 | -1.80% |
| bitvavo - kucoin | €100,00 | 2026-11-21 | 15.1 u | 7 | 5 | 2 | €0,04 | €0,00 (0x) | **€0,04** | 0.04% | €0,79 | €0,83 | 0.83% |
| bitvavo - kucoin | €150,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,78 | €-0,78 | -0.52% |
| bitvavo - kucoin | €150,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,71 | €-2,71 | -1.80% |
| bitvavo - kucoin | €150,00 | 2026-11-21 | 15.1 u | 7 | 5 | 2 | €0,07 | €0,00 (0x) | **€0,07** | 0.04% | €1,18 | €1,25 | 0.83% |
| bitvavo - kucoin | €200,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,04 | €-1,04 | -0.52% |
| bitvavo - kucoin | €200,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,61 | €-3,61 | -1.80% |
| bitvavo - kucoin | €200,00 | 2026-11-21 | 15.1 u | 7 | 5 | 2 | €0,09 | €0,00 (0x) | **€0,09** | 0.04% | €1,58 | €1,66 | 0.83% |
| bitvavo - kucoin | €2.000,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-10,39 | €-10,39 | -0.52% |
| bitvavo - kucoin | €2.000,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-36,07 | €-36,07 | -1.80% |
| bitvavo - kucoin | €2.000,00 | 2026-11-21 | 15.1 u | 7 | 4 | 3 | €0,91 | €2,73 (3x) | **€-1,82** | -0.09% | €15,73 | €13,91 | 0.70% |
| bitvavo - kucoin | €5.000,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-25,99 | €-25,99 | -0.52% |
| bitvavo - kucoin | €5.000,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-90,18 | €-90,18 | -1.80% |
| bitvavo - kucoin | €5.000,00 | 2026-11-21 | 15.1 u | 7 | 4 | 3 | €2,24 | €2,73 (3x) | **€-0,49** | -0.01% | €39,40 | €38,91 | 0.78% |
| gate - kucoin | €100,00 | 2026-11-19 | 14.9 u | 25 | 25 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,82 | €-0,82 | -0.82% |
| gate - kucoin | €100,00 | 2026-11-20 | 22.8 u | 46 | 46 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,62 | €-0,62 | -0.62% |
| gate - kucoin | €100,00 | 2026-11-21 | 15.1 u | 37 | 37 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,84 | €-1,84 | -1.84% |
| gate - kucoin | €150,00 | 2026-11-19 | 14.9 u | 25 | 25 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,23 | €-1,23 | -0.82% |
| gate - kucoin | €150,00 | 2026-11-20 | 22.8 u | 46 | 45 | 1 | €0,12 | €0,00 (0x) | **€0,12** | 0.08% | €-0,93 | €-0,81 | -0.54% |
| gate - kucoin | €150,00 | 2026-11-21 | 15.1 u | 37 | 37 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,77 | €-2,77 | -1.84% |
| gate - kucoin | €200,00 | 2026-11-19 | 14.9 u | 25 | 25 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,64 | €-1,64 | -0.82% |
| gate - kucoin | €200,00 | 2026-11-20 | 22.8 u | 46 | 44 | 2 | €0,24 | €0,00 (1x) | **€0,24** | 0.12% | €-1,24 | €-1,01 | -0.50% |
| gate - kucoin | €200,00 | 2026-11-21 | 15.1 u | 37 | 37 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,69 | €-3,69 | -1.84% |
| gate - kucoin | €2.000,00 | 2026-11-19 | 14.9 u | 25 | 13 | 12 | €1,36 | €0,77 (5x) | **€0,59** | 0.03% | €-16,37 | €-15,78 | -0.79% |
| gate - kucoin | €2.000,00 | 2026-11-20 | 22.8 u | 46 | 25 | 21 | €7,27 | €0,59 (7x) | **€6,68** | 0.33% | €-12,43 | €-5,74 | -0.29% |
| gate - kucoin | €2.000,00 | 2026-11-21 | 15.1 u | 37 | 24 | 13 | €4,25 | €0,28 (3x) | **€3,97** | 0.20% | €-36,88 | €-32,91 | -1.65% |
| gate - kucoin | €5.000,00 | 2026-11-19 | 14.9 u | 25 | 6 | 19 | €5,95 | €3,82 (17x) | **€2,13** | 0.04% | €-40,98 | €-38,85 | -0.78% |
| gate - kucoin | €5.000,00 | 2026-11-20 | 22.8 u | 46 | 10 | 36 | €22,96 | €4,61 (25x) | **€18,35** | 0.37% | €-31,02 | €-12,67 | -0.25% |
| gate - kucoin | €5.000,00 | 2026-11-21 | 15.1 u | 37 | 9 | 28 | €13,56 | €3,71 (20x) | **€9,85** | 0.20% | €-92,01 | €-82,16 | -1.64% |
| kraken - kucoin | €100,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,11 | €0,11 | 0.11% |
| kraken - kucoin | €100,00 | 2026-11-20 | 22.8 u | 15 | 13 | 2 | €0,03 | €0,01 (1x) | **€0,02** | 0.02% | €0,11 | €0,13 | 0.13% |
| kraken - kucoin | €100,00 | 2026-11-21 | 15.1 u | 12 | 12 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,16 | €-0,16 | -0.16% |
| kraken - kucoin | €150,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,16 | €0,16 | 0.11% |
| kraken - kucoin | €150,00 | 2026-11-20 | 22.8 u | 15 | 13 | 2 | €0,05 | €0,01 (1x) | **€0,04** | 0.02% | €0,16 | €0,20 | 0.13% |
| kraken - kucoin | €150,00 | 2026-11-21 | 15.1 u | 12 | 12 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,23 | €-0,23 | -0.16% |
| kraken - kucoin | €200,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,22 | €0,22 | 0.11% |
| kraken - kucoin | €200,00 | 2026-11-20 | 22.8 u | 15 | 13 | 2 | €0,06 | €0,24 (2x) | **€-0,18** | -0.09% | €0,22 | €0,04 | 0.02% |
| kraken - kucoin | €200,00 | 2026-11-21 | 15.1 u | 12 | 12 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,31 | €-0,31 | -0.16% |
| kraken - kucoin | €2.000,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €2,19 | €2,19 | 0.11% |
| kraken - kucoin | €2.000,00 | 2026-11-20 | 22.8 u | 15 | 13 | 2 | €0,61 | €1,24 (3x) | **€-0,63** | -0.03% | €2,19 | €1,56 | 0.08% |
| kraken - kucoin | €2.000,00 | 2026-11-21 | 15.1 u | 12 | 12 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,13 | €-3,13 | -0.16% |
| kraken - kucoin | €5.000,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €5,49 | €5,49 | 0.11% |
| kraken - kucoin | €5.000,00 | 2026-11-20 | 22.8 u | 15 | 13 | 2 | €1,53 | €1,24 (3x) | **€0,28** | 0.01% | €5,48 | €5,77 | 0.12% |
| kraken - kucoin | €5.000,00 | 2026-11-21 | 15.1 u | 12 | 12 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-7,82 | €-7,82 | -0.16% |

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
- bitvavo - kraken, €100,00: munten AVA, CVX, DYM, GMT, KERNEL, LUNA, MERL, PROMPT, VELO; bruto zonder voorraadgrens zou €4.852,94 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitvavo - kraken, €150,00: munten AVA, CVX, DYM, GMT, KERNEL, LUNA, MERL, PROMPT, VELO; bruto zonder voorraadgrens zou €4.852,94 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitvavo - kraken, €200,00: munten AVA, CVX, DYM, GMT, KERNEL, LUNA, MERL, PROMPT, VELO; bruto zonder voorraadgrens zou €4.852,58 zijn, met voorraad €1,02 (GEZIEN boek, GOK model).
- bitvavo - kraken, €2.000,00: munten AVA, CVX, DYM, GMT, KERNEL, LUNA, MERL, PROMPT, VELO; bruto zonder voorraadgrens zou €4.798,27 zijn, met voorraad €58,08 (GEZIEN boek, GOK model).
- bitvavo - kraken, €5.000,00: munten AVA, CVX, DYM, GMT, KERNEL, LUNA, MERL, PROMPT, VELO; bruto zonder voorraadgrens zou €4.721,81 zijn, met voorraad €145,66 (GEZIEN boek, GOK model).
- bitvavo - kucoin, €100,00: munten ETH, USDC; bruto zonder voorraadgrens zou €19,28 zijn, met voorraad €0,04 (GEZIEN boek, GOK model).
- bitvavo - kucoin, €150,00: munten ETH, USDC; bruto zonder voorraadgrens zou €19,28 zijn, met voorraad €0,07 (GEZIEN boek, GOK model).
- bitvavo - kucoin, €200,00: munten ETH, USDC; bruto zonder voorraadgrens zou €19,28 zijn, met voorraad €0,09 (GEZIEN boek, GOK model).
- bitvavo - kucoin, €2.000,00: munten ETH, USDC; bruto zonder voorraadgrens zou €19,28 zijn, met voorraad €0,91 (GEZIEN boek, GOK model).
- bitvavo - kucoin, €5.000,00: munten ETH, USDC; bruto zonder voorraadgrens zou €19,28 zijn, met voorraad €2,24 (GEZIEN boek, GOK model).
- gate - kucoin, €100,00: munten ALKIMI, AVAIL, BARD, CCD, CHR, CWEB, CYBER, EDEN, ENSO, ERG, FTT, HIGH, HTR, IKA, IR, JST, KYO, LUNC, NAKA, NIM, OVR, POKT, RARI, SD, SOUL, STREAM, SUPRA, USDS, USTC, VERONA, XU3O8; bruto zonder voorraadgrens zou €384,35 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- gate - kucoin, €150,00: munten ALKIMI, AVAIL, BARD, CCD, CHR, CWEB, CYBER, EDEN, ENSO, ERG, FTT, HIGH, HTR, IKA, IR, JST, KYO, LUNC, NAKA, NIM, OVR, POKT, RARI, SD, SOUL, STREAM, SUPRA, USDS, USTC, VERONA, XU3O8; bruto zonder voorraadgrens zou €384,35 zijn, met voorraad €0,12 (GEZIEN boek, GOK model).
- gate - kucoin, €200,00: munten ALKIMI, AVAIL, BARD, CCD, CHR, CWEB, CYBER, EDEN, ENSO, ERG, FTT, HIGH, HTR, IKA, IR, JST, KYO, LUNC, NAKA, NIM, OVR, POKT, RARI, SD, SOUL, STREAM, SUPRA, USDS, USTC, VERONA, XU3O8; bruto zonder voorraadgrens zou €384,35 zijn, met voorraad €0,24 (GEZIEN boek, GOK model).
- gate - kucoin, €2.000,00: munten ALKIMI, AVAIL, BARD, CCD, CHR, CWEB, CYBER, EDEN, ENSO, ERG, FTT, HIGH, HTR, IKA, IR, JST, KYO, LUNC, NAKA, NIM, OVR, POKT, RARI, SD, SOUL, STREAM, SUPRA, USDS, USTC, VERONA, XU3O8; bruto zonder voorraadgrens zou €382,99 zijn, met voorraad €12,88 (GEZIEN boek, GOK model).
- gate - kucoin, €5.000,00: munten ALKIMI, AVAIL, BARD, CCD, CHR, CWEB, CYBER, EDEN, ENSO, ERG, FTT, HIGH, HTR, IKA, IR, JST, KYO, LUNC, NAKA, NIM, OVR, POKT, RARI, SD, SOUL, STREAM, SUPRA, USDS, USTC, VERONA, XU3O8; bruto zonder voorraadgrens zou €379,44 zijn, met voorraad €42,47 (GEZIEN boek, GOK model).
- kraken - kucoin, €100,00: munten USDC, USDT; bruto zonder voorraadgrens zou €120,83 zijn, met voorraad €0,03 (GEZIEN boek, GOK model).
- kraken - kucoin, €150,00: munten USDC, USDT; bruto zonder voorraadgrens zou €120,83 zijn, met voorraad €0,05 (GEZIEN boek, GOK model).
- kraken - kucoin, €200,00: munten USDC, USDT; bruto zonder voorraadgrens zou €120,82 zijn, met voorraad €0,06 (GEZIEN boek, GOK model).
- kraken - kucoin, €2.000,00: munten USDC, USDT; bruto zonder voorraadgrens zou €120,54 zijn, met voorraad €0,61 (GEZIEN boek, GOK model).
- kraken - kucoin, €5.000,00: munten USDC, USDT; bruto zonder voorraadgrens zou €120,08 zijn, met voorraad €1,53 (GEZIEN boek, GOK model).

### Met minstens één grijze beurs (de 5 paren met de meeste bruto winst)

| Beurspaar | Inleg | Dag | Gemeten | Kansen | Gemist (geen voorraad) | Kleiner door voorraad | Bruto winst | Kosten terugschuiven | **Netto handel (bruto min kosten)** | Rendement handel | Koerseffect voorraad | Netto met koerseffect | Rendement met koerseffect |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| htx - xt | €100,00 | 2026-11-19 | 14.9 u | 18 | 18 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,09 | €-1,09 | -1.09% |
| htx - xt | €100,00 | 2026-11-20 | 22.8 u | 17 | 17 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,61 | €-2,61 | -2.61% |
| htx - xt | €100,00 | 2026-11-21 | 15.1 u | 12 | 12 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,41 | €-0,41 | -0.41% |
| htx - xt | €150,00 | 2026-11-19 | 14.9 u | 18 | 18 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,63 | €-1,63 | -1.09% |
| htx - xt | €150,00 | 2026-11-20 | 22.8 u | 17 | 17 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,91 | €-3,91 | -2.61% |
| htx - xt | €150,00 | 2026-11-21 | 15.1 u | 12 | 12 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,61 | €-0,61 | -0.41% |
| htx - xt | €200,00 | 2026-11-19 | 14.9 u | 18 | 18 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,17 | €-2,17 | -1.09% |
| htx - xt | €200,00 | 2026-11-20 | 22.8 u | 17 | 17 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-5,22 | €-5,22 | -2.61% |
| htx - xt | €200,00 | 2026-11-21 | 15.1 u | 12 | 12 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,82 | €-0,82 | -0.41% |
| htx - xt | €2.000,00 | 2026-11-19 | 14.9 u | 18 | 14 | 4 | €0,93 | €0,00 (0x) | **€0,93** | 0.05% | €-21,74 | €-20,80 | -1.04% |
| htx - xt | €2.000,00 | 2026-11-20 | 22.8 u | 17 | 9 | 8 | €5,56 | €0,12 (2x) | **€5,44** | 0.27% | €-52,16 | €-46,72 | -2.34% |
| htx - xt | €2.000,00 | 2026-11-21 | 15.1 u | 12 | 4 | 8 | €4,36 | €0,01 (1x) | **€4,35** | 0.22% | €-8,15 | €-3,79 | -0.19% |
| htx - xt | €5.000,00 | 2026-11-19 | 14.9 u | 18 | 5 | 13 | €9,04 | €4,34 (11x) | **€4,70** | 0.09% | €-54,39 | €-49,69 | -0.99% |
| htx - xt | €5.000,00 | 2026-11-20 | 22.8 u | 17 | 2 | 15 | €20,04 | €2,84 (9x) | **€17,20** | 0.34% | €-130,12 | €-112,91 | -2.26% |
| htx - xt | €5.000,00 | 2026-11-21 | 15.1 u | 12 | 2 | 10 | €12,04 | €1,25 (4x) | **€10,79** | 0.22% | €-19,87 | €-9,08 | -0.18% |
| gate - htx | €100,00 | 2026-11-19 | 14.9 u | 19 | 19 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,20 | €-1,20 | -1.20% |
| gate - htx | €100,00 | 2026-11-20 | 22.8 u | 32 | 32 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,86 | €-2,86 | -2.86% |
| gate - htx | €100,00 | 2026-11-21 | 15.1 u | 29 | 29 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,15 | €-0,15 | -0.15% |
| gate - htx | €150,00 | 2026-11-19 | 14.9 u | 19 | 19 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,80 | €-1,80 | -1.20% |
| gate - htx | €150,00 | 2026-11-20 | 22.8 u | 32 | 32 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-4,28 | €-4,28 | -2.86% |
| gate - htx | €150,00 | 2026-11-21 | 15.1 u | 29 | 29 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,23 | €-0,23 | -0.15% |
| gate - htx | €200,00 | 2026-11-19 | 14.9 u | 19 | 19 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,40 | €-2,40 | -1.20% |
| gate - htx | €200,00 | 2026-11-20 | 22.8 u | 32 | 32 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-5,71 | €-5,71 | -2.86% |
| gate - htx | €200,00 | 2026-11-21 | 15.1 u | 29 | 29 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,30 | €-0,30 | -0.15% |
| gate - htx | €2.000,00 | 2026-11-19 | 14.9 u | 19 | 14 | 5 | €0,61 | €0,00 (0x) | **€0,61** | 0.03% | €-24,02 | €-23,41 | -1.17% |
| gate - htx | €2.000,00 | 2026-11-20 | 22.8 u | 32 | 12 | 20 | €4,52 | €0,66 (8x) | **€3,86** | 0.19% | €-57,09 | €-53,24 | -2.66% |
| gate - htx | €2.000,00 | 2026-11-21 | 15.1 u | 29 | 12 | 17 | €2,57 | €1,18 (7x) | **€1,39** | 0.07% | €-3,02 | €-1,63 | -0.08% |
| gate - htx | €5.000,00 | 2026-11-19 | 14.9 u | 19 | 14 | 5 | €1,52 | €0,46 (2x) | **€1,06** | 0.02% | €-60,04 | €-58,98 | -1.18% |
| gate - htx | €5.000,00 | 2026-11-20 | 22.8 u | 32 | 11 | 21 | €11,38 | €1,18 (10x) | **€10,20** | 0.20% | €-142,73 | €-132,53 | -2.65% |
| gate - htx | €5.000,00 | 2026-11-21 | 15.1 u | 29 | 8 | 21 | €7,08 | €2,52 (14x) | **€4,57** | 0.09% | €-7,57 | €-3,00 | -0.06% |
| bitget - htx | €100,00 | 2026-11-19 | 14.9 u | 20 | 20 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €100,00 | 2026-11-20 | 22.8 u | 39 | 39 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €100,00 | 2026-11-21 | 15.1 u | 44 | 44 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €150,00 | 2026-11-19 | 14.9 u | 20 | 20 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €150,00 | 2026-11-20 | 22.8 u | 39 | 39 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €150,00 | 2026-11-21 | 15.1 u | 44 | 44 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €200,00 | 2026-11-19 | 14.9 u | 20 | 20 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €200,00 | 2026-11-20 | 22.8 u | 39 | 39 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €200,00 | 2026-11-21 | 15.1 u | 44 | 44 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €2.000,00 | 2026-11-19 | 14.9 u | 20 | 7 | 13 | €0,68 | €0,31 (7x) | **€0,37** | 0.02% | onbekend | onbekend* | onbekend* |
| bitget - htx | €2.000,00 | 2026-11-20 | 22.8 u | 39 | 23 | 16 | €2,42 | €0,14 (12x) | **€2,28** | 0.11% | onbekend | onbekend* | onbekend* |
| bitget - htx | €2.000,00 | 2026-11-21 | 15.1 u | 44 | 36 | 8 | €0,22 | €0,14 (7x) | **€0,08** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €5.000,00 | 2026-11-19 | 14.9 u | 20 | 6 | 14 | €1,75 | €0,70 (10x) | **€1,05** | 0.02% | onbekend | onbekend* | onbekend* |
| bitget - htx | €5.000,00 | 2026-11-20 | 22.8 u | 39 | 8 | 31 | €9,55 | €1,56 (27x) | **€7,99** | 0.16% | onbekend | onbekend* | onbekend* |
| bitget - htx | €5.000,00 | 2026-11-21 | 15.1 u | 44 | 8 | 36 | €5,30 | €0,66 (27x) | **€4,64** | 0.09% | onbekend | onbekend* | onbekend* |
| htx - kucoin | €100,00 | 2026-11-19 | 14.9 u | 16 | 16 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,62 | €-1,62 | -1.62% |
| htx - kucoin | €100,00 | 2026-11-20 | 22.8 u | 42 | 42 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,30 | €-3,30 | -3.30% |
| htx - kucoin | €100,00 | 2026-11-21 | 15.1 u | 30 | 30 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,03 | €0,03 | 0.03% |
| htx - kucoin | €150,00 | 2026-11-19 | 14.9 u | 16 | 16 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,43 | €-2,43 | -1.62% |
| htx - kucoin | €150,00 | 2026-11-20 | 22.8 u | 42 | 42 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-4,94 | €-4,94 | -3.30% |
| htx - kucoin | €150,00 | 2026-11-21 | 15.1 u | 30 | 30 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,04 | €0,04 | 0.03% |
| htx - kucoin | €200,00 | 2026-11-19 | 14.9 u | 16 | 16 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,24 | €-3,24 | -1.62% |
| htx - kucoin | €200,00 | 2026-11-20 | 22.8 u | 42 | 42 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-6,59 | €-6,59 | -3.30% |
| htx - kucoin | €200,00 | 2026-11-21 | 15.1 u | 30 | 30 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,06 | €0,06 | 0.03% |
| htx - kucoin | €2.000,00 | 2026-11-19 | 14.9 u | 16 | 10 | 6 | €0,52 | €0,00 (1x) | **€0,51** | 0.03% | €-32,36 | €-31,85 | -1.59% |
| htx - kucoin | €2.000,00 | 2026-11-20 | 22.8 u | 42 | 26 | 16 | €3,89 | €0,00 (0x) | **€3,89** | 0.19% | €-65,92 | €-62,03 | -3.10% |
| htx - kucoin | €2.000,00 | 2026-11-21 | 15.1 u | 30 | 13 | 17 | €1,19 | €0,10 (3x) | **€1,09** | 0.05% | €0,55 | €1,64 | 0.08% |
| htx - kucoin | €5.000,00 | 2026-11-19 | 14.9 u | 16 | 7 | 9 | €3,38 | €0,54 (4x) | **€2,84** | 0.06% | €-80,86 | €-78,01 | -1.56% |
| htx - kucoin | €5.000,00 | 2026-11-20 | 22.8 u | 42 | 19 | 23 | €11,62 | €2,40 (11x) | **€9,22** | 0.18% | €-164,76 | €-155,54 | -3.11% |
| htx - kucoin | €5.000,00 | 2026-11-21 | 15.1 u | 30 | 6 | 24 | €5,19 | €3,15 (13x) | **€2,04** | 0.04% | €1,34 | €3,38 | 0.07% |
| kucoin - xt | €100,00 | 2026-11-19 | 14.9 u | 13 | 13 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,04 | €-0,04 | -0.04% |
| kucoin - xt | €100,00 | 2026-11-20 | 22.8 u | 10 | 10 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,34 | €-0,34 | -0.34% |
| kucoin - xt | €100,00 | 2026-11-21 | 15.1 u | 7 | 7 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,43 | €0,43 | 0.43% |
| kucoin - xt | €150,00 | 2026-11-19 | 14.9 u | 13 | 13 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,06 | €-0,06 | -0.04% |
| kucoin - xt | €150,00 | 2026-11-20 | 22.8 u | 10 | 10 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,51 | €-0,51 | -0.34% |
| kucoin - xt | €150,00 | 2026-11-21 | 15.1 u | 7 | 7 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,64 | €0,64 | 0.43% |
| kucoin - xt | €200,00 | 2026-11-19 | 14.9 u | 13 | 13 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,08 | €-0,08 | -0.04% |
| kucoin - xt | €200,00 | 2026-11-20 | 22.8 u | 10 | 10 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,67 | €-0,67 | -0.34% |
| kucoin - xt | €200,00 | 2026-11-21 | 15.1 u | 7 | 6 | 1 | €0,08 | €0,00 (0x) | **€0,08** | 0.04% | €0,86 | €0,94 | 0.47% |
| kucoin - xt | €2.000,00 | 2026-11-19 | 14.9 u | 13 | 4 | 9 | €7,46 | €3,64 (9x) | **€3,82** | 0.19% | €-0,84 | €2,98 | 0.15% |
| kucoin - xt | €2.000,00 | 2026-11-20 | 22.8 u | 10 | 2 | 8 | €6,79 | €2,28 (6x) | **€4,51** | 0.23% | €-6,62 | €-2,11 | -0.11% |
| kucoin - xt | €2.000,00 | 2026-11-21 | 15.1 u | 7 | 1 | 6 | €6,47 | €1,85 (4x) | **€4,62** | 0.23% | €9,10 | €13,72 | 0.69% |
| kucoin - xt | €5.000,00 | 2026-11-19 | 14.9 u | 13 | 3 | 10 | €17,66 | €5,49 (11x) | **€12,17** | 0.24% | €-2,02 | €10,15 | 0.20% |
| kucoin - xt | €5.000,00 | 2026-11-20 | 22.8 u | 10 | 1 | 8 | €16,90 | €6,03 (10x) | **€10,87** | 0.22% | €-16,83 | €-5,96 | -0.12% |
| kucoin - xt | €5.000,00 | 2026-11-21 | 15.1 u | 7 | 0 | 7 | €13,13 | €2,68 (5x) | **€10,46** | 0.21% | €21,72 | €32,18 | 0.64% |

- htx - xt, €100,00: munten APEPE, APT, BIO, BSV, CARV, CBK, CFX, GT, HBAR, LUNC, MEME, PEOPLE, RAIN, SEI, SHIB, XCH, XDC, XMR; bruto zonder voorraadgrens zou €658,39 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - xt, €150,00: munten APEPE, APT, BIO, BSV, CARV, CBK, CFX, GT, HBAR, LUNC, MEME, PEOPLE, RAIN, SEI, SHIB, XCH, XDC, XMR; bruto zonder voorraadgrens zou €658,39 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - xt, €200,00: munten APEPE, APT, BIO, BSV, CARV, CBK, CFX, GT, HBAR, LUNC, MEME, PEOPLE, RAIN, SEI, SHIB, XCH, XDC, XMR; bruto zonder voorraadgrens zou €658,39 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - xt, €2.000,00: munten APEPE, APT, BIO, BSV, CARV, CBK, CFX, GT, HBAR, LUNC, MEME, PEOPLE, RAIN, SEI, SHIB, XCH, XDC, XMR; bruto zonder voorraadgrens zou €658,07 zijn, met voorraad €10,86 (GEZIEN boek, GOK model).
- htx - xt, €5.000,00: munten APEPE, APT, BIO, BSV, CARV, CBK, CFX, GT, HBAR, LUNC, MEME, PEOPLE, RAIN, SEI, SHIB, XCH, XDC, XMR; bruto zonder voorraadgrens zou €656,17 zijn, met voorraad €41,12 (GEZIEN boek, GOK model).
- gate - htx, €100,00: munten APEPE, APT, ATOM, BIO, BRISE, BSV, CBK, CRTS, CVX, ENJ, ENS, GOMINING, GT, HBAR, HIVE, KAS, LAT, LINK, LUNC, MBX, MEME, MOVR, NPC, PEOPLE, QNT, SEI, SHIB, SSV, VIRTUAL, WARD, WLD, XCH, XCN, XDC; bruto zonder voorraadgrens zou €402,06 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- gate - htx, €150,00: munten APEPE, APT, ATOM, BIO, BRISE, BSV, CBK, CRTS, CVX, ENJ, ENS, GOMINING, GT, HBAR, HIVE, KAS, LAT, LINK, LUNC, MBX, MEME, MOVR, NPC, PEOPLE, QNT, SEI, SHIB, SSV, VIRTUAL, WARD, WLD, XCH, XCN, XDC; bruto zonder voorraadgrens zou €402,06 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- gate - htx, €200,00: munten APEPE, APT, ATOM, BIO, BRISE, BSV, CBK, CRTS, CVX, ENJ, ENS, GOMINING, GT, HBAR, HIVE, KAS, LAT, LINK, LUNC, MBX, MEME, MOVR, NPC, PEOPLE, QNT, SEI, SHIB, SSV, VIRTUAL, WARD, WLD, XCH, XCN, XDC; bruto zonder voorraadgrens zou €402,06 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- gate - htx, €2.000,00: munten APEPE, APT, ATOM, BIO, BRISE, BSV, CBK, CRTS, CVX, ENJ, ENS, GOMINING, GT, HBAR, HIVE, KAS, LAT, LINK, LUNC, MBX, MEME, MOVR, NPC, PEOPLE, QNT, SEI, SHIB, SSV, VIRTUAL, WARD, WLD, XCH, XCN, XDC; bruto zonder voorraadgrens zou €401,68 zijn, met voorraad €7,70 (GEZIEN boek, GOK model).
- gate - htx, €5.000,00: munten APEPE, APT, ATOM, BIO, BRISE, BSV, CBK, CRTS, CVX, ENJ, ENS, GOMINING, GT, HBAR, HIVE, KAS, LAT, LINK, LUNC, MBX, MEME, MOVR, NPC, PEOPLE, QNT, SEI, SHIB, SSV, VIRTUAL, WARD, WLD, XCH, XCN, XDC; bruto zonder voorraadgrens zou €401,12 zijn, met voorraad €19,99 (GEZIEN boek, GOK model).
- bitget - htx, €100,00: munten AB, ACN, ALGO, ANIME, ATOM, BABY, BIO, BONK, BSV, BTT, CBK, CFX, CORE, DYDX, ENA, ENJ, ENS, HBAR, HIVE, IOST, JASMY, KAS, LAT, LINK, LIT, LUNA, LUNC, MEME, MOVR, NPC, O, PCI, PEOPLE, QNT, RIVER, SHIB, SOMI, SSV, TAO, TIA, USTC, VIRTUAL, WARD, WLD, XDC, XTZ, ZEN; bruto zonder voorraadgrens zou €422,98 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - htx, €150,00: munten AB, ACN, ALGO, ANIME, ATOM, BABY, BIO, BONK, BSV, BTT, CBK, CFX, CORE, DYDX, ENA, ENJ, ENS, HBAR, HIVE, IOST, JASMY, KAS, LAT, LINK, LIT, LUNA, LUNC, MEME, MOVR, NPC, O, PCI, PEOPLE, QNT, RIVER, SHIB, SOMI, SSV, TAO, TIA, USTC, VIRTUAL, WARD, WLD, XDC, XTZ, ZEN; bruto zonder voorraadgrens zou €422,98 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - htx, €200,00: munten AB, ACN, ALGO, ANIME, ATOM, BABY, BIO, BONK, BSV, BTT, CBK, CFX, CORE, DYDX, ENA, ENJ, ENS, HBAR, HIVE, IOST, JASMY, KAS, LAT, LINK, LIT, LUNA, LUNC, MEME, MOVR, NPC, O, PCI, PEOPLE, QNT, RIVER, SHIB, SOMI, SSV, TAO, TIA, USTC, VIRTUAL, WARD, WLD, XDC, XTZ, ZEN; bruto zonder voorraadgrens zou €422,98 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - htx, €2.000,00: munten AB, ACN, ALGO, ANIME, ATOM, BABY, BIO, BONK, BSV, BTT, CBK, CFX, CORE, DYDX, ENA, ENJ, ENS, HBAR, HIVE, IOST, JASMY, KAS, LAT, LINK, LIT, LUNA, LUNC, MEME, MOVR, NPC, O, PCI, PEOPLE, QNT, RIVER, SHIB, SOMI, SSV, TAO, TIA, USTC, VIRTUAL, WARD, WLD, XDC, XTZ, ZEN; bruto zonder voorraadgrens zou €422,85 zijn, met voorraad €3,32 (GEZIEN boek, GOK model).
- bitget - htx, €5.000,00: munten AB, ACN, ALGO, ANIME, ATOM, BABY, BIO, BONK, BSV, BTT, CBK, CFX, CORE, DYDX, ENA, ENJ, ENS, HBAR, HIVE, IOST, JASMY, KAS, LAT, LINK, LIT, LUNA, LUNC, MEME, MOVR, NPC, O, PCI, PEOPLE, QNT, RIVER, SHIB, SOMI, SSV, TAO, TIA, USTC, VIRTUAL, WARD, WLD, XDC, XTZ, ZEN; bruto zonder voorraadgrens zou €422,12 zijn, met voorraad €16,59 (GEZIEN boek, GOK model).
- htx - kucoin, €100,00: munten ACN, ALGO, ANIME, APT, BIO, BONK, BSV, BTT, CFX, CHIP, CVX, DYDX, ELA, ENJ, ENS, FET, JASMY, JST, LAT, LTC, LUNC, MEME, MOVR, NPC, ONE, PEOPLE, QNT, SHIB, SOMI, SSV, TRAC, VIRTUAL, WAN, WARD, WIN, WLD, XCH, XCN, XEC, XMR, XTZ; bruto zonder voorraadgrens zou €443,88 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - kucoin, €150,00: munten ACN, ALGO, ANIME, APT, BIO, BONK, BSV, BTT, CFX, CHIP, CVX, DYDX, ELA, ENJ, ENS, FET, JASMY, JST, LAT, LTC, LUNC, MEME, MOVR, NPC, ONE, PEOPLE, QNT, SHIB, SOMI, SSV, TRAC, VIRTUAL, WAN, WARD, WIN, WLD, XCH, XCN, XEC, XMR, XTZ; bruto zonder voorraadgrens zou €443,88 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - kucoin, €200,00: munten ACN, ALGO, ANIME, APT, BIO, BONK, BSV, BTT, CFX, CHIP, CVX, DYDX, ELA, ENJ, ENS, FET, JASMY, JST, LAT, LTC, LUNC, MEME, MOVR, NPC, ONE, PEOPLE, QNT, SHIB, SOMI, SSV, TRAC, VIRTUAL, WAN, WARD, WIN, WLD, XCH, XCN, XEC, XMR, XTZ; bruto zonder voorraadgrens zou €443,88 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - kucoin, €2.000,00: munten ACN, ALGO, ANIME, APT, BIO, BONK, BSV, BTT, CFX, CHIP, CVX, DYDX, ELA, ENJ, ENS, FET, JASMY, JST, LAT, LTC, LUNC, MEME, MOVR, NPC, ONE, PEOPLE, QNT, SHIB, SOMI, SSV, TRAC, VIRTUAL, WAN, WARD, WIN, WLD, XCH, XCN, XEC, XMR, XTZ; bruto zonder voorraadgrens zou €443,55 zijn, met voorraad €5,60 (GEZIEN boek, GOK model).
- htx - kucoin, €5.000,00: munten ACN, ALGO, ANIME, APT, BIO, BONK, BSV, BTT, CFX, CHIP, CVX, DYDX, ELA, ENJ, ENS, FET, JASMY, JST, LAT, LTC, LUNC, MEME, MOVR, NPC, ONE, PEOPLE, QNT, SHIB, SOMI, SSV, TRAC, VIRTUAL, WAN, WARD, WIN, WLD, XCH, XCN, XEC, XMR, XTZ; bruto zonder voorraadgrens zou €442,78 zijn, met voorraad €20,18 (GEZIEN boek, GOK model).
- kucoin - xt, €100,00: munten BARD, DAG, ENSO, FIGHT, LUNC, USDS, XMR; bruto zonder voorraadgrens zou €1.060,81 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- kucoin - xt, €150,00: munten BARD, DAG, ENSO, FIGHT, LUNC, USDS, XMR; bruto zonder voorraadgrens zou €1.060,81 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- kucoin - xt, €200,00: munten BARD, DAG, ENSO, FIGHT, LUNC, USDS, XMR; bruto zonder voorraadgrens zou €1.060,81 zijn, met voorraad €0,08 (GEZIEN boek, GOK model).
- kucoin - xt, €2.000,00: munten BARD, DAG, ENSO, FIGHT, LUNC, USDS, XMR; bruto zonder voorraadgrens zou €1.058,33 zijn, met voorraad €20,72 (GEZIEN boek, GOK model).
- kucoin - xt, €5.000,00: munten BARD, DAG, ENSO, FIGHT, LUNC, USDS, XMR; bruto zonder voorraadgrens zou €1.054,71 zijn, met voorraad €47,69 (GEZIEN boek, GOK model).

### Andere keuzes bij bitvavo - kraken (netto handel, alle dagen samen; GOK)

| Keuze | Inleg | Kansen | Gemist | Bruto winst | Kosten terugschuiven | Netto handel |
|---|---|---|---|---|---|---|
| standaard (schuifdrempel 25%, kostengrens 1%) | €150,00 | 70 | 70 | €0,00 | €0,00 | **€0,00** |
| standaard (schuifdrempel 25%, kostengrens 1%) | €2.000,00 | 70 | 39 | €58,08 | €12,67 | **€45,41** |
| schuifdrempel 10% | €150,00 | 70 | 70 | €0,00 | €0,00 | **€0,00** |
| schuifdrempel 10% | €2.000,00 | 70 | 41 | €56,76 | €11,05 | **€45,72** |
| schuifdrempel 40% | €150,00 | 70 | 70 | €0,00 | €0,00 | **€0,00** |
| schuifdrempel 40% | €2.000,00 | 70 | 39 | €56,46 | €12,34 | **€44,12** |
| kostengrens 2% (achteraf vergeleken) | €150,00 | 70 | 70 | €0,00 | €0,00 | **€0,00** |
| kostengrens 2% (achteraf vergeleken) | €2.000,00 | 70 | 30 | €58,18 | €26,97 | **€31,21** |
| kostengrens 5% (achteraf vergeleken) | €150,00 | 70 | 70 | €0,00 | €0,00 | **€0,00** |
| kostengrens 5% (achteraf vergeleken) | €2.000,00 | 70 | 27 | €58,70 | €30,90 | **€27,79** |
| alleen MERL en KERNEL (meer voorraad per munt, achteraf gekozen) | €150,00 | 31 | 29 | €2,05 | €0,00 | **€2,05** |
| alleen MERL en KERNEL (meer voorraad per munt, achteraf gekozen) | €2.000,00 | 31 | 13 | €222,47 | €13,18 | **€209,30** |

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

- Opnamekosten bij de echte kansen: 237 van een netwerk dat aan beide kanten open is, 146 van de beurs zelf (laagste open netwerk), 111 geschat uit wat andere beurzen voor die munt vragen (GOK). Onbekende opnamekosten tellen niet als echte kans.
- Netwerk: KuCoin, Gate, Bitget, HTX, XT, Bitstamp, Bitvavo en Poloniex geven hun netwerken per munt. Als beide beurzen dat doen en de namen te koppelen zijn, moet er een netwerk zijn dat aan beide kanten open is. Anders is het netwerk "niet te koppelen" en telt de kans mee (staat apart in de trechter).
- De duur is gemeten in stappen van ±20 seconden; een kans kan een paar rondes eerder begonnen zijn dan we zagen.
- Takerkosten: uit de API waar die ze per paar geeft, anders het standaardtarief uit de README (deels GOK).
- Laatste run: 15 beurzen antwoordden, 2280 munt-quote-paren op minstens twee beurzen (GEZIEN).
