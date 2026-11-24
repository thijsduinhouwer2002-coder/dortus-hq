# Rapport koersverschil-scanner

Gemaakt 2026-11-24 07:48 UTC uit 36 runs, samen ±109.3 uur gemeten (GEZIEN).
Echte kans = winst na alle kosten (opnamekosten bekend), opnemen en storten open (en een netwerk dat aan beide kanten open is, als de beurzen dat geven), minstens €100,00 op het boek, minstens 2 minuten blijven staan, geen andere munt met dezelfde naam.
**Vergund** = beide beurzen hebben een MiCA-vergunning (ESMA-register), vaak via een EU-dochter die minder munten kan hebben dan de wereldwijde API die we meten (GOK). **Grijs** = minstens één beurs zonder vergunning (MEXC, Bitget, HTX, Poloniex, XT, Bitfinex, Binance). Zie README.md.
**Kraken-tarief:** Kraken rekent 0,80% taker op munt tegen EUR, USD, USDT of USDC (GEZIEN, kraken.com/pro/fees, laagste trede); de scanner rekende tot 19 nov met 0,40%. 399 opgeslagen kansen met Kraken uit die runs zijn hier **opnieuw doorgerekend met 0,80%** (GOK-benadering: 0,40% van de inzet aan de Kraken-kant extra op elk gemeten punt van het boek; het boek zelf is niet bewaard). 233 houden daarna nog winst op het boek. Dat ze met hogere kosten ook korter bleven staan, telt niet mee (dus eerder te gunstig).

## Hoeveel wordt er gecontroleerd? (GEZIEN, stand.jsonl)

Per ronde (mediaan over 1312 metingen): 1063 kandidaten (verschil op de ticker groter dan de takerkosten), 120 met het orderboek gecontroleerd, 2 nog nooit gecontroleerd (0%).
Bijna alle kandidaten komen aan de beurt; de aantallen hieronder missen weinig.

## Trechter (GEZIEN, eigen metingen)

| Stap | Alle beurzen | Alleen MiCA-beurzen | Met minstens één grijze beurs |
|---|---|---|---|
| Verschillen met winst op het boek na alle kosten | 91488 | 12985 | 78503 |
| ...waarvan opnemen of storten dicht | 16600 | 1872 | 14728 |
| ...waarvan status onbekend (beurs geeft het niet openbaar) | 55146 | 9279 | 45867 |
| Opnemen en storten open | 19742 | 1834 | 17908 |
| ...en geen netwerk dat aan beide kanten open is: valt af | 822 | 73 | 749 |
| ...en opnamekosten onbekend: valt af | 5 | 5 | 0 |
| ...en minstens €100,00 op het boek | 6061 | 1081 | 4980 |
| ...en minstens 2 minuten blijven staan | 1675 | 423 | 1252 |
| ...en geen andere munt met dezelfde naam | 1607 | 388 | 1219 |
|    ...waarvan contractadres bekend en gelijk | 269 | 80 | 189 |
|    ...waarvan contractadres onbekend (telt mee, kan een andere munt zijn) | 1338 | 308 | 1030 |
|    ...waarvan netwerk gekoppeld en open | 1036 | 190 | 846 |
|    ...waarvan netwerk niet te koppelen (telt mee) | 571 | 198 | 373 |
| **Echte kansen** (zelfde munt overlappend in de tijd samengevoegd, beste beurspaar telt) | 1011 | 378 | 744 |
| Ter vergelijking: zelfde eisen, maar opnamestatus onbekend (niet meegeteld) | 3947 | 1031 | 3297 |

## Echte kansen per dag (GEZIEN)

| Dag | Echt, alleen MiCA | Echt, met grijs | Mediane winst per kans bij €500 (MiCA / grijs) | Mediane duur |
|---|---|---|---|---|
| 2026-11-19 | 49 | 86 | €2,00 / €1,21 | 5.3 min |
| 2026-11-20 | 53 | 138 | €1,01 / €1,13 | 6.7 min |
| 2026-11-21 | 61 | 176 | €1,13 / €0,88 | 6.7 min |
| 2026-11-22 | 60 | 165 | €1,74 / €0,93 | 9.3 min |
| 2026-11-23 | 53 | 113 | €1,10 / €1,00 | 6.8 min |
| 2026-11-24 | 15 | 42 | €0,77 / €0,42 | 3.7 min |
| Totaal | 291 | 720 | €1,24 / €0,88 | 6.7 min |

## Beste munten (GEZIEN)

| | Soort | Kansen | Som winst bij €500 per kans |
|---|---|---|---|
| MERL-EUR | vergund | 71 | €1.012,65 |
| AI-USDT | grijs | 28 | €354,56 |
| LUNC-USDT | grijs | 38 | €152,20 |
| PYR-USDT | grijs | 11 | €138,01 |
| USTC-USDT | grijs en vergund | 46 | €114,20 |
| NES-USDT | grijs en vergund | 8 | €95,21 |
| XMR-USDT | grijs | 71 | €87,07 |
| DCR-USDT | grijs en vergund | 2 | €52,11 |
| IR-USDT | grijs en vergund | 19 | €48,47 |
| ENSO-USDT | grijs en vergund | 15 | €48,21 |

## Beste beursparen (kopen op > verkopen op) (GEZIEN)

| | Soort | Kansen | Som winst bij €500 per kans |
|---|---|---|---|
| bitvavo > kraken | vergund | 160 | €1.140,57 |
| htx > kucoin | grijs | 41 | €363,49 |
| htx > gate | grijs | 35 | €209,03 |
| bitget > htx | grijs | 98 | €200,23 |
| gate > kucoin | vergund | 58 | €167,93 |
| kucoin > bitget | grijs | 79 | €119,46 |
| bitget > kucoin | grijs | 80 | €117,92 |
| kucoin > htx | grijs | 48 | €106,71 |
| kucoin > gate | vergund | 57 | €96,92 |
| bitget > xt | grijs | 31 | €93,67 |

Beurzen die het vaakst meedoen (koop of verkoop): kucoin 446, bitget (grijs) 419, htx (grijs) 339, gate 246, kraken 199, bitvavo 175, poloniex (grijs) 109, xt (grijs) 86 (GEZIEN).

## Hoeveel kansen blijven staan terwijl je geld schuift? (GEZIEN, duur uit eigen metingen)

Wie geen voorraad op beide beurzen heeft, moet kopen, de munt opnemen, wachten tot hij binnen is en dan verkopen. Hoe lang dat duurt verschilt per munt en netwerk: een paar minuten (snelle ketens) tot een uur of meer (Bitcoin, beurzen die opnames met de hand keuren) (GOK, niet per munt gemeten).

| Overmaaktijd | Alle beurzen | Alleen MiCA-beurzen | Met minstens één grijze beurs |
|---|---|---|---|
| 5 min | 598 van 1011 (59%) | 231 van 378 (61%) | 438 van 744 (59%) |
| 10 min | 399 van 1011 (39%) | 161 van 378 (43%) | 292 van 744 (39%) |
| 30 min | 201 van 1011 (20%) | 79 van 378 (21%) | 156 van 744 (21%) |
| 60 min | 113 van 1011 (11%) | 51 van 378 (13%) | 88 van 744 (12%) |

## Wat zou het opleveren over 3 maanden? (GOK, doorgetrokken uit de metingen)

Gemeten over ±109.3 uur (GEZIEN), doorgetrokken naar 90 dagen (GOK: aanname dat de week die we maten gewoon is).

| Beurzen | Inleg | Model | Kansen per uur | Per kans (mediaan) | 3 maanden |
|---|---|---|---|---|---|
| Alleen MiCA | €2.000,00 | bovengrens: elke kans, geld overal tegelijk | 3.46 | €1,58 | €11.789,41 |
| Alleen MiCA | €2.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 1.46 | €2,53 | €40.549,68 |
| Alleen MiCA | €5.000,00 | bovengrens: elke kans, geld overal tegelijk | 3.46 | €1,90 | €14.214,12 |
| Alleen MiCA | €5.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 1.46 | €3,19 | €74.944,20 |
| Alle (met grijs) | €2.000,00 | bovengrens: elke kans, geld overal tegelijk | 9.25 | €1,35 | €26.959,22 |
| Alle (met grijs) | €2.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 1.46 | €2,53 | €40.549,68 |
| Alle (met grijs) | €5.000,00 | bovengrens: elke kans, geld overal tegelijk | 9.25 | €1,58 | €31.638,84 |
| Alle (met grijs) | €5.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 1.46 | €3,19 | €74.944,20 |

Bovengrens: elke kans met de helft van de inleg aan elke kant, alsof het geld op alle beurzen tegelijk staat (kan in het echt niet). Beste beurspaar: het paar is **achteraf** gekozen uit de metingen (vooraf kiezen levert minder op), en het model neemt aan dat je van elke munt al voorraad op de verkoopbeurs hebt.

Waarom dit te rooskleurig is (GOK): elke kans wordt maar één keer geteld met het mediane boek, maar andere bots pakken hem ook; de munt die je als voorraad aanhoudt kan dalen; na een paar kansen moet de voorraad terug (opnamekosten en tijd); minimale opname- en ordergroottes tellen niet mee; en een kans die we 2 minuten zagen staan, staat er niet per se nog als jouw order binnenkomt. Waarom het te somber kan zijn: niet alle kandidaten zijn gecontroleerd, en met voorraad op beide beurzen kun je dezelfde kans vaker pakken als het boek zich aanvult; dat telt hier niet mee.

## Wat houd je echt over? Voorraad op twee beurzen (simulatie)

Per beurspaar: geld en munten op beide beurzen, elke echte kans uitgevoerd tegen het boek zoals gemeten (niet meer dan de ruimte op het boek en niet meer dan de voorraad op die beurs), terugschuiven als een kant leeg dreigt te raken (met opnamekosten en tijd onderweg), en het koerseffect van de aangehouden munten apart. Netto = bruto min kosten terugschuiven plus koerseffect. **Gemeten** (GEZIEN): de kansen, het boek en de koersen; **de rest is een rekenmodel** (GOK, aannames onder de tabel). Geen advies.

**Met €150: netto €0,26 per dag op bitstamp - kraken (koerseffect erbovenop €-1,27), €0,00 per dag op bitstamp - kucoin (koerseffect erbovenop €0,06), €0,00 per dag op bitvavo - kraken (koerseffect erbovenop €-0,48), €0,01 per dag op bitvavo - kucoin (koerseffect erbovenop €-0,28), €0,00 per dag op gate - kucoin (koerseffect erbovenop €-1,21), €0,01 per dag op kraken - kucoin (koerseffect erbovenop €0,06) (GOK: netto handel, rekenmodel op ±18.2 uur meting per dag, alleen MiCA).** "Per dag" is hier gemiddeld over 6 gemeten dagen achter elkaar; de eerste begint met een gelijk verdeelde voorraad; aan het eind staat de voorraad scheef, dus een volgende dag levert waarschijnlijk minder op, tenzij kansen de andere kant op hem terugbrengen (GOK).

### Alleen MiCA-beurzen (alle paren met echte kansen)

| Beurspaar | Inleg | Dag | Gemeten | Kansen | Gemist (geen voorraad) | Kleiner door voorraad | Bruto winst | Kosten terugschuiven | **Netto handel (bruto min kosten)** | Rendement handel | Koerseffect voorraad | Netto met koerseffect | Rendement met koerseffect |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| bitstamp - kraken | €100,00 | 2026-11-19 | 14.9 u | 2 | 1 | 1 | €0,59 | €0,00 (0x) | **€0,59** | 0.59% | €-0,02 | €0,57 | 0.57% |
| bitstamp - kraken | €100,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,95 | €-2,95 | -2.95% |
| bitstamp - kraken | €100,00 | 2026-11-21 | 22.9 u | 1 | 0 | 1 | €0,45 | €0,00 (0x) | **€0,45** | 0.45% | €-0,70 | €-0,25 | -0.25% |
| bitstamp - kraken | €100,00 | 2026-11-22 | 22.1 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,42 | €-1,42 | -1.42% |
| bitstamp - kraken | €100,00 | 2026-11-23 | 19.7 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,23 | €-0,23 | -0.23% |
| bitstamp - kraken | €100,00 | 2026-11-24 | 6.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,24 | €0,24 | 0.24% |
| bitstamp - kraken | €150,00 | 2026-11-19 | 14.9 u | 2 | 1 | 1 | €0,89 | €0,00 (0x) | **€0,89** | 0.59% | €-0,03 | €0,85 | 0.57% |
| bitstamp - kraken | €150,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-4,43 | €-4,43 | -2.95% |
| bitstamp - kraken | €150,00 | 2026-11-21 | 22.9 u | 1 | 0 | 1 | €0,67 | €0,00 (0x) | **€0,67** | 0.45% | €-1,05 | €-0,38 | -0.25% |
| bitstamp - kraken | €150,00 | 2026-11-22 | 22.1 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,13 | €-2,13 | -1.42% |
| bitstamp - kraken | €150,00 | 2026-11-23 | 19.7 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,34 | €-0,34 | -0.23% |
| bitstamp - kraken | €150,00 | 2026-11-24 | 6.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,37 | €0,37 | 0.24% |
| bitstamp - kraken | €200,00 | 2026-11-19 | 14.9 u | 2 | 1 | 1 | €1,18 | €0,00 (0x) | **€1,18** | 0.59% | €-0,04 | €1,14 | 0.57% |
| bitstamp - kraken | €200,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-5,91 | €-5,91 | -2.95% |
| bitstamp - kraken | €200,00 | 2026-11-21 | 22.9 u | 1 | 0 | 1 | €0,89 | €0,00 (0x) | **€0,89** | 0.45% | €-1,40 | €-0,51 | -0.25% |
| bitstamp - kraken | €200,00 | 2026-11-22 | 22.1 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,85 | €-2,85 | -1.42% |
| bitstamp - kraken | €200,00 | 2026-11-23 | 19.7 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,46 | €-0,46 | -0.23% |
| bitstamp - kraken | €200,00 | 2026-11-24 | 6.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,49 | €0,49 | 0.24% |
| bitstamp - kraken | €2.000,00 | 2026-11-19 | 14.9 u | 2 | 1 | 0 | €11,71 | €0,98 (1x) | **€10,73** | 0.54% | €-0,46 | €10,27 | 0.51% |
| bitstamp - kraken | €2.000,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-59,03 | €-59,03 | -2.95% |
| bitstamp - kraken | €2.000,00 | 2026-11-21 | 22.9 u | 1 | 0 | 0 | €5,30 | €0,00 (0x) | **€5,30** | 0.26% | €-14,01 | €-8,71 | -0.44% |
| bitstamp - kraken | €2.000,00 | 2026-11-22 | 22.1 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-28,41 | €-28,41 | -1.42% |
| bitstamp - kraken | €2.000,00 | 2026-11-23 | 19.7 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-4,54 | €-4,54 | -0.23% |
| bitstamp - kraken | €2.000,00 | 2026-11-24 | 6.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €4,91 | €4,91 | 0.25% |
| bitstamp - kraken | €5.000,00 | 2026-11-19 | 14.9 u | 2 | 1 | 0 | €11,71 | €0,00 (0x) | **€11,71** | 0.23% | €-1,10 | €10,60 | 0.21% |
| bitstamp - kraken | €5.000,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-147,75 | €-147,75 | -2.95% |
| bitstamp - kraken | €5.000,00 | 2026-11-21 | 22.9 u | 1 | 0 | 0 | €5,30 | €0,00 (0x) | **€5,30** | 0.11% | €-35,01 | €-29,71 | -0.59% |
| bitstamp - kraken | €5.000,00 | 2026-11-22 | 22.1 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-71,15 | €-71,15 | -1.42% |
| bitstamp - kraken | €5.000,00 | 2026-11-23 | 19.7 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-11,41 | €-11,41 | -0.23% |
| bitstamp - kraken | €5.000,00 | 2026-11-24 | 6.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €12,23 | €12,23 | 0.24% |
| bitstamp - kucoin | €100,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,11 | €0,11 | 0.11% |
| bitstamp - kucoin | €100,00 | 2026-11-20 | 22.8 u | 1 | 0 | 1 | €0,00 | €0,01 (1x) | **€-0,01** | -0.01% | €0,11 | €0,10 | 0.10% |
| bitstamp - kucoin | €100,00 | 2026-11-21 | 22.9 u | 6 | 5 | 1 | €0,01 | €0,00 (0x) | **€0,01** | 0.01% | €-0,16 | €-0,15 | -0.15% |
| bitstamp - kucoin | €100,00 | 2026-11-22 | 22.1 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,08 | €-0,08 | -0.08% |
| bitstamp - kucoin | €100,00 | 2026-11-23 | 19.7 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,29 | €0,29 | 0.29% |
| bitstamp - kucoin | €100,00 | 2026-11-24 | 6.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,01 | €-0,01 | -0.01% |
| bitstamp - kucoin | €150,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,16 | €0,16 | 0.11% |
| bitstamp - kucoin | €150,00 | 2026-11-20 | 22.8 u | 1 | 0 | 1 | €0,00 | €0,01 (1x) | **€-0,01** | -0.00% | €0,16 | €0,16 | 0.11% |
| bitstamp - kucoin | €150,00 | 2026-11-21 | 22.9 u | 6 | 5 | 1 | €0,02 | €0,00 (0x) | **€0,02** | 0.01% | €-0,24 | €-0,22 | -0.15% |
| bitstamp - kucoin | €150,00 | 2026-11-22 | 22.1 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,12 | €-0,12 | -0.08% |
| bitstamp - kucoin | €150,00 | 2026-11-23 | 19.7 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,44 | €0,44 | 0.29% |
| bitstamp - kucoin | €150,00 | 2026-11-24 | 6.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,02 | €-0,02 | -0.01% |
| bitstamp - kucoin | €200,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,22 | €0,22 | 0.11% |
| bitstamp - kucoin | €200,00 | 2026-11-20 | 22.8 u | 1 | 0 | 1 | €0,01 | €0,01 (1x) | **€-0,00** | -0.00% | €0,22 | €0,22 | 0.11% |
| bitstamp - kucoin | €200,00 | 2026-11-21 | 22.9 u | 6 | 5 | 1 | €0,03 | €0,23 (1x) | **€-0,21** | -0.10% | €-0,32 | €-0,53 | -0.26% |
| bitstamp - kucoin | €200,00 | 2026-11-22 | 22.1 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,16 | €-0,16 | -0.08% |
| bitstamp - kucoin | €200,00 | 2026-11-23 | 19.7 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,58 | €0,58 | 0.29% |
| bitstamp - kucoin | €200,00 | 2026-11-24 | 6.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,03 | €-0,03 | -0.01% |
| bitstamp - kucoin | €2.000,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €2,19 | €2,19 | 0.11% |
| bitstamp - kucoin | €2.000,00 | 2026-11-20 | 22.8 u | 1 | 0 | 1 | €0,05 | €0,01 (1x) | **€0,04** | 0.00% | €2,19 | €2,24 | 0.11% |
| bitstamp - kucoin | €2.000,00 | 2026-11-21 | 22.9 u | 6 | 5 | 1 | €0,27 | €1,23 (2x) | **€-0,97** | -0.05% | €-3,24 | €-4,20 | -0.21% |
| bitstamp - kucoin | €2.000,00 | 2026-11-22 | 22.1 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,59 | €-1,59 | -0.08% |
| bitstamp - kucoin | €2.000,00 | 2026-11-23 | 19.7 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €5,81 | €5,81 | 0.29% |
| bitstamp - kucoin | €2.000,00 | 2026-11-24 | 6.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,27 | €-0,27 | -0.01% |
| bitstamp - kucoin | €5.000,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €5,49 | €5,49 | 0.11% |
| bitstamp - kucoin | €5.000,00 | 2026-11-20 | 22.8 u | 1 | 0 | 1 | €0,13 | €0,01 (1x) | **€0,12** | 0.00% | €5,48 | €5,60 | 0.11% |
| bitstamp - kucoin | €5.000,00 | 2026-11-21 | 22.9 u | 6 | 5 | 1 | €0,64 | €1,23 (2x) | **€-0,59** | -0.01% | €-8,09 | €-8,68 | -0.17% |
| bitstamp - kucoin | €5.000,00 | 2026-11-22 | 22.1 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,98 | €-3,98 | -0.08% |
| bitstamp - kucoin | €5.000,00 | 2026-11-23 | 19.7 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €14,53 | €14,53 | 0.29% |
| bitstamp - kucoin | €5.000,00 | 2026-11-24 | 6.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,69 | €-0,69 | -0.01% |
| bitvavo - kraken | €100,00 | 2026-11-19 | 14.9 u | 43 | 43 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,87 | €-0,87 | -0.87% |
| bitvavo - kraken | €100,00 | 2026-11-20 | 22.8 u | 15 | 15 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,51 | €-1,51 | -1.51% |
| bitvavo - kraken | €100,00 | 2026-11-21 | 22.9 u | 26 | 26 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,57 | €-0,57 | -0.57% |
| bitvavo - kraken | €100,00 | 2026-11-22 | 22.1 u | 40 | 40 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,04 | €-0,04 | -0.04% |
| bitvavo - kraken | €100,00 | 2026-11-23 | 19.7 u | 28 | 28 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,64 | €0,64 | 0.64% |
| bitvavo - kraken | €100,00 | 2026-11-24 | 6.9 u | 8 | 8 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,42 | €0,42 | 0.42% |
| bitvavo - kraken | €150,00 | 2026-11-19 | 14.9 u | 43 | 43 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,30 | €-1,30 | -0.87% |
| bitvavo - kraken | €150,00 | 2026-11-20 | 22.8 u | 15 | 15 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,27 | €-2,27 | -1.51% |
| bitvavo - kraken | €150,00 | 2026-11-21 | 22.9 u | 26 | 26 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,86 | €-0,86 | -0.57% |
| bitvavo - kraken | €150,00 | 2026-11-22 | 22.1 u | 40 | 40 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,06 | €-0,06 | -0.04% |
| bitvavo - kraken | €150,00 | 2026-11-23 | 19.7 u | 28 | 28 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,96 | €0,96 | 0.64% |
| bitvavo - kraken | €150,00 | 2026-11-24 | 6.9 u | 8 | 8 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,63 | €0,63 | 0.42% |
| bitvavo - kraken | €200,00 | 2026-11-19 | 14.9 u | 43 | 43 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,74 | €-1,74 | -0.87% |
| bitvavo - kraken | €200,00 | 2026-11-20 | 22.8 u | 15 | 15 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,03 | €-3,03 | -1.51% |
| bitvavo - kraken | €200,00 | 2026-11-21 | 22.9 u | 26 | 26 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,14 | €-1,14 | -0.57% |
| bitvavo - kraken | €200,00 | 2026-11-22 | 22.1 u | 40 | 40 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,08 | €-0,08 | -0.04% |
| bitvavo - kraken | €200,00 | 2026-11-23 | 19.7 u | 28 | 28 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €1,28 | €1,28 | 0.64% |
| bitvavo - kraken | €200,00 | 2026-11-24 | 6.9 u | 8 | 8 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,84 | €0,84 | 0.42% |
| bitvavo - kraken | €2.000,00 | 2026-11-19 | 14.9 u | 43 | 25 | 18 | €9,30 | €6,00 (17x) | **€3,31** | 0.17% | €-17,30 | €-14,00 | -0.70% |
| bitvavo - kraken | €2.000,00 | 2026-11-20 | 22.8 u | 15 | 9 | 6 | €17,49 | €2,29 (5x) | **€15,21** | 0.76% | €-30,01 | €-14,80 | -0.74% |
| bitvavo - kraken | €2.000,00 | 2026-11-21 | 22.9 u | 26 | 16 | 10 | €18,54 | €3,25 (8x) | **€15,29** | 0.76% | €-11,56 | €3,73 | 0.19% |
| bitvavo - kraken | €2.000,00 | 2026-11-22 | 22.1 u | 40 | 21 | 19 | €8,20 | €7,11 (20x) | **€1,10** | 0.05% | €-0,81 | €0,29 | 0.01% |
| bitvavo - kraken | €2.000,00 | 2026-11-23 | 19.7 u | 28 | 20 | 8 | €2,06 | €3,55 (9x) | **€-1,49** | -0.07% | €12,74 | €11,25 | 0.56% |
| bitvavo - kraken | €2.000,00 | 2026-11-24 | 6.9 u | 8 | 8 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €8,26 | €8,26 | 0.41% |
| bitvavo - kraken | €5.000,00 | 2026-11-19 | 14.9 u | 43 | 17 | 26 | €26,11 | €16,88 (28x) | **€9,23** | 0.18% | €-43,33 | €-34,10 | -0.68% |
| bitvavo - kraken | €5.000,00 | 2026-11-20 | 22.8 u | 15 | 8 | 7 | €44,31 | €3,46 (6x) | **€40,84** | 0.82% | €-74,61 | €-33,77 | -0.68% |
| bitvavo - kraken | €5.000,00 | 2026-11-21 | 22.9 u | 26 | 14 | 12 | €49,08 | €7,52 (13x) | **€41,57** | 0.83% | €-28,54 | €13,03 | 0.26% |
| bitvavo - kraken | €5.000,00 | 2026-11-22 | 22.1 u | 40 | 20 | 20 | €22,44 | €9,07 (22x) | **€13,36** | 0.27% | €-1,76 | €11,61 | 0.23% |
| bitvavo - kraken | €5.000,00 | 2026-11-23 | 19.7 u | 28 | 14 | 14 | €6,89 | €6,12 (15x) | **€0,77** | 0.02% | €31,56 | €32,32 | 0.65% |
| bitvavo - kraken | €5.000,00 | 2026-11-24 | 6.9 u | 8 | 8 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €20,76 | €20,76 | 0.42% |
| bitvavo - kucoin | €100,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,52 | €-0,52 | -0.52% |
| bitvavo - kucoin | €100,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,80 | €-1,80 | -1.80% |
| bitvavo - kucoin | €100,00 | 2026-11-21 | 22.9 u | 7 | 5 | 2 | €0,04 | €0,00 (0x) | **€0,04** | 0.04% | €0,78 | €0,82 | 0.82% |
| bitvavo - kucoin | €100,00 | 2026-11-22 | 22.1 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,45 | €0,45 | 0.45% |
| bitvavo - kucoin | €100,00 | 2026-11-23 | 19.7 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,05 | €0,05 | 0.05% |
| bitvavo - kucoin | €100,00 | 2026-11-24 | 6.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,08 | €-0,08 | -0.08% |
| bitvavo - kucoin | €150,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,78 | €-0,78 | -0.52% |
| bitvavo - kucoin | €150,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,71 | €-2,71 | -1.80% |
| bitvavo - kucoin | €150,00 | 2026-11-21 | 22.9 u | 7 | 5 | 2 | €0,07 | €0,00 (0x) | **€0,07** | 0.04% | €1,17 | €1,23 | 0.82% |
| bitvavo - kucoin | €150,00 | 2026-11-22 | 22.1 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,68 | €0,68 | 0.45% |
| bitvavo - kucoin | €150,00 | 2026-11-23 | 19.7 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,08 | €0,08 | 0.05% |
| bitvavo - kucoin | €150,00 | 2026-11-24 | 6.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,12 | €-0,12 | -0.08% |
| bitvavo - kucoin | €200,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,04 | €-1,04 | -0.52% |
| bitvavo - kucoin | €200,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,61 | €-3,61 | -1.80% |
| bitvavo - kucoin | €200,00 | 2026-11-21 | 22.9 u | 7 | 5 | 2 | €0,09 | €0,00 (0x) | **€0,09** | 0.04% | €1,56 | €1,65 | 0.82% |
| bitvavo - kucoin | €200,00 | 2026-11-22 | 22.1 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,91 | €0,91 | 0.45% |
| bitvavo - kucoin | €200,00 | 2026-11-23 | 19.7 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,10 | €0,10 | 0.05% |
| bitvavo - kucoin | €200,00 | 2026-11-24 | 6.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,16 | €-0,16 | -0.08% |
| bitvavo - kucoin | €2.000,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-10,39 | €-10,39 | -0.52% |
| bitvavo - kucoin | €2.000,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-36,07 | €-36,07 | -1.80% |
| bitvavo - kucoin | €2.000,00 | 2026-11-21 | 22.9 u | 7 | 4 | 3 | €0,91 | €2,73 (3x) | **€-1,82** | -0.09% | €15,55 | €13,72 | 0.69% |
| bitvavo - kucoin | €2.000,00 | 2026-11-22 | 22.1 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €9,04 | €9,04 | 0.45% |
| bitvavo - kucoin | €2.000,00 | 2026-11-23 | 19.7 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €1,02 | €1,02 | 0.05% |
| bitvavo - kucoin | €2.000,00 | 2026-11-24 | 6.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,55 | €-1,55 | -0.08% |
| bitvavo - kucoin | €5.000,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-25,99 | €-25,99 | -0.52% |
| bitvavo - kucoin | €5.000,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-90,18 | €-90,18 | -1.80% |
| bitvavo - kucoin | €5.000,00 | 2026-11-21 | 22.9 u | 7 | 4 | 3 | €2,24 | €2,73 (3x) | **€-0,49** | -0.01% | €38,94 | €38,45 | 0.77% |
| bitvavo - kucoin | €5.000,00 | 2026-11-22 | 22.1 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €22,63 | €22,63 | 0.45% |
| bitvavo - kucoin | €5.000,00 | 2026-11-23 | 19.7 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €2,55 | €2,55 | 0.05% |
| bitvavo - kucoin | €5.000,00 | 2026-11-24 | 6.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,89 | €-3,89 | -0.08% |
| gate - kucoin | €100,00 | 2026-11-19 | 14.9 u | 25 | 25 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,29 | €-0,29 | -0.29% |
| gate - kucoin | €100,00 | 2026-11-20 | 22.8 u | 46 | 46 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,78 | €-0,78 | -0.78% |
| gate - kucoin | €100,00 | 2026-11-21 | 22.9 u | 46 | 46 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,74 | €-1,74 | -1.74% |
| gate - kucoin | €100,00 | 2026-11-22 | 22.1 u | 28 | 28 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,94 | €-1,94 | -1.94% |
| gate - kucoin | €100,00 | 2026-11-23 | 19.7 u | 32 | 32 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,34 | €-0,34 | -0.34% |
| gate - kucoin | €100,00 | 2026-11-24 | 6.9 u | 7 | 7 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,26 | €0,26 | 0.26% |
| gate - kucoin | €150,00 | 2026-11-19 | 14.9 u | 25 | 25 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,44 | €-0,44 | -0.29% |
| gate - kucoin | €150,00 | 2026-11-20 | 22.8 u | 46 | 46 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,18 | €-1,18 | -0.78% |
| gate - kucoin | €150,00 | 2026-11-21 | 22.9 u | 46 | 46 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,61 | €-2,61 | -1.74% |
| gate - kucoin | €150,00 | 2026-11-22 | 22.1 u | 28 | 28 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,90 | €-2,90 | -1.94% |
| gate - kucoin | €150,00 | 2026-11-23 | 19.7 u | 32 | 32 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,50 | €-0,50 | -0.34% |
| gate - kucoin | €150,00 | 2026-11-24 | 6.9 u | 7 | 7 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,39 | €0,39 | 0.26% |
| gate - kucoin | €200,00 | 2026-11-19 | 14.9 u | 25 | 25 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,58 | €-0,58 | -0.29% |
| gate - kucoin | €200,00 | 2026-11-20 | 22.8 u | 46 | 45 | 1 | €0,12 | €0,00 (0x) | **€0,12** | 0.06% | €-1,57 | €-1,45 | -0.73% |
| gate - kucoin | €200,00 | 2026-11-21 | 22.9 u | 46 | 46 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,48 | €-3,48 | -1.74% |
| gate - kucoin | €200,00 | 2026-11-22 | 22.1 u | 28 | 28 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,87 | €-3,87 | -1.94% |
| gate - kucoin | €200,00 | 2026-11-23 | 19.7 u | 32 | 32 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,67 | €-0,67 | -0.34% |
| gate - kucoin | €200,00 | 2026-11-24 | 6.9 u | 7 | 7 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,51 | €0,51 | 0.26% |
| gate - kucoin | €2.000,00 | 2026-11-19 | 14.9 u | 25 | 17 | 8 | €0,83 | €0,00 (0x) | **€0,83** | 0.04% | €-5,84 | €-5,01 | -0.25% |
| gate - kucoin | €2.000,00 | 2026-11-20 | 22.8 u | 46 | 25 | 21 | €5,70 | €0,05 (3x) | **€5,65** | 0.28% | €-15,70 | €-10,05 | -0.50% |
| gate - kucoin | €2.000,00 | 2026-11-21 | 22.9 u | 46 | 34 | 12 | €3,04 | €0,01 (1x) | **€3,03** | 0.15% | €-34,78 | €-31,75 | -1.59% |
| gate - kucoin | €2.000,00 | 2026-11-22 | 22.1 u | 28 | 21 | 7 | €0,66 | €0,01 (2x) | **€0,64** | 0.03% | €-38,73 | €-38,09 | -1.90% |
| gate - kucoin | €2.000,00 | 2026-11-23 | 19.7 u | 32 | 26 | 6 | €0,91 | €0,10 (1x) | **€0,81** | 0.04% | €-6,71 | €-5,90 | -0.30% |
| gate - kucoin | €2.000,00 | 2026-11-24 | 6.9 u | 7 | 6 | 1 | €0,41 | €0,00 (0x) | **€0,41** | 0.02% | €5,14 | €5,55 | 0.28% |
| gate - kucoin | €5.000,00 | 2026-11-19 | 14.9 u | 25 | 10 | 15 | €2,82 | €2,10 (12x) | **€0,72** | 0.01% | €-14,59 | €-13,88 | -0.28% |
| gate - kucoin | €5.000,00 | 2026-11-20 | 22.8 u | 46 | 15 | 31 | €15,11 | €2,80 (19x) | **€12,31** | 0.25% | €-39,21 | €-26,90 | -0.54% |
| gate - kucoin | €5.000,00 | 2026-11-21 | 22.9 u | 46 | 15 | 31 | €10,46 | €3,48 (22x) | **€6,98** | 0.14% | €-86,96 | €-79,98 | -1.60% |
| gate - kucoin | €5.000,00 | 2026-11-22 | 22.1 u | 28 | 6 | 22 | €3,68 | €2,35 (17x) | **€1,33** | 0.03% | €-96,72 | €-95,39 | -1.91% |
| gate - kucoin | €5.000,00 | 2026-11-23 | 19.7 u | 32 | 14 | 18 | €4,11 | €2,10 (15x) | **€2,01** | 0.04% | €-17,01 | €-15,00 | -0.30% |
| gate - kucoin | €5.000,00 | 2026-11-24 | 6.9 u | 7 | 4 | 3 | €1,43 | €0,32 (2x) | **€1,12** | 0.02% | €12,61 | €13,73 | 0.27% |
| kraken - kucoin | €100,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,11 | €0,11 | 0.11% |
| kraken - kucoin | €100,00 | 2026-11-20 | 22.8 u | 15 | 13 | 2 | €0,03 | €0,01 (1x) | **€0,02** | 0.02% | €0,11 | €0,13 | 0.13% |
| kraken - kucoin | €100,00 | 2026-11-21 | 22.9 u | 12 | 12 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,16 | €-0,16 | -0.16% |
| kraken - kucoin | €100,00 | 2026-11-22 | 22.1 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,08 | €-0,08 | -0.08% |
| kraken - kucoin | €100,00 | 2026-11-23 | 19.7 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,29 | €0,29 | 0.29% |
| kraken - kucoin | €100,00 | 2026-11-24 | 6.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,01 | €-0,01 | -0.01% |
| kraken - kucoin | €150,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,16 | €0,16 | 0.11% |
| kraken - kucoin | €150,00 | 2026-11-20 | 22.8 u | 15 | 13 | 2 | €0,05 | €0,01 (1x) | **€0,04** | 0.02% | €0,16 | €0,20 | 0.13% |
| kraken - kucoin | €150,00 | 2026-11-21 | 22.9 u | 12 | 12 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,24 | €-0,24 | -0.16% |
| kraken - kucoin | €150,00 | 2026-11-22 | 22.1 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,12 | €-0,12 | -0.08% |
| kraken - kucoin | €150,00 | 2026-11-23 | 19.7 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,44 | €0,44 | 0.29% |
| kraken - kucoin | €150,00 | 2026-11-24 | 6.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,02 | €-0,02 | -0.01% |
| kraken - kucoin | €200,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,22 | €0,22 | 0.11% |
| kraken - kucoin | €200,00 | 2026-11-20 | 22.8 u | 15 | 13 | 2 | €0,06 | €0,24 (2x) | **€-0,18** | -0.09% | €0,22 | €0,04 | 0.02% |
| kraken - kucoin | €200,00 | 2026-11-21 | 22.9 u | 12 | 12 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,32 | €-0,32 | -0.16% |
| kraken - kucoin | €200,00 | 2026-11-22 | 22.1 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,16 | €-0,16 | -0.08% |
| kraken - kucoin | €200,00 | 2026-11-23 | 19.7 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,58 | €0,58 | 0.29% |
| kraken - kucoin | €200,00 | 2026-11-24 | 6.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,03 | €-0,03 | -0.01% |
| kraken - kucoin | €2.000,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €2,19 | €2,19 | 0.11% |
| kraken - kucoin | €2.000,00 | 2026-11-20 | 22.8 u | 15 | 13 | 2 | €0,61 | €1,24 (3x) | **€-0,63** | -0.03% | €2,19 | €1,56 | 0.08% |
| kraken - kucoin | €2.000,00 | 2026-11-21 | 22.9 u | 12 | 12 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,24 | €-3,24 | -0.16% |
| kraken - kucoin | €2.000,00 | 2026-11-22 | 22.1 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,59 | €-1,59 | -0.08% |
| kraken - kucoin | €2.000,00 | 2026-11-23 | 19.7 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €5,81 | €5,81 | 0.29% |
| kraken - kucoin | €2.000,00 | 2026-11-24 | 6.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,27 | €-0,27 | -0.01% |
| kraken - kucoin | €5.000,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €5,49 | €5,49 | 0.11% |
| kraken - kucoin | €5.000,00 | 2026-11-20 | 22.8 u | 15 | 13 | 2 | €1,53 | €1,24 (3x) | **€0,28** | 0.01% | €5,48 | €5,77 | 0.12% |
| kraken - kucoin | €5.000,00 | 2026-11-21 | 22.9 u | 12 | 12 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-8,09 | €-8,09 | -0.16% |
| kraken - kucoin | €5.000,00 | 2026-11-22 | 22.1 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,98 | €-3,98 | -0.08% |
| kraken - kucoin | €5.000,00 | 2026-11-23 | 19.7 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €14,53 | €14,53 | 0.29% |
| kraken - kucoin | €5.000,00 | 2026-11-24 | 6.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,69 | €-0,69 | -0.01% |

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
- bitvavo - kraken, €100,00: munten AERO, AVA, CVX, CYBER, DYM, GMT, KERNEL, LUNA, MERL, MLN, PROMPT, VELO; bruto zonder voorraadgrens zou €5.495,19 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitvavo - kraken, €150,00: munten AERO, AVA, CVX, CYBER, DYM, GMT, KERNEL, LUNA, MERL, MLN, PROMPT, VELO; bruto zonder voorraadgrens zou €5.495,19 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitvavo - kraken, €200,00: munten AERO, AVA, CVX, CYBER, DYM, GMT, KERNEL, LUNA, MERL, MLN, PROMPT, VELO; bruto zonder voorraadgrens zou €5.495,19 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitvavo - kraken, €2.000,00: munten AERO, AVA, CVX, CYBER, DYM, GMT, KERNEL, LUNA, MERL, MLN, PROMPT, VELO; bruto zonder voorraadgrens zou €5.448,54 zijn, met voorraad €55,60 (GEZIEN boek, GOK model).
- bitvavo - kraken, €5.000,00: munten AERO, AVA, CVX, CYBER, DYM, GMT, KERNEL, LUNA, MERL, MLN, PROMPT, VELO; bruto zonder voorraadgrens zou €5.381,73 zijn, met voorraad €148,83 (GEZIEN boek, GOK model).
- bitvavo - kucoin, €100,00: munten ETH, USDC; bruto zonder voorraadgrens zou €19,28 zijn, met voorraad €0,04 (GEZIEN boek, GOK model).
- bitvavo - kucoin, €150,00: munten ETH, USDC; bruto zonder voorraadgrens zou €19,28 zijn, met voorraad €0,07 (GEZIEN boek, GOK model).
- bitvavo - kucoin, €200,00: munten ETH, USDC; bruto zonder voorraadgrens zou €19,28 zijn, met voorraad €0,09 (GEZIEN boek, GOK model).
- bitvavo - kucoin, €2.000,00: munten ETH, USDC; bruto zonder voorraadgrens zou €19,28 zijn, met voorraad €0,91 (GEZIEN boek, GOK model).
- bitvavo - kucoin, €5.000,00: munten ETH, USDC; bruto zonder voorraadgrens zou €19,28 zijn, met voorraad €2,24 (GEZIEN boek, GOK model).
- gate - kucoin, €100,00: munten ALKIMI, AVAIL, BARD, CAMP, CCD, CHR, CWEB, CYBER, DCR, DMTR, EDEN, ENSO, EPIC, ERG, ESPORTS, EVAA, FTT, HIGH, HTR, IKA, IR, JST, KAVA, KYO, LSK, LUNC, NAKA, NES, NIM, ON, OVR, POKT, POND, RARI, SD, SOUL, STREAM, SUPRA, USDS, USTC, VERONA, XU3O8; bruto zonder voorraadgrens zou €616,70 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- gate - kucoin, €150,00: munten ALKIMI, AVAIL, BARD, CAMP, CCD, CHR, CWEB, CYBER, DCR, DMTR, EDEN, ENSO, EPIC, ERG, ESPORTS, EVAA, FTT, HIGH, HTR, IKA, IR, JST, KAVA, KYO, LSK, LUNC, NAKA, NES, NIM, ON, OVR, POKT, POND, RARI, SD, SOUL, STREAM, SUPRA, USDS, USTC, VERONA, XU3O8; bruto zonder voorraadgrens zou €616,70 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- gate - kucoin, €200,00: munten ALKIMI, AVAIL, BARD, CAMP, CCD, CHR, CWEB, CYBER, DCR, DMTR, EDEN, ENSO, EPIC, ERG, ESPORTS, EVAA, FTT, HIGH, HTR, IKA, IR, JST, KAVA, KYO, LSK, LUNC, NAKA, NES, NIM, ON, OVR, POKT, POND, RARI, SD, SOUL, STREAM, SUPRA, USDS, USTC, VERONA, XU3O8; bruto zonder voorraadgrens zou €616,70 zijn, met voorraad €0,12 (GEZIEN boek, GOK model).
- gate - kucoin, €2.000,00: munten ALKIMI, AVAIL, BARD, CAMP, CCD, CHR, CWEB, CYBER, DCR, DMTR, EDEN, ENSO, EPIC, ERG, ESPORTS, EVAA, FTT, HIGH, HTR, IKA, IR, JST, KAVA, KYO, LSK, LUNC, NAKA, NES, NIM, ON, OVR, POKT, POND, RARI, SD, SOUL, STREAM, SUPRA, USDS, USTC, VERONA, XU3O8; bruto zonder voorraadgrens zou €615,69 zijn, met voorraad €11,55 (GEZIEN boek, GOK model).
- gate - kucoin, €5.000,00: munten ALKIMI, AVAIL, BARD, CAMP, CCD, CHR, CWEB, CYBER, DCR, DMTR, EDEN, ENSO, EPIC, ERG, ESPORTS, EVAA, FTT, HIGH, HTR, IKA, IR, JST, KAVA, KYO, LSK, LUNC, NAKA, NES, NIM, ON, OVR, POKT, POND, RARI, SD, SOUL, STREAM, SUPRA, USDS, USTC, VERONA, XU3O8; bruto zonder voorraadgrens zou €613,91 zijn, met voorraad €37,61 (GEZIEN boek, GOK model).
- kraken - kucoin, €100,00: munten USDC, USDT; bruto zonder voorraadgrens zou €120,83 zijn, met voorraad €0,03 (GEZIEN boek, GOK model).
- kraken - kucoin, €150,00: munten USDC, USDT; bruto zonder voorraadgrens zou €120,83 zijn, met voorraad €0,05 (GEZIEN boek, GOK model).
- kraken - kucoin, €200,00: munten USDC, USDT; bruto zonder voorraadgrens zou €120,82 zijn, met voorraad €0,06 (GEZIEN boek, GOK model).
- kraken - kucoin, €2.000,00: munten USDC, USDT; bruto zonder voorraadgrens zou €120,54 zijn, met voorraad €0,61 (GEZIEN boek, GOK model).
- kraken - kucoin, €5.000,00: munten USDC, USDT; bruto zonder voorraadgrens zou €120,08 zijn, met voorraad €1,53 (GEZIEN boek, GOK model).

### Met minstens één grijze beurs (de 5 paren met de meeste bruto winst)

| Beurspaar | Inleg | Dag | Gemeten | Kansen | Gemist (geen voorraad) | Kleiner door voorraad | Bruto winst | Kosten terugschuiven | **Netto handel (bruto min kosten)** | Rendement handel | Koerseffect voorraad | Netto met koerseffect | Rendement met koerseffect |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| htx - kucoin | €100,00 | 2026-11-19 | 14.9 u | 16 | 16 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,01 | €-1,01 | -1.01% |
| htx - kucoin | €100,00 | 2026-11-20 | 22.8 u | 42 | 42 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,93 | €-2,93 | -2.93% |
| htx - kucoin | €100,00 | 2026-11-21 | 22.9 u | 32 | 32 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,11 | €0,11 | 0.11% |
| htx - kucoin | €100,00 | 2026-11-22 | 22.1 u | 40 | 40 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,27 | €-0,27 | -0.27% |
| htx - kucoin | €100,00 | 2026-11-23 | 19.7 u | 15 | 15 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,65 | €0,65 | 0.65% |
| htx - kucoin | €100,00 | 2026-11-24 | 6.9 u | 10 | 10 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,47 | €0,47 | 0.47% |
| htx - kucoin | €150,00 | 2026-11-19 | 14.9 u | 16 | 16 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,51 | €-1,51 | -1.01% |
| htx - kucoin | €150,00 | 2026-11-20 | 22.8 u | 42 | 42 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-4,39 | €-4,39 | -2.93% |
| htx - kucoin | €150,00 | 2026-11-21 | 22.9 u | 32 | 32 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,17 | €0,17 | 0.11% |
| htx - kucoin | €150,00 | 2026-11-22 | 22.1 u | 40 | 40 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,40 | €-0,40 | -0.27% |
| htx - kucoin | €150,00 | 2026-11-23 | 19.7 u | 15 | 15 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,97 | €0,97 | 0.65% |
| htx - kucoin | €150,00 | 2026-11-24 | 6.9 u | 10 | 10 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,71 | €0,71 | 0.47% |
| htx - kucoin | €200,00 | 2026-11-19 | 14.9 u | 16 | 16 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,02 | €-2,02 | -1.01% |
| htx - kucoin | €200,00 | 2026-11-20 | 22.8 u | 42 | 42 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-5,85 | €-5,85 | -2.93% |
| htx - kucoin | €200,00 | 2026-11-21 | 22.9 u | 32 | 32 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,22 | €0,22 | 0.11% |
| htx - kucoin | €200,00 | 2026-11-22 | 22.1 u | 40 | 40 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,54 | €-0,54 | -0.27% |
| htx - kucoin | €200,00 | 2026-11-23 | 19.7 u | 15 | 15 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €1,29 | €1,29 | 0.65% |
| htx - kucoin | €200,00 | 2026-11-24 | 6.9 u | 10 | 10 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,94 | €0,94 | 0.47% |
| htx - kucoin | €2.000,00 | 2026-11-19 | 14.9 u | 16 | 16 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-20,18 | €-20,18 | -1.01% |
| htx - kucoin | €2.000,00 | 2026-11-20 | 22.8 u | 42 | 42 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-58,54 | €-58,54 | -2.93% |
| htx - kucoin | €2.000,00 | 2026-11-21 | 22.9 u | 32 | 32 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €2,21 | €2,21 | 0.11% |
| htx - kucoin | €2.000,00 | 2026-11-22 | 22.1 u | 40 | 39 | 1 | €0,17 | €0,00 (0x) | **€0,17** | 0.01% | €-5,36 | €-5,19 | -0.26% |
| htx - kucoin | €2.000,00 | 2026-11-23 | 19.7 u | 15 | 13 | 2 | €2,49 | €0,10 (1x) | **€2,39** | 0.12% | €12,97 | €15,36 | 0.77% |
| htx - kucoin | €2.000,00 | 2026-11-24 | 6.9 u | 10 | 10 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €9,45 | €9,45 | 0.47% |
| htx - kucoin | €5.000,00 | 2026-11-19 | 14.9 u | 16 | 9 | 7 | €1,36 | €0,00 (1x) | **€1,36** | 0.03% | €-50,45 | €-49,09 | -0.98% |
| htx - kucoin | €5.000,00 | 2026-11-20 | 22.8 u | 42 | 24 | 18 | €7,85 | €0,00 (1x) | **€7,84** | 0.16% | €-146,34 | €-138,50 | -2.77% |
| htx - kucoin | €5.000,00 | 2026-11-21 | 22.9 u | 32 | 13 | 19 | €2,66 | €0,27 (5x) | **€2,38** | 0.05% | €5,51 | €7,89 | 0.16% |
| htx - kucoin | €5.000,00 | 2026-11-22 | 22.1 u | 40 | 26 | 14 | €7,44 | €0,33 (4x) | **€7,11** | 0.14% | €-13,40 | €-6,29 | -0.13% |
| htx - kucoin | €5.000,00 | 2026-11-23 | 19.7 u | 15 | 8 | 7 | €2,06 | €0,10 (1x) | **€1,96** | 0.04% | €32,36 | €34,33 | 0.69% |
| htx - kucoin | €5.000,00 | 2026-11-24 | 6.9 u | 10 | 9 | 1 | €0,25 | €0,00 (0x) | **€0,25** | 0.00% | €23,61 | €23,86 | 0.48% |
| bitget - htx | €100,00 | 2026-11-19 | 14.9 u | 20 | 20 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €100,00 | 2026-11-20 | 22.8 u | 39 | 39 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €100,00 | 2026-11-21 | 22.9 u | 47 | 47 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €100,00 | 2026-11-22 | 22.1 u | 39 | 39 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €100,00 | 2026-11-23 | 19.7 u | 27 | 27 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €100,00 | 2026-11-24 | 6.9 u | 13 | 13 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €150,00 | 2026-11-19 | 14.9 u | 20 | 20 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €150,00 | 2026-11-20 | 22.8 u | 39 | 39 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €150,00 | 2026-11-21 | 22.9 u | 47 | 47 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €150,00 | 2026-11-22 | 22.1 u | 39 | 39 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €150,00 | 2026-11-23 | 19.7 u | 27 | 27 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €150,00 | 2026-11-24 | 6.9 u | 13 | 13 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €200,00 | 2026-11-19 | 14.9 u | 20 | 20 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €200,00 | 2026-11-20 | 22.8 u | 39 | 39 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €200,00 | 2026-11-21 | 22.9 u | 47 | 47 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €200,00 | 2026-11-22 | 22.1 u | 39 | 39 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €200,00 | 2026-11-23 | 19.7 u | 27 | 27 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €200,00 | 2026-11-24 | 6.9 u | 13 | 13 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €2.000,00 | 2026-11-19 | 14.9 u | 20 | 20 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €2.000,00 | 2026-11-20 | 22.8 u | 39 | 39 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €2.000,00 | 2026-11-21 | 22.9 u | 47 | 47 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €2.000,00 | 2026-11-22 | 22.1 u | 39 | 38 | 1 | €0,18 | €0,00 (0x) | **€0,18** | 0.01% | onbekend | onbekend* | onbekend* |
| bitget - htx | €2.000,00 | 2026-11-23 | 19.7 u | 27 | 26 | 1 | €1,33 | €0,00 (0x) | **€1,33** | 0.07% | onbekend | onbekend* | onbekend* |
| bitget - htx | €2.000,00 | 2026-11-24 | 6.9 u | 13 | 13 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €5.000,00 | 2026-11-19 | 14.9 u | 20 | 6 | 14 | €1,35 | €0,70 (10x) | **€0,65** | 0.01% | onbekend | onbekend* | onbekend* |
| bitget - htx | €5.000,00 | 2026-11-20 | 22.8 u | 39 | 8 | 31 | €7,35 | €0,64 (26x) | **€6,71** | 0.13% | onbekend | onbekend* | onbekend* |
| bitget - htx | €5.000,00 | 2026-11-21 | 22.9 u | 47 | 8 | 39 | €4,14 | €1,59 (31x) | **€2,54** | 0.05% | onbekend | onbekend* | onbekend* |
| bitget - htx | €5.000,00 | 2026-11-22 | 22.1 u | 39 | 17 | 22 | €4,92 | €0,87 (17x) | **€4,05** | 0.08% | onbekend | onbekend* | onbekend* |
| bitget - htx | €5.000,00 | 2026-11-23 | 19.7 u | 27 | 9 | 18 | €2,31 | €0,84 (15x) | **€1,46** | 0.03% | onbekend | onbekend* | onbekend* |
| bitget - htx | €5.000,00 | 2026-11-24 | 6.9 u | 13 | 7 | 6 | €0,82 | €0,25 (5x) | **€0,58** | 0.01% | onbekend | onbekend* | onbekend* |
| gate - htx | €100,00 | 2026-11-19 | 14.9 u | 19 | 19 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,81 | €-0,81 | -0.81% |
| gate - htx | €100,00 | 2026-11-20 | 22.8 u | 32 | 32 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,61 | €-2,61 | -2.61% |
| gate - htx | €100,00 | 2026-11-21 | 22.9 u | 36 | 36 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,06 | €0,06 | 0.06% |
| gate - htx | €100,00 | 2026-11-22 | 22.1 u | 35 | 35 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,77 | €-0,77 | -0.77% |
| gate - htx | €100,00 | 2026-11-23 | 19.7 u | 25 | 25 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,51 | €0,51 | 0.51% |
| gate - htx | €100,00 | 2026-11-24 | 6.9 u | 2 | 2 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,70 | €0,70 | 0.70% |
| gate - htx | €150,00 | 2026-11-19 | 14.9 u | 19 | 19 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,21 | €-1,21 | -0.81% |
| gate - htx | €150,00 | 2026-11-20 | 22.8 u | 32 | 32 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,91 | €-3,91 | -2.61% |
| gate - htx | €150,00 | 2026-11-21 | 22.9 u | 36 | 36 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,09 | €0,09 | 0.06% |
| gate - htx | €150,00 | 2026-11-22 | 22.1 u | 35 | 35 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,15 | €-1,15 | -0.77% |
| gate - htx | €150,00 | 2026-11-23 | 19.7 u | 25 | 25 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,77 | €0,77 | 0.51% |
| gate - htx | €150,00 | 2026-11-24 | 6.9 u | 2 | 2 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €1,05 | €1,05 | 0.70% |
| gate - htx | €200,00 | 2026-11-19 | 14.9 u | 19 | 19 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,62 | €-1,62 | -0.81% |
| gate - htx | €200,00 | 2026-11-20 | 22.8 u | 32 | 32 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-5,21 | €-5,21 | -2.61% |
| gate - htx | €200,00 | 2026-11-21 | 22.9 u | 36 | 36 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,12 | €0,12 | 0.06% |
| gate - htx | €200,00 | 2026-11-22 | 22.1 u | 35 | 35 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,54 | €-1,54 | -0.77% |
| gate - htx | €200,00 | 2026-11-23 | 19.7 u | 25 | 25 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €1,03 | €1,03 | 0.51% |
| gate - htx | €200,00 | 2026-11-24 | 6.9 u | 2 | 2 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €1,41 | €1,41 | 0.70% |
| gate - htx | €2.000,00 | 2026-11-19 | 14.9 u | 19 | 19 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-16,18 | €-16,18 | -0.81% |
| gate - htx | €2.000,00 | 2026-11-20 | 22.8 u | 32 | 32 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-52,15 | €-52,15 | -2.61% |
| gate - htx | €2.000,00 | 2026-11-21 | 22.9 u | 36 | 36 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €1,23 | €1,23 | 0.06% |
| gate - htx | €2.000,00 | 2026-11-22 | 22.1 u | 35 | 34 | 1 | €0,18 | €0,00 (0x) | **€0,18** | 0.01% | €-15,39 | €-15,21 | -0.76% |
| gate - htx | €2.000,00 | 2026-11-23 | 19.7 u | 25 | 25 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €10,25 | €10,25 | 0.51% |
| gate - htx | €2.000,00 | 2026-11-24 | 6.9 u | 2 | 2 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €14,07 | €14,07 | 0.70% |
| gate - htx | €5.000,00 | 2026-11-19 | 14.9 u | 19 | 14 | 5 | €0,96 | €0,17 (1x) | **€0,79** | 0.02% | €-40,45 | €-39,66 | -0.79% |
| gate - htx | €5.000,00 | 2026-11-20 | 22.8 u | 32 | 12 | 20 | €7,11 | €0,66 (8x) | **€6,45** | 0.13% | €-130,36 | €-123,90 | -2.48% |
| gate - htx | €5.000,00 | 2026-11-21 | 22.9 u | 36 | 13 | 23 | €4,85 | €1,00 (14x) | **€3,84** | 0.08% | €3,08 | €6,92 | 0.14% |
| gate - htx | €5.000,00 | 2026-11-22 | 22.1 u | 35 | 10 | 25 | €6,75 | €2,52 (22x) | **€4,23** | 0.08% | €-38,48 | €-34,25 | -0.68% |
| gate - htx | €5.000,00 | 2026-11-23 | 19.7 u | 25 | 16 | 9 | €3,27 | €0,40 (5x) | **€2,87** | 0.06% | €25,51 | €28,38 | 0.57% |
| gate - htx | €5.000,00 | 2026-11-24 | 6.9 u | 2 | 0 | 2 | €1,23 | €0,00 (1x) | **€1,23** | 0.02% | €35,17 | €36,39 | 0.73% |
| htx - xt | €100,00 | 2026-11-19 | 14.9 u | 18 | 18 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,05 | €-1,05 | -1.05% |
| htx - xt | €100,00 | 2026-11-20 | 22.8 u | 17 | 17 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,70 | €-2,70 | -2.70% |
| htx - xt | €100,00 | 2026-11-21 | 22.9 u | 15 | 15 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,15 | €-0,15 | -0.15% |
| htx - xt | €100,00 | 2026-11-22 | 22.1 u | 15 | 15 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,56 | €-0,56 | -0.56% |
| htx - xt | €100,00 | 2026-11-23 | 19.7 u | 9 | 9 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,81 | €0,81 | 0.81% |
| htx - xt | €100,00 | 2026-11-24 | 6.9 u | 1 | 1 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €1,45 | €1,45 | 1.45% |
| htx - xt | €150,00 | 2026-11-19 | 14.9 u | 18 | 18 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,57 | €-1,57 | -1.05% |
| htx - xt | €150,00 | 2026-11-20 | 22.8 u | 17 | 17 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-4,05 | €-4,05 | -2.70% |
| htx - xt | €150,00 | 2026-11-21 | 22.9 u | 15 | 15 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,22 | €-0,22 | -0.15% |
| htx - xt | €150,00 | 2026-11-22 | 22.1 u | 15 | 15 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,83 | €-0,83 | -0.56% |
| htx - xt | €150,00 | 2026-11-23 | 19.7 u | 9 | 9 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €1,21 | €1,21 | 0.81% |
| htx - xt | €150,00 | 2026-11-24 | 6.9 u | 1 | 1 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €2,17 | €2,17 | 1.45% |
| htx - xt | €200,00 | 2026-11-19 | 14.9 u | 18 | 18 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,10 | €-2,10 | -1.05% |
| htx - xt | €200,00 | 2026-11-20 | 22.8 u | 17 | 17 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-5,40 | €-5,40 | -2.70% |
| htx - xt | €200,00 | 2026-11-21 | 22.9 u | 15 | 15 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,29 | €-0,29 | -0.15% |
| htx - xt | €200,00 | 2026-11-22 | 22.1 u | 15 | 15 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,11 | €-1,11 | -0.56% |
| htx - xt | €200,00 | 2026-11-23 | 19.7 u | 9 | 9 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €1,61 | €1,61 | 0.81% |
| htx - xt | €200,00 | 2026-11-24 | 6.9 u | 1 | 1 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €2,90 | €2,90 | 1.45% |
| htx - xt | €2.000,00 | 2026-11-19 | 14.9 u | 18 | 14 | 4 | €0,62 | €0,00 (0x) | **€0,62** | 0.03% | €-20,97 | €-20,35 | -1.02% |
| htx - xt | €2.000,00 | 2026-11-20 | 22.8 u | 17 | 9 | 8 | €3,71 | €0,12 (2x) | **€3,59** | 0.18% | €-53,94 | €-50,36 | -2.52% |
| htx - xt | €2.000,00 | 2026-11-21 | 22.9 u | 15 | 7 | 8 | €2,91 | €0,01 (1x) | **€2,90** | 0.14% | €-2,90 | €0,00 | 0.00% |
| htx - xt | €2.000,00 | 2026-11-22 | 22.1 u | 15 | 10 | 5 | €1,47 | €0,11 (1x) | **€1,36** | 0.07% | €-11,12 | €-9,76 | -0.49% |
| htx - xt | €2.000,00 | 2026-11-23 | 19.7 u | 9 | 6 | 3 | €0,51 | €0,00 (0x) | **€0,51** | 0.03% | €16,14 | €16,64 | 0.83% |
| htx - xt | €2.000,00 | 2026-11-24 | 6.9 u | 1 | 0 | 1 | €0,19 | €0,00 (0x) | **€0,19** | 0.01% | €28,98 | €29,17 | 1.46% |
| htx - xt | €5.000,00 | 2026-11-19 | 14.9 u | 18 | 5 | 13 | €5,99 | €4,29 (11x) | **€1,69** | 0.03% | €-52,48 | €-50,78 | -1.02% |
| htx - xt | €5.000,00 | 2026-11-20 | 22.8 u | 17 | 2 | 15 | €13,28 | €2,81 (9x) | **€10,48** | 0.21% | €-134,57 | €-124,10 | -2.48% |
| htx - xt | €5.000,00 | 2026-11-21 | 22.9 u | 15 | 6 | 9 | €7,75 | €0,01 (1x) | **€7,74** | 0.15% | €-6,59 | €1,15 | 0.02% |
| htx - xt | €5.000,00 | 2026-11-22 | 22.1 u | 15 | 10 | 5 | €3,67 | €0,11 (1x) | **€3,56** | 0.07% | €-27,71 | €-24,15 | -0.48% |
| htx - xt | €5.000,00 | 2026-11-23 | 19.7 u | 9 | 6 | 3 | €1,27 | €0,27 (1x) | **€1,00** | 0.02% | €39,88 | €40,88 | 0.82% |
| htx - xt | €5.000,00 | 2026-11-24 | 6.9 u | 1 | 0 | 1 | €0,47 | €0,00 (0x) | **€0,47** | 0.01% | €72,09 | €72,56 | 1.45% |
| bitget - kucoin | €100,00 | 2026-11-19 | 14.9 u | 21 | 21 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,35 | €-0,35 | -0.35% |
| bitget - kucoin | €100,00 | 2026-11-20 | 22.8 u | 24 | 24 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,54 | €-1,54 | -1.54% |
| bitget - kucoin | €100,00 | 2026-11-21 | 22.9 u | 39 | 39 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,27 | €-0,27 | -0.27% |
| bitget - kucoin | €100,00 | 2026-11-22 | 22.1 u | 49 | 49 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,82 | €-1,82 | -1.82% |
| bitget - kucoin | €100,00 | 2026-11-23 | 19.7 u | 46 | 46 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,61 | €-0,61 | -0.61% |
| bitget - kucoin | €100,00 | 2026-11-24 | 6.9 u | 20 | 20 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €1,12 | €1,12 | 1.12% |
| bitget - kucoin | €150,00 | 2026-11-19 | 14.9 u | 21 | 21 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,52 | €-0,52 | -0.35% |
| bitget - kucoin | €150,00 | 2026-11-20 | 22.8 u | 24 | 24 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,31 | €-2,31 | -1.54% |
| bitget - kucoin | €150,00 | 2026-11-21 | 22.9 u | 39 | 39 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,40 | €-0,40 | -0.27% |
| bitget - kucoin | €150,00 | 2026-11-22 | 22.1 u | 49 | 49 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,73 | €-2,73 | -1.82% |
| bitget - kucoin | €150,00 | 2026-11-23 | 19.7 u | 46 | 46 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,91 | €-0,91 | -0.61% |
| bitget - kucoin | €150,00 | 2026-11-24 | 6.9 u | 20 | 20 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €1,67 | €1,67 | 1.12% |
| bitget - kucoin | €200,00 | 2026-11-19 | 14.9 u | 21 | 21 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,70 | €-0,70 | -0.35% |
| bitget - kucoin | €200,00 | 2026-11-20 | 22.8 u | 24 | 24 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,08 | €-3,08 | -1.54% |
| bitget - kucoin | €200,00 | 2026-11-21 | 22.9 u | 39 | 39 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,54 | €-0,54 | -0.27% |
| bitget - kucoin | €200,00 | 2026-11-22 | 22.1 u | 49 | 49 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,64 | €-3,64 | -1.82% |
| bitget - kucoin | €200,00 | 2026-11-23 | 19.7 u | 46 | 46 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,22 | €-1,22 | -0.61% |
| bitget - kucoin | €200,00 | 2026-11-24 | 6.9 u | 20 | 20 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €2,23 | €2,23 | 1.12% |
| bitget - kucoin | €2.000,00 | 2026-11-19 | 14.9 u | 21 | 14 | 7 | €0,67 | €0,29 (2x) | **€0,39** | 0.02% | €-6,96 | €-6,58 | -0.33% |
| bitget - kucoin | €2.000,00 | 2026-11-20 | 22.8 u | 24 | 14 | 10 | €1,86 | €0,00 (2x) | **€1,86** | 0.09% | €-30,77 | €-28,91 | -1.45% |
| bitget - kucoin | €2.000,00 | 2026-11-21 | 22.9 u | 39 | 23 | 16 | €0,61 | €0,58 (10x) | **€0,03** | 0.00% | €-5,36 | €-5,34 | -0.27% |
| bitget - kucoin | €2.000,00 | 2026-11-22 | 22.1 u | 49 | 39 | 10 | €0,56 | €1,46 (8x) | **€-0,90** | -0.04% | €-36,45 | €-37,35 | -1.87% |
| bitget - kucoin | €2.000,00 | 2026-11-23 | 19.7 u | 46 | 46 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-12,14 | €-12,14 | -0.61% |
| bitget - kucoin | €2.000,00 | 2026-11-24 | 6.9 u | 20 | 18 | 2 | €0,19 | €0,00 (1x) | **€0,19** | 0.01% | €22,33 | €22,53 | 1.13% |
| bitget - kucoin | €5.000,00 | 2026-11-19 | 14.9 u | 21 | 8 | 13 | €3,57 | €2,26 (12x) | **€1,31** | 0.03% | €-17,42 | €-16,11 | -0.32% |
| bitget - kucoin | €5.000,00 | 2026-11-20 | 22.8 u | 24 | 6 | 18 | €7,25 | €1,79 (12x) | **€5,46** | 0.11% | €-76,85 | €-71,39 | -1.43% |
| bitget - kucoin | €5.000,00 | 2026-11-21 | 22.9 u | 39 | 12 | 27 | €5,08 | €4,43 (23x) | **€0,65** | 0.01% | €-13,21 | €-12,56 | -0.25% |
| bitget - kucoin | €5.000,00 | 2026-11-22 | 22.1 u | 49 | 41 | 8 | €1,93 | €0,01 (2x) | **€1,91** | 0.04% | €-91,01 | €-89,10 | -1.78% |
| bitget - kucoin | €5.000,00 | 2026-11-23 | 19.7 u | 46 | 35 | 11 | €1,87 | €1,18 (7x) | **€0,68** | 0.01% | €-30,32 | €-29,64 | -0.59% |
| bitget - kucoin | €5.000,00 | 2026-11-24 | 6.9 u | 20 | 18 | 2 | €0,47 | €0,00 (1x) | **€0,47** | 0.01% | €55,81 | €56,28 | 1.13% |

- htx - kucoin, €100,00: munten ACN, AI, ALGO, ANIME, APT, ATOM, BIO, BONK, BRISE, BSV, BTT, CAP, CELO, CFX, CHIP, CVX, DCR, DYDX, ELA, ENJ, ENS, ENSO, FET, JASMY, JST, KSM, LAT, LTC, LUNA, LUNC, MAPO, MEME, MINA, MOVR, NES, NIGHT, NPC, ONE, PEOPLE, PUMP, QNT, RUNE, SAND, SD, SHIB, SOMI, SSV, TAO, TRAC, VIRTUAL, WAN, WARD, WIN, WLD, XCH, XCN, XEC, XMR, XTZ; bruto zonder voorraadgrens zou €983,84 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - kucoin, €150,00: munten ACN, AI, ALGO, ANIME, APT, ATOM, BIO, BONK, BRISE, BSV, BTT, CAP, CELO, CFX, CHIP, CVX, DCR, DYDX, ELA, ENJ, ENS, ENSO, FET, JASMY, JST, KSM, LAT, LTC, LUNA, LUNC, MAPO, MEME, MINA, MOVR, NES, NIGHT, NPC, ONE, PEOPLE, PUMP, QNT, RUNE, SAND, SD, SHIB, SOMI, SSV, TAO, TRAC, VIRTUAL, WAN, WARD, WIN, WLD, XCH, XCN, XEC, XMR, XTZ; bruto zonder voorraadgrens zou €983,84 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - kucoin, €200,00: munten ACN, AI, ALGO, ANIME, APT, ATOM, BIO, BONK, BRISE, BSV, BTT, CAP, CELO, CFX, CHIP, CVX, DCR, DYDX, ELA, ENJ, ENS, ENSO, FET, JASMY, JST, KSM, LAT, LTC, LUNA, LUNC, MAPO, MEME, MINA, MOVR, NES, NIGHT, NPC, ONE, PEOPLE, PUMP, QNT, RUNE, SAND, SD, SHIB, SOMI, SSV, TAO, TRAC, VIRTUAL, WAN, WARD, WIN, WLD, XCH, XCN, XEC, XMR, XTZ; bruto zonder voorraadgrens zou €983,84 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - kucoin, €2.000,00: munten ACN, AI, ALGO, ANIME, APT, ATOM, BIO, BONK, BRISE, BSV, BTT, CAP, CELO, CFX, CHIP, CVX, DCR, DYDX, ELA, ENJ, ENS, ENSO, FET, JASMY, JST, KSM, LAT, LTC, LUNA, LUNC, MAPO, MEME, MINA, MOVR, NES, NIGHT, NPC, ONE, PEOPLE, PUMP, QNT, RUNE, SAND, SD, SHIB, SOMI, SSV, TAO, TRAC, VIRTUAL, WAN, WARD, WIN, WLD, XCH, XCN, XEC, XMR, XTZ; bruto zonder voorraadgrens zou €983,84 zijn, met voorraad €2,65 (GEZIEN boek, GOK model).
- htx - kucoin, €5.000,00: munten ACN, AI, ALGO, ANIME, APT, ATOM, BIO, BONK, BRISE, BSV, BTT, CAP, CELO, CFX, CHIP, CVX, DCR, DYDX, ELA, ENJ, ENS, ENSO, FET, JASMY, JST, KSM, LAT, LTC, LUNA, LUNC, MAPO, MEME, MINA, MOVR, NES, NIGHT, NPC, ONE, PEOPLE, PUMP, QNT, RUNE, SAND, SD, SHIB, SOMI, SSV, TAO, TRAC, VIRTUAL, WAN, WARD, WIN, WLD, XCH, XCN, XEC, XMR, XTZ; bruto zonder voorraadgrens zou €983,09 zijn, met voorraad €21,61 (GEZIEN boek, GOK model).
- bitget - htx, €100,00: munten AB, ACN, AI, ALGO, ANIME, ATOM, BABY, BIO, BONK, BSV, BTT, CBK, CFX, CORE, DYDX, ENA, ENJ, ENS, ENSO, GALA, HBAR, HIVE, IOST, JASMY, KAITO, KAS, KSM, LAT, LINK, LIT, LUNA, LUNC, M, MAPO, MEME, MINA, MOVR, NES, NPC, O, PCI, PEOPLE, PUMP, QNT, RIVER, S, SAND, SHIB, SNEK, SOMI, SSV, TAO, TIA, TLOS, USTC, VIRTUAL, WARD, WLD, XDC, XTZ, ZEN; bruto zonder voorraadgrens zou €948,62 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - htx, €150,00: munten AB, ACN, AI, ALGO, ANIME, ATOM, BABY, BIO, BONK, BSV, BTT, CBK, CFX, CORE, DYDX, ENA, ENJ, ENS, ENSO, GALA, HBAR, HIVE, IOST, JASMY, KAITO, KAS, KSM, LAT, LINK, LIT, LUNA, LUNC, M, MAPO, MEME, MINA, MOVR, NES, NPC, O, PCI, PEOPLE, PUMP, QNT, RIVER, S, SAND, SHIB, SNEK, SOMI, SSV, TAO, TIA, TLOS, USTC, VIRTUAL, WARD, WLD, XDC, XTZ, ZEN; bruto zonder voorraadgrens zou €948,62 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - htx, €200,00: munten AB, ACN, AI, ALGO, ANIME, ATOM, BABY, BIO, BONK, BSV, BTT, CBK, CFX, CORE, DYDX, ENA, ENJ, ENS, ENSO, GALA, HBAR, HIVE, IOST, JASMY, KAITO, KAS, KSM, LAT, LINK, LIT, LUNA, LUNC, M, MAPO, MEME, MINA, MOVR, NES, NPC, O, PCI, PEOPLE, PUMP, QNT, RIVER, S, SAND, SHIB, SNEK, SOMI, SSV, TAO, TIA, TLOS, USTC, VIRTUAL, WARD, WLD, XDC, XTZ, ZEN; bruto zonder voorraadgrens zou €948,62 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - htx, €2.000,00: munten AB, ACN, AI, ALGO, ANIME, ATOM, BABY, BIO, BONK, BSV, BTT, CBK, CFX, CORE, DYDX, ENA, ENJ, ENS, ENSO, GALA, HBAR, HIVE, IOST, JASMY, KAITO, KAS, KSM, LAT, LINK, LIT, LUNA, LUNC, M, MAPO, MEME, MINA, MOVR, NES, NPC, O, PCI, PEOPLE, PUMP, QNT, RIVER, S, SAND, SHIB, SNEK, SOMI, SSV, TAO, TIA, TLOS, USTC, VIRTUAL, WARD, WLD, XDC, XTZ, ZEN; bruto zonder voorraadgrens zou €948,62 zijn, met voorraad €1,51 (GEZIEN boek, GOK model).
- bitget - htx, €5.000,00: munten AB, ACN, AI, ALGO, ANIME, ATOM, BABY, BIO, BONK, BSV, BTT, CBK, CFX, CORE, DYDX, ENA, ENJ, ENS, ENSO, GALA, HBAR, HIVE, IOST, JASMY, KAITO, KAS, KSM, LAT, LINK, LIT, LUNA, LUNC, M, MAPO, MEME, MINA, MOVR, NES, NPC, O, PCI, PEOPLE, PUMP, QNT, RIVER, S, SAND, SHIB, SNEK, SOMI, SSV, TAO, TIA, TLOS, USTC, VIRTUAL, WARD, WLD, XDC, XTZ, ZEN; bruto zonder voorraadgrens zou €947,93 zijn, met voorraad €20,89 (GEZIEN boek, GOK model).
- gate - htx, €100,00: munten AKT, ALGO, APEPE, APT, ATOM, BIO, BRISE, BSV, BTT, CBK, CELO, CORE, CRTS, CVX, ENJ, ENS, ENSO, GOMINING, GT, HBAR, HIVE, KAS, KCT, KSM, LAT, LINK, LUNA, LUNC, M, MBX, MEGA, MEME, MOVR, NES, NPC, PENGU, PEOPLE, PYR, QNT, SAND, SC, SD, SEI, SHIB, SOMI, SSV, TLOS, ULTIMA, VIRTUAL, WARD, WLD, XCH, XCN, XDC; bruto zonder voorraadgrens zou €771,43 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- gate - htx, €150,00: munten AKT, ALGO, APEPE, APT, ATOM, BIO, BRISE, BSV, BTT, CBK, CELO, CORE, CRTS, CVX, ENJ, ENS, ENSO, GOMINING, GT, HBAR, HIVE, KAS, KCT, KSM, LAT, LINK, LUNA, LUNC, M, MBX, MEGA, MEME, MOVR, NES, NPC, PENGU, PEOPLE, PYR, QNT, SAND, SC, SD, SEI, SHIB, SOMI, SSV, TLOS, ULTIMA, VIRTUAL, WARD, WLD, XCH, XCN, XDC; bruto zonder voorraadgrens zou €771,43 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- gate - htx, €200,00: munten AKT, ALGO, APEPE, APT, ATOM, BIO, BRISE, BSV, BTT, CBK, CELO, CORE, CRTS, CVX, ENJ, ENS, ENSO, GOMINING, GT, HBAR, HIVE, KAS, KCT, KSM, LAT, LINK, LUNA, LUNC, M, MBX, MEGA, MEME, MOVR, NES, NPC, PENGU, PEOPLE, PYR, QNT, SAND, SC, SD, SEI, SHIB, SOMI, SSV, TLOS, ULTIMA, VIRTUAL, WARD, WLD, XCH, XCN, XDC; bruto zonder voorraadgrens zou €771,43 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- gate - htx, €2.000,00: munten AKT, ALGO, APEPE, APT, ATOM, BIO, BRISE, BSV, BTT, CBK, CELO, CORE, CRTS, CVX, ENJ, ENS, ENSO, GOMINING, GT, HBAR, HIVE, KAS, KCT, KSM, LAT, LINK, LUNA, LUNC, M, MBX, MEGA, MEME, MOVR, NES, NPC, PENGU, PEOPLE, PYR, QNT, SAND, SC, SD, SEI, SHIB, SOMI, SSV, TLOS, ULTIMA, VIRTUAL, WARD, WLD, XCH, XCN, XDC; bruto zonder voorraadgrens zou €771,43 zijn, met voorraad €0,18 (GEZIEN boek, GOK model).
- gate - htx, €5.000,00: munten AKT, ALGO, APEPE, APT, ATOM, BIO, BRISE, BSV, BTT, CBK, CELO, CORE, CRTS, CVX, ENJ, ENS, ENSO, GOMINING, GT, HBAR, HIVE, KAS, KCT, KSM, LAT, LINK, LUNA, LUNC, M, MBX, MEGA, MEME, MOVR, NES, NPC, PENGU, PEOPLE, PYR, QNT, SAND, SC, SD, SEI, SHIB, SOMI, SSV, TLOS, ULTIMA, VIRTUAL, WARD, WLD, XCH, XCN, XDC; bruto zonder voorraadgrens zou €770,73 zijn, met voorraad €24,16 (GEZIEN boek, GOK model).
- htx - xt, €100,00: munten ALGO, APEPE, APT, BIO, BSV, CARV, CBK, CELO, CFX, GT, HBAR, KSM, LUNA, LUNC, MEME, MINA, PENGU, PEOPLE, RAIN, SC, SEI, SHIB, SOMI, TLOS, XCH, XDC, XMR; bruto zonder voorraadgrens zou €859,74 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - xt, €150,00: munten ALGO, APEPE, APT, BIO, BSV, CARV, CBK, CELO, CFX, GT, HBAR, KSM, LUNA, LUNC, MEME, MINA, PENGU, PEOPLE, RAIN, SC, SEI, SHIB, SOMI, TLOS, XCH, XDC, XMR; bruto zonder voorraadgrens zou €859,74 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - xt, €200,00: munten ALGO, APEPE, APT, BIO, BSV, CARV, CBK, CELO, CFX, GT, HBAR, KSM, LUNA, LUNC, MEME, MINA, PENGU, PEOPLE, RAIN, SC, SEI, SHIB, SOMI, TLOS, XCH, XDC, XMR; bruto zonder voorraadgrens zou €859,74 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - xt, €2.000,00: munten ALGO, APEPE, APT, BIO, BSV, CARV, CBK, CELO, CFX, GT, HBAR, KSM, LUNA, LUNC, MEME, MINA, PENGU, PEOPLE, RAIN, SC, SEI, SHIB, SOMI, TLOS, XCH, XDC, XMR; bruto zonder voorraadgrens zou €859,52 zijn, met voorraad €9,40 (GEZIEN boek, GOK model).
- htx - xt, €5.000,00: munten ALGO, APEPE, APT, BIO, BSV, CARV, CBK, CELO, CFX, GT, HBAR, KSM, LUNA, LUNC, MEME, MINA, PENGU, PEOPLE, RAIN, SC, SEI, SHIB, SOMI, TLOS, XCH, XDC, XMR; bruto zonder voorraadgrens zou €858,26 zijn, met voorraad €32,42 (GEZIEN boek, GOK model).
- bitget - kucoin, €100,00: munten ACE, BARD, BTC, CARV, CHR, DMC, EDEN, EGL1, ENJ, ENSO, ETH, HYPER, IR, JST, KAVA, KLV, KNC, LAT, LUNC, MASK, MHA, MTX, NES, NOM, PROVE, TAC, TLOS, USDC, USDT, USTC, VERONA; bruto zonder voorraadgrens zou €529,89 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - kucoin, €150,00: munten ACE, BARD, BTC, CARV, CHR, DMC, EDEN, EGL1, ENJ, ENSO, ETH, HYPER, IR, JST, KAVA, KLV, KNC, LAT, LUNC, MASK, MHA, MTX, NES, NOM, PROVE, TAC, TLOS, USDC, USDT, USTC, VERONA; bruto zonder voorraadgrens zou €529,89 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - kucoin, €200,00: munten ACE, BARD, BTC, CARV, CHR, DMC, EDEN, EGL1, ENJ, ENSO, ETH, HYPER, IR, JST, KAVA, KLV, KNC, LAT, LUNC, MASK, MHA, MTX, NES, NOM, PROVE, TAC, TLOS, USDC, USDT, USTC, VERONA; bruto zonder voorraadgrens zou €529,89 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - kucoin, €2.000,00: munten ACE, BARD, BTC, CARV, CHR, DMC, EDEN, EGL1, ENJ, ENSO, ETH, HYPER, IR, JST, KAVA, KLV, KNC, LAT, LUNC, MASK, MHA, MTX, NES, NOM, PROVE, TAC, TLOS, USDC, USDT, USTC, VERONA; bruto zonder voorraadgrens zou €529,54 zijn, met voorraad €3,89 (GEZIEN boek, GOK model).
- bitget - kucoin, €5.000,00: munten ACE, BARD, BTC, CARV, CHR, DMC, EDEN, EGL1, ENJ, ENSO, ETH, HYPER, IR, JST, KAVA, KLV, KNC, LAT, LUNC, MASK, MHA, MTX, NES, NOM, PROVE, TAC, TLOS, USDC, USDT, USTC, VERONA; bruto zonder voorraadgrens zou €527,78 zijn, met voorraad €20,17 (GEZIEN boek, GOK model).

### Andere keuzes bij bitvavo - kraken (netto handel, alle dagen samen; GOK)

| Keuze | Inleg | Kansen | Gemist | Bruto winst | Kosten terugschuiven | Netto handel |
|---|---|---|---|---|---|---|
| standaard (schuifdrempel 25%, kostengrens 1%) | €150,00 | 160 | 160 | €0,00 | €0,00 | **€0,00** |
| standaard (schuifdrempel 25%, kostengrens 1%) | €2.000,00 | 160 | 99 | €55,60 | €22,19 | **€33,41** |
| schuifdrempel 10% | €150,00 | 160 | 160 | €0,00 | €0,00 | **€0,00** |
| schuifdrempel 10% | €2.000,00 | 160 | 99 | €55,60 | €21,19 | **€34,41** |
| schuifdrempel 40% | €150,00 | 160 | 160 | €0,00 | €0,00 | **€0,00** |
| schuifdrempel 40% | €2.000,00 | 160 | 99 | €55,28 | €23,19 | **€32,09** |
| kostengrens 2% (achteraf vergeleken) | €150,00 | 160 | 160 | €0,00 | €0,00 | **€0,00** |
| kostengrens 2% (achteraf vergeleken) | €2.000,00 | 160 | 94 | €55,85 | €25,39 | **€30,46** |
| kostengrens 5% (achteraf vergeleken) | €150,00 | 160 | 160 | €0,00 | €0,00 | **€0,00** |
| kostengrens 5% (achteraf vergeleken) | €2.000,00 | 160 | 50 | €59,94 | €76,68 | **€-16,74** |
| alleen MERL en GMT (meer voorraad per munt, achteraf gekozen) | €150,00 | 131 | 129 | €0,19 | €0,00 | **€0,19** |
| alleen MERL en GMT (meer voorraad per munt, achteraf gekozen) | €2.000,00 | 131 | 44 | €265,16 | €81,15 | **€184,01** |

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

- Opnamekosten bij de echte kansen: 497 van een netwerk dat aan beide kanten open is, 334 van de beurs zelf (laagste open netwerk), 180 geschat uit wat andere beurzen voor die munt vragen (GOK). Onbekende opnamekosten tellen niet als echte kans.
- Netwerk: KuCoin, Gate, Bitget, HTX, XT, Bitstamp, Bitvavo en Poloniex geven hun netwerken per munt. Als beide beurzen dat doen en de namen te koppelen zijn, moet er een netwerk zijn dat aan beide kanten open is. Anders is het netwerk "niet te koppelen" en telt de kans mee (staat apart in de trechter).
- De duur is gemeten in stappen van ±20 seconden; een kans kan een paar rondes eerder begonnen zijn dan we zagen.
- Takerkosten: uit de API waar die ze per paar geeft, anders het standaardtarief uit de README (deels GOK).
- Laatste run: 15 beurzen antwoordden, 2278 munt-quote-paren op minstens twee beurzen (GEZIEN).
