# Driehoek-meter: rapport

## Kort antwoord

Op de beurzen met vergunning (MiCA, ook via een EU-dochter): 17 echte kansen die met €100 konden (17 als je elke driehoek los telt; 85,9 per dag). Samen €263,99 tot €263,99 per dag met €100 en €523,70 tot €523,70 per dag met €200 (GOK; het lage getal voegt driehoeken samen die hetzelfde stukje boek willen, het hoge telt ze los; allebei alsof je ze allemaal als eerste pakt, met het geld al op de juiste beurs). Op de grijze beurzen (geen vergunning): 3 echte kansen die met €100 konden (3 als je elke driehoek los telt; 15,2 per dag). Samen €0,45 tot €0,45 per dag met €100 en €0,90 tot €0,90 per dag met €200 (GOK; het lage getal voegt driehoeken samen die hetzelfde stukje boek willen, het hoge telt ze los; allebei alsof je ze allemaal als eerste pakt, met het geld al op de juiste beurs).

Uitleg: **takerkosten** zijn wat de beurs per order rekent als je meteen koopt of verkoopt tegen de prijs die er ligt (0% tot 0,8% per order; een driehoek is drie orders). **Diepte** is hoeveel euro je tegen die winstgevende prijzen echt kunt kopen en verkopen voordat de prijs slechter wordt. Wij meten elke 3 tot 5 seconden; snelle bots pakken zulke kansen meestal binnen milliseconden, dus wat hier staat is wat er na hen overbleef.

Data: 96 driehoeken met winst op het boek gezien (ook kleine en korte), 1 dag(en) (2026-11-19 tot 2026-11-19). Gemeten: ±4,8 uur per beurs (GEZIEN, uit stand.jsonl).

Een **echte driehoek**: winst na drie keer takerkosten op het orderboek, op twee metingen die minstens 3 seconden uit elkaar liggen elk minstens €100 diepte, bij de latere meting minstens €0,05 winst, en niet meer dan 5% winst (verdacht). Alle bedragen zijn die van de latere meting: wat er na 3 seconden nog stond. Driehoeken op dezelfde beurs die binnen 5 seconden van elkaar bevestigd werden en een paar delen dat geen paar van twee hoofdmunten is (EUR, USD, USDT, USDC, BTC, ETH), tellen als **één kans** (de beste telt): ze willen hetzelfde stukje orderboek. Er wordt niet doorgeketend: een driehoek hoort alleen bij een kans als hij met elk lid ervan dat stukje deelt. Omdat samenvoegen ook te streng kan zijn, staan aantallen en geld er ook los geteld bij (bovengrens).

Regels van vóór 2026-11-19 16:07 UTC (vóór de keuring) hebben geen meting na 3 seconden en tellen daarom nooit als echt. Daar zat ook niets in dat 3 seconden met €100 diepte stond.

## Per beurs: hoe gemeten en hoe dicht bij winst

Beste marge = per ronde de beste driehoek tegen de beste prijzen na kosten (mediaan en hoogste over alle rondes). Negatief = zelfs de beste driehoek verloor geld. Kandidaten = driehoeken die met de beste prijzen winst gaven; daarvan haalt hij de orderboeken op (bekeken), tenzij het budget van die ronde op was (overgeslagen) of de koersen sinds de vorige controle niet veranderden (zelfde). Een positieve beste marge is nog geen winst: de bulk-koers kan achterlopen of er ligt maar een paar cent op die prijs; het orderboek beslist (kolom Winst op boek).

| Beurs | Status | Paren | Driehoeken | Uur | Rondes | Fouten (te veel) | Beste marge mediaan | Beste marge hoogst | Kandidaten | Bekeken | Overgeslagen | Zelfde | Winst op boek | Echt |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| bitget | grijs | 3659 | 202 | 4,8 | 5441 | 1 (0) | -0,285% | 0,012% | 1 | 1 | 0 | 0 | 0 | 0 |
| bitstamp | MiCA | 252 | 346 | 4,8 | 3270 | 0 (0) | -0,232% | 3,905% | 233 | 233 | 0 | 0 | 200 | 13 |
| bitvavo | MiCA | 435 | 22 | 4,8 | 4091 | 0 (0) | -0,759% | -0,670% | 0 | 0 | 0 | 0 | 0 | 0 |
| gate | MiCA-dochter | 2157 | 372 | 4,8 | 4074 | 0 (0) | -0,171% | 1,139% | 894 | 377 | 0 | 517 | 0 | 0 |
| kraken | MiCA | 1352 | 2352 | 4,8 | 3272 | 0 (0) | -0,208% | 1,958% | 152 | 111 | 0 | 40 | 0 | 0 |
| kucoin | MiCA-dochter | 968 | 452 | 4,8 | 5451 | 0 (0) | 0,946% | 1,933% | 6861 | 3461 | 8 | 3390 | 0 | 0 |
| mexc | grijs | 1664 | 886 | 4,8 | 5448 | 0 (0) | 0,493% | 4,975% | 12947 | 5042 | 160 | 7729 | 550 | 3 |
| okx | MiCA-dochter | 1250 | 2338 | 4,8 | 5454 | 0 (0) | -0,134% | 2,841% | 1554 | 1524 | 6 | 24 | 771 | 4 |

## Trechter

| Stap | Alle beurzen | MiCA (ook via EU-dochter) | Grijs |
|---|---|---|---|
| winst op het boek, met de lage kosten (bovengrens) | 96 | 37 | 59 |
| winst op het boek, met de gewone kosten | 96 | 37 | 59 |
| en ooit minstens €100 diepte | 28 | 22 | 6 |
| en na 3 s nog steeds minstens €100 diepte | 22 | 19 | 3 |
| en dan minstens €0,05 winst | 22 | 19 | 3 |
| en niet verdacht = **echt** | 20 | 17 | 3 |
| echte **kansen** (samengevoegd als ze hetzelfde stukje boek willen; ondergrens) | 20 | 17 | 3 |

De lage kosten verschillen alleen bij Bitvavo (categorie B, C en D: USDC- en stablecoinparen; Bitvavo noemt ze lager dan 0,25% maar geeft geen getal, dus laag = 0%, GOK). Overal elders is laag gelijk aan gewoon.

## Per dag (echte kansen, bedragen na 3 seconden)

| Dag | Soort | Driehoeken | Kansen | Mediane winst per kans | Mediane diepte | Mediane duur met €100 diepte | Totale winst (volle diepte) |
|---|---|---|---|---|---|---|---|
| 2026-11-19 | Alle beurzen | 20 | 20 | €8,60 | €227 | 15,0 s | €139,72 |
| 2026-11-19 | MiCA (ook via EU-dochter) | 17 | 17 | €8,97 | €227 | 20,0 s | €119,09 |
| 2026-11-19 | Grijs | 3 | 3 | €0,26 | €3.309 | 6,0 s | €20,63 |
| totaal | Alle beurzen | 20 | 20 | €8,60 | €227 | 15,0 s | €139,72 |
| totaal | MiCA (ook via EU-dochter) | 17 | 17 | €8,97 | €227 | 20,0 s | €119,09 |
| totaal | Grijs | 3 | 3 | €0,26 | €3.309 | 6,0 s | €20,63 |

## Beste driehoeken per beurs (echt, bedragen na 3 seconden)

**bitstamp** (MiCA)

| Driehoek | Keren | Mediane winst | Hoogste winst | Mediane diepte | Mediane duur met €100 diepte | Kosten per stap |
|---|---|---|---|---|---|---|
| EUR>USD>SKY>EUR | 13 | €9,05 | €11,32 | €227 | 15,0 s | 0,08% + 0,40% + 0,40% |

**mexc** (grijs)

| Driehoek | Keren | Mediane winst | Hoogste winst | Mediane diepte | Mediane duur met €100 diepte | Kosten per stap |
|---|---|---|---|---|---|---|
| USDT>BTC>USDC>USDT | 1 | €20,12 | €20,12 | €60.185 | 14,0 s | 0,05% + 0,00% + 0,00% |
| USDT>SOL>USDC>USDT | 1 | €0,26 | €0,26 | €3.309 | 3,0 s | 0,05% + 0,00% + 0,00% |
| USDT>USDC>BTC>USDT | 1 | €0,25 | €0,25 | €694 | 6,0 s | 0,00% + 0,00% + 0,05% |

**okx** (MiCA-dochter)

| Driehoek | Keren | Mediane winst | Hoogste winst | Mediane diepte | Mediane duur met €100 diepte | Kosten per stap |
|---|---|---|---|---|---|---|
| USDT>XANT>USDC>USDT | 3 | €0,80 | €1,98 | €355 | 216,0 s | 0,10% + 0,10% + 0,10% |
| USDT>USDC>XANT>USDT | 1 | €1,75 | €1,75 | €284 | 156,0 s | 0,10% + 0,10% + 0,10% |

Grootste driehoeken die **niet** echt waren (te kort, te dun, te weinig winst of verdacht). Bedragen van het beste moment:

| Beurs | Driehoek | Winst | Diepte | Duur | Na 3 s nog €100 diepte | Verdacht |
|---|---|---|---|---|---|---|
| bitstamp | EUR>USD>SKY>EUR | €12,45 | €227 | 170 s | ja | ja |
| bitstamp | EUR>USD>SKY>EUR | €12,24 | €227 | 15 s | ja | ja |
| bitstamp | EUR>USD>SKY>EUR | €10,43 | €227 | 0 s | nee | nee |
| bitstamp | EUR>USD>SKY>EUR | €10,10 | €227 | 0 s | nee | nee |
| bitstamp | EUR>USD>SKY>EUR | €8,90 | €227 | 0 s | nee | nee |
| bitstamp | EUR>USD>SKY>EUR | €0,96 | €38 | 5 s | nee | nee |
| bitstamp | EUR>USD>SKY>EUR | €0,89 | €38 | 10 s | nee | nee |
| bitstamp | EUR>USD>SKY>EUR | €0,45 | €31 | 25 s | nee | nee |

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

Van de 20 echte kansen konden er 20 met €100 (minimale ordergrootte gehaald op alle drie de orders, winst na 3 seconden).

## Opschaling naar €100, €150, €200, €2.000 en €5.000 inleg (GOK)

Per echte kans nemen we de winst die je bij die inleg na 3 seconden nog had kunnen maken (minder inleggen mag als het boek dunner is; alleen bedragen die de minimale ordergrootte halen). Opgeteld per gemeten dag en dan maal 30 voor een maand.

Elk getal staat er twee keer: **samengevoegd** (ondergrens: driehoeken die op hetzelfde moment, binnen 5 seconden na hun bevestiging, hetzelfde niet-hoofdpaar gebruiken, tellen als één kans; een paar van twee hoofdmunten zoals BTC/EUR of BTCUSDT telt daarbij niet, en er wordt niet doorgeketend) en **los** (bovengrens: elke driehoek apart).

| Soort | Inleg | Kansen per dag (samengevoegd / los) | Winst per dag (samengevoegd / los) | Per maand (GOK, samengevoegd / los) | Alleen de beste beurs, per maand (GOK, samengevoegd) |
|---|---|---|---|---|---|
| Alle beurzen | €100 | 101,1 / 101,1 | €264,44 / €264,44 | €7.933,07 / €7.933,07 | bitstamp: €7.638,67 |
| Alle beurzen | €150 | 101,1 / 101,1 | €394,60 / €394,60 | €11.838,15 / €11.838,15 | bitstamp: €11.399,69 |
| Alle beurzen | €200 | 101,1 / 101,1 | €524,60 / €524,60 | €15.738,08 / €15.738,08 | bitstamp: €15.160,77 |
| Alle beurzen | €2.000 | 101,1 / 101,1 | €607,54 / €607,54 | €18.226,20 / €18.226,20 | bitstamp: €17.289,38 |
| Alle beurzen | €5.000 | 101,1 / 101,1 | €613,74 / €613,74 | €18.412,08 / €18.412,08 | bitstamp: €17.289,38 |
| MiCA (ook via EU-dochter) | €100 | 85,9 / 85,9 | €263,99 / €263,99 | €7.919,58 / €7.919,58 | bitstamp: €7.638,67 |
| MiCA (ook via EU-dochter) | €150 | 85,9 / 85,9 | €393,93 / €393,93 | €11.817,90 / €11.817,90 | bitstamp: €11.399,69 |
| MiCA (ook via EU-dochter) | €200 | 85,9 / 85,9 | €523,70 / €523,70 | €15.711,08 / €15.711,08 | bitstamp: €15.160,77 |
| MiCA (ook via EU-dochter) | €2.000 | 85,9 / 85,9 | €601,72 / €601,72 | €18.051,75 / €18.051,75 | bitstamp: €17.289,38 |
| MiCA (ook via EU-dochter) | €5.000 | 85,9 / 85,9 | €601,72 / €601,72 | €18.051,75 / €18.051,75 | bitstamp: €17.289,38 |
| Grijs | €100 | 15,2 / 15,2 | €0,45 / €0,45 | €13,49 / €13,49 | mexc: €13,49 |
| Grijs | €150 | 15,2 / 15,2 | €0,68 / €0,68 | €20,25 / €20,25 | mexc: €20,25 |
| Grijs | €200 | 15,2 / 15,2 | €0,90 / €0,90 | €27,00 / €27,00 | mexc: €27,00 |
| Grijs | €2.000 | 15,2 / 15,2 | €5,82 / €5,82 | €174,45 / €174,45 | mexc: €174,45 |
| Grijs | €5.000 | 15,2 / 15,2 | €12,01 / €12,01 | €360,33 / €360,33 | mexc: €360,33 |

Waarom dit te rooskleurig is (GOK):

- Het is een **bovengrens**: je pakt elke kans, op elke beurs tegelijk, met het geld al op die beurs. Met weinig geld staat alles op één beurs; de laatste kolom neemt alleen de beste beurs (achteraf gekozen, dus ook te rooskleurig).
- Snelle partijen zitten er in milliseconden bovenop. Wat wij na seconden nog zien, is het restje. Ga je zelf pakken, dan concurreer je met hen en met iedereen die het restje ook ziet; bij elke poging kan een stap net weg zijn (dan zit je met een munt die je niet wilde, en verlies).
- Drie orders na elkaar kosten tijd; tussen stap 1 en 3 kan de prijs bewegen.
- De EU-versie van de beurs kan minder paren hebben dan de wereldwijde API die we meten.

Waarom het te somber kan zijn: lagere kosten (meer handelsvolume, eigen beurs-token, maker in plaats van taker, de 0%-paren van OKX die we niet konden ophalen, Bitstamp gratis onder $1.000 volume per 30 dagen) en sneller meten dan elke paar seconden laten meer zien.

Bron van alle aantallen en bedragen: eigen metingen (GEZIEN), data op de tak `ai-handel-data`, map `driehoek/`. Kosten per stap en hun bron: README.md.
