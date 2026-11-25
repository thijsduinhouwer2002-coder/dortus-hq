# Driehoek-meter: rapport

## Kort antwoord

Op de beurzen met vergunning (MiCA, ook via een EU-dochter): 128 echte kansen die met €100 konden (132 als je elke driehoek los telt; 22,9 per dag). Samen €29,71 tot €29,89 per dag met €100 en €52,46 tot €52,80 per dag met €200 (GOK; het lage getal voegt driehoeken samen die hetzelfde stukje boek willen, het hoge telt ze los; allebei alsof je ze allemaal als eerste pakt, met het geld al op de juiste beurs). Op de grijze beurzen (geen vergunning): 58 echte kansen die met €100 konden (70 als je elke driehoek los telt; 10,4 per dag). Samen €1,91 tot €2,49 per dag met €100 en €2,59 tot €3,27 per dag met €200 (GOK; het lage getal voegt driehoeken samen die hetzelfde stukje boek willen, het hoge telt ze los; allebei alsof je ze allemaal als eerste pakt, met het geld al op de juiste beurs).

Uitleg: **takerkosten** zijn wat de beurs per order rekent als je meteen koopt of verkoopt tegen de prijs die er ligt (0% tot 0,8% per order; een driehoek is drie orders). **Diepte** is hoeveel euro je tegen die winstgevende prijzen echt kunt kopen en verkopen voordat de prijs slechter wordt. Wij meten elke 3 tot 5 seconden; snelle bots pakken zulke kansen meestal binnen milliseconden, dus wat hier staat is wat er na hen overbleef.

Data: 1918 driehoeken met winst op het boek gezien (ook kleine en korte), 7 dag(en) (2026-11-19 tot 2026-11-25). Gemeten: ±134,4 uur per beurs (GEZIEN, uit stand.jsonl).

Een **echte driehoek**: winst na drie keer takerkosten op het orderboek, op twee metingen die minstens 3 seconden uit elkaar liggen elk minstens €100 diepte, bij de latere meting minstens €0,05 winst, en niet meer dan 5% winst (verdacht). Alle bedragen zijn die van de latere meting: wat er na 3 seconden nog stond. Driehoeken op dezelfde beurs die binnen 5 seconden van elkaar bevestigd werden en een paar delen dat geen paar van twee hoofdmunten is (EUR, USD, USDT, USDC, BTC, ETH), tellen als **één kans** (de beste telt): ze willen hetzelfde stukje orderboek. Er wordt niet doorgeketend: een driehoek hoort alleen bij een kans als hij met elk lid ervan dat stukje deelt. Omdat samenvoegen ook te streng kan zijn, staan aantallen en geld er ook los geteld bij (bovengrens).

Regels van vóór 2026-11-19 16:07 UTC (vóór de keuring) hebben geen meting na 3 seconden en tellen daarom nooit als echt. Daar zat ook niets in dat 3 seconden met €100 diepte stond.

## Per beurs: hoe gemeten en hoe dicht bij winst

Beste marge = per ronde de beste driehoek tegen de beste prijzen na kosten (mediaan en hoogste over alle rondes). Negatief = zelfs de beste driehoek verloor geld. Kandidaten = driehoeken die met de beste prijzen winst gaven; daarvan haalt hij de orderboeken op (bekeken), tenzij het budget van die ronde op was (overgeslagen) of de koersen sinds de vorige controle niet veranderden (zelfde). Een positieve beste marge is nog geen winst: de bulk-koers kan achterlopen of er ligt maar een paar cent op die prijs; het orderboek beslist (kolom Winst op boek).

| Beurs | Status | Paren | Driehoeken | Uur | Rondes | Fouten (te veel) | Beste marge mediaan | Beste marge hoogst | Kandidaten | Bekeken | Overgeslagen | Zelfde | Winst op boek | Echt |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| bitget | grijs | 3659 | 202 | 134,4 | 160882 | 2 (0) | -0,276% | 1,738% | 11476 | 9931 | 124 | 1421 | 1 | 0 |
| bitstamp | MiCA | 252 | 346 | 134,4 | 96542 | 3 (0) | -0,223% | 4,996% | 106168 | 102759 | 532 | 2861 | 94830 | 93 |
| bitvavo | MiCA | 433 | 22 | 134,4 | 120695 | 2 (0) | -0,759% | -0,309% | 522 | 321 | 0 | 201 | 9 | 0 |
| gate | MiCA-dochter | 2133 | 372 | 134,4 | 119911 | 5 (0) | -0,176% | 4,641% | 44228 | 18271 | 955 | 25000 | 4 | 0 |
| kraken | MiCA | 1351 | 2350 | 134,4 | 96568 | 1 (0) | -0,200% | 4,992% | 21629 | 13367 | 3335 | 4926 | 3 | 0 |
| kucoin | MiCA-dochter | 969 | 452 | 134,4 | 160968 | 3 (0) | -0,154% | 4,979% | 64107 | 34336 | 278 | 29491 | 9 | 0 |
| mexc | grijs | 1635 | 868 | 134,4 | 160138 | 36 (0) | 0,289% | 4,999% | 436515 | 254286 | 3420 | 172128 | 6099 | 70 |
| okx | MiCA-dochter | 1250 | 2338 | 134,4 | 160898 | 2 (0) | -0,088% | 4,999% | 266688 | 230846 | 13004 | 22813 | 118243 | 39 |

## Trechter

| Stap | Alle beurzen | MiCA (ook via EU-dochter) | Grijs |
|---|---|---|---|
| winst op het boek, met de lage kosten (bovengrens) | 1918 | 941 | 977 |
| winst op het boek, met de gewone kosten | 1909 | 932 | 977 |
| en ooit minstens €100 diepte | 405 | 206 | 199 |
| en na 3 s nog steeds minstens €100 diepte | 244 | 163 | 81 |
| en dan minstens €0,05 winst | 221 | 151 | 70 |
| en niet verdacht = **echt** | 202 | 132 | 70 |
| echte **kansen** (samengevoegd als ze hetzelfde stukje boek willen; ondergrens) | 186 | 128 | 58 |

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
| 2026-11-25 | Alle beurzen | 7 | 6 | €0,22 | €961 | 18,0 s | €84,28 |
| 2026-11-25 | MiCA (ook via EU-dochter) | 4 | 3 | €0,34 | €227 | 25,0 s | €83,67 |
| 2026-11-25 | Grijs | 3 | 3 | €0,10 | €1.694 | 6,0 s | €0,61 |
| totaal | Alle beurzen | 202 | 186 | €0,63 | €227 | 16,0 s | €625,02 |
| totaal | MiCA (ook via EU-dochter) | 132 | 128 | €1,12 | €227 | 43,0 s | €554,04 |
| totaal | Grijs | 70 | 58 | €0,30 | €214 | 6,0 s | €70,97 |

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
| USDT>ETH>BRL>USDT | 5 | €0,30 | €0,45 | €116 | 3,0 s | 0,05% + 0,05% + 0,08% |

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
| bitstamp | MiCA | 346 | 260 | €12 | 326 | 327 | 327 | 242 |
| bitvavo | MiCA | 22 | 22 | ≤ €10 | 22 | 22 | 22 | 22 |
| gate | MiCA-dochter | 372 | 0 | ≤ €10 | 372 | 372 | 372 | 0 |
| kraken | MiCA | 2350 | 1366 | ≤ €10 | 2346 | 2349 | 2349 | 1366 |
| kucoin | MiCA-dochter | 452 | 12 | ≤ €10 | 452 | 452 | 452 | 12 |
| mexc | grijs | 868 | 76 | ≤ €10 | 868 | 868 | 868 | 76 |
| okx | MiCA-dochter | 2338 | 1090 | ≤ €10 | 2330 | 2330 | 2330 | 1090 |

Van de 186 echte kansen konden er 186 met €100 (minimale ordergrootte gehaald op alle drie de orders, winst na 3 seconden).

## Opschaling naar €100, €150, €200, €2.000 en €5.000 inleg (GOK)

Per echte kans nemen we de winst die je bij die inleg na 3 seconden nog had kunnen maken (minder inleggen mag als het boek dunner is; alleen bedragen die de minimale ordergrootte halen). Opgeteld per gemeten dag en dan maal 30 voor een maand.

Elk getal staat er twee keer: **samengevoegd** (ondergrens: driehoeken die op hetzelfde moment, binnen 5 seconden na hun bevestiging, hetzelfde niet-hoofdpaar gebruiken, tellen als één kans; een paar van twee hoofdmunten zoals BTC/EUR of BTCUSDT telt daarbij niet, en er wordt niet doorgeketend) en **los** (bovengrens: elke driehoek apart).

| Soort | Inleg | Kansen per dag (samengevoegd / los) | Winst per dag (samengevoegd / los) | Per maand (GOK, samengevoegd / los) | Alleen de beste beurs, per maand (GOK, samengevoegd) |
|---|---|---|---|---|---|
| Alle beurzen | €100 | 33,2 / 36,1 | €31,62 / €32,38 | €948,64 / €971,38 | bitstamp: €827,20 |
| Alle beurzen | €150 | 33,2 / 36,1 | €44,16 / €45,09 | €1.324,71 / €1.352,75 | bitstamp: €1.163,43 |
| Alle beurzen | €200 | 33,2 / 36,1 | €55,05 / €56,07 | €1.651,49 / €1.682,04 | bitstamp: €1.460,97 |
| Alle beurzen | €2.000 | 33,2 / 36,1 | €75,74 / €78,98 | €2.272,29 / €2.369,48 | bitstamp: €1.620,94 |
| Alle beurzen | €5.000 | 33,2 / 36,1 | €85,67 / €91,30 | €2.570,24 / €2.738,98 | bitstamp: €1.620,94 |
| MiCA (ook via EU-dochter) | €100 | 22,9 / 23,6 | €29,71 / €29,89 | €891,42 / €896,76 | bitstamp: €827,20 |
| MiCA (ook via EU-dochter) | €150 | 22,9 / 23,6 | €41,79 / €42,05 | €1.253,69 / €1.261,49 | bitstamp: €1.163,43 |
| MiCA (ook via EU-dochter) | €200 | 22,9 / 23,6 | €52,46 / €52,80 | €1.573,82 / €1.583,98 | bitstamp: €1.460,97 |
| MiCA (ook via EU-dochter) | €2.000 | 22,9 / 23,6 | €70,45 / €72,84 | €2.113,50 / €2.185,33 | bitstamp: €1.620,94 |
| MiCA (ook via EU-dochter) | €5.000 | 22,9 / 23,6 | €77,91 / €82,55 | €2.337,34 / €2.476,57 | bitstamp: €1.620,94 |
| Grijs | €100 | 10,4 / 12,5 | €1,91 / €2,49 | €57,22 / €74,62 | mexc: €57,22 |
| Grijs | €150 | 10,4 / 12,5 | €2,37 / €3,04 | €71,02 / €91,26 | mexc: €71,02 |
| Grijs | €200 | 10,4 / 12,5 | €2,59 / €3,27 | €77,67 / €98,06 | mexc: €77,67 |
| Grijs | €2.000 | 10,4 / 12,5 | €5,29 / €6,14 | €158,78 / €184,16 | mexc: €158,78 |
| Grijs | €5.000 | 10,4 / 12,5 | €7,76 / €8,75 | €232,89 / €262,41 | mexc: €232,89 |

Waarom dit te rooskleurig is (GOK):

- Het is een **bovengrens**: je pakt elke kans, op elke beurs tegelijk, met het geld al op die beurs. Met weinig geld staat alles op één beurs; de laatste kolom neemt alleen de beste beurs (achteraf gekozen, dus ook te rooskleurig).
- Snelle partijen zitten er in milliseconden bovenop. Wat wij na seconden nog zien, is het restje. Ga je zelf pakken, dan concurreer je met hen en met iedereen die het restje ook ziet; bij elke poging kan een stap net weg zijn (dan zit je met een munt die je niet wilde, en verlies).
- Drie orders na elkaar kosten tijd; tussen stap 1 en 3 kan de prijs bewegen.
- De EU-versie van de beurs kan minder paren hebben dan de wereldwijde API die we meten.

Waarom het te somber kan zijn: lagere kosten (meer handelsvolume, eigen beurs-token, maker in plaats van taker, de 0%-paren van OKX die we niet konden ophalen, Bitstamp gratis onder $1.000 volume per 30 dagen) en sneller meten dan elke paar seconden laten meer zien.

Bron van alle aantallen en bedragen: eigen metingen (GEZIEN), data op de tak `ai-handel-data`, map `driehoek/`. Kosten per stap en hun bron: README.md.
