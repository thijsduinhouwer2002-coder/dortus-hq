# Driehoek-meter: rapport

## Kort antwoord

Op de beurzen met vergunning (MiCA, ook via een EU-dochter): 35 echte kansen die met €100 konden (35 als je elke driehoek los telt; 48,0 per dag). Samen €153,12 tot €153,12 per dag met €100 en €305,07 tot €305,07 per dag met €200 (GOK; het lage getal voegt driehoeken samen die hetzelfde stukje boek willen, het hoge telt ze los; allebei alsof je ze allemaal als eerste pakt, met het geld al op de juiste beurs). Op de grijze beurzen (geen vergunning): 8 echte kansen die met €100 konden (14 als je elke driehoek los telt; 11,0 per dag). Samen €2,02 tot €4,58 per dag met €100 en €2,68 tot €5,55 per dag met €200 (GOK; het lage getal voegt driehoeken samen die hetzelfde stukje boek willen, het hoge telt ze los; allebei alsof je ze allemaal als eerste pakt, met het geld al op de juiste beurs).

Uitleg: **takerkosten** zijn wat de beurs per order rekent als je meteen koopt of verkoopt tegen de prijs die er ligt (0% tot 0,8% per order; een driehoek is drie orders). **Diepte** is hoeveel euro je tegen die winstgevende prijzen echt kunt kopen en verkopen voordat de prijs slechter wordt. Wij meten elke 3 tot 5 seconden; snelle bots pakken zulke kansen meestal binnen milliseconden, dus wat hier staat is wat er na hen overbleef.

Data: 195 driehoeken met winst op het boek gezien (ook kleine en korte), 2 dag(en) (2026-11-19 tot 2026-11-20). Gemeten: ±17,5 uur per beurs (GEZIEN, uit stand.jsonl).

Een **echte driehoek**: winst na drie keer takerkosten op het orderboek, op twee metingen die minstens 3 seconden uit elkaar liggen elk minstens €100 diepte, bij de latere meting minstens €0,05 winst, en niet meer dan 5% winst (verdacht). Alle bedragen zijn die van de latere meting: wat er na 3 seconden nog stond. Driehoeken op dezelfde beurs die binnen 5 seconden van elkaar bevestigd werden en een paar delen dat geen paar van twee hoofdmunten is (EUR, USD, USDT, USDC, BTC, ETH), tellen als **één kans** (de beste telt): ze willen hetzelfde stukje orderboek. Er wordt niet doorgeketend: een driehoek hoort alleen bij een kans als hij met elk lid ervan dat stukje deelt. Omdat samenvoegen ook te streng kan zijn, staan aantallen en geld er ook los geteld bij (bovengrens).

Regels van vóór 2026-11-19 16:07 UTC (vóór de keuring) hebben geen meting na 3 seconden en tellen daarom nooit als echt. Daar zat ook niets in dat 3 seconden met €100 diepte stond.

## Per beurs: hoe gemeten en hoe dicht bij winst

Beste marge = per ronde de beste driehoek tegen de beste prijzen na kosten (mediaan en hoogste over alle rondes). Negatief = zelfs de beste driehoek verloor geld. Kandidaten = driehoeken die met de beste prijzen winst gaven; daarvan haalt hij de orderboeken op (bekeken), tenzij het budget van die ronde op was (overgeslagen) of de koersen sinds de vorige controle niet veranderden (zelfde). Een positieve beste marge is nog geen winst: de bulk-koers kan achterlopen of er ligt maar een paar cent op die prijs; het orderboek beslist (kolom Winst op boek).

| Beurs | Status | Paren | Driehoeken | Uur | Rondes | Fouten (te veel) | Beste marge mediaan | Beste marge hoogst | Kandidaten | Bekeken | Overgeslagen | Zelfde | Winst op boek | Echt |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| bitget | grijs | 3658 | 202 | 17,5 | 20714 | 1 (0) | -0,283% | 0,344% | 396 | 332 | 0 | 64 | 0 | 0 |
| bitstamp | MiCA | 252 | 346 | 17,5 | 12438 | 0 (0) | -0,229% | 3,905% | 6818 | 6816 | 0 | 0 | 6751 | 31 |
| bitvavo | MiCA | 435 | 22 | 17,5 | 15549 | 1 (0) | -0,757% | -0,318% | 156 | 145 | 0 | 11 | 0 | 0 |
| gate | MiCA-dochter | 2153 | 372 | 17,5 | 15468 | 1 (0) | -0,151% | 2,127% | 4234 | 1754 | 14 | 2466 | 1 | 0 |
| kraken | MiCA | 1352 | 2352 | 17,5 | 12446 | 0 (0) | -0,202% | 3,182% | 4449 | 2789 | 1 | 1659 | 0 | 0 |
| kucoin | MiCA-dochter | 967 | 452 | 17,5 | 20744 | 0 (0) | 1,551% | 4,715% | 28021 | 10958 | 79 | 16982 | 0 | 0 |
| mexc | grijs | 1666 | 886 | 17,5 | 20729 | 0 (0) | 0,180% | 4,975% | 40490 | 21069 | 266 | 18987 | 772 | 14 |
| okx | MiCA-dochter | 1250 | 2338 | 17,5 | 20742 | 0 (0) | -0,142% | 4,743% | 8480 | 7603 | 37 | 840 | 779 | 4 |

## Trechter

| Stap | Alle beurzen | MiCA (ook via EU-dochter) | Grijs |
|---|---|---|---|
| winst op het boek, met de lage kosten (bovengrens) | 195 | 78 | 117 |
| winst op het boek, met de gewone kosten | 195 | 78 | 117 |
| en ooit minstens €100 diepte | 79 | 52 | 27 |
| en na 3 s nog steeds minstens €100 diepte | 58 | 44 | 14 |
| en dan minstens €0,05 winst | 58 | 44 | 14 |
| en niet verdacht = **echt** | 49 | 35 | 14 |
| echte **kansen** (samengevoegd als ze hetzelfde stukje boek willen; ondergrens) | 43 | 35 | 8 |

De lage kosten verschillen alleen bij Bitvavo (categorie B, C en D: USDC- en stablecoinparen; Bitvavo noemt ze lager dan 0,25% maar geeft geen getal, dus laag = 0%, GOK). Overal elders is laag gelijk aan gewoon.

## Per dag (echte kansen, bedragen na 3 seconden)

| Dag | Soort | Driehoeken | Kansen | Mediane winst per kans | Mediane diepte | Mediane duur met €100 diepte | Totale winst (volle diepte) |
|---|---|---|---|---|---|---|---|
| 2026-11-19 | Alle beurzen | 48 | 42 | €7,37 | €227 | 17,0 s | €280,75 |
| 2026-11-19 | MiCA (ook via EU-dochter) | 35 | 35 | €7,78 | €227 | 30,0 s | €253,08 |
| 2026-11-19 | Grijs | 13 | 7 | €0,49 | €694 | 7,0 s | €27,67 |
| 2026-11-20 | Alle beurzen | 1 | 1 | €0,38 | €1.000 | 14,0 s | €0,38 |
| 2026-11-20 | MiCA (ook via EU-dochter) | 0 | 0 | - | - | - | €0,00 |
| 2026-11-20 | Grijs | 1 | 1 | €0,38 | €1.000 | 14,0 s | €0,38 |
| totaal | Alle beurzen | 49 | 43 | €7,36 | €227 | 15,0 s | €281,13 |
| totaal | MiCA (ook via EU-dochter) | 35 | 35 | €7,78 | €227 | 30,0 s | €253,08 |
| totaal | Grijs | 14 | 8 | €0,44 | €847 | 7,0 s | €28,05 |

## Beste driehoeken per beurs (echt, bedragen na 3 seconden)

**bitstamp** (MiCA)

| Driehoek | Keren | Mediane winst | Hoogste winst | Mediane diepte | Mediane duur met €100 diepte | Kosten per stap |
|---|---|---|---|---|---|---|
| EUR>USD>SKY>EUR | 31 | €8,22 | €11,32 | €227 | 25,0 s | 0,08% + 0,40% + 0,40% |

**mexc** (grijs)

| Driehoek | Keren | Mediane winst | Hoogste winst | Mediane diepte | Mediane duur met €100 diepte | Kosten per stap |
|---|---|---|---|---|---|---|
| USDT>BTC>USDC>USDT | 2 | €12,85 | €20,12 | €35.093 | 10,0 s | 0,05% + 0,00% + 0,00% |
| USDT>XRP>BRL>USDT | 2 | €0,56 | €0,63 | €148 | 10,0 s | 0,00% + 0,05% + 0,08% |
| USDT>BTC>BRL>USDT | 2 | €0,40 | €0,64 | €146 | 10,0 s | 0,05% + 0,05% + 0,08% |
| USDT>ETH>BRL>USDT | 2 | €0,38 | €0,45 | €116 | 10,0 s | 0,05% + 0,05% + 0,08% |
| USDT>USDC>BRL>USDT | 2 | €0,29 | €0,34 | €131 | 5,0 s | 0,00% + 0,05% + 0,08% |

**okx** (MiCA-dochter)

| Driehoek | Keren | Mediane winst | Hoogste winst | Mediane diepte | Mediane duur met €100 diepte | Kosten per stap |
|---|---|---|---|---|---|---|
| USDT>XANT>USDC>USDT | 3 | €0,80 | €1,98 | €355 | 216,0 s | 0,10% + 0,10% + 0,10% |
| USDT>USDC>XANT>USDT | 1 | €1,75 | €1,75 | €284 | 156,0 s | 0,10% + 0,10% + 0,10% |

Grootste driehoeken die **niet** echt waren (te kort, te dun, te weinig winst of verdacht). Bedragen van het beste moment:

| Beurs | Driehoek | Winst | Diepte | Duur | Na 3 s nog €100 diepte | Verdacht |
|---|---|---|---|---|---|---|
| bitstamp | EUR>USD>SKY>EUR | €14,24 | €227 | 5 s | ja | ja |
| bitstamp | EUR>USD>SKY>EUR | €13,92 | €227 | 30 s | ja | ja |
| bitstamp | EUR>USD>SKY>EUR | €13,13 | €200 | 0 s | nee | ja |
| bitstamp | EUR>USD>SKY>EUR | €12,95 | €227 | 80 s | ja | ja |
| bitstamp | EUR>USD>SKY>EUR | €12,67 | €227 | 0 s | nee | ja |
| bitstamp | EUR>USD>SKY>EUR | €12,45 | €227 | 170 s | ja | ja |
| bitstamp | EUR>USD>SKY>EUR | €12,24 | €227 | 15 s | ja | ja |
| bitstamp | EUR>USD>SKY>EUR | €11,97 | €227 | 20 s | ja | ja |

## Kan een kleine inleg meedoen? (€100, €150, €200)

Minimale ordergrootte per paar uit de openbare API van elke beurs (aantal munten en bedrag in de quote; Bitget: waarde in USDT). Per beurs: hoeveel driehoeken je met dat bedrag kunt rondmaken zonder dat een van de drie orders onder het minimum valt (tegen de beste prijzen, GEZIEN). Het kleinste bedrag dat we toetsen is €10; "≤ €10" betekent dus €10 of minder. Het aantal munten wordt per order naar beneden afgerond op de stapgrootte van de beurs (uit de API), en bij Bitvavo rekenen we per euro-order €0,01 extra (Bitvavo rondt de kosten naar boven af op de cent).

| Beurs | Status | Driehoeken | Met EUR | Mediaan minimale inleg | Mogelijk met €100 | €150 | €200 | Met EUR en €100 |
|---|---|---|---|---|---|---|---|---|
| bitget | grijs | 202 | 46 | ≤ €10 | 202 | 202 | 202 | 46 |
| bitstamp | MiCA | 346 | 260 | €12 | 335 | 336 | 336 | 251 |
| bitvavo | MiCA | 22 | 22 | ≤ €10 | 22 | 22 | 22 | 22 |
| gate | MiCA-dochter | 372 | 0 | ≤ €10 | 372 | 372 | 372 | 0 |
| kraken | MiCA | 2352 | 1368 | ≤ €10 | 2352 | 2352 | 2352 | 1368 |
| kucoin | MiCA-dochter | 452 | 12 | ≤ €10 | 452 | 452 | 452 | 12 |
| mexc | grijs | 886 | 76 | ≤ €10 | 886 | 886 | 886 | 76 |
| okx | MiCA-dochter | 2338 | 1090 | ≤ €10 | 2334 | 2334 | 2334 | 1090 |

Van de 43 echte kansen konden er 43 met €100 (minimale ordergrootte gehaald op alle drie de orders, winst na 3 seconden).

## Opschaling naar €100, €150, €200, €2.000 en €5.000 inleg (GOK)

Per echte kans nemen we de winst die je bij die inleg na 3 seconden nog had kunnen maken (minder inleggen mag als het boek dunner is; alleen bedragen die de minimale ordergrootte halen). Opgeteld per gemeten dag en dan maal 30 voor een maand.

Elk getal staat er twee keer: **samengevoegd** (ondergrens: driehoeken die op hetzelfde moment, binnen 5 seconden na hun bevestiging, hetzelfde niet-hoofdpaar gebruiken, tellen als één kans; een paar van twee hoofdmunten zoals BTC/EUR of BTCUSDT telt daarbij niet, en er wordt niet doorgeketend) en **los** (bovengrens: elke driehoek apart).

| Soort | Inleg | Kansen per dag (samengevoegd / los) | Winst per dag (samengevoegd / los) | Per maand (GOK, samengevoegd / los) | Alleen de beste beurs, per maand (GOK, samengevoegd) |
|---|---|---|---|---|---|
| Alle beurzen | €100 | 59,0 / 67,2 | €155,14 / €157,70 | €4.654,10 / €4.731,00 | bitstamp: €4.517,28 |
| Alle beurzen | €150 | 59,0 / 67,2 | €231,64 / €234,52 | €6.949,23 / €7.035,52 | bitstamp: €6.759,96 |
| Alle beurzen | €200 | 59,0 / 67,2 | €307,74 / €310,62 | €9.232,29 / €9.318,58 | bitstamp: €9.002,65 |
| Alle beurzen | €2.000 | 59,0 / 67,2 | €352,78 / €355,65 | €10.583,26 / €10.669,55 | bitstamp: €10.205,44 |
| Alle beurzen | €5.000 | 59,0 / 67,2 | €356,84 / €359,72 | €10.705,22 / €10.791,51 | bitstamp: €10.205,44 |
| MiCA (ook via EU-dochter) | €100 | 48,0 / 48,0 | €153,12 / €153,12 | €4.593,53 / €4.593,53 | bitstamp: €4.517,28 |
| MiCA (ook via EU-dochter) | €150 | 48,0 / 48,0 | €229,12 / €229,12 | €6.873,47 / €6.873,47 | bitstamp: €6.759,96 |
| MiCA (ook via EU-dochter) | €200 | 48,0 / 48,0 | €305,07 / €305,07 | €9.152,02 / €9.152,02 | bitstamp: €9.002,65 |
| MiCA (ook via EU-dochter) | €2.000 | 48,0 / 48,0 | €347,08 / €347,08 | €10.412,37 / €10.412,37 | bitstamp: €10.205,44 |
| MiCA (ook via EU-dochter) | €5.000 | 48,0 / 48,0 | €347,08 / €347,08 | €10.412,37 / €10.412,37 | bitstamp: €10.205,44 |
| Grijs | €100 | 11,0 / 19,2 | €2,02 / €4,58 | €60,57 / €137,47 | mexc: €60,57 |
| Grijs | €150 | 11,0 / 19,2 | €2,53 / €5,40 | €75,76 / €162,05 | mexc: €75,76 |
| Grijs | €200 | 11,0 / 19,2 | €2,68 / €5,55 | €80,27 / €166,56 | mexc: €80,27 |
| Grijs | €2.000 | 11,0 / 19,2 | €5,70 / €8,57 | €170,89 / €257,18 | mexc: €170,89 |
| Grijs | €5.000 | 11,0 / 19,2 | €9,76 / €12,64 | €292,85 / €379,14 | mexc: €292,85 |

Waarom dit te rooskleurig is (GOK):

- Het is een **bovengrens**: je pakt elke kans, op elke beurs tegelijk, met het geld al op die beurs. Met weinig geld staat alles op één beurs; de laatste kolom neemt alleen de beste beurs (achteraf gekozen, dus ook te rooskleurig).
- Snelle partijen zitten er in milliseconden bovenop. Wat wij na seconden nog zien, is het restje. Ga je zelf pakken, dan concurreer je met hen en met iedereen die het restje ook ziet; bij elke poging kan een stap net weg zijn (dan zit je met een munt die je niet wilde, en verlies).
- Drie orders na elkaar kosten tijd; tussen stap 1 en 3 kan de prijs bewegen.
- De EU-versie van de beurs kan minder paren hebben dan de wereldwijde API die we meten.

Waarom het te somber kan zijn: lagere kosten (meer handelsvolume, eigen beurs-token, maker in plaats van taker, de 0%-paren van OKX die we niet konden ophalen, Bitstamp gratis onder $1.000 volume per 30 dagen) en sneller meten dan elke paar seconden laten meer zien.

Bron van alle aantallen en bedragen: eigen metingen (GEZIEN), data op de tak `ai-handel-data`, map `driehoek/`. Kosten per stap en hun bron: README.md.
