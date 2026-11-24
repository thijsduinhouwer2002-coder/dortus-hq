# Driehoek-meter: rapport

## Kort antwoord

Op de beurzen met vergunning (MiCA, ook via een EU-dochter): 125 echte kansen die met €100 konden (128 als je elke driehoek los telt; 25,7 per dag). Samen €34,13 tot €34,33 per dag met €100 en €60,24 tot €60,62 per dag met €200 (GOK; het lage getal voegt driehoeken samen die hetzelfde stukje boek willen, het hoge telt ze los; allebei alsof je ze allemaal als eerste pakt, met het geld al op de juiste beurs). Op de grijze beurzen (geen vergunning): 53 echte kansen die met €100 konden (63 als je elke driehoek los telt; 10,9 per dag). Samen €2,02 tot €2,56 per dag met €100 en €2,74 tot €3,36 per dag met €200 (GOK; het lage getal voegt driehoeken samen die hetzelfde stukje boek willen, het hoge telt ze los; allebei alsof je ze allemaal als eerste pakt, met het geld al op de juiste beurs).

Uitleg: **takerkosten** zijn wat de beurs per order rekent als je meteen koopt of verkoopt tegen de prijs die er ligt (0% tot 0,8% per order; een driehoek is drie orders). **Diepte** is hoeveel euro je tegen die winstgevende prijzen echt kunt kopen en verkopen voordat de prijs slechter wordt. Wij meten elke 3 tot 5 seconden; snelle bots pakken zulke kansen meestal binnen milliseconden, dus wat hier staat is wat er na hen overbleef.

Data: 1802 driehoeken met winst op het boek gezien (ook kleine en korte), 6 dag(en) (2026-11-19 tot 2026-11-24). Gemeten: ±116,8 uur per beurs (GEZIEN, uit stand.jsonl).

Een **echte driehoek**: winst na drie keer takerkosten op het orderboek, op twee metingen die minstens 3 seconden uit elkaar liggen elk minstens €100 diepte, bij de latere meting minstens €0,05 winst, en niet meer dan 5% winst (verdacht). Alle bedragen zijn die van de latere meting: wat er na 3 seconden nog stond. Driehoeken op dezelfde beurs die binnen 5 seconden van elkaar bevestigd werden en een paar delen dat geen paar van twee hoofdmunten is (EUR, USD, USDT, USDC, BTC, ETH), tellen als **één kans** (de beste telt): ze willen hetzelfde stukje orderboek. Er wordt niet doorgeketend: een driehoek hoort alleen bij een kans als hij met elk lid ervan dat stukje deelt. Omdat samenvoegen ook te streng kan zijn, staan aantallen en geld er ook los geteld bij (bovengrens).

Regels van vóór 2026-11-19 16:07 UTC (vóór de keuring) hebben geen meting na 3 seconden en tellen daarom nooit als echt. Daar zat ook niets in dat 3 seconden met €100 diepte stond.

## Per beurs: hoe gemeten en hoe dicht bij winst

Beste marge = per ronde de beste driehoek tegen de beste prijzen na kosten (mediaan en hoogste over alle rondes). Negatief = zelfs de beste driehoek verloor geld. Kandidaten = driehoeken die met de beste prijzen winst gaven; daarvan haalt hij de orderboeken op (bekeken), tenzij het budget van die ronde op was (overgeslagen) of de koersen sinds de vorige controle niet veranderden (zelfde). Een positieve beste marge is nog geen winst: de bulk-koers kan achterlopen of er ligt maar een paar cent op die prijs; het orderboek beslist (kolom Winst op boek).

| Beurs | Status | Paren | Driehoeken | Uur | Rondes | Fouten (te veel) | Beste marge mediaan | Beste marge hoogst | Kandidaten | Bekeken | Overgeslagen | Zelfde | Winst op boek | Echt |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| bitget | grijs | 3659 | 202 | 116,8 | 139701 | 2 (0) | -0,275% | 1,738% | 11227 | 9720 | 124 | 1383 | 1 | 0 |
| bitstamp | MiCA | 252 | 346 | 116,8 | 83826 | 3 (0) | -0,225% | 4,996% | 86198 | 85152 | 444 | 586 | 82411 | 91 |
| bitvavo | MiCA | 434 | 22 | 116,8 | 104811 | 1 (0) | -0,758% | -0,309% | 517 | 316 | 0 | 201 | 9 | 0 |
| gate | MiCA-dochter | 2157 | 372 | 116,8 | 104067 | 4 (0) | -0,172% | 4,641% | 41120 | 17114 | 951 | 23054 | 4 | 0 |
| kraken | MiCA | 1353 | 2352 | 116,8 | 83857 | 1 (0) | -0,200% | 4,907% | 19498 | 11649 | 3285 | 4564 | 3 | 0 |
| kucoin | MiCA-dochter | 969 | 452 | 116,8 | 139787 | 1 (0) | -0,155% | 4,979% | 57454 | 29687 | 278 | 27487 | 8 | 0 |
| mexc | grijs | 1634 | 868 | 116,8 | 139420 | 10 (0) | 0,283% | 4,999% | 381037 | 222165 | 3389 | 150847 | 5879 | 63 |
| okx | MiCA-dochter | 1250 | 2338 | 116,8 | 139724 | 2 (0) | -0,073% | 4,999% | 213299 | 178628 | 12580 | 22072 | 75844 | 37 |

## Trechter

| Stap | Alle beurzen | MiCA (ook via EU-dochter) | Grijs |
|---|---|---|---|
| winst op het boek, met de lage kosten (bovengrens) | 1802 | 911 | 891 |
| winst op het boek, met de gewone kosten | 1793 | 902 | 891 |
| en ooit minstens €100 diepte | 377 | 199 | 178 |
| en na 3 s nog steeds minstens €100 diepte | 232 | 158 | 74 |
| en dan minstens €0,05 winst | 209 | 146 | 63 |
| en niet verdacht = **echt** | 191 | 128 | 63 |
| echte **kansen** (samengevoegd als ze hetzelfde stukje boek willen; ondergrens) | 178 | 125 | 53 |

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
| 2026-11-22 | Alle beurzen | 10 | 9 | €0,37 | €444 | 21,0 s | €5,33 |
| 2026-11-22 | MiCA (ook via EU-dochter) | 5 | 5 | €0,22 | €355 | 30,0 s | €3,18 |
| 2026-11-22 | Grijs | 5 | 4 | €0,58 | €569 | 6,0 s | €2,15 |
| 2026-11-23 | Alle beurzen | 9 | 8 | €0,21 | €295 | 4,0 s | €4,94 |
| 2026-11-23 | MiCA (ook via EU-dochter) | 2 | 1 | €0,14 | €146 | 66,0 s | €0,14 |
| 2026-11-23 | Grijs | 7 | 7 | €0,23 | €444 | 4,0 s | €4,80 |
| 2026-11-24 | Alle beurzen | 7 | 6 | €0,61 | €148 | 40,0 s | €5,22 |
| 2026-11-24 | MiCA (ook via EU-dochter) | 5 | 4 | €1,49 | €146 | 83,0 s | €5,05 |
| 2026-11-24 | Grijs | 2 | 2 | €0,08 | €217 | 9,0 s | €0,17 |
| totaal | Alle beurzen | 191 | 178 | €0,64 | €227 | 18,0 s | €540,05 |
| totaal | MiCA (ook via EU-dochter) | 128 | 125 | €1,18 | €227 | 44,0 s | €470,37 |
| totaal | Grijs | 63 | 53 | €0,34 | €227 | 6,0 s | €69,69 |

## Beste driehoeken per beurs (echt, bedragen na 3 seconden)

**bitstamp** (MiCA)

| Driehoek | Keren | Mediane winst | Hoogste winst | Mediane diepte | Mediane duur met €100 diepte | Kosten per stap |
|---|---|---|---|---|---|---|
| EUR>IMX>USD>EUR | 48 | €0,39 | €5,07 | €116 | 65,0 s | 0,40% + 0,40% + 0,08% |
| EUR>USD>SKY>EUR | 31 | €8,22 | €11,32 | €227 | 25,0 s | 0,08% + 0,40% + 0,40% |
| EUR>USD>OP>EUR | 5 | €0,07 | €0,14 | €200 | 20,0 s | 0,08% + 0,40% + 0,40% |
| EUR>MOODENG>USD>EUR | 3 | €0,16 | €1,07 | €146 | 65,0 s | 0,40% + 0,40% + 0,08% |
| EUR>SAND>USD>EUR | 2 | €1,80 | €3,00 | €227 | 748,0 s | 0,40% + 0,40% + 0,08% |

**mexc** (grijs)

| Driehoek | Keren | Mediane winst | Hoogste winst | Mediane diepte | Mediane duur met €100 diepte | Kosten per stap |
|---|---|---|---|---|---|---|
| USDT>SOL>BTC>USDT | 7 | €0,12 | €1,04 | €150 | 15,0 s | 0,05% + 0,05% + 0,05% |
| USDT>USDF>ETH>USDT | 5 | €0,81 | €2,09 | €555 | 4,0 s | 0,05% + 0,05% + 0,05% |
| USDT>USDF>BTC>USDT | 5 | €0,45 | €1,08 | €444 | 6,0 s | 0,05% + 0,05% + 0,05% |
| USDT>BTC>BRL>USDT | 5 | €0,52 | €0,64 | €146 | 6,0 s | 0,05% + 0,05% + 0,08% |
| USDT>BTC>USDC>USDT | 4 | €3,12 | €20,12 | €14.861 | 5,0 s | 0,05% + 0,00% + 0,00% |

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
| okx | USDT>ACE>USDC>USDT | €98,04 | €284 | 4159 s | ja | ja |
| gate | USDT>XRP>RLUSD>USDT | €26,32 | €19.722 | 0 s | nee | nee |
| okx | EUR>USDT>ACE>EUR | €18,71 | €182 | 198 s | ja | ja |
| okx | EUR>USDT>ACE>EUR | €16,06 | €182 | 1462 s | ja | ja |
| bitstamp | EUR>USD>SKY>EUR | €14,24 | €227 | 5 s | ja | ja |
| bitstamp | EUR>USD>SKY>EUR | €13,92 | €227 | 30 s | ja | ja |
| bitstamp | EUR>USD>SKY>EUR | €13,13 | €200 | 0 s | nee | ja |
| bitstamp | EUR>USD>SKY>EUR | €12,95 | €227 | 80 s | ja | ja |

## Kan een kleine inleg meedoen? (€100, €150, €200)

Minimale ordergrootte per paar uit de openbare API van elke beurs (aantal munten en bedrag in de quote; Bitget: waarde in USDT). Per beurs: hoeveel driehoeken je met dat bedrag kunt rondmaken zonder dat een van de drie orders onder het minimum valt (tegen de beste prijzen, GEZIEN). Het kleinste bedrag dat we toetsen is €10; "≤ €10" betekent dus €10 of minder. Het aantal munten wordt per order naar beneden afgerond op de stapgrootte van de beurs (uit de API), en bij Bitvavo rekenen we per euro-order €0,01 extra (Bitvavo rondt de kosten naar boven af op de cent).

| Beurs | Status | Driehoeken | Met EUR | Mediaan minimale inleg | Mogelijk met €100 | €150 | €200 | Met EUR en €100 |
|---|---|---|---|---|---|---|---|---|
| bitget | grijs | 202 | 46 | ≤ €10 | 202 | 202 | 202 | 46 |
| bitstamp | MiCA | 346 | 260 | €12 | 337 | 338 | 338 | 253 |
| bitvavo | MiCA | 22 | 22 | ≤ €10 | 22 | 22 | 22 | 22 |
| gate | MiCA-dochter | 372 | 0 | ≤ €10 | 372 | 372 | 372 | 0 |
| kraken | MiCA | 2352 | 1368 | ≤ €10 | 2352 | 2352 | 2352 | 1368 |
| kucoin | MiCA-dochter | 452 | 12 | ≤ €10 | 452 | 452 | 452 | 12 |
| mexc | grijs | 868 | 76 | ≤ €10 | 868 | 868 | 868 | 76 |
| okx | MiCA-dochter | 2338 | 1090 | ≤ €10 | 2326 | 2326 | 2326 | 1086 |

Van de 178 echte kansen konden er 178 met €100 (minimale ordergrootte gehaald op alle drie de orders, winst na 3 seconden).

## Opschaling naar €100, €150, €200, €2.000 en €5.000 inleg (GOK)

Per echte kans nemen we de winst die je bij die inleg na 3 seconden nog had kunnen maken (minder inleggen mag als het boek dunner is; alleen bedragen die de minimale ordergrootte halen). Opgeteld per gemeten dag en dan maal 30 voor een maand.

Elk getal staat er twee keer: **samengevoegd** (ondergrens: driehoeken die op hetzelfde moment, binnen 5 seconden na hun bevestiging, hetzelfde niet-hoofdpaar gebruiken, tellen als één kans; een paar van twee hoofdmunten zoals BTC/EUR of BTCUSDT telt daarbij niet, en er wordt niet doorgeketend) en **los** (bovengrens: elke driehoek apart).

| Soort | Inleg | Kansen per dag (samengevoegd / los) | Winst per dag (samengevoegd / los) | Per maand (GOK, samengevoegd / los) | Alleen de beste beurs, per maand (GOK, samengevoegd) |
|---|---|---|---|---|---|
| Alle beurzen | €100 | 36,6 / 39,3 | €36,15 / €36,89 | €1.084,37 / €1.106,73 | bitstamp: €951,18 |
| Alle beurzen | €150 | 36,6 / 39,3 | €50,48 / €51,39 | €1.514,31 / €1.541,62 | bitstamp: €1.337,69 |
| Alle beurzen | €200 | 36,6 / 39,3 | €62,97 / €63,98 | €1.889,25 / €1.919,39 | bitstamp: €1.679,65 |
| Alle beurzen | €2.000 | 36,6 / 39,3 | €86,05 / €89,54 | €2.581,44 / €2.686,34 | bitstamp: €1.863,50 |
| Alle beurzen | €5.000 | 36,6 / 39,3 | €96,31 / €102,47 | €2.889,39 / €3.074,20 | bitstamp: €1.863,50 |
| MiCA (ook via EU-dochter) | €100 | 25,7 / 26,3 | €34,13 / €34,33 | €1.023,87 / €1.029,91 | bitstamp: €951,18 |
| MiCA (ook via EU-dochter) | €150 | 25,7 / 26,3 | €47,99 / €48,28 | €1.439,74 / €1.448,55 | bitstamp: €1.337,69 |
| MiCA (ook via EU-dochter) | €200 | 25,7 / 26,3 | €60,24 / €60,62 | €1.807,09 / €1.818,56 | bitstamp: €1.679,65 |
| MiCA (ook via EU-dochter) | €2.000 | 25,7 / 26,3 | €80,21 / €82,90 | €2.406,41 / €2.486,89 | bitstamp: €1.863,50 |
| MiCA (ook via EU-dochter) | €5.000 | 25,7 / 26,3 | €87,64 / €92,83 | €2.629,21 / €2.784,82 | bitstamp: €1.863,50 |
| Grijs | €100 | 10,9 / 13,0 | €2,02 / €2,56 | €60,50 / €76,82 | mexc: €60,50 |
| Grijs | €150 | 10,9 / 13,0 | €2,49 / €3,10 | €74,57 / €93,07 | mexc: €74,57 |
| Grijs | €200 | 10,9 / 13,0 | €2,74 / €3,36 | €82,16 / €100,84 | mexc: €82,16 |
| Grijs | €2.000 | 10,9 / 13,0 | €5,83 / €6,65 | €175,03 / €199,45 | mexc: €175,03 |
| Grijs | €5.000 | 10,9 / 13,0 | €8,67 / €9,65 | €260,18 / €289,38 | mexc: €260,18 |

Waarom dit te rooskleurig is (GOK):

- Het is een **bovengrens**: je pakt elke kans, op elke beurs tegelijk, met het geld al op die beurs. Met weinig geld staat alles op één beurs; de laatste kolom neemt alleen de beste beurs (achteraf gekozen, dus ook te rooskleurig).
- Snelle partijen zitten er in milliseconden bovenop. Wat wij na seconden nog zien, is het restje. Ga je zelf pakken, dan concurreer je met hen en met iedereen die het restje ook ziet; bij elke poging kan een stap net weg zijn (dan zit je met een munt die je niet wilde, en verlies).
- Drie orders na elkaar kosten tijd; tussen stap 1 en 3 kan de prijs bewegen.
- De EU-versie van de beurs kan minder paren hebben dan de wereldwijde API die we meten.

Waarom het te somber kan zijn: lagere kosten (meer handelsvolume, eigen beurs-token, maker in plaats van taker, de 0%-paren van OKX die we niet konden ophalen, Bitstamp gratis onder $1.000 volume per 30 dagen) en sneller meten dan elke paar seconden laten meer zien.

Bron van alle aantallen en bedragen: eigen metingen (GEZIEN), data op de tak `ai-handel-data`, map `driehoek/`. Kosten per stap en hun bron: README.md.
