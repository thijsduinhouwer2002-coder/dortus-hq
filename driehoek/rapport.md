# Driehoek-meter: rapport

## Kort antwoord

Op de beurzen met vergunning (MiCA, ook via een EU-dochter): 43 echte kansen die met €100 konden (43 als je elke driehoek los telt; 41,4 per dag). Samen €108,94 tot €108,94 per dag met €100 en €215,90 tot €215,90 per dag met €200 (GOK; het lage getal voegt driehoeken samen die hetzelfde stukje boek willen, het hoge telt ze los; allebei alsof je ze allemaal als eerste pakt, met het geld al op de juiste beurs). Op de grijze beurzen (geen vergunning): 13 echte kansen die met €100 konden (19 als je elke driehoek los telt; 12,5 per dag). Samen €1,62 tot €3,42 per dag met €100 en €2,21 tot €4,23 per dag met €200 (GOK; het lage getal voegt driehoeken samen die hetzelfde stukje boek willen, het hoge telt ze los; allebei alsof je ze allemaal als eerste pakt, met het geld al op de juiste beurs).

Uitleg: **takerkosten** zijn wat de beurs per order rekent als je meteen koopt of verkoopt tegen de prijs die er ligt (0% tot 0,8% per order; een driehoek is drie orders). **Diepte** is hoeveel euro je tegen die winstgevende prijzen echt kunt kopen en verkopen voordat de prijs slechter wordt. Wij meten elke 3 tot 5 seconden; snelle bots pakken zulke kansen meestal binnen milliseconden, dus wat hier staat is wat er na hen overbleef.

Data: 309 driehoeken met winst op het boek gezien (ook kleine en korte), 2 dag(en) (2026-11-19 tot 2026-11-20). Gemeten: ±24,9 uur per beurs (GEZIEN, uit stand.jsonl).

Een **echte driehoek**: winst na drie keer takerkosten op het orderboek, op twee metingen die minstens 3 seconden uit elkaar liggen elk minstens €100 diepte, bij de latere meting minstens €0,05 winst, en niet meer dan 5% winst (verdacht). Alle bedragen zijn die van de latere meting: wat er na 3 seconden nog stond. Driehoeken op dezelfde beurs die binnen 5 seconden van elkaar bevestigd werden en een paar delen dat geen paar van twee hoofdmunten is (EUR, USD, USDT, USDC, BTC, ETH), tellen als **één kans** (de beste telt): ze willen hetzelfde stukje orderboek. Er wordt niet doorgeketend: een driehoek hoort alleen bij een kans als hij met elk lid ervan dat stukje deelt. Omdat samenvoegen ook te streng kan zijn, staan aantallen en geld er ook los geteld bij (bovengrens).

Regels van vóór 2026-11-19 16:07 UTC (vóór de keuring) hebben geen meting na 3 seconden en tellen daarom nooit als echt. Daar zat ook niets in dat 3 seconden met €100 diepte stond.

## Per beurs: hoe gemeten en hoe dicht bij winst

Beste marge = per ronde de beste driehoek tegen de beste prijzen na kosten (mediaan en hoogste over alle rondes). Negatief = zelfs de beste driehoek verloor geld. Kandidaten = driehoeken die met de beste prijzen winst gaven; daarvan haalt hij de orderboeken op (bekeken), tenzij het budget van die ronde op was (overgeslagen) of de koersen sinds de vorige controle niet veranderden (zelfde). Een positieve beste marge is nog geen winst: de bulk-koers kan achterlopen of er ligt maar een paar cent op die prijs; het orderboek beslist (kolom Winst op boek).

| Beurs | Status | Paren | Driehoeken | Uur | Rondes | Fouten (te veel) | Beste marge mediaan | Beste marge hoogst | Kandidaten | Bekeken | Overgeslagen | Zelfde | Winst op boek | Echt |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| bitget | grijs | 3659 | 202 | 24,9 | 29607 | 1 (0) | -0,280% | 0,575% | 1258 | 919 | 0 | 339 | 0 | 0 |
| bitstamp | MiCA | 252 | 346 | 24,9 | 17765 | 0 (0) | -0,229% | 3,905% | 13250 | 13099 | 25 | 123 | 12485 | 39 |
| bitvavo | MiCA | 435 | 22 | 24,9 | 22220 | 1 (0) | -0,757% | -0,318% | 157 | 146 | 0 | 11 | 0 | 0 |
| gate | MiCA-dochter | 2158 | 372 | 24,9 | 21976 | 1 (0) | -0,153% | 4,075% | 7379 | 3116 | 167 | 4095 | 1 | 0 |
| kraken | MiCA | 1353 | 2352 | 24,9 | 17784 | 0 (0) | -0,205% | 3,182% | 5206 | 3462 | 22 | 1722 | 2 | 0 |
| kucoin | MiCA-dochter | 968 | 452 | 24,9 | 29640 | 1 (0) | 1,394% | 4,979% | 39140 | 17016 | 89 | 22033 | 0 | 0 |
| mexc | grijs | 1664 | 886 | 24,9 | 29601 | 0 (0) | 0,194% | 4,975% | 62512 | 31853 | 573 | 29522 | 1464 | 19 |
| okx | MiCA-dochter | 1250 | 2338 | 24,9 | 29638 | 0 (0) | -0,134% | 4,743% | 13443 | 12325 | 112 | 1006 | 3455 | 4 |

## Trechter

| Stap | Alle beurzen | MiCA (ook via EU-dochter) | Grijs |
|---|---|---|---|
| winst op het boek, met de lage kosten (bovengrens) | 309 | 110 | 199 |
| winst op het boek, met de gewone kosten | 309 | 110 | 199 |
| en ooit minstens €100 diepte | 100 | 63 | 37 |
| en na 3 s nog steeds minstens €100 diepte | 71 | 52 | 19 |
| en dan minstens €0,05 winst | 71 | 52 | 19 |
| en niet verdacht = **echt** | 62 | 43 | 19 |
| echte **kansen** (samengevoegd als ze hetzelfde stukje boek willen; ondergrens) | 56 | 43 | 13 |

De lage kosten verschillen alleen bij Bitvavo (categorie B, C en D: USDC- en stablecoinparen; Bitvavo noemt ze lager dan 0,25% maar geeft geen getal, dus laag = 0%, GOK). Overal elders is laag gelijk aan gewoon.

## Per dag (echte kansen, bedragen na 3 seconden)

| Dag | Soort | Driehoeken | Kansen | Mediane winst per kans | Mediane diepte | Mediane duur met €100 diepte | Totale winst (volle diepte) |
|---|---|---|---|---|---|---|---|
| 2026-11-19 | Alle beurzen | 48 | 42 | €7,37 | €227 | 17,0 s | €280,75 |
| 2026-11-19 | MiCA (ook via EU-dochter) | 35 | 35 | €7,78 | €227 | 30,0 s | €253,08 |
| 2026-11-19 | Grijs | 13 | 7 | €0,49 | €694 | 7,0 s | €27,67 |
| 2026-11-20 | Alle beurzen | 14 | 14 | €0,26 | €131 | 19,0 s | €4,00 |
| 2026-11-20 | MiCA (ook via EU-dochter) | 8 | 8 | €0,19 | €116 | 42,0 s | €1,70 |
| 2026-11-20 | Grijs | 6 | 6 | €0,40 | €1.178 | 3,0 s | €2,29 |
| totaal | Alle beurzen | 62 | 56 | €5,64 | €227 | 18,0 s | €284,74 |
| totaal | MiCA (ook via EU-dochter) | 43 | 43 | €6,91 | €227 | 36,0 s | €254,78 |
| totaal | Grijs | 19 | 13 | €0,43 | €1.000 | 6,0 s | €29,96 |

## Beste driehoeken per beurs (echt, bedragen na 3 seconden)

**bitstamp** (MiCA)

| Driehoek | Keren | Mediane winst | Hoogste winst | Mediane diepte | Mediane duur met €100 diepte | Kosten per stap |
|---|---|---|---|---|---|---|
| EUR>USD>SKY>EUR | 31 | €8,22 | €11,32 | €227 | 25,0 s | 0,08% + 0,40% + 0,40% |
| EUR>IMX>USD>EUR | 7 | €0,24 | €0,34 | €116 | 40,0 s | 0,40% + 0,40% + 0,08% |
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
| bitstamp | MiCA | 346 | 260 | €12 | 317 | 318 | 318 | 239 |
| bitvavo | MiCA | 22 | 22 | ≤ €10 | 22 | 22 | 22 | 22 |
| gate | MiCA-dochter | 372 | 0 | ≤ €10 | 372 | 372 | 372 | 0 |
| kraken | MiCA | 2352 | 1368 | ≤ €10 | 2349 | 2352 | 2352 | 1368 |
| kucoin | MiCA-dochter | 452 | 12 | ≤ €10 | 452 | 452 | 452 | 12 |
| mexc | grijs | 886 | 76 | ≤ €10 | 886 | 886 | 886 | 76 |
| okx | MiCA-dochter | 2338 | 1090 | ≤ €10 | 2326 | 2326 | 2326 | 1086 |

Van de 56 echte kansen konden er 56 met €100 (minimale ordergrootte gehaald op alle drie de orders, winst na 3 seconden).

## Opschaling naar €100, €150, €200, €2.000 en €5.000 inleg (GOK)

Per echte kans nemen we de winst die je bij die inleg na 3 seconden nog had kunnen maken (minder inleggen mag als het boek dunner is; alleen bedragen die de minimale ordergrootte halen). Opgeteld per gemeten dag en dan maal 30 voor een maand.

Elk getal staat er twee keer: **samengevoegd** (ondergrens: driehoeken die op hetzelfde moment, binnen 5 seconden na hun bevestiging, hetzelfde niet-hoofdpaar gebruiken, tellen als één kans; een paar van twee hoofdmunten zoals BTC/EUR of BTCUSDT telt daarbij niet, en er wordt niet doorgeketend) en **los** (bovengrens: elke driehoek apart).

| Soort | Inleg | Kansen per dag (samengevoegd / los) | Winst per dag (samengevoegd / los) | Per maand (GOK, samengevoegd / los) | Alleen de beste beurs, per maand (GOK, samengevoegd) |
|---|---|---|---|---|---|
| Alle beurzen | €100 | 53,9 / 59,7 | €110,56 / €112,36 | €3.316,66 / €3.370,67 | bitstamp: €3.214,66 |
| Alle beurzen | €150 | 53,9 / 59,7 | €164,61 / €166,63 | €4.938,23 / €4.998,83 | bitstamp: €4.797,03 |
| Alle beurzen | €200 | 53,9 / 59,7 | €218,11 / €220,13 | €6.543,35 / €6.603,95 | bitstamp: €6.372,17 |
| Alle beurzen | €2.000 | 53,9 / 59,7 | €250,38 / €252,40 | €7.511,53 / €7.572,13 | bitstamp: €7.216,94 |
| Alle beurzen | €5.000 | 53,9 / 59,7 | €253,63 / €255,65 | €7.608,88 / €7.669,49 | bitstamp: €7.216,94 |
| MiCA (ook via EU-dochter) | €100 | 41,4 / 41,4 | €108,94 / €108,94 | €3.268,21 / €3.268,21 | bitstamp: €3.214,66 |
| MiCA (ook via EU-dochter) | €150 | 41,4 / 41,4 | €162,56 / €162,56 | €4.876,76 / €4.876,76 | bitstamp: €4.797,03 |
| MiCA (ook via EU-dochter) | €200 | 41,4 / 41,4 | €215,90 / €215,90 | €6.477,08 / €6.477,08 | bitstamp: €6.372,17 |
| MiCA (ook via EU-dochter) | €2.000 | 41,4 / 41,4 | €245,41 / €245,41 | €7.362,27 / €7.362,27 | bitstamp: €7.216,94 |
| MiCA (ook via EU-dochter) | €5.000 | 41,4 / 41,4 | €245,41 / €245,41 | €7.362,27 / €7.362,27 | bitstamp: €7.216,94 |
| Grijs | €100 | 12,5 / 18,3 | €1,62 / €3,42 | €48,45 / €102,46 | mexc: €48,45 |
| Grijs | €150 | 12,5 / 18,3 | €2,05 / €4,07 | €61,47 / €122,07 | mexc: €61,47 |
| Grijs | €200 | 12,5 / 18,3 | €2,21 / €4,23 | €66,27 / €126,88 | mexc: €66,27 |
| Grijs | €2.000 | 12,5 / 18,3 | €4,98 / €7,00 | €149,25 / €209,86 | mexc: €149,25 |
| Grijs | €5.000 | 12,5 / 18,3 | €8,22 / €10,24 | €246,61 / €307,21 | mexc: €246,61 |

Waarom dit te rooskleurig is (GOK):

- Het is een **bovengrens**: je pakt elke kans, op elke beurs tegelijk, met het geld al op die beurs. Met weinig geld staat alles op één beurs; de laatste kolom neemt alleen de beste beurs (achteraf gekozen, dus ook te rooskleurig).
- Snelle partijen zitten er in milliseconden bovenop. Wat wij na seconden nog zien, is het restje. Ga je zelf pakken, dan concurreer je met hen en met iedereen die het restje ook ziet; bij elke poging kan een stap net weg zijn (dan zit je met een munt die je niet wilde, en verlies).
- Drie orders na elkaar kosten tijd; tussen stap 1 en 3 kan de prijs bewegen.
- De EU-versie van de beurs kan minder paren hebben dan de wereldwijde API die we meten.

Waarom het te somber kan zijn: lagere kosten (meer handelsvolume, eigen beurs-token, maker in plaats van taker, de 0%-paren van OKX die we niet konden ophalen, Bitstamp gratis onder $1.000 volume per 30 dagen) en sneller meten dan elke paar seconden laten meer zien.

Bron van alle aantallen en bedragen: eigen metingen (GEZIEN), data op de tak `ai-handel-data`, map `driehoek/`. Kosten per stap en hun bron: README.md.
