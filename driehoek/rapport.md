# Driehoek-meter: rapport

## Kort antwoord

Op de beurzen met vergunning (MiCA, ook via een EU-dochter): 121 echte kansen die met €100 konden (123 als je elke driehoek los telt; 29,0 per dag). Samen €39,14 tot €39,33 per dag met €100 en €69,49 tot €69,86 per dag met €200 (GOK; het lage getal voegt driehoeken samen die hetzelfde stukje boek willen, het hoge telt ze los; allebei alsof je ze allemaal als eerste pakt, met het geld al op de juiste beurs). Op de grijze beurzen (geen vergunning): 51 echte kansen die met €100 konden (61 als je elke driehoek los telt; 12,2 per dag). Samen €2,32 tot €2,96 per dag met €100 en €3,16 tot €3,89 per dag met €200 (GOK; het lage getal voegt driehoeken samen die hetzelfde stukje boek willen, het hoge telt ze los; allebei alsof je ze allemaal als eerste pakt, met het geld al op de juiste beurs).

Uitleg: **takerkosten** zijn wat de beurs per order rekent als je meteen koopt of verkoopt tegen de prijs die er ligt (0% tot 0,8% per order; een driehoek is drie orders). **Diepte** is hoeveel euro je tegen die winstgevende prijzen echt kunt kopen en verkopen voordat de prijs slechter wordt. Wij meten elke 3 tot 5 seconden; snelle bots pakken zulke kansen meestal binnen milliseconden, dus wat hier staat is wat er na hen overbleef.

Data: 1678 driehoeken met winst op het boek gezien (ook kleine en korte), 5 dag(en) (2026-11-19 tot 2026-11-23). Gemeten: ±100,0 uur per beurs (GEZIEN, uit stand.jsonl).

Een **echte driehoek**: winst na drie keer takerkosten op het orderboek, op twee metingen die minstens 3 seconden uit elkaar liggen elk minstens €100 diepte, bij de latere meting minstens €0,05 winst, en niet meer dan 5% winst (verdacht). Alle bedragen zijn die van de latere meting: wat er na 3 seconden nog stond. Driehoeken op dezelfde beurs die binnen 5 seconden van elkaar bevestigd werden en een paar delen dat geen paar van twee hoofdmunten is (EUR, USD, USDT, USDC, BTC, ETH), tellen als **één kans** (de beste telt): ze willen hetzelfde stukje orderboek. Er wordt niet doorgeketend: een driehoek hoort alleen bij een kans als hij met elk lid ervan dat stukje deelt. Omdat samenvoegen ook te streng kan zijn, staan aantallen en geld er ook los geteld bij (bovengrens).

Regels van vóór 2026-11-19 16:07 UTC (vóór de keuring) hebben geen meting na 3 seconden en tellen daarom nooit als echt. Daar zat ook niets in dat 3 seconden met €100 diepte stond.

## Per beurs: hoe gemeten en hoe dicht bij winst

Beste marge = per ronde de beste driehoek tegen de beste prijzen na kosten (mediaan en hoogste over alle rondes). Negatief = zelfs de beste driehoek verloor geld. Kandidaten = driehoeken die met de beste prijzen winst gaven; daarvan haalt hij de orderboeken op (bekeken), tenzij het budget van die ronde op was (overgeslagen) of de koersen sinds de vorige controle niet veranderden (zelfde). Een positieve beste marge is nog geen winst: de bulk-koers kan achterlopen of er ligt maar een paar cent op die prijs; het orderboek beslist (kolom Winst op boek).

| Beurs | Status | Paren | Driehoeken | Uur | Rondes | Fouten (te veel) | Beste marge mediaan | Beste marge hoogst | Kandidaten | Bekeken | Overgeslagen | Zelfde | Winst op boek | Echt |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| bitget | grijs | 3659 | 202 | 100,0 | 119617 | 1 (0) | -0,274% | 1,738% | 10740 | 9336 | 124 | 1280 | 1 | 0 |
| bitstamp | MiCA | 252 | 346 | 100,0 | 71772 | 3 (0) | -0,224% | 4,996% | 72013 | 71208 | 324 | 467 | 70392 | 89 |
| bitvavo | MiCA | 434 | 22 | 100,0 | 89747 | 1 (0) | -0,758% | -0,309% | 483 | 283 | 0 | 200 | 9 | 0 |
| gate | MiCA-dochter | 2157 | 372 | 100,0 | 89046 | 3 (0) | -0,161% | 4,641% | 38867 | 16184 | 947 | 21735 | 4 | 0 |
| kraken | MiCA | 1353 | 2352 | 100,0 | 71803 | 1 (0) | -0,200% | 4,907% | 16847 | 9949 | 3268 | 3630 | 3 | 0 |
| kucoin | MiCA-dochter | 969 | 452 | 100,0 | 119694 | 1 (0) | -0,152% | 4,979% | 53925 | 26729 | 261 | 26933 | 8 | 0 |
| mexc | grijs | 1634 | 868 | 100,0 | 119370 | 7 (0) | 0,285% | 4,999% | 325089 | 187249 | 3139 | 131546 | 5607 | 61 |
| okx | MiCA-dochter | 1250 | 2338 | 100,0 | 119667 | 1 (0) | -0,085% | 4,999% | 144718 | 118358 | 7757 | 18592 | 35722 | 34 |

## Trechter

| Stap | Alle beurzen | MiCA (ook via EU-dochter) | Grijs |
|---|---|---|---|
| winst op het boek, met de lage kosten (bovengrens) | 1678 | 871 | 807 |
| winst op het boek, met de gewone kosten | 1669 | 862 | 807 |
| en ooit minstens €100 diepte | 351 | 192 | 159 |
| en na 3 s nog steeds minstens €100 diepte | 220 | 151 | 69 |
| en dan minstens €0,05 winst | 201 | 140 | 61 |
| en niet verdacht = **echt** | 184 | 123 | 61 |
| echte **kansen** (samengevoegd als ze hetzelfde stukje boek willen; ondergrens) | 172 | 121 | 51 |

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
| totaal | Alle beurzen | 184 | 172 | €0,64 | €227 | 18,0 s | €534,83 |
| totaal | MiCA (ook via EU-dochter) | 123 | 121 | €1,18 | €227 | 42,0 s | €465,32 |
| totaal | Grijs | 61 | 51 | €0,38 | €227 | 6,0 s | €69,52 |

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
| USDT>USDF>ETH>USDT | 5 | €0,81 | €2,09 | €555 | 4,0 s | 0,05% + 0,05% + 0,05% |
| USDT>USDF>BTC>USDT | 5 | €0,45 | €1,08 | €444 | 6,0 s | 0,05% + 0,05% + 0,05% |
| USDT>BTC>BRL>USDT | 5 | €0,52 | €0,64 | €146 | 6,0 s | 0,05% + 0,05% + 0,08% |
| USDT>SOL>BTC>USDT | 5 | €0,16 | €1,04 | €146 | 17,0 s | 0,05% + 0,05% + 0,05% |
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
| bitstamp | MiCA | 346 | 260 | €12 | 333 | 334 | 334 | 249 |
| bitvavo | MiCA | 22 | 22 | ≤ €10 | 22 | 22 | 22 | 22 |
| gate | MiCA-dochter | 372 | 0 | ≤ €10 | 372 | 372 | 372 | 0 |
| kraken | MiCA | 2352 | 1368 | ≤ €10 | 2352 | 2352 | 2352 | 1368 |
| kucoin | MiCA-dochter | 452 | 12 | ≤ €10 | 452 | 452 | 452 | 12 |
| mexc | grijs | 868 | 76 | ≤ €10 | 868 | 868 | 868 | 76 |
| okx | MiCA-dochter | 2338 | 1090 | ≤ €10 | 2328 | 2328 | 2328 | 1090 |

Van de 172 echte kansen konden er 172 met €100 (minimale ordergrootte gehaald op alle drie de orders, winst na 3 seconden).

## Opschaling naar €100, €150, €200, €2.000 en €5.000 inleg (GOK)

Per echte kans nemen we de winst die je bij die inleg na 3 seconden nog had kunnen maken (minder inleggen mag als het boek dunner is; alleen bedragen die de minimale ordergrootte halen). Opgeteld per gemeten dag en dan maal 30 voor een maand.

Elk getal staat er twee keer: **samengevoegd** (ondergrens: driehoeken die op hetzelfde moment, binnen 5 seconden na hun bevestiging, hetzelfde niet-hoofdpaar gebruiken, tellen als één kans; een paar van twee hoofdmunten zoals BTC/EUR of BTCUSDT telt daarbij niet, en er wordt niet doorgeketend) en **los** (bovengrens: elke driehoek apart).

| Soort | Inleg | Kansen per dag (samengevoegd / los) | Winst per dag (samengevoegd / los) | Per maand (GOK, samengevoegd / los) | Alleen de beste beurs, per maand (GOK, samengevoegd) |
|---|---|---|---|---|---|
| Alle beurzen | €100 | 41,3 / 44,2 | €41,46 / €42,29 | €1.243,81 / €1.268,77 | bitstamp: €1.104,21 |
| Alle beurzen | €150 | 41,3 / 44,2 | €58,08 / €59,09 | €1.742,42 / €1.772,58 | bitstamp: €1.552,94 |
| Alle beurzen | €200 | 41,3 / 44,2 | €72,65 / €73,75 | €2.179,51 / €2.212,42 | bitstamp: €1.952,19 |
| Alle beurzen | €2.000 | 41,3 / 44,2 | €99,21 / €102,84 | €2.976,25 / €3.085,22 | bitstamp: €2.166,83 |
| Alle beurzen | €5.000 | 41,3 / 44,2 | €111,19 / €117,93 | €3.335,78 / €3.538,05 | bitstamp: €2.166,83 |
| MiCA (ook via EU-dochter) | €100 | 29,0 / 29,5 | €39,14 / €39,33 | €1.174,06 / €1.179,97 | bitstamp: €1.104,21 |
| MiCA (ook via EU-dochter) | €150 | 29,0 / 29,5 | €55,22 / €55,50 | €1.656,48 / €1.665,04 | bitstamp: €1.552,94 |
| MiCA (ook via EU-dochter) | €200 | 29,0 / 29,5 | €69,49 / €69,86 | €2.084,75 / €2.095,85 | bitstamp: €1.952,19 |
| MiCA (ook via EU-dochter) | €2.000 | 29,0 / 29,5 | €92,44 / €95,12 | €2.773,12 / €2.853,59 | bitstamp: €2.166,83 |
| MiCA (ook via EU-dochter) | €5.000 | 29,0 / 29,5 | €101,11 / €106,71 | €3.033,23 / €3.201,42 | bitstamp: €2.166,83 |
| Grijs | €100 | 12,2 / 14,6 | €2,32 / €2,96 | €69,74 / €88,80 | mexc: €69,74 |
| Grijs | €150 | 12,2 / 14,6 | €2,86 / €3,58 | €85,94 / €107,54 | mexc: €85,94 |
| Grijs | €200 | 12,2 / 14,6 | €3,16 / €3,89 | €94,76 / €116,57 | mexc: €94,76 |
| Grijs | €2.000 | 12,2 / 14,6 | €6,77 / €7,72 | €203,13 / €231,63 | mexc: €203,13 |
| Grijs | €5.000 | 12,2 / 14,6 | €10,08 / €11,22 | €302,54 / €336,63 | mexc: €302,54 |

Waarom dit te rooskleurig is (GOK):

- Het is een **bovengrens**: je pakt elke kans, op elke beurs tegelijk, met het geld al op die beurs. Met weinig geld staat alles op één beurs; de laatste kolom neemt alleen de beste beurs (achteraf gekozen, dus ook te rooskleurig).
- Snelle partijen zitten er in milliseconden bovenop. Wat wij na seconden nog zien, is het restje. Ga je zelf pakken, dan concurreer je met hen en met iedereen die het restje ook ziet; bij elke poging kan een stap net weg zijn (dan zit je met een munt die je niet wilde, en verlies).
- Drie orders na elkaar kosten tijd; tussen stap 1 en 3 kan de prijs bewegen.
- De EU-versie van de beurs kan minder paren hebben dan de wereldwijde API die we meten.

Waarom het te somber kan zijn: lagere kosten (meer handelsvolume, eigen beurs-token, maker in plaats van taker, de 0%-paren van OKX die we niet konden ophalen, Bitstamp gratis onder $1.000 volume per 30 dagen) en sneller meten dan elke paar seconden laten meer zien.

Bron van alle aantallen en bedragen: eigen metingen (GEZIEN), data op de tak `ai-handel-data`, map `driehoek/`. Kosten per stap en hun bron: README.md.
