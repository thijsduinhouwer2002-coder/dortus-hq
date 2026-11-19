# Kansenradar: rapport

Gemaakt 2026-11-19 15:59 UTC. Gemeten: **0.4 uur** in 2 run(s). Alle aantallen en bedragen zijn GEZIEN (eigen metingen uit openbare API's), behalve waar GOK staat. Uitleg: `platformen/ai-handel/radar/README.md`.

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

Pieken boven 0,1% per 8 uur (gesloten onder 0,05%): **54 positief met spotmarkt**, 326 negatief (niet te dekken zonder spot te shorten), 18 positief zonder spotmarkt. Daarvan liepen er 54 nog bij het einde van een run en 49 al bij de start (duur en winst te laag geteld). Spotmunt met dezelfde naam maar een andere prijs (ander ding, niet geteld): 7. Met winst na kosten: 0; met minstens één verrekening: 0; met meer dan $1 miljoen handel per dag: 17.

Som per piek: funding die echt verrekend werd, min 4 keer takerkosten (spot in en uit, perp in en uit), plus of min het verschil tussen spot- en perpprijs bij in- en uitstappen. Inleg = 2/3 spot en 1/3 onderpand voor de short bij 2x hefboom (GOK, een gangbare verdeling).

| Begin | Perp | Munt | Spot | Max per 8u | Verrekend | Kosten | Prijsverschil | Netto | Duur | Handel/dag |
|---|---|---|---|---|---|---|---|---|---|---|
| 11-19T15:40 | hyperliquid | SAGA | mexc | 0.5015% | 0.0% (0x) | 0.19% | None% | **-0.19%** | 6 min | $0.0 mln |
| 11-19T15:46 | hyperliquid | SAGA | mexc | 0.5003% | 0.0% (0x) | 0.19% | 0.0% | **-0.19%** | 12 min | $0.0 mln |
| 11-19T15:40 | kraken | BB | mexc | 0.36% | 0.0% (0x) | 0.2% | None% | **-0.2%** | 6 min | $0.0 mln |
| 11-19T15:40 | mexc | EVAA | mexc | 0.134% | 0.0% (0x) | 0.2% | None% | **-0.2%** | 6 min | $17.6 mln |
| 11-19T15:40 | mexc | TRUST | mexc | 0.1032% | 0.0% (0x) | 0.2% | None% | **-0.2%** | 6 min | $0.1 mln |
| 11-19T15:42 | kraken | PIXEL | mexc | 0.1456% | 0.0% (0x) | 0.2% | None% | **-0.2%** | 4 min | $0.0 mln |
| 11-19T15:42 | kraken | IOTX | mexc | 0.1145% | 0.0% (0x) | 0.2% | None% | **-0.2%** | 4 min | $0.0 mln |
| 11-19T15:46 | kraken | PIXEL | mexc | 0.1391% | 0.0% (0x) | 0.2% | 0.0% | **-0.2%** | 12 min | $0.0 mln |
| 11-19T15:58 | mexc | AIOT | mexc | 0.1008% | 0.0% (0x) | 0.2% | None% | **-0.2%** | 0 s | $0.3 mln |
| 11-19T15:40 | mexc | SPORTFUN | bingx | 0.1214% | 0.0% (0x) | 0.24% | None% | **-0.24%** | 6 min | $0.1 mln |

**Positieve pieken B, per dag**

| Dag | Aantal (alle / MiCA / grijs) | Mediane winst bij €500 | Mediane duur |
|---|---|---|---|
| 2026-11-19 | 54 / 27 / 27 | -€2,06 | 6 min |

| Inleg | Kan meedoen (alle / MiCA) | Minimum onbekend | Mediane winst per keer | Som gemeten | Per week (GOK) |
|---|---|---|---|---|---|
| €100 | 21 / 12 | 33 | -€0,59 | -€15,61 | - |
| €150 | 21 / 12 | 33 | -€0,88 | -€23,38 | - |
| €200 | 21 / 12 | 33 | -€1,17 | -€31,15 | - |
| €500 | 54 / 27 | 33 | -€2,06 | -€133,87 | - |
| €2.000 | 54 / 27 | 33 | -€8,25 | -€535,38 | - |
| €5.000 | 54 / 27 | 33 | -€20,62 | -€1.338,37 | - |

Bij €100 tot €200 telt een moment alleen als de minimale bedragen bekend zijn en eronder liggen. Vanaf €500 telt onbekend mee (de minima liggen meestal tussen €1 en €10, GEZIEN in de API's).

Vergund bij B betekent: perp- en spotbeurs hebben een MiCA-vergunning voor spot. Of de EU-dochter perps aan Nederlandse particulieren geeft, is niet nagekeken (GOK: vaak niet of beperkt). De opschaling is lineair (GOK): bij een dunne perp (weinig handel per dag) kost een grotere order meer dan de laatste prijs, dat meten we niet.

## C. Stablecoins

**C1, tussen beurzen** (dezelfde stablecoin goedkoper kopen dan elders verkopen, na alle kosten): 32 momenten, waarvan **0 echt**.

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

**C2, los van de koppeling** (boek minstens 0,3% van 1 dollar of 1 euro): 22 momenten, waarvan 16 met minstens €100 op het boek (de rest is een dode markt); daarvan na 2 keer takerkosten nog winst: 8; na kosten nog minstens 0,3%: **8**. Geen arbitrage: je wint alleen als de koers terugkomt (GOK dat hij dat doet; bij USDC in maart 2023 kwam hij terug, bij UST in 2022 niet).

Meest gezien: EURQ-USDT op bitfinex (goedkoop) 2x, EURQ-EUR op bitfinex (goedkoop) 2x, FDUSD-USDT op mexc (goedkoop) 2x, EURQ-EUR op kraken (goedkoop) 2x, EURQ-USD op kraken (goedkoop) 2x, EURQ-USDT op xt (goedkoop) 2x, FDUSD-USDT op xt (goedkoop) 2x, FDUSD-USDT op gate (goedkoop) 2x.

**C2 met winst na kosten, per dag**

| Dag | Aantal (alle / MiCA / grijs) | Mediane winst bij €500 | Mediane duur |
|---|---|---|---|
| 2026-11-19 | 8 / 2 / 6 | €3,86 | 10 min |

| Inleg | Kan meedoen (alle / MiCA) | Minimum onbekend | Mediane winst per keer | Som gemeten | Per week (GOK) |
|---|---|---|---|---|---|
| €100 | 6 / 2 | 2 | €0,77 | €7,36 | - |
| €150 | 6 / 2 | 2 | €1,16 | €11,01 | - |
| €200 | 6 / 2 | 2 | €1,55 | €14,66 | - |
| €500 | 8 / 2 | 2 | €3,86 | €43,62 | - |
| €2.000 | 8 / 2 | 2 | €6,56 | €63,16 | - |
| €5.000 | 8 / 2 | 2 | €8,30 | €70,09 | - |

Bij €100 tot €200 telt een moment alleen als de minimale bedragen bekend zijn en eronder liggen. Vanaf €500 telt onbekend mee (de minima liggen meestal tussen €1 en €10, GEZIEN in de API's).

## Hoe eerlijk is de opschaling naar €2.000 en €5.000

- A en C1: de winst bij €2.000 en €5.000 komt uit het echte orderboek op dat moment (dieper in het boek is duurder). Maar je hebt voorraad op beide beurzen nodig, of je moet overmaken, en dan is het gat vaak weg.
- B: lineair opgeschaald, alleen begrensd door de minimale order. GOK.
- C2: uit het boek, maar het is een gok op terugkeer, geen arbitrage.
- Per week = som gemeten maal 168 uur gedeeld door de gemeten uren. Na een paar uur meten is dat een ruwe GOK; na 7 dagen een week aan metingen.
- Kleine inleg: vaste kosten per keer (opnamekosten van de munt) wegen bij €100 zwaar; die zitten in de winst bij A en C1.

