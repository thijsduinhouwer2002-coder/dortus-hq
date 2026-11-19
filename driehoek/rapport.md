# Driehoek-meter: rapport

Data: 47 driehoeken met winst op het boek gezien (ook kleine en korte), 1 dag(en) (2026-11-19 tot 2026-11-19). Gemeten: ±0,8 uur per beurs (GEZIEN, uit stand.jsonl).

**Lees dit eerst.** Wij meten elke 3 tot 5 seconden met de openbare API. Snelle partijen (bots naast de server van de beurs) pakken een winstgevende driehoek meestal binnen milliseconden. Wat wij zien, is wat er na hen overbleef: driehoeken die korter stonden dan onze ronde zien we vaak niet, en wat wij wel zien, kan jij alleen pakken als je sneller bent dan wie hem nu laat liggen. De sommen onderaan zijn GOK.

Een **echte driehoek**: winst na drie keer takerkosten op het orderboek, minstens €100 diepte, minstens 3 seconden blijven staan (twee metingen na elkaar), niet meer dan 5% winst (verdacht).

## Per beurs: hoe gemeten en hoe dicht bij winst

Beste marge = per ronde de beste driehoek tegen de beste prijzen na kosten (mediaan en hoogste over alle rondes). Negatief = zelfs de beste driehoek verloor geld. Kandidaten = driehoeken die met de beste prijzen winst gaven; daarvan haalt hij de orderboeken op (bekeken), tenzij het budget van die ronde op was (overgeslagen) of de koersen sinds de vorige controle niet veranderden (zelfde). Een positieve beste marge is nog geen winst: de bulk-ticker kan achterlopen of er ligt maar een paar cent op die prijs; het orderboek beslist (kolom Winst op boek).

| Beurs | Status | Paren | Driehoeken | Uur | Rondes | Fouten (te veel) | Beste marge mediaan | Beste marge hoogst | Kandidaten | Bekeken | Overgeslagen | Zelfde | Winst op boek | Echt |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| bitget | grijs | 3659 | 202 | 0,8 | 700 | 0 (0) | -0,281% | -0,054% | 0 | 0 | 0 | 0 | 0 | 0 |
| bitstamp | MiCA | 252 | 346 | 0,8 | 422 | 0 (0) | -0,944% | -0,406% | 0 | 0 | 0 | 0 | 0 | 0 |
| bitvavo | MiCA | 435 | 22 | 0,8 | 529 | 0 (0) | -0,760% | -0,702% | 0 | 0 | 0 | 0 | 0 | 0 |
| gate | MiCA-dochter | 2156 | 372 | 0,8 | 524 | 0 (0) | -0,178% | 0,273% | 64 | 21 | 0 | 43 | 0 | 0 |
| kraken | MiCA | 1352 | 2352 | 0,8 | 423 | 0 (0) | -0,593% | -0,271% | 0 | 0 | 0 | 0 | 0 | 0 |
| kucoin | MiCA-dochter | 968 | 452 | 0,8 | 700 | 0 (0) | 0,502% | 0,613% | 1455 | 1187 | 8 | 258 | 0 | 0 |
| mexc | grijs | 1664 | 886 | 0,8 | 699 | 0 (0) | 0,504% | 1,660% | 3446 | 2144 | 160 | 1130 | 375 | 0 |
| okx | MiCA-dochter | 1248 | 2336 | 0,8 | 703 | 0 (0) | -0,122% | 0,363% | 155 | 148 | 0 | 7 | 0 | 0 |

## Trechter

| Stap | Alle beurzen | MiCA (ook via EU-dochter) | Grijs |
|---|---|---|---|
| winst op het boek, met de lage kosten (bovengrens) | 47 | 0 | 47 |
| winst op het boek, met de gewone kosten | 47 | 0 | 47 |
| en minstens €100 diepte | 1 | 0 | 1 |
| en minstens 3 s blijven staan | 0 | 0 | 0 |
| en niet verdacht = **echt** | 0 | 0 | 0 |

De lage kosten verschillen alleen bij Bitvavo (categorie B, C en D: USDC- en stablecoinparen; Bitvavo noemt ze lager dan 0,25% maar geeft geen getal, dus laag = 0%, GOK). Overal elders is laag gelijk aan gewoon.

## Per dag (echte driehoeken)

| Dag | Soort | Aantal | Mediane winst per keer | Mediane diepte | Mediane duur | Totale winst (beste moment, volle diepte) |
|---|---|---|---|---|---|---|
| 2026-11-19 | Alle beurzen | 0 | - | - | - | €0,00 |
| 2026-11-19 | MiCA (ook via EU-dochter) | 0 | - | - | - | €0,00 |
| 2026-11-19 | Grijs | 0 | - | - | - | €0,00 |
| totaal | Alle beurzen | 0 | - | - | - | €0,00 |
| totaal | MiCA (ook via EU-dochter) | 0 | - | - | - | €0,00 |
| totaal | Grijs | 0 | - | - | - | €0,00 |

## Beste driehoeken per beurs (echt)

Nog geen echte driehoeken gezien.

Grootste driehoeken die **niet** echt waren (te kort, te dun of verdacht):

| Beurs | Driehoek | Winst | Diepte | Duur | Verdacht |
|---|---|---|---|---|---|
| mexc | USDT>SOL>BTC>USDT | €0,29 | €75 | 357 s | nee |
| mexc | USDC>SOL>BTC>USDC | €0,16 | €75 | 24 s | nee |
| mexc | USDC>SOL>BTC>USDC | €0,16 | €75 | 3 s | nee |
| mexc | USDC>SOL>BTC>USDC | €0,15 | €75 | 9 s | nee |
| mexc | USDC>SOL>BTC>USDC | €0,15 | €75 | 0 s | nee |
| mexc | EUR>SOL>BTC>EUR | €0,13 | €75 | 150 s | nee |
| mexc | USDC>SOL>BTC>USDC | €0,11 | €75 | 0 s | nee |
| mexc | USDC>SOL>BTC>USDC | €0,10 | €75 | 6 s | nee |

## Kan een kleine inleg meedoen? (€100, €150, €200)

Minimale ordergrootte per paar uit de openbare API van elke beurs (aantal munten en bedrag in de quote; Bitget: waarde in USDT). Per beurs: hoeveel driehoeken je met dat bedrag kunt rondmaken zonder dat een van de drie orders onder het minimum valt (tegen de beste prijzen, GEZIEN). Het kleinste bedrag dat we toetsen is €10; "≤ €10" betekent dus €10 of minder. Afronding op de stapgrootte van de beurs rekenen we niet mee (bij €100 een paar cent, GOK).

| Beurs | Status | Driehoeken | Met EUR | Mediaan minimale inleg | Mogelijk met €100 | €150 | €200 | Met EUR en €100 |
|---|---|---|---|---|---|---|---|---|
| bitget | grijs | 202 | 46 | ≤ €10 | 202 | 202 | 202 | 46 |
| bitstamp | MiCA | 346 | 260 | €12 | 335 | 336 | 336 | 251 |
| bitvavo | MiCA | 22 | 22 | ≤ €10 | 22 | 22 | 22 | 22 |
| gate | MiCA-dochter | 372 | 0 | ≤ €10 | 372 | 372 | 372 | 0 |
| kraken | MiCA | 2352 | 1368 | ≤ €10 | 2352 | 2352 | 2352 | 1368 |
| kucoin | MiCA-dochter | 452 | 12 | ≤ €10 | 452 | 452 | 452 | 12 |
| mexc | grijs | 886 | 76 | ≤ €10 | 886 | 886 | 886 | 76 |
| okx | MiCA-dochter | 2336 | 1090 | ≤ €10 | 2332 | 2332 | 2332 | 1090 |

Van de 0 echte driehoeken konden er 0 met €100 of minder (minimale ordergrootte gehaald op alle drie stappen).

## Opschaling naar €100, €150, €200, €2.000 en €5.000 inleg (GOK)

Per echte driehoek nemen we de winst die je bij die inleg had kunnen maken op het beste moment (minder inleggen mag als het boek dunner is; alleen bedragen die de minimale ordergrootte halen). Opgeteld per gemeten dag en dan maal 30 voor een maand.

| Soort | Inleg | Echte driehoeken per dag | Winst per dag | Per maand (GOK) | Alleen de beste beurs, per maand (GOK) |
|---|---|---|---|---|---|
| Alle beurzen | €100 | 0,0 | €0,00 | €0,00 | -: €0,00 |
| Alle beurzen | €150 | 0,0 | €0,00 | €0,00 | -: €0,00 |
| Alle beurzen | €200 | 0,0 | €0,00 | €0,00 | -: €0,00 |
| Alle beurzen | €2.000 | 0,0 | €0,00 | €0,00 | -: €0,00 |
| Alle beurzen | €5.000 | 0,0 | €0,00 | €0,00 | -: €0,00 |
| MiCA (ook via EU-dochter) | €100 | 0,0 | €0,00 | €0,00 | -: €0,00 |
| MiCA (ook via EU-dochter) | €150 | 0,0 | €0,00 | €0,00 | -: €0,00 |
| MiCA (ook via EU-dochter) | €200 | 0,0 | €0,00 | €0,00 | -: €0,00 |
| MiCA (ook via EU-dochter) | €2.000 | 0,0 | €0,00 | €0,00 | -: €0,00 |
| MiCA (ook via EU-dochter) | €5.000 | 0,0 | €0,00 | €0,00 | -: €0,00 |
| Grijs | €100 | 0,0 | €0,00 | €0,00 | -: €0,00 |
| Grijs | €150 | 0,0 | €0,00 | €0,00 | -: €0,00 |
| Grijs | €200 | 0,0 | €0,00 | €0,00 | -: €0,00 |
| Grijs | €2.000 | 0,0 | €0,00 | €0,00 | -: €0,00 |
| Grijs | €5.000 | 0,0 | €0,00 | €0,00 | -: €0,00 |

Waarom dit te rooskleurig is (GOK):
- Het is een **bovengrens**: je pakt elke driehoek, op elke beurs tegelijk, met het geld al op die beurs. Met weinig geld staat alles op één beurs; de laatste kolom neemt alleen de beste beurs (achteraf gekozen, dus ook te rooskleurig).
- Snelle partijen zitten er in milliseconden bovenop. Wat wij na seconden nog zien, is het restje. Ga je zelf pakken, dan concurreer je met hen en met iedereen die het restje ook ziet; bij elke poging kan een stap net weg zijn (dan zit je met een munt die je niet wilde, en verlies).
- Drie orders na elkaar kosten tijd; tussen stap 1 en 3 kan de prijs bewegen.
- Afronding op de stapgrootte en de EU-versie van de beurs (minder paren) rekenen we niet mee.
Waarom het te somber kan zijn: lagere kosten (meer handelsvolume, eigen beurs-token, maker in plaats van taker) en sneller meten dan elke paar seconden laten meer zien.

Bron van alle aantallen en bedragen: eigen metingen (GEZIEN), data op de tak `ai-handel-data`, map `driehoek/`. Kosten per stap en hun bron: README.md.
