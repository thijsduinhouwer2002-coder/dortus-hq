# Driehoek-meter: rapport

## Kort antwoord

Op de beurzen met vergunning (MiCA, ook via een EU-dochter): 35 echte kansen die met €100 konden (35 als je elke driehoek los telt; 160,0 per dag). Samen €510,39 tot €510,39 per dag met €100 en €1.016,89 tot €1.016,89 per dag met €200 (GOK; het lage getal voegt driehoeken samen die hetzelfde stukje boek willen, het hoge telt ze los; allebei alsof je ze allemaal als eerste pakt, met het geld al op de juiste beurs). Op de grijze beurzen (geen vergunning): 4 echte kansen die met €100 konden (4 als je elke driehoek los telt; 18,3 per dag). Samen €0,67 tot €0,67 per dag met €100 en €1,34 tot €1,34 per dag met €200 (GOK; het lage getal voegt driehoeken samen die hetzelfde stukje boek willen, het hoge telt ze los; allebei alsof je ze allemaal als eerste pakt, met het geld al op de juiste beurs).

Uitleg: **takerkosten** zijn wat de beurs per order rekent als je meteen koopt of verkoopt tegen de prijs die er ligt (0% tot 0,8% per order; een driehoek is drie orders). **Diepte** is hoeveel euro je tegen die winstgevende prijzen echt kunt kopen en verkopen voordat de prijs slechter wordt. Wij meten elke 3 tot 5 seconden; snelle bots pakken zulke kansen meestal binnen milliseconden, dus wat hier staat is wat er na hen overbleef.

Data: 126 driehoeken met winst op het boek gezien (ook kleine en korte), 1 dag(en) (2026-11-19 tot 2026-11-19). Gemeten: ±5,2 uur per beurs (GEZIEN, uit stand.jsonl).

Een **echte driehoek**: winst na drie keer takerkosten op het orderboek, op twee metingen die minstens 3 seconden uit elkaar liggen elk minstens €100 diepte, bij de latere meting minstens €0,05 winst, en niet meer dan 5% winst (verdacht). Alle bedragen zijn die van de latere meting: wat er na 3 seconden nog stond. Driehoeken op dezelfde beurs die binnen 5 seconden van elkaar bevestigd werden en een paar delen dat geen paar van twee hoofdmunten is (EUR, USD, USDT, USDC, BTC, ETH), tellen als **één kans** (de beste telt): ze willen hetzelfde stukje orderboek. Er wordt niet doorgeketend: een driehoek hoort alleen bij een kans als hij met elk lid ervan dat stukje deelt. Omdat samenvoegen ook te streng kan zijn, staan aantallen en geld er ook los geteld bij (bovengrens).

Regels van vóór 2026-11-19 16:07 UTC (vóór de keuring) hebben geen meting na 3 seconden en tellen daarom nooit als echt. Daar zat ook niets in dat 3 seconden met €100 diepte stond.

## Per beurs: hoe gemeten en hoe dicht bij winst

Beste marge = per ronde de beste driehoek tegen de beste prijzen na kosten (mediaan en hoogste over alle rondes). Negatief = zelfs de beste driehoek verloor geld. Kandidaten = driehoeken die met de beste prijzen winst gaven; daarvan haalt hij de orderboeken op (bekeken), tenzij het budget van die ronde op was (overgeslagen) of de koersen sinds de vorige controle niet veranderden (zelfde). Een positieve beste marge is nog geen winst: de bulk-koers kan achterlopen of er ligt maar een paar cent op die prijs; het orderboek beslist (kolom Winst op boek).

| Beurs | Status | Paren | Driehoeken | Uur | Rondes | Fouten (te veel) | Beste marge mediaan | Beste marge hoogst | Kandidaten | Bekeken | Overgeslagen | Zelfde | Winst op boek | Echt |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| bitget | grijs | 3659 | 202 | 5,2 | 6039 | 1 (0) | -0,284% | 0,012% | 1 | 1 | 0 | 0 | 0 | 0 |
| bitstamp | MiCA | 252 | 346 | 5,2 | 3629 | 0 (0) | -0,232% | 3,905% | 569 | 568 | 0 | 0 | 518 | 31 |
| bitvavo | MiCA | 435 | 22 | 5,2 | 4541 | 0 (0) | -0,759% | -0,670% | 0 | 0 | 0 | 0 | 0 | 0 |
| gate | MiCA-dochter | 2158 | 372 | 5,2 | 4522 | 0 (0) | -0,152% | 1,139% | 1054 | 443 | 0 | 611 | 0 | 0 |
| kraken | MiCA | 1352 | 2352 | 5,2 | 3632 | 0 (0) | -0,207% | 1,958% | 512 | 372 | 0 | 139 | 0 | 0 |
| kucoin | MiCA-dochter | 968 | 452 | 5,2 | 6051 | 0 (0) | 0,968% | 1,933% | 7570 | 3634 | 8 | 3926 | 0 | 0 |
| mexc | grijs | 1664 | 886 | 5,2 | 6047 | 0 (0) | 0,493% | 4,975% | 14260 | 5692 | 166 | 8385 | 554 | 4 |
| okx | MiCA-dochter | 1250 | 2338 | 5,2 | 6054 | 0 (0) | -0,135% | 2,841% | 1556 | 1526 | 6 | 24 | 771 | 4 |

## Trechter

| Stap | Alle beurzen | MiCA (ook via EU-dochter) | Grijs |
|---|---|---|---|
| winst op het boek, met de lage kosten (bovengrens) | 126 | 65 | 61 |
| winst op het boek, met de gewone kosten | 126 | 65 | 61 |
| en ooit minstens €100 diepte | 57 | 50 | 7 |
| en na 3 s nog steeds minstens €100 diepte | 47 | 43 | 4 |
| en dan minstens €0,05 winst | 47 | 43 | 4 |
| en niet verdacht = **echt** | 39 | 35 | 4 |
| echte **kansen** (samengevoegd als ze hetzelfde stukje boek willen; ondergrens) | 39 | 35 | 4 |

De lage kosten verschillen alleen bij Bitvavo (categorie B, C en D: USDC- en stablecoinparen; Bitvavo noemt ze lager dan 0,25% maar geeft geen getal, dus laag = 0%, GOK). Overal elders is laag gelijk aan gewoon.

## Per dag (echte kansen, bedragen na 3 seconden)

| Dag | Soort | Driehoeken | Kansen | Mediane winst per kans | Mediane diepte | Mediane duur met €100 diepte | Totale winst (volle diepte) |
|---|---|---|---|---|---|---|---|
| 2026-11-19 | Alle beurzen | 39 | 39 | €7,61 | €227 | 25,0 s | €279,28 |
| 2026-11-19 | MiCA (ook via EU-dochter) | 35 | 35 | €7,78 | €227 | 30,0 s | €253,08 |
| 2026-11-19 | Grijs | 4 | 4 | €2,92 | €6.654 | 6,0 s | €26,21 |
| totaal | Alle beurzen | 39 | 39 | €7,61 | €227 | 25,0 s | €279,28 |
| totaal | MiCA (ook via EU-dochter) | 35 | 35 | €7,78 | €227 | 30,0 s | €253,08 |
| totaal | Grijs | 4 | 4 | €2,92 | €6.654 | 6,0 s | €26,21 |

## Beste driehoeken per beurs (echt, bedragen na 3 seconden)

**bitstamp** (MiCA)

| Driehoek | Keren | Mediane winst | Hoogste winst | Mediane diepte | Mediane duur met €100 diepte | Kosten per stap |
|---|---|---|---|---|---|---|
| EUR>USD>SKY>EUR | 31 | €8,22 | €11,32 | €227 | 25,0 s | 0,08% + 0,40% + 0,40% |

**mexc** (grijs)

| Driehoek | Keren | Mediane winst | Hoogste winst | Mediane diepte | Mediane duur met €100 diepte | Kosten per stap |
|---|---|---|---|---|---|---|
| USDT>BTC>USDC>USDT | 2 | €12,85 | €20,12 | €35.093 | 10,0 s | 0,05% + 0,00% + 0,00% |
| USDT>SOL>USDC>USDT | 1 | €0,26 | €0,26 | €3.309 | 3,0 s | 0,05% + 0,00% + 0,00% |
| USDT>USDC>BTC>USDT | 1 | €0,25 | €0,25 | €694 | 6,0 s | 0,00% + 0,00% + 0,05% |

**okx** (MiCA-dochter)

| Driehoek | Keren | Mediane winst | Hoogste winst | Mediane diepte | Mediane duur met €100 diepte | Kosten per stap |
|---|---|---|---|---|---|---|
| USDT>XANT>USDC>USDT | 3 | €0,80 | €1,98 | €355 | 216,0 s | 0,10% + 0,10% + 0,10% |
| USDT>USDC>XANT>USDT | 1 | €1,75 | €1,75 | €284 | 156,0 s | 0,10% + 0,10% + 0,10% |

Grootste driehoeken die **niet** echt waren (te kort, te dun, te weinig winst of verdacht). Bedragen van het beste moment:

| Beurs | Driehoek | Winst | Diepte | Duur | Na 3 s nog €100 diepte | Verdacht |
|---|---|---|---|---|---|---|
| bitstamp | EUR>USD>SKY>EUR | €13,92 | €227 | 30 s | ja | ja |
| bitstamp | EUR>USD>SKY>EUR | €13,13 | €200 | 0 s | nee | ja |
| bitstamp | EUR>USD>SKY>EUR | €12,95 | €227 | 80 s | ja | ja |
| bitstamp | EUR>USD>SKY>EUR | €12,45 | €227 | 170 s | ja | ja |
| bitstamp | EUR>USD>SKY>EUR | €12,24 | €227 | 15 s | ja | ja |
| bitstamp | EUR>USD>SKY>EUR | €11,97 | €227 | 20 s | ja | ja |
| bitstamp | EUR>USD>SKY>EUR | €11,90 | €227 | 165 s | ja | ja |
| bitstamp | EUR>USD>SKY>EUR | €11,70 | €227 | 175 s | ja | ja |

## Kan een kleine inleg meedoen? (€100, €150, €200)

Minimale ordergrootte per paar uit de openbare API van elke beurs (aantal munten en bedrag in de quote; Bitget: waarde in USDT). Per beurs: hoeveel driehoeken je met dat bedrag kunt rondmaken zonder dat een van de drie orders onder het minimum valt (tegen de beste prijzen, GEZIEN). Het kleinste bedrag dat we toetsen is €10; "≤ €10" betekent dus €10 of minder. Het aantal munten wordt per order naar beneden afgerond op de stapgrootte van de beurs (uit de API), en bij Bitvavo rekenen we per euro-order €0,01 extra (Bitvavo rondt de kosten naar boven af op de cent).

| Beurs | Status | Driehoeken | Met EUR | Mediaan minimale inleg | Mogelijk met €100 | €150 | €200 | Met EUR en €100 |
|---|---|---|---|---|---|---|---|---|
| bitget | grijs | 202 | 46 | ≤ €10 | 202 | 202 | 202 | 46 |
| bitstamp | MiCA | 346 | 260 | €12 | 335 | 336 | 336 | 251 |
| bitvavo | MiCA | 22 | 22 | ≤ €10 | 22 | 22 | 22 | 22 |
| gate | MiCA-dochter | 372 | 0 | ≤ €10 | 372 | 372 | 372 | 0 |
| kraken | MiCA | 2352 | 1368 | ≤ €10 | 2352 | 2352 | 2352 | 1368 |
| kucoin | MiCA-dochter | 452 | 12 | ≤ €10 | 452 | 452 | 452 | 12 |
| mexc | grijs | 886 | 76 | ≤ €10 | 886 | 886 | 886 | 76 |
| okx | MiCA-dochter | 2338 | 1090 | ≤ €10 | 2326 | 2326 | 2326 | 1082 |

Van de 39 echte kansen konden er 39 met €100 (minimale ordergrootte gehaald op alle drie de orders, winst na 3 seconden).

## Opschaling naar €100, €150, €200, €2.000 en €5.000 inleg (GOK)

Per echte kans nemen we de winst die je bij die inleg na 3 seconden nog had kunnen maken (minder inleggen mag als het boek dunner is; alleen bedragen die de minimale ordergrootte halen). Opgeteld per gemeten dag en dan maal 30 voor een maand.

Elk getal staat er twee keer: **samengevoegd** (ondergrens: driehoeken die op hetzelfde moment, binnen 5 seconden na hun bevestiging, hetzelfde niet-hoofdpaar gebruiken, tellen als één kans; een paar van twee hoofdmunten zoals BTC/EUR of BTCUSDT telt daarbij niet, en er wordt niet doorgeketend) en **los** (bovengrens: elke driehoek apart).

| Soort | Inleg | Kansen per dag (samengevoegd / los) | Winst per dag (samengevoegd / los) | Per maand (GOK, samengevoegd / los) | Alleen de beste beurs, per maand (GOK, samengevoegd) |
|---|---|---|---|---|---|
| Alle beurzen | €100 | 178,3 / 178,3 | €511,06 / €511,06 | €15.331,91 / €15.331,91 | bitstamp: €15.057,61 |
| Alle beurzen | €150 | 178,3 / 178,3 | €764,73 / €764,73 | €22.941,81 / €22.941,81 | bitstamp: €22.533,19 |
| Alle beurzen | €200 | 178,3 / 178,3 | €1.018,23 / €1.018,23 | €30.547,04 / €30.547,04 | bitstamp: €30.008,83 |
| Alle beurzen | €2.000 | 178,3 / 178,3 | €1.167,49 / €1.167,49 | €35.024,64 / €35.024,64 | bitstamp: €34.018,15 |
| Alle beurzen | €5.000 | 178,3 / 178,3 | €1.181,04 / €1.181,04 | €35.431,16 / €35.431,16 | bitstamp: €34.018,15 |
| MiCA (ook via EU-dochter) | €100 | 160,0 / 160,0 | €510,39 / €510,39 | €15.311,77 / €15.311,77 | bitstamp: €15.057,61 |
| MiCA (ook via EU-dochter) | €150 | 160,0 / 160,0 | €763,72 / €763,72 | €22.911,57 / €22.911,57 | bitstamp: €22.533,19 |
| MiCA (ook via EU-dochter) | €200 | 160,0 / 160,0 | €1.016,89 / €1.016,89 | €30.506,73 / €30.506,73 | bitstamp: €30.008,83 |
| MiCA (ook via EU-dochter) | €2.000 | 160,0 / 160,0 | €1.156,93 / €1.156,93 | €34.707,91 / €34.707,91 | bitstamp: €34.018,15 |
| MiCA (ook via EU-dochter) | €5.000 | 160,0 / 160,0 | €1.156,93 / €1.156,93 | €34.707,91 / €34.707,91 | bitstamp: €34.018,15 |
| Grijs | €100 | 18,3 / 18,3 | €0,67 / €0,67 | €20,15 / €20,15 | mexc: €20,15 |
| Grijs | €150 | 18,3 / 18,3 | €1,01 / €1,01 | €30,24 / €30,24 | mexc: €30,24 |
| Grijs | €200 | 18,3 / 18,3 | €1,34 / €1,34 | €40,31 / €40,31 | mexc: €40,31 |
| Grijs | €2.000 | 18,3 / 18,3 | €10,56 / €10,56 | €316,73 / €316,73 | mexc: €316,73 |
| Grijs | €5.000 | 18,3 / 18,3 | €24,11 / €24,11 | €723,25 / €723,25 | mexc: €723,25 |

Waarom dit te rooskleurig is (GOK):

- Het is een **bovengrens**: je pakt elke kans, op elke beurs tegelijk, met het geld al op die beurs. Met weinig geld staat alles op één beurs; de laatste kolom neemt alleen de beste beurs (achteraf gekozen, dus ook te rooskleurig).
- Snelle partijen zitten er in milliseconden bovenop. Wat wij na seconden nog zien, is het restje. Ga je zelf pakken, dan concurreer je met hen en met iedereen die het restje ook ziet; bij elke poging kan een stap net weg zijn (dan zit je met een munt die je niet wilde, en verlies).
- Drie orders na elkaar kosten tijd; tussen stap 1 en 3 kan de prijs bewegen.
- De EU-versie van de beurs kan minder paren hebben dan de wereldwijde API die we meten.

Waarom het te somber kan zijn: lagere kosten (meer handelsvolume, eigen beurs-token, maker in plaats van taker, de 0%-paren van OKX die we niet konden ophalen, Bitstamp gratis onder $1.000 volume per 30 dagen) en sneller meten dan elke paar seconden laten meer zien.

Bron van alle aantallen en bedragen: eigen metingen (GEZIEN), data op de tak `ai-handel-data`, map `driehoek/`. Kosten per stap en hun bron: README.md.
