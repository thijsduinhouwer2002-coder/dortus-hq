# Rapport koersverschil-scanner

Gemaakt 2026-11-22 17:59 UTC uit 29 runs, samen ±77.0 uur gemeten (GEZIEN).
Echte kans = winst na alle kosten (opnamekosten bekend), opnemen en storten open (en een netwerk dat aan beide kanten open is, als de beurzen dat geven), minstens €100,00 op het boek, minstens 2 minuten blijven staan, geen andere munt met dezelfde naam.
**Vergund** = beide beurzen hebben een MiCA-vergunning (ESMA-register), vaak via een EU-dochter die minder munten kan hebben dan de wereldwijde API die we meten (GOK). **Grijs** = minstens één beurs zonder vergunning (MEXC, Bitget, HTX, Poloniex, XT, Bitfinex, Binance). Zie README.md.
**Kraken-tarief:** Kraken rekent 0,80% taker op munt tegen EUR, USD, USDT of USDC (GEZIEN, kraken.com/pro/fees, laagste trede); de scanner rekende tot 19 nov met 0,40%. 399 opgeslagen kansen met Kraken uit die runs zijn hier **opnieuw doorgerekend met 0,80%** (GOK-benadering: 0,40% van de inzet aan de Kraken-kant extra op elk gemeten punt van het boek; het boek zelf is niet bewaard). 233 houden daarna nog winst op het boek. Dat ze met hogere kosten ook korter bleven staan, telt niet mee (dus eerder te gunstig).

## Hoeveel wordt er gecontroleerd? (GEZIEN, stand.jsonl)

Per ronde (mediaan over 924 metingen): 1102 kandidaten (verschil op de ticker groter dan de takerkosten), 120 met het orderboek gecontroleerd, 3 nog nooit gecontroleerd (0%).
Bijna alle kandidaten komen aan de beurt; de aantallen hieronder missen weinig.

## Trechter (GEZIEN, eigen metingen)

| Stap | Alle beurzen | Alleen MiCA-beurzen | Met minstens één grijze beurs |
|---|---|---|---|
| Verschillen met winst op het boek na alle kosten | 68123 | 9257 | 58866 |
| ...waarvan opnemen of storten dicht | 12122 | 1296 | 10826 |
| ...waarvan status onbekend (beurs geeft het niet openbaar) | 41577 | 6646 | 34931 |
| Opnemen en storten open | 14424 | 1315 | 13109 |
| ...en geen netwerk dat aan beide kanten open is: valt af | 435 | 38 | 397 |
| ...en opnamekosten onbekend: valt af | 5 | 5 | 0 |
| ...en minstens €100,00 op het boek | 4625 | 835 | 3790 |
| ...en minstens 2 minuten blijven staan | 1271 | 326 | 945 |
| ...en geen andere munt met dezelfde naam | 1206 | 292 | 914 |
|    ...waarvan contractadres bekend en gelijk | 189 | 56 | 133 |
|    ...waarvan contractadres onbekend (telt mee, kan een andere munt zijn) | 1017 | 236 | 781 |
|    ...waarvan netwerk gekoppeld en open | 795 | 148 | 647 |
|    ...waarvan netwerk niet te koppelen (telt mee) | 411 | 144 | 267 |
| **Echte kansen** (zelfde munt overlappend in de tijd samengevoegd, beste beurspaar telt) | 732 | 282 | 548 |
| Ter vergelijking: zelfde eisen, maar opnamestatus onbekend (niet meegeteld) | 2819 | 697 | 2365 |

## Echte kansen per dag (GEZIEN)

| Dag | Echt, alleen MiCA | Echt, met grijs | Mediane winst per kans bij €500 (MiCA / grijs) | Mediane duur |
|---|---|---|---|---|
| 2026-11-19 | 49 | 86 | €2,00 / €1,21 | 5.3 min |
| 2026-11-20 | 53 | 138 | €1,01 / €1,13 | 6.7 min |
| 2026-11-21 | 61 | 176 | €1,13 / €0,88 | 6.7 min |
| 2026-11-22 | 41 | 128 | €1,67 / €0,72 | 8.3 min |
| Totaal | 204 | 528 | €1,42 / €0,91 | 6.7 min |

## Beste munten (GEZIEN)

| | Soort | Kansen | Som winst bij €500 per kans |
|---|---|---|---|
| MERL-EUR | vergund | 45 | €931,41 |
| LUNC-USDT | grijs | 23 | €124,40 |
| USTC-USDT | grijs en vergund | 32 | €93,85 |
| AI-USDT | grijs | 13 | €81,15 |
| XMR-USDT | grijs | 50 | €65,69 |
| KERNEL-EUR | vergund | 1 | €47,33 |
| ENSO-USDT | grijs en vergund | 11 | €45,15 |
| BSV-USDT | grijs | 28 | €44,32 |
| MEME-USDT | grijs | 1 | €37,90 |
| KYO-USDT | vergund | 5 | €30,94 |

## Beste beursparen (kopen op > verkopen op) (GEZIEN)

| | Soort | Kansen | Som winst bij €500 per kans |
|---|---|---|---|
| bitvavo > kraken | vergund | 108 | €1.040,29 |
| bitget > htx | grijs | 86 | €181,03 |
| kucoin > bitget | grijs | 67 | €104,36 |
| kucoin > htx | grijs | 45 | €100,81 |
| gate > kucoin | vergund | 40 | €99,34 |
| gate > htx | grijs | 32 | €82,64 |
| bitget > xt | grijs | 26 | €79,82 |
| htx > kucoin | grijs | 23 | €73,85 |
| kucoin > gate | vergund | 40 | €59,33 |
| bitget > gate | grijs | 25 | €58,63 |

Beurzen die het vaakst meedoen (koop of verkoop): bitget (grijs) 314, kucoin 310, htx (grijs) 255, gate 171, kraken 146, bitvavo 123, poloniex (grijs) 74, xt (grijs) 68 (GEZIEN).

## Hoeveel kansen blijven staan terwijl je geld schuift? (GEZIEN, duur uit eigen metingen)

Wie geen voorraad op beide beurzen heeft, moet kopen, de munt opnemen, wachten tot hij binnen is en dan verkopen. Hoe lang dat duurt verschilt per munt en netwerk: een paar minuten (snelle ketens) tot een uur of meer (Bitcoin, beurzen die opnames met de hand keuren) (GOK, niet per munt gemeten).

| Overmaaktijd | Alle beurzen | Alleen MiCA-beurzen | Met minstens één grijze beurs |
|---|---|---|---|
| 5 min | 436 van 732 (60%) | 165 van 282 (59%) | 335 van 548 (61%) |
| 10 min | 287 van 732 (39%) | 115 van 282 (41%) | 220 van 548 (40%) |
| 30 min | 149 van 732 (20%) | 58 van 282 (21%) | 122 van 548 (22%) |
| 60 min | 88 van 732 (12%) | 40 van 282 (14%) | 72 van 548 (13%) |

## Wat zou het opleveren over 3 maanden? (GOK, doorgetrokken uit de metingen)

Gemeten over ±77.0 uur (GEZIEN), doorgetrokken naar 90 dagen (GOK: aanname dat de week die we maten gewoon is).

| Beurzen | Inleg | Model | Kansen per uur | Per kans (mediaan) | 3 maanden |
|---|---|---|---|---|---|
| Alleen MiCA | €2.000,00 | bovengrens: elke kans, geld overal tegelijk | 3.66 | €1,58 | €12.517,10 |
| Alleen MiCA | €2.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 1.40 | €3,49 | €52.710,30 |
| Alleen MiCA | €5.000,00 | bovengrens: elke kans, geld overal tegelijk | 3.66 | €1,82 | €14.422,73 |
| Alleen MiCA | €5.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 1.40 | €3,97 | €99.563,93 |
| Alle (met grijs) | €2.000,00 | bovengrens: elke kans, geld overal tegelijk | 9.51 | €1,37 | €28.073,41 |
| Alle (met grijs) | €2.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 1.40 | €3,49 | €52.710,30 |
| Alle (met grijs) | €5.000,00 | bovengrens: elke kans, geld overal tegelijk | 9.51 | €1,62 | €33.320,75 |
| Alle (met grijs) | €5.000,00 | alleen het beste beurspaar (bitvavo > kraken) | 1.40 | €3,97 | €99.563,93 |

Bovengrens: elke kans met de helft van de inleg aan elke kant, alsof het geld op alle beurzen tegelijk staat (kan in het echt niet). Beste beurspaar: het paar is **achteraf** gekozen uit de metingen (vooraf kiezen levert minder op), en het model neemt aan dat je van elke munt al voorraad op de verkoopbeurs hebt.

Waarom dit te rooskleurig is (GOK): elke kans wordt maar één keer geteld met het mediane boek, maar andere bots pakken hem ook; de munt die je als voorraad aanhoudt kan dalen; na een paar kansen moet de voorraad terug (opnamekosten en tijd); minimale opname- en ordergroottes tellen niet mee; en een kans die we 2 minuten zagen staan, staat er niet per se nog als jouw order binnenkomt. Waarom het te somber kan zijn: niet alle kandidaten zijn gecontroleerd, en met voorraad op beide beurzen kun je dezelfde kans vaker pakken als het boek zich aanvult; dat telt hier niet mee.

## Wat houd je echt over? Voorraad op twee beurzen (simulatie)

Per beurspaar: geld en munten op beide beurzen, elke echte kans uitgevoerd tegen het boek zoals gemeten (niet meer dan de ruimte op het boek en niet meer dan de voorraad op die beurs), terugschuiven als een kant leeg dreigt te raken (met opnamekosten en tijd onderweg), en het koerseffect van de aangehouden munten apart. Netto = bruto min kosten terugschuiven plus koerseffect. **Gemeten** (GEZIEN): de kansen, het boek en de koersen; **de rest is een rekenmodel** (GOK, aannames onder de tabel). Geen advies.

**Met €150: netto €0,39 per dag op bitstamp - kraken (koerseffect erbovenop €-1,83), €0,00 per dag op bitstamp - kucoin (koerseffect erbovenop €0,00), €0,00 per dag op bitvavo - kraken (koerseffect erbovenop €-1,22), €0,02 per dag op bitvavo - kucoin (koerseffect erbovenop €-0,42), €0,00 per dag op gate - kucoin (koerseffect erbovenop €-1,71), €0,01 per dag op kraken - kucoin (koerseffect erbovenop €0,00) (GOK: netto handel, rekenmodel op ±19.2 uur meting per dag, alleen MiCA).** "Per dag" is hier gemiddeld over 4 gemeten dagen achter elkaar; de eerste begint met een gelijk verdeelde voorraad; aan het eind staat de voorraad scheef, dus een volgende dag levert waarschijnlijk minder op, tenzij kansen de andere kant op hem terugbrengen (GOK).

### Alleen MiCA-beurzen (alle paren met echte kansen)

| Beurspaar | Inleg | Dag | Gemeten | Kansen | Gemist (geen voorraad) | Kleiner door voorraad | Bruto winst | Kosten terugschuiven | **Netto handel (bruto min kosten)** | Rendement handel | Koerseffect voorraad | Netto met koerseffect | Rendement met koerseffect |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| bitstamp - kraken | €100,00 | 2026-11-19 | 14.9 u | 2 | 1 | 1 | €0,59 | €0,00 (0x) | **€0,59** | 0.59% | €-0,02 | €0,57 | 0.57% |
| bitstamp - kraken | €100,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,95 | €-2,95 | -2.95% |
| bitstamp - kraken | €100,00 | 2026-11-21 | 22.9 u | 1 | 0 | 1 | €0,45 | €0,00 (0x) | **€0,45** | 0.45% | €-0,70 | €-0,25 | -0.25% |
| bitstamp - kraken | €100,00 | 2026-11-22 | 16.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,20 | €-1,20 | -1.20% |
| bitstamp - kraken | €150,00 | 2026-11-19 | 14.9 u | 2 | 1 | 1 | €0,89 | €0,00 (0x) | **€0,89** | 0.59% | €-0,03 | €0,85 | 0.57% |
| bitstamp - kraken | €150,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-4,43 | €-4,43 | -2.95% |
| bitstamp - kraken | €150,00 | 2026-11-21 | 22.9 u | 1 | 0 | 1 | €0,67 | €0,00 (0x) | **€0,67** | 0.45% | €-1,05 | €-0,38 | -0.25% |
| bitstamp - kraken | €150,00 | 2026-11-22 | 16.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,80 | €-1,80 | -1.20% |
| bitstamp - kraken | €200,00 | 2026-11-19 | 14.9 u | 2 | 1 | 1 | €1,18 | €0,00 (0x) | **€1,18** | 0.59% | €-0,04 | €1,14 | 0.57% |
| bitstamp - kraken | €200,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-5,91 | €-5,91 | -2.95% |
| bitstamp - kraken | €200,00 | 2026-11-21 | 22.9 u | 1 | 0 | 1 | €0,89 | €0,00 (0x) | **€0,89** | 0.45% | €-1,40 | €-0,51 | -0.25% |
| bitstamp - kraken | €200,00 | 2026-11-22 | 16.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,40 | €-2,40 | -1.20% |
| bitstamp - kraken | €2.000,00 | 2026-11-19 | 14.9 u | 2 | 1 | 0 | €11,71 | €0,98 (1x) | **€10,73** | 0.54% | €-0,46 | €10,27 | 0.51% |
| bitstamp - kraken | €2.000,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-59,03 | €-59,03 | -2.95% |
| bitstamp - kraken | €2.000,00 | 2026-11-21 | 22.9 u | 1 | 0 | 0 | €5,30 | €0,00 (0x) | **€5,30** | 0.26% | €-14,01 | €-8,71 | -0.44% |
| bitstamp - kraken | €2.000,00 | 2026-11-22 | 16.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-23,94 | €-23,94 | -1.20% |
| bitstamp - kraken | €5.000,00 | 2026-11-19 | 14.9 u | 2 | 1 | 0 | €11,71 | €0,00 (0x) | **€11,71** | 0.23% | €-1,10 | €10,60 | 0.21% |
| bitstamp - kraken | €5.000,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-147,75 | €-147,75 | -2.95% |
| bitstamp - kraken | €5.000,00 | 2026-11-21 | 22.9 u | 1 | 0 | 0 | €5,30 | €0,00 (0x) | **€5,30** | 0.11% | €-35,01 | €-29,71 | -0.59% |
| bitstamp - kraken | €5.000,00 | 2026-11-22 | 16.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-59,96 | €-59,96 | -1.20% |
| bitstamp - kucoin | €100,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,11 | €0,11 | 0.11% |
| bitstamp - kucoin | €100,00 | 2026-11-20 | 22.8 u | 1 | 0 | 1 | €0,00 | €0,01 (1x) | **€-0,01** | -0.01% | €0,11 | €0,10 | 0.10% |
| bitstamp - kucoin | €100,00 | 2026-11-21 | 22.9 u | 6 | 5 | 1 | €0,01 | €0,00 (0x) | **€0,01** | 0.01% | €-0,16 | €-0,15 | -0.15% |
| bitstamp - kucoin | €100,00 | 2026-11-22 | 16.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,05 | €-0,05 | -0.05% |
| bitstamp - kucoin | €150,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,16 | €0,16 | 0.11% |
| bitstamp - kucoin | €150,00 | 2026-11-20 | 22.8 u | 1 | 0 | 1 | €0,00 | €0,01 (1x) | **€-0,01** | -0.00% | €0,16 | €0,16 | 0.11% |
| bitstamp - kucoin | €150,00 | 2026-11-21 | 22.9 u | 6 | 5 | 1 | €0,02 | €0,00 (0x) | **€0,02** | 0.01% | €-0,24 | €-0,22 | -0.15% |
| bitstamp - kucoin | €150,00 | 2026-11-22 | 16.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,07 | €-0,07 | -0.05% |
| bitstamp - kucoin | €200,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,22 | €0,22 | 0.11% |
| bitstamp - kucoin | €200,00 | 2026-11-20 | 22.8 u | 1 | 0 | 1 | €0,01 | €0,01 (1x) | **€-0,00** | -0.00% | €0,22 | €0,22 | 0.11% |
| bitstamp - kucoin | €200,00 | 2026-11-21 | 22.9 u | 6 | 5 | 1 | €0,03 | €0,23 (1x) | **€-0,21** | -0.10% | €-0,32 | €-0,53 | -0.26% |
| bitstamp - kucoin | €200,00 | 2026-11-22 | 16.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,09 | €-0,09 | -0.05% |
| bitstamp - kucoin | €2.000,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €2,19 | €2,19 | 0.11% |
| bitstamp - kucoin | €2.000,00 | 2026-11-20 | 22.8 u | 1 | 0 | 1 | €0,05 | €0,01 (1x) | **€0,04** | 0.00% | €2,19 | €2,24 | 0.11% |
| bitstamp - kucoin | €2.000,00 | 2026-11-21 | 22.9 u | 6 | 5 | 1 | €0,27 | €1,23 (2x) | **€-0,97** | -0.05% | €-3,24 | €-4,20 | -0.21% |
| bitstamp - kucoin | €2.000,00 | 2026-11-22 | 16.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,93 | €-0,93 | -0.05% |
| bitstamp - kucoin | €5.000,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €5,49 | €5,49 | 0.11% |
| bitstamp - kucoin | €5.000,00 | 2026-11-20 | 22.8 u | 1 | 0 | 1 | €0,13 | €0,01 (1x) | **€0,12** | 0.00% | €5,48 | €5,60 | 0.11% |
| bitstamp - kucoin | €5.000,00 | 2026-11-21 | 22.9 u | 6 | 5 | 1 | €0,64 | €1,23 (2x) | **€-0,59** | -0.01% | €-8,09 | €-8,68 | -0.17% |
| bitstamp - kucoin | €5.000,00 | 2026-11-22 | 16.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,33 | €-2,33 | -0.05% |
| bitvavo - kraken | €100,00 | 2026-11-19 | 14.9 u | 43 | 43 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,71 | €-0,71 | -0.71% |
| bitvavo - kraken | €100,00 | 2026-11-20 | 22.8 u | 15 | 15 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,47 | €-1,47 | -1.47% |
| bitvavo - kraken | €100,00 | 2026-11-21 | 22.9 u | 26 | 26 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,65 | €-0,65 | -0.65% |
| bitvavo - kraken | €100,00 | 2026-11-22 | 16.3 u | 24 | 24 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,42 | €-0,42 | -0.42% |
| bitvavo - kraken | €150,00 | 2026-11-19 | 14.9 u | 43 | 43 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,07 | €-1,07 | -0.71% |
| bitvavo - kraken | €150,00 | 2026-11-20 | 22.8 u | 15 | 15 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,21 | €-2,21 | -1.47% |
| bitvavo - kraken | €150,00 | 2026-11-21 | 22.9 u | 26 | 26 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,97 | €-0,97 | -0.65% |
| bitvavo - kraken | €150,00 | 2026-11-22 | 16.3 u | 24 | 24 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,63 | €-0,63 | -0.42% |
| bitvavo - kraken | €200,00 | 2026-11-19 | 14.9 u | 43 | 43 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,43 | €-1,43 | -0.71% |
| bitvavo - kraken | €200,00 | 2026-11-20 | 22.8 u | 15 | 15 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,94 | €-2,94 | -1.47% |
| bitvavo - kraken | €200,00 | 2026-11-21 | 22.9 u | 26 | 26 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,29 | €-1,29 | -0.65% |
| bitvavo - kraken | €200,00 | 2026-11-22 | 16.3 u | 24 | 24 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,84 | €-0,84 | -0.42% |
| bitvavo - kraken | €2.000,00 | 2026-11-19 | 14.9 u | 43 | 25 | 18 | €9,82 | €7,00 (18x) | **€2,83** | 0.14% | €-14,21 | €-11,38 | -0.57% |
| bitvavo - kraken | €2.000,00 | 2026-11-20 | 22.8 u | 15 | 9 | 6 | €19,13 | €1,28 (4x) | **€17,84** | 0.89% | €-29,13 | €-11,29 | -0.56% |
| bitvavo - kraken | €2.000,00 | 2026-11-21 | 22.9 u | 26 | 16 | 10 | €20,33 | €3,25 (8x) | **€17,08** | 0.85% | €-13,05 | €4,03 | 0.20% |
| bitvavo - kraken | €2.000,00 | 2026-11-22 | 16.3 u | 24 | 12 | 12 | €6,38 | €4,85 (13x) | **€1,53** | 0.08% | €-8,35 | €-6,83 | -0.34% |
| bitvavo - kraken | €5.000,00 | 2026-11-19 | 14.9 u | 43 | 18 | 25 | €26,04 | €16,56 (27x) | **€9,48** | 0.19% | €-35,59 | €-26,10 | -0.52% |
| bitvavo - kraken | €5.000,00 | 2026-11-20 | 22.8 u | 15 | 2 | 13 | €50,25 | €12,35 (15x) | **€37,90** | 0.76% | €-72,11 | €-34,21 | -0.68% |
| bitvavo - kraken | €5.000,00 | 2026-11-21 | 22.9 u | 26 | 13 | 13 | €53,81 | €7,51 (13x) | **€46,29** | 0.93% | €-32,19 | €14,11 | 0.28% |
| bitvavo - kraken | €5.000,00 | 2026-11-22 | 16.3 u | 24 | 11 | 13 | €17,32 | €5,82 (14x) | **€11,50** | 0.23% | €-20,71 | €-9,21 | -0.18% |
| bitvavo - kucoin | €100,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,52 | €-0,52 | -0.52% |
| bitvavo - kucoin | €100,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,80 | €-1,80 | -1.80% |
| bitvavo - kucoin | €100,00 | 2026-11-21 | 22.9 u | 7 | 5 | 2 | €0,04 | €0,00 (0x) | **€0,04** | 0.04% | €0,78 | €0,82 | 0.82% |
| bitvavo - kucoin | €100,00 | 2026-11-22 | 16.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,42 | €0,42 | 0.42% |
| bitvavo - kucoin | €150,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,78 | €-0,78 | -0.52% |
| bitvavo - kucoin | €150,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,71 | €-2,71 | -1.80% |
| bitvavo - kucoin | €150,00 | 2026-11-21 | 22.9 u | 7 | 5 | 2 | €0,07 | €0,00 (0x) | **€0,07** | 0.04% | €1,17 | €1,23 | 0.82% |
| bitvavo - kucoin | €150,00 | 2026-11-22 | 16.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,63 | €0,63 | 0.42% |
| bitvavo - kucoin | €200,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,04 | €-1,04 | -0.52% |
| bitvavo - kucoin | €200,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,61 | €-3,61 | -1.80% |
| bitvavo - kucoin | €200,00 | 2026-11-21 | 22.9 u | 7 | 5 | 2 | €0,09 | €0,00 (0x) | **€0,09** | 0.04% | €1,56 | €1,65 | 0.82% |
| bitvavo - kucoin | €200,00 | 2026-11-22 | 16.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,83 | €0,83 | 0.42% |
| bitvavo - kucoin | €2.000,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-10,39 | €-10,39 | -0.52% |
| bitvavo - kucoin | €2.000,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-36,07 | €-36,07 | -1.80% |
| bitvavo - kucoin | €2.000,00 | 2026-11-21 | 22.9 u | 7 | 4 | 3 | €0,91 | €2,73 (3x) | **€-1,82** | -0.09% | €15,55 | €13,72 | 0.69% |
| bitvavo - kucoin | €2.000,00 | 2026-11-22 | 16.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €8,33 | €8,33 | 0.42% |
| bitvavo - kucoin | €5.000,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-25,99 | €-25,99 | -0.52% |
| bitvavo - kucoin | €5.000,00 | 2026-11-20 | 22.8 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-90,18 | €-90,18 | -1.80% |
| bitvavo - kucoin | €5.000,00 | 2026-11-21 | 22.9 u | 7 | 4 | 3 | €2,24 | €2,73 (3x) | **€-0,49** | -0.01% | €38,94 | €38,45 | 0.77% |
| bitvavo - kucoin | €5.000,00 | 2026-11-22 | 16.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €20,85 | €20,85 | 0.42% |
| gate - kucoin | €100,00 | 2026-11-19 | 14.9 u | 25 | 25 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,34 | €-0,34 | -0.34% |
| gate - kucoin | €100,00 | 2026-11-20 | 22.8 u | 46 | 46 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,41 | €-0,41 | -0.41% |
| gate - kucoin | €100,00 | 2026-11-21 | 22.9 u | 46 | 46 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,32 | €-2,32 | -2.32% |
| gate - kucoin | €100,00 | 2026-11-22 | 16.3 u | 23 | 23 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,48 | €-1,48 | -1.48% |
| gate - kucoin | €150,00 | 2026-11-19 | 14.9 u | 25 | 25 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,52 | €-0,52 | -0.34% |
| gate - kucoin | €150,00 | 2026-11-20 | 22.8 u | 46 | 46 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,62 | €-0,62 | -0.41% |
| gate - kucoin | €150,00 | 2026-11-21 | 22.9 u | 46 | 46 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,49 | €-3,49 | -2.32% |
| gate - kucoin | €150,00 | 2026-11-22 | 16.3 u | 23 | 23 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,22 | €-2,22 | -1.48% |
| gate - kucoin | €200,00 | 2026-11-19 | 14.9 u | 25 | 25 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,69 | €-0,69 | -0.34% |
| gate - kucoin | €200,00 | 2026-11-20 | 22.8 u | 46 | 44 | 2 | €0,22 | €0,00 (1x) | **€0,22** | 0.11% | €-0,82 | €-0,61 | -0.30% |
| gate - kucoin | €200,00 | 2026-11-21 | 22.9 u | 46 | 46 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-4,65 | €-4,65 | -2.32% |
| gate - kucoin | €200,00 | 2026-11-22 | 16.3 u | 23 | 23 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,97 | €-2,97 | -1.48% |
| gate - kucoin | €2.000,00 | 2026-11-19 | 14.9 u | 25 | 17 | 8 | €1,02 | €0,13 (1x) | **€0,89** | 0.04% | €-6,90 | €-6,01 | -0.30% |
| gate - kucoin | €2.000,00 | 2026-11-20 | 22.8 u | 46 | 25 | 21 | €6,72 | €0,45 (6x) | **€6,26** | 0.31% | €-8,23 | €-1,97 | -0.10% |
| gate - kucoin | €2.000,00 | 2026-11-21 | 22.9 u | 46 | 34 | 12 | €3,72 | €0,01 (1x) | **€3,71** | 0.19% | €-46,46 | €-42,75 | -2.14% |
| gate - kucoin | €2.000,00 | 2026-11-22 | 16.3 u | 23 | 17 | 6 | €0,68 | €0,01 (2x) | **€0,66** | 0.03% | €-29,63 | €-28,97 | -1.45% |
| gate - kucoin | €5.000,00 | 2026-11-19 | 14.9 u | 25 | 6 | 19 | €5,43 | €3,74 (17x) | **€1,68** | 0.03% | €-17,26 | €-15,58 | -0.31% |
| gate - kucoin | €5.000,00 | 2026-11-20 | 22.8 u | 46 | 10 | 36 | €20,93 | €4,22 (24x) | **€16,71** | 0.33% | €-20,46 | €-3,76 | -0.08% |
| gate - kucoin | €5.000,00 | 2026-11-21 | 22.9 u | 46 | 14 | 32 | €13,16 | €4,13 (24x) | **€9,03** | 0.18% | €-115,94 | €-106,91 | -2.14% |
| gate - kucoin | €5.000,00 | 2026-11-22 | 16.3 u | 23 | 3 | 20 | €4,12 | €3,69 (18x) | **€0,43** | 0.01% | €-73,87 | €-73,44 | -1.47% |
| kraken - kucoin | €100,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,11 | €0,11 | 0.11% |
| kraken - kucoin | €100,00 | 2026-11-20 | 22.8 u | 15 | 13 | 2 | €0,03 | €0,01 (1x) | **€0,02** | 0.02% | €0,11 | €0,13 | 0.13% |
| kraken - kucoin | €100,00 | 2026-11-21 | 22.9 u | 12 | 12 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,16 | €-0,16 | -0.16% |
| kraken - kucoin | €100,00 | 2026-11-22 | 16.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,05 | €-0,05 | -0.05% |
| kraken - kucoin | €150,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,16 | €0,16 | 0.11% |
| kraken - kucoin | €150,00 | 2026-11-20 | 22.8 u | 15 | 13 | 2 | €0,05 | €0,01 (1x) | **€0,04** | 0.02% | €0,16 | €0,20 | 0.13% |
| kraken - kucoin | €150,00 | 2026-11-21 | 22.9 u | 12 | 12 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,24 | €-0,24 | -0.16% |
| kraken - kucoin | €150,00 | 2026-11-22 | 16.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,07 | €-0,07 | -0.05% |
| kraken - kucoin | €200,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,22 | €0,22 | 0.11% |
| kraken - kucoin | €200,00 | 2026-11-20 | 22.8 u | 15 | 13 | 2 | €0,06 | €0,24 (2x) | **€-0,18** | -0.09% | €0,22 | €0,04 | 0.02% |
| kraken - kucoin | €200,00 | 2026-11-21 | 22.9 u | 12 | 12 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,32 | €-0,32 | -0.16% |
| kraken - kucoin | €200,00 | 2026-11-22 | 16.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,09 | €-0,09 | -0.05% |
| kraken - kucoin | €2.000,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €2,19 | €2,19 | 0.11% |
| kraken - kucoin | €2.000,00 | 2026-11-20 | 22.8 u | 15 | 13 | 2 | €0,61 | €1,24 (3x) | **€-0,63** | -0.03% | €2,19 | €1,56 | 0.08% |
| kraken - kucoin | €2.000,00 | 2026-11-21 | 22.9 u | 12 | 12 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,24 | €-3,24 | -0.16% |
| kraken - kucoin | €2.000,00 | 2026-11-22 | 16.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,93 | €-0,93 | -0.05% |
| kraken - kucoin | €5.000,00 | 2026-11-19 | 14.9 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €5,49 | €5,49 | 0.11% |
| kraken - kucoin | €5.000,00 | 2026-11-20 | 22.8 u | 15 | 13 | 2 | €1,53 | €1,24 (3x) | **€0,28** | 0.01% | €5,48 | €5,77 | 0.12% |
| kraken - kucoin | €5.000,00 | 2026-11-21 | 22.9 u | 12 | 12 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-8,09 | €-8,09 | -0.16% |
| kraken - kucoin | €5.000,00 | 2026-11-22 | 16.3 u | 0 | 0 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,33 | €-2,33 | -0.05% |

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
- bitvavo - kraken, €100,00: munten AVA, CVX, CYBER, DYM, GMT, KERNEL, LUNA, MERL, MLN, PROMPT, VELO; bruto zonder voorraadgrens zou €5.209,76 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitvavo - kraken, €150,00: munten AVA, CVX, CYBER, DYM, GMT, KERNEL, LUNA, MERL, MLN, PROMPT, VELO; bruto zonder voorraadgrens zou €5.209,76 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitvavo - kraken, €200,00: munten AVA, CVX, CYBER, DYM, GMT, KERNEL, LUNA, MERL, MLN, PROMPT, VELO; bruto zonder voorraadgrens zou €5.209,76 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitvavo - kraken, €2.000,00: munten AVA, CVX, CYBER, DYM, GMT, KERNEL, LUNA, MERL, MLN, PROMPT, VELO; bruto zonder voorraadgrens zou €5.163,39 zijn, met voorraad €55,66 (GEZIEN boek, GOK model).
- bitvavo - kraken, €5.000,00: munten AVA, CVX, CYBER, DYM, GMT, KERNEL, LUNA, MERL, MLN, PROMPT, VELO; bruto zonder voorraadgrens zou €5.089,09 zijn, met voorraad €147,41 (GEZIEN boek, GOK model).
- bitvavo - kucoin, €100,00: munten ETH, USDC; bruto zonder voorraadgrens zou €19,28 zijn, met voorraad €0,04 (GEZIEN boek, GOK model).
- bitvavo - kucoin, €150,00: munten ETH, USDC; bruto zonder voorraadgrens zou €19,28 zijn, met voorraad €0,07 (GEZIEN boek, GOK model).
- bitvavo - kucoin, €200,00: munten ETH, USDC; bruto zonder voorraadgrens zou €19,28 zijn, met voorraad €0,09 (GEZIEN boek, GOK model).
- bitvavo - kucoin, €2.000,00: munten ETH, USDC; bruto zonder voorraadgrens zou €19,28 zijn, met voorraad €0,91 (GEZIEN boek, GOK model).
- bitvavo - kucoin, €5.000,00: munten ETH, USDC; bruto zonder voorraadgrens zou €19,28 zijn, met voorraad €2,24 (GEZIEN boek, GOK model).
- gate - kucoin, €100,00: munten ALKIMI, AVAIL, BARD, CCD, CHR, CWEB, CYBER, EDEN, ENSO, ERG, ESPORTS, EVAA, FTT, HIGH, HTR, IKA, IR, JST, KYO, LUNC, NAKA, NIM, OVR, POKT, POND, RARI, SD, SOUL, STREAM, SUPRA, USDS, USTC, VERONA, XU3O8; bruto zonder voorraadgrens zou €463,87 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- gate - kucoin, €150,00: munten ALKIMI, AVAIL, BARD, CCD, CHR, CWEB, CYBER, EDEN, ENSO, ERG, ESPORTS, EVAA, FTT, HIGH, HTR, IKA, IR, JST, KYO, LUNC, NAKA, NIM, OVR, POKT, POND, RARI, SD, SOUL, STREAM, SUPRA, USDS, USTC, VERONA, XU3O8; bruto zonder voorraadgrens zou €463,87 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- gate - kucoin, €200,00: munten ALKIMI, AVAIL, BARD, CCD, CHR, CWEB, CYBER, EDEN, ENSO, ERG, ESPORTS, EVAA, FTT, HIGH, HTR, IKA, IR, JST, KYO, LUNC, NAKA, NIM, OVR, POKT, POND, RARI, SD, SOUL, STREAM, SUPRA, USDS, USTC, VERONA, XU3O8; bruto zonder voorraadgrens zou €463,87 zijn, met voorraad €0,22 (GEZIEN boek, GOK model).
- gate - kucoin, €2.000,00: munten ALKIMI, AVAIL, BARD, CCD, CHR, CWEB, CYBER, EDEN, ENSO, ERG, ESPORTS, EVAA, FTT, HIGH, HTR, IKA, IR, JST, KYO, LUNC, NAKA, NIM, OVR, POKT, POND, RARI, SD, SOUL, STREAM, SUPRA, USDS, USTC, VERONA, XU3O8; bruto zonder voorraadgrens zou €462,62 zijn, met voorraad €12,14 (GEZIEN boek, GOK model).
- gate - kucoin, €5.000,00: munten ALKIMI, AVAIL, BARD, CCD, CHR, CWEB, CYBER, EDEN, ENSO, ERG, ESPORTS, EVAA, FTT, HIGH, HTR, IKA, IR, JST, KYO, LUNC, NAKA, NIM, OVR, POKT, POND, RARI, SD, SOUL, STREAM, SUPRA, USDS, USTC, VERONA, XU3O8; bruto zonder voorraadgrens zou €459,39 zijn, met voorraad €43,65 (GEZIEN boek, GOK model).
- kraken - kucoin, €100,00: munten USDC, USDT; bruto zonder voorraadgrens zou €120,83 zijn, met voorraad €0,03 (GEZIEN boek, GOK model).
- kraken - kucoin, €150,00: munten USDC, USDT; bruto zonder voorraadgrens zou €120,83 zijn, met voorraad €0,05 (GEZIEN boek, GOK model).
- kraken - kucoin, €200,00: munten USDC, USDT; bruto zonder voorraadgrens zou €120,82 zijn, met voorraad €0,06 (GEZIEN boek, GOK model).
- kraken - kucoin, €2.000,00: munten USDC, USDT; bruto zonder voorraadgrens zou €120,54 zijn, met voorraad €0,61 (GEZIEN boek, GOK model).
- kraken - kucoin, €5.000,00: munten USDC, USDT; bruto zonder voorraadgrens zou €120,08 zijn, met voorraad €1,53 (GEZIEN boek, GOK model).

### Met minstens één grijze beurs (de 5 paren met de meeste bruto winst)

| Beurspaar | Inleg | Dag | Gemeten | Kansen | Gemist (geen voorraad) | Kleiner door voorraad | Bruto winst | Kosten terugschuiven | **Netto handel (bruto min kosten)** | Rendement handel | Koerseffect voorraad | Netto met koerseffect | Rendement met koerseffect |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| gate - htx | €100,00 | 2026-11-19 | 14.9 u | 19 | 19 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,02 | €-1,02 | -1.02% |
| gate - htx | €100,00 | 2026-11-20 | 22.8 u | 32 | 32 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,73 | €-2,73 | -2.73% |
| gate - htx | €100,00 | 2026-11-21 | 22.9 u | 36 | 36 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,36 | €0,36 | 0.36% |
| gate - htx | €100,00 | 2026-11-22 | 16.3 u | 28 | 28 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,12 | €-0,12 | -0.12% |
| gate - htx | €150,00 | 2026-11-19 | 14.9 u | 19 | 19 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,53 | €-1,53 | -1.02% |
| gate - htx | €150,00 | 2026-11-20 | 22.8 u | 32 | 32 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-4,10 | €-4,10 | -2.73% |
| gate - htx | €150,00 | 2026-11-21 | 22.9 u | 36 | 36 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,54 | €0,54 | 0.36% |
| gate - htx | €150,00 | 2026-11-22 | 16.3 u | 28 | 28 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,17 | €-0,17 | -0.12% |
| gate - htx | €200,00 | 2026-11-19 | 14.9 u | 19 | 19 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,04 | €-2,04 | -1.02% |
| gate - htx | €200,00 | 2026-11-20 | 22.8 u | 32 | 32 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-5,47 | €-5,47 | -2.73% |
| gate - htx | €200,00 | 2026-11-21 | 22.9 u | 36 | 36 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,72 | €0,72 | 0.36% |
| gate - htx | €200,00 | 2026-11-22 | 16.3 u | 28 | 28 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,23 | €-0,23 | -0.12% |
| gate - htx | €2.000,00 | 2026-11-19 | 14.9 u | 19 | 14 | 5 | €0,45 | €0,00 (0x) | **€0,45** | 0.02% | €-20,36 | €-19,91 | -1.00% |
| gate - htx | €2.000,00 | 2026-11-20 | 22.8 u | 32 | 20 | 12 | €2,67 | €0,00 (1x) | **€2,67** | 0.13% | €-54,69 | €-52,02 | -2.60% |
| gate - htx | €2.000,00 | 2026-11-21 | 22.9 u | 36 | 30 | 6 | €0,58 | €0,07 (6x) | **€0,51** | 0.03% | €7,20 | €7,71 | 0.39% |
| gate - htx | €2.000,00 | 2026-11-22 | 16.3 u | 28 | 15 | 13 | €1,06 | €0,33 (11x) | **€0,73** | 0.04% | €-2,30 | €-1,57 | -0.08% |
| gate - htx | €5.000,00 | 2026-11-19 | 14.9 u | 19 | 14 | 5 | €1,13 | €0,17 (1x) | **€0,96** | 0.02% | €-50,90 | €-49,94 | -1.00% |
| gate - htx | €5.000,00 | 2026-11-20 | 22.8 u | 32 | 12 | 20 | €8,36 | €0,66 (8x) | **€7,70** | 0.15% | €-136,72 | €-129,02 | -2.58% |
| gate - htx | €5.000,00 | 2026-11-21 | 22.9 u | 36 | 13 | 23 | €5,69 | €1,23 (15x) | **€4,46** | 0.09% | €17,98 | €22,45 | 0.45% |
| gate - htx | €5.000,00 | 2026-11-22 | 16.3 u | 28 | 5 | 23 | €6,75 | €2,47 (21x) | **€4,28** | 0.09% | €-5,78 | €-1,49 | -0.03% |
| htx - kucoin | €100,00 | 2026-11-19 | 14.9 u | 16 | 16 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,45 | €-1,45 | -1.45% |
| htx - kucoin | €100,00 | 2026-11-20 | 22.8 u | 42 | 42 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,03 | €-3,03 | -3.03% |
| htx - kucoin | €100,00 | 2026-11-21 | 22.9 u | 32 | 32 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,19 | €0,19 | 0.19% |
| htx - kucoin | €100,00 | 2026-11-22 | 16.3 u | 32 | 32 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,02 | €-0,02 | -0.02% |
| htx - kucoin | €150,00 | 2026-11-19 | 14.9 u | 16 | 16 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,17 | €-2,17 | -1.45% |
| htx - kucoin | €150,00 | 2026-11-20 | 22.8 u | 42 | 42 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-4,55 | €-4,55 | -3.03% |
| htx - kucoin | €150,00 | 2026-11-21 | 22.9 u | 32 | 32 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,29 | €0,29 | 0.19% |
| htx - kucoin | €150,00 | 2026-11-22 | 16.3 u | 32 | 32 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,03 | €-0,03 | -0.02% |
| htx - kucoin | €200,00 | 2026-11-19 | 14.9 u | 16 | 16 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,90 | €-2,90 | -1.45% |
| htx - kucoin | €200,00 | 2026-11-20 | 22.8 u | 42 | 42 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-6,06 | €-6,06 | -3.03% |
| htx - kucoin | €200,00 | 2026-11-21 | 22.9 u | 32 | 32 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,39 | €0,39 | 0.19% |
| htx - kucoin | €200,00 | 2026-11-22 | 16.3 u | 32 | 32 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,04 | €-0,04 | -0.02% |
| htx - kucoin | €2.000,00 | 2026-11-19 | 14.9 u | 16 | 15 | 1 | €0,01 | €0,00 (0x) | **€0,01** | 0.00% | €-28,96 | €-28,95 | -1.45% |
| htx - kucoin | €2.000,00 | 2026-11-20 | 22.8 u | 42 | 42 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-60,63 | €-60,63 | -3.03% |
| htx - kucoin | €2.000,00 | 2026-11-21 | 22.9 u | 32 | 32 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €3,89 | €3,89 | 0.19% |
| htx - kucoin | €2.000,00 | 2026-11-22 | 16.3 u | 32 | 30 | 2 | €0,90 | €0,00 (0x) | **€0,90** | 0.04% | €-0,40 | €0,50 | 0.02% |
| htx - kucoin | €5.000,00 | 2026-11-19 | 14.9 u | 16 | 8 | 8 | €2,51 | €0,18 (2x) | **€2,33** | 0.05% | €-72,37 | €-70,04 | -1.40% |
| htx - kucoin | €5.000,00 | 2026-11-20 | 22.8 u | 42 | 23 | 19 | €9,47 | €0,60 (4x) | **€8,87** | 0.18% | €-151,58 | €-142,72 | -2.85% |
| htx - kucoin | €5.000,00 | 2026-11-21 | 22.9 u | 32 | 12 | 20 | €3,96 | €0,47 (6x) | **€3,49** | 0.07% | €9,70 | €13,18 | 0.26% |
| htx - kucoin | €5.000,00 | 2026-11-22 | 16.3 u | 32 | 19 | 13 | €6,04 | €0,93 (7x) | **€5,11** | 0.10% | €-0,99 | €4,11 | 0.08% |
| bitget - htx | €100,00 | 2026-11-19 | 14.9 u | 20 | 20 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €100,00 | 2026-11-20 | 22.8 u | 39 | 39 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €100,00 | 2026-11-21 | 22.9 u | 47 | 47 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €100,00 | 2026-11-22 | 16.3 u | 33 | 33 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €150,00 | 2026-11-19 | 14.9 u | 20 | 20 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €150,00 | 2026-11-20 | 22.8 u | 39 | 39 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €150,00 | 2026-11-21 | 22.9 u | 47 | 47 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €150,00 | 2026-11-22 | 16.3 u | 33 | 33 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €200,00 | 2026-11-19 | 14.9 u | 20 | 20 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €200,00 | 2026-11-20 | 22.8 u | 39 | 39 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €200,00 | 2026-11-21 | 22.9 u | 47 | 47 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €200,00 | 2026-11-22 | 16.3 u | 33 | 33 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €2.000,00 | 2026-11-19 | 14.9 u | 20 | 20 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €2.000,00 | 2026-11-20 | 22.8 u | 39 | 39 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €2.000,00 | 2026-11-21 | 22.9 u | 47 | 47 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | onbekend | onbekend* | onbekend* |
| bitget - htx | €2.000,00 | 2026-11-22 | 16.3 u | 33 | 31 | 2 | €0,84 | €0,00 (0x) | **€0,84** | 0.04% | onbekend | onbekend* | onbekend* |
| bitget - htx | €5.000,00 | 2026-11-19 | 14.9 u | 20 | 6 | 14 | €1,52 | €0,70 (10x) | **€0,82** | 0.02% | onbekend | onbekend* | onbekend* |
| bitget - htx | €5.000,00 | 2026-11-20 | 22.8 u | 39 | 8 | 31 | €8,32 | €0,64 (26x) | **€7,68** | 0.15% | onbekend | onbekend* | onbekend* |
| bitget - htx | €5.000,00 | 2026-11-21 | 22.9 u | 47 | 8 | 39 | €4,68 | €1,59 (31x) | **€3,09** | 0.06% | onbekend | onbekend* | onbekend* |
| bitget - htx | €5.000,00 | 2026-11-22 | 16.3 u | 33 | 13 | 20 | €4,04 | €0,86 (17x) | **€3,19** | 0.06% | onbekend | onbekend* | onbekend* |
| htx - xt | €100,00 | 2026-11-19 | 14.9 u | 18 | 18 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,09 | €-1,09 | -1.09% |
| htx - xt | €100,00 | 2026-11-20 | 22.8 u | 17 | 17 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,65 | €-2,65 | -2.65% |
| htx - xt | €100,00 | 2026-11-21 | 22.9 u | 15 | 15 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,17 | €0,17 | 0.17% |
| htx - xt | €100,00 | 2026-11-22 | 16.3 u | 14 | 14 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,48 | €-0,48 | -0.48% |
| htx - xt | €150,00 | 2026-11-19 | 14.9 u | 18 | 18 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,64 | €-1,64 | -1.09% |
| htx - xt | €150,00 | 2026-11-20 | 22.8 u | 17 | 17 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-3,97 | €-3,97 | -2.65% |
| htx - xt | €150,00 | 2026-11-21 | 22.9 u | 15 | 15 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,26 | €0,26 | 0.17% |
| htx - xt | €150,00 | 2026-11-22 | 16.3 u | 14 | 14 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,72 | €-0,72 | -0.48% |
| htx - xt | €200,00 | 2026-11-19 | 14.9 u | 18 | 18 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-2,18 | €-2,18 | -1.09% |
| htx - xt | €200,00 | 2026-11-20 | 22.8 u | 17 | 17 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-5,29 | €-5,29 | -2.65% |
| htx - xt | €200,00 | 2026-11-21 | 22.9 u | 15 | 15 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €0,34 | €0,34 | 0.17% |
| htx - xt | €200,00 | 2026-11-22 | 16.3 u | 14 | 14 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,96 | €-0,96 | -0.48% |
| htx - xt | €2.000,00 | 2026-11-19 | 14.9 u | 18 | 14 | 4 | €0,73 | €0,00 (0x) | **€0,73** | 0.04% | €-21,82 | €-21,09 | -1.05% |
| htx - xt | €2.000,00 | 2026-11-20 | 22.8 u | 17 | 9 | 8 | €4,37 | €0,12 (2x) | **€4,25** | 0.21% | €-52,91 | €-48,66 | -2.43% |
| htx - xt | €2.000,00 | 2026-11-21 | 22.9 u | 15 | 7 | 8 | €3,41 | €0,01 (1x) | **€3,40** | 0.17% | €3,44 | €6,85 | 0.34% |
| htx - xt | €2.000,00 | 2026-11-22 | 16.3 u | 14 | 9 | 5 | €1,72 | €0,11 (1x) | **€1,61** | 0.08% | €-9,55 | €-7,94 | -0.40% |
| htx - xt | €5.000,00 | 2026-11-19 | 14.9 u | 18 | 5 | 13 | €7,05 | €4,30 (11x) | **€2,75** | 0.05% | €-54,59 | €-51,85 | -1.04% |
| htx - xt | €5.000,00 | 2026-11-20 | 22.8 u | 17 | 2 | 15 | €15,67 | €2,81 (9x) | **€12,86** | 0.26% | €-131,99 | €-119,13 | -2.38% |
| htx - xt | €5.000,00 | 2026-11-21 | 22.9 u | 15 | 2 | 13 | €10,98 | €1,93 (6x) | **€9,05** | 0.18% | €9,29 | €18,33 | 0.37% |
| htx - xt | €5.000,00 | 2026-11-22 | 16.3 u | 14 | 6 | 8 | €5,20 | €1,27 (4x) | **€3,94** | 0.08% | €-23,66 | €-19,73 | -0.39% |
| kucoin - xt | €100,00 | 2026-11-19 | 14.9 u | 13 | 13 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,04 | €-0,04 | -0.04% |
| kucoin - xt | €100,00 | 2026-11-20 | 22.8 u | 10 | 10 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,34 | €-0,34 | -0.34% |
| kucoin - xt | €100,00 | 2026-11-21 | 22.9 u | 9 | 9 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €1,21 | €1,21 | 1.21% |
| kucoin - xt | €100,00 | 2026-11-22 | 16.3 u | 6 | 6 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,84 | €-0,84 | -0.84% |
| kucoin - xt | €150,00 | 2026-11-19 | 14.9 u | 13 | 13 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,06 | €-0,06 | -0.04% |
| kucoin - xt | €150,00 | 2026-11-20 | 22.8 u | 10 | 10 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,51 | €-0,51 | -0.34% |
| kucoin - xt | €150,00 | 2026-11-21 | 22.9 u | 9 | 9 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €1,81 | €1,81 | 1.21% |
| kucoin - xt | €150,00 | 2026-11-22 | 16.3 u | 6 | 6 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,26 | €-1,26 | -0.84% |
| kucoin - xt | €200,00 | 2026-11-19 | 14.9 u | 13 | 13 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,08 | €-0,08 | -0.04% |
| kucoin - xt | €200,00 | 2026-11-20 | 22.8 u | 10 | 10 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-0,67 | €-0,67 | -0.34% |
| kucoin - xt | €200,00 | 2026-11-21 | 22.9 u | 9 | 8 | 1 | €0,08 | €0,00 (0x) | **€0,08** | 0.04% | €2,42 | €2,50 | 1.25% |
| kucoin - xt | €200,00 | 2026-11-22 | 16.3 u | 6 | 6 | 0 | €0,00 | €0,00 (0x) | **€0,00** | 0.00% | €-1,68 | €-1,68 | -0.84% |
| kucoin - xt | €2.000,00 | 2026-11-19 | 14.9 u | 13 | 4 | 9 | €7,46 | €3,63 (9x) | **€3,84** | 0.19% | €-0,84 | €3,00 | 0.15% |
| kucoin - xt | €2.000,00 | 2026-11-20 | 22.8 u | 10 | 2 | 8 | €6,79 | €2,27 (6x) | **€4,52** | 0.23% | €-6,62 | €-2,10 | -0.10% |
| kucoin - xt | €2.000,00 | 2026-11-21 | 22.9 u | 9 | 2 | 7 | €7,31 | €2,19 (5x) | **€5,12** | 0.26% | €24,74 | €29,86 | 1.49% |
| kucoin - xt | €2.000,00 | 2026-11-22 | 16.3 u | 6 | 4 | 2 | €1,19 | €0,68 (2x) | **€0,51** | 0.03% | €-16,67 | €-16,16 | -0.81% |
| kucoin - xt | €5.000,00 | 2026-11-19 | 14.9 u | 13 | 3 | 10 | €17,66 | €5,47 (11x) | **€12,19** | 0.24% | €-2,02 | €10,17 | 0.20% |
| kucoin - xt | €5.000,00 | 2026-11-20 | 22.8 u | 10 | 1 | 8 | €16,90 | €6,07 (10x) | **€10,83** | 0.22% | €-16,83 | €-6,00 | -0.12% |
| kucoin - xt | €5.000,00 | 2026-11-21 | 22.9 u | 9 | 0 | 9 | €15,58 | €3,90 (7x) | **€11,68** | 0.23% | €60,55 | €72,23 | 1.44% |
| kucoin - xt | €5.000,00 | 2026-11-22 | 16.3 u | 6 | 1 | 5 | €7,34 | €3,33 (5x) | **€4,01** | 0.08% | €-41,91 | €-37,90 | -0.76% |

- gate - htx, €100,00: munten AKT, ALGO, APEPE, APT, ATOM, BIO, BRISE, BSV, BTT, CBK, CELO, CORE, CRTS, CVX, ENJ, ENS, ENSO, GOMINING, GT, HBAR, HIVE, KAS, KCT, KSM, LAT, LINK, LUNC, MBX, MEGA, MEME, MOVR, NPC, PEOPLE, QNT, SAND, SC, SD, SEI, SHIB, SSV, VIRTUAL, WARD, WLD, XCH, XCN, XDC; bruto zonder voorraadgrens zou €545,09 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- gate - htx, €150,00: munten AKT, ALGO, APEPE, APT, ATOM, BIO, BRISE, BSV, BTT, CBK, CELO, CORE, CRTS, CVX, ENJ, ENS, ENSO, GOMINING, GT, HBAR, HIVE, KAS, KCT, KSM, LAT, LINK, LUNC, MBX, MEGA, MEME, MOVR, NPC, PEOPLE, QNT, SAND, SC, SD, SEI, SHIB, SSV, VIRTUAL, WARD, WLD, XCH, XCN, XDC; bruto zonder voorraadgrens zou €545,09 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- gate - htx, €200,00: munten AKT, ALGO, APEPE, APT, ATOM, BIO, BRISE, BSV, BTT, CBK, CELO, CORE, CRTS, CVX, ENJ, ENS, ENSO, GOMINING, GT, HBAR, HIVE, KAS, KCT, KSM, LAT, LINK, LUNC, MBX, MEGA, MEME, MOVR, NPC, PEOPLE, QNT, SAND, SC, SD, SEI, SHIB, SSV, VIRTUAL, WARD, WLD, XCH, XCN, XDC; bruto zonder voorraadgrens zou €545,09 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- gate - htx, €2.000,00: munten AKT, ALGO, APEPE, APT, ATOM, BIO, BRISE, BSV, BTT, CBK, CELO, CORE, CRTS, CVX, ENJ, ENS, ENSO, GOMINING, GT, HBAR, HIVE, KAS, KCT, KSM, LAT, LINK, LUNC, MBX, MEGA, MEME, MOVR, NPC, PEOPLE, QNT, SAND, SC, SD, SEI, SHIB, SSV, VIRTUAL, WARD, WLD, XCH, XCN, XDC; bruto zonder voorraadgrens zou €545,03 zijn, met voorraad €4,76 (GEZIEN boek, GOK model).
- gate - htx, €5.000,00: munten AKT, ALGO, APEPE, APT, ATOM, BIO, BRISE, BSV, BTT, CBK, CELO, CORE, CRTS, CVX, ENJ, ENS, ENSO, GOMINING, GT, HBAR, HIVE, KAS, KCT, KSM, LAT, LINK, LUNC, MBX, MEGA, MEME, MOVR, NPC, PEOPLE, QNT, SAND, SC, SD, SEI, SHIB, SSV, VIRTUAL, WARD, WLD, XCH, XCN, XDC; bruto zonder voorraadgrens zou €544,40 zijn, met voorraad €21,93 (GEZIEN boek, GOK model).
- htx - kucoin, €100,00: munten ACN, AI, ALGO, ANIME, APT, ATOM, BIO, BONK, BRISE, BSV, BTT, CELO, CFX, CHIP, CVX, DYDX, ELA, ENJ, ENS, ENSO, FET, JASMY, JST, KSM, LAT, LTC, LUNC, MEME, MINA, MOVR, NPC, ONE, PEOPLE, QNT, SAND, SD, SHIB, SOMI, SSV, TRAC, VIRTUAL, WAN, WARD, WIN, WLD, XCH, XCN, XEC, XMR, XTZ; bruto zonder voorraadgrens zou €592,65 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - kucoin, €150,00: munten ACN, AI, ALGO, ANIME, APT, ATOM, BIO, BONK, BRISE, BSV, BTT, CELO, CFX, CHIP, CVX, DYDX, ELA, ENJ, ENS, ENSO, FET, JASMY, JST, KSM, LAT, LTC, LUNC, MEME, MINA, MOVR, NPC, ONE, PEOPLE, QNT, SAND, SD, SHIB, SOMI, SSV, TRAC, VIRTUAL, WAN, WARD, WIN, WLD, XCH, XCN, XEC, XMR, XTZ; bruto zonder voorraadgrens zou €592,65 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - kucoin, €200,00: munten ACN, AI, ALGO, ANIME, APT, ATOM, BIO, BONK, BRISE, BSV, BTT, CELO, CFX, CHIP, CVX, DYDX, ELA, ENJ, ENS, ENSO, FET, JASMY, JST, KSM, LAT, LTC, LUNC, MEME, MINA, MOVR, NPC, ONE, PEOPLE, QNT, SAND, SD, SHIB, SOMI, SSV, TRAC, VIRTUAL, WAN, WARD, WIN, WLD, XCH, XCN, XEC, XMR, XTZ; bruto zonder voorraadgrens zou €592,65 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - kucoin, €2.000,00: munten ACN, AI, ALGO, ANIME, APT, ATOM, BIO, BONK, BRISE, BSV, BTT, CELO, CFX, CHIP, CVX, DYDX, ELA, ENJ, ENS, ENSO, FET, JASMY, JST, KSM, LAT, LTC, LUNC, MEME, MINA, MOVR, NPC, ONE, PEOPLE, QNT, SAND, SD, SHIB, SOMI, SSV, TRAC, VIRTUAL, WAN, WARD, WIN, WLD, XCH, XCN, XEC, XMR, XTZ; bruto zonder voorraadgrens zou €592,65 zijn, met voorraad €0,91 (GEZIEN boek, GOK model).
- htx - kucoin, €5.000,00: munten ACN, AI, ALGO, ANIME, APT, ATOM, BIO, BONK, BRISE, BSV, BTT, CELO, CFX, CHIP, CVX, DYDX, ELA, ENJ, ENS, ENSO, FET, JASMY, JST, KSM, LAT, LTC, LUNC, MEME, MINA, MOVR, NPC, ONE, PEOPLE, QNT, SAND, SD, SHIB, SOMI, SSV, TRAC, VIRTUAL, WAN, WARD, WIN, WLD, XCH, XCN, XEC, XMR, XTZ; bruto zonder voorraadgrens zou €591,75 zijn, met voorraad €21,99 (GEZIEN boek, GOK model).
- bitget - htx, €100,00: munten AB, ACN, AI, ALGO, ANIME, ATOM, BABY, BIO, BONK, BSV, BTT, CBK, CFX, CORE, DYDX, ENA, ENJ, ENS, ENSO, HBAR, HIVE, IOST, JASMY, KAS, KSM, LAT, LINK, LIT, LUNA, LUNC, M, MEME, MINA, MOVR, NPC, O, PCI, PEOPLE, QNT, RIVER, SAND, SHIB, SOMI, SSV, TAO, TIA, TLOS, USTC, VIRTUAL, WARD, WLD, XDC, XTZ, ZEN; bruto zonder voorraadgrens zou €546,85 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - htx, €150,00: munten AB, ACN, AI, ALGO, ANIME, ATOM, BABY, BIO, BONK, BSV, BTT, CBK, CFX, CORE, DYDX, ENA, ENJ, ENS, ENSO, HBAR, HIVE, IOST, JASMY, KAS, KSM, LAT, LINK, LIT, LUNA, LUNC, M, MEME, MINA, MOVR, NPC, O, PCI, PEOPLE, QNT, RIVER, SAND, SHIB, SOMI, SSV, TAO, TIA, TLOS, USTC, VIRTUAL, WARD, WLD, XDC, XTZ, ZEN; bruto zonder voorraadgrens zou €546,85 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - htx, €200,00: munten AB, ACN, AI, ALGO, ANIME, ATOM, BABY, BIO, BONK, BSV, BTT, CBK, CFX, CORE, DYDX, ENA, ENJ, ENS, ENSO, HBAR, HIVE, IOST, JASMY, KAS, KSM, LAT, LINK, LIT, LUNA, LUNC, M, MEME, MINA, MOVR, NPC, O, PCI, PEOPLE, QNT, RIVER, SAND, SHIB, SOMI, SSV, TAO, TIA, TLOS, USTC, VIRTUAL, WARD, WLD, XDC, XTZ, ZEN; bruto zonder voorraadgrens zou €546,85 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- bitget - htx, €2.000,00: munten AB, ACN, AI, ALGO, ANIME, ATOM, BABY, BIO, BONK, BSV, BTT, CBK, CFX, CORE, DYDX, ENA, ENJ, ENS, ENSO, HBAR, HIVE, IOST, JASMY, KAS, KSM, LAT, LINK, LIT, LUNA, LUNC, M, MEME, MINA, MOVR, NPC, O, PCI, PEOPLE, QNT, RIVER, SAND, SHIB, SOMI, SSV, TAO, TIA, TLOS, USTC, VIRTUAL, WARD, WLD, XDC, XTZ, ZEN; bruto zonder voorraadgrens zou €546,85 zijn, met voorraad €0,84 (GEZIEN boek, GOK model).
- bitget - htx, €5.000,00: munten AB, ACN, AI, ALGO, ANIME, ATOM, BABY, BIO, BONK, BSV, BTT, CBK, CFX, CORE, DYDX, ENA, ENJ, ENS, ENSO, HBAR, HIVE, IOST, JASMY, KAS, KSM, LAT, LINK, LIT, LUNA, LUNC, M, MEME, MINA, MOVR, NPC, O, PCI, PEOPLE, QNT, RIVER, SAND, SHIB, SOMI, SSV, TAO, TIA, TLOS, USTC, VIRTUAL, WARD, WLD, XDC, XTZ, ZEN; bruto zonder voorraadgrens zou €546,08 zijn, met voorraad €18,56 (GEZIEN boek, GOK model).
- htx - xt, €100,00: munten ALGO, APEPE, APT, BIO, BSV, CARV, CBK, CELO, CFX, GT, HBAR, KSM, LUNC, MEME, MINA, PEOPLE, RAIN, SC, SEI, SHIB, XCH, XDC, XMR; bruto zonder voorraadgrens zou €797,59 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - xt, €150,00: munten ALGO, APEPE, APT, BIO, BSV, CARV, CBK, CELO, CFX, GT, HBAR, KSM, LUNC, MEME, MINA, PEOPLE, RAIN, SC, SEI, SHIB, XCH, XDC, XMR; bruto zonder voorraadgrens zou €797,59 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - xt, €200,00: munten ALGO, APEPE, APT, BIO, BSV, CARV, CBK, CELO, CFX, GT, HBAR, KSM, LUNC, MEME, MINA, PEOPLE, RAIN, SC, SEI, SHIB, XCH, XDC, XMR; bruto zonder voorraadgrens zou €797,59 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- htx - xt, €2.000,00: munten ALGO, APEPE, APT, BIO, BSV, CARV, CBK, CELO, CFX, GT, HBAR, KSM, LUNC, MEME, MINA, PEOPLE, RAIN, SC, SEI, SHIB, XCH, XDC, XMR; bruto zonder voorraadgrens zou €797,33 zijn, met voorraad €10,23 (GEZIEN boek, GOK model).
- htx - xt, €5.000,00: munten ALGO, APEPE, APT, BIO, BSV, CARV, CBK, CELO, CFX, GT, HBAR, KSM, LUNC, MEME, MINA, PEOPLE, RAIN, SC, SEI, SHIB, XCH, XDC, XMR; bruto zonder voorraadgrens zou €795,85 zijn, met voorraad €38,90 (GEZIEN boek, GOK model).
- kucoin - xt, €100,00: munten BARD, DAG, ENSO, FIGHT, LUNC, USDS, XMR; bruto zonder voorraadgrens zou €1.324,03 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- kucoin - xt, €150,00: munten BARD, DAG, ENSO, FIGHT, LUNC, USDS, XMR; bruto zonder voorraadgrens zou €1.324,03 zijn, met voorraad €0,00 (GEZIEN boek, GOK model).
- kucoin - xt, €200,00: munten BARD, DAG, ENSO, FIGHT, LUNC, USDS, XMR; bruto zonder voorraadgrens zou €1.324,03 zijn, met voorraad €0,08 (GEZIEN boek, GOK model).
- kucoin - xt, €2.000,00: munten BARD, DAG, ENSO, FIGHT, LUNC, USDS, XMR; bruto zonder voorraadgrens zou €1.321,09 zijn, met voorraad €22,75 (GEZIEN boek, GOK model).
- kucoin - xt, €5.000,00: munten BARD, DAG, ENSO, FIGHT, LUNC, USDS, XMR; bruto zonder voorraadgrens zou €1.317,11 zijn, met voorraad €57,47 (GEZIEN boek, GOK model).

### Andere keuzes bij bitvavo - kraken (netto handel, alle dagen samen; GOK)

| Keuze | Inleg | Kansen | Gemist | Bruto winst | Kosten terugschuiven | Netto handel |
|---|---|---|---|---|---|---|
| standaard (schuifdrempel 25%, kostengrens 1%) | €150,00 | 108 | 108 | €0,00 | €0,00 | **€0,00** |
| standaard (schuifdrempel 25%, kostengrens 1%) | €2.000,00 | 108 | 62 | €55,66 | €16,38 | **€39,28** |
| schuifdrempel 10% | €150,00 | 108 | 108 | €0,00 | €0,00 | **€0,00** |
| schuifdrempel 10% | €2.000,00 | 108 | 63 | €54,86 | €16,06 | **€38,80** |
| schuifdrempel 40% | €150,00 | 108 | 108 | €0,00 | €0,00 | **€0,00** |
| schuifdrempel 40% | €2.000,00 | 108 | 62 | €55,66 | €17,38 | **€38,28** |
| kostengrens 2% (achteraf vergeleken) | €150,00 | 108 | 108 | €0,00 | €0,00 | **€0,00** |
| kostengrens 2% (achteraf vergeleken) | €2.000,00 | 108 | 62 | €55,66 | €17,97 | **€37,69** |
| kostengrens 5% (achteraf vergeleken) | €150,00 | 108 | 108 | €0,00 | €0,00 | **€0,00** |
| kostengrens 5% (achteraf vergeleken) | €2.000,00 | 108 | 30 | €58,71 | €58,07 | **€0,64** |
| alleen MERL en KERNEL (meer voorraad per munt, achteraf gekozen) | €150,00 | 46 | 44 | €2,05 | €0,00 | **€2,05** |
| alleen MERL en KERNEL (meer voorraad per munt, achteraf gekozen) | €2.000,00 | 46 | 16 | €255,47 | €20,03 | **€235,44** |

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

- Opnamekosten bij de echte kansen: 363 van een netwerk dat aan beide kanten open is, 232 van de beurs zelf (laagste open netwerk), 137 geschat uit wat andere beurzen voor die munt vragen (GOK). Onbekende opnamekosten tellen niet als echte kans.
- Netwerk: KuCoin, Gate, Bitget, HTX, XT, Bitstamp, Bitvavo en Poloniex geven hun netwerken per munt. Als beide beurzen dat doen en de namen te koppelen zijn, moet er een netwerk zijn dat aan beide kanten open is. Anders is het netwerk "niet te koppelen" en telt de kans mee (staat apart in de trechter).
- De duur is gemeten in stappen van ±20 seconden; een kans kan een paar rondes eerder begonnen zijn dan we zagen.
- Takerkosten: uit de API waar die ze per paar geeft, anders het standaardtarief uit de README (deels GOK).
- Laatste run: 15 beurzen antwoordden, 2270 munt-quote-paren op minstens twee beurzen (GEZIEN).
