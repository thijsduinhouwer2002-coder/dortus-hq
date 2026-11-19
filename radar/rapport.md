# Kansenradar: rapport

Gemaakt 2026-11-19 16:20 UTC. Gemeten: **0.8 uur** in 3 run(s). Alle aantallen en bedragen zijn GEZIEN (eigen metingen uit openbare API's), behalve waar GOK staat. Uitleg: `platformen/ai-handel/radar/README.md`.

**Wat we niet zien.** We kijken elke 15 seconden (stablecoins), elke minuut (boeken bij nieuwe noteringen), elke 2 minuten (funding) of elke 3 minuten (lijsten met paren). Snelle partijen kijken elke milliseconde en zitten vaak bij de beurs in de kast. Wat korter bestaat dan onze stap, zien we niet; wat we wel zien, is vaak al half weggekocht voor een gewone gebruiker zijn order plaatst. De sommen per week nemen aan dat je elk moment pakt dat wij zagen, en zijn daarom een **bovengrens (GOK)**.

## A. Nieuwe noteringen

Nieuwe munten op een beurs gezien: **0** (waarvan 0 bij de eerste vergelijking na de start, die kunnen in het gat tussen twee runs genoteerd zijn), 0 stonden al op een andere beurs met dezelfde quote. Prijsverschil-momenten daarna: 0, waarvan **0 echt** (alles open en minstens €100 winstgevend op het boek, zie boven).

**Echte momenten A, per dag**

Nog geen momenten.

| Inleg | Kan meedoen (alle / MiCA) | Minimum onbekend | Mediane winst per keer | Som gemeten | Per week (GOK) |
|---|---|---|---|---|---|
| €100 | 0 / 0 | 0 | - | €0,00 | - |
| €150 | 0 / 0 | 0 | - | €0,00 | - |
| €200 | 0 / 0 | 0 | - | €0,00 | - |
| €500 | 0 / 0 | 0 | - | €0,00 | - |
| €2.000 | 0 / 0 | 0 | - | €0,00 | - |
| €5.000 | 0 / 0 | 0 | - | €0,00 | - |

Bij €100 tot €200 telt een moment alleen als de minimale bedragen bekend zijn en eronder liggen. Vanaf €500 telt onbekend mee (de minima liggen meestal tussen €1 en €10, GEZIEN in de API's).

## B. Funding-pieken

Pieken boven 0,1% per 8 uur (gesloten onder 0,05%): **114 positief met spotmarkt**, 637 negatief (niet te dekken zonder spot te shorten), 39 positief zonder spotmarkt. Daarvan liepen er 114 nog bij het einde van een run en 71 al bij de start (duur en winst te laag geteld). Spotmunt met dezelfde naam maar een andere prijs (ander ding, niet geteld): 13. Met winst na kosten: 1; met minstens één verrekening: 0; met meer dan $1 miljoen handel per dag: 37.

Som per piek: funding die echt verrekend werd, min 4 keer takerkosten (spot in en uit, perp in en uit), plus of min het verschil tussen spot- en perpprijs bij in- en uitstappen. Inleg = 2/3 spot en 1/3 onderpand voor de short bij 2x hefboom (GOK, een gangbare verdeling).

| Begin | Perp | Munt | Spot | Max per 8u | Verrekend | Kosten | Prijsverschil | Netto | Duur | Handel/dag |
|---|---|---|---|---|---|---|---|---|---|---|
| 11-19T16:02 | gate | MMT | gate | 0.2188% | 0.0% (0x) | 0.5% | 0.6368% | **0.1368%** | 18 min | $34.7 mln |
| 11-19T16:06 | mexc | BULLA | mexc | 0.1048% | 0.0% (0x) | 0.2% | 0.1862% | **-0.0138%** | 14 min | $1.0 mln |
| 11-19T16:06 | kraken | METAX | mexc | 0.1789% | 0.0% (0x) | 0.26% | 0.2178% | **-0.0422%** | 14 min | $1.1 mln |
| 11-19T16:02 | gate | SNXX | htx | 0.1146% | 0.0% (0x) | 0.5% | 0.3469% | **-0.1531%** | 18 min | $14.9 mln |
| 11-19T16:02 | gate | VELVET | gate | 0.1939% | 0.0% (0x) | 0.5% | 0.3343% | **-0.1657%** | 18 min | $5.1 mln |
| 11-19T15:40 | hyperliquid | SAGA | mexc | 0.5015% | 0.0% (0x) | 0.19% | None% | **-0.19%** | 6 min | $0.0 mln |
| 11-19T15:46 | hyperliquid | SAGA | mexc | 0.5003% | 0.0% (0x) | 0.19% | 0.0% | **-0.19%** | 12 min | $0.0 mln |
| 11-19T15:40 | kraken | BB | mexc | 0.36% | 0.0% (0x) | 0.2% | None% | **-0.2%** | 6 min | $0.0 mln |
| 11-19T15:40 | mexc | EVAA | mexc | 0.134% | 0.0% (0x) | 0.2% | None% | **-0.2%** | 6 min | $17.6 mln |
| 11-19T15:40 | mexc | TRUST | mexc | 0.1032% | 0.0% (0x) | 0.2% | None% | **-0.2%** | 6 min | $0.1 mln |

**Positieve pieken B, per dag**

| Dag | Aantal (alle / MiCA / grijs) | Mediane winst bij €500 | Mediane duur |
|---|---|---|---|
| 2026-11-19 | 114 / 61 / 53 | -€2,40 | 12 min |

| Inleg | Kan meedoen (alle / MiCA) | Minimum onbekend | Mediane winst per keer | Som gemeten | Per week (GOK) |
|---|---|---|---|---|---|
| €100 | 64 / 37 | 50 | -€0,53 | -€42,21 | - |
| €150 | 64 / 37 | 50 | -€0,79 | -€63,24 | - |
| €200 | 64 / 37 | 50 | -€1,06 | -€84,34 | - |
| €500 | 114 / 61 | 50 | -€2,40 | -€387,63 | - |
| €2.000 | 114 / 61 | 50 | -€9,60 | -€1.550,25 | - |
| €5.000 | 114 / 61 | 50 | -€24,00 | -€3.875,68 | - |

Bij €100 tot €200 telt een moment alleen als de minimale bedragen bekend zijn en eronder liggen. Vanaf €500 telt onbekend mee (de minima liggen meestal tussen €1 en €10, GEZIEN in de API's).

Vergund bij B betekent: perp- en spotbeurs hebben een MiCA-vergunning voor spot. Of de EU-dochter perps aan Nederlandse particulieren geeft, is niet nagekeken (GOK: vaak niet of beperkt). De opschaling is lineair (GOK): bij een dunne perp (weinig handel per dag) kost een grotere order meer dan de laatste prijs, dat meten we niet.

## C. Stablecoins

**C1, tussen beurzen** (dezelfde stablecoin goedkoper kopen dan elders verkopen, na alle kosten): 58 momenten, waarvan **0 echt**.

**Echte momenten C1, per dag**

Nog geen momenten.

| Inleg | Kan meedoen (alle / MiCA) | Minimum onbekend | Mediane winst per keer | Som gemeten | Per week (GOK) |
|---|---|---|---|---|---|
| €100 | 0 / 0 | 0 | - | €0,00 | - |
| €150 | 0 / 0 | 0 | - | €0,00 | - |
| €200 | 0 / 0 | 0 | - | €0,00 | - |
| €500 | 0 / 0 | 0 | - | €0,00 | - |
| €2.000 | 0 / 0 | 0 | - | €0,00 | - |
| €5.000 | 0 / 0 | 0 | - | €0,00 | - |

Bij €100 tot €200 telt een moment alleen als de minimale bedragen bekend zijn en eronder liggen. Vanaf €500 telt onbekend mee (de minima liggen meestal tussen €1 en €10, GEZIEN in de API's).

**C2, los van de koppeling** (boek minstens 0,3% van 1 dollar of 1 euro): 33 momenten, waarvan 24 met minstens €100 op het boek (de rest is een dode markt); daarvan na 2 keer takerkosten nog winst: 11; na kosten nog minstens 0,3%: **11**. Geen arbitrage: je wint alleen als de koers terugkomt (GOK dat hij dat doet; bij USDC in maart 2023 kwam hij terug, bij UST in 2022 niet).

Meest gezien: EURQ-USDT op bitfinex (goedkoop) 3x, EURQ-EUR op bitfinex (goedkoop) 3x, FDUSD-USDT op mexc (goedkoop) 3x, EURQ-EUR op kraken (goedkoop) 3x, EURQ-USD op kraken (goedkoop) 3x, EURQ-USDT op xt (goedkoop) 3x, FDUSD-USDT op xt (goedkoop) 3x, FDUSD-USDT op gate (goedkoop) 3x.

**C2 met winst na kosten, per dag**

| Dag | Aantal (alle / MiCA / grijs) | Mediane winst bij €500 | Mediane duur |
|---|---|---|---|
| 2026-11-19 | 11 / 2 / 9 | €3,86 | 13 min |

| Inleg | Kan meedoen (alle / MiCA) | Minimum onbekend | Mediane winst per keer | Som gemeten | Per week (GOK) |
|---|---|---|---|---|---|
| €100 | 8 / 2 | 3 | €0,77 | €10,76 | - |
| €150 | 8 / 2 | 3 | €1,16 | €16,10 | - |
| €200 | 8 / 2 | 3 | €1,55 | €21,45 | - |
| €500 | 11 / 2 | 3 | €3,86 | €64,11 | - |
| €2.000 | 11 / 2 | 3 | €8,72 | €90,24 | - |
| €5.000 | 11 / 2 | 3 | €11,72 | €100,17 | - |

Bij €100 tot €200 telt een moment alleen als de minimale bedragen bekend zijn en eronder liggen. Vanaf €500 telt onbekend mee (de minima liggen meestal tussen €1 en €10, GEZIEN in de API's).

## Hoe eerlijk is de opschaling naar €2.000 en €5.000

- A en C1: de winst bij €2.000 en €5.000 komt uit het echte orderboek op dat moment (dieper in het boek is duurder). Maar je hebt voorraad op beide beurzen nodig, of je moet overmaken, en dan is het gat vaak weg.
- B: lineair opgeschaald, alleen begrensd door de minimale order. GOK.
- C2: uit het boek, maar het is een gok op terugkeer, geen arbitrage.
- Per week = som gemeten maal 168 uur gedeeld door de gemeten uren. Na een paar uur meten is dat een ruwe GOK; na 7 dagen een week aan metingen.
- Kleine inleg: vaste kosten per keer (opnamekosten van de munt) wegen bij €100 zwaar; die zitten in de winst bij A en C1.

