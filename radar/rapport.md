# Kansenradar: rapport

Gemaakt 2026-11-23 08:56 UTC. Gemeten: **85,6 uur** in 21 run(s). Cijfers zijn GEZIEN (eigen metingen uit openbare API's), behalve waar GOK staat. Uitleg: `onderzoek/ai-handel/radar/README.md`.

## Het antwoord tot nu toe

- **A, nieuwe noteringen:** 32 nieuwe munten gezien, 0 echte prijsverschillen daarna; met één pot van €150 had je hier tot nu toe niets kunnen pakken.
- **B, funding-pieken:** 3275 pieken afgerond met spot en perp, waarvan 177 met winst na alle kosten bij €150; met één pot van €150 had je 12 keer kunnen instappen, samen -€3,44 (van €150 gaat €100 in de positie, GOK).
- **C1, stablecoin tussen beurzen:** 553 echte momenten; met één pot van €150 had je 67 keer kunnen instappen, samen -€32,32.
- **C2, stablecoin naast zijn gewone prijs:** 616 momenten met winst na kosten; met één pot van €150 had je 133 keer kunnen instappen, samen €29,41. Dit is geen arbitrage: je wint alleen als de koers terugkomt.

Alle sommen zijn een **bovengrens (GOK)**: we kijken elke 15 seconden tot 3 minuten, snelle partijen elke milliseconde. Wat we zien, is vaak al deels weg voor een gewone gebruiker zijn order plaatst. Apart gezet en niet geteld: 823 regels uit de eerste uren (oude code of het oude Kraken-tarief, zie onderaan).

## A. Nieuwe noteringen

Nieuwe munten op een beurs: **32** (waarvan 0 bij de eerste vergelijking na de start: die kunnen in het gat tussen twee runs genoteerd zijn); 19 stonden al op een andere beurs met dezelfde quote. Prijsverschillen daarna: 14, waarvan **0 echt**.

| Tijd | Beurs | Munt | Al op | Opnemen / storten op de nieuwe beurs |
|---|---|---|---|---|
| 11-20 11:19 | mexc (grijs) | ANTON-USDT | gate | onbekend / onbekend |
| 11-20 11:19 | mexc (grijs) | ANTX-USDT | gate, bingx | onbekend / onbekend |
| 11-20 12:01 | poloniex (grijs) | PIEVERSE-USDT | gate, kucoin, mexc, bingx | dicht / open |
| 11-20 12:31 | poloniex (grijs) | VVV-USDT | gate, kucoin, mexc, okx, bingx | dicht / open |
| 11-20 13:01 | htx (grijs) | PIEVERSE-USDT | gate, kucoin, mexc, bingx, poloniex | dicht / open |
| 11-20 13:31 | htx (grijs) | VVV-USDT | gate, kucoin, mexc, okx, bingx, poloniex | dicht / open |
| 11-20 14:01 | bitget (grijs) | CLEAR-USDT | mexc | open / open |
| 11-20 14:31 | kucoin | ANTX-USDT | gate, mexc, bingx | dicht / open |
| 11-20 15:04 | kraken | BFI-USD | - | open / open |
| 11-22 04:09 | mexc (grijs) | RINGS-USDT | - | onbekend / onbekend |
| 11-23 05:02 | poloniex (grijs) | SNDK-USDT | - | dicht / dicht |
| 11-23 05:32 | poloniex (grijs) | MU-USDT | - | dicht / open |
| 11-23 07:32 | htx (grijs) | MU-USDT | poloniex | dicht / open |
| 11-23 08:02 | kucoin | CLEAR-USDT | bitget, gate, mexc | dicht / open |
| 11-23 08:02 | gate | CLEAR-USDT | bitget, kucoin, mexc | dicht / open |

**Echte momenten A, per dag:** nog geen momenten.

| Inleg | Kan meedoen (alle / MiCA) | Minimum onbekend | Tegelijk open (hoogst) | Met één pot gepakt | Mediane winst per keer | Winst met één pot | Per week (GOK) |
|---|---|---|---|---|---|---|---|
| €100 | 0 / 0 | 0 | 0 | 0 | - | €0,00 | €0,00 |
| €150 | 0 / 0 | 0 | 0 | 0 | - | €0,00 | €0,00 |
| €200 | 0 / 0 | 0 | 0 | 0 | - | €0,00 | €0,00 |
| €500 | 0 / 0 | 0 | 0 | 0 | - | €0,00 | €0,00 |
| €2.000 | 0 / 0 | 0 | 0 | 0 | - | €0,00 | €0,00 |
| €5.000 | 0 / 0 | 0 | 0 | 0 | - | €0,00 | €0,00 |

Met één pot: je pakt een moment als je geld vrij is, bij gelijke start het beste. "Tegelijk open" zegt hoeveel potten je nodig had om alles te pakken. Bij €100 tot €200 doet een moment alleen mee als de minimale bedragen bekend zijn en eronder liggen; vanaf €500 telt onbekend mee (meestal €1 tot €10).

## B. Funding-pieken

Positieve pieken (boven 0,1% per 8 uur, uit onder 0,05% na minstens één verrekening): **3275 afgerond en te rekenen**. Verder: spotkoers onbekend 0, andere munt met dezelfde naam 127, geen spotmarkt 1479, onderbroken door een te lang gat tussen runs 0; negatieve pieken 7055 (dan moet je spot shorten, dat kan een particulier meestal niet). Open pieken gaan mee naar de volgende run, dus een piek betaalt maar één keer de kosten.

Som per piek: verrekende funding, min 4 keer takerkosten (spot in en uit, perp in en uit), plus of min het prijsverschil tussen spot en perp, min één keer overmaken (opname van USDT of USDC) als spot en perp op twee beurzen zitten. Inleg = 2/3 spot en 1/3 onderpand voor de short bij 2x hefboom (GOK). Bij 2x kan een sprong van ±50% de short liquideren; dat zit niet in de som.

| Begin | Perp | Munt | Spot | Hoogste funding per 8 uur | Ontvangen funding | Kosten | Prijsverschil | Overmaken | Netto | Winst bij €150 | Duur | Handel per dag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 11-20 16:08 | kraken | MNT | kraken | 4,00% | 7,22% (15 keer) | 1,70% | 2,71% | €0,00 | **8,23%** | €8,23 | 15,1 uur | $0,0 mln |
| 11-21 14:02 | kucoin | SPORTFUN | bingx | 0,24% | 0,05% (1 keer) | 0,32% | 6,74% | €0,01 | **6,48%** | €6,47 | 2,6 uur | $0,0 mln |
| 11-21 01:20 | kucoin | SPORTFUN | bingx | 2,10% | 1,05% (1 keer) | 0,32% | 3,25% | €0,01 | **3,98%** | €3,97 | 6,0 uur | $0,0 mln |
| 11-21 06:09 | kraken | AGLD | mexc | 0,54% | 0,01% (1 keer) | 0,26% | 4,12% | €0,01 | **3,87%** | €3,86 | 52 min | $0,0 mln |
| 11-21 06:17 | kraken | BB | mexc | 0,32% | 0,01% (1 keer) | 0,20% | 3,81% | €0,01 | **3,62%** | €3,61 | 52 min | $0,0 mln |
| 11-21 06:09 | kraken | PIXEL | mexc | 0,17% | 0,01% (1 keer) | 0,20% | 3,54% | €0,01 | **3,35%** | €3,34 | 58 min | $0,0 mln |
| 11-23 04:44 | kraken | AGLD | mexc | 4,00% | 1,09% (3 keer) | 0,26% | 2,10% | €0,01 | **2,94%** | €2,93 | 2,4 uur | $0,0 mln |
| 11-20 18:12 | kraken | BRETT | bingx | 0,11% | 0,00% (1 keer) | 0,30% | 3,18% | €0,01 | **2,88%** | €2,87 | 48 min | $0,0 mln |
| 11-22 22:24 | kraken | BB | mexc | 4,00% | 2,51% (6 keer) | 0,20% | 0,41% | €0,01 | **2,71%** | €2,70 | 5,6 uur | $0,0 mln |
| 11-19 19:03 | kraken | TREAD | kraken | 4,00% | -0,40% (1 keer) | 1,70% | 4,73% | €0,00 | **2,62%** | €2,62 | 90 min | $0,0 mln |

**Afgeronde pieken B, per dag**

| Dag | Aantal (alle / MiCA / grijs) | Mediane winst bij €500 | Mediane duur |
|---|---|---|---|
| 2026-11-19 | 231 / 127 / 104 | -€3,28 | 74 min |
| 2026-11-20 | 910 / 562 / 348 | -€3,57 | 94 min |
| 2026-11-21 | 910 / 565 / 345 | -€3,87 | 64 min |
| 2026-11-22 | 871 / 571 / 300 | -€3,57 | 2,0 uur |
| 2026-11-23 | 353 / 217 / 136 | -€3,95 | 58 min |

| Inleg | Kan meedoen (alle / MiCA) | Minimum onbekend | Tegelijk open (hoogst) | Met één pot gepakt | Mediane winst per keer | Winst met één pot | Per week (GOK) |
|---|---|---|---|---|---|---|---|
| €100 | 1092 / 896 | 2180 | 125 | 12 | -€0,28 | -€2,30 | -€4,51 |
| €150 | 1095 / 896 | 2180 | 125 | 12 | -€0,42 | -€3,44 | -€6,75 |
| €200 | 1095 / 896 | 2180 | 125 | 12 | -€0,55 | -€4,56 | -€8,95 |
| €500 | 3275 / 2042 | 2180 | 181 | 34 | -€1,35 | -€50,86 | -€99,80 |
| €2.000 | 3275 / 2042 | 2180 | 181 | 34 | -€5,39 | -€202,83 | -€398,00 |
| €5.000 | 3275 / 2042 | 2180 | 181 | 34 | -€13,47 | -€506,78 | -€994,43 |

Met één pot: je pakt een moment als je geld vrij is, bij gelijke start het beste. "Tegelijk open" zegt hoeveel potten je nodig had om alles te pakken. Bij €100 tot €200 doet een moment alleen mee als de minimale bedragen bekend zijn en eronder liggen; vanaf €500 telt onbekend mee (meestal €1 tot €10).

Vergund bij B: perp- en spotbeurs hebben een MiCA-vergunning voor spot. Of de EU-dochter perps aan Nederlandse particulieren geeft, is niet nagekeken (GOK, vaak niet of beperkt). De som is lineair in de inleg (GOK): bij een dunne perp kost een grotere order meer dan de laatste prijs.

## C. Stablecoins

**C1, tussen beurzen** (dezelfde stablecoin goedkoper kopen dan elders verkopen, na alle kosten): 2587 momenten, waarvan **553 echt**.

**Echte momenten C1, per dag**

| Dag | Aantal (alle / MiCA / grijs) | Mediane winst bij €500 | Mediane duur |
|---|---|---|---|
| 2026-11-20 | 173 / 99 / 74 | €0,03 | 2 min |
| 2026-11-21 | 188 / 109 / 79 | €0,04 | 3 min |
| 2026-11-22 | 189 / 0 / 189 | €0,11 | 1 min |
| 2026-11-23 | 3 / 0 / 3 | €0,03 | 30 s |

| Inleg | Kan meedoen (alle / MiCA) | Minimum onbekend | Tegelijk open (hoogst) | Met één pot gepakt | Mediane winst per keer | Winst met één pot | Per week (GOK) |
|---|---|---|---|---|---|---|---|
| €100 | 139 / 39 | 414 | 3 | 67 | -€0,90 | -€37,78 | -€74,13 |
| €150 | 139 / 39 | 414 | 3 | 67 | -€0,85 | -€32,32 | -€63,42 |
| €200 | 139 / 39 | 414 | 3 | 67 | -€0,79 | -€26,88 | -€52,74 |
| €500 | 553 / 208 | 414 | 9 | 101 | €0,05 | €16,58 | €32,53 |
| €2.000 | 553 / 208 | 414 | 9 | 101 | €0,32 | €93,45 | €183,36 |
| €5.000 | 553 / 208 | 414 | 9 | 101 | €0,40 | €185,93 | €364,84 |

Met één pot: je pakt een moment als je geld vrij is, bij gelijke start het beste. "Tegelijk open" zegt hoeveel potten je nodig had om alles te pakken. Bij €100 tot €200 doet een moment alleen mee als de minimale bedragen bekend zijn en eronder liggen; vanaf €500 telt onbekend mee (meestal €1 tot €10).

**C2, naast de gewone prijs** (minstens 0,3% naast de basislijn: de mediaan per dag over de laatste 45 dagen): 1127 momenten met basislijn, waarvan 755 met minstens €100 op het boek en **616 met winst na 2 keer takerkosten** (bij de eerste meting). Zonder basislijn (munt te nieuw of geen bron, niet geteld): 17. Geen arbitrage: je wint alleen als de koers naar zijn gewone prijs terugkomt (GOK).

Meest gezien: EURQ-EUR op kraken (duur) 214 keer, USDC-USD op bitfinex (duur) 170 keer, USDT-EUR op kucoin (duur) 130 keer, USDT-EUR op bitget (duur) 79 keer, USDC-EUR op bitget (duur) 46 keer, USDQ-USD op kraken (duur) 32 keer, TUSD-USDT op kucoin (goedkoop) 27 keer, USDC-EUR op kucoin (duur) 17 keer.

**C2 met winst na kosten, per dag**

| Dag | Aantal (alle / MiCA / grijs) | Mediane winst bij €500 | Mediane duur |
|---|---|---|---|
| 2026-11-19 | 5 / 4 / 1 | €0,81 | 5 min |
| 2026-11-20 | 167 / 97 / 70 | €0,59 | 45 s |
| 2026-11-21 | 313 / 99 / 214 | €1,54 | 15 s |
| 2026-11-22 | 100 / 77 / 23 | €0,11 | 4 min |
| 2026-11-23 | 31 / 28 / 3 | €0,02 | 4 min |

| Inleg | Kan meedoen (alle / MiCA) | Minimum onbekend | Tegelijk open (hoogst) | Met één pot gepakt | Mediane winst per keer | Winst met één pot | Per week (GOK) |
|---|---|---|---|---|---|---|---|
| €100 | 615 / 305 | 1 | 8 | 138 | €0,11 | €20,22 | €39,68 |
| €150 | 615 / 305 | 1 | 8 | 133 | €0,16 | €29,41 | €57,71 |
| €200 | 615 / 305 | 1 | 8 | 133 | €0,20 | €36,20 | €71,03 |
| €500 | 616 / 305 | 1 | 8 | 133 | €0,50 | €75,72 | €148,57 |
| €2.000 | 616 / 305 | 1 | 8 | 120 | €1,93 | €242,23 | €475,33 |
| €5.000 | 616 / 305 | 1 | 8 | 121 | €2,44 | €472,54 | €927,25 |

Met één pot: je pakt een moment als je geld vrij is, bij gelijke start het beste. "Tegelijk open" zegt hoeveel potten je nodig had om alles te pakken. Bij €100 tot €200 doet een moment alleen mee als de minimale bedragen bekend zijn en eronder liggen; vanaf €500 telt onbekend mee (meestal €1 tot €10).

## Apart gezet (niet in de sommen)

- Oude Kraken-tarief (0,40% gerekend waar het 0,80% is, of 0,40/0,80% op een stablecoin-paar waar het 0,20% is): A 0, B 0, C1 0, C2 0.
- Funding-pieken uit de eerste code (doorgeknipt bij het einde van een run, zonder overmaken): 790 (waarvan 153 positief), waarvan 789 doorgeknipt. Die zijn niet na te rekenen (de rest van de piek is niet gevolgd) en tellen niet mee.
- C2 uit de eerste code (gemeten tegen 1 dollar of 1 euro, zonder basislijn; vooral EURQ, die al weken rond 0,97 euro staat): 33.

## Hoe eerlijk zijn de sommen

- A en C1: de winst bij elke inleg komt uit het echte orderboek op dat moment. Je hebt wel voorraad op beide beurzen nodig, of je moet overmaken, en dan is het gat vaak weg.
- B: lineair in de inleg, met de vaste kosten van overmaken. Bij €100 tot €200 wegen die zwaar.
- C2: uit het boek, maar een gok op terugkeer naar de gewone prijs.
- Per week = winst met één pot maal 168 uur gedeeld door de gemeten uren (pas vanaf 3 uur). Na een paar uur is dat een ruwe GOK; na 7 dagen een week aan metingen.

