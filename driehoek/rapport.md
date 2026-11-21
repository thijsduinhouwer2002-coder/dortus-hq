# Driehoek-meter: rapport

## Kort antwoord

Op de beurzen met vergunning (MiCA, ook via een EU-dochter): 115 echte kansen die met €100 konden (116 als je elke driehoek los telt; 59,9 per dag). Samen €83,98 tot €84,35 per dag met €100 en €149,29 tot €150,02 per dag met €200 (GOK; het lage getal voegt driehoeken samen die hetzelfde stukje boek willen, het hoge telt ze los; allebei alsof je ze allemaal als eerste pakt, met het geld al op de juiste beurs). Op de grijze beurzen (geen vergunning): 40 echte kansen die met €100 konden (49 als je elke driehoek los telt; 20,8 per dag). Samen €4,31 tot €5,64 per dag met €100 en €5,69 tot €7,22 per dag met €200 (GOK; het lage getal voegt driehoeken samen die hetzelfde stukje boek willen, het hoge telt ze los; allebei alsof je ze allemaal als eerste pakt, met het geld al op de juiste beurs).

Uitleg: **takerkosten** zijn wat de beurs per order rekent als je meteen koopt of verkoopt tegen de prijs die er ligt (0% tot 0,8% per order; een driehoek is drie orders). **Diepte** is hoeveel euro je tegen die winstgevende prijzen echt kunt kopen en verkopen voordat de prijs slechter wordt. Wij meten elke 3 tot 5 seconden; snelle bots pakken zulke kansen meestal binnen milliseconden, dus wat hier staat is wat er na hen overbleef.

Data: 960 driehoeken met winst op het boek gezien (ook kleine en korte), 3 dag(en) (2026-11-19 tot 2026-11-21). Gemeten: ±46,1 uur per beurs (GEZIEN, uit stand.jsonl).

Een **echte driehoek**: winst na drie keer takerkosten op het orderboek, op twee metingen die minstens 3 seconden uit elkaar liggen elk minstens €100 diepte, bij de latere meting minstens €0,05 winst, en niet meer dan 5% winst (verdacht). Alle bedragen zijn die van de latere meting: wat er na 3 seconden nog stond. Driehoeken op dezelfde beurs die binnen 5 seconden van elkaar bevestigd werden en een paar delen dat geen paar van twee hoofdmunten is (EUR, USD, USDT, USDC, BTC, ETH), tellen als **één kans** (de beste telt): ze willen hetzelfde stukje orderboek. Er wordt niet doorgeketend: een driehoek hoort alleen bij een kans als hij met elk lid ervan dat stukje deelt. Omdat samenvoegen ook te streng kan zijn, staan aantallen en geld er ook los geteld bij (bovengrens).

Regels van vóór 2026-11-19 16:07 UTC (vóór de keuring) hebben geen meting na 3 seconden en tellen daarom nooit als echt. Daar zat ook niets in dat 3 seconden met €100 diepte stond.

## Per beurs: hoe gemeten en hoe dicht bij winst

Beste marge = per ronde de beste driehoek tegen de beste prijzen na kosten (mediaan en hoogste over alle rondes). Negatief = zelfs de beste driehoek verloor geld. Kandidaten = driehoeken die met de beste prijzen winst gaven; daarvan haalt hij de orderboeken op (bekeken), tenzij het budget van die ronde op was (overgeslagen) of de koersen sinds de vorige controle niet veranderden (zelfde). Een positieve beste marge is nog geen winst: de bulk-koers kan achterlopen of er ligt maar een paar cent op die prijs; het orderboek beslist (kolom Winst op boek).

| Beurs | Status | Paren | Driehoeken | Uur | Rondes | Fouten (te veel) | Beste marge mediaan | Beste marge hoogst | Kandidaten | Bekeken | Overgeslagen | Zelfde | Winst op boek | Echt |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| bitget | grijs | 3658 | 202 | 46,1 | 54985 | 1 (0) | -0,271% | 1,502% | 6741 | 5710 | 122 | 909 | 1 | 0 |
| bitstamp | MiCA | 252 | 346 | 46,1 | 32995 | 0 (0) | -0,224% | 4,996% | 33517 | 32720 | 324 | 467 | 31933 | 89 |
| bitvavo | MiCA | 435 | 22 | 46,1 | 41255 | 1 (0) | -0,757% | -0,318% | 175 | 163 | 0 | 12 | 9 | 0 |
| gate | MiCA-dochter | 2158 | 372 | 46,1 | 40811 | 1 (0) | -0,131% | 4,075% | 26207 | 11188 | 799 | 14219 | 3 | 0 |
| kraken | MiCA | 1353 | 2352 | 46,1 | 33014 | 0 (0) | -0,200% | 4,907% | 10992 | 6440 | 1911 | 2641 | 3 | 0 |
| kucoin | MiCA-dochter | 968 | 452 | 46,1 | 55030 | 1 (0) | 0,029% | 4,979% | 45405 | 22376 | 256 | 22771 | 8 | 0 |
| mexc | grijs | 1661 | 886 | 46,1 | 54940 | 0 (0) | 0,318% | 4,975% | 152327 | 88002 | 2064 | 61656 | 4119 | 49 |
| okx | MiCA-dochter | 1250 | 2338 | 46,1 | 55024 | 0 (0) | -0,111% | 4,743% | 47311 | 41542 | 1225 | 4544 | 4877 | 27 |

## Trechter

| Stap | Alle beurzen | MiCA (ook via EU-dochter) | Grijs |
|---|---|---|---|
| winst op het boek, met de lage kosten (bovengrens) | 960 | 463 | 497 |
| winst op het boek, met de gewone kosten | 951 | 454 | 497 |
| en ooit minstens €100 diepte | 284 | 178 | 106 |
| en na 3 s nog steeds minstens €100 diepte | 192 | 138 | 54 |
| en dan minstens €0,05 winst | 179 | 130 | 49 |
| en niet verdacht = **echt** | 165 | 116 | 49 |
| echte **kansen** (samengevoegd als ze hetzelfde stukje boek willen; ondergrens) | 155 | 115 | 40 |

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
| 2026-11-21 | Alle beurzen | 69 | 65 | €0,75 | €227 | 9,0 s | €226,66 |
| 2026-11-21 | MiCA (ook via EU-dochter) | 43 | 42 | €2,58 | €320 | 21,0 s | €194,67 |
| 2026-11-21 | Grijs | 26 | 23 | €0,38 | €182 | 6,0 s | €31,99 |
| totaal | Alle beurzen | 165 | 155 | €0,66 | €227 | 20,0 s | €524,56 |
| totaal | MiCA (ook via EU-dochter) | 116 | 115 | €1,42 | €227 | 44,0 s | €461,99 |
| totaal | Grijs | 49 | 40 | €0,36 | €200 | 6,0 s | €62,57 |

## Beste driehoeken per beurs (echt, bedragen na 3 seconden)

**bitstamp** (MiCA)

| Driehoek | Keren | Mediane winst | Hoogste winst | Mediane diepte | Mediane duur met €100 diepte | Kosten per stap |
|---|---|---|---|---|---|---|
| EUR>IMX>USD>EUR | 48 | €0,39 | €5,07 | €116 | 65,0 s | 0,40% + 0,40% + 0,08% |
| EUR>USD>SKY>EUR | 31 | €8,22 | €11,32 | €227 | 25,0 s | 0,08% + 0,40% + 0,40% |
| EUR>USD>OP>EUR | 5 | €0,07 | €0,14 | €200 | 20,0 s | 0,08% + 0,40% + 0,40% |
| EUR>SAND>USD>EUR | 2 | €1,80 | €3,00 | €227 | 748,0 s | 0,40% + 0,40% + 0,08% |
| EUR>USD>HBAR>EUR | 2 | €0,18 | €0,21 | €355 | 490,0 s | 0,08% + 0,40% + 0,40% |

**mexc** (grijs)

| Driehoek | Keren | Mediane winst | Hoogste winst | Mediane diepte | Mediane duur met €100 diepte | Kosten per stap |
|---|---|---|---|---|---|---|
| USDT>SOL>BTC>USDT | 5 | €0,16 | €1,04 | €146 | 17,0 s | 0,05% + 0,05% + 0,05% |
| USDT>BTC>USDC>USDT | 4 | €3,12 | €20,12 | €14.861 | 5,0 s | 0,05% + 0,00% + 0,00% |
| USDT>USDF>ETH>USDT | 4 | €0,68 | €2,09 | €656 | 5,0 s | 0,05% + 0,05% + 0,05% |
| USDT>BTC>BRL>USDT | 4 | €0,58 | €0,64 | €146 | 6,0 s | 0,05% + 0,05% + 0,08% |
| USDT>ETH>BRL>USDT | 3 | €0,30 | €0,45 | €116 | 6,0 s | 0,05% + 0,05% + 0,08% |

**okx** (MiCA-dochter)

| Driehoek | Keren | Mediane winst | Hoogste winst | Mediane diepte | Mediane duur met €100 diepte | Kosten per stap |
|---|---|---|---|---|---|---|
| USDT>SOL>AUD>USDT | 5 | €2,63 | €4,03 | €2.000 | 15,0 s | 0,10% + 0,10% + 0,10% |
| USDT>BTC>AUD>USDT | 4 | €7,67 | €20,31 | €4.154 | 100,0 s | 0,10% + 0,10% + 0,10% |
| USDT>XANT>USDC>USDT | 3 | €0,80 | €1,98 | €355 | 216,0 s | 0,10% + 0,10% + 0,10% |
| USDT>XRP>AUD>USDT | 3 | €0,29 | €1,68 | €555 | 18,0 s | 0,10% + 0,10% + 0,10% |
| USDT>AUD>BTC>USDT | 2 | €4,04 | €4,89 | €2.647 | 15,0 s | 0,10% + 0,10% + 0,10% |

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
| bitstamp | MiCA | 346 | 260 | €12 | 329 | 329 | 329 | 248 |
| bitvavo | MiCA | 22 | 22 | ≤ €10 | 22 | 22 | 22 | 22 |
| gate | MiCA-dochter | 372 | 0 | ≤ €10 | 372 | 372 | 372 | 0 |
| kraken | MiCA | 2352 | 1368 | ≤ €10 | 2352 | 2352 | 2352 | 1368 |
| kucoin | MiCA-dochter | 452 | 12 | ≤ €10 | 452 | 452 | 452 | 12 |
| mexc | grijs | 886 | 76 | ≤ €10 | 886 | 886 | 886 | 76 |
| okx | MiCA-dochter | 2338 | 1090 | ≤ €10 | 2330 | 2330 | 2330 | 1090 |

Van de 155 echte kansen konden er 155 met €100 (minimale ordergrootte gehaald op alle drie de orders, winst na 3 seconden).

## Opschaling naar €100, €150, €200, €2.000 en €5.000 inleg (GOK)

Per echte kans nemen we de winst die je bij die inleg na 3 seconden nog had kunnen maken (minder inleggen mag als het boek dunner is; alleen bedragen die de minimale ordergrootte halen). Opgeteld per gemeten dag en dan maal 30 voor een maand.

Elk getal staat er twee keer: **samengevoegd** (ondergrens: driehoeken die op hetzelfde moment, binnen 5 seconden na hun bevestiging, hetzelfde niet-hoofdpaar gebruiken, tellen als één kans; een paar van twee hoofdmunten zoals BTC/EUR of BTCUSDT telt daarbij niet, en er wordt niet doorgeketend) en **los** (bovengrens: elke driehoek apart).

| Soort | Inleg | Kansen per dag (samengevoegd / los) | Winst per dag (samengevoegd / los) | Per maand (GOK, samengevoegd / los) | Alleen de beste beurs, per maand (GOK, samengevoegd) |
|---|---|---|---|---|---|
| Alle beurzen | €100 | 80,7 / 85,9 | €88,29 / €89,99 | €2.648,72 / €2.699,71 | bitstamp: €2.396,12 |
| Alle beurzen | €150 | 80,7 / 85,9 | €123,69 / €125,76 | €3.710,71 / €3.772,73 | bitstamp: €3.369,86 |
| Alle beurzen | €200 | 80,7 / 85,9 | €154,98 / €157,25 | €4.649,38 / €4.717,36 | bitstamp: €4.236,22 |
| Alle beurzen | €2.000 | 80,7 / 85,9 | €210,97 / €218,74 | €6.329,20 / €6.562,25 | bitstamp: €4.701,99 |
| Alle beurzen | €5.000 | 80,7 / 85,9 | €236,65 / €251,16 | €7.099,44 / €7.534,95 | bitstamp: €4.701,99 |
| MiCA (ook via EU-dochter) | €100 | 59,9 / 60,4 | €83,98 / €84,35 | €2.519,41 / €2.530,43 | bitstamp: €2.396,12 |
| MiCA (ook via EU-dochter) | €150 | 59,9 / 60,4 | €118,44 / €118,99 | €3.553,10 / €3.569,63 | bitstamp: €3.369,86 |
| MiCA (ook via EU-dochter) | €200 | 59,9 / 60,4 | €149,29 / €150,02 | €4.478,65 / €4.500,69 | bitstamp: €4.236,22 |
| MiCA (ook via EU-dochter) | €2.000 | 59,9 / 60,4 | €198,86 / €204,61 | €5.965,67 / €6.138,26 | bitstamp: €4.701,99 |
| MiCA (ook via EU-dochter) | €5.000 | 59,9 / 60,4 | €217,67 / €229,77 | €6.530,12 / €6.893,05 | bitstamp: €4.701,99 |
| Grijs | €100 | 20,8 / 25,5 | €4,31 / €5,64 | €129,32 / €169,28 | mexc: €129,32 |
| Grijs | €150 | 20,8 / 25,5 | €5,25 / €6,77 | €157,61 / €203,10 | mexc: €157,61 |
| Grijs | €200 | 20,8 / 25,5 | €5,69 / €7,22 | €170,73 / €216,67 | mexc: €170,73 |
| Grijs | €2.000 | 20,8 / 25,5 | €12,12 / €14,13 | €363,53 / €423,99 | mexc: €363,53 |
| Grijs | €5.000 | 20,8 / 25,5 | €18,98 / €21,40 | €569,32 / €641,90 | mexc: €569,32 |

Waarom dit te rooskleurig is (GOK):

- Het is een **bovengrens**: je pakt elke kans, op elke beurs tegelijk, met het geld al op die beurs. Met weinig geld staat alles op één beurs; de laatste kolom neemt alleen de beste beurs (achteraf gekozen, dus ook te rooskleurig).
- Snelle partijen zitten er in milliseconden bovenop. Wat wij na seconden nog zien, is het restje. Ga je zelf pakken, dan concurreer je met hen en met iedereen die het restje ook ziet; bij elke poging kan een stap net weg zijn (dan zit je met een munt die je niet wilde, en verlies).
- Drie orders na elkaar kosten tijd; tussen stap 1 en 3 kan de prijs bewegen.
- De EU-versie van de beurs kan minder paren hebben dan de wereldwijde API die we meten.

Waarom het te somber kan zijn: lagere kosten (meer handelsvolume, eigen beurs-token, maker in plaats van taker, de 0%-paren van OKX die we niet konden ophalen, Bitstamp gratis onder $1.000 volume per 30 dagen) en sneller meten dan elke paar seconden laten meer zien.

Bron van alle aantallen en bedragen: eigen metingen (GEZIEN), data op de tak `ai-handel-data`, map `driehoek/`. Kosten per stap en hun bron: README.md.
