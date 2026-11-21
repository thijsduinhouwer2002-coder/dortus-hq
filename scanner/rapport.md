# Rapport koersverschil-scanner

Gemaakt 2026-11-21 08:38 UTC uit 22 runs, samen ±45.7 uur gemeten (GEZIEN).
Echte kans = winst na alle kosten (opnamekosten bekend), opnemen en storten open (en een netwerk dat aan beide kanten open is, als de beurzen dat geven), minstens €100,00 op het boek, minstens 2 minuten blijven staan, geen andere munt met dezelfde naam.
**Vergund** = beide beurzen hebben een MiCA-vergunning (ESMA-register), vaak via een EU-dochter die minder munten kan hebben dan de wereldwijde API die we meten (GOK). **Grijs** = minstens één beurs zonder vergunning (MEXC, Bitget, HTX, Poloniex, XT, Bitfinex, Binance). Zie README.md.
**Kraken-tarief:** Kraken rekent 0,80% taker op munt tegen EUR, USD, USDT of USDC (GEZIEN, kraken.com/pro/fees, laagste trede); de scanner rekende tot 19 nov met 0,40%. 399 opgeslagen kansen met Kraken uit die runs zijn hier **opnieuw doorgerekend met 0,80%** (GOK-benadering: 0,40% van de inzet aan de Kraken-kant extra op elk gemeten punt van het boek; het boek zelf is niet bewaard). 233 houden daarna nog winst op het boek. Dat ze met hogere kosten ook korter bleven staan, telt niet mee (dus eerder te gunstig).

## Hoeveel wordt er gecontroleerd? (GEZIEN, stand.jsonl)

Per ronde (mediaan over 548 metingen): 1162 kandidaten (verschil op de ticker groter dan de takerkosten), 120 met het orderboek gecontroleerd, 2 nog nooit gecontroleerd (0%).
Bijna alle kandidaten komen aan de beurt; de aantallen hieronder missen weinig.

## Trechter (GEZIEN, eigen metingen)

| Stap | Alle beurzen | Alleen MiCA-beurzen | Met minstens één grijze beurs |
|---|---|---|---|
| Verschillen met winst op het boek na alle kosten | 44264 | 6012 | 38252 |
| ...waarvan opnemen of storten dicht | 7850 | 874 | 6976 |
| ...waarvan status onbekend (beurs geeft het niet openbaar) | 27101 | 4236 | 22865 |
| Opnemen en storten open | 9313 | 902 | 8411 |
| ...en geen netwerk dat aan beide kanten open is: valt af | 186 | 19 | 167 |
| ...en opnamekosten onbekend: valt af | 4 | 4 | 0 |
| ...en minstens €100,00 op het boek | 2730 | 557 | 2173 |
| ...en minstens 2 minuten blijven staan | 777 | 214 | 563 |
| ...en geen andere munt met dezelfde naam | 731 | 193 | 538 |
|    ...waarvan contractadres bekend en gelijk | 90 | 35 | 55 |
|    ...waarvan contractadres onbekend (telt mee, kan een andere munt zijn) | 641 | 158 | 483 |
|    ...waarvan netwerk gekoppeld en open | 476 | 94 | 382 |
|    ...waarvan netwerk niet te koppelen (telt mee) | 255 | 99 | 156 |
| **Echte kansen** (zelfde munt overlappend in de tijd samengevoegd, beste beurspaar telt) | 426 | 184 | 314 |
| Ter vergelijking: zelfde eisen, maar opnamestatus onbekend (niet meegeteld) | 1631 | 344 | 1415 |

## Echte kansen per dag (GEZIEN)

| Dag | Echt, alleen MiCA | Echt, met grijs | Mediane winst per kans bij €500 (MiCA / grijs) | Mediane duur |
|---|---|---|---|---|
| 2026-11-19 | 49 | 86 | €2,00 / €1,21 | 5.3 min |
| 2026-11-20 | 53 | 138 | €1,01 / €1,13 | 6.7 min |
| 2026-11-21 | 25 | 75 | €4,38 / €1,23 | 5.0 min |
| Totaal | 127 | 299 | €1,60 / €1,18 | 5.8 min |

## Beste munten (GEZIEN)

| | Soort | Kansen | Som winst bij €500 per kans |
|---|---|---|---|
| MERL-EUR | vergund | 28 | €820,61 |
| LUNC-USDT | grijs | 15 | €87,98 |
| USTC-USDT | grijs | 15 | €59,86 |
| KERNEL-EUR | vergund | 1 | €47,33 |
| MEME-USDT | grijs | 1 | €37,90 |
| BSV-USDT | grijs | 21 | €33,53 |
| ENSO-USDT | grijs en vergund | 8 | €33,41 |
| KYO-USDT | vergund | 5 | €30,94 |
| BARD-USDT | grijs | 4 | €24,39 |
| SHIB-USDT | grijs | 8 | €22,78 |

## Beste beursparen (kopen op > verkopen op) (GEZIEN)

| | Soort | Kansen | Som winst bij €500 per kans |
|---|---|---|---|
| bitvavo > kraken | vergund | 66 | €913,83 |
| bitget > htx | grijs | 71 | €144,54 |
| gate > kucoin | vergund | 32 | €91,91 |
| kucoin > htx | grijs | 37 | €88,26 |
| kucoin > bitget | grijs | 24 | €67,13 |
| bitget > xt | grijs | 14 | €50,97 |
| gate > htx | grijs | 21 | €39,42 |
| htx > gate | grijs | 5 | €36,53 |
| bitget > kucoin | grijs | 23 | €35,31 |
| bitget > gate | grijs | 13 | €32,84 |

Beurzen die het vaakst meedoen (koop of verkoop): bitget (grijs) 182, kucoin 167, htx (grijs) 162, gate 100, kraken 99, bitvavo 69, xt (grijs) 45, poloniex (grijs) 25 (GEZIEN).

## Hoeveel kansen blijven staan terwijl je geld schuift? (GEZIEN, duur uit eigen metingen)

Wie geen voorraad op beide beurzen heeft, moet kopen, de munt opnemen, wachten tot hij binnen is en dan verkopen. Hoe lang dat duurt verschilt per munt en netwerk: een paar minuten (snelle ketens) tot een uur of meer (Bitcoin, beurzen die opnames met de hand keuren) (GOK, niet per munt gemeten).

| Overmaaktijd | Alle beurzen | Alleen MiCA-beurzen | Met minstens één grijze beurs |
|---|---|---|---|
| 5 min | 244 van 426 (57%) | 104 van 184 (57%) | 186 van 314 (59%) |
| 10 min | 150 van 426 (35%) | 70 van 184 (38%) | 114 van 314 (36%) |
| 30 min | 79 van 426 (19%) | 43 van 184 (23%) | 60 van 314 (19%) |
| 60 min | 46 van 426 (11%) | 32 van 184 (17%) | 35 van 314 (11%) |

## Wat zou het opleveren over 3 maanden? (GOK, doorgetrokken uit de metingen)

Gemeten over ±45.7 uur (GEZIEN), doorgetrokken naar 90 dagen (GOK: aanname dat de week die we maten gewoon is).

| Beurzen | Inleg | Model | Kansen per uur | Per kans (mediaan) | 3 maanden |
|---|---|---|---|---|---|
| Alleen MiCA | €2.000,00 | bovengrens: elke kans, geld overal tegelijk | 4.03 | €1,73 | €15.046,27 |
| Alleen MiCA | €2.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 1.45 | €3,72 | €78.152,88 |
| Alleen MiCA | €5.000,00 | bovengrens: elke kans, geld overal tegelijk | 4.03 | €2,31 | €20.112,17 |
| Alleen MiCA | €5.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 1.45 | €4,37 | €150.594,99 |
| Alle (met grijs) | €2.000,00 | bovengrens: elke kans, geld overal tegelijk | 9.33 | €1,59 | €32.009,51 |
| Alle (met grijs) | €2.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 1.45 | €3,72 | €78.152,88 |
| Alle (met grijs) | €5.000,00 | bovengrens: elke kans, geld overal tegelijk | 9.33 | €1,90 | €38.274,81 |
| Alle (met grijs) | €5.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 1.45 | €4,37 | €150.594,99 |

Bovengrens: elke kans met de helft van de inleg aan elke kant, alsof het geld op alle beurzen tegelijk staat (kan in het echt niet). Beste beurspaar: het paar is **achteraf** gekozen uit de metingen (vooraf kiezen levert minder op), en het model neemt aan dat je van elke munt al voorraad op de verkoopbeurs hebt.

Waarom dit te rooskleurig is (GOK): elke kans wordt maar één keer geteld met het mediane boek, maar andere bots pakken hem ook; de munt die je als voorraad aanhoudt kan dalen; na een paar kansen moet de voorraad terug (opnamekosten en tijd); minimale opname- en ordergroottes tellen niet mee; en een kans die we 2 minuten zagen staan, staat er niet per se nog als jouw order binnenkomt. Waarom het te somber kan zijn: niet alle kandidaten zijn gecontroleerd, en met voorraad op beide beurzen kun je dezelfde kans vaker pakken als het boek zich aanvult; dat telt hier niet mee.

## Wat houd je echt over? Voorraad op twee beurzen (simulatie)

Per beurspaar: geld en munten op beide beurzen, elke echte kans uitgevoerd tegen het boek zoals gemeten (niet meer dan de ruimte op het boek en niet meer dan de voorraad op die beurs), terugschuiven als een kant leeg dreigt te raken (met opnamekosten en tijd onderweg), en het koerseffect van de aangehouden munten apart. Netto = bruto min kosten terugschuiven plus koerseffect. **Gemeten** (GEZIEN): de kansen, het boek en de koersen; **de rest is een rekenmodel** (GOK, aannames onder de tabel). Geen advies.

**Met €150: netto €0,52 per dag op bitstamp - kraken (koerseffect erbovenop €-1,97), €0,01 per dag op bitstamp - kucoin (koerseffect erbovenop €0,20), €0,25 per dag op bitvavo - kraken (koerseffect erbovenop €-2,15), €0,02 per dag op bitvavo - kucoin (koerseffect erbovenop €-1,07), €0,07 per dag op gate - kucoin (koerseffect erbovenop €-1,63), €0,01 per dag op kraken - kucoin (koerseffect erbovenop €0,20) (GOK: netto handel, rekenmodel op ±15.2 uur meting per dag, alleen MiCA).** "Per dag" is hier gemiddeld over 3 gemeten dagen achter elkaar; de eerste begint met een gelijk verdeelde voorraad; aan het eind staat de voorraad scheef, dus een volgende dag levert waarschijnlijk minder op, tenzij kansen de andere kant op hem terugbrengen (GOK).

### Alleen MiCA-beurzen (alle paren met echte kansen)

| Beurspaar | Inleg | Dag | Gemeten | Kansen | Gemist (geen voorraad) | Kleiner door voorraad | Bruto winst | Kosten terugschuiven | **Netto handel (bruto min kosten)** | Rendement handel | Koerseffect voorraad | Netto met koerseffect | Rendement met koerseffect |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| bitstamp - kraken | €100,00 | 2026-11-19 | 14.9 u | 2 | 1 | 1 | €0,59 | €0,00 (0x) | **€0,59** | 0.59% | €-0,02 | €0,57 | 0.57% |
| bitstamp - kraken | €100,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,95 | €-2,95 | -2.95% |
| bitstamp - kraken | €100,00 | 2026-11-21 | 7.9 u | 1 | 0 | 1 | €0,45 | €0,00 (0x) | **€0,45** | 0.45% | €-0,97 | €-0,53 | -0.53% |
| bitstamp - kraken | €150,00 | 2026-11-19 | 14.9 u | 2 | 1 | 1 | €0,89 | €0,00 (0x) | **€0,89** | 0.59% | €-0,03 | €0,85 | 0.57% |
| bitstamp - kraken | €150,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-4,43 | €-4,43 | -2.95% |
| bitstamp - kraken | €150,00 | 2026-11-21 | 7.9 u | 1 | 0 | 1 | €0,67 | €0,00 (0x) | **€0,67** | 0.45% | €-1,46 | €-0,79 | -0.53% |
| bitstamp - kraken | €200,00 | 2026-11-19 | 14.9 u | 2 | 1 | 1 | €1,18 | €0,00 (0x) | **€1,18** | 0.59% | €-0,04 | €1,14 | 0.57% |
| bitstamp - kraken | €200,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-5,91 | €-5,91 | -2.95% |
| bitstamp - kraken | €200,00 | 2026-11-21 | 7.9 u | 1 | 0 | 1 | €0,89 | €0,00 (0x) | **€0,89** | 0.45% | €-1,94 | €-1,05 | -0.53% |
| bitstamp - kraken | €2.000,00 | 2026-11-19 | 14.9 u | 2 | 1 | 0 | €11,71 | €0,98 (1x) | **€10,73** | 0.54% | €-0,46 | €10,27 | 0.51% |
| bitstamp - kraken | €2.000,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-59,03 | €-59,03 | -2.95% |
| bitstamp - kraken | €2.000,00 | 2026-11-21 | 7.9 u | 1 | 0 | 0 | €5,30 | €0,00 (0x) | **€5,30** | 0.26% | €-19,46 | €-14,16 | -0.71% |
| bitstamp - kraken | €5.000,00 | 2026-11-19 | 14.9 u | 2 | 1 | 0 | €11,71 | €0,00 (0x) | **€11,71** | 0.23% | €-1,10 | €10,60 | 0.21% |
| bitstamp - kraken | €5.000,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-147,75 | €-147,75 | -2.95% |
| bitstamp - kraken | €5.000,00 | 2026-11-21 | 7.9 u | 1 | 0 | 0 | €5,30 | €0,00 (0x) | **€5,30** | 0.11% | €-48,62 | €-43,33 | -0.87% |
| bitstamp - kucoin | €100,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,11 | €0,11 | 0.11% |
| bitstamp - kucoin | €100,00 | 2026-11-20 | 22.8 u | 1 | 0 | 1 | €0,00 | €0,01 (1x) | **€-0,01** | -0.01% | €0,11 | €0,10 | 0.10% |
| bitstamp - kucoin | €100,00 | 2026-11-21 | 7.9 u | 6 | 5 | 1 | €0,01 | €0,00 (0x) | **€0,01** | 0.01% | €0,18 | €0,19 | 0.19% |
| bitstamp - kucoin | €150,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,16 | €0,16 | 0.11% |
| bitstamp - kucoin | €150,00 | 2026-11-20 | 22.8 u | 1 | 0 | 1 | €0,00 | €0,01 (1x) | **€-0,01** | -0.00% | €0,16 | €0,16 | 0.11% |
| bitstamp - kucoin | €150,00 | 2026-11-21 | 7.9 u | 6 | 5 | 1 | €0,02 | €0,00 (0x) | **€0,02** | 0.01% | €0,27 | €0,29 | 0.19% |
| bitstamp - kucoin | €200,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,22 | €0,22 | 0.11% |
| bitstamp - kucoin | €200,00 | 2026-11-20 | 22.8 u | 1 | 0 | 1 | €0,01 | €0,01 (1x) | **€-0,00** | -0.00% | €0,22 | €0,22 | 0.11% |
| bitstamp - kucoin | €200,00 | 2026-11-21 | 7.9 u | 6 | 5 | 1 | €0,03 | €0,23 (1x) | **€-0,21** | -0.10% | €0,36 | €0,15 | 0.08% |
| bitstamp - kucoin | €2.000,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €2,19 | €2,19 | 0.11% |
| bitstamp - kucoin | €2.000,00 | 2026-11-20 | 22.8 u | 1 | 0 | 1 | €0,05 | €0,01 (1x) | **€0,04** | 0.00% | €2,19 | €2,24 | 0.11% |
| bitstamp - kucoin | €2.000,00 | 2026-11-21 | 7.9 u | 6 | 5 | 1 | €0,27 | €1,23 (2x) | **€-0,97** | -0.05% | €3,62 | €2,65 | 0.13% |
| bitstamp - kucoin | €5.000,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €5,49 | €5,49 | 0.11% |
| bitstamp - kucoin | €5.000,00 | 2026-11-20 | 22.8 u | 1 | 0 | 1 | €0,13 | €0,01 (1x) | **€0,12** | 0.00% | €5,48 | €5,60 | 0.11% |
| bitstamp - kucoin | €5.000,00 | 2026-11-21 | 7.9 u | 6 | 5 | 1 | €0,64 | €1,23 (2x) | **€-0,59** | -0.01% | €9,05 | €8,46 | 0.17% |
| bitvavo - kraken | €100,00 | 2026-11-19 | 14.9 u | 43 | 43 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,62 | €-0,62 | -0.62% |
| bitvavo - kraken | €100,00 | 2026-11-20 | 22.8 u | 15 | 15 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,69 | €-1,69 | -1.69% |
| bitvavo - kraken | €100,00 | 2026-11-21 | 7.9 u | 8 | 8 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,99 | €-1,99 | -1.99% |
| bitvavo - kraken | €150,00 | 2026-11-19 | 14.9 u | 43 | 43 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,93 | €-0,93 | -0.62% |
| bitvavo - kraken | €150,00 | 2026-11-20 | 22.8 u | 15 | 14 | 1 | €0,76 | €0,00 (0x) | **€0,76** | 0.51% | €-2,53 | €-1,77 | -1.18% |
| bitvavo - kraken | €150,00 | 2026-11-21 | 7.9 u | 8 | 8 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,99 | €-2,99 | -1.99% |
| bitvavo - kraken | €200,00 | 2026-11-19 | 14.9 u | 43 | 37 | 6 | €0,14 | €0,00 (0x) | **€0,14** | 0.07% | €-1,24 | €-1,10 | -0.55% |
| bitvavo - kraken | €200,00 | 2026-11-20 | 22.8 u | 15 | 14 | 1 | €1,01 | €0,00 (0x) | **€1,01** | 0.51% | €-3,38 | €-2,36 | -1.18% |
| bitvavo - kraken | €200,00 | 2026-11-21 | 7.9 u | 8 | 8 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,99 | €-3,99 | -1.99% |
| bitvavo - kraken | €2.000,00 | 2026-11-19 | 14.9 u | 43 | 27 | 16 | €11,14 | €6,40 (16x) | **€4,73** | 0.24% | €-12,31 | €-7,58 | -0.38% |
| bitvavo - kraken | €2.000,00 | 2026-11-20 | 22.8 u | 15 | 9 | 6 | €26,53 | €2,29 (5x) | **€24,24** | 1.21% | €-33,54 | €-9,31 | -0.47% |
| bitvavo - kraken | €2.000,00 | 2026-11-21 | 7.9 u | 8 | 4 | 4 | €24,10 | €1,29 (4x) | **€22,80** | 1.14% | €-39,69 | €-16,89 | -0.84% |
| bitvavo - kraken | €5.000,00 | 2026-11-19 | 14.9 u | 43 | 22 | 21 | €28,08 | €14,97 (24x) | **€13,11** | 0.26% | €-30,85 | €-17,74 | -0.35% |
| bitvavo - kraken | €5.000,00 | 2026-11-20 | 22.8 u | 15 | 2 | 13 | €68,91 | €12,31 (15x) | **€56,60** | 1.13% | €-83,17 | €-26,57 | -0.53% |
| bitvavo - kraken | €5.000,00 | 2026-11-21 | 7.9 u | 8 | 4 | 4 | €61,55 | €1,29 (4x) | **€60,26** | 1.21% | €-99,01 | €-38,75 | -0.77% |
| bitvavo - kucoin | €100,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,52 | €-0,52 | -0.52% |
| bitvavo - kucoin | €100,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,80 | €-1,80 | -1.80% |
| bitvavo - kucoin | €100,00 | 2026-11-21 | 7.9 u | 6 | 4 | 2 | €0,04 | €0,00 (0x) | **€0,04** | 0.04% | €0,17 | €0,22 | 0.22% |
| bitvavo - kucoin | €150,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,78 | €-0,78 | -0.52% |
| bitvavo - kucoin | €150,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,71 | €-2,71 | -1.80% |
| bitvavo - kucoin | €150,00 | 2026-11-21 | 7.9 u | 6 | 4 | 2 | €0,07 | €0,00 (0x) | **€0,07** | 0.04% | €0,26 | €0,33 | 0.22% |
| bitvavo - kucoin | €200,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,04 | €-1,04 | -0.52% |
| bitvavo - kucoin | €200,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,61 | €-3,61 | -1.80% |
| bitvavo - kucoin | €200,00 | 2026-11-21 | 7.9 u | 6 | 4 | 2 | €0,09 | €0,00 (0x) | **€0,09** | 0.04% | €0,35 | €0,44 | 0.22% |
| bitvavo - kucoin | €2.000,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-10,39 | €-10,39 | -0.52% |
| bitvavo - kucoin | €2.000,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-36,07 | €-36,07 | -1.80% |
| bitvavo - kucoin | €2.000,00 | 2026-11-21 | 7.9 u | 6 | 3 | 3 | €0,91 | €2,73 (3x) | **€-1,82** | -0.09% | €3,47 | €1,64 | 0.08% |
| bitvavo - kucoin | €5.000,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-25,99 | €-25,99 | -0.52% |
| bitvavo - kucoin | €5.000,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-90,18 | €-90,18 | -1.80% |
| bitvavo - kucoin | €5.000,00 | 2026-11-21 | 7.9 u | 6 | 3 | 3 | €2,24 | €2,73 (3x) | **€-0,49** | -0.01% | €8,71 | €8,22 | 0.16% |
| gate - kucoin | €100,00 | 2026-11-19 | 14.9 u | 25 | 25 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,92 | €-0,92 | -0.92% |
| gate - kucoin | €100,00 | 2026-11-20 | 22.8 u | 46 | 46 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,50 | €-0,50 | -0.50% |
| gate - kucoin | €100,00 | 2026-11-21 | 7.9 u | 16 | 16 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,83 | €-1,83 | -1.83% |
| gate - kucoin | €150,00 | 2026-11-19 | 14.9 u | 25 | 25 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,38 | €-1,38 | -0.92% |
| gate - kucoin | €150,00 | 2026-11-20 | 22.8 u | 46 | 44 | 2 | €0,20 | €0,00 (1x) | **€0,20** | 0.13% | €-0,75 | €-0,56 | -0.37% |
| gate - kucoin | €150,00 | 2026-11-21 | 7.9 u | 16 | 16 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,74 | €-2,74 | -1.83% |
| gate - kucoin | €200,00 | 2026-11-19 | 14.9 u | 25 | 25 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,84 | €-1,84 | -0.92% |
| gate - kucoin | €200,00 | 2026-11-20 | 22.8 u | 46 | 44 | 2 | €0,14 | €0,00 (1x) | **€0,14** | 0.07% | €-1,01 | €-0,87 | -0.44% |
| gate - kucoin | €200,00 | 2026-11-21 | 7.9 u | 16 | 14 | 2 | €0,13 | €0,00 (0x) | **€0,13** | 0.07% | €-3,65 | €-3,52 | -1.76% |
| gate - kucoin | €2.000,00 | 2026-11-19 | 14.9 u | 25 | 11 | 14 | €1,61 | €1,27 (8x) | **€0,34** | 0.02% | €-18,38 | €-18,04 | -0.90% |
| gate - kucoin | €2.000,00 | 2026-11-20 | 22.8 u | 46 | 22 | 24 | €8,30 | €0,92 (9x) | **€7,38** | 0.37% | €-10,02 | €-2,64 | -0.13% |
| gate - kucoin | €2.000,00 | 2026-11-21 | 7.9 u | 16 | 8 | 8 | €4,27 | €0,01 (1x) | **€4,26** | 0.21% | €-36,46 | €-32,20 | -1.61% |
| gate - kucoin | €5.000,00 | 2026-11-19 | 14.9 u | 25 | 6 | 19 | €6,60 | €3,84 (17x) | **€2,76** | 0.06% | €-46,03 | €-43,27 | -0.87% |
| gate - kucoin | €5.000,00 | 2026-11-20 | 22.8 u | 46 | 10 | 36 | €25,44 | €5,52 (27x) | **€19,91** | 0.40% | €-25,07 | €-5,16 | -0.10% |
| gate - kucoin | €5.000,00 | 2026-11-21 | 7.9 u | 16 | 1 | 15 | €12,30 | €2,22 (10x) | **€10,08** | 0.20% | €-90,98 | €-80,91 | -1.62% |
| kraken - kucoin | €100,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,11 | €0,11 | 0.11% |
| kraken - kucoin | €100,00 | 2026-11-20 | 22.8 u | 15 | 13 | 2 | €0,03 | €0,01 (1x) | **€0,02** | 0.02% | €0,11 | €0,13 | 0.13% |
| kraken - kucoin | €100,00 | 2026-11-21 | 7.9 u | 9 | 9 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,18 | €0,18 | 0.18% |
| kraken - kucoin | €150,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,16 | €0,16 | 0.11% |
| kraken - kucoin | €150,00 | 2026-11-20 | 22.8 u | 15 | 13 | 2 | €0,05 | €0,01 (1x) | **€0,04** | 0.02% | €0,16 | €0,20 | 0.13% |
| kraken - kucoin | €150,00 | 2026-11-21 | 7.9 u | 9 | 9 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,27 | €0,27 | 0.18% |
| kraken - kucoin | €200,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,22 | €0,22 | 0.11% |
| kraken - kucoin | €200,00 | 2026-11-20 | 22.8 u | 15 | 13 | 2 | €0,06 | €0,24 (2x) | **€-0,18** | -0.09% | €0,22 | €0,04 | 0.02% |
| kraken - kucoin | €200,00 | 2026-11-21 | 7.9 u | 9 | 9 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,36 | €0,36 | 0.18% |
| kraken - kucoin | €2.000,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €2,19 | €2,19 | 0.11% |
| kraken - kucoin | €2.000,00 | 2026-11-20 | 22.8 u | 15 | 13 | 2 | €0,61 | €1,24 (3x) | **€-0,63** | -0.03% | €2,19 | €1,56 | 0.08% |
| kraken - kucoin | €2.000,00 | 2026-11-21 | 7.9 u | 9 | 9 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €3,62 | €3,62 | 0.18% |
| kraken - kucoin | €5.000,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €5,49 | €5,49 | 0.11% |
| kraken - kucoin | €5.000,00 | 2026-11-20 | 22.8 u | 15 | 13 | 2 | €1,53 | €1,24 (3x) | **€0,28** | 0.01% | €5,48 | €5,77 | 0.12% |
| kraken - kucoin | €5.000,00 | 2026-11-21 | 7.9 u | 9 | 9 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €9,05 | €9,05 | 0.18% |

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
- bitvavo - kraken, €100,00: munten AVA, CVX, DYM, GMT, KERNEL, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €4.784,32 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitvavo - kraken, €150,00: munten AVA, CVX, DYM, GMT, KERNEL, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €4.784,32 zijn, met voorraad €0,76 (GEZIEN boek, GOK model).
- bitvavo - kraken, €200,00: munten AVA, CVX, DYM, GMT, KERNEL, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €4.783,92 zijn, met voorraad €1,15 (GEZIEN boek, GOK model).
- bitvavo - kraken, €2.000,00: munten AVA, CVX, DYM, GMT, KERNEL, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €4.727,03 zijn, met voorraad €61,76 (GEZIEN boek, GOK model).
- bitvavo - kraken, €5.000,00: munten AVA, CVX, DYM, GMT, KERNEL, LUNA, MERL, PROMPT; bruto zonder voorraadgrens zou €4.639,95 zijn, met voorraad €158,54 (GEZIEN boek, GOK model).
- bitvavo - kucoin, €100,00: munten ETH, USDC; bruto zonder voorraadgrens zou €16,33 zijn, met voorraad €0,04 (GEZIEN boek, GOK model).
- bitvavo - kucoin, €150,00: munten ETH, USDC; bruto zonder voorraadgrens zou €16,33 zijn, met voorraad €0,07 (GEZIEN boek, GOK model).
- bitvavo - kucoin, €200,00: munten ETH, USDC; bruto zonder voorraadgrens zou €16,33 zijn, met voorraad €0,09 (GEZIEN boek, GOK model).
- bitvavo - kucoin, €2.000,00: munten ETH, USDC; bruto zonder voorraadgrens zou €16,33 zijn, met voorraad €0,91 (GEZIEN boek, GOK model).
- bitvavo - kucoin, €5.000,00: munten ETH, USDC; bruto zonder voorraadgrens zou €16,33 zijn, met voorraad €2,24 (GEZIEN boek, GOK model).
- gate - kucoin, €100,00: munten ALKIMI, AVAIL, BARD, CCD, CHR, CWEB, CYBER, EDEN, ENSO, ERG, FTT, HIGH, HTR, IKA, IR, KYO, LUNC, NAKA, NIM, OVR, POKT, RARI, SOUL, STREAM, SUPRA, USDS, USTC, VERONA; bruto zonder voorraadgrens zou €351,42 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- gate - kucoin, €150,00: munten ALKIMI, AVAIL, BARD, CCD, CHR, CWEB, CYBER, EDEN, ENSO, ERG, FTT, HIGH, HTR, IKA, IR, KYO, LUNC, NAKA, NIM, OVR, POKT, RARI, SOUL, STREAM, SUPRA, USDS, USTC, VERONA; bruto zonder voorraadgrens zou €351,42 zijn, met voorraad €0,20 (GEZIEN boek, GOK model).
- gate - kucoin, €200,00: munten ALKIMI, AVAIL, BARD, CCD, CHR, CWEB, CYBER, EDEN, ENSO, ERG, FTT, HIGH, HTR, IKA, IR, KYO, LUNC, NAKA, NIM, OVR, POKT, RARI, SOUL, STREAM, SUPRA, USDS, USTC, VERONA; bruto zonder voorraadgrens zou €351,39 zijn, met voorraad €0,27 (GEZIEN boek, GOK model).
- gate - kucoin, €2.000,00: munten ALKIMI, AVAIL, BARD, CCD, CHR, CWEB, CYBER, EDEN, ENSO, ERG, FTT, HIGH, HTR, IKA, IR, KYO, LUNC, NAKA, NIM, OVR, POKT, RARI, SOUL, STREAM, SUPRA, USDS, USTC, VERONA; bruto zonder voorraadgrens zou €349,93 zijn, met voorraad €14,18 (GEZIEN boek, GOK model).
- gate - kucoin, €5.000,00: munten ALKIMI, AVAIL, BARD, CCD, CHR, CWEB, CYBER, EDEN, ENSO, ERG, FTT, HIGH, HTR, IKA, IR, KYO, LUNC, NAKA, NIM, OVR, POKT, RARI, SOUL, STREAM, SUPRA, USDS, USTC, VERONA; bruto zonder voorraadgrens zou €346,06 zijn, met voorraad €44,33 (GEZIEN boek, GOK model).
- kraken - kucoin, €100,00: munten USDC, USDT; bruto zonder voorraadgrens zou €116,39 zijn, met voorraad €0,03 (GEZIEN boek, GOK model).
- kraken - kucoin, €150,00: munten USDC, USDT; bruto zonder voorraadgrens zou €116,38 zijn, met voorraad €0,05 (GEZIEN boek, GOK model).
- kraken - kucoin, €200,00: munten USDC, USDT; bruto zonder voorraadgrens zou €116,37 zijn, met voorraad €0,06 (GEZIEN boek, GOK model).
- kraken - kucoin, €2.000,00: munten USDC, USDT; bruto zonder voorraadgrens zou €116,09 zijn, met voorraad €0,61 (GEZIEN boek, GOK model).
- kraken - kucoin, €5.000,00: munten USDC, USDT; bruto zonder voorraadgrens zou €115,64 zijn, met voorraad €1,53 (GEZIEN boek, GOK model).

### Met minstens één grijze beurs (de 5 paren met de meeste bruto winst)

| Beurspaar | Inleg | Dag | Gemeten | Kansen | Gemist (geen voorraad) | Kleiner door voorraad | Bruto winst | Kosten terugschuiven | **Netto handel (bruto min kosten)** | Rendement handel | Koerseffect voorraad | Netto met koerseffect | Rendement met koerseffect |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| htx - xt | €100,00 | 2026-11-19 | 14.9 u | 18 | 18 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,97 | €-0,97 | -0.97% |
| htx - xt | €100,00 | 2026-11-20 | 22.8 u | 17 | 17 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,10 | €-3,10 | -3.10% |
| htx - xt | €100,00 | 2026-11-21 | 7.9 u | 9 | 9 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,63 | €-1,63 | -1.63% |
| htx - xt | €150,00 | 2026-11-19 | 14.9 u | 18 | 18 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,46 | €-1,46 | -0.97% |
| htx - xt | €150,00 | 2026-11-20 | 22.8 u | 17 | 17 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-4,65 | €-4,65 | -3.10% |
| htx - xt | €150,00 | 2026-11-21 | 7.9 u | 9 | 9 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,45 | €-2,45 | -1.63% |
| htx - xt | €200,00 | 2026-11-19 | 14.9 u | 18 | 18 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,95 | €-1,95 | -0.97% |
| htx - xt | €200,00 | 2026-11-20 | 22.8 u | 17 | 17 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-6,20 | €-6,20 | -3.10% |
| htx - xt | €200,00 | 2026-11-21 | 7.9 u | 9 | 9 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,26 | €-3,26 | -1.63% |
| htx - xt | €2.000,00 | 2026-11-19 | 14.9 u | 18 | 14 | 4 | €1,05 | €0,00 (0x) | **€1,05** | 0.05% | €-19,46 | €-18,41 | -0.92% |
| htx - xt | €2.000,00 | 2026-11-20 | 22.8 u | 17 | 9 | 8 | €6,26 | €0,12 (2x) | **€6,14** | 0.31% | €-62,00 | €-55,86 | -2.79% |
| htx - xt | €2.000,00 | 2026-11-21 | 7.9 u | 9 | 3 | 6 | €4,70 | €0,00 (0x) | **€4,70** | 0.24% | €-32,63 | €-27,93 | -1.40% |
| htx - xt | €5.000,00 | 2026-11-19 | 14.9 u | 18 | 5 | 13 | €10,18 | €4,34 (11x) | **€5,84** | 0.12% | €-48,69 | €-42,85 | -0.86% |
| htx - xt | €5.000,00 | 2026-11-20 | 22.8 u | 17 | 2 | 15 | €22,58 | €3,75 (10x) | **€18,83** | 0.38% | €-154,71 | €-135,88 | -2.72% |
| htx - xt | €5.000,00 | 2026-11-21 | 7.9 u | 9 | 2 | 7 | €12,16 | €0,85 (2x) | **€11,30** | 0.23% | €-81,06 | €-69,76 | -1.40% |
| gate - htx | €100,00 | 2026-11-19 | 14.9 u | 19 | 19 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,17 | €-1,17 | -1.17% |
| gate - htx | €100,00 | 2026-11-20 | 22.8 u | 32 | 32 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,90 | €-2,90 | -2.90% |
| gate - htx | €100,00 | 2026-11-21 | 7.9 u | 23 | 23 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,56 | €-1,56 | -1.56% |
| gate - htx | €150,00 | 2026-11-19 | 14.9 u | 19 | 19 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,76 | €-1,76 | -1.17% |
| gate - htx | €150,00 | 2026-11-20 | 22.8 u | 32 | 32 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-4,36 | €-4,36 | -2.90% |
| gate - htx | €150,00 | 2026-11-21 | 7.9 u | 23 | 23 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,35 | €-2,35 | -1.56% |
| gate - htx | €200,00 | 2026-11-19 | 14.9 u | 19 | 19 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,34 | €-2,34 | -1.17% |
| gate - htx | €200,00 | 2026-11-20 | 22.8 u | 32 | 32 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-5,81 | €-5,81 | -2.90% |
| gate - htx | €200,00 | 2026-11-21 | 7.9 u | 23 | 23 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,13 | €-3,13 | -1.56% |
| gate - htx | €2.000,00 | 2026-11-19 | 14.9 u | 19 | 14 | 5 | €0,67 | €0,00 (0x) | **€0,67** | 0.03% | €-23,42 | €-22,75 | -1.14% |
| gate - htx | €2.000,00 | 2026-11-20 | 22.8 u | 32 | 12 | 20 | €4,95 | €0,66 (8x) | **€4,29** | 0.21% | €-58,09 | €-53,79 | -2.69% |
| gate - htx | €2.000,00 | 2026-11-21 | 7.9 u | 23 | 10 | 13 | €2,46 | €1,27 (5x) | **€1,20** | 0.06% | €-31,24 | €-30,05 | -1.50% |
| gate - htx | €5.000,00 | 2026-11-19 | 14.9 u | 19 | 7 | 12 | €5,30 | €3,55 (10x) | **€1,75** | 0.03% | €-58,59 | €-56,85 | -1.14% |
| gate - htx | €5.000,00 | 2026-11-20 | 22.8 u | 32 | 7 | 25 | €14,39 | €3,13 (15x) | **€11,26** | 0.23% | €-144,95 | €-133,69 | -2.67% |
| gate - htx | €5.000,00 | 2026-11-21 | 7.9 u | 23 | 7 | 16 | €6,75 | €1,42 (9x) | **€5,33** | 0.11% | €-77,78 | €-72,45 | -1.45% |
| htx - kucoin | €100,00 | 2026-11-19 | 14.9 u | 16 | 16 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,88 | €-1,88 | -1.88% |
| htx - kucoin | €100,00 | 2026-11-20 | 22.8 u | 42 | 42 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,32 | €-3,32 | -3.32% |
| htx - kucoin | €100,00 | 2026-11-21 | 7.9 u | 25 | 25 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,48 | €-1,48 | -1.48% |
| htx - kucoin | €150,00 | 2026-11-19 | 14.9 u | 16 | 16 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,81 | €-2,81 | -1.88% |
| htx - kucoin | €150,00 | 2026-11-20 | 22.8 u | 42 | 42 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-4,99 | €-4,99 | -3.32% |
| htx - kucoin | €150,00 | 2026-11-21 | 7.9 u | 25 | 25 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,22 | €-2,22 | -1.48% |
| htx - kucoin | €200,00 | 2026-11-19 | 14.9 u | 16 | 16 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,75 | €-3,75 | -1.88% |
| htx - kucoin | €200,00 | 2026-11-20 | 22.8 u | 42 | 42 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-6,65 | €-6,65 | -3.32% |
| htx - kucoin | €200,00 | 2026-11-21 | 7.9 u | 25 | 25 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,97 | €-2,97 | -1.48% |
| htx - kucoin | €2.000,00 | 2026-11-19 | 14.9 u | 16 | 10 | 6 | €0,57 | €0,00 (1x) | **€0,57** | 0.03% | €-37,52 | €-36,95 | -1.85% |
| htx - kucoin | €2.000,00 | 2026-11-20 | 22.8 u | 42 | 25 | 17 | €4,75 | €0,00 (0x) | **€4,75** | 0.24% | €-66,50 | €-61,74 | -3.09% |
| htx - kucoin | €2.000,00 | 2026-11-21 | 7.9 u | 25 | 12 | 13 | €1,19 | €0,09 (2x) | **€1,11** | 0.06% | €-29,66 | €-28,55 | -1.43% |
| htx - kucoin | €5.000,00 | 2026-11-19 | 14.9 u | 16 | 7 | 9 | €3,75 | €0,86 (5x) | **€2,88** | 0.06% | €-93,74 | €-90,86 | -1.82% |
| htx - kucoin | €5.000,00 | 2026-11-20 | 22.8 u | 42 | 18 | 24 | €12,91 | €2,40 (11x) | **€10,51** | 0.21% | €-166,17 | €-155,67 | -3.11% |
| htx - kucoin | €5.000,00 | 2026-11-21 | 7.9 u | 25 | 6 | 19 | €5,07 | €3,13 (12x) | **€1,94** | 0.04% | €-74,07 | €-72,13 | -1.44% |
| bitget - htx | €100,00 | 2026-11-19 | 14.9 u | 20 | 20 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €100,00 | 2026-11-20 | 22.8 u | 39 | 39 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €100,00 | 2026-11-21 | 7.9 u | 34 | 34 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €150,00 | 2026-11-19 | 14.9 u | 20 | 20 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €150,00 | 2026-11-20 | 22.8 u | 39 | 39 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €150,00 | 2026-11-21 | 7.9 u | 34 | 34 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €200,00 | 2026-11-19 | 14.9 u | 20 | 20 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €200,00 | 2026-11-20 | 22.8 u | 39 | 39 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €200,00 | 2026-11-21 | 7.9 u | 34 | 34 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €2.000,00 | 2026-11-19 | 14.9 u | 20 | 7 | 13 | €0,72 | €0,31 (7x) | **€0,41** | 0.02% | onbekend | onbekend* | onbekend* |
| bitget - htx | €2.000,00 | 2026-11-20 | 22.8 u | 39 | 11 | 28 | €3,75 | €0,37 (21x) | **€3,38** | 0.17% | onbekend | onbekend* | onbekend* |
| bitget - htx | €2.000,00 | 2026-11-21 | 7.9 u | 34 | 18 | 16 | €0,97 | €1,13 (12x) | **€-0,16** | -0.01% | onbekend | onbekend* | onbekend* |
| bitget - htx | €5.000,00 | 2026-11-19 | 14.9 u | 20 | 6 | 14 | €1,87 | €0,70 (10x) | **€1,17** | 0.02% | onbekend | onbekend* | onbekend* |
| bitget - htx | €5.000,00 | 2026-11-20 | 22.8 u | 39 | 8 | 31 | €10,20 | €1,56 (27x) | **€8,64** | 0.17% | onbekend | onbekend* | onbekend* |
| bitget - htx | €5.000,00 | 2026-11-21 | 7.9 u | 34 | 8 | 26 | €4,97 | €0,58 (18x) | **€4,40** | 0.09% | onbekend | onbekend* | onbekend* |
| kucoin - xt | €100,00 | 2026-11-19 | 14.9 u | 13 | 13 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,04 | €-0,04 | -0.04% |
| kucoin - xt | €100,00 | 2026-11-20 | 22.8 u | 10 | 10 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,34 | €-0,34 | -0.34% |
| kucoin - xt | €100,00 | 2026-11-21 | 7.9 u | 6 | 6 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,25 | €-0,25 | -0.25% |
| kucoin - xt | €150,00 | 2026-11-19 | 14.9 u | 13 | 13 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,06 | €-0,06 | -0.04% |
| kucoin - xt | €150,00 | 2026-11-20 | 22.8 u | 10 | 10 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,51 | €-0,51 | -0.34% |
| kucoin - xt | €150,00 | 2026-11-21 | 7.9 u | 6 | 6 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,38 | €-0,38 | -0.25% |
| kucoin - xt | €200,00 | 2026-11-19 | 14.9 u | 13 | 13 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,08 | €-0,08 | -0.04% |
| kucoin - xt | €200,00 | 2026-11-20 | 22.8 u | 10 | 10 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,67 | €-0,67 | -0.34% |
| kucoin - xt | €200,00 | 2026-11-21 | 7.9 u | 6 | 5 | 1 | €0,08 | €0,00 (0x) | **€0,08** | 0.04% | €-0,50 | €-0,42 | -0.21% |
| kucoin - xt | €2.000,00 | 2026-11-19 | 14.9 u | 13 | 4 | 9 | €7,46 | €3,64 (9x) | **€3,82** | 0.19% | €-0,84 | €2,98 | 0.15% |
| kucoin - xt | €2.000,00 | 2026-11-20 | 22.8 u | 10 | 2 | 8 | €6,79 | €2,28 (6x) | **€4,51** | 0.23% | €-6,62 | €-2,11 | -0.11% |
| kucoin - xt | €2.000,00 | 2026-11-21 | 7.9 u | 6 | 1 | 5 | €5,86 | €1,51 (3x) | **€4,35** | 0.22% | €-4,51 | €-0,16 | -0.01% |
| kucoin - xt | €5.000,00 | 2026-11-19 | 14.9 u | 13 | 3 | 10 | €17,66 | €5,49 (11x) | **€12,17** | 0.24% | €-2,02 | €10,15 | 0.20% |
| kucoin - xt | €5.000,00 | 2026-11-20 | 22.8 u | 10 | 1 | 8 | €16,90 | €6,03 (10x) | **€10,87** | 0.22% | €-16,83 | €-5,96 | -0.12% |
| kucoin - xt | €5.000,00 | 2026-11-21 | 7.9 u | 6 | 0 | 6 | €11,59 | €2,34 (4x) | **€9,25** | 0.19% | €-12,08 | €-2,83 | -0.06% |

- htx - xt, €100,00: munten APT, BSV, CARV, CBK, CFX, GT, HBAR, LUNC, MEME, PEOPLE, RAIN, SEI, SHIB, XCH, XDC, XMR; bruto zonder voorraadgrens zou €637,28 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - xt, €150,00: munten APT, BSV, CARV, CBK, CFX, GT, HBAR, LUNC, MEME, PEOPLE, RAIN, SEI, SHIB, XCH, XDC, XMR; bruto zonder voorraadgrens zou €637,28 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - xt, €200,00: munten APT, BSV, CARV, CBK, CFX, GT, HBAR, LUNC, MEME, PEOPLE, RAIN, SEI, SHIB, XCH, XDC, XMR; bruto zonder voorraadgrens zou €637,28 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - xt, €2.000,00: munten APT, BSV, CARV, CBK, CFX, GT, HBAR, LUNC, MEME, PEOPLE, RAIN, SEI, SHIB, XCH, XDC, XMR; bruto zonder voorraadgrens zou €636,91 zijn, met voorraad €12,01 (GEZIEN boek, GOK model).
- htx - xt, €5.000,00: munten APT, BSV, CARV, CBK, CFX, GT, HBAR, LUNC, MEME, PEOPLE, RAIN, SEI, SHIB, XCH, XDC, XMR; bruto zonder voorraadgrens zou €634,77 zijn, met voorraad €44,92 (GEZIEN boek, GOK model).
- gate - htx, €100,00: munten APEPE, APT, ATOM, BRISE, BSV, CBK, CRTS, CVX, ENJ, ENS, GOMINING, GT, KAS, LAT, LINK, LUNC, MBX, MEME, MOVR, NPC, PEOPLE, QNT, SEI, SHIB, SSV, VIRTUAL, WARD, WLD, XCH, XCN, XDC; bruto zonder voorraadgrens zou €388,25 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- gate - htx, €150,00: munten APEPE, APT, ATOM, BRISE, BSV, CBK, CRTS, CVX, ENJ, ENS, GOMINING, GT, KAS, LAT, LINK, LUNC, MBX, MEME, MOVR, NPC, PEOPLE, QNT, SEI, SHIB, SSV, VIRTUAL, WARD, WLD, XCH, XCN, XDC; bruto zonder voorraadgrens zou €388,25 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- gate - htx, €200,00: munten APEPE, APT, ATOM, BRISE, BSV, CBK, CRTS, CVX, ENJ, ENS, GOMINING, GT, KAS, LAT, LINK, LUNC, MBX, MEME, MOVR, NPC, PEOPLE, QNT, SEI, SHIB, SSV, VIRTUAL, WARD, WLD, XCH, XCN, XDC; bruto zonder voorraadgrens zou €388,25 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- gate - htx, €2.000,00: munten APEPE, APT, ATOM, BRISE, BSV, CBK, CRTS, CVX, ENJ, ENS, GOMINING, GT, KAS, LAT, LINK, LUNC, MBX, MEME, MOVR, NPC, PEOPLE, QNT, SEI, SHIB, SSV, VIRTUAL, WARD, WLD, XCH, XCN, XDC; bruto zonder voorraadgrens zou €387,84 zijn, met voorraad €8,08 (GEZIEN boek, GOK model).
- gate - htx, €5.000,00: munten APEPE, APT, ATOM, BRISE, BSV, CBK, CRTS, CVX, ENJ, ENS, GOMINING, GT, KAS, LAT, LINK, LUNC, MBX, MEME, MOVR, NPC, PEOPLE, QNT, SEI, SHIB, SSV, VIRTUAL, WARD, WLD, XCH, XCN, XDC; bruto zonder voorraadgrens zou €385,29 zijn, met voorraad €26,44 (GEZIEN boek, GOK model).
- htx - kucoin, €100,00: munten ALGO, ANIME, APT, BONK, BSV, BTT, CFX, CHIP, CVX, DYDX, ELA, ENJ, ENS, FET, JASMY, LAT, LTC, LUNC, MEME, MOVR, NPC, ONE, PEOPLE, QNT, SHIB, SOMI, SSV, TRAC, VIRTUAL, WAN, WARD, WLD, XCH, XCN, XEC, XMR, XTZ; bruto zonder voorraadgrens zou €433,82 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - kucoin, €150,00: munten ALGO, ANIME, APT, BONK, BSV, BTT, CFX, CHIP, CVX, DYDX, ELA, ENJ, ENS, FET, JASMY, LAT, LTC, LUNC, MEME, MOVR, NPC, ONE, PEOPLE, QNT, SHIB, SOMI, SSV, TRAC, VIRTUAL, WAN, WARD, WLD, XCH, XCN, XEC, XMR, XTZ; bruto zonder voorraadgrens zou €433,82 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - kucoin, €200,00: munten ALGO, ANIME, APT, BONK, BSV, BTT, CFX, CHIP, CVX, DYDX, ELA, ENJ, ENS, FET, JASMY, LAT, LTC, LUNC, MEME, MOVR, NPC, ONE, PEOPLE, QNT, SHIB, SOMI, SSV, TRAC, VIRTUAL, WAN, WARD, WLD, XCH, XCN, XEC, XMR, XTZ; bruto zonder voorraadgrens zou €433,82 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - kucoin, €2.000,00: munten ALGO, ANIME, APT, BONK, BSV, BTT, CFX, CHIP, CVX, DYDX, ELA, ENJ, ENS, FET, JASMY, LAT, LTC, LUNC, MEME, MOVR, NPC, ONE, PEOPLE, QNT, SHIB, SOMI, SSV, TRAC, VIRTUAL, WAN, WARD, WLD, XCH, XCN, XEC, XMR, XTZ; bruto zonder voorraadgrens zou €433,45 zijn, met voorraad €6,52 (GEZIEN boek, GOK model).
- htx - kucoin, €5.000,00: munten ALGO, ANIME, APT, BONK, BSV, BTT, CFX, CHIP, CVX, DYDX, ELA, ENJ, ENS, FET, JASMY, LAT, LTC, LUNC, MEME, MOVR, NPC, ONE, PEOPLE, QNT, SHIB, SOMI, SSV, TRAC, VIRTUAL, WAN, WARD, WLD, XCH, XCN, XEC, XMR, XTZ; bruto zonder voorraadgrens zou €432,60 zijn, met voorraad €21,72 (GEZIEN boek, GOK model).
- bitget - htx, €100,00: munten AB, ACN, ALGO, ANIME, ATOM, BABY, BONK, BSV, BTT, CBK, CFX, CORE, DYDX, ENA, ENJ, ENS, HBAR, IOST, JASMY, KAS, LAT, LINK, LIT, LUNA, LUNC, MEME, MOVR, NPC, O, PEOPLE, QNT, RIVER, SHIB, SOMI, SSV, TAO, TIA, USTC, VIRTUAL, WARD, WLD, XDC, XTZ, ZEN; bruto zonder voorraadgrens zou €403,33 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - htx, €150,00: munten AB, ACN, ALGO, ANIME, ATOM, BABY, BONK, BSV, BTT, CBK, CFX, CORE, DYDX, ENA, ENJ, ENS, HBAR, IOST, JASMY, KAS, LAT, LINK, LIT, LUNA, LUNC, MEME, MOVR, NPC, O, PEOPLE, QNT, RIVER, SHIB, SOMI, SSV, TAO, TIA, USTC, VIRTUAL, WARD, WLD, XDC, XTZ, ZEN; bruto zonder voorraadgrens zou €403,33 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - htx, €200,00: munten AB, ACN, ALGO, ANIME, ATOM, BABY, BONK, BSV, BTT, CBK, CFX, CORE, DYDX, ENA, ENJ, ENS, HBAR, IOST, JASMY, KAS, LAT, LINK, LIT, LUNA, LUNC, MEME, MOVR, NPC, O, PEOPLE, QNT, RIVER, SHIB, SOMI, SSV, TAO, TIA, USTC, VIRTUAL, WARD, WLD, XDC, XTZ, ZEN; bruto zonder voorraadgrens zou €403,33 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - htx, €2.000,00: munten AB, ACN, ALGO, ANIME, ATOM, BABY, BONK, BSV, BTT, CBK, CFX, CORE, DYDX, ENA, ENJ, ENS, HBAR, IOST, JASMY, KAS, LAT, LINK, LIT, LUNA, LUNC, MEME, MOVR, NPC, O, PEOPLE, QNT, RIVER, SHIB, SOMI, SSV, TAO, TIA, USTC, VIRTUAL, WARD, WLD, XDC, XTZ, ZEN; bruto zonder voorraadgrens zou €403,09 zijn, met voorraad €5,44 (GEZIEN boek, GOK model).
- bitget - htx, €5.000,00: munten AB, ACN, ALGO, ANIME, ATOM, BABY, BONK, BSV, BTT, CBK, CFX, CORE, DYDX, ENA, ENJ, ENS, HBAR, IOST, JASMY, KAS, LAT, LINK, LIT, LUNA, LUNC, MEME, MOVR, NPC, O, PEOPLE, QNT, RIVER, SHIB, SOMI, SSV, TAO, TIA, USTC, VIRTUAL, WARD, WLD, XDC, XTZ, ZEN; bruto zonder voorraadgrens zou €402,41 zijn, met voorraad €17,03 (GEZIEN boek, GOK model).
- kucoin - xt, €100,00: munten BARD, DAG, ENSO, FIGHT, LUNC, USDS, XMR; bruto zonder voorraadgrens zou €1.025,31 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- kucoin - xt, €150,00: munten BARD, DAG, ENSO, FIGHT, LUNC, USDS, XMR; bruto zonder voorraadgrens zou €1.025,31 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- kucoin - xt, €200,00: munten BARD, DAG, ENSO, FIGHT, LUNC, USDS, XMR; bruto zonder voorraadgrens zou €1.025,31 zijn, met voorraad €0,08 (GEZIEN boek, GOK model).
- kucoin - xt, €2.000,00: munten BARD, DAG, ENSO, FIGHT, LUNC, USDS, XMR; bruto zonder voorraadgrens zou €1.022,83 zijn, met voorraad €20,11 (GEZIEN boek, GOK model).
- kucoin - xt, €5.000,00: munten BARD, DAG, ENSO, FIGHT, LUNC, USDS, XMR; bruto zonder voorraadgrens zou €1.019,21 zijn, met voorraad €46,14 (GEZIEN boek, GOK model).

### Andere keuzes bij bitvavo - kraken (netto handel, alle dagen samen; GOK)

| Keuze | Inleg | Kansen | Gemist | Bruto winst | Kosten terugschuiven | Netto handel |
|---|---|---|---|---|---|---|
| standaard (schuifdrempel 25%, kostengrens 1%) | €150,00 | 66 | 65 | €0,76 | €0,00 | **€0,76** |
| standaard (schuifdrempel 25%, kostengrens 1%) | €2.000,00 | 66 | 40 | €61,76 | €9,99 | **€51,77** |
| schuifdrempel 10% | €150,00 | 66 | 65 | €0,76 | €0,00 | **€0,76** |
| schuifdrempel 10% | €2.000,00 | 66 | 41 | €61,80 | €9,68 | **€52,12** |
| schuifdrempel 40% | €150,00 | 66 | 65 | €0,76 | €0,00 | **€0,76** |
| schuifdrempel 40% | €2.000,00 | 66 | 38 | €64,59 | €12,61 | **€51,98** |
| kostengrens 2% (achteraf vergeleken) | €150,00 | 66 | 65 | €0,76 | €0,00 | **€0,76** |
| kostengrens 2% (achteraf vergeleken) | €2.000,00 | 66 | 28 | €64,47 | €28,57 | **€35,90** |
| kostengrens 5% (achteraf vergeleken) | €150,00 | 66 | 65 | €0,76 | €0,00 | **€0,76** |
| kostengrens 5% (achteraf vergeleken) | €2.000,00 | 66 | 28 | €64,47 | €28,57 | **€35,90** |
| alleen MERL en KERNEL (meer voorraad per munt, achteraf gekozen) | €150,00 | 29 | 27 | €2,05 | €0,00 | **€2,05** |
| alleen MERL en KERNEL (meer voorraad per munt, achteraf gekozen) | €2.000,00 | 29 | 13 | €219,60 | €11,85 | **€207,75** |

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

- Opnamekosten bij de echte kansen: 188 van een netwerk dat aan beide kanten open is, 134 van de beurs zelf (laagste open netwerk), 104 geschat uit wat andere beurzen voor die munt vragen (GOK). Onbekende opnamekosten tellen niet als echte kans.
- Netwerk: KuCoin, Gate, Bitget, HTX, XT, Bitstamp, Bitvavo en Poloniex geven hun netwerken per munt. Als beide beurzen dat doen en de namen te koppelen zijn, moet er een netwerk zijn dat aan beide kanten open is. Anders is het netwerk "niet te koppelen" en telt de kans mee (staat apart in de trechter).
- De duur is gemeten in stappen van ±20 seconden; een kans kan een paar rondes eerder begonnen zijn dan we zagen.
- Takerkosten: uit de API waar die ze per paar geeft, anders het standaardtarief uit de README (deels GOK).
- Laatste run: 15 beurzen antwoordden, 2280 munt-quote-paren op minstens twee beurzen (GEZIEN).
