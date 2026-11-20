# Driehoek-meter: rapport

## Kort antwoord

Op de beurzen met vergunning (MiCA, ook via een EU-dochter): 53 echte kansen die met €100 konden (53 als je elke driehoek los telt; 49,1 per dag). Samen €107,36 tot €107,36 per dag met €100 en €210,62 tot €210,62 per dag met €200 (GOK; het lage getal voegt driehoeken samen die hetzelfde stukje boek willen, het hoge telt ze los; allebei alsof je ze allemaal als eerste pakt, met het geld al op de juiste beurs). Op de grijze beurzen (geen vergunning): 14 echte kansen die met €100 konden (20 als je elke driehoek los telt; 13,0 per dag). Samen €1,58 tot €3,31 per dag met €100 en €2,18 tot €4,13 per dag met €200 (GOK; het lage getal voegt driehoeken samen die hetzelfde stukje boek willen, het hoge telt ze los; allebei alsof je ze allemaal als eerste pakt, met het geld al op de juiste beurs).

Uitleg: **takerkosten** zijn wat de beurs per order rekent als je meteen koopt of verkoopt tegen de prijs die er ligt (0% tot 0,8% per order; een driehoek is drie orders). **Diepte** is hoeveel euro je tegen die winstgevende prijzen echt kunt kopen en verkopen voordat de prijs slechter wordt. Wij meten elke 3 tot 5 seconden; snelle bots pakken zulke kansen meestal binnen milliseconden, dus wat hier staat is wat er na hen overbleef.

Data: 327 driehoeken met winst op het boek gezien (ook kleine en korte), 2 dag(en) (2026-11-19 tot 2026-11-20). Gemeten: ±25,9 uur per beurs (GEZIEN, uit stand.jsonl).

Een **echte driehoek**: winst na drie keer takerkosten op het orderboek, op twee metingen die minstens 3 seconden uit elkaar liggen elk minstens €100 diepte, bij de latere meting minstens €0,05 winst, en niet meer dan 5% winst (verdacht). Alle bedragen zijn die van de latere meting: wat er na 3 seconden nog stond. Driehoeken op dezelfde beurs die binnen 5 seconden van elkaar bevestigd werden en een paar delen dat geen paar van twee hoofdmunten is (EUR, USD, USDT, USDC, BTC, ETH), tellen als **één kans** (de beste telt): ze willen hetzelfde stukje orderboek. Er wordt niet doorgeketend: een driehoek hoort alleen bij een kans als hij met elk lid ervan dat stukje deelt. Omdat samenvoegen ook te streng kan zijn, staan aantallen en geld er ook los geteld bij (bovengrens).

Regels van vóór 2026-11-19 16:07 UTC (vóór de keuring) hebben geen meting na 3 seconden en tellen daarom nooit als echt. Daar zat ook niets in dat 3 seconden met €100 diepte stond.

## Per beurs: hoe gemeten en hoe dicht bij winst

Beste marge = per ronde de beste driehoek tegen de beste prijzen na kosten (mediaan en hoogste over alle rondes). Negatief = zelfs de beste driehoek verloor geld. Kandidaten = driehoeken die met de beste prijzen winst gaven; daarvan haalt hij de orderboeken op (bekeken), tenzij het budget van die ronde op was (overgeslagen) of de koersen sinds de vorige controle niet veranderden (zelfde). Een positieve beste marge is nog geen winst: de bulk-koers kan achterlopen of er ligt maar een paar cent op die prijs; het orderboek beslist (kolom Winst op boek).

| Beurs | Status | Paren | Driehoeken | Uur | Rondes | Fouten (te veel) | Beste marge mediaan | Beste marge hoogst | Kandidaten | Bekeken | Overgeslagen | Zelfde | Winst op boek | Echt |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| bitget | grijs | 3659 | 202 | 25,9 | 30806 | 1 (0) | -0,279% | 0,575% | 1296 | 957 | 0 | 339 | 0 | 0 |
| bitstamp | MiCA | 252 | 346 | 25,9 | 18485 | 0 (0) | -0,229% | 3,905% | 14681 | 14530 | 25 | 123 | 13912 | 49 |
| bitvavo | MiCA | 435 | 22 | 25,9 | 23119 | 1 (0) | -0,757% | -0,318% | 157 | 146 | 0 | 11 | 0 | 0 |
| gate | MiCA-dochter | 2158 | 372 | 25,9 | 22862 | 1 (0) | -0,151% | 4,075% | 8270 | 3512 | 167 | 4591 | 1 | 0 |
| kraken | MiCA | 1353 | 2352 | 25,9 | 18504 | 0 (0) | -0,205% | 3,182% | 5251 | 3502 | 22 | 1727 | 2 | 0 |
| kucoin | MiCA-dochter | 968 | 452 | 25,9 | 30840 | 1 (0) | 1,371% | 4,979% | 39316 | 17187 | 89 | 22038 | 0 | 0 |
| mexc | grijs | 1664 | 886 | 25,9 | 30800 | 0 (0) | 0,203% | 4,975% | 65145 | 34008 | 575 | 29998 | 1481 | 20 |
| okx | MiCA-dochter | 1250 | 2338 | 25,9 | 30836 | 0 (0) | -0,135% | 4,743% | 13491 | 12371 | 112 | 1007 | 3456 | 4 |

## Trechter

| Stap | Alle beurzen | MiCA (ook via EU-dochter) | Grijs |
|---|---|---|---|
| winst op het boek, met de lage kosten (bovengrens) | 327 | 122 | 205 |
| winst op het boek, met de gewone kosten | 327 | 122 | 205 |
| en ooit minstens €100 diepte | 114 | 74 | 40 |
| en na 3 s nog steeds minstens €100 diepte | 83 | 62 | 21 |
| en dan minstens €0,05 winst | 82 | 62 | 20 |
| en niet verdacht = **echt** | 73 | 53 | 20 |
| echte **kansen** (samengevoegd als ze hetzelfde stukje boek willen; ondergrens) | 67 | 53 | 14 |

De lage kosten verschillen alleen bij Bitvavo (categorie B, C en D: USDC- en stablecoinparen; Bitvavo noemt ze lager dan 0,25% maar geeft geen getal, dus laag = 0%, GOK). Overal elders is laag gelijk aan gewoon.

## Per dag (echte kansen, bedragen na 3 seconden)

| Dag | Soort | Driehoeken | Kansen | Mediane winst per kans | Mediane diepte | Mediane duur met €100 diepte | Totale winst (volle diepte) |
|---|---|---|---|---|---|---|---|
| 2026-11-19 | Alle beurzen | 48 | 42 | €7,37 | €227 | 17,0 s | €280,75 |
| 2026-11-19 | MiCA (ook via EU-dochter) | 35 | 35 | €7,78 | €227 | 30,0 s | €253,08 |
| 2026-11-19 | Grijs | 13 | 7 | €0,49 | €694 | 7,0 s | €27,67 |
| 2026-11-20 | Alle beurzen | 25 | 25 | €0,24 | €116 | 45,0 s | €7,36 |
| 2026-11-20 | MiCA (ook via EU-dochter) | 18 | 18 | €0,19 | €116 | 75,0 s | €5,00 |
| 2026-11-20 | Grijs | 7 | 7 | €0,38 | €1.000 | 3,0 s | €2,37 |
| totaal | Alle beurzen | 73 | 67 | €1,98 | €227 | 25,0 s | €288,11 |
| totaal | MiCA (ook via EU-dochter) | 53 | 53 | €5,66 | €227 | 45,0 s | €258,08 |
| totaal | Grijs | 20 | 14 | €0,40 | €847 | 6,0 s | €30,04 |

## Beste driehoeken per beurs (echt, bedragen na 3 seconden)

**bitstamp** (MiCA)

| Driehoek | Keren | Mediane winst | Hoogste winst | Mediane diepte | Mediane duur met €100 diepte | Kosten per stap |
|---|---|---|---|---|---|---|
| EUR>USD>SKY>EUR | 31 | €8,22 | €11,32 | €227 | 25,0 s | 0,08% + 0,40% + 0,40% |
| EUR>IMX>USD>EUR | 17 | €0,24 | €0,94 | €116 | 95,0 s | 0,40% + 0,40% + 0,08% |
| EUR>MOODENG>USD>EUR | 1 | €0,13 | €0,13 | €150 | 45,0 s | 0,40% + 0,40% + 0,08% |

**mexc** (grijs)

| Driehoek | Keren | Mediane winst | Hoogste winst | Mediane diepte | Mediane duur met €100 diepte | Kosten per stap |
|---|---|---|---|---|---|---|
| USDT>BTC>USDC>USDT | 4 | €3,12 | €20,12 | €14.861 | 5,0 s | 0,05% + 0,00% + 0,00% |
| USDT>ETH>BRL>USDT | 3 | €0,30 | €0,45 | €116 | 6,0 s | 0,05% + 0,05% + 0,08% |
| USDT>XRP>BRL>USDT | 2 | €0,56 | €0,63 | €148 | 10,0 s | 0,00% + 0,05% + 0,08% |
| USDT>BTC>BRL>USDT | 2 | €0,40 | €0,64 | €146 | 10,0 s | 0,05% + 0,05% + 0,08% |
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
| okx | MiCA-dochter | 2338 | 1090 | ≤ €10 | 2322 | 2322 | 2322 | 1082 |

Van de 67 echte kansen konden er 67 met €100 (minimale ordergrootte gehaald op alle drie de orders, winst na 3 seconden).

## Opschaling naar €100, €150, €200, €2.000 en €5.000 inleg (GOK)

Per echte kans nemen we de winst die je bij die inleg na 3 seconden nog had kunnen maken (minder inleggen mag als het boek dunner is; alleen bedragen die de minimale ordergrootte halen). Opgeteld per gemeten dag en dan maal 30 voor een maand.

Elk getal staat er twee keer: **samengevoegd** (ondergrens: driehoeken die op hetzelfde moment, binnen 5 seconden na hun bevestiging, hetzelfde niet-hoofdpaar gebruiken, tellen als één kans; een paar van twee hoofdmunten zoals BTC/EUR of BTCUSDT telt daarbij niet, en er wordt niet doorgeketend) en **los** (bovengrens: elke driehoek apart).

| Soort | Inleg | Kansen per dag (samengevoegd / los) | Winst per dag (samengevoegd / los) | Per maand (GOK, samengevoegd / los) | Alleen de beste beurs, per maand (GOK, samengevoegd) |
|---|---|---|---|---|---|
| Alle beurzen | €100 | 62,0 / 67,6 | €108,94 / €110,67 | €3.268,20 / €3.320,13 | bitstamp: €3.169,22 |
| Alle beurzen | €150 | 62,0 / 67,6 | €161,35 / €163,29 | €4.840,55 / €4.898,82 | bitstamp: €4.703,44 |
| Alle beurzen | €200 | 62,0 / 67,6 | €212,81 / €214,75 | €6.384,20 / €6.442,46 | bitstamp: €6.217,79 |
| Alle beurzen | €2.000 | 62,0 / 67,6 | €243,84 / €245,78 | €7.315,27 / €7.373,54 | bitstamp: €7.029,97 |
| Alle beurzen | €5.000 | 62,0 / 67,6 | €246,96 / €248,90 | €7.408,88 / €7.467,14 | bitstamp: €7.029,97 |
| MiCA (ook via EU-dochter) | €100 | 49,1 / 49,1 | €107,36 / €107,36 | €3.220,71 / €3.220,71 | bitstamp: €3.169,22 |
| MiCA (ook via EU-dochter) | €150 | 49,1 / 49,1 | €159,34 / €159,34 | €4.780,08 / €4.780,08 | bitstamp: €4.703,44 |
| MiCA (ook via EU-dochter) | €200 | 49,1 / 49,1 | €210,62 / €210,62 | €6.318,65 / €6.318,65 | bitstamp: €6.217,79 |
| MiCA (ook via EU-dochter) | €2.000 | 49,1 / 49,1 | €238,99 / €238,99 | €7.169,70 / €7.169,70 | bitstamp: €7.029,97 |
| MiCA (ook via EU-dochter) | €5.000 | 49,1 / 49,1 | €238,99 / €238,99 | €7.169,70 / €7.169,70 | bitstamp: €7.029,97 |
| Grijs | €100 | 13,0 / 18,5 | €1,58 / €3,31 | €47,50 / €99,42 | mexc: €47,50 |
| Grijs | €150 | 13,0 / 18,5 | €2,02 / €3,96 | €60,47 / €118,73 | mexc: €60,47 |
| Grijs | €200 | 13,0 / 18,5 | €2,18 / €4,13 | €65,54 / €123,81 | mexc: €65,54 |
| Grijs | €2.000 | 13,0 / 18,5 | €4,85 / €6,79 | €145,58 / €203,84 | mexc: €145,58 |
| Grijs | €5.000 | 13,0 / 18,5 | €7,97 / €9,91 | €239,18 / €297,44 | mexc: €239,18 |

Waarom dit te rooskleurig is (GOK):

- Het is een **bovengrens**: je pakt elke kans, op elke beurs tegelijk, met het geld al op die beurs. Met weinig geld staat alles op één beurs; de laatste kolom neemt alleen de beste beurs (achteraf gekozen, dus ook te rooskleurig).
- Snelle partijen zitten er in milliseconden bovenop. Wat wij na seconden nog zien, is het restje. Ga je zelf pakken, dan concurreer je met hen en met iedereen die het restje ook ziet; bij elke poging kan een stap net weg zijn (dan zit je met een munt die je niet wilde, en verlies).
- Drie orders na elkaar kosten tijd; tussen stap 1 en 3 kan de prijs bewegen.
- De EU-versie van de beurs kan minder paren hebben dan de wereldwijde API die we meten.

Waarom het te somber kan zijn: lagere kosten (meer handelsvolume, eigen beurs-token, maker in plaats van taker, de 0%-paren van OKX die we niet konden ophalen, Bitstamp gratis onder $1.000 volume per 30 dagen) en sneller meten dan elke paar seconden laten meer zien.

Bron van alle aantallen en bedragen: eigen metingen (GEZIEN), data op de tak `ai-handel-data`, map `driehoek/`. Kosten per stap en hun bron: README.md.
