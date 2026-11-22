# Driehoek-meter: rapport

## Kort antwoord

Op de beurzen met vergunning (MiCA, ook via een EU-dochter): 117 echte kansen die met €100 konden (118 als je elke driehoek los telt; 38,0 per dag). Samen €52,37 tot €52,60 per dag met €100 en €93,10 tot €93,56 per dag met €200 (GOK; het lage getal voegt driehoeken samen die hetzelfde stukje boek willen, het hoge telt ze los; allebei alsof je ze allemaal als eerste pakt, met het geld al op de juiste beurs). Op de grijze beurzen (geen vergunning): 44 echte kansen die met €100 konden (54 als je elke driehoek los telt; 14,3 per dag). Samen €2,82 tot €3,68 per dag met €100 en €3,79 tot €4,77 per dag met €200 (GOK; het lage getal voegt driehoeken samen die hetzelfde stukje boek willen, het hoge telt ze los; allebei alsof je ze allemaal als eerste pakt, met het geld al op de juiste beurs).

Uitleg: **takerkosten** zijn wat de beurs per order rekent als je meteen koopt of verkoopt tegen de prijs die er ligt (0% tot 0,8% per order; een driehoek is drie orders). **Diepte** is hoeveel euro je tegen die winstgevende prijzen echt kunt kopen en verkopen voordat de prijs slechter wordt. Wij meten elke 3 tot 5 seconden; snelle bots pakken zulke kansen meestal binnen milliseconden, dus wat hier staat is wat er na hen overbleef.

Data: 1239 driehoeken met winst op het boek gezien (ook kleine en korte), 4 dag(en) (2026-11-19 tot 2026-11-22). Gemeten: ±73,9 uur per beurs (GEZIEN, uit stand.jsonl).

Een **echte driehoek**: winst na drie keer takerkosten op het orderboek, op twee metingen die minstens 3 seconden uit elkaar liggen elk minstens €100 diepte, bij de latere meting minstens €0,05 winst, en niet meer dan 5% winst (verdacht). Alle bedragen zijn die van de latere meting: wat er na 3 seconden nog stond. Driehoeken op dezelfde beurs die binnen 5 seconden van elkaar bevestigd werden en een paar delen dat geen paar van twee hoofdmunten is (EUR, USD, USDT, USDC, BTC, ETH), tellen als **één kans** (de beste telt): ze willen hetzelfde stukje orderboek. Er wordt niet doorgeketend: een driehoek hoort alleen bij een kans als hij met elk lid ervan dat stukje deelt. Omdat samenvoegen ook te streng kan zijn, staan aantallen en geld er ook los geteld bij (bovengrens).

Regels van vóór 2026-11-19 16:07 UTC (vóór de keuring) hebben geen meting na 3 seconden en tellen daarom nooit als echt. Daar zat ook niets in dat 3 seconden met €100 diepte stond.

## Per beurs: hoe gemeten en hoe dicht bij winst

Beste marge = per ronde de beste driehoek tegen de beste prijzen na kosten (mediaan en hoogste over alle rondes). Negatief = zelfs de beste driehoek verloor geld. Kandidaten = driehoeken die met de beste prijzen winst gaven; daarvan haalt hij de orderboeken op (bekeken), tenzij het budget van die ronde op was (overgeslagen) of de koersen sinds de vorige controle niet veranderden (zelfde). Een positieve beste marge is nog geen winst: de bulk-koers kan achterlopen of er ligt maar een paar cent op die prijs; het orderboek beslist (kolom Winst op boek).

| Beurs | Status | Paren | Driehoeken | Uur | Rondes | Fouten (te veel) | Beste marge mediaan | Beste marge hoogst | Kandidaten | Bekeken | Overgeslagen | Zelfde | Winst op boek | Echt |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| bitget | grijs | 3658 | 202 | 73,9 | 88344 | 1 (0) | -0,274% | 1,502% | 7879 | 6682 | 122 | 1075 | 1 | 0 |
| bitstamp | MiCA | 252 | 346 | 73,9 | 53000 | 2 (0) | -0,224% | 4,996% | 53518 | 52713 | 324 | 467 | 51926 | 89 |
| bitvavo | MiCA | 435 | 22 | 73,9 | 66287 | 1 (0) | -0,757% | -0,318% | 214 | 185 | 0 | 29 | 9 | 0 |
| gate | MiCA-dochter | 2157 | 372 | 73,9 | 65716 | 3 (0) | -0,157% | 4,075% | 31966 | 13550 | 858 | 17557 | 4 | 0 |
| kraken | MiCA | 1353 | 2352 | 73,9 | 53035 | 1 (0) | -0,200% | 4,907% | 14056 | 8376 | 2229 | 3451 | 3 | 0 |
| kucoin | MiCA-dochter | 968 | 452 | 73,9 | 88406 | 1 (0) | -0,124% | 4,979% | 49976 | 24347 | 256 | 25371 | 8 | 0 |
| mexc | grijs | 1635 | 868 | 73,9 | 88215 | 3 (0) | 0,359% | 4,975% | 260463 | 147958 | 2418 | 108595 | 5337 | 54 |
| okx | MiCA-dochter | 1250 | 2338 | 73,9 | 88397 | 0 (0) | -0,091% | 4,743% | 79174 | 68434 | 1274 | 9464 | 7390 | 29 |

## Trechter

| Stap | Alle beurzen | MiCA (ook via EU-dochter) | Grijs |
|---|---|---|---|
| winst op het boek, met de lage kosten (bovengrens) | 1239 | 564 | 675 |
| winst op het boek, met de gewone kosten | 1230 | 555 | 675 |
| en ooit minstens €100 diepte | 310 | 184 | 126 |
| en na 3 s nog steeds minstens €100 diepte | 202 | 143 | 59 |
| en dan minstens €0,05 winst | 186 | 132 | 54 |
| en niet verdacht = **echt** | 172 | 118 | 54 |
| echte **kansen** (samengevoegd als ze hetzelfde stukje boek willen; ondergrens) | 161 | 117 | 44 |

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
| 2026-11-22 | Alle beurzen | 7 | 6 | €0,37 | €569 | 7,0 s | €2,44 |
| 2026-11-22 | MiCA (ook via EU-dochter) | 2 | 2 | €0,14 | €720 | 31,0 s | €0,29 |
| 2026-11-22 | Grijs | 5 | 4 | €0,58 | €569 | 6,0 s | €2,15 |
| totaal | Alle beurzen | 172 | 161 | €0,64 | €227 | 18,0 s | €527,00 |
| totaal | MiCA (ook via EU-dochter) | 118 | 117 | €1,23 | €227 | 42,0 s | €462,28 |
| totaal | Grijs | 54 | 44 | €0,38 | €214 | 6,0 s | €64,72 |

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
| USDT>BTC>BRL>USDT | 5 | €0,52 | €0,64 | €146 | 6,0 s | 0,05% + 0,05% + 0,08% |
| USDT>SOL>BTC>USDT | 5 | €0,16 | €1,04 | €146 | 17,0 s | 0,05% + 0,05% + 0,05% |
| USDT>BTC>USDC>USDT | 4 | €3,12 | €20,12 | €14.861 | 5,0 s | 0,05% + 0,00% + 0,00% |
| USDT>USDF>ETH>USDT | 4 | €0,68 | €2,09 | €656 | 5,0 s | 0,05% + 0,05% + 0,05% |
| USDT>USDF>BTC>USDT | 4 | €0,34 | €0,53 | €444 | 6,0 s | 0,05% + 0,05% + 0,05% |

**okx** (MiCA-dochter)

| Driehoek | Keren | Mediane winst | Hoogste winst | Mediane diepte | Mediane duur met €100 diepte | Kosten per stap |
|---|---|---|---|---|---|---|
| USDT>SOL>AUD>USDT | 5 | €2,63 | €4,03 | €2.000 | 15,0 s | 0,10% + 0,10% + 0,10% |
| USDT>BTC>AUD>USDT | 4 | €7,67 | €20,31 | €4.154 | 100,0 s | 0,10% + 0,10% + 0,10% |
| USDT>AUD>BTC>USDT | 4 | €1,70 | €4,89 | €1.866 | 26,0 s | 0,10% + 0,10% + 0,10% |
| USDT>XANT>USDC>USDT | 3 | €0,80 | €1,98 | €355 | 216,0 s | 0,10% + 0,10% + 0,10% |
| USDT>XRP>AUD>USDT | 3 | €0,29 | €1,68 | €555 | 18,0 s | 0,10% + 0,10% + 0,10% |

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
| mexc | grijs | 868 | 76 | ≤ €10 | 868 | 868 | 868 | 76 |
| okx | MiCA-dochter | 2338 | 1090 | ≤ €10 | 2334 | 2334 | 2334 | 1090 |

Van de 161 echte kansen konden er 161 met €100 (minimale ordergrootte gehaald op alle drie de orders, winst na 3 seconden).

## Opschaling naar €100, €150, €200, €2.000 en €5.000 inleg (GOK)

Per echte kans nemen we de winst die je bij die inleg na 3 seconden nog had kunnen maken (minder inleggen mag als het boek dunner is; alleen bedragen die de minimale ordergrootte halen). Opgeteld per gemeten dag en dan maal 30 voor een maand.

Elk getal staat er twee keer: **samengevoegd** (ondergrens: driehoeken die op hetzelfde moment, binnen 5 seconden na hun bevestiging, hetzelfde niet-hoofdpaar gebruiken, tellen als één kans; een paar van twee hoofdmunten zoals BTC/EUR of BTCUSDT telt daarbij niet, en er wordt niet doorgeketend) en **los** (bovengrens: elke driehoek apart).

| Soort | Inleg | Kansen per dag (samengevoegd / los) | Winst per dag (samengevoegd / los) | Per maand (GOK, samengevoegd / los) | Alleen de beste beurs, per maand (GOK, samengevoegd) |
|---|---|---|---|---|---|
| Alle beurzen | €100 | 52,3 / 55,8 | €55,20 / €56,28 | €1.655,86 / €1.688,51 | bitstamp: €1.493,86 |
| Alle beurzen | €150 | 52,3 / 55,8 | €77,32 / €78,64 | €2.319,68 / €2.359,21 | bitstamp: €2.100,94 |
| Alle beurzen | €200 | 52,3 / 55,8 | €96,89 / €98,33 | €2.906,57 / €2.949,81 | bitstamp: €2.641,07 |
| Alle beurzen | €2.000 | 52,3 / 55,8 | €132,29 / €137,16 | €3.968,72 / €4.114,88 | bitstamp: €2.931,46 |
| Alle beurzen | €5.000 | 52,3 / 55,8 | €148,33 / €157,41 | €4.449,89 / €4.722,27 | bitstamp: €2.931,46 |
| MiCA (ook via EU-dochter) | €100 | 38,0 / 38,3 | €52,37 / €52,60 | €1.571,11 / €1.577,98 | bitstamp: €1.493,86 |
| MiCA (ook via EU-dochter) | €150 | 38,0 / 38,3 | €73,86 / €74,20 | €2.215,76 / €2.226,07 | bitstamp: €2.100,94 |
| MiCA (ook via EU-dochter) | €200 | 38,0 / 38,3 | €93,10 / €93,56 | €2.792,99 / €2.806,74 | bitstamp: €2.641,07 |
| MiCA (ook via EU-dochter) | €2.000 | 38,0 / 38,3 | €124,07 / €127,66 | €3.722,12 / €3.829,71 | bitstamp: €2.931,46 |
| MiCA (ook via EU-dochter) | €5.000 | 38,0 / 38,3 | €135,80 / €143,34 | €4.074,02 / €4.300,29 | bitstamp: €2.931,46 |
| Grijs | €100 | 14,3 / 17,5 | €2,82 / €3,68 | €84,74 / €110,52 | mexc: €84,74 |
| Grijs | €150 | 14,3 / 17,5 | €3,46 / €4,44 | €103,91 / €133,14 | mexc: €103,91 |
| Grijs | €200 | 14,3 / 17,5 | €3,79 / €4,77 | €113,57 / €143,07 | mexc: €113,57 |
| Grijs | €2.000 | 14,3 / 17,5 | €8,22 / €9,51 | €246,61 / €285,17 | mexc: €246,61 |
| Grijs | €5.000 | 14,3 / 17,5 | €12,53 / €14,07 | €375,87 / €421,98 | mexc: €375,87 |

Waarom dit te rooskleurig is (GOK):

- Het is een **bovengrens**: je pakt elke kans, op elke beurs tegelijk, met het geld al op die beurs. Met weinig geld staat alles op één beurs; de laatste kolom neemt alleen de beste beurs (achteraf gekozen, dus ook te rooskleurig).
- Snelle partijen zitten er in milliseconden bovenop. Wat wij na seconden nog zien, is het restje. Ga je zelf pakken, dan concurreer je met hen en met iedereen die het restje ook ziet; bij elke poging kan een stap net weg zijn (dan zit je met een munt die je niet wilde, en verlies).
- Drie orders na elkaar kosten tijd; tussen stap 1 en 3 kan de prijs bewegen.
- De EU-versie van de beurs kan minder paren hebben dan de wereldwijde API die we meten.

Waarom het te somber kan zijn: lagere kosten (meer handelsvolume, eigen beurs-token, maker in plaats van taker, de 0%-paren van OKX die we niet konden ophalen, Bitstamp gratis onder $1.000 volume per 30 dagen) en sneller meten dan elke paar seconden laten meer zien.

Bron van alle aantallen en bedragen: eigen metingen (GEZIEN), data op de tak `ai-handel-data`, map `driehoek/`. Kosten per stap en hun bron: README.md.
