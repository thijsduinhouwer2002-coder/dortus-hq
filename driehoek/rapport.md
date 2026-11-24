# Driehoek-meter: rapport

## Kort antwoord

Op de beurzen met vergunning (MiCA, ook via een EU-dochter): 122 echte kansen die met €100 konden (125 als je elke driehoek los telt; 27,9 per dag). Samen €37,34 tot €37,56 per dag met €100 en €66,31 tot €66,74 per dag met €200 (GOK; het lage getal voegt driehoeken samen die hetzelfde stukje boek willen, het hoge telt ze los; allebei alsof je ze allemaal als eerste pakt, met het geld al op de juiste beurs). Op de grijze beurzen (geen vergunning): 51 echte kansen die met €100 konden (61 als je elke driehoek los telt; 11,7 per dag). Samen €2,22 tot €2,82 per dag met €100 en €3,01 tot €3,70 per dag met €200 (GOK; het lage getal voegt driehoeken samen die hetzelfde stukje boek willen, het hoge telt ze los; allebei alsof je ze allemaal als eerste pakt, met het geld al op de juiste beurs).

Uitleg: **takerkosten** zijn wat de beurs per order rekent als je meteen koopt of verkoopt tegen de prijs die er ligt (0% tot 0,8% per order; een driehoek is drie orders). **Diepte** is hoeveel euro je tegen die winstgevende prijzen echt kunt kopen en verkopen voordat de prijs slechter wordt. Wij meten elke 3 tot 5 seconden; snelle bots pakken zulke kansen meestal binnen milliseconden, dus wat hier staat is wat er na hen overbleef.

Data: 1713 driehoeken met winst op het boek gezien (ook kleine en korte), 6 dag(en) (2026-11-19 tot 2026-11-24). Gemeten: ±104,9 uur per beurs (GEZIEN, uit stand.jsonl).

Een **echte driehoek**: winst na drie keer takerkosten op het orderboek, op twee metingen die minstens 3 seconden uit elkaar liggen elk minstens €100 diepte, bij de latere meting minstens €0,05 winst, en niet meer dan 5% winst (verdacht). Alle bedragen zijn die van de latere meting: wat er na 3 seconden nog stond. Driehoeken op dezelfde beurs die binnen 5 seconden van elkaar bevestigd werden en een paar delen dat geen paar van twee hoofdmunten is (EUR, USD, USDT, USDC, BTC, ETH), tellen als **één kans** (de beste telt): ze willen hetzelfde stukje orderboek. Er wordt niet doorgeketend: een driehoek hoort alleen bij een kans als hij met elk lid ervan dat stukje deelt. Omdat samenvoegen ook te streng kan zijn, staan aantallen en geld er ook los geteld bij (bovengrens).

Regels van vóór 2026-11-19 16:07 UTC (vóór de keuring) hebben geen meting na 3 seconden en tellen daarom nooit als echt. Daar zat ook niets in dat 3 seconden met €100 diepte stond.

## Per beurs: hoe gemeten en hoe dicht bij winst

Beste marge = per ronde de beste driehoek tegen de beste prijzen na kosten (mediaan en hoogste over alle rondes). Negatief = zelfs de beste driehoek verloor geld. Kandidaten = driehoeken die met de beste prijzen winst gaven; daarvan haalt hij de orderboeken op (bekeken), tenzij het budget van die ronde op was (overgeslagen) of de koersen sinds de vorige controle niet veranderden (zelfde). Een positieve beste marge is nog geen winst: de bulk-koers kan achterlopen of er ligt maar een paar cent op die prijs; het orderboek beslist (kolom Winst op boek).

| Beurs | Status | Paren | Driehoeken | Uur | Rondes | Fouten (te veel) | Beste marge mediaan | Beste marge hoogst | Kandidaten | Bekeken | Overgeslagen | Zelfde | Winst op boek | Echt |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| bitget | grijs | 3659 | 202 | 104,9 | 125513 | 1 (0) | -0,274% | 1,738% | 10769 | 9364 | 124 | 1281 | 1 | 0 |
| bitstamp | MiCA | 252 | 346 | 104,9 | 75311 | 3 (0) | -0,224% | 4,996% | 75529 | 74724 | 324 | 467 | 73903 | 89 |
| bitvavo | MiCA | 434 | 22 | 104,9 | 94169 | 1 (0) | -0,758% | -0,309% | 516 | 315 | 0 | 201 | 9 | 0 |
| gate | MiCA-dochter | 2157 | 372 | 104,9 | 93451 | 3 (0) | -0,165% | 4,641% | 39720 | 16534 | 950 | 22235 | 4 | 0 |
| kraken | MiCA | 1353 | 2352 | 104,9 | 75341 | 1 (0) | -0,200% | 4,907% | 17800 | 10393 | 3282 | 4125 | 3 | 0 |
| kucoin | MiCA-dochter | 969 | 452 | 104,9 | 125592 | 1 (0) | -0,152% | 4,979% | 54975 | 27684 | 261 | 27028 | 8 | 0 |
| mexc | grijs | 1634 | 868 | 104,9 | 125254 | 9 (0) | 0,277% | 4,999% | 334997 | 192516 | 3175 | 135833 | 5650 | 61 |
| okx | MiCA-dochter | 1250 | 2338 | 104,9 | 125559 | 1 (0) | -0,092% | 4,999% | 158494 | 131933 | 7835 | 18715 | 47518 | 36 |

## Trechter

| Stap | Alle beurzen | MiCA (ook via EU-dochter) | Grijs |
|---|---|---|---|
| winst op het boek, met de lage kosten (bovengrens) | 1713 | 890 | 823 |
| winst op het boek, met de gewone kosten | 1704 | 881 | 823 |
| en ooit minstens €100 diepte | 356 | 194 | 162 |
| en na 3 s nog steeds minstens €100 diepte | 223 | 153 | 70 |
| en dan minstens €0,05 winst | 203 | 142 | 61 |
| en niet verdacht = **echt** | 186 | 125 | 61 |
| echte **kansen** (samengevoegd als ze hetzelfde stukje boek willen; ondergrens) | 173 | 122 | 51 |

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
| 2026-11-24 | Alle beurzen | 2 | 1 | €1,91 | €1.355 | 15,0 s | €1,91 |
| 2026-11-24 | MiCA (ook via EU-dochter) | 2 | 1 | €1,91 | €1.355 | 15,0 s | €1,91 |
| 2026-11-24 | Grijs | 0 | 0 | - | - | - | €0,00 |
| totaal | Alle beurzen | 186 | 173 | €0,64 | €227 | 17,0 s | €536,74 |
| totaal | MiCA (ook via EU-dochter) | 125 | 122 | €1,20 | €227 | 41,0 s | €467,23 |
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

Van de 173 echte kansen konden er 173 met €100 (minimale ordergrootte gehaald op alle drie de orders, winst na 3 seconden).

## Opschaling naar €100, €150, €200, €2.000 en €5.000 inleg (GOK)

Per echte kans nemen we de winst die je bij die inleg na 3 seconden nog had kunnen maken (minder inleggen mag als het boek dunner is; alleen bedragen die de minimale ordergrootte halen). Opgeteld per gemeten dag en dan maal 30 voor een maand.

Elk getal staat er twee keer: **samengevoegd** (ondergrens: driehoeken die op hetzelfde moment, binnen 5 seconden na hun bevestiging, hetzelfde niet-hoofdpaar gebruiken, tellen als één kans; een paar van twee hoofdmunten zoals BTC/EUR of BTCUSDT telt daarbij niet, en er wordt niet doorgeketend) en **los** (bovengrens: elke driehoek apart).

| Soort | Inleg | Kansen per dag (samengevoegd / los) | Winst per dag (samengevoegd / los) | Per maand (GOK, samengevoegd / los) | Alleen de beste beurs, per maand (GOK, samengevoegd) |
|---|---|---|---|---|---|
| Alle beurzen | €100 | 39,6 / 42,5 | €39,56 / €40,39 | €1.186,68 / €1.211,56 | bitstamp: €1.052,46 |
| Alle beurzen | €150 | 39,6 / 42,5 | €55,42 / €56,43 | €1.662,50 / €1.692,88 | bitstamp: €1.480,17 |
| Alle beurzen | €200 | 39,6 / 42,5 | €69,32 / €70,44 | €2.079,69 / €2.113,23 | bitstamp: €1.860,71 |
| Alle beurzen | €2.000 | 39,6 / 42,5 | €95,00 / €98,89 | €2.849,90 / €2.966,62 | bitstamp: €2.065,29 |
| Alle beurzen | €5.000 | 39,6 / 42,5 | €106,42 / €113,27 | €3.192,58 / €3.398,23 | bitstamp: €2.065,29 |
| MiCA (ook via EU-dochter) | €100 | 27,9 / 28,6 | €37,34 / €37,56 | €1.120,20 / €1.126,92 | bitstamp: €1.052,46 |
| MiCA (ook via EU-dochter) | €150 | 27,9 / 28,6 | €52,69 / €53,01 | €1.580,59 / €1.590,38 | bitstamp: €1.480,17 |
| MiCA (ook via EU-dochter) | €200 | 27,9 / 28,6 | €66,31 / €66,74 | €1.989,37 / €2.002,13 | bitstamp: €1.860,71 |
| MiCA (ook via EU-dochter) | €2.000 | 27,9 / 28,6 | €88,54 / €91,53 | €2.656,28 / €2.745,84 | bitstamp: €2.065,29 |
| MiCA (ook via EU-dochter) | €5.000 | 27,9 / 28,6 | €96,81 / €102,58 | €2.904,21 / €3.077,38 | bitstamp: €2.065,29 |
| Grijs | €100 | 11,7 / 14,0 | €2,22 / €2,82 | €66,47 / €84,64 | mexc: €66,47 |
| Grijs | €150 | 11,7 / 14,0 | €2,73 / €3,42 | €81,91 / €102,50 | mexc: €81,91 |
| Grijs | €200 | 11,7 / 14,0 | €3,01 / €3,70 | €90,32 / €111,10 | mexc: €90,32 |
| Grijs | €2.000 | 11,7 / 14,0 | €6,45 / €7,36 | €193,61 / €220,78 | mexc: €193,61 |
| Grijs | €5.000 | 11,7 / 14,0 | €9,61 / €10,70 | €288,37 / €320,85 | mexc: €288,37 |

Waarom dit te rooskleurig is (GOK):

- Het is een **bovengrens**: je pakt elke kans, op elke beurs tegelijk, met het geld al op die beurs. Met weinig geld staat alles op één beurs; de laatste kolom neemt alleen de beste beurs (achteraf gekozen, dus ook te rooskleurig).
- Snelle partijen zitten er in milliseconden bovenop. Wat wij na seconden nog zien, is het restje. Ga je zelf pakken, dan concurreer je met hen en met iedereen die het restje ook ziet; bij elke poging kan een stap net weg zijn (dan zit je met een munt die je niet wilde, en verlies).
- Drie orders na elkaar kosten tijd; tussen stap 1 en 3 kan de prijs bewegen.
- De EU-versie van de beurs kan minder paren hebben dan de wereldwijde API die we meten.

Waarom het te somber kan zijn: lagere kosten (meer handelsvolume, eigen beurs-token, maker in plaats van taker, de 0%-paren van OKX die we niet konden ophalen, Bitstamp gratis onder $1.000 volume per 30 dagen) en sneller meten dan elke paar seconden laten meer zien.

Bron van alle aantallen en bedragen: eigen metingen (GEZIEN), data op de tak `ai-handel-data`, map `driehoek/`. Kosten per stap en hun bron: README.md.
