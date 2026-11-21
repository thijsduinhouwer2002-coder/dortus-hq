# Driehoek-meter: rapport

## Kort antwoord

Op de beurzen met vergunning (MiCA, ook via een EU-dochter): 106 echte kansen die met €100 konden (107 als je elke driehoek los telt; 62,6 per dag). Samen €94,04 tot €94,45 per dag met €100 en €167,00 tot €167,83 per dag met €200 (GOK; het lage getal voegt driehoeken samen die hetzelfde stukje boek willen, het hoge telt ze los; allebei alsof je ze allemaal als eerste pakt, met het geld al op de juiste beurs). Op de grijze beurzen (geen vergunning): 29 echte kansen die met €100 konden (37 als je elke driehoek los telt; 17,1 per dag). Samen €2,90 tot €4,28 per dag met €100 en €3,92 tot €5,51 per dag met €200 (GOK; het lage getal voegt driehoeken samen die hetzelfde stukje boek willen, het hoge telt ze los; allebei alsof je ze allemaal als eerste pakt, met het geld al op de juiste beurs).

Uitleg: **takerkosten** zijn wat de beurs per order rekent als je meteen koopt of verkoopt tegen de prijs die er ligt (0% tot 0,8% per order; een driehoek is drie orders). **Diepte** is hoeveel euro je tegen die winstgevende prijzen echt kunt kopen en verkopen voordat de prijs slechter wordt. Wij meten elke 3 tot 5 seconden; snelle bots pakken zulke kansen meestal binnen milliseconden, dus wat hier staat is wat er na hen overbleef.

Data: 748 driehoeken met winst op het boek gezien (ook kleine en korte), 3 dag(en) (2026-11-19 tot 2026-11-21). Gemeten: ±40,7 uur per beurs (GEZIEN, uit stand.jsonl).

Een **echte driehoek**: winst na drie keer takerkosten op het orderboek, op twee metingen die minstens 3 seconden uit elkaar liggen elk minstens €100 diepte, bij de latere meting minstens €0,05 winst, en niet meer dan 5% winst (verdacht). Alle bedragen zijn die van de latere meting: wat er na 3 seconden nog stond. Driehoeken op dezelfde beurs die binnen 5 seconden van elkaar bevestigd werden en een paar delen dat geen paar van twee hoofdmunten is (EUR, USD, USDT, USDC, BTC, ETH), tellen als **één kans** (de beste telt): ze willen hetzelfde stukje orderboek. Er wordt niet doorgeketend: een driehoek hoort alleen bij een kans als hij met elk lid ervan dat stukje deelt. Omdat samenvoegen ook te streng kan zijn, staan aantallen en geld er ook los geteld bij (bovengrens).

Regels van vóór 2026-11-19 16:07 UTC (vóór de keuring) hebben geen meting na 3 seconden en tellen daarom nooit als echt. Daar zat ook niets in dat 3 seconden met €100 diepte stond.

## Per beurs: hoe gemeten en hoe dicht bij winst

Beste marge = per ronde de beste driehoek tegen de beste prijzen na kosten (mediaan en hoogste over alle rondes). Negatief = zelfs de beste driehoek verloor geld. Kandidaten = driehoeken die met de beste prijzen winst gaven; daarvan haalt hij de orderboeken op (bekeken), tenzij het budget van die ronde op was (overgeslagen) of de koersen sinds de vorige controle niet veranderden (zelfde). Een positieve beste marge is nog geen winst: de bulk-koers kan achterlopen of er ligt maar een paar cent op die prijs; het orderboek beslist (kolom Winst op boek).

| Beurs | Status | Paren | Driehoeken | Uur | Rondes | Fouten (te veel) | Beste marge mediaan | Beste marge hoogst | Kandidaten | Bekeken | Overgeslagen | Zelfde | Winst op boek | Echt |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| bitget | grijs | 3658 | 202 | 40,7 | 48490 | 1 (0) | -0,273% | 1,502% | 5339 | 4520 | 121 | 698 | 1 | 0 |
| bitstamp | MiCA | 252 | 346 | 40,7 | 29098 | 0 (0) | -0,224% | 4,996% | 28771 | 28395 | 248 | 123 | 27733 | 84 |
| bitvavo | MiCA | 435 | 22 | 40,7 | 36383 | 1 (0) | -0,757% | -0,318% | 164 | 153 | 0 | 11 | 5 | 0 |
| gate | MiCA-dochter | 2158 | 372 | 40,7 | 35988 | 1 (0) | -0,133% | 4,075% | 24370 | 10438 | 782 | 13149 | 3 | 0 |
| kraken | MiCA | 1353 | 2352 | 40,7 | 29116 | 0 (0) | -0,201% | 4,907% | 10285 | 6201 | 1465 | 2619 | 3 | 0 |
| kucoin | MiCA-dochter | 968 | 452 | 40,7 | 48533 | 1 (0) | 0,189% | 4,979% | 44671 | 21670 | 249 | 22750 | 5 | 0 |
| mexc | grijs | 1664 | 886 | 40,7 | 48470 | 0 (0) | 0,259% | 4,975% | 123879 | 69157 | 1450 | 52685 | 3300 | 37 |
| okx | MiCA-dochter | 1250 | 2338 | 40,7 | 48528 | 0 (0) | -0,111% | 4,743% | 41323 | 36168 | 907 | 4248 | 4097 | 23 |

## Trechter

| Stap | Alle beurzen | MiCA (ook via EU-dochter) | Grijs |
|---|---|---|---|
| winst op het boek, met de lage kosten (bovengrens) | 748 | 344 | 404 |
| winst op het boek, met de gewone kosten | 743 | 339 | 404 |
| en ooit minstens €100 diepte | 245 | 161 | 84 |
| en na 3 s nog steeds minstens €100 diepte | 167 | 127 | 40 |
| en dan minstens €0,05 winst | 158 | 121 | 37 |
| en niet verdacht = **echt** | 144 | 107 | 37 |
| echte **kansen** (samengevoegd als ze hetzelfde stukje boek willen; ondergrens) | 135 | 106 | 29 |

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
| 2026-11-21 | Alle beurzen | 48 | 45 | €1,34 | €284 | 15,0 s | €203,43 |
| 2026-11-21 | MiCA (ook via EU-dochter) | 34 | 33 | €2,68 | €355 | 24,0 s | €177,76 |
| 2026-11-21 | Grijs | 14 | 12 | €0,40 | €166 | 6,0 s | €25,66 |
| totaal | Alle beurzen | 144 | 135 | €0,69 | €227 | 24,0 s | €501,33 |
| totaal | MiCA (ook via EU-dochter) | 107 | 106 | €1,55 | €227 | 45,0 s | €445,09 |
| totaal | Grijs | 37 | 29 | €0,38 | €200 | 6,0 s | €56,24 |

## Beste driehoeken per beurs (echt, bedragen na 3 seconden)

**bitstamp** (MiCA)

| Driehoek | Keren | Mediane winst | Hoogste winst | Mediane diepte | Mediane duur met €100 diepte | Kosten per stap |
|---|---|---|---|---|---|---|
| EUR>IMX>USD>EUR | 48 | €0,39 | €5,07 | €116 | 65,0 s | 0,40% + 0,40% + 0,08% |
| EUR>USD>SKY>EUR | 31 | €8,22 | €11,32 | €227 | 25,0 s | 0,08% + 0,40% + 0,40% |
| EUR>SAND>USD>EUR | 2 | €1,80 | €3,00 | €227 | 748,0 s | 0,40% + 0,40% + 0,08% |
| EUR>USD>HBAR>EUR | 2 | €0,18 | €0,21 | €355 | 490,0 s | 0,08% + 0,40% + 0,40% |
| EUR>MOODENG>USD>EUR | 1 | €0,13 | €0,13 | €150 | 45,0 s | 0,40% + 0,40% + 0,08% |

**mexc** (grijs)

| Driehoek | Keren | Mediane winst | Hoogste winst | Mediane diepte | Mediane duur met €100 diepte | Kosten per stap |
|---|---|---|---|---|---|---|
| USDT>BTC>USDC>USDT | 4 | €3,12 | €20,12 | €14.861 | 5,0 s | 0,05% + 0,00% + 0,00% |
| USDT>BTC>BRL>USDT | 4 | €0,58 | €0,64 | €146 | 6,0 s | 0,05% + 0,05% + 0,08% |
| USDT>SOL>BTC>USDT | 4 | €0,14 | €0,42 | €146 | 19,0 s | 0,05% + 0,05% + 0,05% |
| USDT>ETH>BRL>USDT | 3 | €0,30 | €0,45 | €116 | 6,0 s | 0,05% + 0,05% + 0,08% |
| USDT>SOL>BRL>USDT | 3 | €0,16 | €0,31 | €116 | 9,0 s | 0,05% + 0,05% + 0,08% |

**okx** (MiCA-dochter)

| Driehoek | Keren | Mediane winst | Hoogste winst | Mediane diepte | Mediane duur met €100 diepte | Kosten per stap |
|---|---|---|---|---|---|---|
| USDT>SOL>AUD>USDT | 5 | €2,63 | €4,03 | €2.000 | 15,0 s | 0,10% + 0,10% + 0,10% |
| USDT>BTC>AUD>USDT | 4 | €7,67 | €20,31 | €4.154 | 100,0 s | 0,10% + 0,10% + 0,10% |
| USDT>XANT>USDC>USDT | 3 | €0,80 | €1,98 | €355 | 216,0 s | 0,10% + 0,10% + 0,10% |
| USDT>XRP>AUD>USDT | 3 | €0,29 | €1,68 | €555 | 18,0 s | 0,10% + 0,10% + 0,10% |
| USDT>BTC>AED>USDT | 1 | €72,14 | €72,14 | €15.777 | 9,0 s | 0,10% + 0,10% + 0,10% |

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
| bitstamp | MiCA | 346 | 260 | €12 | 325 | 325 | 325 | 247 |
| bitvavo | MiCA | 22 | 22 | ≤ €10 | 22 | 22 | 22 | 22 |
| gate | MiCA-dochter | 372 | 0 | ≤ €10 | 372 | 372 | 372 | 0 |
| kraken | MiCA | 2352 | 1368 | ≤ €10 | 2352 | 2352 | 2352 | 1368 |
| kucoin | MiCA-dochter | 452 | 12 | ≤ €10 | 452 | 452 | 452 | 12 |
| mexc | grijs | 886 | 76 | ≤ €10 | 886 | 886 | 886 | 76 |
| okx | MiCA-dochter | 2338 | 1090 | ≤ €10 | 2322 | 2322 | 2322 | 1082 |

Van de 135 echte kansen konden er 135 met €100 (minimale ordergrootte gehaald op alle drie de orders, winst na 3 seconden).

## Opschaling naar €100, €150, €200, €2.000 en €5.000 inleg (GOK)

Per echte kans nemen we de winst die je bij die inleg na 3 seconden nog had kunnen maken (minder inleggen mag als het boek dunner is; alleen bedragen die de minimale ordergrootte halen). Opgeteld per gemeten dag en dan maal 30 voor een maand.

Elk getal staat er twee keer: **samengevoegd** (ondergrens: driehoeken die op hetzelfde moment, binnen 5 seconden na hun bevestiging, hetzelfde niet-hoofdpaar gebruiken, tellen als één kans; een paar van twee hoofdmunten zoals BTC/EUR of BTCUSDT telt daarbij niet, en er wordt niet doorgeketend) en **los** (bovengrens: elke driehoek apart).

| Soort | Inleg | Kansen per dag (samengevoegd / los) | Winst per dag (samengevoegd / los) | Per maand (GOK, samengevoegd / los) | Alleen de beste beurs, per maand (GOK, samengevoegd) |
|---|---|---|---|---|---|
| Alle beurzen | €100 | 79,7 / 85,0 | €96,94 / €98,73 | €2.908,14 / €2.961,88 | bitstamp: €2.710,89 |
| Alle beurzen | €150 | 79,7 / 85,0 | €136,19 / €138,39 | €4.085,84 / €4.151,74 | bitstamp: €3.812,22 |
| Alle beurzen | €200 | 79,7 / 85,0 | €170,92 / €173,34 | €5.127,57 / €5.200,22 | bitstamp: €4.791,85 |
| Alle beurzen | €2.000 | 79,7 / 85,0 | €226,49 / €235,15 | €6.794,70 / €7.054,40 | bitstamp: €5.319,66 |
| Alle beurzen | €5.000 | 79,7 / 85,0 | €254,46 / €270,76 | €7.633,66 / €8.122,78 | bitstamp: €5.319,66 |
| MiCA (ook via EU-dochter) | €100 | 62,6 / 63,1 | €94,04 / €94,45 | €2.821,06 / €2.833,55 | bitstamp: €2.710,89 |
| MiCA (ook via EU-dochter) | €150 | 62,6 / 63,1 | €132,56 / €133,19 | €3.976,83 / €3.995,57 | bitstamp: €3.812,22 |
| MiCA (ook via EU-dochter) | €200 | 62,6 / 63,1 | €167,00 / €167,83 | €5.010,07 / €5.035,04 | bitstamp: €4.791,85 |
| MiCA (ook via EU-dochter) | €2.000 | 62,6 / 63,1 | €216,49 / €223,01 | €6.494,84 / €6.690,41 | bitstamp: €5.319,66 |
| MiCA (ook via EU-dochter) | €5.000 | 62,6 / 63,1 | €236,69 / €250,40 | €7.100,60 / €7.511,87 | bitstamp: €5.319,66 |
| Grijs | €100 | 17,1 / 21,8 | €2,90 / €4,28 | €87,08 / €128,33 | mexc: €87,08 |
| Grijs | €150 | 17,1 / 21,8 | €3,63 / €5,21 | €109,01 / €156,17 | mexc: €109,01 |
| Grijs | €200 | 17,1 / 21,8 | €3,92 / €5,51 | €117,51 / €165,17 | mexc: €117,51 |
| Grijs | €2.000 | 17,1 / 21,8 | €10,00 / €12,13 | €299,85 / €363,99 | mexc: €299,85 |
| Grijs | €5.000 | 17,1 / 21,8 | €17,77 / €20,36 | €533,06 / €610,92 | mexc: €533,06 |

Waarom dit te rooskleurig is (GOK):

- Het is een **bovengrens**: je pakt elke kans, op elke beurs tegelijk, met het geld al op die beurs. Met weinig geld staat alles op één beurs; de laatste kolom neemt alleen de beste beurs (achteraf gekozen, dus ook te rooskleurig).
- Snelle partijen zitten er in milliseconden bovenop. Wat wij na seconden nog zien, is het restje. Ga je zelf pakken, dan concurreer je met hen en met iedereen die het restje ook ziet; bij elke poging kan een stap net weg zijn (dan zit je met een munt die je niet wilde, en verlies).
- Drie orders na elkaar kosten tijd; tussen stap 1 en 3 kan de prijs bewegen.
- De EU-versie van de beurs kan minder paren hebben dan de wereldwijde API die we meten.

Waarom het te somber kan zijn: lagere kosten (meer handelsvolume, eigen beurs-token, maker in plaats van taker, de 0%-paren van OKX die we niet konden ophalen, Bitstamp gratis onder $1.000 volume per 30 dagen) en sneller meten dan elke paar seconden laten meer zien.

Bron van alle aantallen en bedragen: eigen metingen (GEZIEN), data op de tak `ai-handel-data`, map `driehoek/`. Kosten per stap en hun bron: README.md.
