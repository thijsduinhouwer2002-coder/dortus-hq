# Driehoek-meter: rapport

## Kort antwoord

Op de beurzen met vergunning (MiCA, ook via een EU-dochter): 106 echte kansen die met €100 konden (107 als je elke driehoek los telt; 64,1 per dag). Samen €96,41 tot €96,83 per dag met €100 en €171,21 tot €172,07 per dag met €200 (GOK; het lage getal voegt driehoeken samen die hetzelfde stukje boek willen, het hoge telt ze los; allebei alsof je ze allemaal als eerste pakt, met het geld al op de juiste beurs). Op de grijze beurzen (geen vergunning): 29 echte kansen die met €100 konden (37 als je elke driehoek los telt; 17,5 per dag). Samen €2,98 tot €4,39 per dag met €100 en €4,02 tot €5,64 per dag met €200 (GOK; het lage getal voegt driehoeken samen die hetzelfde stukje boek willen, het hoge telt ze los; allebei alsof je ze allemaal als eerste pakt, met het geld al op de juiste beurs).

Uitleg: **takerkosten** zijn wat de beurs per order rekent als je meteen koopt of verkoopt tegen de prijs die er ligt (0% tot 0,8% per order; een driehoek is drie orders). **Diepte** is hoeveel euro je tegen die winstgevende prijzen echt kunt kopen en verkopen voordat de prijs slechter wordt. Wij meten elke 3 tot 5 seconden; snelle bots pakken zulke kansen meestal binnen milliseconden, dus wat hier staat is wat er na hen overbleef.

Data: 737 driehoeken met winst op het boek gezien (ook kleine en korte), 3 dag(en) (2026-11-19 tot 2026-11-21). Gemeten: ±39,7 uur per beurs (GEZIEN, uit stand.jsonl).

Een **echte driehoek**: winst na drie keer takerkosten op het orderboek, op twee metingen die minstens 3 seconden uit elkaar liggen elk minstens €100 diepte, bij de latere meting minstens €0,05 winst, en niet meer dan 5% winst (verdacht). Alle bedragen zijn die van de latere meting: wat er na 3 seconden nog stond. Driehoeken op dezelfde beurs die binnen 5 seconden van elkaar bevestigd werden en een paar delen dat geen paar van twee hoofdmunten is (EUR, USD, USDT, USDC, BTC, ETH), tellen als **één kans** (de beste telt): ze willen hetzelfde stukje orderboek. Er wordt niet doorgeketend: een driehoek hoort alleen bij een kans als hij met elk lid ervan dat stukje deelt. Omdat samenvoegen ook te streng kan zijn, staan aantallen en geld er ook los geteld bij (bovengrens).

Regels van vóór 2026-11-19 16:07 UTC (vóór de keuring) hebben geen meting na 3 seconden en tellen daarom nooit als echt. Daar zat ook niets in dat 3 seconden met €100 diepte stond.

## Per beurs: hoe gemeten en hoe dicht bij winst

Beste marge = per ronde de beste driehoek tegen de beste prijzen na kosten (mediaan en hoogste over alle rondes). Negatief = zelfs de beste driehoek verloor geld. Kandidaten = driehoeken die met de beste prijzen winst gaven; daarvan haalt hij de orderboeken op (bekeken), tenzij het budget van die ronde op was (overgeslagen) of de koersen sinds de vorige controle niet veranderden (zelfde). Een positieve beste marge is nog geen winst: de bulk-koers kan achterlopen of er ligt maar een paar cent op die prijs; het orderboek beslist (kolom Winst op boek).

| Beurs | Status | Paren | Driehoeken | Uur | Rondes | Fouten (te veel) | Beste marge mediaan | Beste marge hoogst | Kandidaten | Bekeken | Overgeslagen | Zelfde | Winst op boek | Echt |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| bitget | grijs | 3658 | 202 | 39,7 | 47291 | 1 (0) | -0,273% | 1,502% | 5339 | 4520 | 121 | 698 | 1 | 0 |
| bitstamp | MiCA | 252 | 346 | 39,7 | 28378 | 0 (0) | -0,225% | 4,996% | 28051 | 27675 | 248 | 123 | 27013 | 84 |
| bitvavo | MiCA | 435 | 22 | 39,7 | 35483 | 1 (0) | -0,757% | -0,318% | 157 | 146 | 0 | 11 | 0 | 0 |
| gate | MiCA-dochter | 2158 | 372 | 39,7 | 35094 | 1 (0) | -0,130% | 4,075% | 24181 | 10356 | 782 | 13042 | 3 | 0 |
| kraken | MiCA | 1353 | 2352 | 39,7 | 28396 | 0 (0) | -0,202% | 4,907% | 9455 | 5732 | 1212 | 2511 | 3 | 0 |
| kucoin | MiCA-dochter | 968 | 452 | 39,7 | 47333 | 1 (0) | 0,379% | 4,979% | 44168 | 21244 | 249 | 22672 | 5 | 0 |
| mexc | grijs | 1664 | 886 | 39,7 | 47271 | 0 (0) | 0,248% | 4,975% | 118664 | 65567 | 1444 | 51070 | 3119 | 37 |
| okx | MiCA-dochter | 1250 | 2338 | 39,7 | 47328 | 0 (0) | -0,111% | 4,743% | 40848 | 35840 | 907 | 4101 | 4096 | 23 |

## Trechter

| Stap | Alle beurzen | MiCA (ook via EU-dochter) | Grijs |
|---|---|---|---|
| winst op het boek, met de lage kosten (bovengrens) | 737 | 338 | 399 |
| winst op het boek, met de gewone kosten | 737 | 338 | 399 |
| en ooit minstens €100 diepte | 244 | 161 | 83 |
| en na 3 s nog steeds minstens €100 diepte | 167 | 127 | 40 |
| en dan minstens €0,05 winst | 158 | 121 | 37 |
| en niet verdacht = **echt** | 144 | 107 | 37 |
| echte **kansen** (samengevoegd als ze hetzelfde stukje boek willen; ondergrens) | 135 | 106 | 29 |

De lage kosten verschillen alleen bij Bitvavo (categorie B, C en D: USDC- en stablecoinparen; Bitvavo noemt ze lager dan 0,25% maar geeft geen getal, dus laag = 0%, GOK). Overal elders is laag gelijk aan gewoon.

## Per dag (echte kansen, bedragen na 3 seconden)

| Dag | Soort | Driehoeken | Kansen | Mediane winst per kans | Mediane diepte | Mediane duur met €100 diepte | Totale winst (volle diepte) |
|---|---|---|---|---|---|---|---|
| 2026-11-19 | Alle beurzen | 48 | 42 | €7,37 | €227 | 17,0 s | €280,75 |
| 2026-11-19 | MiCA (ook via EU-dochter) | 35 | 35 | €7,78 | €227 | 30,0 s | €253,08 |
| 2026-11-19 | Grijs | 13 | 7 | €0,49 | €694 | 7,0 s | €27,67 |
| 2026-11-20 | Alle beurzen | 48 | 48 | €0,27 | €116 | 45,0 s | €17,15 |
| 2026-11-20 | MiCA (ook via EU-dochter) | 38 | 38 | €0,27 | €116 | 70,0 s | €14,25 |
| 2026-11-20 | Grijs | 10 | 10 | €0,21 | €214 | 3,0 s | €2,91 |
| 2026-11-21 | Alle beurzen | 48 | 45 | €1,34 | €284 | 15,0 s | €203,43 |
| 2026-11-21 | MiCA (ook via EU-dochter) | 34 | 33 | €2,68 | €355 | 24,0 s | €177,76 |
| 2026-11-21 | Grijs | 14 | 12 | €0,40 | €166 | 6,0 s | €25,66 |
| totaal | Alle beurzen | 144 | 135 | €0,69 | €227 | 24,0 s | €501,33 |
| totaal | MiCA (ook via EU-dochter) | 107 | 106 | €1,55 | €227 | 45,0 s | €445,09 |
| totaal | Grijs | 37 | 29 | €0,38 | €200 | 6,0 s | €56,24 |

## Beste driehoeken per beurs (echt, bedragen na 3 seconden)

**bitstamp** (MiCA)

| Driehoek | Keren | Mediane winst | Hoogste winst | Mediane diepte | Mediane duur met €100 diepte | Kosten per stap |
|---|---|---|---|---|---|---|
| EUR>IMX>USD>EUR | 48 | €0,39 | €5,07 | €116 | 65,0 s | 0,40% + 0,40% + 0,08% |
| EUR>USD>SKY>EUR | 31 | €8,22 | €11,32 | €227 | 25,0 s | 0,08% + 0,40% + 0,40% |
| EUR>SAND>USD>EUR | 2 | €1,80 | €3,00 | €227 | 748,0 s | 0,40% + 0,40% + 0,08% |
| EUR>USD>HBAR>EUR | 2 | €0,18 | €0,21 | €355 | 490,0 s | 0,08% + 0,40% + 0,40% |
| EUR>MOODENG>USD>EUR | 1 | €0,13 | €0,13 | €150 | 45,0 s | 0,40% + 0,40% + 0,08% |

**mexc** (grijs)

| Driehoek | Keren | Mediane winst | Hoogste winst | Mediane diepte | Mediane duur met €100 diepte | Kosten per stap |
|---|---|---|---|---|---|---|
| USDT>BTC>USDC>USDT | 4 | €3,12 | €20,12 | €14.861 | 5,0 s | 0,05% + 0,00% + 0,00% |
| USDT>BTC>BRL>USDT | 4 | €0,58 | €0,64 | €146 | 6,0 s | 0,05% + 0,05% + 0,08% |
| USDT>SOL>BTC>USDT | 4 | €0,14 | €0,42 | €146 | 19,0 s | 0,05% + 0,05% + 0,05% |
| USDT>ETH>BRL>USDT | 3 | €0,30 | €0,45 | €116 | 6,0 s | 0,05% + 0,05% + 0,08% |
| USDT>SOL>BRL>USDT | 3 | €0,16 | €0,31 | €116 | 9,0 s | 0,05% + 0,05% + 0,08% |

**okx** (MiCA-dochter)

| Driehoek | Keren | Mediane winst | Hoogste winst | Mediane diepte | Mediane duur met €100 diepte | Kosten per stap |
|---|---|---|---|---|---|---|
| USDT>SOL>AUD>USDT | 5 | €2,63 | €4,03 | €2.000 | 15,0 s | 0,10% + 0,10% + 0,10% |
| USDT>BTC>AUD>USDT | 4 | €7,67 | €20,31 | €4.154 | 100,0 s | 0,10% + 0,10% + 0,10% |
| USDT>XANT>USDC>USDT | 3 | €0,80 | €1,98 | €355 | 216,0 s | 0,10% + 0,10% + 0,10% |
| USDT>XRP>AUD>USDT | 3 | €0,29 | €1,68 | €555 | 18,0 s | 0,10% + 0,10% + 0,10% |
| USDT>BTC>AED>USDT | 1 | €72,14 | €72,14 | €15.777 | 9,0 s | 0,10% + 0,10% + 0,10% |

Grootste driehoeken die **niet** echt waren (te kort, te dun, te weinig winst of verdacht). Bedragen van het beste moment:

| Beurs | Driehoek | Winst | Diepte | Duur | Na 3 s nog €100 diepte | Verdacht |
|---|---|---|---|---|---|---|
| gate | USDT>XRP>RLUSD>USDT | €26,32 | €19.722 | 0 s | nee | nee |
| bitstamp | EUR>USD>SKY>EUR | €14,24 | €227 | 5 s | ja | ja |
| bitstamp | EUR>USD>SKY>EUR | €13,92 | €227 | 30 s | ja | ja |
| bitstamp | EUR>USD>SKY>EUR | €13,13 | €200 | 0 s | nee | ja |
| bitstamp | EUR>USD>SKY>EUR | €12,95 | €227 | 80 s | ja | ja |
| bitstamp | EUR>USD>SKY>EUR | €12,67 | €227 | 0 s | nee | ja |
| bitstamp | EUR>USD>SKY>EUR | €12,45 | €227 | 170 s | ja | ja |
| bitstamp | EUR>USD>SKY>EUR | €12,24 | €227 | 15 s | ja | ja |

## Kan een kleine inleg meedoen? (€100, €150, €200)

Minimale ordergrootte per paar uit de openbare API van elke beurs (aantal munten en bedrag in de quote; Bitget: waarde in USDT). Per beurs: hoeveel driehoeken je met dat bedrag kunt rondmaken zonder dat een van de drie orders onder het minimum valt (tegen de beste prijzen, GEZIEN). Het kleinste bedrag dat we toetsen is €10; "≤ €10" betekent dus €10 of minder. Het aantal munten wordt per order naar beneden afgerond op de stapgrootte van de beurs (uit de API), en bij Bitvavo rekenen we per euro-order €0,01 extra (Bitvavo rondt de kosten naar boven af op de cent).

| Beurs | Status | Driehoeken | Met EUR | Mediaan minimale inleg | Mogelijk met €100 | €150 | €200 | Met EUR en €100 |
|---|---|---|---|---|---|---|---|---|
| bitget | grijs | 202 | 46 | ≤ €10 | 202 | 202 | 202 | 46 |
| bitstamp | MiCA | 346 | 260 | €12 | 327 | 327 | 327 | 249 |
| bitvavo | MiCA | 22 | 22 | ≤ €10 | 22 | 22 | 22 | 22 |
| gate | MiCA-dochter | 372 | 0 | ≤ €10 | 372 | 372 | 372 | 0 |
| kraken | MiCA | 2352 | 1368 | ≤ €10 | 2352 | 2352 | 2352 | 1368 |
| kucoin | MiCA-dochter | 452 | 12 | ≤ €10 | 452 | 452 | 452 | 12 |
| mexc | grijs | 886 | 76 | ≤ €10 | 886 | 886 | 886 | 76 |
| okx | MiCA-dochter | 2338 | 1090 | ≤ €10 | 2330 | 2330 | 2330 | 1090 |

Van de 135 echte kansen konden er 135 met €100 (minimale ordergrootte gehaald op alle drie de orders, winst na 3 seconden).

## Opschaling naar €100, €150, €200, €2.000 en €5.000 inleg (GOK)

Per echte kans nemen we de winst die je bij die inleg na 3 seconden nog had kunnen maken (minder inleggen mag als het boek dunner is; alleen bedragen die de minimale ordergrootte halen). Opgeteld per gemeten dag en dan maal 30 voor een maand.

Elk getal staat er twee keer: **samengevoegd** (ondergrens: driehoeken die op hetzelfde moment, binnen 5 seconden na hun bevestiging, hetzelfde niet-hoofdpaar gebruiken, tellen als één kans; een paar van twee hoofdmunten zoals BTC/EUR of BTCUSDT telt daarbij niet, en er wordt niet doorgeketend) en **los** (bovengrens: elke driehoek apart).

| Soort | Inleg | Kansen per dag (samengevoegd / los) | Winst per dag (samengevoegd / los) | Per maand (GOK, samengevoegd / los) | Alleen de beste beurs, per maand (GOK, samengevoegd) |
|---|---|---|---|---|---|
| Alle beurzen | €100 | 81,7 / 87,1 | €99,38 / €101,22 | €2.981,45 / €3.036,54 | bitstamp: €2.779,24 |
| Alle beurzen | €150 | 81,7 / 87,1 | €139,63 / €141,88 | €4.188,85 / €4.256,41 | bitstamp: €3.908,32 |
| Alle beurzen | €200 | 81,7 / 87,1 | €175,23 / €177,71 | €5.256,84 / €5.331,32 | bitstamp: €4.912,65 |
| Alle beurzen | €2.000 | 81,7 / 87,1 | €232,20 / €241,07 | €6.965,99 / €7.232,24 | bitstamp: €5.453,77 |
| Alle beurzen | €5.000 | 81,7 / 87,1 | €260,87 / €277,59 | €7.826,10 / €8.327,56 | bitstamp: €5.453,77 |
| MiCA (ook via EU-dochter) | €100 | 64,1 / 64,7 | €96,41 / €96,83 | €2.892,18 / €2.904,98 | bitstamp: €2.779,24 |
| MiCA (ook via EU-dochter) | €150 | 64,1 / 64,7 | €135,90 / €136,54 | €4.077,09 / €4.096,30 | bitstamp: €3.908,32 |
| MiCA (ook via EU-dochter) | €200 | 64,1 / 64,7 | €171,21 / €172,07 | €5.136,37 / €5.161,98 | bitstamp: €4.912,65 |
| MiCA (ook via EU-dochter) | €2.000 | 64,1 / 64,7 | €221,95 / €228,64 | €6.658,58 / €6.859,08 | bitstamp: €5.453,77 |
| MiCA (ook via EU-dochter) | €5.000 | 64,1 / 64,7 | €242,65 / €256,71 | €7.279,60 / €7.701,24 | bitstamp: €5.453,77 |
| Grijs | €100 | 17,5 / 22,4 | €2,98 / €4,39 | €89,27 / €131,56 | mexc: €89,27 |
| Grijs | €150 | 17,5 / 22,4 | €3,73 / €5,34 | €111,76 / €160,11 | mexc: €111,76 |
| Grijs | €200 | 17,5 / 22,4 | €4,02 / €5,64 | €120,47 / €169,34 | mexc: €120,47 |
| Grijs | €2.000 | 17,5 / 22,4 | €10,25 / €12,44 | €307,41 / €373,16 | mexc: €307,41 |
| Grijs | €5.000 | 17,5 / 22,4 | €18,22 / €20,88 | €546,50 / €626,32 | mexc: €546,50 |

Waarom dit te rooskleurig is (GOK):

- Het is een **bovengrens**: je pakt elke kans, op elke beurs tegelijk, met het geld al op die beurs. Met weinig geld staat alles op één beurs; de laatste kolom neemt alleen de beste beurs (achteraf gekozen, dus ook te rooskleurig).
- Snelle partijen zitten er in milliseconden bovenop. Wat wij na seconden nog zien, is het restje. Ga je zelf pakken, dan concurreer je met hen en met iedereen die het restje ook ziet; bij elke poging kan een stap net weg zijn (dan zit je met een munt die je niet wilde, en verlies).
- Drie orders na elkaar kosten tijd; tussen stap 1 en 3 kan de prijs bewegen.
- De EU-versie van de beurs kan minder paren hebben dan de wereldwijde API die we meten.

Waarom het te somber kan zijn: lagere kosten (meer handelsvolume, eigen beurs-token, maker in plaats van taker, de 0%-paren van OKX die we niet konden ophalen, Bitstamp gratis onder $1.000 volume per 30 dagen) en sneller meten dan elke paar seconden laten meer zien.

Bron van alle aantallen en bedragen: eigen metingen (GEZIEN), data op de tak `ai-handel-data`, map `driehoek/`. Kosten per stap en hun bron: README.md.
