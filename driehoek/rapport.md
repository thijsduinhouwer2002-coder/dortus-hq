# Driehoek-meter: rapport

## Kort antwoord

Op de beurzen met vergunning (MiCA, ook via een EU-dochter): 35 echte kansen die met €100 konden (35 als je elke driehoek los telt; 82,6 per dag). Samen €263,56 tot €263,56 per dag met €100 en €525,12 tot €525,12 per dag met €200 (GOK; het lage getal voegt driehoeken samen die hetzelfde stukje boek willen, het hoge telt ze los; allebei alsof je ze allemaal als eerste pakt, met het geld al op de juiste beurs). Op de grijze beurzen (geen vergunning): 7 echte kansen die met €100 konden (13 als je elke driehoek los telt; 16,5 per dag). Samen €3,20 tot €7,61 per dag met €100 en €4,15 tot €9,10 per dag met €200 (GOK; het lage getal voegt driehoeken samen die hetzelfde stukje boek willen, het hoge telt ze los; allebei alsof je ze allemaal als eerste pakt, met het geld al op de juiste beurs).

Uitleg: **takerkosten** zijn wat de beurs per order rekent als je meteen koopt of verkoopt tegen de prijs die er ligt (0% tot 0,8% per order; een driehoek is drie orders). **Diepte** is hoeveel euro je tegen die winstgevende prijzen echt kunt kopen en verkopen voordat de prijs slechter wordt. Wij meten elke 3 tot 5 seconden; snelle bots pakken zulke kansen meestal binnen milliseconden, dus wat hier staat is wat er na hen overbleef.

Data: 161 driehoeken met winst op het boek gezien (ook kleine en korte), 2 dag(en) (2026-11-19 tot 2026-11-20). Gemeten: ±10,2 uur per beurs (GEZIEN, uit stand.jsonl).

Een **echte driehoek**: winst na drie keer takerkosten op het orderboek, op twee metingen die minstens 3 seconden uit elkaar liggen elk minstens €100 diepte, bij de latere meting minstens €0,05 winst, en niet meer dan 5% winst (verdacht). Alle bedragen zijn die van de latere meting: wat er na 3 seconden nog stond. Driehoeken op dezelfde beurs die binnen 5 seconden van elkaar bevestigd werden en een paar delen dat geen paar van twee hoofdmunten is (EUR, USD, USDT, USDC, BTC, ETH), tellen als **één kans** (de beste telt): ze willen hetzelfde stukje orderboek. Er wordt niet doorgeketend: een driehoek hoort alleen bij een kans als hij met elk lid ervan dat stukje deelt. Omdat samenvoegen ook te streng kan zijn, staan aantallen en geld er ook los geteld bij (bovengrens).

Regels van vóór 2026-11-19 16:07 UTC (vóór de keuring) hebben geen meting na 3 seconden en tellen daarom nooit als echt. Daar zat ook niets in dat 3 seconden met €100 diepte stond.

## Per beurs: hoe gemeten en hoe dicht bij winst

Beste marge = per ronde de beste driehoek tegen de beste prijzen na kosten (mediaan en hoogste over alle rondes). Negatief = zelfs de beste driehoek verloor geld. Kandidaten = driehoeken die met de beste prijzen winst gaven; daarvan haalt hij de orderboeken op (bekeken), tenzij het budget van die ronde op was (overgeslagen) of de koersen sinds de vorige controle niet veranderden (zelfde). Een positieve beste marge is nog geen winst: de bulk-koers kan achterlopen of er ligt maar een paar cent op die prijs; het orderboek beslist (kolom Winst op boek).

| Beurs | Status | Paren | Driehoeken | Uur | Rondes | Fouten (te veel) | Beste marge mediaan | Beste marge hoogst | Kandidaten | Bekeken | Overgeslagen | Zelfde | Winst op boek | Echt |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| bitget | grijs | 3658 | 202 | 10,2 | 11921 | 1 (0) | -0,283% | 0,019% | 2 | 2 | 0 | 0 | 0 | 0 |
| bitstamp | MiCA | 252 | 346 | 10,2 | 7161 | 0 (0) | -0,230% | 3,905% | 1546 | 1545 | 0 | 0 | 1480 | 31 |
| bitvavo | MiCA | 435 | 22 | 10,2 | 8959 | 1 (0) | -0,758% | -0,318% | 144 | 133 | 0 | 11 | 0 | 0 |
| gate | MiCA-dochter | 2153 | 372 | 10,2 | 8929 | 0 (0) | -0,159% | 1,139% | 1729 | 684 | 0 | 1045 | 0 | 0 |
| kraken | MiCA | 1352 | 2352 | 10,2 | 7170 | 0 (0) | 0,121% | 2,789% | 3998 | 2448 | 1 | 1549 | 0 | 0 |
| kucoin | MiCA-dochter | 968 | 452 | 10,2 | 11948 | 0 (0) | 1,214% | 2,324% | 15305 | 7070 | 18 | 8215 | 0 | 0 |
| mexc | grijs | 1664 | 886 | 10,2 | 11939 | 0 (0) | 0,094% | 4,975% | 24753 | 12022 | 191 | 12515 | 671 | 13 |
| okx | MiCA-dochter | 1250 | 2338 | 10,2 | 11947 | 0 (0) | -0,130% | 4,743% | 7105 | 6325 | 11 | 769 | 777 | 4 |

## Trechter

| Stap | Alle beurzen | MiCA (ook via EU-dochter) | Grijs |
|---|---|---|---|
| winst op het boek, met de lage kosten (bovengrens) | 161 | 71 | 90 |
| winst op het boek, met de gewone kosten | 161 | 71 | 90 |
| en ooit minstens €100 diepte | 73 | 52 | 21 |
| en na 3 s nog steeds minstens €100 diepte | 57 | 44 | 13 |
| en dan minstens €0,05 winst | 57 | 44 | 13 |
| en niet verdacht = **echt** | 48 | 35 | 13 |
| echte **kansen** (samengevoegd als ze hetzelfde stukje boek willen; ondergrens) | 42 | 35 | 7 |

De lage kosten verschillen alleen bij Bitvavo (categorie B, C en D: USDC- en stablecoinparen; Bitvavo noemt ze lager dan 0,25% maar geeft geen getal, dus laag = 0%, GOK). Overal elders is laag gelijk aan gewoon.

## Per dag (echte kansen, bedragen na 3 seconden)

| Dag | Soort | Driehoeken | Kansen | Mediane winst per kans | Mediane diepte | Mediane duur met €100 diepte | Totale winst (volle diepte) |
|---|---|---|---|---|---|---|---|
| 2026-11-19 | Alle beurzen | 48 | 42 | €7,37 | €227 | 17,0 s | €280,75 |
| 2026-11-19 | MiCA (ook via EU-dochter) | 35 | 35 | €7,78 | €227 | 30,0 s | €253,08 |
| 2026-11-19 | Grijs | 13 | 7 | €0,49 | €694 | 7,0 s | €27,67 |
| 2026-11-20 | Alle beurzen | 0 | 0 | - | - | - | €0,00 |
| 2026-11-20 | MiCA (ook via EU-dochter) | 0 | 0 | - | - | - | €0,00 |
| 2026-11-20 | Grijs | 0 | 0 | - | - | - | €0,00 |
| totaal | Alle beurzen | 48 | 42 | €7,37 | €227 | 17,0 s | €280,75 |
| totaal | MiCA (ook via EU-dochter) | 35 | 35 | €7,78 | €227 | 30,0 s | €253,08 |
| totaal | Grijs | 13 | 7 | €0,49 | €694 | 7,0 s | €27,67 |

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
| bitstamp | MiCA | 346 | 260 | €12 | 323 | 324 | 324 | 239 |
| bitvavo | MiCA | 22 | 22 | ≤ €10 | 22 | 22 | 22 | 22 |
| gate | MiCA-dochter | 372 | 0 | ≤ €10 | 372 | 372 | 372 | 0 |
| kraken | MiCA | 2352 | 1368 | ≤ €10 | 2352 | 2352 | 2352 | 1368 |
| kucoin | MiCA-dochter | 452 | 12 | ≤ €10 | 452 | 452 | 452 | 12 |
| mexc | grijs | 886 | 76 | ≤ €10 | 886 | 886 | 886 | 76 |
| okx | MiCA-dochter | 2336 | 1090 | ≤ €10 | 2332 | 2332 | 2332 | 1090 |

Van de 42 echte kansen konden er 42 met €100 (minimale ordergrootte gehaald op alle drie de orders, winst na 3 seconden).

## Opschaling naar €100, €150, €200, €2.000 en €5.000 inleg (GOK)

Per echte kans nemen we de winst die je bij die inleg na 3 seconden nog had kunnen maken (minder inleggen mag als het boek dunner is; alleen bedragen die de minimale ordergrootte halen). Opgeteld per gemeten dag en dan maal 30 voor een maand.

Elk getal staat er twee keer: **samengevoegd** (ondergrens: driehoeken die op hetzelfde moment, binnen 5 seconden na hun bevestiging, hetzelfde niet-hoofdpaar gebruiken, tellen als één kans; een paar van twee hoofdmunten zoals BTC/EUR of BTCUSDT telt daarbij niet, en er wordt niet doorgeketend) en **los** (bovengrens: elke driehoek apart).

| Soort | Inleg | Kansen per dag (samengevoegd / los) | Winst per dag (samengevoegd / los) | Per maand (GOK, samengevoegd / los) | Alleen de beste beurs, per maand (GOK, samengevoegd) |
|---|---|---|---|---|---|
| Alle beurzen | €100 | 99,1 / 113,3 | €266,76 / €271,18 | €8.002,92 / €8.135,29 | bitstamp: €7.775,65 |
| Alle beurzen | €150 | 99,1 / 113,3 | €398,35 / €403,31 | €11.950,63 / €12.099,16 | bitstamp: €11.635,99 |
| Alle beurzen | €200 | 99,1 / 113,3 | €529,26 / €534,21 | €15.877,92 / €16.026,45 | bitstamp: €15.496,36 |
| Alle beurzen | €2.000 | 99,1 / 113,3 | €606,34 / €611,29 | €18.190,12 / €18.338,65 | bitstamp: €17.566,75 |
| Alle beurzen | €5.000 | 99,1 / 113,3 | €613,33 / €618,29 | €18.400,05 / €18.548,58 | bitstamp: €17.566,75 |
| MiCA (ook via EU-dochter) | €100 | 82,6 / 82,6 | €263,56 / €263,56 | €7.906,90 / €7.906,90 | bitstamp: €7.775,65 |
| MiCA (ook via EU-dochter) | €150 | 82,6 / 82,6 | €394,38 / €394,38 | €11.831,38 / €11.831,38 | bitstamp: €11.635,99 |
| MiCA (ook via EU-dochter) | €200 | 82,6 / 82,6 | €525,12 / €525,12 | €15.753,47 / €15.753,47 | bitstamp: €15.496,36 |
| MiCA (ook via EU-dochter) | €2.000 | 82,6 / 82,6 | €597,43 / €597,43 | €17.922,94 / €17.922,94 | bitstamp: €17.566,75 |
| MiCA (ook via EU-dochter) | €5.000 | 82,6 / 82,6 | €597,43 / €597,43 | €17.922,94 / €17.922,94 | bitstamp: €17.566,75 |
| Grijs | €100 | 16,5 / 30,7 | €3,20 / €7,61 | €96,02 / €228,39 | mexc: €96,02 |
| Grijs | €150 | 16,5 / 30,7 | €3,97 / €8,93 | €119,25 / €267,78 | mexc: €119,25 |
| Grijs | €200 | 16,5 / 30,7 | €4,15 / €9,10 | €124,44 / €272,97 | mexc: €124,44 |
| Grijs | €2.000 | 16,5 / 30,7 | €8,91 / €13,86 | €267,19 / €415,72 | mexc: €267,19 |
| Grijs | €5.000 | 16,5 / 30,7 | €15,90 / €20,85 | €477,11 / €625,64 | mexc: €477,11 |

Waarom dit te rooskleurig is (GOK):

- Het is een **bovengrens**: je pakt elke kans, op elke beurs tegelijk, met het geld al op die beurs. Met weinig geld staat alles op één beurs; de laatste kolom neemt alleen de beste beurs (achteraf gekozen, dus ook te rooskleurig).
- Snelle partijen zitten er in milliseconden bovenop. Wat wij na seconden nog zien, is het restje. Ga je zelf pakken, dan concurreer je met hen en met iedereen die het restje ook ziet; bij elke poging kan een stap net weg zijn (dan zit je met een munt die je niet wilde, en verlies).
- Drie orders na elkaar kosten tijd; tussen stap 1 en 3 kan de prijs bewegen.
- De EU-versie van de beurs kan minder paren hebben dan de wereldwijde API die we meten.

Waarom het te somber kan zijn: lagere kosten (meer handelsvolume, eigen beurs-token, maker in plaats van taker, de 0%-paren van OKX die we niet konden ophalen, Bitstamp gratis onder $1.000 volume per 30 dagen) en sneller meten dan elke paar seconden laten meer zien.

Bron van alle aantallen en bedragen: eigen metingen (GEZIEN), data op de tak `ai-handel-data`, map `driehoek/`. Kosten per stap en hun bron: README.md.
