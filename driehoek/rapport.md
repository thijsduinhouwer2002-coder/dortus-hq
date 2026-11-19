# Driehoek-meter: rapport

## Kort antwoord

Op de beurzen met vergunning (MiCA, ook via een EU-dochter): 35 echte kansen die met €100 konden (35 als je elke driehoek los telt; 126,0 per dag). Samen €401,93 tot €401,93 per dag met €100 en €800,80 tot €800,80 per dag met €200 (GOK; het lage getal voegt driehoeken samen die hetzelfde stukje boek willen, het hoge telt ze los; allebei alsof je ze allemaal als eerste pakt, met het geld al op de juiste beurs). Op de grijze beurzen (geen vergunning): 6 echte kansen die met €100 konden (9 als je elke driehoek los telt; 21,6 per dag). Samen €3,57 tot €8,09 per dag met €100 en €4,56 tot €9,60 per dag met €200 (GOK; het lage getal voegt driehoeken samen die hetzelfde stukje boek willen, het hoge telt ze los; allebei alsof je ze allemaal als eerste pakt, met het geld al op de juiste beurs).

Uitleg: **takerkosten** zijn wat de beurs per order rekent als je meteen koopt of verkoopt tegen de prijs die er ligt (0% tot 0,8% per order; een driehoek is drie orders). **Diepte** is hoeveel euro je tegen die winstgevende prijzen echt kunt kopen en verkopen voordat de prijs slechter wordt. Wij meten elke 3 tot 5 seconden; snelle bots pakken zulke kansen meestal binnen milliseconden, dus wat hier staat is wat er na hen overbleef.

Data: 148 driehoeken met winst op het boek gezien (ook kleine en korte), 1 dag(en) (2026-11-19 tot 2026-11-19). Gemeten: ±6,7 uur per beurs (GEZIEN, uit stand.jsonl).

Een **echte driehoek**: winst na drie keer takerkosten op het orderboek, op twee metingen die minstens 3 seconden uit elkaar liggen elk minstens €100 diepte, bij de latere meting minstens €0,05 winst, en niet meer dan 5% winst (verdacht). Alle bedragen zijn die van de latere meting: wat er na 3 seconden nog stond. Driehoeken op dezelfde beurs die binnen 5 seconden van elkaar bevestigd werden en een paar delen dat geen paar van twee hoofdmunten is (EUR, USD, USDT, USDC, BTC, ETH), tellen als **één kans** (de beste telt): ze willen hetzelfde stukje orderboek. Er wordt niet doorgeketend: een driehoek hoort alleen bij een kans als hij met elk lid ervan dat stukje deelt. Omdat samenvoegen ook te streng kan zijn, staan aantallen en geld er ook los geteld bij (bovengrens).

Regels van vóór 2026-11-19 16:07 UTC (vóór de keuring) hebben geen meting na 3 seconden en tellen daarom nooit als echt. Daar zat ook niets in dat 3 seconden met €100 diepte stond.

## Per beurs: hoe gemeten en hoe dicht bij winst

Beste marge = per ronde de beste driehoek tegen de beste prijzen na kosten (mediaan en hoogste over alle rondes). Negatief = zelfs de beste driehoek verloor geld. Kandidaten = driehoeken die met de beste prijzen winst gaven; daarvan haalt hij de orderboeken op (bekeken), tenzij het budget van die ronde op was (overgeslagen) of de koersen sinds de vorige controle niet veranderden (zelfde). Een positieve beste marge is nog geen winst: de bulk-koers kan achterlopen of er ligt maar een paar cent op die prijs; het orderboek beslist (kolom Winst op boek).

| Beurs | Status | Paren | Driehoeken | Uur | Rondes | Fouten (te veel) | Beste marge mediaan | Beste marge hoogst | Kandidaten | Bekeken | Overgeslagen | Zelfde | Winst op boek | Echt |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| bitget | grijs | 3659 | 202 | 6,7 | 7737 | 1 (0) | -0,283% | 0,019% | 2 | 2 | 0 | 0 | 0 | 0 |
| bitstamp | MiCA | 252 | 346 | 6,7 | 4648 | 0 (0) | -0,230% | 3,905% | 589 | 589 | 0 | 0 | 524 | 31 |
| bitvavo | MiCA | 435 | 22 | 6,7 | 5814 | 0 (0) | -0,759% | -0,655% | 0 | 0 | 0 | 0 | 0 | 0 |
| gate | MiCA-dochter | 2158 | 372 | 6,7 | 5793 | 0 (0) | -0,151% | 1,139% | 1187 | 498 | 0 | 689 | 0 | 0 |
| kraken | MiCA | 1352 | 2352 | 6,7 | 4651 | 0 (0) | -0,203% | 2,789% | 1530 | 1049 | 0 | 481 | 0 | 0 |
| kucoin | MiCA-dochter | 968 | 452 | 6,7 | 7749 | 0 (0) | 1,057% | 2,034% | 9853 | 4280 | 8 | 5563 | 0 | 0 |
| mexc | grijs | 1664 | 886 | 6,7 | 7741 | 0 (0) | 0,304% | 4,975% | 20075 | 9428 | 190 | 10440 | 615 | 9 |
| okx | MiCA-dochter | 1250 | 2338 | 6,7 | 7749 | 0 (0) | -0,135% | 4,743% | 1869 | 1795 | 6 | 68 | 777 | 4 |

## Trechter

| Stap | Alle beurzen | MiCA (ook via EU-dochter) | Grijs |
|---|---|---|---|
| winst op het boek, met de lage kosten (bovengrens) | 148 | 71 | 77 |
| winst op het boek, met de gewone kosten | 148 | 71 | 77 |
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
| Alle beurzen | €100 | 147,6 / 158,4 | €405,51 / €410,03 | €12.165,25 / €12.300,81 | bitstamp: €11.857,87 |
| Alle beurzen | €150 | 147,6 / 158,4 | €605,73 / €610,77 | €18.171,86 / €18.322,98 | bitstamp: €17.744,89 |
| Alle beurzen | €200 | 147,6 / 158,4 | €805,37 / €810,40 | €24.160,98 / €24.312,10 | bitstamp: €23.631,96 |
| Alle beurzen | €2.000 | 147,6 / 158,4 | €922,90 / €927,94 | €27.687,10 / €27.838,21 | bitstamp: €26.789,29 |
| Alle beurzen | €5.000 | 147,6 / 158,4 | €933,57 / €938,61 | €28.007,23 / €28.158,34 | bitstamp: €26.789,29 |
| MiCA (ook via EU-dochter) | €100 | 126,0 / 126,0 | €401,93 / €401,93 | €12.058,02 / €12.058,02 | bitstamp: €11.857,87 |
| MiCA (ook via EU-dochter) | €150 | 126,0 / 126,0 | €601,43 / €601,43 | €18.042,86 / €18.042,86 | bitstamp: €17.744,89 |
| MiCA (ook via EU-dochter) | €200 | 126,0 / 126,0 | €800,80 / €800,80 | €24.024,05 / €24.024,05 | bitstamp: €23.631,96 |
| MiCA (ook via EU-dochter) | €2.000 | 126,0 / 126,0 | €911,08 / €911,08 | €27.332,48 / €27.332,48 | bitstamp: €26.789,29 |
| MiCA (ook via EU-dochter) | €5.000 | 126,0 / 126,0 | €911,08 / €911,08 | €27.332,48 / €27.332,48 | bitstamp: €26.789,29 |
| Grijs | €100 | 21,6 / 32,4 | €3,57 / €8,09 | €107,23 / €242,79 | mexc: €107,23 |
| Grijs | €150 | 21,6 / 32,4 | €4,30 / €9,34 | €129,01 / €280,12 | mexc: €129,01 |
| Grijs | €200 | 21,6 / 32,4 | €4,56 / €9,60 | €136,93 / €288,05 | mexc: €136,93 |
| Grijs | €2.000 | 21,6 / 32,4 | €11,82 / €16,86 | €354,62 / €505,73 | mexc: €354,62 |
| Grijs | €5.000 | 21,6 / 32,4 | €22,49 / €27,53 | €674,75 / €825,87 | mexc: €674,75 |

Waarom dit te rooskleurig is (GOK):

- Het is een **bovengrens**: je pakt elke kans, op elke beurs tegelijk, met het geld al op die beurs. Met weinig geld staat alles op één beurs; de laatste kolom neemt alleen de beste beurs (achteraf gekozen, dus ook te rooskleurig).
- Snelle partijen zitten er in milliseconden bovenop. Wat wij na seconden nog zien, is het restje. Ga je zelf pakken, dan concurreer je met hen en met iedereen die het restje ook ziet; bij elke poging kan een stap net weg zijn (dan zit je met een munt die je niet wilde, en verlies).
- Drie orders na elkaar kosten tijd; tussen stap 1 en 3 kan de prijs bewegen.
- De EU-versie van de beurs kan minder paren hebben dan de wereldwijde API die we meten.

Waarom het te somber kan zijn: lagere kosten (meer handelsvolume, eigen beurs-token, maker in plaats van taker, de 0%-paren van OKX die we niet konden ophalen, Bitstamp gratis onder $1.000 volume per 30 dagen) en sneller meten dan elke paar seconden laten meer zien.

Bron van alle aantallen en bedragen: eigen metingen (GEZIEN), data op de tak `ai-handel-data`, map `driehoek/`. Kosten per stap en hun bron: README.md.
