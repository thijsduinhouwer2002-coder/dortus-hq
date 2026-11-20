# Driehoek-meter: rapport

## Kort antwoord

Op de beurzen met vergunning (MiCA, ook via een EU-dochter): 36 echte kansen die met €100 konden (36 als je elke driehoek los telt; 36,9 per dag). Samen €114,55 tot €114,55 per dag met €100 en €228,13 tot €228,13 per dag met €200 (GOK; het lage getal voegt driehoeken samen die hetzelfde stukje boek willen, het hoge telt ze los; allebei alsof je ze allemaal als eerste pakt, met het geld al op de juiste beurs). Op de grijze beurzen (geen vergunning): 12 echte kansen die met €100 konden (18 als je elke driehoek los telt; 12,3 per dag). Samen €1,68 tot €3,60 per dag met €100 en €2,28 tot €4,43 per dag met €200 (GOK; het lage getal voegt driehoeken samen die hetzelfde stukje boek willen, het hoge telt ze los; allebei alsof je ze allemaal als eerste pakt, met het geld al op de juiste beurs).

Uitleg: **takerkosten** zijn wat de beurs per order rekent als je meteen koopt of verkoopt tegen de prijs die er ligt (0% tot 0,8% per order; een driehoek is drie orders). **Diepte** is hoeveel euro je tegen die winstgevende prijzen echt kunt kopen en verkopen voordat de prijs slechter wordt. Wij meten elke 3 tot 5 seconden; snelle bots pakken zulke kansen meestal binnen milliseconden, dus wat hier staat is wat er na hen overbleef.

Data: 288 driehoeken met winst op het boek gezien (ook kleine en korte), 2 dag(en) (2026-11-19 tot 2026-11-20). Gemeten: ±23,4 uur per beurs (GEZIEN, uit stand.jsonl).

Een **echte driehoek**: winst na drie keer takerkosten op het orderboek, op twee metingen die minstens 3 seconden uit elkaar liggen elk minstens €100 diepte, bij de latere meting minstens €0,05 winst, en niet meer dan 5% winst (verdacht). Alle bedragen zijn die van de latere meting: wat er na 3 seconden nog stond. Driehoeken op dezelfde beurs die binnen 5 seconden van elkaar bevestigd werden en een paar delen dat geen paar van twee hoofdmunten is (EUR, USD, USDT, USDC, BTC, ETH), tellen als **één kans** (de beste telt): ze willen hetzelfde stukje orderboek. Er wordt niet doorgeketend: een driehoek hoort alleen bij een kans als hij met elk lid ervan dat stukje deelt. Omdat samenvoegen ook te streng kan zijn, staan aantallen en geld er ook los geteld bij (bovengrens).

Regels van vóór 2026-11-19 16:07 UTC (vóór de keuring) hebben geen meting na 3 seconden en tellen daarom nooit als echt. Daar zat ook niets in dat 3 seconden met €100 diepte stond.

## Per beurs: hoe gemeten en hoe dicht bij winst

Beste marge = per ronde de beste driehoek tegen de beste prijzen na kosten (mediaan en hoogste over alle rondes). Negatief = zelfs de beste driehoek verloor geld. Kandidaten = driehoeken die met de beste prijzen winst gaven; daarvan haalt hij de orderboeken op (bekeken), tenzij het budget van die ronde op was (overgeslagen) of de koersen sinds de vorige controle niet veranderden (zelfde). Een positieve beste marge is nog geen winst: de bulk-koers kan achterlopen of er ligt maar een paar cent op die prijs; het orderboek beslist (kolom Winst op boek).

| Beurs | Status | Paren | Driehoeken | Uur | Rondes | Fouten (te veel) | Beste marge mediaan | Beste marge hoogst | Kandidaten | Bekeken | Overgeslagen | Zelfde | Winst op boek | Echt |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| bitget | grijs | 3659 | 202 | 23,4 | 27808 | 1 (0) | -0,280% | 0,537% | 1141 | 804 | 0 | 337 | 0 | 0 |
| bitstamp | MiCA | 252 | 346 | 23,4 | 16686 | 0 (0) | -0,230% | 3,905% | 11264 | 11261 | 0 | 0 | 11189 | 32 |
| bitvavo | MiCA | 435 | 22 | 23,4 | 20870 | 1 (0) | -0,756% | -0,318% | 157 | 146 | 0 | 11 | 0 | 0 |
| gate | MiCA-dochter | 2158 | 372 | 23,4 | 20717 | 1 (0) | -0,157% | 2,851% | 5900 | 2390 | 66 | 3442 | 1 | 0 |
| kraken | MiCA | 1353 | 2352 | 23,4 | 16704 | 0 (0) | -0,205% | 3,182% | 5077 | 3339 | 22 | 1716 | 2 | 0 |
| kucoin | MiCA-dochter | 968 | 452 | 23,4 | 27841 | 1 (0) | 1,484% | 4,979% | 38161 | 16226 | 89 | 21844 | 0 | 0 |
| mexc | grijs | 1664 | 886 | 23,4 | 27803 | 0 (0) | 0,192% | 4,975% | 59314 | 29954 | 553 | 28244 | 1396 | 18 |
| okx | MiCA-dochter | 1250 | 2338 | 23,4 | 27838 | 0 (0) | -0,134% | 4,743% | 11493 | 10435 | 75 | 983 | 2009 | 4 |

## Trechter

| Stap | Alle beurzen | MiCA (ook via EU-dochter) | Grijs |
|---|---|---|---|
| winst op het boek, met de lage kosten (bovengrens) | 288 | 98 | 190 |
| winst op het boek, met de gewone kosten | 288 | 98 | 190 |
| en ooit minstens €100 diepte | 91 | 55 | 36 |
| en na 3 s nog steeds minstens €100 diepte | 63 | 45 | 18 |
| en dan minstens €0,05 winst | 63 | 45 | 18 |
| en niet verdacht = **echt** | 54 | 36 | 18 |
| echte **kansen** (samengevoegd als ze hetzelfde stukje boek willen; ondergrens) | 48 | 36 | 12 |

De lage kosten verschillen alleen bij Bitvavo (categorie B, C en D: USDC- en stablecoinparen; Bitvavo noemt ze lager dan 0,25% maar geeft geen getal, dus laag = 0%, GOK). Overal elders is laag gelijk aan gewoon.

## Per dag (echte kansen, bedragen na 3 seconden)

| Dag | Soort | Driehoeken | Kansen | Mediane winst per kans | Mediane diepte | Mediane duur met €100 diepte | Totale winst (volle diepte) |
|---|---|---|---|---|---|---|---|
| 2026-11-19 | Alle beurzen | 48 | 42 | €7,37 | €227 | 17,0 s | €280,75 |
| 2026-11-19 | MiCA (ook via EU-dochter) | 35 | 35 | €7,78 | €227 | 30,0 s | €253,08 |
| 2026-11-19 | Grijs | 13 | 7 | €0,49 | €694 | 7,0 s | €27,67 |
| 2026-11-20 | Alle beurzen | 6 | 6 | €0,26 | €600 | 9,0 s | €2,00 |
| 2026-11-20 | MiCA (ook via EU-dochter) | 1 | 1 | €0,14 | €116 | 40,0 s | €0,14 |
| 2026-11-20 | Grijs | 5 | 5 | €0,38 | €1.000 | 3,0 s | €1,86 |
| totaal | Alle beurzen | 54 | 48 | €6,46 | €227 | 15,0 s | €282,75 |
| totaal | MiCA (ook via EU-dochter) | 36 | 36 | €7,69 | €227 | 33,0 s | €253,21 |
| totaal | Grijs | 18 | 12 | €0,44 | €847 | 6,0 s | €29,53 |

## Beste driehoeken per beurs (echt, bedragen na 3 seconden)

**bitstamp** (MiCA)

| Driehoek | Keren | Mediane winst | Hoogste winst | Mediane diepte | Mediane duur met €100 diepte | Kosten per stap |
|---|---|---|---|---|---|---|
| EUR>USD>SKY>EUR | 31 | €8,22 | €11,32 | €227 | 25,0 s | 0,08% + 0,40% + 0,40% |
| EUR>IMX>USD>EUR | 1 | €0,14 | €0,14 | €116 | 40,0 s | 0,40% + 0,40% + 0,08% |

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
| bitstamp | MiCA | 346 | 260 | €12 | 333 | 334 | 334 | 249 |
| bitvavo | MiCA | 22 | 22 | ≤ €10 | 22 | 22 | 22 | 22 |
| gate | MiCA-dochter | 372 | 0 | ≤ €10 | 372 | 372 | 372 | 0 |
| kraken | MiCA | 2352 | 1368 | ≤ €10 | 2352 | 2352 | 2352 | 1368 |
| kucoin | MiCA-dochter | 452 | 12 | ≤ €10 | 452 | 452 | 452 | 12 |
| mexc | grijs | 886 | 76 | ≤ €10 | 886 | 886 | 886 | 76 |
| okx | MiCA-dochter | 2338 | 1090 | ≤ €10 | 2330 | 2330 | 2330 | 1090 |

Van de 48 echte kansen konden er 48 met €100 (minimale ordergrootte gehaald op alle drie de orders, winst na 3 seconden).

## Opschaling naar €100, €150, €200, €2.000 en €5.000 inleg (GOK)

Per echte kans nemen we de winst die je bij die inleg na 3 seconden nog had kunnen maken (minder inleggen mag als het boek dunner is; alleen bedragen die de minimale ordergrootte halen). Opgeteld per gemeten dag en dan maal 30 voor een maand.

Elk getal staat er twee keer: **samengevoegd** (ondergrens: driehoeken die op hetzelfde moment, binnen 5 seconden na hun bevestiging, hetzelfde niet-hoofdpaar gebruiken, tellen als één kans; een paar van twee hoofdmunten zoals BTC/EUR of BTCUSDT telt daarbij niet, en er wordt niet doorgeketend) en **los** (bovengrens: elke driehoek apart).

| Soort | Inleg | Kansen per dag (samengevoegd / los) | Winst per dag (samengevoegd / los) | Per maand (GOK, samengevoegd / los) | Alleen de beste beurs, per maand (GOK, samengevoegd) |
|---|---|---|---|---|---|
| Alle beurzen | €100 | 49,2 / 55,3 | €116,23 / €118,15 | €3.487,02 / €3.544,49 | bitstamp: €3.379,50 |
| Alle beurzen | €150 | 49,2 / 55,3 | €173,49 / €175,64 | €5.204,83 / €5.269,31 | bitstamp: €5.056,11 |
| Alle beurzen | €200 | 49,2 / 55,3 | €230,41 / €232,56 | €6.912,26 / €6.976,75 | bitstamp: €6.732,14 |
| Alle beurzen | €2.000 | 49,2 / 55,3 | €264,38 / €266,53 | €7.931,34 / €7.995,83 | bitstamp: €7.631,03 |
| Alle beurzen | €5.000 | 49,2 / 55,3 | €267,83 / €269,98 | €8.034,94 / €8.099,42 | bitstamp: €7.631,03 |
| MiCA (ook via EU-dochter) | €100 | 36,9 / 36,9 | €114,55 / €114,55 | €3.436,48 / €3.436,48 | bitstamp: €3.379,50 |
| MiCA (ook via EU-dochter) | €150 | 36,9 / 36,9 | €171,36 / €171,36 | €5.140,94 / €5.140,94 | bitstamp: €5.056,11 |
| MiCA (ook via EU-dochter) | €200 | 36,9 / 36,9 | €228,13 / €228,13 | €6.843,77 / €6.843,77 | bitstamp: €6.732,14 |
| MiCA (ook via EU-dochter) | €2.000 | 36,9 / 36,9 | €259,52 / €259,52 | €7.785,67 / €7.785,67 | bitstamp: €7.631,03 |
| MiCA (ook via EU-dochter) | €5.000 | 36,9 / 36,9 | €259,52 / €259,52 | €7.785,67 / €7.785,67 | bitstamp: €7.631,03 |
| Grijs | €100 | 12,3 / 18,4 | €1,68 / €3,60 | €50,54 / €108,01 | mexc: €50,54 |
| Grijs | €150 | 12,3 / 18,4 | €2,13 / €4,28 | €63,89 / €128,37 | mexc: €63,89 |
| Grijs | €200 | 12,3 / 18,4 | €2,28 / €4,43 | €68,49 / €132,98 | mexc: €68,49 |
| Grijs | €2.000 | 12,3 / 18,4 | €4,86 / €7,01 | €145,67 / €210,16 | mexc: €145,67 |
| Grijs | €5.000 | 12,3 / 18,4 | €8,31 / €10,46 | €249,27 / €313,75 | mexc: €249,27 |

Waarom dit te rooskleurig is (GOK):

- Het is een **bovengrens**: je pakt elke kans, op elke beurs tegelijk, met het geld al op die beurs. Met weinig geld staat alles op één beurs; de laatste kolom neemt alleen de beste beurs (achteraf gekozen, dus ook te rooskleurig).
- Snelle partijen zitten er in milliseconden bovenop. Wat wij na seconden nog zien, is het restje. Ga je zelf pakken, dan concurreer je met hen en met iedereen die het restje ook ziet; bij elke poging kan een stap net weg zijn (dan zit je met een munt die je niet wilde, en verlies).
- Drie orders na elkaar kosten tijd; tussen stap 1 en 3 kan de prijs bewegen.
- De EU-versie van de beurs kan minder paren hebben dan de wereldwijde API die we meten.

Waarom het te somber kan zijn: lagere kosten (meer handelsvolume, eigen beurs-token, maker in plaats van taker, de 0%-paren van OKX die we niet konden ophalen, Bitstamp gratis onder $1.000 volume per 30 dagen) en sneller meten dan elke paar seconden laten meer zien.

Bron van alle aantallen en bedragen: eigen metingen (GEZIEN), data op de tak `ai-handel-data`, map `driehoek/`. Kosten per stap en hun bron: README.md.
