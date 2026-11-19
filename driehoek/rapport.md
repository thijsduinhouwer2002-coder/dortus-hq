# Driehoek-meter: rapport

## Kort antwoord

Op de beurzen met vergunning (MiCA, ook via een EU-dochter): nog geen enkele driehoek die je met €100 tot €200 had kunnen pakken. Na de kosten en na 3 seconden bleef er niets over met minstens €100 diepte. De beste driehoek per ronde zat in de mediaan op -0,21% (negatief = verlies; positief zegt nog niet dat er op het boek iets te halen was). Op de grijze beurzen (geen vergunning): 3 echte kansen die met €100 konden (3 als je elke driehoek los telt; 32,0 per dag). Samen €0,95 tot €0,95 per dag met €100 en €1,90 tot €1,90 per dag met €200 (GOK; het lage getal voegt driehoeken samen die hetzelfde stukje boek willen, het hoge telt ze los; allebei alsof je ze allemaal als eerste pakt, met het geld al op de juiste beurs).

Uitleg: **takerkosten** zijn wat de beurs per order rekent als je meteen koopt of verkoopt tegen de prijs die er ligt (0% tot 0,8% per order; een driehoek is drie orders). **Diepte** is hoeveel euro je tegen die winstgevende prijzen echt kunt kopen en verkopen voordat de prijs slechter wordt. Wij meten elke 3 tot 5 seconden; snelle bots pakken zulke kansen meestal binnen milliseconden, dus wat hier staat is wat er na hen overbleef.

Data: 56 driehoeken met winst op het boek gezien (ook kleine en korte), 1 dag(en) (2026-11-19 tot 2026-11-19). Gemeten: ±2,2 uur per beurs (GEZIEN, uit stand.jsonl).

Een **echte driehoek**: winst na drie keer takerkosten op het orderboek, op twee metingen die minstens 3 seconden uit elkaar liggen elk minstens €100 diepte, bij de latere meting minstens €0,05 winst, en niet meer dan 5% winst (verdacht). Alle bedragen zijn die van de latere meting: wat er na 3 seconden nog stond. Driehoeken op dezelfde beurs die binnen 5 seconden van elkaar bevestigd werden en een paar delen dat geen paar van twee hoofdmunten is (EUR, USD, USDT, USDC, BTC, ETH), tellen als **één kans** (de beste telt): ze willen hetzelfde stukje orderboek. Er wordt niet doorgeketend: een driehoek hoort alleen bij een kans als hij met elk lid ervan dat stukje deelt. Omdat samenvoegen ook te streng kan zijn, staan aantallen en geld er ook los geteld bij (bovengrens).

Regels van vóór 2026-11-19 16:07 UTC (vóór de keuring) hebben geen meting na 3 seconden en tellen daarom nooit als echt. Daar zat ook niets in dat 3 seconden met €100 diepte stond.

## Per beurs: hoe gemeten en hoe dicht bij winst

Beste marge = per ronde de beste driehoek tegen de beste prijzen na kosten (mediaan en hoogste over alle rondes). Negatief = zelfs de beste driehoek verloor geld. Kandidaten = driehoeken die met de beste prijzen winst gaven; daarvan haalt hij de orderboeken op (bekeken), tenzij het budget van die ronde op was (overgeslagen) of de koersen sinds de vorige controle niet veranderden (zelfde). Een positieve beste marge is nog geen winst: de bulk-koers kan achterlopen of er ligt maar een paar cent op die prijs; het orderboek beslist (kolom Winst op boek).

| Beurs | Status | Paren | Driehoeken | Uur | Rondes | Fouten (te veel) | Beste marge mediaan | Beste marge hoogst | Kandidaten | Bekeken | Overgeslagen | Zelfde | Winst op boek | Echt |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| bitget | grijs | 3659 | 202 | 2,2 | 2448 | 0 (0) | -0,279% | -0,014% | 0 | 0 | 0 | 0 | 0 | 0 |
| bitstamp | MiCA | 252 | 346 | 2,2 | 1471 | 0 (0) | -0,236% | -0,102% | 0 | 0 | 0 | 0 | 0 | 0 |
| bitvavo | MiCA | 435 | 22 | 2,2 | 1843 | 0 (0) | -0,760% | -0,671% | 0 | 0 | 0 | 0 | 0 | 0 |
| gate | MiCA-dochter | 2156 | 372 | 2,2 | 1833 | 0 (0) | -0,157% | 1,100% | 234 | 90 | 0 | 144 | 0 | 0 |
| kraken | MiCA | 1352 | 2352 | 2,2 | 1474 | 0 (0) | -0,210% | 0,179% | 127 | 93 | 0 | 34 | 0 | 0 |
| kucoin | MiCA-dochter | 968 | 452 | 2,2 | 2452 | 0 (0) | 0,768% | 1,933% | 3518 | 1436 | 8 | 2072 | 0 | 0 |
| mexc | grijs | 1664 | 886 | 2,2 | 2449 | 0 (0) | 0,583% | 4,975% | 7761 | 3616 | 160 | 3971 | 539 | 3 |
| okx | MiCA-dochter | 1248 | 2336 | 2,2 | 2455 | 0 (0) | -0,133% | 0,363% | 331 | 319 | 0 | 12 | 0 | 0 |

## Trechter

| Stap | Alle beurzen | MiCA (ook via EU-dochter) | Grijs |
|---|---|---|---|
| winst op het boek, met de lage kosten (bovengrens) | 56 | 0 | 56 |
| winst op het boek, met de gewone kosten | 56 | 0 | 56 |
| en ooit minstens €100 diepte | 5 | 0 | 5 |
| en na 3 s nog steeds minstens €100 diepte | 3 | 0 | 3 |
| en dan minstens €0,05 winst | 3 | 0 | 3 |
| en niet verdacht = **echt** | 3 | 0 | 3 |
| echte **kansen** (samengevoegd als ze hetzelfde stukje boek willen; ondergrens) | 3 | 0 | 3 |

De lage kosten verschillen alleen bij Bitvavo (categorie B, C en D: USDC- en stablecoinparen; Bitvavo noemt ze lager dan 0,25% maar geeft geen getal, dus laag = 0%, GOK). Overal elders is laag gelijk aan gewoon.

## Per dag (echte kansen, bedragen na 3 seconden)

| Dag | Soort | Driehoeken | Kansen | Mediane winst per kans | Mediane diepte | Mediane duur met €100 diepte | Totale winst (volle diepte) |
|---|---|---|---|---|---|---|---|
| 2026-11-19 | Alle beurzen | 3 | 3 | €0,26 | €3.309 | 6,0 s | €20,63 |
| 2026-11-19 | MiCA (ook via EU-dochter) | 0 | 0 | - | - | - | €0,00 |
| 2026-11-19 | Grijs | 3 | 3 | €0,26 | €3.309 | 6,0 s | €20,63 |
| totaal | Alle beurzen | 3 | 3 | €0,26 | €3.309 | 6,0 s | €20,63 |
| totaal | MiCA (ook via EU-dochter) | 0 | 0 | - | - | - | €0,00 |
| totaal | Grijs | 3 | 3 | €0,26 | €3.309 | 6,0 s | €20,63 |

## Beste driehoeken per beurs (echt, bedragen na 3 seconden)

**mexc** (grijs)

| Driehoek | Keren | Mediane winst | Hoogste winst | Mediane diepte | Mediane duur met €100 diepte | Kosten per stap |
|---|---|---|---|---|---|---|
| USDT>BTC>USDC>USDT | 1 | €20,12 | €20,12 | €60.185 | 14,0 s | 0,05% + 0,00% + 0,00% |
| USDT>SOL>USDC>USDT | 1 | €0,26 | €0,26 | €3.309 | 3,0 s | 0,05% + 0,00% + 0,00% |
| USDT>USDC>BTC>USDT | 1 | €0,25 | €0,25 | €694 | 6,0 s | 0,00% + 0,00% + 0,05% |

Grootste driehoeken die **niet** echt waren (te kort, te dun, te weinig winst of verdacht). Bedragen van het beste moment:

| Beurs | Driehoek | Winst | Diepte | Duur | Na 3 s nog €100 diepte | Verdacht |
|---|---|---|---|---|---|---|
| mexc | USDT>SOL>BTC>USDT | €0,29 | €75 | 357 s | nee | nee |
| mexc | USDC>SOL>BTC>USDC | €0,16 | €75 | 24 s | nee | nee |
| mexc | USDC>SOL>BTC>USDC | €0,16 | €75 | 3 s | nee | nee |
| mexc | USDC>SOL>BTC>USDC | €0,15 | €75 | 9 s | nee | nee |
| mexc | USDC>SOL>BTC>USDC | €0,15 | €75 | 0 s | nee | nee |
| mexc | EUR>SOL>BTC>EUR | €0,13 | €75 | 150 s | nee | nee |
| mexc | USDC>SOL>BTC>USDC | €0,11 | €75 | 0 s | nee | nee |
| mexc | USDC>SOL>BTC>USDC | €0,10 | €75 | 6 s | nee | nee |

## Kan een kleine inleg meedoen? (€100, €150, €200)

Minimale ordergrootte per paar uit de openbare API van elke beurs (aantal munten en bedrag in de quote; Bitget: waarde in USDT). Per beurs: hoeveel driehoeken je met dat bedrag kunt rondmaken zonder dat een van de drie orders onder het minimum valt (tegen de beste prijzen, GEZIEN). Het kleinste bedrag dat we toetsen is €10; "≤ €10" betekent dus €10 of minder. Het aantal munten wordt per order naar beneden afgerond op de stapgrootte van de beurs (uit de API), en bij Bitvavo rekenen we per euro-order €0,01 extra (Bitvavo rondt de kosten naar boven af op de cent).

| Beurs | Status | Driehoeken | Met EUR | Mediaan minimale inleg | Mogelijk met €100 | €150 | €200 | Met EUR en €100 |
|---|---|---|---|---|---|---|---|---|
| bitget | grijs | 202 | 46 | ≤ €10 | 202 | 202 | 202 | 46 |
| bitstamp | MiCA | 346 | 260 | €12 | 325 | 326 | 326 | 247 |
| bitvavo | MiCA | 22 | 22 | ≤ €10 | 22 | 22 | 22 | 22 |
| gate | MiCA-dochter | 372 | 0 | ≤ €10 | 372 | 372 | 372 | 0 |
| kraken | MiCA | 2352 | 1368 | ≤ €10 | 2352 | 2352 | 2352 | 1368 |
| kucoin | MiCA-dochter | 452 | 12 | ≤ €10 | 452 | 452 | 452 | 12 |
| mexc | grijs | 886 | 76 | ≤ €10 | 886 | 886 | 886 | 76 |
| okx | MiCA-dochter | 2336 | 1090 | ≤ €10 | 2328 | 2328 | 2328 | 1086 |

Van de 3 echte kansen konden er 3 met €100 (minimale ordergrootte gehaald op alle drie de orders, winst na 3 seconden).

## Opschaling naar €100, €150, €200, €2.000 en €5.000 inleg (GOK)

Per echte kans nemen we de winst die je bij die inleg na 3 seconden nog had kunnen maken (minder inleggen mag als het boek dunner is; alleen bedragen die de minimale ordergrootte halen). Opgeteld per gemeten dag en dan maal 30 voor een maand.

Elk getal staat er twee keer: **samengevoegd** (ondergrens: driehoeken die op hetzelfde moment, binnen 5 seconden na hun bevestiging, hetzelfde niet-hoofdpaar gebruiken, tellen als één kans; een paar van twee hoofdmunten zoals BTC/EUR of BTCUSDT telt daarbij niet, en er wordt niet doorgeketend) en **los** (bovengrens: elke driehoek apart).

| Soort | Inleg | Kansen per dag (samengevoegd / los) | Winst per dag (samengevoegd / los) | Per maand (GOK, samengevoegd / los) | Alleen de beste beurs, per maand (GOK, samengevoegd) |
|---|---|---|---|---|---|
| Alle beurzen | €100 | 32,0 / 32,0 | €0,95 / €0,95 | €28,48 / €28,48 | mexc: €28,48 |
| Alle beurzen | €150 | 32,0 / 32,0 | €1,43 / €1,43 | €42,75 / €42,75 | mexc: €42,75 |
| Alle beurzen | €200 | 32,0 / 32,0 | €1,90 / €1,90 | €56,99 / €56,99 | mexc: €56,99 |
| Alle beurzen | €2.000 | 32,0 / 32,0 | €12,28 / €12,28 | €368,29 / €368,29 | mexc: €368,29 |
| Alle beurzen | €5.000 | 32,0 / 32,0 | €25,36 / €25,36 | €760,70 / €760,70 | mexc: €760,70 |
| MiCA (ook via EU-dochter) | €100 | 0,0 / 0,0 | €0,00 / €0,00 | €0,00 / €0,00 | -: €0,00 |
| MiCA (ook via EU-dochter) | €150 | 0,0 / 0,0 | €0,00 / €0,00 | €0,00 / €0,00 | -: €0,00 |
| MiCA (ook via EU-dochter) | €200 | 0,0 / 0,0 | €0,00 / €0,00 | €0,00 / €0,00 | -: €0,00 |
| MiCA (ook via EU-dochter) | €2.000 | 0,0 / 0,0 | €0,00 / €0,00 | €0,00 / €0,00 | -: €0,00 |
| MiCA (ook via EU-dochter) | €5.000 | 0,0 / 0,0 | €0,00 / €0,00 | €0,00 / €0,00 | -: €0,00 |
| Grijs | €100 | 32,0 / 32,0 | €0,95 / €0,95 | €28,48 / €28,48 | mexc: €28,48 |
| Grijs | €150 | 32,0 / 32,0 | €1,43 / €1,43 | €42,75 / €42,75 | mexc: €42,75 |
| Grijs | €200 | 32,0 / 32,0 | €1,90 / €1,90 | €56,99 / €56,99 | mexc: €56,99 |
| Grijs | €2.000 | 32,0 / 32,0 | €12,28 / €12,28 | €368,29 / €368,29 | mexc: €368,29 |
| Grijs | €5.000 | 32,0 / 32,0 | €25,36 / €25,36 | €760,70 / €760,70 | mexc: €760,70 |

Waarom dit te rooskleurig is (GOK):

- Het is een **bovengrens**: je pakt elke kans, op elke beurs tegelijk, met het geld al op die beurs. Met weinig geld staat alles op één beurs; de laatste kolom neemt alleen de beste beurs (achteraf gekozen, dus ook te rooskleurig).
- Snelle partijen zitten er in milliseconden bovenop. Wat wij na seconden nog zien, is het restje. Ga je zelf pakken, dan concurreer je met hen en met iedereen die het restje ook ziet; bij elke poging kan een stap net weg zijn (dan zit je met een munt die je niet wilde, en verlies).
- Drie orders na elkaar kosten tijd; tussen stap 1 en 3 kan de prijs bewegen.
- De EU-versie van de beurs kan minder paren hebben dan de wereldwijde API die we meten.

Waarom het te somber kan zijn: lagere kosten (meer handelsvolume, eigen beurs-token, maker in plaats van taker, de 0%-paren van OKX die we niet konden ophalen, Bitstamp gratis onder $1.000 volume per 30 dagen) en sneller meten dan elke paar seconden laten meer zien.

Bron van alle aantallen en bedragen: eigen metingen (GEZIEN), data op de tak `ai-handel-data`, map `driehoek/`. Kosten per stap en hun bron: README.md.
