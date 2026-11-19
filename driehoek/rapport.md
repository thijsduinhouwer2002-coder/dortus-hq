# Driehoek-meter: rapport

## Kort antwoord

Op de beurzen met vergunning (MiCA, ook via een EU-dochter): 35 echte kansen die met €100 konden (35 als je elke driehoek los telt; 118,6 per dag). Samen €378,29 tot €378,29 per dag met €100 en €753,70 tot €753,70 per dag met €200 (GOK; het lage getal voegt driehoeken samen die hetzelfde stukje boek willen, het hoge telt ze los; allebei alsof je ze allemaal als eerste pakt, met het geld al op de juiste beurs). Op de grijze beurzen (geen vergunning): 6 echte kansen die met €100 konden (9 als je elke driehoek los telt; 20,3 per dag). Samen €3,36 tot €7,62 per dag met €100 en €4,30 tot €9,04 per dag met €200 (GOK; het lage getal voegt driehoeken samen die hetzelfde stukje boek willen, het hoge telt ze los; allebei alsof je ze allemaal als eerste pakt, met het geld al op de juiste beurs).

Uitleg: **takerkosten** zijn wat de beurs per order rekent als je meteen koopt of verkoopt tegen de prijs die er ligt (0% tot 0,8% per order; een driehoek is drie orders). **Diepte** is hoeveel euro je tegen die winstgevende prijzen echt kunt kopen en verkopen voordat de prijs slechter wordt. Wij meten elke 3 tot 5 seconden; snelle bots pakken zulke kansen meestal binnen milliseconden, dus wat hier staat is wat er na hen overbleef.

Data: 149 driehoeken met winst op het boek gezien (ook kleine en korte), 1 dag(en) (2026-11-19 tot 2026-11-19). Gemeten: ±7,1 uur per beurs (GEZIEN, uit stand.jsonl).

Een **echte driehoek**: winst na drie keer takerkosten op het orderboek, op twee metingen die minstens 3 seconden uit elkaar liggen elk minstens €100 diepte, bij de latere meting minstens €0,05 winst, en niet meer dan 5% winst (verdacht). Alle bedragen zijn die van de latere meting: wat er na 3 seconden nog stond. Driehoeken op dezelfde beurs die binnen 5 seconden van elkaar bevestigd werden en een paar delen dat geen paar van twee hoofdmunten is (EUR, USD, USDT, USDC, BTC, ETH), tellen als **één kans** (de beste telt): ze willen hetzelfde stukje orderboek. Er wordt niet doorgeketend: een driehoek hoort alleen bij een kans als hij met elk lid ervan dat stukje deelt. Omdat samenvoegen ook te streng kan zijn, staan aantallen en geld er ook los geteld bij (bovengrens).

Regels van vóór 2026-11-19 16:07 UTC (vóór de keuring) hebben geen meting na 3 seconden en tellen daarom nooit als echt. Daar zat ook niets in dat 3 seconden met €100 diepte stond.

## Per beurs: hoe gemeten en hoe dicht bij winst

Beste marge = per ronde de beste driehoek tegen de beste prijzen na kosten (mediaan en hoogste over alle rondes). Negatief = zelfs de beste driehoek verloor geld. Kandidaten = driehoeken die met de beste prijzen winst gaven; daarvan haalt hij de orderboeken op (bekeken), tenzij het budget van die ronde op was (overgeslagen) of de koersen sinds de vorige controle niet veranderden (zelfde). Een positieve beste marge is nog geen winst: de bulk-koers kan achterlopen of er ligt maar een paar cent op die prijs; het orderboek beslist (kolom Winst op boek).

| Beurs | Status | Paren | Driehoeken | Uur | Rondes | Fouten (te veel) | Beste marge mediaan | Beste marge hoogst | Kandidaten | Bekeken | Overgeslagen | Zelfde | Winst op boek | Echt |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| bitget | grijs | 3659 | 202 | 7,1 | 8237 | 1 (0) | -0,283% | 0,019% | 2 | 2 | 0 | 0 | 0 | 0 |
| bitstamp | MiCA | 252 | 346 | 7,1 | 4948 | 0 (0) | -0,231% | 3,905% | 589 | 589 | 0 | 0 | 524 | 31 |
| bitvavo | MiCA | 435 | 22 | 7,1 | 6190 | 0 (0) | -0,759% | -0,655% | 0 | 0 | 0 | 0 | 0 | 0 |
| gate | MiCA-dochter | 2158 | 372 | 7,1 | 6167 | 0 (0) | -0,152% | 1,139% | 1263 | 531 | 0 | 732 | 0 | 0 |
| kraken | MiCA | 1352 | 2352 | 7,1 | 4952 | 0 (0) | -0,202% | 2,789% | 1832 | 1271 | 1 | 560 | 0 | 0 |
| kucoin | MiCA-dochter | 968 | 452 | 7,1 | 8250 | 0 (0) | 1,057% | 2,034% | 10406 | 4347 | 8 | 6049 | 0 | 0 |
| mexc | grijs | 1664 | 886 | 7,1 | 8240 | 0 (0) | 0,311% | 4,975% | 22118 | 10396 | 191 | 11513 | 616 | 9 |
| okx | MiCA-dochter | 1250 | 2338 | 7,1 | 8249 | 0 (0) | -0,135% | 4,743% | 2445 | 2305 | 10 | 128 | 777 | 4 |

## Trechter

| Stap | Alle beurzen | MiCA (ook via EU-dochter) | Grijs |
|---|---|---|---|
| winst op het boek, met de lage kosten (bovengrens) | 149 | 71 | 78 |
| winst op het boek, met de gewone kosten | 149 | 71 | 78 |
| en ooit minstens €100 diepte | 66 | 52 | 14 |
| en na 3 s nog steeds minstens €100 diepte | 53 | 44 | 9 |
| en dan minstens €0,05 winst | 53 | 44 | 9 |
| en niet verdacht = **echt** | 44 | 35 | 9 |
| echte **kansen** (samengevoegd als ze hetzelfde stukje boek willen; ondergrens) | 41 | 35 | 6 |

De lage kosten verschillen alleen bij Bitvavo (categorie B, C en D: USDC- en stablecoinparen; Bitvavo noemt ze lager dan 0,25% maar geeft geen getal, dus laag = 0%, GOK). Overal elders is laag gelijk aan gewoon.

## Per dag (echte kansen, bedragen na 3 seconden)

| Dag | Soort | Driehoeken | Kansen | Mediane winst per kans | Mediane diepte | Mediane duur met €100 diepte | Totale winst (volle diepte) |
|---|---|---|---|---|---|---|---|
| 2026-11-19 | Alle beurzen | 44 | 41 | €7,38 | €227 | 20,0 s | €280,26 |
| 2026-11-19 | MiCA (ook via EU-dochter) | 35 | 35 | €7,78 | €227 | 30,0 s | €253,08 |
| 2026-11-19 | Grijs | 9 | 6 | €0,49 | €2.001 | 7,0 s | €27,18 |
| totaal | Alle beurzen | 44 | 41 | €7,38 | €227 | 20,0 s | €280,26 |
| totaal | MiCA (ook via EU-dochter) | 35 | 35 | €7,78 | €227 | 30,0 s | €253,08 |
| totaal | Grijs | 9 | 6 | €0,49 | €2.001 | 7,0 s | €27,18 |

## Beste driehoeken per beurs (echt, bedragen na 3 seconden)

**bitstamp** (MiCA)

| Driehoek | Keren | Mediane winst | Hoogste winst | Mediane diepte | Mediane duur met €100 diepte | Kosten per stap |
|---|---|---|---|---|---|---|
| EUR>USD>SKY>EUR | 31 | €8,22 | €11,32 | €227 | 25,0 s | 0,08% + 0,40% + 0,40% |

**mexc** (grijs)

| Driehoek | Keren | Mediane winst | Hoogste winst | Mediane diepte | Mediane duur met €100 diepte | Kosten per stap |
|---|---|---|---|---|---|---|
| USDT>BTC>USDC>USDT | 2 | €12,85 | €20,12 | €35.093 | 10,0 s | 0,05% + 0,00% + 0,00% |
| USDT>BTC>BRL>USDT | 1 | €0,64 | €0,64 | €146 | 14,0 s | 0,05% + 0,05% + 0,08% |
| USDT>XRP>BRL>USDT | 1 | €0,63 | €0,63 | €146 | 14,0 s | 0,00% + 0,05% + 0,08% |
| USDT>ETH>BRL>USDT | 1 | €0,45 | €0,45 | €116 | 14,0 s | 0,05% + 0,05% + 0,08% |
| USDT>USDC>BRL>USDT | 1 | €0,34 | €0,34 | €116 | 7,0 s | 0,00% + 0,05% + 0,08% |

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

Van de 41 echte kansen konden er 41 met €100 (minimale ordergrootte gehaald op alle drie de orders, winst na 3 seconden).

## Opschaling naar €100, €150, €200, €2.000 en €5.000 inleg (GOK)

Per echte kans nemen we de winst die je bij die inleg na 3 seconden nog had kunnen maken (minder inleggen mag als het boek dunner is; alleen bedragen die de minimale ordergrootte halen). Opgeteld per gemeten dag en dan maal 30 voor een maand.

Elk getal staat er twee keer: **samengevoegd** (ondergrens: driehoeken die op hetzelfde moment, binnen 5 seconden na hun bevestiging, hetzelfde niet-hoofdpaar gebruiken, tellen als één kans; een paar van twee hoofdmunten zoals BTC/EUR of BTCUSDT telt daarbij niet, en er wordt niet doorgeketend) en **los** (bovengrens: elke driehoek apart).

| Soort | Inleg | Kansen per dag (samengevoegd / los) | Winst per dag (samengevoegd / los) | Per maand (GOK, samengevoegd / los) | Alleen de beste beurs, per maand (GOK, samengevoegd) |
|---|---|---|---|---|---|
| Alle beurzen | €100 | 138,9 / 149,1 | €381,65 / €385,91 | €11.449,65 / €11.577,23 | bitstamp: €11.160,35 |
| Alle beurzen | €150 | 138,9 / 149,1 | €570,10 / €574,84 | €17.102,93 / €17.245,16 | bitstamp: €16.701,07 |
| Alle beurzen | €200 | 138,9 / 149,1 | €757,99 / €762,73 | €22.739,75 / €22.881,97 | bitstamp: €22.241,84 |
| Alle beurzen | €2.000 | 138,9 / 149,1 | €868,61 / €873,36 | €26.058,44 / €26.200,67 | bitstamp: €25.213,45 |
| Alle beurzen | €5.000 | 138,9 / 149,1 | €878,66 / €883,40 | €26.359,75 / €26.501,97 | bitstamp: €25.213,45 |
| MiCA (ook via EU-dochter) | €100 | 118,6 / 118,6 | €378,29 / €378,29 | €11.348,72 / €11.348,72 | bitstamp: €11.160,35 |
| MiCA (ook via EU-dochter) | €150 | 118,6 / 118,6 | €566,05 / €566,05 | €16.981,51 / €16.981,51 | bitstamp: €16.701,07 |
| MiCA (ook via EU-dochter) | €200 | 118,6 / 118,6 | €753,70 / €753,70 | €22.610,87 / €22.610,87 | bitstamp: €22.241,84 |
| MiCA (ook via EU-dochter) | €2.000 | 118,6 / 118,6 | €857,49 / €857,49 | €25.724,69 / €25.724,69 | bitstamp: €25.213,45 |
| MiCA (ook via EU-dochter) | €5.000 | 118,6 / 118,6 | €857,49 / €857,49 | €25.724,69 / €25.724,69 | bitstamp: €25.213,45 |
| Grijs | €100 | 20,3 / 30,5 | €3,36 / €7,62 | €100,93 / €228,51 | mexc: €100,93 |
| Grijs | €150 | 20,3 / 30,5 | €4,05 / €8,79 | €121,42 / €263,64 | mexc: €121,42 |
| Grijs | €200 | 20,3 / 30,5 | €4,30 / €9,04 | €128,88 / €271,10 | mexc: €128,88 |
| Grijs | €2.000 | 20,3 / 30,5 | €11,13 / €15,87 | €333,76 / €475,98 | mexc: €333,76 |
| Grijs | €5.000 | 20,3 / 30,5 | €21,17 / €25,91 | €635,06 / €777,28 | mexc: €635,06 |

Waarom dit te rooskleurig is (GOK):

- Het is een **bovengrens**: je pakt elke kans, op elke beurs tegelijk, met het geld al op die beurs. Met weinig geld staat alles op één beurs; de laatste kolom neemt alleen de beste beurs (achteraf gekozen, dus ook te rooskleurig).
- Snelle partijen zitten er in milliseconden bovenop. Wat wij na seconden nog zien, is het restje. Ga je zelf pakken, dan concurreer je met hen en met iedereen die het restje ook ziet; bij elke poging kan een stap net weg zijn (dan zit je met een munt die je niet wilde, en verlies).
- Drie orders na elkaar kosten tijd; tussen stap 1 en 3 kan de prijs bewegen.
- De EU-versie van de beurs kan minder paren hebben dan de wereldwijde API die we meten.

Waarom het te somber kan zijn: lagere kosten (meer handelsvolume, eigen beurs-token, maker in plaats van taker, de 0%-paren van OKX die we niet konden ophalen, Bitstamp gratis onder $1.000 volume per 30 dagen) en sneller meten dan elke paar seconden laten meer zien.

Bron van alle aantallen en bedragen: eigen metingen (GEZIEN), data op de tak `ai-handel-data`, map `driehoek/`. Kosten per stap en hun bron: README.md.
