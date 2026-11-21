# Rapport koersverschil-scanner

Gemaakt 2026-11-21 13:32 UTC uit 23 runs, samen ±50.5 uur gemeten (GEZIEN).
Echte kans = winst na alle kosten (opnamekosten bekend), opnemen en storten open (en een netwerk dat aan beide kanten open is, als de beurzen dat geven), minstens €100,00 op het boek, minstens 2 minuten blijven staan, geen andere munt met dezelfde naam.
**Vergund** = beide beurzen hebben een MiCA-vergunning (ESMA-register), vaak via een EU-dochter die minder munten kan hebben dan de wereldwijde API die we meten (GOK). **Grijs** = minstens één beurs zonder vergunning (MEXC, Bitget, HTX, Poloniex, XT, Bitfinex, Binance). Zie README.md.
**Kraken-tarief:** Kraken rekent 0,80% taker op munt tegen EUR, USD, USDT of USDC (GEZIEN, kraken.com/pro/fees, laagste trede); de scanner rekende tot 19 nov met 0,40%. 399 opgeslagen kansen met Kraken uit die runs zijn hier **opnieuw doorgerekend met 0,80%** (GOK-benadering: 0,40% van de inzet aan de Kraken-kant extra op elk gemeten punt van het boek; het boek zelf is niet bewaard). 233 houden daarna nog winst op het boek. Dat ze met hogere kosten ook korter bleven staan, telt niet mee (dus eerder te gunstig).

## Hoeveel wordt er gecontroleerd? (GEZIEN, stand.jsonl)

Per ronde (mediaan over 606 metingen): 1154 kandidaten (verschil op de ticker groter dan de takerkosten), 120 met het orderboek gecontroleerd, 2 nog nooit gecontroleerd (0%).
Bijna alle kandidaten komen aan de beurt; de aantallen hieronder missen weinig.

## Trechter (GEZIEN, eigen metingen)

| Stap | Alle beurzen | Alleen MiCA-beurzen | Met minstens één grijze beurs |
|---|---|---|---|
| Verschillen met winst op het boek na alle kosten | 49212 | 6564 | 42648 |
| ...waarvan opnemen of storten dicht | 8393 | 916 | 7477 |
| ...waarvan status onbekend (beurs geeft het niet openbaar) | 30515 | 4670 | 25845 |
| Opnemen en storten open | 10304 | 978 | 9326 |
| ...en geen netwerk dat aan beide kanten open is: valt af | 208 | 19 | 189 |
| ...en opnamekosten onbekend: valt af | 4 | 4 | 0 |
| ...en minstens €100,00 op het boek | 3033 | 613 | 2420 |
| ...en minstens 2 minuten blijven staan | 836 | 235 | 601 |
| ...en geen andere munt met dezelfde naam | 789 | 213 | 576 |
|    ...waarvan contractadres bekend en gelijk | 109 | 43 | 66 |
|    ...waarvan contractadres onbekend (telt mee, kan een andere munt zijn) | 680 | 170 | 510 |
|    ...waarvan netwerk gekoppeld en open | 518 | 109 | 409 |
|    ...waarvan netwerk niet te koppelen (telt mee) | 271 | 104 | 167 |
| **Echte kansen** (zelfde munt overlappend in de tijd samengevoegd, beste beurspaar telt) | 473 | 203 | 343 |
| Ter vergelijking: zelfde eisen, maar opnamestatus onbekend (niet meegeteld) | 1907 | 404 | 1645 |

## Echte kansen per dag (GEZIEN)

| Dag | Echt, alleen MiCA | Echt, met grijs | Mediane winst per kans bij €500 (MiCA / grijs) | Mediane duur |
|---|---|---|---|---|
| 2026-11-19 | 49 | 86 | €2,00 / €1,21 | 5.3 min |
| 2026-11-20 | 53 | 138 | €1,01 / €1,13 | 6.7 min |
| 2026-11-21 | 44 | 103 | €1,12 / €0,96 | 5.3 min |
| Totaal | 146 | 327 | €1,28 / €1,10 | 5.9 min |

## Beste munten (GEZIEN)

| | Soort | Kansen | Som winst bij €500 per kans |
|---|---|---|---|
| MERL-EUR | vergund | 28 | €820,61 |
| LUNC-USDT | grijs | 15 | €87,98 |
| USTC-USDT | grijs en vergund | 19 | €63,03 |
| KERNEL-EUR | vergund | 1 | €47,33 |
| MEME-USDT | grijs | 1 | €37,90 |
| ENSO-USDT | grijs en vergund | 10 | €37,15 |
| BSV-USDT | grijs | 21 | €33,53 |
| KYO-USDT | vergund | 5 | €30,94 |
| BARD-USDT | grijs | 4 | €24,39 |
| SHIB-USDT | grijs | 8 | €22,78 |

## Beste beursparen (kopen op > verkopen op) (GEZIEN)

| | Soort | Kansen | Som winst bij €500 per kans |
|---|---|---|---|
| bitvavo > kraken | vergund | 68 | €920,88 |
| bitget > htx | grijs | 73 | €144,89 |
| gate > kucoin | vergund | 33 | €93,02 |
| kucoin > htx | grijs | 38 | €88,52 |
| kucoin > bitget | grijs | 25 | €68,62 |
| bitget > xt | grijs | 16 | €52,05 |
| bitget > gate | grijs | 17 | €42,95 |
| gate > htx | grijs | 21 | €39,42 |
| bitget > kucoin | grijs | 25 | €37,90 |
| kucoin > gate | vergund | 26 | €36,84 |

Beurzen die het vaakst meedoen (koop of verkoop): bitget (grijs) 200, kucoin 193, htx (grijs) 173, gate 118, kraken 104, bitvavo 72, xt (grijs) 48, poloniex (grijs) 35 (GEZIEN).

## Hoeveel kansen blijven staan terwijl je geld schuift? (GEZIEN, duur uit eigen metingen)

Wie geen voorraad op beide beurzen heeft, moet kopen, de munt opnemen, wachten tot hij binnen is en dan verkopen. Hoe lang dat duurt verschilt per munt en netwerk: een paar minuten (snelle ketens) tot een uur of meer (Bitcoin, beurzen die opnames met de hand keuren) (GOK, niet per munt gemeten).

| Overmaaktijd | Alle beurzen | Alleen MiCA-beurzen | Met minstens één grijze beurs |
|---|---|---|---|
| 5 min | 269 van 473 (57%) | 112 van 203 (55%) | 204 van 343 (59%) |
| 10 min | 167 van 473 (35%) | 76 van 203 (37%) | 126 van 343 (37%) |
| 30 min | 83 van 473 (18%) | 43 van 203 (21%) | 65 van 343 (19%) |
| 60 min | 48 van 473 (10%) | 32 van 203 (16%) | 37 van 343 (11%) |

## Wat zou het opleveren over 3 maanden? (GOK, doorgetrokken uit de metingen)

Gemeten over ±50.5 uur (GEZIEN), doorgetrokken naar 90 dagen (GOK: aanname dat de week die we maten gewoon is).

| Beurzen | Inleg | Model | Kansen per uur | Per kans (mediaan) | 3 maanden |
|---|---|---|---|---|---|
| Alleen MiCA | €2.000,00 | bovengrens: elke kans, geld overal tegelijk | 4.02 | €1,58 | €13.723,54 |
| Alleen MiCA | €2.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 1.35 | €3,72 | €71.104,01 |
| Alleen MiCA | €5.000,00 | bovengrens: elke kans, geld overal tegelijk | 4.02 | €2,12 | €18.385,16 |
| Alleen MiCA | €5.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 1.35 | €4,40 | €136.637,94 |
| Alle (met grijs) | €2.000,00 | bovengrens: elke kans, geld overal tegelijk | 9.37 | €1,49 | €30.175,99 |
| Alle (met grijs) | €2.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 1.35 | €3,72 | €71.104,01 |
| Alle (met grijs) | €5.000,00 | bovengrens: elke kans, geld overal tegelijk | 9.37 | €1,69 | €34.232,23 |
| Alle (met grijs) | €5.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 1.35 | €4,40 | €136.637,94 |

Bovengrens: elke kans met de helft van de inleg aan elke kant, alsof het geld op alle beurzen tegelijk staat (kan in het echt niet). Beste beurspaar: het paar is **achteraf** gekozen uit de metingen (vooraf kiezen levert minder op), en het model neemt aan dat je van elke munt al voorraad op de verkoopbeurs hebt.

Waarom dit te rooskleurig is (GOK): elke kans wordt maar één keer geteld met het mediane boek, maar andere bots pakken hem ook; de munt die je als voorraad aanhoudt kan dalen; na een paar kansen moet de voorraad terug (opnamekosten en tijd); minimale opname- en ordergroottes tellen niet mee; en een kans die we 2 minuten zagen staan, staat er niet per se nog als jouw order binnenkomt. Waarom het te somber kan zijn: niet alle kandidaten zijn gecontroleerd, en met voorraad op beide beurzen kun je dezelfde kans vaker pakken als het boek zich aanvult; dat telt hier niet mee.

## Wat houd je echt over? Voorraad op twee beurzen (simulatie)

Per beurspaar: geld en munten op beide beurzen, elke echte kans uitgevoerd tegen het boek zoals gemeten (niet meer dan de ruimte op het boek en niet meer dan de voorraad op die beurs), terugschuiven als een kant leeg dreigt te raken (met opnamekosten en tijd onderweg), en het koerseffect van de aangehouden munten apart. Netto = bruto min kosten terugschuiven plus koerseffect. **Gemeten** (GEZIEN): de kansen, het boek en de koersen; **de rest is een rekenmodel** (GOK, aannames onder de tabel). Geen advies.

**Met €150: netto €0,52 per dag op bitstamp - kraken (koerseffect erbovenop €-1,82), €0,01 per dag op bitstamp - kucoin (koerseffect erbovenop €0,07), €0,00 per dag op bitvavo - kraken (koerseffect erbovenop €-2,01), €0,02 per dag op bitvavo - kucoin (koerseffect erbovenop €-0,82), €0,04 per dag op gate - kucoin (koerseffect erbovenop €-1,72), €0,01 per dag op kraken - kucoin (koerseffect erbovenop €0,07) (GOK: netto handel, rekenmodel op ±16.8 uur meting per dag, alleen MiCA).** "Per dag" is hier gemiddeld over 3 gemeten dagen achter elkaar; de eerste begint met een gelijk verdeelde voorraad; aan het eind staat de voorraad scheef, dus een volgende dag levert waarschijnlijk minder op, tenzij kansen de andere kant op hem terugbrengen (GOK).

### Alleen MiCA-beurzen (alle paren met echte kansen)

| Beurspaar | Inleg | Dag | Gemeten | Kansen | Gemist (geen voorraad) | Kleiner door voorraad | Bruto winst | Kosten terugschuiven | **Netto handel (bruto min kosten)** | Rendement handel | Koerseffect voorraad | Netto met koerseffect | Rendement met koerseffect |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| bitstamp - kraken | €100,00 | 2026-11-19 | 14.9 u | 2 | 1 | 1 | €0,59 | €0,00 (0x) | **€0,59** | 0.59% | €-0,02 | €0,57 | 0.57% |
| bitstamp - kraken | €100,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,95 | €-2,95 | -2.95% |
| bitstamp - kraken | €100,00 | 2026-11-21 | 12.8 u | 1 | 0 | 1 | €0,45 | €0,00 (0x) | **€0,45** | 0.45% | €-0,67 | €-0,22 | -0.22% |
| bitstamp - kraken | €150,00 | 2026-11-19 | 14.9 u | 2 | 1 | 1 | €0,89 | €0,00 (0x) | **€0,89** | 0.59% | €-0,03 | €0,85 | 0.57% |
| bitstamp - kraken | €150,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-4,43 | €-4,43 | -2.95% |
| bitstamp - kraken | €150,00 | 2026-11-21 | 12.8 u | 1 | 0 | 1 | €0,67 | €0,00 (0x) | **€0,67** | 0.45% | €-1,00 | €-0,33 | -0.22% |
| bitstamp - kraken | €200,00 | 2026-11-19 | 14.9 u | 2 | 1 | 1 | €1,18 | €0,00 (0x) | **€1,18** | 0.59% | €-0,04 | €1,14 | 0.57% |
| bitstamp - kraken | €200,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-5,91 | €-5,91 | -2.95% |
| bitstamp - kraken | €200,00 | 2026-11-21 | 12.8 u | 1 | 0 | 1 | €0,89 | €0,00 (0x) | **€0,89** | 0.45% | €-1,34 | €-0,44 | -0.22% |
| bitstamp - kraken | €2.000,00 | 2026-11-19 | 14.9 u | 2 | 1 | 0 | €11,71 | €0,98 (1x) | **€10,73** | 0.54% | €-0,46 | €10,27 | 0.51% |
| bitstamp - kraken | €2.000,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-59,03 | €-59,03 | -2.95% |
| bitstamp - kraken | €2.000,00 | 2026-11-21 | 12.8 u | 1 | 0 | 0 | €5,30 | €0,00 (0x) | **€5,30** | 0.26% | €-13,38 | €-8,09 | -0.40% |
| bitstamp - kraken | €5.000,00 | 2026-11-19 | 14.9 u | 2 | 1 | 0 | €11,71 | €0,00 (0x) | **€11,71** | 0.23% | €-1,10 | €10,60 | 0.21% |
| bitstamp - kraken | €5.000,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-147,75 | €-147,75 | -2.95% |
| bitstamp - kraken | €5.000,00 | 2026-11-21 | 12.8 u | 1 | 0 | 0 | €5,30 | €0,00 (0x) | **€5,30** | 0.11% | €-33,45 | €-28,15 | -0.56% |
| bitstamp - kucoin | €100,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,11 | €0,11 | 0.11% |
| bitstamp - kucoin | €100,00 | 2026-11-20 | 22.8 u | 1 | 0 | 1 | €0,00 | €0,01 (1x) | **€-0,01** | -0.01% | €0,11 | €0,10 | 0.10% |
| bitstamp - kucoin | €100,00 | 2026-11-21 | 12.8 u | 6 | 5 | 1 | €0,01 | €0,00 (0x) | **€0,01** | 0.01% | €-0,09 | €-0,07 | -0.07% |
| bitstamp - kucoin | €150,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,16 | €0,16 | 0.11% |
| bitstamp - kucoin | €150,00 | 2026-11-20 | 22.8 u | 1 | 0 | 1 | €0,00 | €0,01 (1x) | **€-0,01** | -0.00% | €0,16 | €0,16 | 0.11% |
| bitstamp - kucoin | €150,00 | 2026-11-21 | 12.8 u | 6 | 5 | 1 | €0,02 | €0,00 (0x) | **€0,02** | 0.01% | €-0,13 | €-0,11 | -0.07% |
| bitstamp - kucoin | €200,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,22 | €0,22 | 0.11% |
| bitstamp - kucoin | €200,00 | 2026-11-20 | 22.8 u | 1 | 0 | 1 | €0,01 | €0,01 (1x) | **€-0,00** | -0.00% | €0,22 | €0,22 | 0.11% |
| bitstamp - kucoin | €200,00 | 2026-11-21 | 12.8 u | 6 | 5 | 1 | €0,03 | €0,23 (1x) | **€-0,21** | -0.10% | €-0,17 | €-0,38 | -0.19% |
| bitstamp - kucoin | €2.000,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €2,19 | €2,19 | 0.11% |
| bitstamp - kucoin | €2.000,00 | 2026-11-20 | 22.8 u | 1 | 0 | 1 | €0,05 | €0,01 (1x) | **€0,04** | 0.00% | €2,19 | €2,24 | 0.11% |
| bitstamp - kucoin | €2.000,00 | 2026-11-21 | 12.8 u | 6 | 5 | 1 | €0,27 | €1,23 (2x) | **€-0,97** | -0.05% | €-1,75 | €-2,72 | -0.14% |
| bitstamp - kucoin | €5.000,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €5,49 | €5,49 | 0.11% |
| bitstamp - kucoin | €5.000,00 | 2026-11-20 | 22.8 u | 1 | 0 | 1 | €0,13 | €0,01 (1x) | **€0,12** | 0.00% | €5,48 | €5,60 | 0.11% |
| bitstamp - kucoin | €5.000,00 | 2026-11-21 | 12.8 u | 6 | 5 | 1 | €0,64 | €1,23 (2x) | **€-0,59** | -0.01% | €-4,39 | €-4,98 | -0.10% |
| bitvavo - kraken | €100,00 | 2026-11-19 | 14.9 u | 43 | 43 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,83 | €-0,83 | -0.83% |
| bitvavo - kraken | €100,00 | 2026-11-20 | 22.8 u | 15 | 15 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,35 | €-2,35 | -2.35% |
| bitvavo - kraken | €100,00 | 2026-11-21 | 12.8 u | 10 | 10 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,85 | €-0,85 | -0.85% |
| bitvavo - kraken | €150,00 | 2026-11-19 | 14.9 u | 43 | 43 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,25 | €-1,25 | -0.83% |
| bitvavo - kraken | €150,00 | 2026-11-20 | 22.8 u | 15 | 15 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,52 | €-3,52 | -2.35% |
| bitvavo - kraken | €150,00 | 2026-11-21 | 12.8 u | 10 | 10 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,27 | €-1,27 | -0.85% |
| bitvavo - kraken | €200,00 | 2026-11-19 | 14.9 u | 43 | 38 | 5 | €0,12 | €0,00 (0x) | **€0,12** | 0.06% | €-1,67 | €-1,55 | -0.77% |
| bitvavo - kraken | €200,00 | 2026-11-20 | 22.8 u | 15 | 14 | 1 | €0,90 | €0,00 (0x) | **€0,90** | 0.45% | €-4,70 | €-3,80 | -1.90% |
| bitvavo - kraken | €200,00 | 2026-11-21 | 12.8 u | 10 | 10 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,69 | €-1,69 | -0.85% |
| bitvavo - kraken | €2.000,00 | 2026-11-19 | 14.9 u | 43 | 25 | 18 | €12,03 | €7,02 (18x) | **€5,02** | 0.25% | €-16,59 | €-11,57 | -0.58% |
| bitvavo - kraken | €2.000,00 | 2026-11-20 | 22.8 u | 15 | 9 | 6 | €23,49 | €2,29 (5x) | **€21,19** | 1.06% | €-46,68 | €-25,49 | -1.27% |
| bitvavo - kraken | €2.000,00 | 2026-11-21 | 12.8 u | 10 | 5 | 5 | €21,53 | €1,71 (5x) | **€19,83** | 0.99% | €-16,99 | €2,84 | 0.14% |
| bitvavo - kraken | €5.000,00 | 2026-11-19 | 14.9 u | 43 | 20 | 23 | €26,34 | €16,24 (26x) | **€10,10** | 0.20% | €-41,54 | €-31,43 | -0.63% |
| bitvavo - kraken | €5.000,00 | 2026-11-20 | 22.8 u | 15 | 2 | 13 | €61,31 | €12,31 (15x) | **€49,00** | 0.98% | €-116,07 | €-67,08 | -1.34% |
| bitvavo - kraken | €5.000,00 | 2026-11-21 | 12.8 u | 10 | 5 | 5 | €55,36 | €1,71 (5x) | **€53,66** | 1.07% | €-42,05 | €11,61 | 0.23% |
| bitvavo - kucoin | €100,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,52 | €-0,52 | -0.52% |
| bitvavo - kucoin | €100,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,80 | €-1,80 | -1.80% |
| bitvavo - kucoin | €100,00 | 2026-11-21 | 12.8 u | 7 | 5 | 2 | €0,04 | €0,00 (0x) | **€0,04** | 0.04% | €0,68 | €0,72 | 0.72% |
| bitvavo - kucoin | €150,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,78 | €-0,78 | -0.52% |
| bitvavo - kucoin | €150,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,71 | €-2,71 | -1.80% |
| bitvavo - kucoin | €150,00 | 2026-11-21 | 12.8 u | 7 | 5 | 2 | €0,07 | €0,00 (0x) | **€0,07** | 0.04% | €1,02 | €1,09 | 0.72% |
| bitvavo - kucoin | €200,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,04 | €-1,04 | -0.52% |
| bitvavo - kucoin | €200,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,61 | €-3,61 | -1.80% |
| bitvavo - kucoin | €200,00 | 2026-11-21 | 12.8 u | 7 | 5 | 2 | €0,09 | €0,00 (0x) | **€0,09** | 0.04% | €1,36 | €1,45 | 0.72% |
| bitvavo - kucoin | €2.000,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-10,39 | €-10,39 | -0.52% |
| bitvavo - kucoin | €2.000,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-36,07 | €-36,07 | -1.80% |
| bitvavo - kucoin | €2.000,00 | 2026-11-21 | 12.8 u | 7 | 4 | 3 | €0,91 | €2,73 (3x) | **€-1,82** | -0.09% | €13,58 | €11,76 | 0.59% |
| bitvavo - kucoin | €5.000,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-25,99 | €-25,99 | -0.52% |
| bitvavo - kucoin | €5.000,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-90,18 | €-90,18 | -1.80% |
| bitvavo - kucoin | €5.000,00 | 2026-11-21 | 12.8 u | 7 | 4 | 3 | €2,24 | €2,73 (3x) | **€-0,49** | -0.01% | €34,02 | €33,53 | 0.67% |
| gate - kucoin | €100,00 | 2026-11-19 | 14.9 u | 25 | 25 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,84 | €-0,84 | -0.84% |
| gate - kucoin | €100,00 | 2026-11-20 | 22.8 u | 46 | 46 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,50 | €-0,50 | -0.50% |
| gate - kucoin | €100,00 | 2026-11-21 | 12.8 u | 30 | 30 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,10 | €-2,10 | -2.10% |
| gate - kucoin | €150,00 | 2026-11-19 | 14.9 u | 25 | 25 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,25 | €-1,25 | -0.84% |
| gate - kucoin | €150,00 | 2026-11-20 | 22.8 u | 46 | 45 | 1 | €0,12 | €0,00 (0x) | **€0,12** | 0.08% | €-0,76 | €-0,63 | -0.42% |
| gate - kucoin | €150,00 | 2026-11-21 | 12.8 u | 30 | 30 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,15 | €-3,15 | -2.10% |
| gate - kucoin | €200,00 | 2026-11-19 | 14.9 u | 25 | 25 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,67 | €-1,67 | -0.84% |
| gate - kucoin | €200,00 | 2026-11-20 | 22.8 u | 46 | 44 | 2 | €0,13 | €0,00 (1x) | **€0,13** | 0.06% | €-1,01 | €-0,88 | -0.44% |
| gate - kucoin | €200,00 | 2026-11-21 | 12.8 u | 30 | 30 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-4,20 | €-4,20 | -2.10% |
| gate - kucoin | €2.000,00 | 2026-11-19 | 14.9 u | 25 | 12 | 13 | €1,44 | €1,10 (7x) | **€0,34** | 0.02% | €-16,68 | €-16,34 | -0.82% |
| gate - kucoin | €2.000,00 | 2026-11-20 | 22.8 u | 46 | 24 | 22 | €7,58 | €0,59 (7x) | **€6,99** | 0.35% | €-10,04 | €-3,05 | -0.15% |
| gate - kucoin | €2.000,00 | 2026-11-21 | 12.8 u | 30 | 18 | 12 | €4,29 | €0,28 (3x) | **€4,01** | 0.20% | €-41,92 | €-37,91 | -1.90% |
| gate - kucoin | €5.000,00 | 2026-11-19 | 14.9 u | 25 | 6 | 19 | €6,15 | €3,83 (17x) | **€2,32** | 0.05% | €-41,78 | €-39,46 | -0.79% |
| gate - kucoin | €5.000,00 | 2026-11-20 | 22.8 u | 46 | 10 | 36 | €23,73 | €4,62 (25x) | **€19,11** | 0.38% | €-25,09 | €-5,98 | -0.12% |
| gate - kucoin | €5.000,00 | 2026-11-21 | 12.8 u | 30 | 7 | 23 | €12,96 | €3,13 (16x) | **€9,83** | 0.20% | €-104,63 | €-94,80 | -1.90% |
| kraken - kucoin | €100,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,11 | €0,11 | 0.11% |
| kraken - kucoin | €100,00 | 2026-11-20 | 22.8 u | 15 | 13 | 2 | €0,03 | €0,01 (1x) | **€0,02** | 0.02% | €0,11 | €0,13 | 0.13% |
| kraken - kucoin | €100,00 | 2026-11-21 | 12.8 u | 12 | 12 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,09 | €-0,09 | -0.09% |
| kraken - kucoin | €150,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,16 | €0,16 | 0.11% |
| kraken - kucoin | €150,00 | 2026-11-20 | 22.8 u | 15 | 13 | 2 | €0,05 | €0,01 (1x) | **€0,04** | 0.02% | €0,16 | €0,20 | 0.13% |
| kraken - kucoin | €150,00 | 2026-11-21 | 12.8 u | 12 | 12 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,13 | €-0,13 | -0.09% |
| kraken - kucoin | €200,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,22 | €0,22 | 0.11% |
| kraken - kucoin | €200,00 | 2026-11-20 | 22.8 u | 15 | 13 | 2 | €0,06 | €0,24 (2x) | **€-0,18** | -0.09% | €0,22 | €0,04 | 0.02% |
| kraken - kucoin | €200,00 | 2026-11-21 | 12.8 u | 12 | 12 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,18 | €-0,18 | -0.09% |
| kraken - kucoin | €2.000,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €2,19 | €2,19 | 0.11% |
| kraken - kucoin | €2.000,00 | 2026-11-20 | 22.8 u | 15 | 13 | 2 | €0,61 | €1,24 (3x) | **€-0,63** | -0.03% | €2,19 | €1,56 | 0.08% |
| kraken - kucoin | €2.000,00 | 2026-11-21 | 12.8 u | 12 | 12 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,76 | €-1,76 | -0.09% |
| kraken - kucoin | €5.000,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €5,49 | €5,49 | 0.11% |
| kraken - kucoin | €5.000,00 | 2026-11-20 | 22.8 u | 15 | 13 | 2 | €1,53 | €1,24 (3x) | **€0,28** | 0.01% | €5,48 | €5,77 | 0.12% |
| kraken - kucoin | €5.000,00 | 2026-11-21 | 12.8 u | 12 | 12 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-4,39 | €-4,39 | -0.09% |

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
- bitvavo - kraken, €100,00: munten AVA, CVX, DYM, GMT, KERNEL, LUNA, MERL, PROMPT, VELO; bruto zonder voorraadgrens zou €4.795,82 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitvavo - kraken, €150,00: munten AVA, CVX, DYM, GMT, KERNEL, LUNA, MERL, PROMPT, VELO; bruto zonder voorraadgrens zou €4.795,82 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitvavo - kraken, €200,00: munten AVA, CVX, DYM, GMT, KERNEL, LUNA, MERL, PROMPT, VELO; bruto zonder voorraadgrens zou €4.795,46 zijn, met voorraad €1,02 (GEZIEN boek, GOK model).
- bitvavo - kraken, €2.000,00: munten AVA, CVX, DYM, GMT, KERNEL, LUNA, MERL, PROMPT, VELO; bruto zonder voorraadgrens zou €4.741,39 zijn, met voorraad €57,05 (GEZIEN boek, GOK model).
- bitvavo - kraken, €5.000,00: munten AVA, CVX, DYM, GMT, KERNEL, LUNA, MERL, PROMPT, VELO; bruto zonder voorraadgrens zou €4.665,33 zijn, met voorraad €143,01 (GEZIEN boek, GOK model).
- bitvavo - kucoin, €100,00: munten ETH, USDC; bruto zonder voorraadgrens zou €19,28 zijn, met voorraad €0,04 (GEZIEN boek, GOK model).
- bitvavo - kucoin, €150,00: munten ETH, USDC; bruto zonder voorraadgrens zou €19,28 zijn, met voorraad €0,07 (GEZIEN boek, GOK model).
- bitvavo - kucoin, €200,00: munten ETH, USDC; bruto zonder voorraadgrens zou €19,28 zijn, met voorraad €0,09 (GEZIEN boek, GOK model).
- bitvavo - kucoin, €2.000,00: munten ETH, USDC; bruto zonder voorraadgrens zou €19,28 zijn, met voorraad €0,91 (GEZIEN boek, GOK model).
- bitvavo - kucoin, €5.000,00: munten ETH, USDC; bruto zonder voorraadgrens zou €19,28 zijn, met voorraad €2,24 (GEZIEN boek, GOK model).
- gate - kucoin, €100,00: munten ALKIMI, AVAIL, BARD, CCD, CHR, CWEB, CYBER, EDEN, ENSO, ERG, FTT, HIGH, HTR, IKA, IR, JST, KYO, LUNC, NAKA, NIM, OVR, POKT, RARI, SOUL, STREAM, SUPRA, USDS, USTC, VERONA, XU3O8; bruto zonder voorraadgrens zou €371,33 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- gate - kucoin, €150,00: munten ALKIMI, AVAIL, BARD, CCD, CHR, CWEB, CYBER, EDEN, ENSO, ERG, FTT, HIGH, HTR, IKA, IR, JST, KYO, LUNC, NAKA, NIM, OVR, POKT, RARI, SOUL, STREAM, SUPRA, USDS, USTC, VERONA, XU3O8; bruto zonder voorraadgrens zou €371,33 zijn, met voorraad €0,12 (GEZIEN boek, GOK model).
- gate - kucoin, €200,00: munten ALKIMI, AVAIL, BARD, CCD, CHR, CWEB, CYBER, EDEN, ENSO, ERG, FTT, HIGH, HTR, IKA, IR, JST, KYO, LUNC, NAKA, NIM, OVR, POKT, RARI, SOUL, STREAM, SUPRA, USDS, USTC, VERONA, XU3O8; bruto zonder voorraadgrens zou €371,31 zijn, met voorraad €0,13 (GEZIEN boek, GOK model).
- gate - kucoin, €2.000,00: munten ALKIMI, AVAIL, BARD, CCD, CHR, CWEB, CYBER, EDEN, ENSO, ERG, FTT, HIGH, HTR, IKA, IR, JST, KYO, LUNC, NAKA, NIM, OVR, POKT, RARI, SOUL, STREAM, SUPRA, USDS, USTC, VERONA, XU3O8; bruto zonder voorraadgrens zou €369,92 zijn, met voorraad €13,32 (GEZIEN boek, GOK model).
- gate - kucoin, €5.000,00: munten ALKIMI, AVAIL, BARD, CCD, CHR, CWEB, CYBER, EDEN, ENSO, ERG, FTT, HIGH, HTR, IKA, IR, JST, KYO, LUNC, NAKA, NIM, OVR, POKT, RARI, SOUL, STREAM, SUPRA, USDS, USTC, VERONA, XU3O8; bruto zonder voorraadgrens zou €366,26 zijn, met voorraad €42,85 (GEZIEN boek, GOK model).
- kraken - kucoin, €100,00: munten USDC, USDT; bruto zonder voorraadgrens zou €120,83 zijn, met voorraad €0,03 (GEZIEN boek, GOK model).
- kraken - kucoin, €150,00: munten USDC, USDT; bruto zonder voorraadgrens zou €120,83 zijn, met voorraad €0,05 (GEZIEN boek, GOK model).
- kraken - kucoin, €200,00: munten USDC, USDT; bruto zonder voorraadgrens zou €120,82 zijn, met voorraad €0,06 (GEZIEN boek, GOK model).
- kraken - kucoin, €2.000,00: munten USDC, USDT; bruto zonder voorraadgrens zou €120,54 zijn, met voorraad €0,61 (GEZIEN boek, GOK model).
- kraken - kucoin, €5.000,00: munten USDC, USDT; bruto zonder voorraadgrens zou €120,08 zijn, met voorraad €1,53 (GEZIEN boek, GOK model).

### Met minstens één grijze beurs (de 5 paren met de meeste bruto winst)

| Beurspaar | Inleg | Dag | Gemeten | Kansen | Gemist (geen voorraad) | Kleiner door voorraad | Bruto winst | Kosten terugschuiven | **Netto handel (bruto min kosten)** | Rendement handel | Koerseffect voorraad | Netto met koerseffect | Rendement met koerseffect |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| htx - xt | €100,00 | 2026-11-19 | 14.9 u | 18 | 18 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,05 | €-1,05 | -1.05% |
| htx - xt | €100,00 | 2026-11-20 | 22.8 u | 17 | 17 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,64 | €-2,64 | -2.64% |
| htx - xt | €100,00 | 2026-11-21 | 12.8 u | 10 | 10 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,95 | €-0,95 | -0.95% |
| htx - xt | €150,00 | 2026-11-19 | 14.9 u | 18 | 18 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,57 | €-1,57 | -1.05% |
| htx - xt | €150,00 | 2026-11-20 | 22.8 u | 17 | 17 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,96 | €-3,96 | -2.64% |
| htx - xt | €150,00 | 2026-11-21 | 12.8 u | 10 | 10 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,42 | €-1,42 | -0.95% |
| htx - xt | €200,00 | 2026-11-19 | 14.9 u | 18 | 18 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,10 | €-2,10 | -1.05% |
| htx - xt | €200,00 | 2026-11-20 | 22.8 u | 17 | 17 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-5,28 | €-5,28 | -2.64% |
| htx - xt | €200,00 | 2026-11-21 | 12.8 u | 10 | 10 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,89 | €-1,89 | -0.95% |
| htx - xt | €2.000,00 | 2026-11-19 | 14.9 u | 18 | 14 | 4 | €0,99 | €0,00 (0x) | **€0,99** | 0.05% | €-20,99 | €-20,00 | -1.00% |
| htx - xt | €2.000,00 | 2026-11-20 | 22.8 u | 17 | 9 | 8 | €5,89 | €0,12 (2x) | **€5,77** | 0.29% | €-52,77 | €-47,01 | -2.35% |
| htx - xt | €2.000,00 | 2026-11-21 | 12.8 u | 10 | 3 | 7 | €4,48 | €0,01 (1x) | **€4,47** | 0.22% | €-18,90 | €-14,42 | -0.72% |
| htx - xt | €5.000,00 | 2026-11-19 | 14.9 u | 18 | 5 | 13 | €9,58 | €4,34 (11x) | **€5,24** | 0.10% | €-52,52 | €-47,29 | -0.95% |
| htx - xt | €5.000,00 | 2026-11-20 | 22.8 u | 17 | 2 | 15 | €21,24 | €2,84 (9x) | **€18,40** | 0.37% | €-131,65 | €-113,25 | -2.26% |
| htx - xt | €5.000,00 | 2026-11-21 | 12.8 u | 10 | 2 | 8 | €11,63 | €0,86 (3x) | **€10,77** | 0.22% | €-46,73 | €-35,96 | -0.72% |
| gate - htx | €100,00 | 2026-11-19 | 14.9 u | 19 | 19 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,17 | €-1,17 | -1.17% |
| gate - htx | €100,00 | 2026-11-20 | 22.8 u | 32 | 32 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,91 | €-2,91 | -2.91% |
| gate - htx | €100,00 | 2026-11-21 | 12.8 u | 24 | 24 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,72 | €-0,72 | -0.72% |
| gate - htx | €150,00 | 2026-11-19 | 14.9 u | 19 | 19 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,76 | €-1,76 | -1.17% |
| gate - htx | €150,00 | 2026-11-20 | 22.8 u | 32 | 32 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-4,36 | €-4,36 | -2.91% |
| gate - htx | €150,00 | 2026-11-21 | 12.8 u | 24 | 24 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,08 | €-1,08 | -0.72% |
| gate - htx | €200,00 | 2026-11-19 | 14.9 u | 19 | 19 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,35 | €-2,35 | -1.17% |
| gate - htx | €200,00 | 2026-11-20 | 22.8 u | 32 | 32 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-5,82 | €-5,82 | -2.91% |
| gate - htx | €200,00 | 2026-11-21 | 12.8 u | 24 | 24 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,45 | €-1,45 | -0.72% |
| gate - htx | €2.000,00 | 2026-11-19 | 14.9 u | 19 | 14 | 5 | €0,65 | €0,00 (0x) | **€0,65** | 0.03% | €-23,46 | €-22,81 | -1.14% |
| gate - htx | €2.000,00 | 2026-11-20 | 22.8 u | 32 | 12 | 20 | €4,80 | €0,66 (8x) | **€4,14** | 0.21% | €-58,15 | €-54,01 | -2.70% |
| gate - htx | €2.000,00 | 2026-11-21 | 12.8 u | 24 | 10 | 14 | €2,40 | €1,27 (6x) | **€1,14** | 0.06% | €-14,46 | €-13,32 | -0.67% |
| gate - htx | €5.000,00 | 2026-11-19 | 14.9 u | 19 | 7 | 12 | €5,13 | €3,17 (9x) | **€1,97** | 0.04% | €-58,68 | €-56,72 | -1.13% |
| gate - htx | €5.000,00 | 2026-11-20 | 22.8 u | 32 | 10 | 22 | €12,55 | €1,94 (12x) | **€10,61** | 0.21% | €-145,17 | €-134,56 | -2.69% |
| gate - htx | €5.000,00 | 2026-11-21 | 12.8 u | 24 | 7 | 17 | €6,59 | €1,42 (10x) | **€5,16** | 0.10% | €-35,90 | €-30,73 | -0.61% |
| bitget - htx | €100,00 | 2026-11-19 | 14.9 u | 20 | 20 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €100,00 | 2026-11-20 | 22.8 u | 39 | 39 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €100,00 | 2026-11-21 | 12.8 u | 40 | 40 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €150,00 | 2026-11-19 | 14.9 u | 20 | 20 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €150,00 | 2026-11-20 | 22.8 u | 39 | 39 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €150,00 | 2026-11-21 | 12.8 u | 40 | 40 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €200,00 | 2026-11-19 | 14.9 u | 20 | 20 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €200,00 | 2026-11-20 | 22.8 u | 39 | 39 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €200,00 | 2026-11-21 | 12.8 u | 40 | 40 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €2.000,00 | 2026-11-19 | 14.9 u | 20 | 7 | 13 | €0,69 | €0,31 (7x) | **€0,38** | 0.02% | onbekend | onbekend* | onbekend* |
| bitget - htx | €2.000,00 | 2026-11-20 | 22.8 u | 39 | 16 | 23 | €2,90 | €0,36 (18x) | **€2,54** | 0.13% | onbekend | onbekend* | onbekend* |
| bitget - htx | €2.000,00 | 2026-11-21 | 12.8 u | 40 | 30 | 10 | €0,27 | €0,15 (9x) | **€0,12** | 0.01% | onbekend | onbekend* | onbekend* |
| bitget - htx | €5.000,00 | 2026-11-19 | 14.9 u | 20 | 6 | 14 | €1,78 | €0,70 (10x) | **€1,09** | 0.02% | onbekend | onbekend* | onbekend* |
| bitget - htx | €5.000,00 | 2026-11-20 | 22.8 u | 39 | 8 | 31 | €9,75 | €1,56 (27x) | **€8,20** | 0.16% | onbekend | onbekend* | onbekend* |
| bitget - htx | €5.000,00 | 2026-11-21 | 12.8 u | 40 | 8 | 32 | €5,09 | €0,61 (24x) | **€4,48** | 0.09% | onbekend | onbekend* | onbekend* |
| htx - kucoin | €100,00 | 2026-11-19 | 14.9 u | 16 | 16 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,75 | €-1,75 | -1.75% |
| htx - kucoin | €100,00 | 2026-11-20 | 22.8 u | 42 | 42 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,24 | €-3,24 | -3.24% |
| htx - kucoin | €100,00 | 2026-11-21 | 12.8 u | 28 | 28 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,62 | €-0,62 | -0.62% |
| htx - kucoin | €150,00 | 2026-11-19 | 14.9 u | 16 | 16 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,62 | €-2,62 | -1.75% |
| htx - kucoin | €150,00 | 2026-11-20 | 22.8 u | 42 | 42 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-4,86 | €-4,86 | -3.24% |
| htx - kucoin | €150,00 | 2026-11-21 | 12.8 u | 28 | 28 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,93 | €-0,93 | -0.62% |
| htx - kucoin | €200,00 | 2026-11-19 | 14.9 u | 16 | 16 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,50 | €-3,50 | -1.75% |
| htx - kucoin | €200,00 | 2026-11-20 | 22.8 u | 42 | 42 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-6,47 | €-6,47 | -3.24% |
| htx - kucoin | €200,00 | 2026-11-21 | 12.8 u | 28 | 28 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,25 | €-1,25 | -0.62% |
| htx - kucoin | €2.000,00 | 2026-11-19 | 14.9 u | 16 | 10 | 6 | €0,55 | €0,00 (1x) | **€0,54** | 0.03% | €-34,96 | €-34,42 | -1.72% |
| htx - kucoin | €2.000,00 | 2026-11-20 | 22.8 u | 42 | 25 | 17 | €4,51 | €0,00 (0x) | **€4,51** | 0.23% | €-64,75 | €-60,24 | -3.01% |
| htx - kucoin | €2.000,00 | 2026-11-21 | 12.8 u | 28 | 12 | 16 | €1,27 | €0,10 (3x) | **€1,17** | 0.06% | €-12,45 | €-11,28 | -0.56% |
| htx - kucoin | €5.000,00 | 2026-11-19 | 14.9 u | 16 | 7 | 9 | €3,55 | €0,54 (4x) | **€3,02** | 0.06% | €-87,35 | €-84,33 | -1.69% |
| htx - kucoin | €5.000,00 | 2026-11-20 | 22.8 u | 42 | 19 | 23 | €12,21 | €2,40 (11x) | **€9,81** | 0.20% | €-161,82 | €-152,01 | -3.04% |
| htx - kucoin | €5.000,00 | 2026-11-21 | 12.8 u | 28 | 6 | 22 | €5,16 | €3,15 (13x) | **€2,01** | 0.04% | €-31,14 | €-29,12 | -0.58% |
| kucoin - xt | €100,00 | 2026-11-19 | 14.9 u | 13 | 13 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,04 | €-0,04 | -0.04% |
| kucoin - xt | €100,00 | 2026-11-20 | 22.8 u | 10 | 10 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,34 | €-0,34 | -0.34% |
| kucoin - xt | €100,00 | 2026-11-21 | 12.8 u | 6 | 6 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,27 | €0,27 | 0.27% |
| kucoin - xt | €150,00 | 2026-11-19 | 14.9 u | 13 | 13 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,06 | €-0,06 | -0.04% |
| kucoin - xt | €150,00 | 2026-11-20 | 22.8 u | 10 | 10 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,51 | €-0,51 | -0.34% |
| kucoin - xt | €150,00 | 2026-11-21 | 12.8 u | 6 | 6 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,40 | €0,40 | 0.27% |
| kucoin - xt | €200,00 | 2026-11-19 | 14.9 u | 13 | 13 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,08 | €-0,08 | -0.04% |
| kucoin - xt | €200,00 | 2026-11-20 | 22.8 u | 10 | 10 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,67 | €-0,67 | -0.34% |
| kucoin - xt | €200,00 | 2026-11-21 | 12.8 u | 6 | 5 | 1 | €0,08 | €0,00 (0x) | **€0,08** | 0.04% | €0,53 | €0,62 | 0.31% |
| kucoin - xt | €2.000,00 | 2026-11-19 | 14.9 u | 13 | 4 | 9 | €7,46 | €3,64 (9x) | **€3,82** | 0.19% | €-0,84 | €2,98 | 0.15% |
| kucoin - xt | €2.000,00 | 2026-11-20 | 22.8 u | 10 | 2 | 8 | €6,79 | €2,28 (6x) | **€4,51** | 0.23% | €-6,62 | €-2,11 | -0.11% |
| kucoin - xt | €2.000,00 | 2026-11-21 | 12.8 u | 6 | 1 | 5 | €5,86 | €1,51 (3x) | **€4,35** | 0.22% | €5,87 | €10,22 | 0.51% |
| kucoin - xt | €5.000,00 | 2026-11-19 | 14.9 u | 13 | 3 | 10 | €17,66 | €5,49 (11x) | **€12,17** | 0.24% | €-2,02 | €10,15 | 0.20% |
| kucoin - xt | €5.000,00 | 2026-11-20 | 22.8 u | 10 | 1 | 8 | €16,90 | €6,03 (10x) | **€10,87** | 0.22% | €-16,83 | €-5,96 | -0.12% |
| kucoin - xt | €5.000,00 | 2026-11-21 | 12.8 u | 6 | 0 | 6 | €11,59 | €2,34 (4x) | **€9,25** | 0.19% | €13,69 | €22,95 | 0.46% |

- htx - xt, €100,00: munten APEPE, APT, BSV, CARV, CBK, CFX, GT, HBAR, LUNC, MEME, PEOPLE, RAIN, SEI, SHIB, XCH, XDC, XMR; bruto zonder voorraadgrens zou €638,40 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - xt, €150,00: munten APEPE, APT, BSV, CARV, CBK, CFX, GT, HBAR, LUNC, MEME, PEOPLE, RAIN, SEI, SHIB, XCH, XDC, XMR; bruto zonder voorraadgrens zou €638,40 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - xt, €200,00: munten APEPE, APT, BSV, CARV, CBK, CFX, GT, HBAR, LUNC, MEME, PEOPLE, RAIN, SEI, SHIB, XCH, XDC, XMR; bruto zonder voorraadgrens zou €638,40 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - xt, €2.000,00: munten APEPE, APT, BSV, CARV, CBK, CFX, GT, HBAR, LUNC, MEME, PEOPLE, RAIN, SEI, SHIB, XCH, XDC, XMR; bruto zonder voorraadgrens zou €638,05 zijn, met voorraad €11,36 (GEZIEN boek, GOK model).
- htx - xt, €5.000,00: munten APEPE, APT, BSV, CARV, CBK, CFX, GT, HBAR, LUNC, MEME, PEOPLE, RAIN, SEI, SHIB, XCH, XDC, XMR; bruto zonder voorraadgrens zou €636,04 zijn, met voorraad €42,45 (GEZIEN boek, GOK model).
- gate - htx, €100,00: munten APEPE, APT, ATOM, BRISE, BSV, CBK, CRTS, CVX, ENJ, ENS, GOMINING, GT, HIVE, KAS, LAT, LINK, LUNC, MBX, MEME, MOVR, NPC, PEOPLE, QNT, SEI, SHIB, SSV, VIRTUAL, WARD, WLD, XCH, XCN, XDC; bruto zonder voorraadgrens zou €388,44 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- gate - htx, €150,00: munten APEPE, APT, ATOM, BRISE, BSV, CBK, CRTS, CVX, ENJ, ENS, GOMINING, GT, HIVE, KAS, LAT, LINK, LUNC, MBX, MEME, MOVR, NPC, PEOPLE, QNT, SEI, SHIB, SSV, VIRTUAL, WARD, WLD, XCH, XCN, XDC; bruto zonder voorraadgrens zou €388,44 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- gate - htx, €200,00: munten APEPE, APT, ATOM, BRISE, BSV, CBK, CRTS, CVX, ENJ, ENS, GOMINING, GT, HIVE, KAS, LAT, LINK, LUNC, MBX, MEME, MOVR, NPC, PEOPLE, QNT, SEI, SHIB, SSV, VIRTUAL, WARD, WLD, XCH, XCN, XDC; bruto zonder voorraadgrens zou €388,44 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- gate - htx, €2.000,00: munten APEPE, APT, ATOM, BRISE, BSV, CBK, CRTS, CVX, ENJ, ENS, GOMINING, GT, HIVE, KAS, LAT, LINK, LUNC, MBX, MEME, MOVR, NPC, PEOPLE, QNT, SEI, SHIB, SSV, VIRTUAL, WARD, WLD, XCH, XCN, XDC; bruto zonder voorraadgrens zou €388,05 zijn, met voorraad €7,85 (GEZIEN boek, GOK model).
- gate - htx, €5.000,00: munten APEPE, APT, ATOM, BRISE, BSV, CBK, CRTS, CVX, ENJ, ENS, GOMINING, GT, HIVE, KAS, LAT, LINK, LUNC, MBX, MEME, MOVR, NPC, PEOPLE, QNT, SEI, SHIB, SSV, VIRTUAL, WARD, WLD, XCH, XCN, XDC; bruto zonder voorraadgrens zou €385,57 zijn, met voorraad €24,27 (GEZIEN boek, GOK model).
- bitget - htx, €100,00: munten AB, ACN, ALGO, ANIME, ATOM, BABY, BONK, BSV, BTT, CBK, CFX, CORE, DYDX, ENA, ENJ, ENS, HBAR, HIVE, IOST, JASMY, KAS, LAT, LINK, LIT, LUNA, LUNC, MEME, MOVR, NPC, O, PCI, PEOPLE, QNT, RIVER, SHIB, SOMI, SSV, TAO, TIA, USTC, VIRTUAL, WARD, WLD, XDC, XTZ, ZEN; bruto zonder voorraadgrens zou €410,15 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - htx, €150,00: munten AB, ACN, ALGO, ANIME, ATOM, BABY, BONK, BSV, BTT, CBK, CFX, CORE, DYDX, ENA, ENJ, ENS, HBAR, HIVE, IOST, JASMY, KAS, LAT, LINK, LIT, LUNA, LUNC, MEME, MOVR, NPC, O, PCI, PEOPLE, QNT, RIVER, SHIB, SOMI, SSV, TAO, TIA, USTC, VIRTUAL, WARD, WLD, XDC, XTZ, ZEN; bruto zonder voorraadgrens zou €410,15 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - htx, €200,00: munten AB, ACN, ALGO, ANIME, ATOM, BABY, BONK, BSV, BTT, CBK, CFX, CORE, DYDX, ENA, ENJ, ENS, HBAR, HIVE, IOST, JASMY, KAS, LAT, LINK, LIT, LUNA, LUNC, MEME, MOVR, NPC, O, PCI, PEOPLE, QNT, RIVER, SHIB, SOMI, SSV, TAO, TIA, USTC, VIRTUAL, WARD, WLD, XDC, XTZ, ZEN; bruto zonder voorraadgrens zou €410,15 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - htx, €2.000,00: munten AB, ACN, ALGO, ANIME, ATOM, BABY, BONK, BSV, BTT, CBK, CFX, CORE, DYDX, ENA, ENJ, ENS, HBAR, HIVE, IOST, JASMY, KAS, LAT, LINK, LIT, LUNA, LUNC, MEME, MOVR, NPC, O, PCI, PEOPLE, QNT, RIVER, SHIB, SOMI, SSV, TAO, TIA, USTC, VIRTUAL, WARD, WLD, XDC, XTZ, ZEN; bruto zonder voorraadgrens zou €409,99 zijn, met voorraad €3,87 (GEZIEN boek, GOK model).
- bitget - htx, €5.000,00: munten AB, ACN, ALGO, ANIME, ATOM, BABY, BONK, BSV, BTT, CBK, CFX, CORE, DYDX, ENA, ENJ, ENS, HBAR, HIVE, IOST, JASMY, KAS, LAT, LINK, LIT, LUNA, LUNC, MEME, MOVR, NPC, O, PCI, PEOPLE, QNT, RIVER, SHIB, SOMI, SSV, TAO, TIA, USTC, VIRTUAL, WARD, WLD, XDC, XTZ, ZEN; bruto zonder voorraadgrens zou €409,27 zijn, met voorraad €16,63 (GEZIEN boek, GOK model).
- htx - kucoin, €100,00: munten ACN, ALGO, ANIME, APT, BONK, BSV, BTT, CFX, CHIP, CVX, DYDX, ELA, ENJ, ENS, FET, JASMY, JST, LAT, LTC, LUNC, MEME, MOVR, NPC, ONE, PEOPLE, QNT, SHIB, SOMI, SSV, TRAC, VIRTUAL, WAN, WARD, WLD, XCH, XCN, XEC, XMR, XTZ; bruto zonder voorraadgrens zou €437,22 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - kucoin, €150,00: munten ACN, ALGO, ANIME, APT, BONK, BSV, BTT, CFX, CHIP, CVX, DYDX, ELA, ENJ, ENS, FET, JASMY, JST, LAT, LTC, LUNC, MEME, MOVR, NPC, ONE, PEOPLE, QNT, SHIB, SOMI, SSV, TRAC, VIRTUAL, WAN, WARD, WLD, XCH, XCN, XEC, XMR, XTZ; bruto zonder voorraadgrens zou €437,22 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - kucoin, €200,00: munten ACN, ALGO, ANIME, APT, BONK, BSV, BTT, CFX, CHIP, CVX, DYDX, ELA, ENJ, ENS, FET, JASMY, JST, LAT, LTC, LUNC, MEME, MOVR, NPC, ONE, PEOPLE, QNT, SHIB, SOMI, SSV, TRAC, VIRTUAL, WAN, WARD, WLD, XCH, XCN, XEC, XMR, XTZ; bruto zonder voorraadgrens zou €437,22 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - kucoin, €2.000,00: munten ACN, ALGO, ANIME, APT, BONK, BSV, BTT, CFX, CHIP, CVX, DYDX, ELA, ENJ, ENS, FET, JASMY, JST, LAT, LTC, LUNC, MEME, MOVR, NPC, ONE, PEOPLE, QNT, SHIB, SOMI, SSV, TRAC, VIRTUAL, WAN, WARD, WLD, XCH, XCN, XEC, XMR, XTZ; bruto zonder voorraadgrens zou €436,88 zijn, met voorraad €6,33 (GEZIEN boek, GOK model).
- htx - kucoin, €5.000,00: munten ACN, ALGO, ANIME, APT, BONK, BSV, BTT, CFX, CHIP, CVX, DYDX, ELA, ENJ, ENS, FET, JASMY, JST, LAT, LTC, LUNC, MEME, MOVR, NPC, ONE, PEOPLE, QNT, SHIB, SOMI, SSV, TRAC, VIRTUAL, WAN, WARD, WLD, XCH, XCN, XEC, XMR, XTZ; bruto zonder voorraadgrens zou €436,07 zijn, met voorraad €20,93 (GEZIEN boek, GOK model).
- kucoin - xt, €100,00: munten BARD, DAG, ENSO, FIGHT, LUNC, USDS, XMR; bruto zonder voorraadgrens zou €1.025,31 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- kucoin - xt, €150,00: munten BARD, DAG, ENSO, FIGHT, LUNC, USDS, XMR; bruto zonder voorraadgrens zou €1.025,31 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- kucoin - xt, €200,00: munten BARD, DAG, ENSO, FIGHT, LUNC, USDS, XMR; bruto zonder voorraadgrens zou €1.025,31 zijn, met voorraad €0,08 (GEZIEN boek, GOK model).
- kucoin - xt, €2.000,00: munten BARD, DAG, ENSO, FIGHT, LUNC, USDS, XMR; bruto zonder voorraadgrens zou €1.022,83 zijn, met voorraad €20,11 (GEZIEN boek, GOK model).
- kucoin - xt, €5.000,00: munten BARD, DAG, ENSO, FIGHT, LUNC, USDS, XMR; bruto zonder voorraadgrens zou €1.019,21 zijn, met voorraad €46,14 (GEZIEN boek, GOK model).

### Andere keuzes bij bitvavo - kraken (netto handel, alle dagen samen; GOK)

| Keuze | Inleg | Kansen | Gemist | Bruto winst | Kosten terugschuiven | Netto handel |
|---|---|---|---|---|---|---|
| standaard (schuifdrempel 25%, kostengrens 1%) | €150,00 | 68 | 68 | €0,00 | €0,00 | **€0,00** |
| standaard (schuifdrempel 25%, kostengrens 1%) | €2.000,00 | 68 | 39 | €57,05 | €11,02 | **€46,03** |
| schuifdrempel 10% | €150,00 | 68 | 68 | €0,00 | €0,00 | **€0,00** |
| schuifdrempel 10% | €2.000,00 | 68 | 41 | €55,74 | €10,40 | **€45,34** |
| schuifdrempel 40% | €150,00 | 68 | 68 | €0,00 | €0,00 | **€0,00** |
| schuifdrempel 40% | €2.000,00 | 68 | 39 | €55,44 | €11,69 | **€43,74** |
| kostengrens 2% (achteraf vergeleken) | €150,00 | 68 | 68 | €0,00 | €0,00 | **€0,00** |
| kostengrens 2% (achteraf vergeleken) | €2.000,00 | 68 | 30 | €57,16 | €25,33 | **€31,83** |
| kostengrens 5% (achteraf vergeleken) | €150,00 | 68 | 68 | €0,00 | €0,00 | **€0,00** |
| kostengrens 5% (achteraf vergeleken) | €2.000,00 | 68 | 27 | €57,67 | €30,25 | **€27,42** |
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

- Opnamekosten bij de echte kansen: 223 van een netwerk dat aan beide kanten open is, 142 van de beurs zelf (laagste open netwerk), 108 geschat uit wat andere beurzen voor die munt vragen (GOK). Onbekende opnamekosten tellen niet als echte kans.
- Netwerk: KuCoin, Gate, Bitget, HTX, XT, Bitstamp, Bitvavo en Poloniex geven hun netwerken per munt. Als beide beurzen dat doen en de namen te koppelen zijn, moet er een netwerk zijn dat aan beide kanten open is. Anders is het netwerk "niet te koppelen" en telt de kans mee (staat apart in de trechter).
- De duur is gemeten in stappen van ±20 seconden; een kans kan een paar rondes eerder begonnen zijn dan we zagen.
- Takerkosten: uit de API waar die ze per paar geeft, anders het standaardtarief uit de README (deels GOK).
- Laatste run: 15 beurzen antwoordden, 2279 munt-quote-paren op minstens twee beurzen (GEZIEN).
