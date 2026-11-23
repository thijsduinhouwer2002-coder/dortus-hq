# Driehoek-meter: rapport

## Kort antwoord

Op de beurzen met vergunning (MiCA, ook via een EU-dochter): 120 echte kansen die met €100 konden (121 als je elke driehoek los telt; 34,2 per dag). Samen €46,42 tot €46,62 per dag met €100 en €82,44 tot €82,84 per dag met €200 (GOK; het lage getal voegt driehoeken samen die hetzelfde stukje boek willen, het hoge telt ze los; allebei alsof je ze allemaal als eerste pakt, met het geld al op de juiste beurs). Op de grijze beurzen (geen vergunning): 46 echte kansen die met €100 konden (56 als je elke driehoek los telt; 13,1 per dag). Samen €2,60 tot €3,35 per dag met €100 en €3,50 tot €4,37 per dag met €200 (GOK; het lage getal voegt driehoeken samen die hetzelfde stukje boek willen, het hoge telt ze los; allebei alsof je ze allemaal als eerste pakt, met het geld al op de juiste beurs).

Uitleg: **takerkosten** zijn wat de beurs per order rekent als je meteen koopt of verkoopt tegen de prijs die er ligt (0% tot 0,8% per order; een driehoek is drie orders). **Diepte** is hoeveel euro je tegen die winstgevende prijzen echt kunt kopen en verkopen voordat de prijs slechter wordt. Wij meten elke 3 tot 5 seconden; snelle bots pakken zulke kansen meestal binnen milliseconden, dus wat hier staat is wat er na hen overbleef.

Data: 1305 driehoeken met winst op het boek gezien (ook kleine en korte), 5 dag(en) (2026-11-19 tot 2026-11-23). Gemeten: ±84,2 uur per beurs (GEZIEN, uit stand.jsonl).

Een **echte driehoek**: winst na drie keer takerkosten op het orderboek, op twee metingen die minstens 3 seconden uit elkaar liggen elk minstens €100 diepte, bij de latere meting minstens €0,05 winst, en niet meer dan 5% winst (verdacht). Alle bedragen zijn die van de latere meting: wat er na 3 seconden nog stond. Driehoeken op dezelfde beurs die binnen 5 seconden van elkaar bevestigd werden en een paar delen dat geen paar van twee hoofdmunten is (EUR, USD, USDT, USDC, BTC, ETH), tellen als **één kans** (de beste telt): ze willen hetzelfde stukje orderboek. Er wordt niet doorgeketend: een driehoek hoort alleen bij een kans als hij met elk lid ervan dat stukje deelt. Omdat samenvoegen ook te streng kan zijn, staan aantallen en geld er ook los geteld bij (bovengrens).

Regels van vóór 2026-11-19 16:07 UTC (vóór de keuring) hebben geen meting na 3 seconden en tellen daarom nooit als echt. Daar zat ook niets in dat 3 seconden met €100 diepte stond.

## Per beurs: hoe gemeten en hoe dicht bij winst

Beste marge = per ronde de beste driehoek tegen de beste prijzen na kosten (mediaan en hoogste over alle rondes). Negatief = zelfs de beste driehoek verloor geld. Kandidaten = driehoeken die met de beste prijzen winst gaven; daarvan haalt hij de orderboeken op (bekeken), tenzij het budget van die ronde op was (overgeslagen) of de koersen sinds de vorige controle niet veranderden (zelfde). Een positieve beste marge is nog geen winst: de bulk-koers kan achterlopen of er ligt maar een paar cent op die prijs; het orderboek beslist (kolom Winst op boek).

| Beurs | Status | Paren | Driehoeken | Uur | Rondes | Fouten (te veel) | Beste marge mediaan | Beste marge hoogst | Kandidaten | Bekeken | Overgeslagen | Zelfde | Winst op boek | Echt |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| bitget | grijs | 3658 | 202 | 84,2 | 100734 | 1 (0) | -0,274% | 1,502% | 8742 | 7502 | 124 | 1116 | 1 | 0 |
| bitstamp | MiCA | 252 | 346 | 84,2 | 60438 | 2 (0) | -0,223% | 4,996% | 60848 | 60043 | 324 | 467 | 59249 | 89 |
| bitvavo | MiCA | 435 | 22 | 84,2 | 75582 | 1 (0) | -0,757% | -0,309% | 472 | 280 | 0 | 192 | 9 | 0 |
| gate | MiCA-dochter | 2156 | 372 | 84,2 | 74994 | 3 (0) | -0,158% | 4,075% | 34510 | 14283 | 860 | 19366 | 4 | 0 |
| kraken | MiCA | 1353 | 2352 | 84,2 | 60470 | 1 (0) | -0,200% | 4,907% | 15931 | 9347 | 3025 | 3559 | 3 | 0 |
| kucoin | MiCA-dochter | 968 | 452 | 84,2 | 100801 | 1 (0) | -0,141% | 4,979% | 51313 | 24897 | 256 | 26158 | 8 | 0 |
| mexc | grijs | 1635 | 868 | 84,2 | 100599 | 3 (0) | 0,292% | 4,975% | 270577 | 153582 | 2450 | 112871 | 5419 | 56 |
| okx | MiCA-dochter | 1250 | 2338 | 84,2 | 100790 | 0 (0) | -0,093% | 4,743% | 87856 | 75877 | 1281 | 10695 | 7803 | 32 |

## Trechter

| Stap | Alle beurzen | MiCA (ook via EU-dochter) | Grijs |
|---|---|---|---|
| winst op het boek, met de lage kosten (bovengrens) | 1305 | 599 | 706 |
| winst op het boek, met de gewone kosten | 1296 | 590 | 706 |
| en ooit minstens €100 diepte | 321 | 187 | 134 |
| en na 3 s nog steeds minstens €100 diepte | 208 | 146 | 62 |
| en dan minstens €0,05 winst | 191 | 135 | 56 |
| en niet verdacht = **echt** | 177 | 121 | 56 |
| echte **kansen** (samengevoegd als ze hetzelfde stukje boek willen; ondergrens) | 166 | 120 | 46 |

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
| 2026-11-23 | Alle beurzen | 2 | 2 | €0,52 | €336 | 4,0 s | €1,04 |
| 2026-11-23 | MiCA (ook via EU-dochter) | 0 | 0 | - | - | - | €0,00 |
| 2026-11-23 | Grijs | 2 | 2 | €0,52 | €336 | 4,0 s | €1,04 |
| totaal | Alle beurzen | 177 | 166 | €0,64 | €227 | 19,0 s | €530,93 |
| totaal | MiCA (ook via EU-dochter) | 121 | 120 | €1,20 | €227 | 41,0 s | €465,17 |
| totaal | Grijs | 56 | 46 | €0,38 | €214 | 6,0 s | €65,76 |

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
| USDT>BTC>BRL>USDT | 5 | €0,52 | €0,64 | €146 | 6,0 s | 0,05% + 0,05% + 0,08% |
| USDT>SOL>BTC>USDT | 5 | €0,16 | €1,04 | €146 | 17,0 s | 0,05% + 0,05% + 0,05% |
| USDT>BTC>USDC>USDT | 4 | €3,12 | €20,12 | €14.861 | 5,0 s | 0,05% + 0,00% + 0,00% |
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
| bitstamp | MiCA | 346 | 260 | €12 | 325 | 325 | 325 | 247 |
| bitvavo | MiCA | 22 | 22 | ≤ €10 | 22 | 22 | 22 | 22 |
| gate | MiCA-dochter | 372 | 0 | ≤ €10 | 372 | 372 | 372 | 0 |
| kraken | MiCA | 2352 | 1368 | ≤ €10 | 2352 | 2352 | 2352 | 1368 |
| kucoin | MiCA-dochter | 452 | 12 | ≤ €10 | 452 | 452 | 452 | 12 |
| mexc | grijs | 868 | 76 | ≤ €10 | 868 | 868 | 868 | 76 |
| okx | MiCA-dochter | 2338 | 1090 | ≤ €10 | 2334 | 2334 | 2334 | 1090 |

Van de 166 echte kansen konden er 166 met €100 (minimale ordergrootte gehaald op alle drie de orders, winst na 3 seconden).

## Opschaling naar €100, €150, €200, €2.000 en €5.000 inleg (GOK)

Per echte kans nemen we de winst die je bij die inleg na 3 seconden nog had kunnen maken (minder inleggen mag als het boek dunner is; alleen bedragen die de minimale ordergrootte halen). Opgeteld per gemeten dag en dan maal 30 voor een maand.

Elk getal staat er twee keer: **samengevoegd** (ondergrens: driehoeken die op hetzelfde moment, binnen 5 seconden na hun bevestiging, hetzelfde niet-hoofdpaar gebruiken, tellen als één kans; een paar van twee hoofdmunten zoals BTC/EUR of BTCUSDT telt daarbij niet, en er wordt niet doorgeketend) en **los** (bovengrens: elke driehoek apart).

| Soort | Inleg | Kansen per dag (samengevoegd / los) | Winst per dag (samengevoegd / los) | Per maand (GOK, samengevoegd / los) | Alleen de beste beurs, per maand (GOK, samengevoegd) |
|---|---|---|---|---|---|
| Alle beurzen | €100 | 47,3 / 50,4 | €49,01 / €49,97 | €1.470,42 / €1.499,06 | bitstamp: €1.310,64 |
| Alle beurzen | €150 | 47,3 / 50,4 | €68,69 / €69,85 | €2.060,70 / €2.095,38 | bitstamp: €1.843,26 |
| Alle beurzen | €200 | 47,3 / 50,4 | €85,95 / €87,21 | €2.578,38 / €2.616,32 | bitstamp: €2.317,14 |
| Alle beurzen | €2.000 | 47,3 / 50,4 | €117,18 / €121,46 | €3.515,52 / €3.643,75 | bitstamp: €2.571,91 |
| Alle beurzen | €5.000 | 47,3 / 50,4 | €131,26 / €139,22 | €3.937,68 / €4.176,65 | bitstamp: €2.571,91 |
| MiCA (ook via EU-dochter) | €100 | 34,2 / 34,5 | €46,42 / €46,62 | €1.392,49 / €1.398,51 | bitstamp: €1.310,64 |
| MiCA (ook via EU-dochter) | €150 | 34,2 / 34,5 | €65,50 / €65,80 | €1.964,91 / €1.973,95 | bitstamp: €1.843,26 |
| MiCA (ook via EU-dochter) | €200 | 34,2 / 34,5 | €82,44 / €82,84 | €2.473,24 / €2.485,30 | bitstamp: €2.317,14 |
| MiCA (ook via EU-dochter) | €2.000 | 34,2 / 34,5 | €109,68 / €112,82 | €3.290,29 / €3.384,69 | bitstamp: €2.571,91 |
| MiCA (ook via EU-dochter) | €5.000 | 34,2 / 34,5 | €119,97 / €126,59 | €3.599,04 / €3.797,55 | bitstamp: €2.571,91 |
| Grijs | €100 | 13,1 / 16,0 | €2,60 / €3,35 | €77,93 / €100,55 | mexc: €77,93 |
| Grijs | €150 | 13,1 / 16,0 | €3,19 / €4,05 | €95,79 / €121,42 | mexc: €95,79 |
| Grijs | €200 | 13,1 / 16,0 | €3,50 / €4,37 | €105,14 / €131,02 | mexc: €105,14 |
| Grijs | €2.000 | 13,1 / 16,0 | €7,51 / €8,64 | €225,23 / €259,06 | mexc: €225,23 |
| Grijs | €5.000 | 13,1 / 16,0 | €11,29 / €12,64 | €338,64 / €379,10 | mexc: €338,64 |

Waarom dit te rooskleurig is (GOK):

- Het is een **bovengrens**: je pakt elke kans, op elke beurs tegelijk, met het geld al op die beurs. Met weinig geld staat alles op één beurs; de laatste kolom neemt alleen de beste beurs (achteraf gekozen, dus ook te rooskleurig).
- Snelle partijen zitten er in milliseconden bovenop. Wat wij na seconden nog zien, is het restje. Ga je zelf pakken, dan concurreer je met hen en met iedereen die het restje ook ziet; bij elke poging kan een stap net weg zijn (dan zit je met een munt die je niet wilde, en verlies).
- Drie orders na elkaar kosten tijd; tussen stap 1 en 3 kan de prijs bewegen.
- De EU-versie van de beurs kan minder paren hebben dan de wereldwijde API die we meten.

Waarom het te somber kan zijn: lagere kosten (meer handelsvolume, eigen beurs-token, maker in plaats van taker, de 0%-paren van OKX die we niet konden ophalen, Bitstamp gratis onder $1.000 volume per 30 dagen) en sneller meten dan elke paar seconden laten meer zien.

Bron van alle aantallen en bedragen: eigen metingen (GEZIEN), data op de tak `ai-handel-data`, map `driehoek/`. Kosten per stap en hun bron: README.md.
