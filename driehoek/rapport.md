# Driehoek-meter: rapport

## Kort antwoord

Op de beurzen met vergunning (MiCA, ook via een EU-dochter): 155 echte kansen die met €100 konden (159 als je elke driehoek los telt; 19,8 per dag). Samen €22,18 tot €22,31 per dag met €100 en €38,95 tot €39,19 per dag met €200 (GOK; het lage getal voegt driehoeken samen die hetzelfde stukje boek willen, het hoge telt ze los; allebei alsof je ze allemaal als eerste pakt, met het geld al op de juiste beurs). Op de grijze beurzen (geen vergunning): 82 echte kansen die met €100 konden (95 als je elke driehoek los telt; 10,5 per dag). Samen €1,67 tot €2,11 per dag met €100 en €2,34 tot €2,85 per dag met €200 (GOK; het lage getal voegt driehoeken samen die hetzelfde stukje boek willen, het hoge telt ze los; allebei alsof je ze allemaal als eerste pakt, met het geld al op de juiste beurs).

Uitleg: **takerkosten** zijn wat de beurs per order rekent als je meteen koopt of verkoopt tegen de prijs die er ligt (0% tot 0,8% per order; een driehoek is drie orders). **Diepte** is hoeveel euro je tegen die winstgevende prijzen echt kunt kopen en verkopen voordat de prijs slechter wordt. Wij meten elke 3 tot 5 seconden; snelle bots pakken zulke kansen meestal binnen milliseconden, dus wat hier staat is wat er na hen overbleef.

Data: 2320 driehoeken met winst op het boek gezien (ook kleine en korte), 9 dag(en) (2026-11-19 tot 2026-11-27). Gemeten: ±187,7 uur per beurs (GEZIEN, uit stand.jsonl).

Een **echte driehoek**: winst na drie keer takerkosten op het orderboek, op twee metingen die minstens 3 seconden uit elkaar liggen elk minstens €100 diepte, bij de latere meting minstens €0,05 winst, en niet meer dan 5% winst (verdacht). Alle bedragen zijn die van de latere meting: wat er na 3 seconden nog stond. Driehoeken op dezelfde beurs die binnen 5 seconden van elkaar bevestigd werden en een paar delen dat geen paar van twee hoofdmunten is (EUR, USD, USDT, USDC, BTC, ETH), tellen als **één kans** (de beste telt): ze willen hetzelfde stukje orderboek. Er wordt niet doorgeketend: een driehoek hoort alleen bij een kans als hij met elk lid ervan dat stukje deelt. Omdat samenvoegen ook te streng kan zijn, staan aantallen en geld er ook los geteld bij (bovengrens).

Regels van vóór 2026-11-19 16:07 UTC (vóór de keuring) hebben geen meting na 3 seconden en tellen daarom nooit als echt. Daar zat ook niets in dat 3 seconden met €100 diepte stond.

## Per beurs: hoe gemeten en hoe dicht bij winst

Beste marge = per ronde de beste driehoek tegen de beste prijzen na kosten (mediaan en hoogste over alle rondes). Negatief = zelfs de beste driehoek verloor geld. Kandidaten = driehoeken die met de beste prijzen winst gaven; daarvan haalt hij de orderboeken op (bekeken), tenzij het budget van die ronde op was (overgeslagen) of de koersen sinds de vorige controle niet veranderden (zelfde). Een positieve beste marge is nog geen winst: de bulk-koers kan achterlopen of er ligt maar een paar cent op die prijs; het orderboek beslist (kolom Winst op boek).

| Beurs | Status | Paren | Driehoeken | Uur | Rondes | Fouten (te veel) | Beste marge mediaan | Beste marge hoogst | Kandidaten | Bekeken | Overgeslagen | Zelfde | Winst op boek | Echt |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| bitget | grijs | 3647 | 202 | 187,7 | 224735 | 2 (0) | -0,277% | 1,738% | 12052 | 10268 | 124 | 1660 | 1 | 0 |
| bitstamp | MiCA | 252 | 346 | 187,7 | 134862 | 3 (0) | -0,227% | 4,996% | 144976 | 141509 | 587 | 2861 | 133524 | 107 |
| bitvavo | MiCA | 433 | 22 | 187,7 | 168587 | 2 (0) | -0,759% | -0,309% | 610 | 408 | 0 | 202 | 9 | 0 |
| gate | MiCA-dochter | 2134 | 372 | 187,7 | 167598 | 8 (0) | -0,174% | 4,641% | 60609 | 24303 | 1126 | 35179 | 5 | 0 |
| kraken | MiCA | 1353 | 2352 | 187,7 | 134884 | 1 (0) | -0,201% | 4,992% | 32748 | 20781 | 3847 | 8118 | 11 | 0 |
| kucoin | MiCA-dochter | 973 | 452 | 187,7 | 224843 | 3 (0) | -0,145% | 4,979% | 86624 | 47127 | 292 | 39202 | 9 | 0 |
| mexc | grijs | 1586 | 850 | 187,7 | 223898 | 46 (0) | 0,317% | 4,999% | 581579 | 339194 | 3811 | 225299 | 6900 | 95 |
| okx | MiCA-dochter | 1250 | 2338 | 187,7 | 224718 | 2 (0) | -0,089% | 5,000% | 442944 | 391604 | 16686 | 34616 | 228115 | 52 |

## Trechter

| Stap | Alle beurzen | MiCA (ook via EU-dochter) | Grijs |
|---|---|---|---|
| winst op het boek, met de lage kosten (bovengrens) | 2320 | 1127 | 1193 |
| winst op het boek, met de gewone kosten | 2311 | 1118 | 1193 |
| en ooit minstens €100 diepte | 528 | 248 | 280 |
| en na 3 s nog steeds minstens €100 diepte | 306 | 194 | 112 |
| en dan minstens €0,05 winst | 273 | 178 | 95 |
| en niet verdacht = **echt** | 254 | 159 | 95 |
| echte **kansen** (samengevoegd als ze hetzelfde stukje boek willen; ondergrens) | 237 | 155 | 82 |

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
| 2026-11-24 | Alle beurzen | 11 | 8 | €0,39 | €150 | 15,0 s | €5,90 |
| 2026-11-24 | MiCA (ook via EU-dochter) | 5 | 4 | €1,49 | €146 | 83,0 s | €5,05 |
| 2026-11-24 | Grijs | 6 | 4 | €0,09 | €166 | 6,0 s | €0,85 |
| 2026-11-25 | Alle beurzen | 24 | 23 | €0,40 | €1.694 | 12,0 s | €116,88 |
| 2026-11-25 | MiCA (ook via EU-dochter) | 11 | 10 | €0,40 | €227 | 14,0 s | €88,03 |
| 2026-11-25 | Grijs | 13 | 13 | €0,45 | €6.462 | 9,0 s | €28,85 |
| 2026-11-26 | Alle beurzen | 19 | 19 | €0,50 | €444 | 30,0 s | €14,42 |
| 2026-11-26 | MiCA (ook via EU-dochter) | 14 | 14 | €0,47 | €355 | 60,0 s | €10,30 |
| 2026-11-26 | Grijs | 5 | 5 | €0,50 | €1.084 | 6,0 s | €4,12 |
| 2026-11-27 | Alle beurzen | 16 | 15 | €0,17 | €146 | 4,0 s | €3,71 |
| 2026-11-27 | MiCA (ook via EU-dochter) | 6 | 6 | €0,21 | €280 | 246,0 s | €1,55 |
| 2026-11-27 | Grijs | 10 | 9 | €0,13 | €146 | 3,0 s | €2,15 |
| totaal | Alle beurzen | 254 | 237 | €0,52 | €227 | 15,0 s | €675,75 |
| totaal | MiCA (ook via EU-dochter) | 159 | 155 | €0,80 | €227 | 40,0 s | €570,26 |
| totaal | Grijs | 95 | 82 | €0,30 | €355 | 6,0 s | €105,49 |

## Beste driehoeken per beurs (echt, bedragen na 3 seconden)

**bitstamp** (MiCA)

| Driehoek | Keren | Mediane winst | Hoogste winst | Mediane diepte | Mediane duur met €100 diepte | Kosten per stap |
|---|---|---|---|---|---|---|
| EUR>IMX>USD>EUR | 48 | €0,39 | €5,07 | €116 | 65,0 s | 0,40% + 0,40% + 0,08% |
| EUR>USD>SKY>EUR | 31 | €8,22 | €11,32 | €227 | 25,0 s | 0,08% + 0,40% + 0,40% |
| EUR>MOODENG>USD>EUR | 16 | €0,42 | €2,73 | €320 | 72,0 s | 0,40% + 0,40% + 0,08% |
| EUR>USD>OP>EUR | 5 | €0,07 | €0,14 | €200 | 20,0 s | 0,08% + 0,40% + 0,40% |
| EUR>USD>AXS>EUR | 3 | €0,13 | €0,34 | €227 | 35,0 s | 0,08% + 0,40% + 0,40% |

**mexc** (grijs)

| Driehoek | Keren | Mediane winst | Hoogste winst | Mediane diepte | Mediane duur met €100 diepte | Kosten per stap |
|---|---|---|---|---|---|---|
| USDT>USDF>ETH>USDT | 8 | €0,65 | €2,51 | €555 | 4,0 s | 0,05% + 0,05% + 0,05% |
| USDT>USDF>BTC>USDT | 7 | €0,29 | €1,08 | €444 | 6,0 s | 0,05% + 0,05% + 0,05% |
| USDT>SOL>BTC>USDT | 7 | €0,12 | €1,04 | €150 | 15,0 s | 0,05% + 0,05% + 0,05% |
| USDT>ETH>BRL>USDT | 6 | €0,24 | €0,45 | €116 | 3,0 s | 0,05% + 0,05% + 0,08% |
| USDT>ETH>BTC>USDT | 5 | €4,53 | €9,56 | €10.000 | 6,0 s | 0,05% + 0,05% + 0,05% |

**okx** (MiCA-dochter)

| Driehoek | Keren | Mediane winst | Hoogste winst | Mediane diepte | Mediane duur met €100 diepte | Kosten per stap |
|---|---|---|---|---|---|---|
| USDT>SOL>AUD>USDT | 5 | €2,63 | €4,03 | €2.000 | 15,0 s | 0,10% + 0,10% + 0,10% |
| USDT>BTC>AUD>USDT | 4 | €7,67 | €20,31 | €4.154 | 100,0 s | 0,10% + 0,10% + 0,10% |
| USDT>AUD>BTC>USDT | 4 | €1,70 | €4,89 | €1.866 | 26,0 s | 0,10% + 0,10% + 0,10% |
| USDC>ETH>PLN>USDC | 4 | €0,21 | €0,25 | €116 | 246,0 s | 0,10% + 0,10% + 0,10% |
| USDT>XANT>USDC>USDT | 3 | €0,80 | €1,98 | €355 | 216,0 s | 0,10% + 0,10% + 0,10% |

Grootste driehoeken die **niet** echt waren (te kort, te dun, te weinig winst of verdacht). Bedragen van het beste moment:

| Beurs | Driehoek | Winst | Diepte | Duur | Na 3 s nog €100 diepte | Verdacht |
|---|---|---|---|---|---|---|
| okx | USDT>ACE>USDC>USDT | €98,04 | €284 | 4159 s | ja | ja |
| kraken | EUR>ESP>USD>EUR | €57,40 | €20 | 35 s | nee | ja |
| gate | USDT>XRP>RLUSD>USDT | €26,32 | €19.722 | 0 s | nee | nee |
| okx | EUR>USDT>ACE>EUR | €18,71 | €182 | 198 s | ja | ja |
| okx | EUR>USDT>ACE>EUR | €16,06 | €182 | 1462 s | ja | ja |
| bitstamp | EUR>USD>SKY>EUR | €14,24 | €227 | 5 s | ja | ja |
| bitstamp | EUR>USD>SKY>EUR | €13,92 | €227 | 30 s | ja | ja |
| bitstamp | EUR>USD>SKY>EUR | €13,13 | €200 | 0 s | nee | ja |

## Kan een kleine inleg meedoen? (€100, €150, €200)

Minimale ordergrootte per paar uit de openbare API van elke beurs (aantal munten en bedrag in de quote; Bitget: waarde in USDT). Per beurs: hoeveel driehoeken je met dat bedrag kunt rondmaken zonder dat een van de drie orders onder het minimum valt (tegen de beste prijzen, GEZIEN). Het kleinste bedrag dat we toetsen is €10; "≤ €10" betekent dus €10 of minder. Het aantal munten wordt per order naar beneden afgerond op de stapgrootte van de beurs (uit de API), en bij Bitvavo rekenen we per euro-order €0,01 extra (Bitvavo rondt de kosten naar boven af op de cent).

| Beurs | Status | Driehoeken | Met EUR | Mediaan minimale inleg | Mogelijk met €100 | €150 | €200 | Met EUR en €100 |
|---|---|---|---|---|---|---|---|---|
| bitget | grijs | 202 | 46 | ≤ €10 | 202 | 202 | 202 | 46 |
| bitstamp | MiCA | 346 | 260 | €12 | 335 | 335 | 335 | 251 |
| bitvavo | MiCA | 22 | 22 | ≤ €10 | 22 | 22 | 22 | 22 |
| gate | MiCA-dochter | 372 | 0 | ≤ €10 | 372 | 372 | 372 | 0 |
| kraken | MiCA | 2352 | 1368 | ≤ €10 | 2352 | 2352 | 2352 | 1368 |
| kucoin | MiCA-dochter | 452 | 12 | ≤ €10 | 452 | 452 | 452 | 12 |
| mexc | grijs | 850 | 76 | ≤ €10 | 850 | 850 | 850 | 76 |
| okx | MiCA-dochter | 2338 | 1090 | ≤ €10 | 2330 | 2330 | 2330 | 1090 |

Van de 237 echte kansen konden er 237 met €100 (minimale ordergrootte gehaald op alle drie de orders, winst na 3 seconden).

## Opschaling naar €100, €150, €200, €2.000 en €5.000 inleg (GOK)

Per echte kans nemen we de winst die je bij die inleg na 3 seconden nog had kunnen maken (minder inleggen mag als het boek dunner is; alleen bedragen die de minimale ordergrootte halen). Opgeteld per gemeten dag en dan maal 30 voor een maand.

Elk getal staat er twee keer: **samengevoegd** (ondergrens: driehoeken die op hetzelfde moment, binnen 5 seconden na hun bevestiging, hetzelfde niet-hoofdpaar gebruiken, tellen als één kans; een paar van twee hoofdmunten zoals BTC/EUR of BTCUSDT telt daarbij niet, en er wordt niet doorgeketend) en **los** (bovengrens: elke driehoek apart).

| Soort | Inleg | Kansen per dag (samengevoegd / los) | Winst per dag (samengevoegd / los) | Per maand (GOK, samengevoegd / los) | Alleen de beste beurs, per maand (GOK, samengevoegd) |
|---|---|---|---|---|---|
| Alle beurzen | €100 | 30,3 / 32,5 | €23,85 / €24,42 | €715,54 / €732,62 | bitstamp: €603,37 |
| Alle beurzen | €150 | 30,3 / 32,5 | €33,18 / €33,87 | €995,28 / €1.016,16 | bitstamp: €849,63 |
| Alle beurzen | €200 | 30,3 / 32,5 | €41,28 / €42,04 | €1.238,51 / €1.261,19 | bitstamp: €1.068,16 |
| Alle beurzen | €2.000 | 30,3 / 32,5 | €57,82 / €60,17 | €1.734,64 / €1.805,06 | bitstamp: €1.196,11 |
| Alle beurzen | €5.000 | 30,3 / 32,5 | €65,97 / €70,02 | €1.979,00 / €2.100,66 | bitstamp: €1.196,11 |
| MiCA (ook via EU-dochter) | €100 | 19,8 / 20,3 | €22,18 / €22,31 | €665,53 / €669,36 | bitstamp: €603,37 |
| MiCA (ook via EU-dochter) | €150 | 19,8 / 20,3 | €31,08 / €31,27 | €932,42 / €938,00 | bitstamp: €849,63 |
| MiCA (ook via EU-dochter) | €200 | 19,8 / 20,3 | €38,95 / €39,19 | €1.168,38 / €1.175,66 | bitstamp: €1.068,16 |
| MiCA (ook via EU-dochter) | €2.000 | 19,8 / 20,3 | €52,46 / €54,17 | €1.573,69 / €1.625,14 | bitstamp: €1.196,11 |
| MiCA (ook via EU-dochter) | €5.000 | 19,8 / 20,3 | €57,88 / €61,20 | €1.736,34 / €1.836,05 | bitstamp: €1.196,11 |
| Grijs | €100 | 10,5 / 12,1 | €1,67 / €2,11 | €50,02 / €63,26 | mexc: €50,02 |
| Grijs | €150 | 10,5 / 12,1 | €2,10 / €2,61 | €62,86 / €78,15 | mexc: €62,86 |
| Grijs | €200 | 10,5 / 12,1 | €2,34 / €2,85 | €70,13 / €85,53 | mexc: €70,13 |
| Grijs | €2.000 | 10,5 / 12,1 | €5,37 / €6,00 | €160,95 / €179,92 | mexc: €160,95 |
| Grijs | €5.000 | 10,5 / 12,1 | €8,09 / €8,82 | €242,66 / €264,61 | mexc: €242,66 |

Waarom dit te rooskleurig is (GOK):

- Het is een **bovengrens**: je pakt elke kans, op elke beurs tegelijk, met het geld al op die beurs. Met weinig geld staat alles op één beurs; de laatste kolom neemt alleen de beste beurs (achteraf gekozen, dus ook te rooskleurig).
- Snelle partijen zitten er in milliseconden bovenop. Wat wij na seconden nog zien, is het restje. Ga je zelf pakken, dan concurreer je met hen en met iedereen die het restje ook ziet; bij elke poging kan een stap net weg zijn (dan zit je met een munt die je niet wilde, en verlies).
- Drie orders na elkaar kosten tijd; tussen stap 1 en 3 kan de prijs bewegen.
- De EU-versie van de beurs kan minder paren hebben dan de wereldwijde API die we meten.

Waarom het te somber kan zijn: lagere kosten (meer handelsvolume, eigen beurs-token, maker in plaats van taker, de 0%-paren van OKX die we niet konden ophalen, Bitstamp gratis onder $1.000 volume per 30 dagen) en sneller meten dan elke paar seconden laten meer zien.

Bron van alle aantallen en bedragen: eigen metingen (GEZIEN), data op de tak `ai-handel-data`, map `driehoek/`. Kosten per stap en hun bron: README.md.
