# Driehoek-meter: rapport

## Kort antwoord

Op de beurzen met vergunning (MiCA, ook via een EU-dochter): 69 echte kansen die met €100 konden (69 als je elke driehoek los telt; 59,3 per dag). Samen €104,97 tot €104,97 per dag met €100 en €201,71 tot €201,71 per dag met €200 (GOK; het lage getal voegt driehoeken samen die hetzelfde stukje boek willen, het hoge telt ze los; allebei alsof je ze allemaal als eerste pakt, met het geld al op de juiste beurs). Op de grijze beurzen (geen vergunning): 14 echte kansen die met €100 konden (20 als je elke driehoek los telt; 12,0 per dag). Samen €1,47 tot €3,08 per dag met €100 en €2,03 tot €3,83 per dag met €200 (GOK; het lage getal voegt driehoeken samen die hetzelfde stukje boek willen, het hoge telt ze los; allebei alsof je ze allemaal als eerste pakt, met het geld al op de juiste beurs).

Uitleg: **takerkosten** zijn wat de beurs per order rekent als je meteen koopt of verkoopt tegen de prijs die er ligt (0% tot 0,8% per order; een driehoek is drie orders). **Diepte** is hoeveel euro je tegen die winstgevende prijzen echt kunt kopen en verkopen voordat de prijs slechter wordt. Wij meten elke 3 tot 5 seconden; snelle bots pakken zulke kansen meestal binnen milliseconden, dus wat hier staat is wat er na hen overbleef.

Data: 378 driehoeken met winst op het boek gezien (ook kleine en korte), 2 dag(en) (2026-11-19 tot 2026-11-20). Gemeten: ±27,9 uur per beurs (GEZIEN, uit stand.jsonl).

Een **echte driehoek**: winst na drie keer takerkosten op het orderboek, op twee metingen die minstens 3 seconden uit elkaar liggen elk minstens €100 diepte, bij de latere meting minstens €0,05 winst, en niet meer dan 5% winst (verdacht). Alle bedragen zijn die van de latere meting: wat er na 3 seconden nog stond. Driehoeken op dezelfde beurs die binnen 5 seconden van elkaar bevestigd werden en een paar delen dat geen paar van twee hoofdmunten is (EUR, USD, USDT, USDC, BTC, ETH), tellen als **één kans** (de beste telt): ze willen hetzelfde stukje orderboek. Er wordt niet doorgeketend: een driehoek hoort alleen bij een kans als hij met elk lid ervan dat stukje deelt. Omdat samenvoegen ook te streng kan zijn, staan aantallen en geld er ook los geteld bij (bovengrens).

Regels van vóór 2026-11-19 16:07 UTC (vóór de keuring) hebben geen meting na 3 seconden en tellen daarom nooit als echt. Daar zat ook niets in dat 3 seconden met €100 diepte stond.

## Per beurs: hoe gemeten en hoe dicht bij winst

Beste marge = per ronde de beste driehoek tegen de beste prijzen na kosten (mediaan en hoogste over alle rondes). Negatief = zelfs de beste driehoek verloor geld. Kandidaten = driehoeken die met de beste prijzen winst gaven; daarvan haalt hij de orderboeken op (bekeken), tenzij het budget van die ronde op was (overgeslagen) of de koersen sinds de vorige controle niet veranderden (zelfde). Een positieve beste marge is nog geen winst: de bulk-koers kan achterlopen of er ligt maar een paar cent op die prijs; het orderboek beslist (kolom Winst op boek).

| Beurs | Status | Paren | Driehoeken | Uur | Rondes | Fouten (te veel) | Beste marge mediaan | Beste marge hoogst | Kandidaten | Bekeken | Overgeslagen | Zelfde | Winst op boek | Echt |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| bitget | grijs | 3659 | 202 | 27,9 | 33204 | 1 (0) | -0,278% | 0,575% | 1597 | 1239 | 0 | 358 | 0 | 0 |
| bitstamp | MiCA | 252 | 346 | 27,9 | 19922 | 0 (0) | -0,229% | 3,905% | 16518 | 16366 | 26 | 123 | 15739 | 65 |
| bitvavo | MiCA | 435 | 22 | 27,9 | 24918 | 1 (0) | -0,757% | -0,318% | 157 | 146 | 0 | 11 | 0 | 0 |
| gate | MiCA-dochter | 2158 | 372 | 27,9 | 24648 | 1 (0) | -0,149% | 4,075% | 8816 | 3764 | 170 | 4882 | 1 | 0 |
| kraken | MiCA | 1353 | 2352 | 27,9 | 19943 | 0 (0) | -0,205% | 3,182% | 5336 | 3580 | 22 | 1734 | 2 | 0 |
| kucoin | MiCA-dochter | 968 | 452 | 27,9 | 33239 | 1 (0) | 1,281% | 4,979% | 40202 | 18032 | 108 | 22060 | 0 | 0 |
| mexc | grijs | 1664 | 886 | 27,9 | 33187 | 0 (0) | 0,206% | 4,975% | 72647 | 38941 | 842 | 32297 | 1786 | 20 |
| okx | MiCA-dochter | 1250 | 2338 | 27,9 | 33236 | 0 (0) | -0,134% | 4,743% | 15733 | 14366 | 115 | 1252 | 3458 | 4 |

## Trechter

| Stap | Alle beurzen | MiCA (ook via EU-dochter) | Grijs |
|---|---|---|---|
| winst op het boek, met de lage kosten (bovengrens) | 378 | 147 | 231 |
| winst op het boek, met de gewone kosten | 378 | 147 | 231 |
| en ooit minstens €100 diepte | 138 | 95 | 43 |
| en na 3 s nog steeds minstens €100 diepte | 102 | 80 | 22 |
| en dan minstens €0,05 winst | 98 | 78 | 20 |
| en niet verdacht = **echt** | 89 | 69 | 20 |
| echte **kansen** (samengevoegd als ze hetzelfde stukje boek willen; ondergrens) | 83 | 69 | 14 |

De lage kosten verschillen alleen bij Bitvavo (categorie B, C en D: USDC- en stablecoinparen; Bitvavo noemt ze lager dan 0,25% maar geeft geen getal, dus laag = 0%, GOK). Overal elders is laag gelijk aan gewoon.

## Per dag (echte kansen, bedragen na 3 seconden)

| Dag | Soort | Driehoeken | Kansen | Mediane winst per kans | Mediane diepte | Mediane duur met €100 diepte | Totale winst (volle diepte) |
|---|---|---|---|---|---|---|---|
| 2026-11-19 | Alle beurzen | 48 | 42 | €7,37 | €227 | 17,0 s | €280,75 |
| 2026-11-19 | MiCA (ook via EU-dochter) | 35 | 35 | €7,78 | €227 | 30,0 s | €253,08 |
| 2026-11-19 | Grijs | 13 | 7 | €0,49 | €694 | 7,0 s | €27,67 |
| 2026-11-20 | Alle beurzen | 41 | 41 | €0,27 | €116 | 45,0 s | €14,54 |
| 2026-11-20 | MiCA (ook via EU-dochter) | 34 | 34 | €0,27 | €116 | 60,0 s | €12,18 |
| 2026-11-20 | Grijs | 7 | 7 | €0,38 | €1.000 | 3,0 s | €2,37 |
| totaal | Alle beurzen | 89 | 83 | €0,69 | €227 | 36,0 s | €295,29 |
| totaal | MiCA (ook via EU-dochter) | 69 | 69 | €1,02 | €200 | 50,0 s | €265,26 |
| totaal | Grijs | 20 | 14 | €0,40 | €847 | 6,0 s | €30,04 |

## Beste driehoeken per beurs (echt, bedragen na 3 seconden)

**bitstamp** (MiCA)

| Driehoek | Keren | Mediane winst | Hoogste winst | Mediane diepte | Mediane duur met €100 diepte | Kosten per stap |
|---|---|---|---|---|---|---|
| EUR>IMX>USD>EUR | 33 | €0,27 | €1,23 | €116 | 65,0 s | 0,40% + 0,40% + 0,08% |
| EUR>USD>SKY>EUR | 31 | €8,22 | €11,32 | €227 | 25,0 s | 0,08% + 0,40% + 0,40% |
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
| mexc | USDT>BTC>USDC>USDT | €12,08 | €24.652 | 0 s | nee | nee |

## Kan een kleine inleg meedoen? (€100, €150, €200)

Minimale ordergrootte per paar uit de openbare API van elke beurs (aantal munten en bedrag in de quote; Bitget: waarde in USDT). Per beurs: hoeveel driehoeken je met dat bedrag kunt rondmaken zonder dat een van de drie orders onder het minimum valt (tegen de beste prijzen, GEZIEN). Het kleinste bedrag dat we toetsen is €10; "≤ €10" betekent dus €10 of minder. Het aantal munten wordt per order naar beneden afgerond op de stapgrootte van de beurs (uit de API), en bij Bitvavo rekenen we per euro-order €0,01 extra (Bitvavo rondt de kosten naar boven af op de cent).

| Beurs | Status | Driehoeken | Met EUR | Mediaan minimale inleg | Mogelijk met €100 | €150 | €200 | Met EUR en €100 |
|---|---|---|---|---|---|---|---|---|
| bitget | grijs | 202 | 46 | ≤ €10 | 202 | 202 | 202 | 46 |
| bitstamp | MiCA | 346 | 260 | €12 | 333 | 334 | 334 | 249 |
| bitvavo | MiCA | 22 | 22 | ≤ €10 | 22 | 22 | 22 | 22 |
| gate | MiCA-dochter | 372 | 0 | ≤ €10 | 372 | 372 | 372 | 0 |
| kraken | MiCA | 2352 | 1368 | ≤ €10 | 2351 | 2352 | 2352 | 1368 |
| kucoin | MiCA-dochter | 452 | 12 | ≤ €10 | 452 | 452 | 452 | 12 |
| mexc | grijs | 886 | 76 | ≤ €10 | 886 | 886 | 886 | 76 |
| okx | MiCA-dochter | 2338 | 1090 | ≤ €10 | 2326 | 2326 | 2326 | 1086 |

Van de 83 echte kansen konden er 83 met €100 (minimale ordergrootte gehaald op alle drie de orders, winst na 3 seconden).

## Opschaling naar €100, €150, €200, €2.000 en €5.000 inleg (GOK)

Per echte kans nemen we de winst die je bij die inleg na 3 seconden nog had kunnen maken (minder inleggen mag als het boek dunner is; alleen bedragen die de minimale ordergrootte halen). Opgeteld per gemeten dag en dan maal 30 voor een maand.

Elk getal staat er twee keer: **samengevoegd** (ondergrens: driehoeken die op hetzelfde moment, binnen 5 seconden na hun bevestiging, hetzelfde niet-hoofdpaar gebruiken, tellen als één kans; een paar van twee hoofdmunten zoals BTC/EUR of BTCUSDT telt daarbij niet, en er wordt niet doorgeketend) en **los** (bovengrens: elke driehoek apart).

| Soort | Inleg | Kansen per dag (samengevoegd / los) | Winst per dag (samengevoegd / los) | Per maand (GOK, samengevoegd / los) | Alleen de beste beurs, per maand (GOK, samengevoegd) |
|---|---|---|---|---|---|
| Alle beurzen | €100 | 71,4 / 76,5 | €106,44 / €108,04 | €3.193,13 / €3.241,34 | bitstamp: €3.101,24 |
| Alle beurzen | €150 | 71,4 / 76,5 | €155,96 / €157,77 | €4.678,95 / €4.733,04 | bitstamp: €4.551,65 |
| Alle beurzen | €200 | 71,4 / 76,5 | €203,73 / €205,54 | €6.112,00 / €6.166,09 | bitstamp: €5.957,52 |
| Alle beurzen | €2.000 | 71,4 / 76,5 | €232,55 / €234,35 | €6.976,37 / €7.030,47 | bitstamp: €6.711,51 |
| Alle beurzen | €5.000 | 71,4 / 76,5 | €235,44 / €237,25 | €7.063,27 / €7.117,36 | bitstamp: €6.711,51 |
| MiCA (ook via EU-dochter) | €100 | 59,3 / 59,3 | €104,97 / €104,97 | €3.149,04 / €3.149,04 | bitstamp: €3.101,24 |
| MiCA (ook via EU-dochter) | €150 | 59,3 / 59,3 | €154,09 / €154,09 | €4.622,81 / €4.622,81 | bitstamp: €4.551,65 |
| MiCA (ook via EU-dochter) | €200 | 59,3 / 59,3 | €201,71 / €201,71 | €6.051,15 / €6.051,15 | bitstamp: €5.957,52 |
| MiCA (ook via EU-dochter) | €2.000 | 59,3 / 59,3 | €228,04 / €228,04 | €6.841,23 / €6.841,23 | bitstamp: €6.711,51 |
| MiCA (ook via EU-dochter) | €5.000 | 59,3 / 59,3 | €228,04 / €228,04 | €6.841,23 / €6.841,23 | bitstamp: €6.711,51 |
| Grijs | €100 | 12,0 / 17,2 | €1,47 / €3,08 | €44,09 / €92,30 | mexc: €44,09 |
| Grijs | €150 | 12,0 / 17,2 | €1,87 / €3,67 | €56,14 / €110,23 | mexc: €56,14 |
| Grijs | €200 | 12,0 / 17,2 | €2,03 / €3,83 | €60,85 / €114,94 | mexc: €60,85 |
| Grijs | €2.000 | 12,0 / 17,2 | €4,50 / €6,31 | €135,15 / €189,24 | mexc: €135,15 |
| Grijs | €5.000 | 12,0 / 17,2 | €7,40 / €9,20 | €222,04 / €276,13 | mexc: €222,04 |

Waarom dit te rooskleurig is (GOK):

- Het is een **bovengrens**: je pakt elke kans, op elke beurs tegelijk, met het geld al op die beurs. Met weinig geld staat alles op één beurs; de laatste kolom neemt alleen de beste beurs (achteraf gekozen, dus ook te rooskleurig).
- Snelle partijen zitten er in milliseconden bovenop. Wat wij na seconden nog zien, is het restje. Ga je zelf pakken, dan concurreer je met hen en met iedereen die het restje ook ziet; bij elke poging kan een stap net weg zijn (dan zit je met een munt die je niet wilde, en verlies).
- Drie orders na elkaar kosten tijd; tussen stap 1 en 3 kan de prijs bewegen.
- De EU-versie van de beurs kan minder paren hebben dan de wereldwijde API die we meten.

Waarom het te somber kan zijn: lagere kosten (meer handelsvolume, eigen beurs-token, maker in plaats van taker, de 0%-paren van OKX die we niet konden ophalen, Bitstamp gratis onder $1.000 volume per 30 dagen) en sneller meten dan elke paar seconden laten meer zien.

Bron van alle aantallen en bedragen: eigen metingen (GEZIEN), data op de tak `ai-handel-data`, map `driehoek/`. Kosten per stap en hun bron: README.md.
