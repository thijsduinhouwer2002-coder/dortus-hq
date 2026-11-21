# Driehoek-meter: rapport

## Kort antwoord

Op de beurzen met vergunning (MiCA, ook via een EU-dochter): 115 echte kansen die met €100 konden (116 als je elke driehoek los telt; 54,1 per dag). Samen €75,88 tot €76,22 per dag met €100 en €134,90 tot €135,56 per dag met €200 (GOK; het lage getal voegt driehoeken samen die hetzelfde stukje boek willen, het hoge telt ze los; allebei alsof je ze allemaal als eerste pakt, met het geld al op de juiste beurs). Op de grijze beurzen (geen vergunning): 40 echte kansen die met €100 konden (49 als je elke driehoek los telt; 18,8 per dag). Samen €3,89 tot €5,10 per dag met €100 en €5,14 tot €6,53 per dag met €200 (GOK; het lage getal voegt driehoeken samen die hetzelfde stukje boek willen, het hoge telt ze los; allebei alsof je ze allemaal als eerste pakt, met het geld al op de juiste beurs).

Uitleg: **takerkosten** zijn wat de beurs per order rekent als je meteen koopt of verkoopt tegen de prijs die er ligt (0% tot 0,8% per order; een driehoek is drie orders). **Diepte** is hoeveel euro je tegen die winstgevende prijzen echt kunt kopen en verkopen voordat de prijs slechter wordt. Wij meten elke 3 tot 5 seconden; snelle bots pakken zulke kansen meestal binnen milliseconden, dus wat hier staat is wat er na hen overbleef.

Data: 975 driehoeken met winst op het boek gezien (ook kleine en korte), 3 dag(en) (2026-11-19 tot 2026-11-21). Gemeten: ±51,0 uur per beurs (GEZIEN, uit stand.jsonl).

Een **echte driehoek**: winst na drie keer takerkosten op het orderboek, op twee metingen die minstens 3 seconden uit elkaar liggen elk minstens €100 diepte, bij de latere meting minstens €0,05 winst, en niet meer dan 5% winst (verdacht). Alle bedragen zijn die van de latere meting: wat er na 3 seconden nog stond. Driehoeken op dezelfde beurs die binnen 5 seconden van elkaar bevestigd werden en een paar delen dat geen paar van twee hoofdmunten is (EUR, USD, USDT, USDC, BTC, ETH), tellen als **één kans** (de beste telt): ze willen hetzelfde stukje orderboek. Er wordt niet doorgeketend: een driehoek hoort alleen bij een kans als hij met elk lid ervan dat stukje deelt. Omdat samenvoegen ook te streng kan zijn, staan aantallen en geld er ook los geteld bij (bovengrens).

Regels van vóór 2026-11-19 16:07 UTC (vóór de keuring) hebben geen meting na 3 seconden en tellen daarom nooit als echt. Daar zat ook niets in dat 3 seconden met €100 diepte stond.

## Per beurs: hoe gemeten en hoe dicht bij winst

Beste marge = per ronde de beste driehoek tegen de beste prijzen na kosten (mediaan en hoogste over alle rondes). Negatief = zelfs de beste driehoek verloor geld. Kandidaten = driehoeken die met de beste prijzen winst gaven; daarvan haalt hij de orderboeken op (bekeken), tenzij het budget van die ronde op was (overgeslagen) of de koersen sinds de vorige controle niet veranderden (zelfde). Een positieve beste marge is nog geen winst: de bulk-koers kan achterlopen of er ligt maar een paar cent op die prijs; het orderboek beslist (kolom Winst op boek).

| Beurs | Status | Paren | Driehoeken | Uur | Rondes | Fouten (te veel) | Beste marge mediaan | Beste marge hoogst | Kandidaten | Bekeken | Overgeslagen | Zelfde | Winst op boek | Echt |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| bitget | grijs | 3658 | 202 | 51,0 | 60881 | 1 (0) | -0,272% | 1,502% | 6766 | 5734 | 122 | 910 | 1 | 0 |
| bitstamp | MiCA | 252 | 346 | 51,0 | 36534 | 0 (0) | -0,224% | 4,996% | 37056 | 36259 | 324 | 467 | 35472 | 89 |
| bitvavo | MiCA | 435 | 22 | 51,0 | 45678 | 1 (0) | -0,757% | -0,318% | 175 | 163 | 0 | 12 | 9 | 0 |
| gate | MiCA-dochter | 2158 | 372 | 51,0 | 45220 | 2 (0) | -0,134% | 4,075% | 27124 | 11552 | 799 | 14772 | 4 | 0 |
| kraken | MiCA | 1353 | 2352 | 51,0 | 36549 | 1 (0) | -0,200% | 4,907% | 11444 | 6700 | 2089 | 2655 | 3 | 0 |
| kucoin | MiCA-dochter | 968 | 452 | 51,0 | 60927 | 1 (0) | 0,002% | 4,979% | 46818 | 23275 | 256 | 23285 | 8 | 0 |
| mexc | grijs | 1661 | 886 | 51,0 | 60827 | 1 (0) | 0,345% | 4,975% | 166951 | 95102 | 2084 | 69150 | 4213 | 49 |
| okx | MiCA-dochter | 1250 | 2338 | 51,0 | 60921 | 0 (0) | -0,111% | 4,743% | 51015 | 44404 | 1225 | 5386 | 4879 | 27 |

## Trechter

| Stap | Alle beurzen | MiCA (ook via EU-dochter) | Grijs |
|---|---|---|---|
| winst op het boek, met de lage kosten (bovengrens) | 975 | 467 | 508 |
| winst op het boek, met de gewone kosten | 966 | 458 | 508 |
| en ooit minstens €100 diepte | 286 | 178 | 108 |
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
| bitstamp | MiCA | 346 | 260 | €12 | 331 | 331 | 331 | 250 |
| bitvavo | MiCA | 22 | 22 | ≤ €10 | 22 | 22 | 22 | 22 |
| gate | MiCA-dochter | 372 | 0 | ≤ €10 | 372 | 372 | 372 | 0 |
| kraken | MiCA | 2352 | 1368 | ≤ €10 | 2352 | 2352 | 2352 | 1368 |
| kucoin | MiCA-dochter | 452 | 12 | ≤ €10 | 452 | 452 | 452 | 12 |
| mexc | grijs | 886 | 76 | ≤ €10 | 886 | 886 | 886 | 76 |
| okx | MiCA-dochter | 2338 | 1090 | ≤ €10 | 2330 | 2330 | 2330 | 1086 |

Van de 155 echte kansen konden er 155 met €100 (minimale ordergrootte gehaald op alle drie de orders, winst na 3 seconden).

## Opschaling naar €100, €150, €200, €2.000 en €5.000 inleg (GOK)

Per echte kans nemen we de winst die je bij die inleg na 3 seconden nog had kunnen maken (minder inleggen mag als het boek dunner is; alleen bedragen die de minimale ordergrootte halen). Opgeteld per gemeten dag en dan maal 30 voor een maand.

Elk getal staat er twee keer: **samengevoegd** (ondergrens: driehoeken die op hetzelfde moment, binnen 5 seconden na hun bevestiging, hetzelfde niet-hoofdpaar gebruiken, tellen als één kans; een paar van twee hoofdmunten zoals BTC/EUR of BTCUSDT telt daarbij niet, en er wordt niet doorgeketend) en **los** (bovengrens: elke driehoek apart).

| Soort | Inleg | Kansen per dag (samengevoegd / los) | Winst per dag (samengevoegd / los) | Per maand (GOK, samengevoegd / los) | Alleen de beste beurs, per maand (GOK, samengevoegd) |
|---|---|---|---|---|---|
| Alle beurzen | €100 | 72,9 / 77,6 | €79,78 / €81,31 | €2.393,37 / €2.439,44 | bitstamp: €2.165,12 |
| Alle beurzen | €150 | 72,9 / 77,6 | €111,77 / €113,63 | €3.352,98 / €3.409,02 | bitstamp: €3.044,99 |
| Alle beurzen | €200 | 72,9 / 77,6 | €140,04 / €142,09 | €4.201,16 / €4.262,58 | bitstamp: €3.827,83 |
| Alle beurzen | €2.000 | 72,9 / 77,6 | €190,63 / €197,65 | €5.719,03 / €5.929,61 | bitstamp: €4.248,69 |
| Alle beurzen | €5.000 | 72,9 / 77,6 | €213,83 / €226,95 | €6.415,02 / €6.808,54 | bitstamp: €4.248,69 |
| MiCA (ook via EU-dochter) | €100 | 54,1 / 54,6 | €75,88 / €76,22 | €2.276,52 / €2.286,48 | bitstamp: €2.165,12 |
| MiCA (ook via EU-dochter) | €150 | 54,1 / 54,6 | €107,02 / €107,52 | €3.210,56 / €3.225,50 | bitstamp: €3.044,99 |
| MiCA (ook via EU-dochter) | €200 | 54,1 / 54,6 | €134,90 / €135,56 | €4.046,88 / €4.066,80 | bitstamp: €3.827,83 |
| MiCA (ook via EU-dochter) | €2.000 | 54,1 / 54,6 | €179,69 / €184,88 | €5.390,55 / €5.546,50 | bitstamp: €4.248,69 |
| MiCA (ook via EU-dochter) | €5.000 | 54,1 / 54,6 | €196,69 / €207,62 | €5.900,58 / €6.228,52 | bitstamp: €4.248,69 |
| Grijs | €100 | 18,8 / 23,1 | €3,89 / €5,10 | €116,85 / €152,96 | mexc: €116,85 |
| Grijs | €150 | 18,8 / 23,1 | €4,75 / €6,12 | €142,42 / €183,52 | mexc: €142,42 |
| Grijs | €200 | 18,8 / 23,1 | €5,14 / €6,53 | €154,27 / €195,78 | mexc: €154,27 |
| Grijs | €2.000 | 18,8 / 23,1 | €10,95 / €12,77 | €328,48 / €383,12 | mexc: €328,48 |
| Grijs | €5.000 | 18,8 / 23,1 | €17,15 / €19,33 | €514,43 / €580,02 | mexc: €514,43 |

Waarom dit te rooskleurig is (GOK):

- Het is een **bovengrens**: je pakt elke kans, op elke beurs tegelijk, met het geld al op die beurs. Met weinig geld staat alles op één beurs; de laatste kolom neemt alleen de beste beurs (achteraf gekozen, dus ook te rooskleurig).
- Snelle partijen zitten er in milliseconden bovenop. Wat wij na seconden nog zien, is het restje. Ga je zelf pakken, dan concurreer je met hen en met iedereen die het restje ook ziet; bij elke poging kan een stap net weg zijn (dan zit je met een munt die je niet wilde, en verlies).
- Drie orders na elkaar kosten tijd; tussen stap 1 en 3 kan de prijs bewegen.
- De EU-versie van de beurs kan minder paren hebben dan de wereldwijde API die we meten.

Waarom het te somber kan zijn: lagere kosten (meer handelsvolume, eigen beurs-token, maker in plaats van taker, de 0%-paren van OKX die we niet konden ophalen, Bitstamp gratis onder $1.000 volume per 30 dagen) en sneller meten dan elke paar seconden laten meer zien.

Bron van alle aantallen en bedragen: eigen metingen (GEZIEN), data op de tak `ai-handel-data`, map `driehoek/`. Kosten per stap en hun bron: README.md.
