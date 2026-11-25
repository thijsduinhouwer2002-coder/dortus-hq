# Rapport koersverschil-scanner

Gemaakt 2026-11-25 03:18 UTC uit 39 runs, samen ±125.4 uur gemeten (GEZIEN).
Echte kans = winst na alle kosten (opnamekosten bekend), opnemen en storten open (en een netwerk dat aan beide kanten open is, als de beurzen dat geven), minstens €100,00 op het boek, minstens 2 minuten blijven staan, geen andere munt met dezelfde naam.
**Vergund** = beide beurzen hebben een MiCA-vergunning (ESMA-register), vaak via een EU-dochter die minder munten kan hebben dan de wereldwijde API die we meten (GOK). **Grijs** = minstens één beurs zonder vergunning (MEXC, Bitget, HTX, Poloniex, XT, Bitfinex, Binance). Zie README.md.
**Kraken-tarief:** Kraken rekent 0,80% taker op munt tegen EUR, USD, USDT of USDC (GEZIEN, kraken.com/pro/fees, laagste trede); de scanner rekende tot 19 nov met 0,40%. 399 opgeslagen kansen met Kraken uit die runs zijn hier **opnieuw doorgerekend met 0,80%** (GOK-benadering: 0,40% van de inzet aan de Kraken-kant extra op elk gemeten punt van het boek; het boek zelf is niet bewaard). 233 houden daarna nog winst op het boek. Dat ze met hogere kosten ook korter bleven staan, telt niet mee (dus eerder te gunstig).

## Hoeveel wordt er gecontroleerd? (GEZIEN, stand.jsonl)

Per ronde (mediaan over 1502 metingen): 1054 kandidaten (verschil op de ticker groter dan de takerkosten), 120 met het orderboek gecontroleerd, 2 nog nooit gecontroleerd (0%).
Bijna alle kandidaten komen aan de beurt; de aantallen hieronder missen weinig.

## Trechter (GEZIEN, eigen metingen)

| Stap | Alle beurzen | Alleen MiCA-beurzen | Met minstens één grijze beurs |
|---|---|---|---|
| Verschillen met winst op het boek na alle kosten | 106441 | 14432 | 92009 |
| ...waarvan opnemen of storten dicht | 19719 | 2221 | 17498 |
| ...waarvan status onbekend (beurs geeft het niet openbaar) | 62803 | 10132 | 52671 |
| Opnemen en storten open | 23919 | 2079 | 21840 |
| ...en geen netwerk dat aan beide kanten open is: valt af | 873 | 79 | 794 |
| ...en opnamekosten onbekend: valt af | 5 | 5 | 0 |
| ...en minstens €100,00 op het boek | 6937 | 1213 | 5724 |
| ...en minstens 2 minuten blijven staan | 1891 | 461 | 1430 |
| ...en geen andere munt met dezelfde naam | 1823 | 426 | 1397 |
|    ...waarvan contractadres bekend en gelijk | 302 | 81 | 221 |
|    ...waarvan contractadres onbekend (telt mee, kan een andere munt zijn) | 1521 | 345 | 1176 |
|    ...waarvan netwerk gekoppeld en open | 1152 | 205 | 947 |
|    ...waarvan netwerk niet te koppelen (telt mee) | 671 | 221 | 450 |
| **Echte kansen** (zelfde munt overlappend in de tijd samengevoegd, beste beurspaar telt) | 1146 | 416 | 848 |
| Ter vergelijking: zelfde eisen, maar opnamestatus onbekend (niet meegeteld) | 4480 | 1134 | 3766 |

## Echte kansen per dag (GEZIEN)

| Dag | Echt, alleen MiCA | Echt, met grijs | Mediane winst per kans bij €500 (MiCA / grijs) | Mediane duur |
|---|---|---|---|---|
| 2026-11-19 | 49 | 86 | €2,00 / €1,21 | 5.3 min |
| 2026-11-20 | 53 | 138 | €1,01 / €1,13 | 6.7 min |
| 2026-11-21 | 61 | 176 | €1,13 / €0,88 | 6.7 min |
| 2026-11-22 | 60 | 165 | €1,74 / €0,93 | 9.3 min |
| 2026-11-23 | 53 | 113 | €1,10 / €1,00 | 6.8 min |
| 2026-11-24 | 42 | 129 | €0,65 / €0,53 | 4.3 min |
| 2026-11-25 | 5 | 16 | €0,27 / €24,94 | 4.3 min |
| Totaal | 323 | 823 | €1,03 / €0,89 | 6.3 min |

## Beste munten (GEZIEN)

| | Soort | Kansen | Som winst bij €500 per kans |
|---|---|---|---|
| MERL-EUR | vergund | 75 | €1.013,65 |
| AI-USDT | grijs | 44 | €791,44 |
| PYR-USDT | grijs | 15 | €184,06 |
| LUNC-USDT | grijs | 44 | €171,85 |
| USTC-USDT | grijs en vergund | 58 | €127,37 |
| XMR-USDT | grijs | 82 | €103,39 |
| NES-USDT | grijs en vergund | 8 | €95,21 |
| DCR-USDT | grijs en vergund | 3 | €58,78 |
| IR-USDT | grijs en vergund | 19 | €48,47 |
| ENSO-USDT | grijs en vergund | 15 | €48,21 |

## Beste beursparen (kopen op > verkopen op) (GEZIEN)

| | Soort | Kansen | Som winst bij €500 per kans |
|---|---|---|---|
| bitvavo > kraken | vergund | 183 | €1.164,80 |
| htx > kucoin | grijs | 61 | €750,36 |
| htx > gate | grijs | 41 | €269,19 |
| bitget > htx | grijs | 102 | €205,10 |
| gate > kucoin | vergund | 58 | €167,93 |
| kucoin > bitget | grijs | 97 | €148,33 |
| htx > bitget | grijs | 38 | €140,49 |
| bitget > kucoin | grijs | 98 | €133,15 |
| kucoin > htx | grijs | 52 | €108,15 |
| gate > htx | grijs | 41 | €105,19 |

Beurzen die het vaakst meedoen (koop of verkoop): kucoin 528, bitget (grijs) 470, htx (grijs) 385, gate 269, kraken 223, bitvavo 198, poloniex (grijs) 124, xt (grijs) 92 (GEZIEN).

## Hoeveel kansen blijven staan terwijl je geld schuift? (GEZIEN, duur uit eigen metingen)

Wie geen voorraad op beide beurzen heeft, moet kopen, de munt opnemen, wachten tot hij binnen is en dan verkopen. Hoe lang dat duurt verschilt per munt en netwerk: een paar minuten (snelle ketens) tot een uur of meer (Bitcoin, beurzen die opnames met de hand keuren) (GOK, niet per munt gemeten).

| Overmaaktijd | Alle beurzen | Alleen MiCA-beurzen | Met minstens één grijze beurs |
|---|---|---|---|
| 5 min | 663 van 1146 (58%) | 251 van 416 (60%) | 488 van 848 (58%) |
| 10 min | 438 van 1146 (38%) | 173 van 416 (42%) | 323 van 848 (38%) |
| 30 min | 220 van 1146 (19%) | 87 van 416 (21%) | 169 van 848 (20%) |
| 60 min | 122 van 1146 (11%) | 54 van 416 (13%) | 95 van 848 (11%) |

## Wat zou het opleveren over 3 maanden? (GOK, doorgetrokken uit de metingen)

Gemeten over ±125.4 uur (GEZIEN), doorgetrokken naar 90 dagen (GOK: aanname dat de week die we maten gewoon is).

| Beurzen | Inleg | Model | Kansen per uur | Per kans (mediaan) | 3 maanden |
|---|---|---|---|---|---|
| Alleen MiCA | €2.000,00 | bovengrens: elke kans, geld overal tegelijk | 3.32 | €1,41 | €10.106,07 |
| Alleen MiCA | €2.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 1.46 | €1,78 | €36.027,31 |
| Alleen MiCA | €5.000,00 | bovengrens: elke kans, geld overal tegelijk | 3.32 | €1,76 | €12.580,91 |
| Alleen MiCA | €5.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 1.46 | €2,80 | €66.203,37 |
| Alle (met grijs) | €2.000,00 | bovengrens: elke kans, geld overal tegelijk | 9.14 | €1,29 | €25.495,67 |
| Alle (met grijs) | €2.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 1.46 | €1,78 | €36.027,31 |
| Alle (met grijs) | €5.000,00 | bovengrens: elke kans, geld overal tegelijk | 9.14 | €1,51 | €29.851,35 |
| Alle (met grijs) | €5.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 1.46 | €2,80 | €66.203,37 |

Bovengrens: elke kans met de helft van de inleg aan elke kant, alsof het geld op alle beurzen tegelijk staat (kan in het echt niet). Beste beurspaar: het paar is **achteraf** gekozen uit de metingen (vooraf kiezen levert minder op), en het model neemt aan dat je van elke munt al voorraad op de verkoopbeurs hebt.

Waarom dit te rooskleurig is (GOK): elke kans wordt maar één keer geteld met het mediane boek, maar andere bots pakken hem ook; de munt die je als voorraad aanhoudt kan dalen; na een paar kansen moet de voorraad terug (opnamekosten en tijd); minimale opname- en ordergroottes tellen niet mee; en een kans die we 2 minuten zagen staan, staat er niet per se nog als jouw order binnenkomt. Waarom het te somber kan zijn: niet alle kandidaten zijn gecontroleerd, en met voorraad op beide beurzen kun je dezelfde kans vaker pakken als het boek zich aanvult; dat telt hier niet mee.

## Wat houd je echt over? Voorraad op twee beurzen (simulatie)

Per beurspaar: geld en munten op beide beurzen, elke echte kans uitgevoerd tegen het boek zoals gemeten (niet meer dan de ruimte op het boek en niet meer dan de voorraad op die beurs), terugschuiven als een kant leeg dreigt te raken (met opnamekosten en tijd onderweg), en het koerseffect van de aangehouden munten apart. Netto = bruto min kosten terugschuiven plus koerseffect. **Gemeten** (GEZIEN): de kansen, het boek en de koersen; **de rest is een rekenmodel** (GOK, aannames onder de tabel). Geen advies.

**Met €150: netto €0,22 per dag op bitstamp - kraken (koerseffect erbovenop €-1,15), €0,00 per dag op bitstamp - kucoin (koerseffect erbovenop €0,01), €0,00 per dag op bitvavo - kraken (koerseffect erbovenop €-0,68), €0,01 per dag op bitvavo - kucoin (koerseffect erbovenop €-0,42), €0,00 per dag op gate - kucoin (koerseffect erbovenop €-1,17), €0,01 per dag op kraken - kucoin (koerseffect erbovenop €0,01) (GOK: netto handel, rekenmodel op ±17.9 uur meting per dag, alleen MiCA).** "Per dag" is hier gemiddeld over 7 gemeten dagen achter elkaar; de eerste begint met een gelijk verdeelde voorraad; aan het eind staat de voorraad scheef, dus een volgende dag levert waarschijnlijk minder op, tenzij kansen de andere kant op hem terugbrengen (GOK).

### Alleen MiCA-beurzen (alle paren met echte kansen)

| Beurspaar | Inleg | Dag | Gemeten | Kansen | Gemist (geen voorraad) | Kleiner door voorraad | Bruto winst | Kosten terugschuiven | **Netto handel (bruto min kosten)** | Rendement handel | Koerseffect voorraad | Netto met koerseffect | Rendement met koerseffect |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| bitstamp - kraken | €100,00 | 2026-11-19 | 14.9 u | 2 | 1 | 1 | €0,59 | €0,00 (0x) | **€0,59** | 0.59% | €-0,02 | €0,57 | 0.57% |
| bitstamp - kraken | €100,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,95 | €-2,95 | -2.95% |
| bitstamp - kraken | €100,00 | 2026-11-21 | 22.9 u | 1 | 0 | 1 | €0,45 | €0,00 (0x) | **€0,45** | 0.45% | €-0,70 | €-0,25 | -0.25% |
| bitstamp - kraken | €100,00 | 2026-11-22 | 22.1 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,42 | €-1,42 | -1.42% |
| bitstamp - kraken | €100,00 | 2026-11-23 | 19.7 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,23 | €-0,23 | -0.23% |
| bitstamp - kraken | €100,00 | 2026-11-24 | 19.5 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,19 | €0,19 | 0.19% |
| bitstamp - kraken | €100,00 | 2026-11-25 | 3.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,22 | €-0,22 | -0.22% |
| bitstamp - kraken | €150,00 | 2026-11-19 | 14.9 u | 2 | 1 | 1 | €0,89 | €0,00 (0x) | **€0,89** | 0.59% | €-0,03 | €0,85 | 0.57% |
| bitstamp - kraken | €150,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-4,43 | €-4,43 | -2.95% |
| bitstamp - kraken | €150,00 | 2026-11-21 | 22.9 u | 1 | 0 | 1 | €0,67 | €0,00 (0x) | **€0,67** | 0.45% | €-1,05 | €-0,38 | -0.25% |
| bitstamp - kraken | €150,00 | 2026-11-22 | 22.1 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,13 | €-2,13 | -1.42% |
| bitstamp - kraken | €150,00 | 2026-11-23 | 19.7 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,34 | €-0,34 | -0.23% |
| bitstamp - kraken | €150,00 | 2026-11-24 | 19.5 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,28 | €0,28 | 0.19% |
| bitstamp - kraken | €150,00 | 2026-11-25 | 3.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,33 | €-0,33 | -0.22% |
| bitstamp - kraken | €200,00 | 2026-11-19 | 14.9 u | 2 | 1 | 1 | €1,18 | €0,00 (0x) | **€1,18** | 0.59% | €-0,04 | €1,14 | 0.57% |
| bitstamp - kraken | €200,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-5,91 | €-5,91 | -2.95% |
| bitstamp - kraken | €200,00 | 2026-11-21 | 22.9 u | 1 | 0 | 1 | €0,89 | €0,00 (0x) | **€0,89** | 0.45% | €-1,40 | €-0,51 | -0.25% |
| bitstamp - kraken | €200,00 | 2026-11-22 | 22.1 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,85 | €-2,85 | -1.42% |
| bitstamp - kraken | €200,00 | 2026-11-23 | 19.7 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,46 | €-0,46 | -0.23% |
| bitstamp - kraken | €200,00 | 2026-11-24 | 19.5 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,38 | €0,38 | 0.19% |
| bitstamp - kraken | €200,00 | 2026-11-25 | 3.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,44 | €-0,44 | -0.22% |
| bitstamp - kraken | €2.000,00 | 2026-11-19 | 14.9 u | 2 | 1 | 0 | €11,71 | €0,98 (1x) | **€10,73** | 0.54% | €-0,46 | €10,27 | 0.51% |
| bitstamp - kraken | €2.000,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-59,03 | €-59,03 | -2.95% |
| bitstamp - kraken | €2.000,00 | 2026-11-21 | 22.9 u | 1 | 0 | 0 | €5,30 | €0,00 (0x) | **€5,30** | 0.26% | €-14,01 | €-8,71 | -0.44% |
| bitstamp - kraken | €2.000,00 | 2026-11-22 | 22.1 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-28,41 | €-28,41 | -1.42% |
| bitstamp - kraken | €2.000,00 | 2026-11-23 | 19.7 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-4,54 | €-4,54 | -0.23% |
| bitstamp - kraken | €2.000,00 | 2026-11-24 | 19.5 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €3,78 | €3,78 | 0.19% |
| bitstamp - kraken | €2.000,00 | 2026-11-25 | 3.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-4,38 | €-4,38 | -0.22% |
| bitstamp - kraken | €5.000,00 | 2026-11-19 | 14.9 u | 2 | 1 | 0 | €11,71 | €0,00 (0x) | **€11,71** | 0.23% | €-1,10 | €10,60 | 0.21% |
| bitstamp - kraken | €5.000,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-147,75 | €-147,75 | -2.95% |
| bitstamp - kraken | €5.000,00 | 2026-11-21 | 22.9 u | 1 | 0 | 0 | €5,30 | €0,00 (0x) | **€5,30** | 0.11% | €-35,01 | €-29,71 | -0.59% |
| bitstamp - kraken | €5.000,00 | 2026-11-22 | 22.1 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-71,15 | €-71,15 | -1.42% |
| bitstamp - kraken | €5.000,00 | 2026-11-23 | 19.7 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-11,41 | €-11,41 | -0.23% |
| bitstamp - kraken | €5.000,00 | 2026-11-24 | 19.5 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €9,49 | €9,49 | 0.19% |
| bitstamp - kraken | €5.000,00 | 2026-11-25 | 3.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-10,95 | €-10,95 | -0.22% |
| bitstamp - kucoin | €100,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,11 | €0,11 | 0.11% |
| bitstamp - kucoin | €100,00 | 2026-11-20 | 22.8 u | 1 | 0 | 1 | €0,00 | €0,01 (1x) | **€-0,01** | -0.01% | €0,11 | €0,10 | 0.10% |
| bitstamp - kucoin | €100,00 | 2026-11-21 | 22.9 u | 6 | 5 | 1 | €0,01 | €0,00 (0x) | **€0,01** | 0.01% | €-0,16 | €-0,15 | -0.15% |
| bitstamp - kucoin | €100,00 | 2026-11-22 | 22.1 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,08 | €-0,08 | -0.08% |
| bitstamp - kucoin | €100,00 | 2026-11-23 | 19.7 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,29 | €0,29 | 0.29% |
| bitstamp - kucoin | €100,00 | 2026-11-24 | 19.5 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,25 | €-0,25 | -0.25% |
| bitstamp - kucoin | €100,00 | 2026-11-25 | 3.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,03 | €0,03 | 0.03% |
| bitstamp - kucoin | €150,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,16 | €0,16 | 0.11% |
| bitstamp - kucoin | €150,00 | 2026-11-20 | 22.8 u | 1 | 0 | 1 | €0,00 | €0,01 (1x) | **€-0,01** | -0.00% | €0,16 | €0,16 | 0.11% |
| bitstamp - kucoin | €150,00 | 2026-11-21 | 22.9 u | 6 | 5 | 1 | €0,02 | €0,00 (0x) | **€0,02** | 0.01% | €-0,24 | €-0,22 | -0.15% |
| bitstamp - kucoin | €150,00 | 2026-11-22 | 22.1 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,12 | €-0,12 | -0.08% |
| bitstamp - kucoin | €150,00 | 2026-11-23 | 19.7 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,44 | €0,44 | 0.29% |
| bitstamp - kucoin | €150,00 | 2026-11-24 | 19.5 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,38 | €-0,38 | -0.25% |
| bitstamp - kucoin | €150,00 | 2026-11-25 | 3.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,05 | €0,05 | 0.03% |
| bitstamp - kucoin | €200,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,22 | €0,22 | 0.11% |
| bitstamp - kucoin | €200,00 | 2026-11-20 | 22.8 u | 1 | 0 | 1 | €0,01 | €0,01 (1x) | **€-0,00** | -0.00% | €0,22 | €0,22 | 0.11% |
| bitstamp - kucoin | €200,00 | 2026-11-21 | 22.9 u | 6 | 5 | 1 | €0,03 | €0,23 (1x) | **€-0,21** | -0.10% | €-0,32 | €-0,53 | -0.26% |
| bitstamp - kucoin | €200,00 | 2026-11-22 | 22.1 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,16 | €-0,16 | -0.08% |
| bitstamp - kucoin | €200,00 | 2026-11-23 | 19.7 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,58 | €0,58 | 0.29% |
| bitstamp - kucoin | €200,00 | 2026-11-24 | 19.5 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,50 | €-0,50 | -0.25% |
| bitstamp - kucoin | €200,00 | 2026-11-25 | 3.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,06 | €0,06 | 0.03% |
| bitstamp - kucoin | €2.000,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €2,19 | €2,19 | 0.11% |
| bitstamp - kucoin | €2.000,00 | 2026-11-20 | 22.8 u | 1 | 0 | 1 | €0,05 | €0,01 (1x) | **€0,04** | 0.00% | €2,19 | €2,24 | 0.11% |
| bitstamp - kucoin | €2.000,00 | 2026-11-21 | 22.9 u | 6 | 5 | 1 | €0,27 | €1,23 (2x) | **€-0,97** | -0.05% | €-3,24 | €-4,20 | -0.21% |
| bitstamp - kucoin | €2.000,00 | 2026-11-22 | 22.1 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,59 | €-1,59 | -0.08% |
| bitstamp - kucoin | €2.000,00 | 2026-11-23 | 19.7 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €5,81 | €5,81 | 0.29% |
| bitstamp - kucoin | €2.000,00 | 2026-11-24 | 19.5 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-5,05 | €-5,05 | -0.25% |
| bitstamp - kucoin | €2.000,00 | 2026-11-25 | 3.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,60 | €0,60 | 0.03% |
| bitstamp - kucoin | €5.000,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €5,49 | €5,49 | 0.11% |
| bitstamp - kucoin | €5.000,00 | 2026-11-20 | 22.8 u | 1 | 0 | 1 | €0,13 | €0,01 (1x) | **€0,12** | 0.00% | €5,48 | €5,60 | 0.11% |
| bitstamp - kucoin | €5.000,00 | 2026-11-21 | 22.9 u | 6 | 5 | 1 | €0,64 | €1,23 (2x) | **€-0,59** | -0.01% | €-8,09 | €-8,68 | -0.17% |
| bitstamp - kucoin | €5.000,00 | 2026-11-22 | 22.1 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,98 | €-3,98 | -0.08% |
| bitstamp - kucoin | €5.000,00 | 2026-11-23 | 19.7 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €14,53 | €14,53 | 0.29% |
| bitstamp - kucoin | €5.000,00 | 2026-11-24 | 19.5 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-12,61 | €-12,61 | -0.25% |
| bitstamp - kucoin | €5.000,00 | 2026-11-25 | 3.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €1,51 | €1,51 | 0.03% |
| bitvavo - kraken | €100,00 | 2026-11-19 | 14.9 u | 43 | 43 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,66 | €-0,66 | -0.66% |
| bitvavo - kraken | €100,00 | 2026-11-20 | 22.8 u | 15 | 15 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,98 | €-1,98 | -1.98% |
| bitvavo - kraken | €100,00 | 2026-11-21 | 22.9 u | 26 | 26 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,46 | €-0,46 | -0.46% |
| bitvavo - kraken | €100,00 | 2026-11-22 | 22.1 u | 40 | 40 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,07 | €-0,07 | -0.07% |
| bitvavo - kraken | €100,00 | 2026-11-23 | 19.7 u | 28 | 28 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €1,45 | €1,45 | 1.45% |
| bitvavo - kraken | €100,00 | 2026-11-24 | 19.5 u | 28 | 28 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,52 | €-1,52 | -1.52% |
| bitvavo - kraken | €100,00 | 2026-11-25 | 3.3 u | 3 | 3 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,05 | €0,05 | 0.05% |
| bitvavo - kraken | €150,00 | 2026-11-19 | 14.9 u | 43 | 43 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,99 | €-0,99 | -0.66% |
| bitvavo - kraken | €150,00 | 2026-11-20 | 22.8 u | 15 | 15 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,97 | €-2,97 | -1.98% |
| bitvavo - kraken | €150,00 | 2026-11-21 | 22.9 u | 26 | 26 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,69 | €-0,69 | -0.46% |
| bitvavo - kraken | €150,00 | 2026-11-22 | 22.1 u | 40 | 40 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,11 | €-0,11 | -0.07% |
| bitvavo - kraken | €150,00 | 2026-11-23 | 19.7 u | 28 | 28 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €2,17 | €2,17 | 1.45% |
| bitvavo - kraken | €150,00 | 2026-11-24 | 19.5 u | 28 | 28 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,28 | €-2,28 | -1.52% |
| bitvavo - kraken | €150,00 | 2026-11-25 | 3.3 u | 3 | 3 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,08 | €0,08 | 0.05% |
| bitvavo - kraken | €200,00 | 2026-11-19 | 14.9 u | 43 | 43 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,32 | €-1,32 | -0.66% |
| bitvavo - kraken | €200,00 | 2026-11-20 | 22.8 u | 15 | 15 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,96 | €-3,96 | -1.98% |
| bitvavo - kraken | €200,00 | 2026-11-21 | 22.9 u | 26 | 26 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,92 | €-0,92 | -0.46% |
| bitvavo - kraken | €200,00 | 2026-11-22 | 22.1 u | 40 | 40 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,14 | €-0,14 | -0.07% |
| bitvavo - kraken | €200,00 | 2026-11-23 | 19.7 u | 28 | 28 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €2,89 | €2,89 | 1.45% |
| bitvavo - kraken | €200,00 | 2026-11-24 | 19.5 u | 28 | 28 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,03 | €-3,03 | -1.52% |
| bitvavo - kraken | €200,00 | 2026-11-25 | 3.3 u | 3 | 3 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,10 | €0,10 | 0.05% |
| bitvavo - kraken | €2.000,00 | 2026-11-19 | 14.9 u | 43 | 25 | 18 | €7,68 | €6,00 (17x) | **€1,68** | 0.08% | €-13,10 | €-11,41 | -0.57% |
| bitvavo - kraken | €2.000,00 | 2026-11-20 | 22.8 u | 15 | 11 | 4 | €9,18 | €1,32 (2x) | **€7,86** | 0.39% | €-39,30 | €-31,44 | -1.57% |
| bitvavo - kraken | €2.000,00 | 2026-11-21 | 22.9 u | 26 | 23 | 3 | €1,21 | €0,32 (1x) | **€0,89** | 0.04% | €-9,18 | €-8,29 | -0.41% |
| bitvavo - kraken | €2.000,00 | 2026-11-22 | 22.1 u | 40 | 37 | 3 | €1,40 | €0,64 (2x) | **€0,75** | 0.04% | €-1,35 | €-0,60 | -0.03% |
| bitvavo - kraken | €2.000,00 | 2026-11-23 | 19.7 u | 28 | 27 | 1 | €0,37 | €0,30 (1x) | **€0,07** | 0.00% | €28,87 | €28,94 | 1.45% |
| bitvavo - kraken | €2.000,00 | 2026-11-24 | 19.5 u | 28 | 26 | 2 | €1,32 | €0,33 (1x) | **€0,99** | 0.05% | €-30,27 | €-29,28 | -1.46% |
| bitvavo - kraken | €2.000,00 | 2026-11-25 | 3.3 u | 3 | 3 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €1,09 | €1,09 | 0.05% |
| bitvavo - kraken | €5.000,00 | 2026-11-19 | 14.9 u | 43 | 25 | 18 | €19,39 | €6,00 (17x) | **€13,39** | 0.27% | €-32,87 | €-19,48 | -0.39% |
| bitvavo - kraken | €5.000,00 | 2026-11-20 | 22.8 u | 15 | 9 | 6 | €37,79 | €3,46 (6x) | **€34,32** | 0.69% | €-98,41 | €-64,08 | -1.28% |
| bitvavo - kraken | €5.000,00 | 2026-11-21 | 22.9 u | 26 | 16 | 10 | €41,04 | €2,66 (8x) | **€38,38** | 0.77% | €-22,96 | €15,42 | 0.31% |
| bitvavo - kraken | €5.000,00 | 2026-11-22 | 22.1 u | 40 | 21 | 19 | €18,83 | €8,11 (21x) | **€10,72** | 0.21% | €-3,61 | €7,12 | 0.14% |
| bitvavo - kraken | €5.000,00 | 2026-11-23 | 19.7 u | 28 | 15 | 13 | €5,42 | €6,12 (15x) | **€-0,70** | -0.01% | €72,28 | €71,58 | 1.43% |
| bitvavo - kraken | €5.000,00 | 2026-11-24 | 19.5 u | 28 | 23 | 5 | €3,55 | €2,25 (5x) | **€1,30** | 0.03% | €-75,64 | €-74,34 | -1.49% |
| bitvavo - kraken | €5.000,00 | 2026-11-25 | 3.3 u | 3 | 3 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €2,71 | €2,71 | 0.05% |
| bitvavo - kucoin | €100,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,52 | €-0,52 | -0.52% |
| bitvavo - kucoin | €100,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,80 | €-1,80 | -1.80% |
| bitvavo - kucoin | €100,00 | 2026-11-21 | 22.9 u | 7 | 5 | 2 | €0,04 | €0,00 (0x) | **€0,04** | 0.04% | €0,78 | €0,82 | 0.82% |
| bitvavo - kucoin | €100,00 | 2026-11-22 | 22.1 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,45 | €0,45 | 0.45% |
| bitvavo - kucoin | €100,00 | 2026-11-23 | 19.7 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,05 | €0,05 | 0.05% |
| bitvavo - kucoin | €100,00 | 2026-11-24 | 19.5 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,60 | €-0,60 | -0.60% |
| bitvavo - kucoin | €100,00 | 2026-11-25 | 3.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,30 | €-0,30 | -0.30% |
| bitvavo - kucoin | €150,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,78 | €-0,78 | -0.52% |
| bitvavo - kucoin | €150,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,71 | €-2,71 | -1.80% |
| bitvavo - kucoin | €150,00 | 2026-11-21 | 22.9 u | 7 | 5 | 2 | €0,07 | €0,00 (0x) | **€0,07** | 0.04% | €1,17 | €1,23 | 0.82% |
| bitvavo - kucoin | €150,00 | 2026-11-22 | 22.1 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,68 | €0,68 | 0.45% |
| bitvavo - kucoin | €150,00 | 2026-11-23 | 19.7 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,08 | €0,08 | 0.05% |
| bitvavo - kucoin | €150,00 | 2026-11-24 | 19.5 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,90 | €-0,90 | -0.60% |
| bitvavo - kucoin | €150,00 | 2026-11-25 | 3.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,46 | €-0,46 | -0.30% |
| bitvavo - kucoin | €200,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,04 | €-1,04 | -0.52% |
| bitvavo - kucoin | €200,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,61 | €-3,61 | -1.80% |
| bitvavo - kucoin | €200,00 | 2026-11-21 | 22.9 u | 7 | 5 | 2 | €0,09 | €0,00 (0x) | **€0,09** | 0.04% | €1,56 | €1,65 | 0.82% |
| bitvavo - kucoin | €200,00 | 2026-11-22 | 22.1 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,91 | €0,91 | 0.45% |
| bitvavo - kucoin | €200,00 | 2026-11-23 | 19.7 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,10 | €0,10 | 0.05% |
| bitvavo - kucoin | €200,00 | 2026-11-24 | 19.5 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,20 | €-1,20 | -0.60% |
| bitvavo - kucoin | €200,00 | 2026-11-25 | 3.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,61 | €-0,61 | -0.30% |
| bitvavo - kucoin | €2.000,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-10,39 | €-10,39 | -0.52% |
| bitvavo - kucoin | €2.000,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-36,07 | €-36,07 | -1.80% |
| bitvavo - kucoin | €2.000,00 | 2026-11-21 | 22.9 u | 7 | 4 | 3 | €0,91 | €2,73 (3x) | **€-1,82** | -0.09% | €15,55 | €13,72 | 0.69% |
| bitvavo - kucoin | €2.000,00 | 2026-11-22 | 22.1 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €9,04 | €9,04 | 0.45% |
| bitvavo - kucoin | €2.000,00 | 2026-11-23 | 19.7 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €1,02 | €1,02 | 0.05% |
| bitvavo - kucoin | €2.000,00 | 2026-11-24 | 19.5 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-12,01 | €-12,01 | -0.60% |
| bitvavo - kucoin | €2.000,00 | 2026-11-25 | 3.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-6,08 | €-6,08 | -0.30% |
| bitvavo - kucoin | €5.000,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-25,99 | €-25,99 | -0.52% |
| bitvavo - kucoin | €5.000,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-90,18 | €-90,18 | -1.80% |
| bitvavo - kucoin | €5.000,00 | 2026-11-21 | 22.9 u | 7 | 4 | 3 | €2,24 | €2,73 (3x) | **€-0,49** | -0.01% | €38,94 | €38,45 | 0.77% |
| bitvavo - kucoin | €5.000,00 | 2026-11-22 | 22.1 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €22,63 | €22,63 | 0.45% |
| bitvavo - kucoin | €5.000,00 | 2026-11-23 | 19.7 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €2,55 | €2,55 | 0.05% |
| bitvavo - kucoin | €5.000,00 | 2026-11-24 | 19.5 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-30,06 | €-30,06 | -0.60% |
| bitvavo - kucoin | €5.000,00 | 2026-11-25 | 3.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-15,22 | €-15,22 | -0.30% |
| gate - kucoin | €100,00 | 2026-11-19 | 14.9 u | 25 | 25 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,29 | €-0,29 | -0.29% |
| gate - kucoin | €100,00 | 2026-11-20 | 22.8 u | 46 | 46 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,78 | €-0,78 | -0.78% |
| gate - kucoin | €100,00 | 2026-11-21 | 22.9 u | 46 | 46 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,74 | €-1,74 | -1.74% |
| gate - kucoin | €100,00 | 2026-11-22 | 22.1 u | 28 | 28 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,94 | €-1,94 | -1.94% |
| gate - kucoin | €100,00 | 2026-11-23 | 19.7 u | 32 | 32 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,34 | €-0,34 | -0.34% |
| gate - kucoin | €100,00 | 2026-11-24 | 19.5 u | 20 | 20 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,62 | €-0,62 | -0.62% |
| gate - kucoin | €100,00 | 2026-11-25 | 3.3 u | 2 | 2 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,25 | €0,25 | 0.25% |
| gate - kucoin | €150,00 | 2026-11-19 | 14.9 u | 25 | 25 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,44 | €-0,44 | -0.29% |
| gate - kucoin | €150,00 | 2026-11-20 | 22.8 u | 46 | 46 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,18 | €-1,18 | -0.78% |
| gate - kucoin | €150,00 | 2026-11-21 | 22.9 u | 46 | 46 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,61 | €-2,61 | -1.74% |
| gate - kucoin | €150,00 | 2026-11-22 | 22.1 u | 28 | 28 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,90 | €-2,90 | -1.94% |
| gate - kucoin | €150,00 | 2026-11-23 | 19.7 u | 32 | 32 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,50 | €-0,50 | -0.34% |
| gate - kucoin | €150,00 | 2026-11-24 | 19.5 u | 20 | 20 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,94 | €-0,94 | -0.62% |
| gate - kucoin | €150,00 | 2026-11-25 | 3.3 u | 2 | 2 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,38 | €0,38 | 0.25% |
| gate - kucoin | €200,00 | 2026-11-19 | 14.9 u | 25 | 25 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,58 | €-0,58 | -0.29% |
| gate - kucoin | €200,00 | 2026-11-20 | 22.8 u | 46 | 45 | 1 | €0,12 | €0,00 (0x) | **€0,12** | 0.06% | €-1,57 | €-1,45 | -0.73% |
| gate - kucoin | €200,00 | 2026-11-21 | 22.9 u | 46 | 46 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,48 | €-3,48 | -1.74% |
| gate - kucoin | €200,00 | 2026-11-22 | 22.1 u | 28 | 28 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,87 | €-3,87 | -1.94% |
| gate - kucoin | €200,00 | 2026-11-23 | 19.7 u | 32 | 32 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,67 | €-0,67 | -0.34% |
| gate - kucoin | €200,00 | 2026-11-24 | 19.5 u | 20 | 20 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,25 | €-1,25 | -0.62% |
| gate - kucoin | €200,00 | 2026-11-25 | 3.3 u | 2 | 2 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,51 | €0,51 | 0.25% |
| gate - kucoin | €2.000,00 | 2026-11-19 | 14.9 u | 25 | 17 | 8 | €0,83 | €0,00 (0x) | **€0,83** | 0.04% | €-5,84 | €-5,01 | -0.25% |
| gate - kucoin | €2.000,00 | 2026-11-20 | 22.8 u | 46 | 25 | 21 | €5,70 | €0,05 (3x) | **€5,65** | 0.28% | €-15,70 | €-10,05 | -0.50% |
| gate - kucoin | €2.000,00 | 2026-11-21 | 22.9 u | 46 | 34 | 12 | €3,04 | €0,01 (1x) | **€3,03** | 0.15% | €-34,78 | €-31,75 | -1.59% |
| gate - kucoin | €2.000,00 | 2026-11-22 | 22.1 u | 28 | 21 | 7 | €0,66 | €0,01 (2x) | **€0,64** | 0.03% | €-38,73 | €-38,09 | -1.90% |
| gate - kucoin | €2.000,00 | 2026-11-23 | 19.7 u | 32 | 26 | 6 | €0,91 | €0,10 (1x) | **€0,81** | 0.04% | €-6,71 | €-5,90 | -0.30% |
| gate - kucoin | €2.000,00 | 2026-11-24 | 19.5 u | 20 | 18 | 2 | €0,65 | €0,10 (1x) | **€0,55** | 0.03% | €-12,49 | €-11,94 | -0.60% |
| gate - kucoin | €2.000,00 | 2026-11-25 | 3.3 u | 2 | 2 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €5,10 | €5,10 | 0.26% |
| gate - kucoin | €5.000,00 | 2026-11-19 | 14.9 u | 25 | 10 | 15 | €2,82 | €2,11 (12x) | **€0,71** | 0.01% | €-14,59 | €-13,88 | -0.28% |
| gate - kucoin | €5.000,00 | 2026-11-20 | 22.8 u | 46 | 15 | 31 | €15,11 | €2,81 (19x) | **€12,30** | 0.25% | €-39,21 | €-26,91 | -0.54% |
| gate - kucoin | €5.000,00 | 2026-11-21 | 22.9 u | 46 | 15 | 31 | €10,46 | €3,50 (22x) | **€6,96** | 0.14% | €-86,96 | €-80,00 | -1.60% |
| gate - kucoin | €5.000,00 | 2026-11-22 | 22.1 u | 28 | 6 | 22 | €3,68 | €2,37 (17x) | **€1,31** | 0.03% | €-96,72 | €-95,40 | -1.91% |
| gate - kucoin | €5.000,00 | 2026-11-23 | 19.7 u | 32 | 14 | 18 | €4,11 | €2,11 (15x) | **€2,00** | 0.04% | €-17,01 | €-15,01 | -0.30% |
| gate - kucoin | €5.000,00 | 2026-11-24 | 19.5 u | 20 | 6 | 14 | €3,47 | €2,93 (14x) | **€0,54** | 0.01% | €-30,79 | €-30,24 | -0.60% |
| gate - kucoin | €5.000,00 | 2026-11-25 | 3.3 u | 2 | 0 | 2 | €0,15 | €0,32 (2x) | **€-0,17** | -0.00% | €12,72 | €12,55 | 0.25% |
| kraken - kucoin | €100,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,11 | €0,11 | 0.11% |
| kraken - kucoin | €100,00 | 2026-11-20 | 22.8 u | 15 | 13 | 2 | €0,03 | €0,01 (1x) | **€0,02** | 0.02% | €0,11 | €0,13 | 0.13% |
| kraken - kucoin | €100,00 | 2026-11-21 | 22.9 u | 12 | 12 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,16 | €-0,16 | -0.16% |
| kraken - kucoin | €100,00 | 2026-11-22 | 22.1 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,08 | €-0,08 | -0.08% |
| kraken - kucoin | €100,00 | 2026-11-23 | 19.7 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,29 | €0,29 | 0.29% |
| kraken - kucoin | €100,00 | 2026-11-24 | 19.5 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,25 | €-0,25 | -0.25% |
| kraken - kucoin | €100,00 | 2026-11-25 | 3.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,03 | €0,03 | 0.03% |
| kraken - kucoin | €150,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,16 | €0,16 | 0.11% |
| kraken - kucoin | €150,00 | 2026-11-20 | 22.8 u | 15 | 13 | 2 | €0,05 | €0,01 (1x) | **€0,04** | 0.02% | €0,16 | €0,20 | 0.13% |
| kraken - kucoin | €150,00 | 2026-11-21 | 22.9 u | 12 | 12 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,24 | €-0,24 | -0.16% |
| kraken - kucoin | €150,00 | 2026-11-22 | 22.1 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,12 | €-0,12 | -0.08% |
| kraken - kucoin | €150,00 | 2026-11-23 | 19.7 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,44 | €0,44 | 0.29% |
| kraken - kucoin | €150,00 | 2026-11-24 | 19.5 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,38 | €-0,38 | -0.25% |
| kraken - kucoin | €150,00 | 2026-11-25 | 3.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,05 | €0,05 | 0.03% |
| kraken - kucoin | €200,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,22 | €0,22 | 0.11% |
| kraken - kucoin | €200,00 | 2026-11-20 | 22.8 u | 15 | 13 | 2 | €0,06 | €0,24 (2x) | **€-0,18** | -0.09% | €0,22 | €0,04 | 0.02% |
| kraken - kucoin | €200,00 | 2026-11-21 | 22.9 u | 12 | 12 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,32 | €-0,32 | -0.16% |
| kraken - kucoin | €200,00 | 2026-11-22 | 22.1 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,16 | €-0,16 | -0.08% |
| kraken - kucoin | €200,00 | 2026-11-23 | 19.7 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,58 | €0,58 | 0.29% |
| kraken - kucoin | €200,00 | 2026-11-24 | 19.5 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,50 | €-0,50 | -0.25% |
| kraken - kucoin | €200,00 | 2026-11-25 | 3.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,06 | €0,06 | 0.03% |
| kraken - kucoin | €2.000,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €2,19 | €2,19 | 0.11% |
| kraken - kucoin | €2.000,00 | 2026-11-20 | 22.8 u | 15 | 13 | 2 | €0,61 | €1,24 (3x) | **€-0,63** | -0.03% | €2,19 | €1,56 | 0.08% |
| kraken - kucoin | €2.000,00 | 2026-11-21 | 22.9 u | 12 | 12 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,24 | €-3,24 | -0.16% |
| kraken - kucoin | €2.000,00 | 2026-11-22 | 22.1 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,59 | €-1,59 | -0.08% |
| kraken - kucoin | €2.000,00 | 2026-11-23 | 19.7 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €5,81 | €5,81 | 0.29% |
| kraken - kucoin | €2.000,00 | 2026-11-24 | 19.5 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-5,05 | €-5,05 | -0.25% |
| kraken - kucoin | €2.000,00 | 2026-11-25 | 3.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,60 | €0,60 | 0.03% |
| kraken - kucoin | €5.000,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €5,49 | €5,49 | 0.11% |
| kraken - kucoin | €5.000,00 | 2026-11-20 | 22.8 u | 15 | 13 | 2 | €1,53 | €1,24 (3x) | **€0,28** | 0.01% | €5,48 | €5,77 | 0.12% |
| kraken - kucoin | €5.000,00 | 2026-11-21 | 22.9 u | 12 | 12 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-8,09 | €-8,09 | -0.16% |
| kraken - kucoin | €5.000,00 | 2026-11-22 | 22.1 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,98 | €-3,98 | -0.08% |
| kraken - kucoin | €5.000,00 | 2026-11-23 | 19.7 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €14,53 | €14,53 | 0.29% |
| kraken - kucoin | €5.000,00 | 2026-11-24 | 19.5 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-12,61 | €-12,61 | -0.25% |
| kraken - kucoin | €5.000,00 | 2026-11-25 | 3.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €1,51 | €1,51 | 0.03% |

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
- bitvavo - kraken, €100,00: munten AERO, AVA, BABY, CVX, CYBER, DYM, GMT, KERNEL, LUNA, MERL, MLN, PROMPT, VELO, ZRC; bruto zonder voorraadgrens zou €5.565,18 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitvavo - kraken, €150,00: munten AERO, AVA, BABY, CVX, CYBER, DYM, GMT, KERNEL, LUNA, MERL, MLN, PROMPT, VELO, ZRC; bruto zonder voorraadgrens zou €5.565,18 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitvavo - kraken, €200,00: munten AERO, AVA, BABY, CVX, CYBER, DYM, GMT, KERNEL, LUNA, MERL, MLN, PROMPT, VELO, ZRC; bruto zonder voorraadgrens zou €5.565,18 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitvavo - kraken, €2.000,00: munten AERO, AVA, BABY, CVX, CYBER, DYM, GMT, KERNEL, LUNA, MERL, MLN, PROMPT, VELO, ZRC; bruto zonder voorraadgrens zou €5.550,05 zijn, met voorraad €21,15 (GEZIEN boek, GOK model).
- bitvavo - kraken, €5.000,00: munten AERO, AVA, BABY, CVX, CYBER, DYM, GMT, KERNEL, LUNA, MERL, MLN, PROMPT, VELO, ZRC; bruto zonder voorraadgrens zou €5.462,79 zijn, met voorraad €126,01 (GEZIEN boek, GOK model).
- bitvavo - kucoin, €100,00: munten ETH, USDC; bruto zonder voorraadgrens zou €19,28 zijn, met voorraad €0,04 (GEZIEN boek, GOK model).
- bitvavo - kucoin, €150,00: munten ETH, USDC; bruto zonder voorraadgrens zou €19,28 zijn, met voorraad €0,07 (GEZIEN boek, GOK model).
- bitvavo - kucoin, €200,00: munten ETH, USDC; bruto zonder voorraadgrens zou €19,28 zijn, met voorraad €0,09 (GEZIEN boek, GOK model).
- bitvavo - kucoin, €2.000,00: munten ETH, USDC; bruto zonder voorraadgrens zou €19,28 zijn, met voorraad €0,91 (GEZIEN boek, GOK model).
- bitvavo - kucoin, €5.000,00: munten ETH, USDC; bruto zonder voorraadgrens zou €19,28 zijn, met voorraad €2,24 (GEZIEN boek, GOK model).
- gate - kucoin, €100,00: munten ALKIMI, AVAIL, BARD, CAMP, CCD, CHR, CWEB, CYBER, DCR, DMTR, EDEN, ENSO, EPIC, ERG, ESPORTS, EVAA, FTT, HIGH, HTR, IKA, IR, JST, KAVA, KYO, LSK, LUNC, NAKA, NES, NIM, ON, OVR, POKT, POND, RARI, SD, SOUL, STREAM, SUPRA, USDS, USTC, VERONA, XU3O8; bruto zonder voorraadgrens zou €641,53 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- gate - kucoin, €150,00: munten ALKIMI, AVAIL, BARD, CAMP, CCD, CHR, CWEB, CYBER, DCR, DMTR, EDEN, ENSO, EPIC, ERG, ESPORTS, EVAA, FTT, HIGH, HTR, IKA, IR, JST, KAVA, KYO, LSK, LUNC, NAKA, NES, NIM, ON, OVR, POKT, POND, RARI, SD, SOUL, STREAM, SUPRA, USDS, USTC, VERONA, XU3O8; bruto zonder voorraadgrens zou €641,53 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- gate - kucoin, €200,00: munten ALKIMI, AVAIL, BARD, CAMP, CCD, CHR, CWEB, CYBER, DCR, DMTR, EDEN, ENSO, EPIC, ERG, ESPORTS, EVAA, FTT, HIGH, HTR, IKA, IR, JST, KAVA, KYO, LSK, LUNC, NAKA, NES, NIM, ON, OVR, POKT, POND, RARI, SD, SOUL, STREAM, SUPRA, USDS, USTC, VERONA, XU3O8; bruto zonder voorraadgrens zou €641,53 zijn, met voorraad €0,12 (GEZIEN boek, GOK model).
- gate - kucoin, €2.000,00: munten ALKIMI, AVAIL, BARD, CAMP, CCD, CHR, CWEB, CYBER, DCR, DMTR, EDEN, ENSO, EPIC, ERG, ESPORTS, EVAA, FTT, HIGH, HTR, IKA, IR, JST, KAVA, KYO, LSK, LUNC, NAKA, NES, NIM, ON, OVR, POKT, POND, RARI, SD, SOUL, STREAM, SUPRA, USDS, USTC, VERONA, XU3O8; bruto zonder voorraadgrens zou €640,52 zijn, met voorraad €11,79 (GEZIEN boek, GOK model).
- gate - kucoin, €5.000,00: munten ALKIMI, AVAIL, BARD, CAMP, CCD, CHR, CWEB, CYBER, DCR, DMTR, EDEN, ENSO, EPIC, ERG, ESPORTS, EVAA, FTT, HIGH, HTR, IKA, IR, JST, KAVA, KYO, LSK, LUNC, NAKA, NES, NIM, ON, OVR, POKT, POND, RARI, SD, SOUL, STREAM, SUPRA, USDS, USTC, VERONA, XU3O8; bruto zonder voorraadgrens zou €638,74 zijn, met voorraad €39,79 (GEZIEN boek, GOK model).
- kraken - kucoin, €100,00: munten USDC, USDT; bruto zonder voorraadgrens zou €120,83 zijn, met voorraad €0,03 (GEZIEN boek, GOK model).
- kraken - kucoin, €150,00: munten USDC, USDT; bruto zonder voorraadgrens zou €120,83 zijn, met voorraad €0,05 (GEZIEN boek, GOK model).
- kraken - kucoin, €200,00: munten USDC, USDT; bruto zonder voorraadgrens zou €120,82 zijn, met voorraad €0,06 (GEZIEN boek, GOK model).
- kraken - kucoin, €2.000,00: munten USDC, USDT; bruto zonder voorraadgrens zou €120,54 zijn, met voorraad €0,61 (GEZIEN boek, GOK model).
- kraken - kucoin, €5.000,00: munten USDC, USDT; bruto zonder voorraadgrens zou €120,08 zijn, met voorraad €1,53 (GEZIEN boek, GOK model).

### Met minstens één grijze beurs (de 5 paren met de meeste bruto winst)

| Beurspaar | Inleg | Dag | Gemeten | Kansen | Gemist (geen voorraad) | Kleiner door voorraad | Bruto winst | Kosten terugschuiven | **Netto handel (bruto min kosten)** | Rendement handel | Koerseffect voorraad | Netto met koerseffect | Rendement met koerseffect |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| htx - kucoin | €100,00 | 2026-11-19 | 14.9 u | 16 | 16 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,00 | €-1,00 | -1.00% |
| htx - kucoin | €100,00 | 2026-11-20 | 22.8 u | 42 | 42 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,81 | €-2,81 | -2.81% |
| htx - kucoin | €100,00 | 2026-11-21 | 22.9 u | 32 | 32 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,14 | €0,14 | 0.14% |
| htx - kucoin | €100,00 | 2026-11-22 | 22.1 u | 40 | 40 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,11 | €-0,11 | -0.11% |
| htx - kucoin | €100,00 | 2026-11-23 | 19.7 u | 15 | 15 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,79 | €0,79 | 0.79% |
| htx - kucoin | €100,00 | 2026-11-24 | 19.5 u | 43 | 43 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,65 | €-0,65 | -0.65% |
| htx - kucoin | €100,00 | 2026-11-25 | 3.3 u | 10 | 10 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,54 | €-0,54 | -0.54% |
| htx - kucoin | €150,00 | 2026-11-19 | 14.9 u | 16 | 16 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,50 | €-1,50 | -1.00% |
| htx - kucoin | €150,00 | 2026-11-20 | 22.8 u | 42 | 42 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-4,22 | €-4,22 | -2.81% |
| htx - kucoin | €150,00 | 2026-11-21 | 22.9 u | 32 | 32 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,21 | €0,21 | 0.14% |
| htx - kucoin | €150,00 | 2026-11-22 | 22.1 u | 40 | 40 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,17 | €-0,17 | -0.11% |
| htx - kucoin | €150,00 | 2026-11-23 | 19.7 u | 15 | 15 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €1,18 | €1,18 | 0.79% |
| htx - kucoin | €150,00 | 2026-11-24 | 19.5 u | 43 | 43 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,97 | €-0,97 | -0.65% |
| htx - kucoin | €150,00 | 2026-11-25 | 3.3 u | 10 | 10 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,81 | €-0,81 | -0.54% |
| htx - kucoin | €200,00 | 2026-11-19 | 14.9 u | 16 | 16 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,00 | €-2,00 | -1.00% |
| htx - kucoin | €200,00 | 2026-11-20 | 22.8 u | 42 | 42 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-5,63 | €-5,63 | -2.81% |
| htx - kucoin | €200,00 | 2026-11-21 | 22.9 u | 32 | 32 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,28 | €0,28 | 0.14% |
| htx - kucoin | €200,00 | 2026-11-22 | 22.1 u | 40 | 40 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,23 | €-0,23 | -0.11% |
| htx - kucoin | €200,00 | 2026-11-23 | 19.7 u | 15 | 15 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €1,57 | €1,57 | 0.79% |
| htx - kucoin | €200,00 | 2026-11-24 | 19.5 u | 43 | 43 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,30 | €-1,30 | -0.65% |
| htx - kucoin | €200,00 | 2026-11-25 | 3.3 u | 10 | 10 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,08 | €-1,08 | -0.54% |
| htx - kucoin | €2.000,00 | 2026-11-19 | 14.9 u | 16 | 16 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-20,00 | €-20,00 | -1.00% |
| htx - kucoin | €2.000,00 | 2026-11-20 | 22.8 u | 42 | 42 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-56,27 | €-56,27 | -2.81% |
| htx - kucoin | €2.000,00 | 2026-11-21 | 22.9 u | 32 | 32 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €2,75 | €2,75 | 0.14% |
| htx - kucoin | €2.000,00 | 2026-11-22 | 22.1 u | 40 | 40 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,28 | €-2,28 | -0.11% |
| htx - kucoin | €2.000,00 | 2026-11-23 | 19.7 u | 15 | 14 | 1 | €1,11 | €0,10 (1x) | **€1,01** | 0.05% | €15,74 | €16,75 | 0.84% |
| htx - kucoin | €2.000,00 | 2026-11-24 | 19.5 u | 43 | 42 | 1 | €0,05 | €0,00 (0x) | **€0,05** | 0.00% | €-12,97 | €-12,91 | -0.65% |
| htx - kucoin | €2.000,00 | 2026-11-25 | 3.3 u | 10 | 10 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-10,82 | €-10,82 | -0.54% |
| htx - kucoin | €5.000,00 | 2026-11-19 | 14.9 u | 16 | 9 | 7 | €1,24 | €0,00 (1x) | **€1,23** | 0.02% | €-50,01 | €-48,78 | -0.98% |
| htx - kucoin | €5.000,00 | 2026-11-20 | 22.8 u | 42 | 24 | 18 | €7,12 | €0,00 (1x) | **€7,12** | 0.14% | €-140,68 | €-133,56 | -2.67% |
| htx - kucoin | €5.000,00 | 2026-11-21 | 22.9 u | 32 | 13 | 19 | €2,41 | €0,11 (4x) | **€2,30** | 0.05% | €6,88 | €9,18 | 0.18% |
| htx - kucoin | €5.000,00 | 2026-11-22 | 22.1 u | 40 | 26 | 14 | €6,75 | €0,14 (3x) | **€6,61** | 0.13% | €-5,69 | €0,91 | 0.02% |
| htx - kucoin | €5.000,00 | 2026-11-23 | 19.7 u | 15 | 8 | 7 | €1,87 | €0,10 (1x) | **€1,77** | 0.04% | €39,28 | €41,06 | 0.82% |
| htx - kucoin | €5.000,00 | 2026-11-24 | 19.5 u | 43 | 36 | 7 | €1,37 | €0,17 (1x) | **€1,20** | 0.02% | €-32,41 | €-31,21 | -0.62% |
| htx - kucoin | €5.000,00 | 2026-11-25 | 3.3 u | 10 | 10 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-27,04 | €-27,04 | -0.54% |
| bitget - htx | €100,00 | 2026-11-19 | 14.9 u | 20 | 20 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €100,00 | 2026-11-20 | 22.8 u | 39 | 39 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €100,00 | 2026-11-21 | 22.9 u | 47 | 47 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €100,00 | 2026-11-22 | 22.1 u | 39 | 39 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €100,00 | 2026-11-23 | 19.7 u | 27 | 27 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €100,00 | 2026-11-24 | 19.5 u | 33 | 33 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €100,00 | 2026-11-25 | 3.3 u | 10 | 10 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €150,00 | 2026-11-19 | 14.9 u | 20 | 20 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €150,00 | 2026-11-20 | 22.8 u | 39 | 39 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €150,00 | 2026-11-21 | 22.9 u | 47 | 47 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €150,00 | 2026-11-22 | 22.1 u | 39 | 39 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €150,00 | 2026-11-23 | 19.7 u | 27 | 27 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €150,00 | 2026-11-24 | 19.5 u | 33 | 33 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €150,00 | 2026-11-25 | 3.3 u | 10 | 10 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €200,00 | 2026-11-19 | 14.9 u | 20 | 20 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €200,00 | 2026-11-20 | 22.8 u | 39 | 39 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €200,00 | 2026-11-21 | 22.9 u | 47 | 47 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €200,00 | 2026-11-22 | 22.1 u | 39 | 39 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €200,00 | 2026-11-23 | 19.7 u | 27 | 27 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €200,00 | 2026-11-24 | 19.5 u | 33 | 33 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €200,00 | 2026-11-25 | 3.3 u | 10 | 10 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €2.000,00 | 2026-11-19 | 14.9 u | 20 | 20 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €2.000,00 | 2026-11-20 | 22.8 u | 39 | 39 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €2.000,00 | 2026-11-21 | 22.9 u | 47 | 47 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €2.000,00 | 2026-11-22 | 22.1 u | 39 | 39 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €2.000,00 | 2026-11-23 | 19.7 u | 27 | 27 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €2.000,00 | 2026-11-24 | 19.5 u | 33 | 32 | 1 | €0,05 | €0,00 (0x) | **€0,05** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €2.000,00 | 2026-11-25 | 3.3 u | 10 | 10 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €5.000,00 | 2026-11-19 | 14.9 u | 20 | 6 | 14 | €1,23 | €0,70 (10x) | **€0,53** | 0.01% | onbekend | onbekend* | onbekend* |
| bitget - htx | €5.000,00 | 2026-11-20 | 22.8 u | 39 | 8 | 31 | €6,69 | €0,64 (26x) | **€6,05** | 0.12% | onbekend | onbekend* | onbekend* |
| bitget - htx | €5.000,00 | 2026-11-21 | 22.9 u | 47 | 8 | 39 | €3,77 | €1,59 (31x) | **€2,18** | 0.04% | onbekend | onbekend* | onbekend* |
| bitget - htx | €5.000,00 | 2026-11-22 | 22.1 u | 39 | 17 | 22 | €4,48 | €0,72 (16x) | **€3,77** | 0.08% | onbekend | onbekend* | onbekend* |
| bitget - htx | €5.000,00 | 2026-11-23 | 19.7 u | 27 | 10 | 17 | €1,99 | €0,84 (15x) | **€1,14** | 0.02% | onbekend | onbekend* | onbekend* |
| bitget - htx | €5.000,00 | 2026-11-24 | 19.5 u | 33 | 18 | 15 | €2,16 | €0,86 (13x) | **€1,30** | 0.03% | onbekend | onbekend* | onbekend* |
| bitget - htx | €5.000,00 | 2026-11-25 | 3.3 u | 10 | 8 | 2 | €0,12 | €0,08 (1x) | **€0,04** | 0.00% | onbekend | onbekend* | onbekend* |
| gate - htx | €100,00 | 2026-11-19 | 14.9 u | 19 | 19 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,82 | €-0,82 | -0.82% |
| gate - htx | €100,00 | 2026-11-20 | 22.8 u | 32 | 32 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,64 | €-2,64 | -2.64% |
| gate - htx | €100,00 | 2026-11-21 | 22.9 u | 36 | 36 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,09 | €0,09 | 0.09% |
| gate - htx | €100,00 | 2026-11-22 | 22.1 u | 35 | 35 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,67 | €-0,67 | -0.67% |
| gate - htx | €100,00 | 2026-11-23 | 19.7 u | 25 | 25 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,45 | €0,45 | 0.45% |
| gate - htx | €100,00 | 2026-11-24 | 19.5 u | 14 | 14 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,97 | €-0,97 | -0.97% |
| gate - htx | €100,00 | 2026-11-25 | 3.3 u | 3 | 3 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,22 | €-0,22 | -0.22% |
| gate - htx | €150,00 | 2026-11-19 | 14.9 u | 19 | 19 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,22 | €-1,22 | -0.82% |
| gate - htx | €150,00 | 2026-11-20 | 22.8 u | 32 | 32 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,95 | €-3,95 | -2.64% |
| gate - htx | €150,00 | 2026-11-21 | 22.9 u | 36 | 36 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,14 | €0,14 | 0.09% |
| gate - htx | €150,00 | 2026-11-22 | 22.1 u | 35 | 35 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,01 | €-1,01 | -0.67% |
| gate - htx | €150,00 | 2026-11-23 | 19.7 u | 25 | 25 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,67 | €0,67 | 0.45% |
| gate - htx | €150,00 | 2026-11-24 | 19.5 u | 14 | 14 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,46 | €-1,46 | -0.97% |
| gate - htx | €150,00 | 2026-11-25 | 3.3 u | 3 | 3 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,33 | €-0,33 | -0.22% |
| gate - htx | €200,00 | 2026-11-19 | 14.9 u | 19 | 19 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,63 | €-1,63 | -0.82% |
| gate - htx | €200,00 | 2026-11-20 | 22.8 u | 32 | 32 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-5,27 | €-5,27 | -2.64% |
| gate - htx | €200,00 | 2026-11-21 | 22.9 u | 36 | 36 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,19 | €0,19 | 0.09% |
| gate - htx | €200,00 | 2026-11-22 | 22.1 u | 35 | 35 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,34 | €-1,34 | -0.67% |
| gate - htx | €200,00 | 2026-11-23 | 19.7 u | 25 | 25 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,90 | €0,90 | 0.45% |
| gate - htx | €200,00 | 2026-11-24 | 19.5 u | 14 | 14 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,94 | €-1,94 | -0.97% |
| gate - htx | €200,00 | 2026-11-25 | 3.3 u | 3 | 3 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,44 | €-0,44 | -0.22% |
| gate - htx | €2.000,00 | 2026-11-19 | 14.9 u | 19 | 19 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-16,33 | €-16,33 | -0.82% |
| gate - htx | €2.000,00 | 2026-11-20 | 22.8 u | 32 | 32 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-52,72 | €-52,72 | -2.64% |
| gate - htx | €2.000,00 | 2026-11-21 | 22.9 u | 36 | 36 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €1,86 | €1,86 | 0.09% |
| gate - htx | €2.000,00 | 2026-11-22 | 22.1 u | 35 | 34 | 1 | €0,17 | €0,00 (0x) | **€0,17** | 0.01% | €-13,41 | €-13,24 | -0.66% |
| gate - htx | €2.000,00 | 2026-11-23 | 19.7 u | 25 | 25 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €8,96 | €8,96 | 0.45% |
| gate - htx | €2.000,00 | 2026-11-24 | 19.5 u | 14 | 14 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-19,42 | €-19,42 | -0.97% |
| gate - htx | €2.000,00 | 2026-11-25 | 3.3 u | 3 | 3 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-4,36 | €-4,36 | -0.22% |
| gate - htx | €5.000,00 | 2026-11-19 | 14.9 u | 19 | 14 | 5 | €0,91 | €0,17 (1x) | **€0,74** | 0.01% | €-40,83 | €-40,09 | -0.80% |
| gate - htx | €5.000,00 | 2026-11-20 | 22.8 u | 32 | 12 | 20 | €6,74 | €0,66 (8x) | **€6,08** | 0.12% | €-131,78 | €-125,70 | -2.51% |
| gate - htx | €5.000,00 | 2026-11-21 | 22.9 u | 36 | 13 | 23 | €4,59 | €1,00 (14x) | **€3,59** | 0.07% | €4,63 | €8,22 | 0.16% |
| gate - htx | €5.000,00 | 2026-11-22 | 22.1 u | 35 | 11 | 24 | €6,29 | €0,97 (18x) | **€5,31** | 0.11% | €-33,54 | €-28,22 | -0.56% |
| gate - htx | €5.000,00 | 2026-11-23 | 19.7 u | 25 | 17 | 8 | €2,79 | €0,40 (5x) | **€2,39** | 0.05% | €22,32 | €24,71 | 0.49% |
| gate - htx | €5.000,00 | 2026-11-24 | 19.5 u | 14 | 9 | 5 | €2,01 | €0,00 (1x) | **€2,01** | 0.04% | €-48,48 | €-46,47 | -0.93% |
| gate - htx | €5.000,00 | 2026-11-25 | 3.3 u | 3 | 1 | 2 | €0,81 | €0,01 (1x) | **€0,80** | 0.02% | €-10,88 | €-10,08 | -0.20% |
| bitget - kucoin | €100,00 | 2026-11-19 | 14.9 u | 21 | 21 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,41 | €-0,41 | -0.41% |
| bitget - kucoin | €100,00 | 2026-11-20 | 22.8 u | 24 | 24 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,47 | €-1,47 | -1.47% |
| bitget - kucoin | €100,00 | 2026-11-21 | 22.9 u | 39 | 39 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,13 | €-0,13 | -0.13% |
| bitget - kucoin | €100,00 | 2026-11-22 | 22.1 u | 49 | 49 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,30 | €-1,30 | -1.30% |
| bitget - kucoin | €100,00 | 2026-11-23 | 19.7 u | 46 | 46 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,07 | €-0,07 | -0.07% |
| bitget - kucoin | €100,00 | 2026-11-24 | 19.5 u | 63 | 63 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,22 | €0,22 | 0.22% |
| bitget - kucoin | €100,00 | 2026-11-25 | 3.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,53 | €-0,53 | -0.53% |
| bitget - kucoin | €150,00 | 2026-11-19 | 14.9 u | 21 | 21 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,62 | €-0,62 | -0.41% |
| bitget - kucoin | €150,00 | 2026-11-20 | 22.8 u | 24 | 24 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,20 | €-2,20 | -1.47% |
| bitget - kucoin | €150,00 | 2026-11-21 | 22.9 u | 39 | 39 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,20 | €-0,20 | -0.13% |
| bitget - kucoin | €150,00 | 2026-11-22 | 22.1 u | 49 | 49 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,95 | €-1,95 | -1.30% |
| bitget - kucoin | €150,00 | 2026-11-23 | 19.7 u | 46 | 46 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,10 | €-0,10 | -0.07% |
| bitget - kucoin | €150,00 | 2026-11-24 | 19.5 u | 63 | 63 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,33 | €0,33 | 0.22% |
| bitget - kucoin | €150,00 | 2026-11-25 | 3.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,80 | €-0,80 | -0.53% |
| bitget - kucoin | €200,00 | 2026-11-19 | 14.9 u | 21 | 21 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,83 | €-0,83 | -0.41% |
| bitget - kucoin | €200,00 | 2026-11-20 | 22.8 u | 24 | 24 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,93 | €-2,93 | -1.47% |
| bitget - kucoin | €200,00 | 2026-11-21 | 22.9 u | 39 | 39 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,27 | €-0,27 | -0.13% |
| bitget - kucoin | €200,00 | 2026-11-22 | 22.1 u | 49 | 49 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,60 | €-2,60 | -1.30% |
| bitget - kucoin | €200,00 | 2026-11-23 | 19.7 u | 46 | 46 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,14 | €-0,14 | -0.07% |
| bitget - kucoin | €200,00 | 2026-11-24 | 19.5 u | 63 | 63 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,44 | €0,44 | 0.22% |
| bitget - kucoin | €200,00 | 2026-11-25 | 3.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,06 | €-1,06 | -0.53% |
| bitget - kucoin | €2.000,00 | 2026-11-19 | 14.9 u | 21 | 14 | 7 | €0,50 | €0,00 (0x) | **€0,50** | 0.03% | €-8,26 | €-7,75 | -0.39% |
| bitget - kucoin | €2.000,00 | 2026-11-20 | 22.8 u | 24 | 14 | 10 | €1,60 | €0,00 (2x) | **€1,60** | 0.08% | €-29,30 | €-27,71 | -1.39% |
| bitget - kucoin | €2.000,00 | 2026-11-21 | 22.9 u | 39 | 25 | 14 | €0,58 | €0,57 (9x) | **€0,01** | 0.00% | €-2,69 | €-2,67 | -0.13% |
| bitget - kucoin | €2.000,00 | 2026-11-22 | 22.1 u | 49 | 37 | 12 | €0,52 | €1,62 (10x) | **€-1,10** | -0.05% | €-26,05 | €-27,15 | -1.36% |
| bitget - kucoin | €2.000,00 | 2026-11-23 | 19.7 u | 46 | 46 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,37 | €-1,37 | -0.07% |
| bitget - kucoin | €2.000,00 | 2026-11-24 | 19.5 u | 63 | 57 | 6 | €2,19 | €0,00 (0x) | **€2,19** | 0.11% | €4,37 | €6,56 | 0.33% |
| bitget - kucoin | €2.000,00 | 2026-11-25 | 3.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-10,59 | €-10,59 | -0.53% |
| bitget - kucoin | €5.000,00 | 2026-11-19 | 14.9 u | 21 | 8 | 13 | €3,07 | €2,26 (12x) | **€0,81** | 0.02% | €-20,63 | €-19,82 | -0.40% |
| bitget - kucoin | €5.000,00 | 2026-11-20 | 22.8 u | 24 | 6 | 18 | €6,24 | €1,79 (12x) | **€4,44** | 0.09% | €-73,16 | €-68,71 | -1.37% |
| bitget - kucoin | €5.000,00 | 2026-11-21 | 22.9 u | 39 | 12 | 27 | €4,32 | €2,96 (21x) | **€1,36** | 0.03% | €-6,54 | €-5,19 | -0.10% |
| bitget - kucoin | €5.000,00 | 2026-11-22 | 22.1 u | 49 | 39 | 10 | €1,70 | €1,39 (6x) | **€0,31** | 0.01% | €-65,00 | €-64,69 | -1.29% |
| bitget - kucoin | €5.000,00 | 2026-11-23 | 19.7 u | 46 | 36 | 10 | €0,69 | €1,00 (6x) | **€-0,32** | -0.01% | €-3,48 | €-3,79 | -0.08% |
| bitget - kucoin | €5.000,00 | 2026-11-24 | 19.5 u | 63 | 53 | 10 | €6,09 | €0,91 (5x) | **€5,17** | 0.10% | €11,00 | €16,17 | 0.32% |
| bitget - kucoin | €5.000,00 | 2026-11-25 | 3.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-26,42 | €-26,42 | -0.53% |
| htx - xt | €100,00 | 2026-11-19 | 14.9 u | 18 | 18 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,05 | €-1,05 | -1.05% |
| htx - xt | €100,00 | 2026-11-20 | 22.8 u | 17 | 17 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,70 | €-2,70 | -2.70% |
| htx - xt | €100,00 | 2026-11-21 | 22.9 u | 15 | 15 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,15 | €-0,15 | -0.15% |
| htx - xt | €100,00 | 2026-11-22 | 22.1 u | 15 | 15 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,56 | €-0,56 | -0.56% |
| htx - xt | €100,00 | 2026-11-23 | 19.7 u | 9 | 9 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,81 | €0,81 | 0.81% |
| htx - xt | €100,00 | 2026-11-24 | 19.5 u | 5 | 5 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,52 | €-0,52 | -0.52% |
| htx - xt | €100,00 | 2026-11-25 | 3.3 u | 1 | 1 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,48 | €-0,48 | -0.48% |
| htx - xt | €150,00 | 2026-11-19 | 14.9 u | 18 | 18 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,57 | €-1,57 | -1.05% |
| htx - xt | €150,00 | 2026-11-20 | 22.8 u | 17 | 17 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-4,05 | €-4,05 | -2.70% |
| htx - xt | €150,00 | 2026-11-21 | 22.9 u | 15 | 15 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,22 | €-0,22 | -0.15% |
| htx - xt | €150,00 | 2026-11-22 | 22.1 u | 15 | 15 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,83 | €-0,83 | -0.56% |
| htx - xt | €150,00 | 2026-11-23 | 19.7 u | 9 | 9 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €1,21 | €1,21 | 0.81% |
| htx - xt | €150,00 | 2026-11-24 | 19.5 u | 5 | 5 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,77 | €-0,77 | -0.52% |
| htx - xt | €150,00 | 2026-11-25 | 3.3 u | 1 | 1 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,72 | €-0,72 | -0.48% |
| htx - xt | €200,00 | 2026-11-19 | 14.9 u | 18 | 18 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,10 | €-2,10 | -1.05% |
| htx - xt | €200,00 | 2026-11-20 | 22.8 u | 17 | 17 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-5,40 | €-5,40 | -2.70% |
| htx - xt | €200,00 | 2026-11-21 | 22.9 u | 15 | 15 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,29 | €-0,29 | -0.15% |
| htx - xt | €200,00 | 2026-11-22 | 22.1 u | 15 | 15 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,11 | €-1,11 | -0.56% |
| htx - xt | €200,00 | 2026-11-23 | 19.7 u | 9 | 9 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €1,61 | €1,61 | 0.81% |
| htx - xt | €200,00 | 2026-11-24 | 19.5 u | 5 | 5 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,03 | €-1,03 | -0.52% |
| htx - xt | €200,00 | 2026-11-25 | 3.3 u | 1 | 1 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,96 | €-0,96 | -0.48% |
| htx - xt | €2.000,00 | 2026-11-19 | 14.9 u | 18 | 14 | 4 | €0,62 | €0,00 (0x) | **€0,62** | 0.03% | €-20,97 | €-20,35 | -1.02% |
| htx - xt | €2.000,00 | 2026-11-20 | 22.8 u | 17 | 9 | 8 | €3,71 | €0,12 (2x) | **€3,59** | 0.18% | €-53,94 | €-50,36 | -2.52% |
| htx - xt | €2.000,00 | 2026-11-21 | 22.9 u | 15 | 7 | 8 | €2,91 | €0,01 (1x) | **€2,90** | 0.14% | €-2,90 | €0,00 | 0.00% |
| htx - xt | €2.000,00 | 2026-11-22 | 22.1 u | 15 | 10 | 5 | €1,47 | €0,11 (1x) | **€1,36** | 0.07% | €-11,12 | €-9,76 | -0.49% |
| htx - xt | €2.000,00 | 2026-11-23 | 19.7 u | 9 | 6 | 3 | €0,51 | €0,00 (0x) | **€0,51** | 0.03% | €16,14 | €16,64 | 0.83% |
| htx - xt | €2.000,00 | 2026-11-24 | 19.5 u | 5 | 4 | 1 | €0,19 | €0,00 (0x) | **€0,19** | 0.01% | €-10,31 | €-10,12 | -0.51% |
| htx - xt | €2.000,00 | 2026-11-25 | 3.3 u | 1 | 1 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-9,62 | €-9,62 | -0.48% |
| htx - xt | €5.000,00 | 2026-11-19 | 14.9 u | 18 | 5 | 13 | €5,99 | €4,29 (11x) | **€1,69** | 0.03% | €-52,48 | €-50,78 | -1.02% |
| htx - xt | €5.000,00 | 2026-11-20 | 22.8 u | 17 | 2 | 15 | €13,28 | €2,81 (9x) | **€10,48** | 0.21% | €-134,57 | €-124,10 | -2.48% |
| htx - xt | €5.000,00 | 2026-11-21 | 22.9 u | 15 | 6 | 9 | €7,75 | €0,01 (1x) | **€7,74** | 0.15% | €-6,59 | €1,15 | 0.02% |
| htx - xt | €5.000,00 | 2026-11-22 | 22.1 u | 15 | 10 | 5 | €3,67 | €0,11 (1x) | **€3,56** | 0.07% | €-27,71 | €-24,15 | -0.48% |
| htx - xt | €5.000,00 | 2026-11-23 | 19.7 u | 9 | 6 | 3 | €1,27 | €0,27 (1x) | **€1,00** | 0.02% | €39,88 | €40,88 | 0.82% |
| htx - xt | €5.000,00 | 2026-11-24 | 19.5 u | 5 | 4 | 1 | €0,47 | €0,38 (1x) | **€0,09** | 0.00% | €-25,97 | €-25,88 | -0.52% |
| htx - xt | €5.000,00 | 2026-11-25 | 3.3 u | 1 | 1 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-24,05 | €-24,05 | -0.48% |

- htx - kucoin, €100,00: munten ACN, AI, ALGO, ANIME, APT, ATOM, BIO, BONK, BRISE, BSV, BTT, CAP, CELO, CFX, CHIP, CVX, DCR, DYDX, ELA, ENJ, ENS, ENSO, FET, JASMY, JST, KSM, LAT, LISTA, LTC, LUNA, LUNC, MAPO, MEME, MINA, MOVR, NES, NIGHT, NPC, ONE, PEOPLE, PUMP, QNT, RUNE, SAND, SD, SHIB, SOMI, SSV, TAO, TLOS, TRAC, USDS, USTC, VIRTUAL, WAN, WARD, WIN, WLD, XCH, XCN, XDC, XEC, XMR, XTZ, ZBCN; bruto zonder voorraadgrens zou €1.441,15 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - kucoin, €150,00: munten ACN, AI, ALGO, ANIME, APT, ATOM, BIO, BONK, BRISE, BSV, BTT, CAP, CELO, CFX, CHIP, CVX, DCR, DYDX, ELA, ENJ, ENS, ENSO, FET, JASMY, JST, KSM, LAT, LISTA, LTC, LUNA, LUNC, MAPO, MEME, MINA, MOVR, NES, NIGHT, NPC, ONE, PEOPLE, PUMP, QNT, RUNE, SAND, SD, SHIB, SOMI, SSV, TAO, TLOS, TRAC, USDS, USTC, VIRTUAL, WAN, WARD, WIN, WLD, XCH, XCN, XDC, XEC, XMR, XTZ, ZBCN; bruto zonder voorraadgrens zou €1.441,15 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - kucoin, €200,00: munten ACN, AI, ALGO, ANIME, APT, ATOM, BIO, BONK, BRISE, BSV, BTT, CAP, CELO, CFX, CHIP, CVX, DCR, DYDX, ELA, ENJ, ENS, ENSO, FET, JASMY, JST, KSM, LAT, LISTA, LTC, LUNA, LUNC, MAPO, MEME, MINA, MOVR, NES, NIGHT, NPC, ONE, PEOPLE, PUMP, QNT, RUNE, SAND, SD, SHIB, SOMI, SSV, TAO, TLOS, TRAC, USDS, USTC, VIRTUAL, WAN, WARD, WIN, WLD, XCH, XCN, XDC, XEC, XMR, XTZ, ZBCN; bruto zonder voorraadgrens zou €1.441,15 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - kucoin, €2.000,00: munten ACN, AI, ALGO, ANIME, APT, ATOM, BIO, BONK, BRISE, BSV, BTT, CAP, CELO, CFX, CHIP, CVX, DCR, DYDX, ELA, ENJ, ENS, ENSO, FET, JASMY, JST, KSM, LAT, LISTA, LTC, LUNA, LUNC, MAPO, MEME, MINA, MOVR, NES, NIGHT, NPC, ONE, PEOPLE, PUMP, QNT, RUNE, SAND, SD, SHIB, SOMI, SSV, TAO, TLOS, TRAC, USDS, USTC, VIRTUAL, WAN, WARD, WIN, WLD, XCH, XCN, XDC, XEC, XMR, XTZ, ZBCN; bruto zonder voorraadgrens zou €1.441,15 zijn, met voorraad €1,17 (GEZIEN boek, GOK model).
- htx - kucoin, €5.000,00: munten ACN, AI, ALGO, ANIME, APT, ATOM, BIO, BONK, BRISE, BSV, BTT, CAP, CELO, CFX, CHIP, CVX, DCR, DYDX, ELA, ENJ, ENS, ENSO, FET, JASMY, JST, KSM, LAT, LISTA, LTC, LUNA, LUNC, MAPO, MEME, MINA, MOVR, NES, NIGHT, NPC, ONE, PEOPLE, PUMP, QNT, RUNE, SAND, SD, SHIB, SOMI, SSV, TAO, TLOS, TRAC, USDS, USTC, VIRTUAL, WAN, WARD, WIN, WLD, XCH, XCN, XDC, XEC, XMR, XTZ, ZBCN; bruto zonder voorraadgrens zou €1.440,46 zijn, met voorraad €20,76 (GEZIEN boek, GOK model).
- bitget - htx, €100,00: munten AB, ACN, AI, ALGO, ANIME, ATOM, BABY, BIO, BONK, BSV, BTT, CBK, CFX, CORE, DYDX, ENA, ENJ, ENS, ENSO, GALA, HBAR, HIVE, INJ, IOST, JASMY, JOE, KAITO, KAS, KSM, LAT, LINK, LISTA, LIT, LUNA, LUNC, M, MANTA, MAPO, MEME, MINA, MOVR, NES, NPC, O, PCI, PEOPLE, PONS, PUFFER, PUMP, QNT, RIVER, S, SAND, SHIB, SNEK, SOMI, SSV, TAO, TIA, TLOS, USTC, VIRTUAL, WARD, WLD, XDC, XTZ, ZEN; bruto zonder voorraadgrens zou €1.411,10 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - htx, €150,00: munten AB, ACN, AI, ALGO, ANIME, ATOM, BABY, BIO, BONK, BSV, BTT, CBK, CFX, CORE, DYDX, ENA, ENJ, ENS, ENSO, GALA, HBAR, HIVE, INJ, IOST, JASMY, JOE, KAITO, KAS, KSM, LAT, LINK, LISTA, LIT, LUNA, LUNC, M, MANTA, MAPO, MEME, MINA, MOVR, NES, NPC, O, PCI, PEOPLE, PONS, PUFFER, PUMP, QNT, RIVER, S, SAND, SHIB, SNEK, SOMI, SSV, TAO, TIA, TLOS, USTC, VIRTUAL, WARD, WLD, XDC, XTZ, ZEN; bruto zonder voorraadgrens zou €1.411,10 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - htx, €200,00: munten AB, ACN, AI, ALGO, ANIME, ATOM, BABY, BIO, BONK, BSV, BTT, CBK, CFX, CORE, DYDX, ENA, ENJ, ENS, ENSO, GALA, HBAR, HIVE, INJ, IOST, JASMY, JOE, KAITO, KAS, KSM, LAT, LINK, LISTA, LIT, LUNA, LUNC, M, MANTA, MAPO, MEME, MINA, MOVR, NES, NPC, O, PCI, PEOPLE, PONS, PUFFER, PUMP, QNT, RIVER, S, SAND, SHIB, SNEK, SOMI, SSV, TAO, TIA, TLOS, USTC, VIRTUAL, WARD, WLD, XDC, XTZ, ZEN; bruto zonder voorraadgrens zou €1.411,10 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - htx, €2.000,00: munten AB, ACN, AI, ALGO, ANIME, ATOM, BABY, BIO, BONK, BSV, BTT, CBK, CFX, CORE, DYDX, ENA, ENJ, ENS, ENSO, GALA, HBAR, HIVE, INJ, IOST, JASMY, JOE, KAITO, KAS, KSM, LAT, LINK, LISTA, LIT, LUNA, LUNC, M, MANTA, MAPO, MEME, MINA, MOVR, NES, NPC, O, PCI, PEOPLE, PONS, PUFFER, PUMP, QNT, RIVER, S, SAND, SHIB, SNEK, SOMI, SSV, TAO, TIA, TLOS, USTC, VIRTUAL, WARD, WLD, XDC, XTZ, ZEN; bruto zonder voorraadgrens zou €1.411,10 zijn, met voorraad €0,05 (GEZIEN boek, GOK model).
- bitget - htx, €5.000,00: munten AB, ACN, AI, ALGO, ANIME, ATOM, BABY, BIO, BONK, BSV, BTT, CBK, CFX, CORE, DYDX, ENA, ENJ, ENS, ENSO, GALA, HBAR, HIVE, INJ, IOST, JASMY, JOE, KAITO, KAS, KSM, LAT, LINK, LISTA, LIT, LUNA, LUNC, M, MANTA, MAPO, MEME, MINA, MOVR, NES, NPC, O, PCI, PEOPLE, PONS, PUFFER, PUMP, QNT, RIVER, S, SAND, SHIB, SNEK, SOMI, SSV, TAO, TIA, TLOS, USTC, VIRTUAL, WARD, WLD, XDC, XTZ, ZEN; bruto zonder voorraadgrens zou €1.410,48 zijn, met voorraad €20,44 (GEZIEN boek, GOK model).
- gate - htx, €100,00: munten AKT, ALGO, APEPE, APT, ATOM, BIO, BRISE, BSV, BTT, CBK, CELO, CORE, CRTS, CVX, DKA, ENJ, ENS, ENSO, GOMINING, GT, HBAR, HIVE, INJ, KAS, KCT, KSM, LAT, LINK, LUNA, LUNC, M, MBX, MEGA, MEME, MOVR, NES, NPC, PENGU, PEOPLE, PYR, QNT, SAND, SC, SD, SEI, SHIB, SOMI, SSV, TLOS, ULTIMA, VIRTUAL, WARD, WLD, XCH, XCN, XDC, ZBCN; bruto zonder voorraadgrens zou €863,79 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- gate - htx, €150,00: munten AKT, ALGO, APEPE, APT, ATOM, BIO, BRISE, BSV, BTT, CBK, CELO, CORE, CRTS, CVX, DKA, ENJ, ENS, ENSO, GOMINING, GT, HBAR, HIVE, INJ, KAS, KCT, KSM, LAT, LINK, LUNA, LUNC, M, MBX, MEGA, MEME, MOVR, NES, NPC, PENGU, PEOPLE, PYR, QNT, SAND, SC, SD, SEI, SHIB, SOMI, SSV, TLOS, ULTIMA, VIRTUAL, WARD, WLD, XCH, XCN, XDC, ZBCN; bruto zonder voorraadgrens zou €863,79 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- gate - htx, €200,00: munten AKT, ALGO, APEPE, APT, ATOM, BIO, BRISE, BSV, BTT, CBK, CELO, CORE, CRTS, CVX, DKA, ENJ, ENS, ENSO, GOMINING, GT, HBAR, HIVE, INJ, KAS, KCT, KSM, LAT, LINK, LUNA, LUNC, M, MBX, MEGA, MEME, MOVR, NES, NPC, PENGU, PEOPLE, PYR, QNT, SAND, SC, SD, SEI, SHIB, SOMI, SSV, TLOS, ULTIMA, VIRTUAL, WARD, WLD, XCH, XCN, XDC, ZBCN; bruto zonder voorraadgrens zou €863,79 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- gate - htx, €2.000,00: munten AKT, ALGO, APEPE, APT, ATOM, BIO, BRISE, BSV, BTT, CBK, CELO, CORE, CRTS, CVX, DKA, ENJ, ENS, ENSO, GOMINING, GT, HBAR, HIVE, INJ, KAS, KCT, KSM, LAT, LINK, LUNA, LUNC, M, MBX, MEGA, MEME, MOVR, NES, NPC, PENGU, PEOPLE, PYR, QNT, SAND, SC, SD, SEI, SHIB, SOMI, SSV, TLOS, ULTIMA, VIRTUAL, WARD, WLD, XCH, XCN, XDC, ZBCN; bruto zonder voorraadgrens zou €863,79 zijn, met voorraad €0,17 (GEZIEN boek, GOK model).
- gate - htx, €5.000,00: munten AKT, ALGO, APEPE, APT, ATOM, BIO, BRISE, BSV, BTT, CBK, CELO, CORE, CRTS, CVX, DKA, ENJ, ENS, ENSO, GOMINING, GT, HBAR, HIVE, INJ, KAS, KCT, KSM, LAT, LINK, LUNA, LUNC, M, MBX, MEGA, MEME, MOVR, NES, NPC, PENGU, PEOPLE, PYR, QNT, SAND, SC, SD, SEI, SHIB, SOMI, SSV, TLOS, ULTIMA, VIRTUAL, WARD, WLD, XCH, XCN, XDC, ZBCN; bruto zonder voorraadgrens zou €863,13 zijn, met voorraad €24,14 (GEZIEN boek, GOK model).
- bitget - kucoin, €100,00: munten ACE, BARD, BTC, CARV, CHR, DMC, EDEN, EGL1, ENJ, ENSO, ETH, HMSTR, HYPER, IOST, IR, JST, KAVA, KLV, KNC, LAT, LISTA, LUNC, MASK, MHA, MTX, NES, NOM, PROVE, PYUSD, SNEK, TAC, TLOS, USDC, USDT, USTC, VERONA; bruto zonder voorraadgrens zou €636,46 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - kucoin, €150,00: munten ACE, BARD, BTC, CARV, CHR, DMC, EDEN, EGL1, ENJ, ENSO, ETH, HMSTR, HYPER, IOST, IR, JST, KAVA, KLV, KNC, LAT, LISTA, LUNC, MASK, MHA, MTX, NES, NOM, PROVE, PYUSD, SNEK, TAC, TLOS, USDC, USDT, USTC, VERONA; bruto zonder voorraadgrens zou €636,46 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - kucoin, €200,00: munten ACE, BARD, BTC, CARV, CHR, DMC, EDEN, EGL1, ENJ, ENSO, ETH, HMSTR, HYPER, IOST, IR, JST, KAVA, KLV, KNC, LAT, LISTA, LUNC, MASK, MHA, MTX, NES, NOM, PROVE, PYUSD, SNEK, TAC, TLOS, USDC, USDT, USTC, VERONA; bruto zonder voorraadgrens zou €636,46 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - kucoin, €2.000,00: munten ACE, BARD, BTC, CARV, CHR, DMC, EDEN, EGL1, ENJ, ENSO, ETH, HMSTR, HYPER, IOST, IR, JST, KAVA, KLV, KNC, LAT, LISTA, LUNC, MASK, MHA, MTX, NES, NOM, PROVE, PYUSD, SNEK, TAC, TLOS, USDC, USDT, USTC, VERONA; bruto zonder voorraadgrens zou €636,09 zijn, met voorraad €5,39 (GEZIEN boek, GOK model).
- bitget - kucoin, €5.000,00: munten ACE, BARD, BTC, CARV, CHR, DMC, EDEN, EGL1, ENJ, ENSO, ETH, HMSTR, HYPER, IOST, IR, JST, KAVA, KLV, KNC, LAT, LISTA, LUNC, MASK, MHA, MTX, NES, NOM, PROVE, PYUSD, SNEK, TAC, TLOS, USDC, USDT, USTC, VERONA; bruto zonder voorraadgrens zou €634,55 zijn, met voorraad €22,10 (GEZIEN boek, GOK model).
- htx - xt, €100,00: munten ALGO, APEPE, APT, BIO, BSV, CARV, CBK, CELO, CFX, GT, HBAR, KSM, LUNA, LUNC, MEME, MINA, PENGU, PEOPLE, RAIN, SC, SEI, SHIB, SOMI, TLOS, XCH, XDC, XMR; bruto zonder voorraadgrens zou €914,40 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - xt, €150,00: munten ALGO, APEPE, APT, BIO, BSV, CARV, CBK, CELO, CFX, GT, HBAR, KSM, LUNA, LUNC, MEME, MINA, PENGU, PEOPLE, RAIN, SC, SEI, SHIB, SOMI, TLOS, XCH, XDC, XMR; bruto zonder voorraadgrens zou €914,40 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - xt, €200,00: munten ALGO, APEPE, APT, BIO, BSV, CARV, CBK, CELO, CFX, GT, HBAR, KSM, LUNA, LUNC, MEME, MINA, PENGU, PEOPLE, RAIN, SC, SEI, SHIB, SOMI, TLOS, XCH, XDC, XMR; bruto zonder voorraadgrens zou €914,40 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - xt, €2.000,00: munten ALGO, APEPE, APT, BIO, BSV, CARV, CBK, CELO, CFX, GT, HBAR, KSM, LUNA, LUNC, MEME, MINA, PENGU, PEOPLE, RAIN, SC, SEI, SHIB, SOMI, TLOS, XCH, XDC, XMR; bruto zonder voorraadgrens zou €914,19 zijn, met voorraad €9,40 (GEZIEN boek, GOK model).
- htx - xt, €5.000,00: munten ALGO, APEPE, APT, BIO, BSV, CARV, CBK, CELO, CFX, GT, HBAR, KSM, LUNA, LUNC, MEME, MINA, PENGU, PEOPLE, RAIN, SC, SEI, SHIB, SOMI, TLOS, XCH, XDC, XMR; bruto zonder voorraadgrens zou €912,92 zijn, met voorraad €32,42 (GEZIEN boek, GOK model).

### Andere keuzes bij bitvavo - kraken (netto handel, alle dagen samen; GOK)

| Keuze | Inleg | Kansen | Gemist | Bruto winst | Kosten terugschuiven | Netto handel |
|---|---|---|---|---|---|---|
| standaard (schuifdrempel 25%, kostengrens 1%) | €150,00 | 183 | 183 | €0,00 | €0,00 | **€0,00** |
| standaard (schuifdrempel 25%, kostengrens 1%) | €2.000,00 | 183 | 152 | €21,15 | €8,92 | **€12,24** |
| schuifdrempel 10% | €150,00 | 183 | 183 | €0,00 | €0,00 | **€0,00** |
| schuifdrempel 10% | €2.000,00 | 183 | 153 | €19,96 | €8,62 | **€11,34** |
| schuifdrempel 40% | €150,00 | 183 | 183 | €0,00 | €0,00 | **€0,00** |
| schuifdrempel 40% | €2.000,00 | 183 | 152 | €21,15 | €9,92 | **€11,24** |
| kostengrens 2% (achteraf vergeleken) | €150,00 | 183 | 183 | €0,00 | €0,00 | **€0,00** |
| kostengrens 2% (achteraf vergeleken) | €2.000,00 | 183 | 112 | €48,53 | €25,51 | **€23,02** |
| kostengrens 5% (achteraf vergeleken) | €150,00 | 183 | 183 | €0,00 | €0,00 | **€0,00** |
| kostengrens 5% (achteraf vergeleken) | €2.000,00 | 183 | 79 | €51,96 | €66,04 | **€-14,08** |
| alleen MERL en GMT (meer voorraad per munt, achteraf gekozen) | €150,00 | 152 | 150 | €0,19 | €0,00 | **€0,19** |
| alleen MERL en GMT (meer voorraad per munt, achteraf gekozen) | €2.000,00 | 152 | 52 | €272,42 | €97,67 | **€174,75** |

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

- Opnamekosten bij de echte kansen: 565 van een netwerk dat aan beide kanten open is, 387 van de beurs zelf (laagste open netwerk), 194 geschat uit wat andere beurzen voor die munt vragen (GOK). Onbekende opnamekosten tellen niet als echte kans.
- Netwerk: KuCoin, Gate, Bitget, HTX, XT, Bitstamp, Bitvavo en Poloniex geven hun netwerken per munt. Als beide beurzen dat doen en de namen te koppelen zijn, moet er een netwerk zijn dat aan beide kanten open is. Anders is het netwerk "niet te koppelen" en telt de kans mee (staat apart in de trechter).
- De duur is gemeten in stappen van ±20 seconden; een kans kan een paar rondes eerder begonnen zijn dan we zagen.
- Takerkosten: uit de API waar die ze per paar geeft, anders het standaardtarief uit de README (deels GOK).
- Laatste run: 15 beurzen antwoordden, 2277 munt-quote-paren op minstens twee beurzen (GEZIEN).
