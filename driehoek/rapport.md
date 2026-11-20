# Driehoek-meter: rapport

## Kort antwoord

Op de beurzen met vergunning (MiCA, ook via een EU-dochter): 71 echte kansen die met €100 konden (71 als je elke driehoek los telt; 60,1 per dag). Samen €104,10 tot €104,10 per dag met €100 en €199,53 tot €199,53 per dag met €200 (GOK; het lage getal voegt driehoeken samen die hetzelfde stukje boek willen, het hoge telt ze los; allebei alsof je ze allemaal als eerste pakt, met het geld al op de juiste beurs). Op de grijze beurzen (geen vergunning): 16 echte kansen die met €100 konden (22 als je elke driehoek los telt; 13,6 per dag). Samen €1,67 tot €3,25 per dag met €100 en €2,24 tot €4,02 per dag met €200 (GOK; het lage getal voegt driehoeken samen die hetzelfde stukje boek willen, het hoge telt ze los; allebei alsof je ze allemaal als eerste pakt, met het geld al op de juiste beurs).

Uitleg: **takerkosten** zijn wat de beurs per order rekent als je meteen koopt of verkoopt tegen de prijs die er ligt (0% tot 0,8% per order; een driehoek is drie orders). **Diepte** is hoeveel euro je tegen die winstgevende prijzen echt kunt kopen en verkopen voordat de prijs slechter wordt. Wij meten elke 3 tot 5 seconden; snelle bots pakken zulke kansen meestal binnen milliseconden, dus wat hier staat is wat er na hen overbleef.

Data: 409 driehoeken met winst op het boek gezien (ook kleine en korte), 2 dag(en) (2026-11-19 tot 2026-11-20). Gemeten: ±28,3 uur per beurs (GEZIEN, uit stand.jsonl).

Een **echte driehoek**: winst na drie keer takerkosten op het orderboek, op twee metingen die minstens 3 seconden uit elkaar liggen elk minstens €100 diepte, bij de latere meting minstens €0,05 winst, en niet meer dan 5% winst (verdacht). Alle bedragen zijn die van de latere meting: wat er na 3 seconden nog stond. Driehoeken op dezelfde beurs die binnen 5 seconden van elkaar bevestigd werden en een paar delen dat geen paar van twee hoofdmunten is (EUR, USD, USDT, USDC, BTC, ETH), tellen als **één kans** (de beste telt): ze willen hetzelfde stukje orderboek. Er wordt niet doorgeketend: een driehoek hoort alleen bij een kans als hij met elk lid ervan dat stukje deelt. Omdat samenvoegen ook te streng kan zijn, staan aantallen en geld er ook los geteld bij (bovengrens).

Regels van vóór 2026-11-19 16:07 UTC (vóór de keuring) hebben geen meting na 3 seconden en tellen daarom nooit als echt. Daar zat ook niets in dat 3 seconden met €100 diepte stond.

## Per beurs: hoe gemeten en hoe dicht bij winst

Beste marge = per ronde de beste driehoek tegen de beste prijzen na kosten (mediaan en hoogste over alle rondes). Negatief = zelfs de beste driehoek verloor geld. Kandidaten = driehoeken die met de beste prijzen winst gaven; daarvan haalt hij de orderboeken op (bekeken), tenzij het budget van die ronde op was (overgeslagen) of de koersen sinds de vorige controle niet veranderden (zelfde). Een positieve beste marge is nog geen winst: de bulk-koers kan achterlopen of er ligt maar een paar cent op die prijs; het orderboek beslist (kolom Winst op boek).

| Beurs | Status | Paren | Driehoeken | Uur | Rondes | Fouten (te veel) | Beste marge mediaan | Beste marge hoogst | Kandidaten | Bekeken | Overgeslagen | Zelfde | Winst op boek | Echt |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| bitget | grijs | 3659 | 202 | 28,3 | 33703 | 1 (0) | -0,278% | 0,575% | 1628 | 1269 | 0 | 359 | 0 | 0 |
| bitstamp | MiCA | 252 | 346 | 28,3 | 20221 | 0 (0) | -0,228% | 3,905% | 16940 | 16787 | 26 | 123 | 16158 | 67 |
| bitvavo | MiCA | 435 | 22 | 28,3 | 25291 | 1 (0) | -0,757% | -0,318% | 157 | 146 | 0 | 11 | 0 | 0 |
| gate | MiCA-dochter | 2158 | 372 | 28,3 | 25013 | 1 (0) | -0,150% | 4,075% | 9042 | 3868 | 173 | 5001 | 1 | 0 |
| kraken | MiCA | 1353 | 2352 | 28,3 | 20242 | 0 (0) | -0,205% | 3,182% | 5336 | 3580 | 22 | 1734 | 2 | 0 |
| kucoin | MiCA-dochter | 968 | 452 | 28,3 | 33737 | 1 (0) | 1,264% | 4,979% | 40509 | 18314 | 108 | 22085 | 0 | 0 |
| mexc | grijs | 1664 | 886 | 28,3 | 33682 | 0 (0) | 0,206% | 4,975% | 73579 | 39581 | 858 | 32573 | 1881 | 22 |
| okx | MiCA-dochter | 1250 | 2338 | 28,3 | 33734 | 0 (0) | -0,134% | 4,743% | 16265 | 14880 | 120 | 1265 | 3493 | 4 |

## Trechter

| Stap | Alle beurzen | MiCA (ook via EU-dochter) | Grijs |
|---|---|---|---|
| winst op het boek, met de lage kosten (bovengrens) | 409 | 163 | 246 |
| winst op het boek, met de gewone kosten | 409 | 163 | 246 |
| en ooit minstens €100 diepte | 144 | 99 | 45 |
| en na 3 s nog steeds minstens €100 diepte | 107 | 83 | 24 |
| en dan minstens €0,05 winst | 102 | 80 | 22 |
| en niet verdacht = **echt** | 93 | 71 | 22 |
| echte **kansen** (samengevoegd als ze hetzelfde stukje boek willen; ondergrens) | 87 | 71 | 16 |

De lage kosten verschillen alleen bij Bitvavo (categorie B, C en D: USDC- en stablecoinparen; Bitvavo noemt ze lager dan 0,25% maar geeft geen getal, dus laag = 0%, GOK). Overal elders is laag gelijk aan gewoon.

## Per dag (echte kansen, bedragen na 3 seconden)

| Dag | Soort | Driehoeken | Kansen | Mediane winst per kans | Mediane diepte | Mediane duur met €100 diepte | Totale winst (volle diepte) |
|---|---|---|---|---|---|---|---|
| 2026-11-19 | Alle beurzen | 48 | 42 | €7,37 | €227 | 17,0 s | €280,75 |
| 2026-11-19 | MiCA (ook via EU-dochter) | 35 | 35 | €7,78 | €227 | 30,0 s | €253,08 |
| 2026-11-19 | Grijs | 13 | 7 | €0,49 | €694 | 7,0 s | €27,67 |
| 2026-11-20 | Alle beurzen | 45 | 45 | €0,27 | €116 | 45,0 s | €15,76 |
| 2026-11-20 | MiCA (ook via EU-dochter) | 36 | 36 | €0,27 | €116 | 60,0 s | €13,11 |
| 2026-11-20 | Grijs | 9 | 9 | €0,16 | €227 | 3,0 s | €2,66 |
| totaal | Alle beurzen | 93 | 87 | €0,66 | €200 | 30,0 s | €296,51 |
| totaal | MiCA (ook via EU-dochter) | 71 | 71 | €0,94 | €150 | 50,0 s | €266,19 |
| totaal | Grijs | 22 | 16 | €0,36 | €461 | 6,0 s | €30,32 |

## Beste driehoeken per beurs (echt, bedragen na 3 seconden)

**bitstamp** (MiCA)

| Driehoek | Keren | Mediane winst | Hoogste winst | Mediane diepte | Mediane duur met €100 diepte | Kosten per stap |
|---|---|---|---|---|---|---|
| EUR>IMX>USD>EUR | 35 | €0,27 | €1,23 | €116 | 65,0 s | 0,40% + 0,40% + 0,08% |
| EUR>USD>SKY>EUR | 31 | €8,22 | €11,32 | €227 | 25,0 s | 0,08% + 0,40% + 0,40% |
| EUR>MOODENG>USD>EUR | 1 | €0,13 | €0,13 | €150 | 45,0 s | 0,40% + 0,40% + 0,08% |

**mexc** (grijs)

| Driehoek | Keren | Mediane winst | Hoogste winst | Mediane diepte | Mediane duur met €100 diepte | Kosten per stap |
|---|---|---|---|---|---|---|
| USDT>BTC>USDC>USDT | 4 | €3,12 | €20,12 | €14.861 | 5,0 s | 0,05% + 0,00% + 0,00% |
| USDT>ETH>BRL>USDT | 3 | €0,30 | €0,45 | €116 | 6,0 s | 0,05% + 0,05% + 0,08% |
| USDT>SOL>BTC>USDT | 3 | €0,12 | €0,16 | €146 | 17,0 s | 0,05% + 0,05% + 0,05% |
| USDT>XRP>BRL>USDT | 2 | €0,56 | €0,63 | €148 | 10,0 s | 0,00% + 0,05% + 0,08% |
| USDT>BTC>BRL>USDT | 2 | €0,40 | €0,64 | €146 | 10,0 s | 0,05% + 0,05% + 0,08% |

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

Van de 87 echte kansen konden er 87 met €100 (minimale ordergrootte gehaald op alle drie de orders, winst na 3 seconden).

## Opschaling naar €100, €150, €200, €2.000 en €5.000 inleg (GOK)

Per echte kans nemen we de winst die je bij die inleg na 3 seconden nog had kunnen maken (minder inleggen mag als het boek dunner is; alleen bedragen die de minimale ordergrootte halen). Opgeteld per gemeten dag en dan maal 30 voor een maand.

Elk getal staat er twee keer: **samengevoegd** (ondergrens: driehoeken die op hetzelfde moment, binnen 5 seconden na hun bevestiging, hetzelfde niet-hoofdpaar gebruiken, tellen als één kans; een paar van twee hoofdmunten zoals BTC/EUR of BTCUSDT telt daarbij niet, en er wordt niet doorgeketend) en **los** (bovengrens: elke driehoek apart).

| Soort | Inleg | Kansen per dag (samengevoegd / los) | Winst per dag (samengevoegd / los) | Per maand (GOK, samengevoegd / los) | Alleen de beste beurs, per maand (GOK, samengevoegd) |
|---|---|---|---|---|---|
| Alle beurzen | €100 | 73,7 / 78,8 | €105,77 / €107,35 | €3.173,14 / €3.220,63 | bitstamp: €3.075,98 |
| Alle beurzen | €150 | 73,7 / 78,8 | €154,70 / €156,48 | €4.641,14 / €4.694,44 | bitstamp: €4.508,41 |
| Alle beurzen | €200 | 73,7 / 78,8 | €201,77 / €203,55 | €6.053,13 / €6.106,42 | bitstamp: €5.893,60 |
| Alle beurzen | €2.000 | 73,7 / 78,8 | €230,16 / €231,94 | €6.904,79 / €6.958,08 | bitstamp: €6.636,50 |
| Alle beurzen | €5.000 | 73,7 / 78,8 | €233,01 / €234,79 | €6.990,40 / €7.043,70 | bitstamp: €6.636,50 |
| MiCA (ook via EU-dochter) | €100 | 60,1 / 60,1 | €104,10 / €104,10 | €3.123,08 / €3.123,08 | bitstamp: €3.075,98 |
| MiCA (ook via EU-dochter) | €150 | 60,1 / 60,1 | €152,62 / €152,62 | €4.578,52 / €4.578,52 | bitstamp: €4.508,41 |
| MiCA (ook via EU-dochter) | €200 | 60,1 / 60,1 | €199,53 / €199,53 | €5.985,86 / €5.985,86 | bitstamp: €5.893,60 |
| MiCA (ook via EU-dochter) | €2.000 | 60,1 / 60,1 | €225,48 / €225,48 | €6.764,31 / €6.764,31 | bitstamp: €6.636,50 |
| MiCA (ook via EU-dochter) | €5.000 | 60,1 / 60,1 | €225,48 / €225,48 | €6.764,31 / €6.764,31 | bitstamp: €6.636,50 |
| Grijs | €100 | 13,6 / 18,6 | €1,67 / €3,25 | €50,06 / €97,56 | mexc: €50,06 |
| Grijs | €150 | 13,6 / 18,6 | €2,09 / €3,86 | €62,63 / €115,92 | mexc: €62,63 |
| Grijs | €200 | 13,6 / 18,6 | €2,24 / €4,02 | €67,27 / €120,57 | mexc: €67,27 |
| Grijs | €2.000 | 13,6 / 18,6 | €4,68 / €6,46 | €140,48 / €193,77 | mexc: €140,48 |
| Grijs | €5.000 | 13,6 / 18,6 | €7,54 / €9,31 | €226,09 / €279,39 | mexc: €226,09 |

Waarom dit te rooskleurig is (GOK):

- Het is een **bovengrens**: je pakt elke kans, op elke beurs tegelijk, met het geld al op die beurs. Met weinig geld staat alles op één beurs; de laatste kolom neemt alleen de beste beurs (achteraf gekozen, dus ook te rooskleurig).
- Snelle partijen zitten er in milliseconden bovenop. Wat wij na seconden nog zien, is het restje. Ga je zelf pakken, dan concurreer je met hen en met iedereen die het restje ook ziet; bij elke poging kan een stap net weg zijn (dan zit je met een munt die je niet wilde, en verlies).
- Drie orders na elkaar kosten tijd; tussen stap 1 en 3 kan de prijs bewegen.
- De EU-versie van de beurs kan minder paren hebben dan de wereldwijde API die we meten.

Waarom het te somber kan zijn: lagere kosten (meer handelsvolume, eigen beurs-token, maker in plaats van taker, de 0%-paren van OKX die we niet konden ophalen, Bitstamp gratis onder $1.000 volume per 30 dagen) en sneller meten dan elke paar seconden laten meer zien.

Bron van alle aantallen en bedragen: eigen metingen (GEZIEN), data op de tak `ai-handel-data`, map `driehoek/`. Kosten per stap en hun bron: README.md.
