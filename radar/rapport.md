# Kansenradar: rapport

Gemaakt 2026-11-27 02:38 UTC. Gemeten: **171,8 uur** in 36 run(s). Cijfers zijn GEZIEN (eigen metingen uit openbare API's), behalve waar GOK staat. Uitleg: `onderzoek/ai-handel/radar/README.md`.

## Het antwoord tot nu toe

- **A, nieuwe noteringen:** 66 nieuwe munten gezien, 43 echte prijsverschillen daarna; met één pot van €150 had je 19 keer kunnen instappen, samen €22,05.
- **B, funding-pieken:** 6404 pieken afgerond met spot en perp, waarvan 297 met winst na alle kosten bij €150; met één pot van €150 had je 33 keer kunnen instappen, samen -€11,89 (van €150 gaat €100 in de positie, GOK).
- **C1, stablecoin tussen beurzen:** 1011 echte momenten; met één pot van €150 had je 202 keer kunnen instappen, samen -€32,81.
- **C2, stablecoin naast zijn gewone prijs:** 917 momenten met winst na kosten; met één pot van €150 had je 213 keer kunnen instappen, samen €53,73. Dit is geen arbitrage: je wint alleen als de koers terugkomt.

Alle sommen zijn een **bovengrens (GOK)**: we kijken elke 15 seconden tot 3 minuten, snelle partijen elke milliseconde. Wat we zien, is vaak al deels weg voor een gewone gebruiker zijn order plaatst. Apart gezet en niet geteld: 823 regels uit de eerste uren (oude code of het oude Kraken-tarief, zie onderaan).

## A. Nieuwe noteringen

Nieuwe munten op een beurs: **66** (waarvan 2 bij de eerste vergelijking na de start: die kunnen in het gat tussen twee runs genoteerd zijn); 41 stonden al op een andere beurs met dezelfde quote. Prijsverschillen daarna: 357, waarvan **43 echt**.

| Tijd | Beurs | Munt | Al op | Opnemen / storten op de nieuwe beurs |
|---|---|---|---|---|
| 11-26 06:56 | mexc (grijs) | VERITY-USDT | - | onbekend / onbekend |
| 11-26 08:02 | kucoin | VERITY-USDT | mexc, bingx | dicht / open |
| 11-26 08:02 | poloniex (grijs) | ANT-USDT | - | dicht / open |
| 11-26 08:02 | poloniex (grijs) | AVGO-USDT | - | dicht / open |
| 11-26 08:02 | poloniex (grijs) | BMNR-USDT | - | dicht / open |
| 11-26 08:02 | poloniex (grijs) | BNC-USDT | gate, bingx | dicht / open |
| 11-26 08:02 | poloniex (grijs) | COIN-USDT | - | dicht / open |
| 11-26 08:02 | bingx | VERITY-USDT | kucoin, mexc | onbekend / onbekend |
| 11-26 10:01 | htx (grijs) | ANT-USDT | poloniex | dicht / open |
| 11-26 10:01 | htx (grijs) | AVGO-USDT | poloniex | dicht / open |
| 11-26 10:01 | htx (grijs) | BMNR-USDT | poloniex | dicht / open |
| 11-26 10:01 | htx (grijs) | BNC-USDT | gate, bingx, poloniex | dicht / open |
| 11-26 10:01 | htx (grijs) | COIN-USDT | poloniex | dicht / open |
| 11-26 11:01 | htx (grijs) | IRYS-USDT | bitget, gate, kucoin, mexc, okx, bingx, poloniex, xt | dicht / open |
| 11-26 12:01 | gate | ETNM-USDT | - | dicht / open |

**Echte momenten A, per dag**

| Dag | Aantal (alle / MiCA / grijs) | Mediane winst bij €500 | Mediane duur |
|---|---|---|---|
| 2026-11-25 | 43 / 0 / 43 | €0,98 | 3 min |

| Inleg | Kan meedoen (alle / MiCA) | Minimum onbekend | Tegelijk open (hoogst) | Met één pot gepakt | Mediane winst per keer | Winst met één pot | Per week (GOK) |
|---|---|---|---|---|---|---|---|
| €100 | 27 / 0 | 16 | 2 | 19 | €0,80 | €16,66 | €16,30 |
| €150 | 27 / 0 | 16 | 2 | 19 | €1,04 | €22,05 | €21,57 |
| €200 | 27 / 0 | 16 | 2 | 19 | €1,04 | €22,46 | €21,97 |
| €500 | 43 / 0 | 16 | 3 | 19 | €1,04 | €23,84 | €23,32 |
| €2.000 | 43 / 0 | 16 | 3 | 19 | €1,04 | €23,84 | €23,32 |
| €5.000 | 43 / 0 | 16 | 3 | 19 | €1,04 | €23,84 | €23,32 |

Met één pot: je pakt een moment als je geld vrij is, bij gelijke start het beste. "Tegelijk open" zegt hoeveel potten je nodig had om alles te pakken. Bij €100 tot €200 doet een moment alleen mee als de minimale bedragen bekend zijn en eronder liggen; vanaf €500 telt onbekend mee (meestal €1 tot €10).

## B. Funding-pieken

Positieve pieken (boven 0,1% per 8 uur, uit onder 0,05% na minstens één verrekening): **6404 afgerond en te rekenen**. Verder: spotkoers onbekend 0, andere munt met dezelfde naam 272, geen spotmarkt 3203, onderbroken door een te lang gat tussen runs 0; negatieve pieken 13073 (dan moet je spot shorten, dat kan een particulier meestal niet). Open pieken gaan mee naar de volgende run, dus een piek betaalt maar één keer de kosten.

Som per piek: verrekende funding, min 4 keer takerkosten (spot in en uit, perp in en uit), plus of min het prijsverschil tussen spot en perp, min één keer overmaken (opname van USDT of USDC) als spot en perp op twee beurzen zitten. Inleg = 2/3 spot en 1/3 onderpand voor de short bij 2x hefboom (GOK). Bij 2x kan een sprong van ±50% de short liquideren; dat zit niet in de som.

| Begin | Perp | Munt | Spot | Hoogste funding per 8 uur | Ontvangen funding | Kosten | Prijsverschil | Overmaken | Netto | Winst bij €150 | Duur | Handel per dag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 11-24 12:40 | hyperliquid | ACE | mexc | 4,00% | 8,35% (18 keer) | 0,19% | 12,03% | €0,01 | **20,19%** | €20,18 | 17,5 uur | $2,9 mln |
| 11-25 10:00 | gate | GUA | gate | 0,23% | 0,06% (1 keer) | 0,55% | 9,98% | €0,00 | **9,49%** | €9,49 | 2,1 uur | $4,4 mln |
| 11-20 16:08 | kraken | MNT | kraken | 4,00% | 7,22% (15 keer) | 1,70% | 2,71% | €0,00 | **8,23%** | €8,23 | 15,1 uur | $0,0 mln |
| 11-23 13:16 | gate | 牛逼 | mexc | 0,17% | 0,00% (1 keer) | 0,31% | 7,33% | €0,01 | **7,02%** | €7,01 | 62 min | $0,1 mln |
| 11-21 14:02 | kucoin | SPORTFUN | bingx | 0,24% | 0,05% (1 keer) | 0,32% | 6,74% | €0,01 | **6,48%** | €6,47 | 2,6 uur | $0,0 mln |
| 11-21 01:20 | kucoin | SPORTFUN | bingx | 2,10% | 1,05% (1 keer) | 0,32% | 3,25% | €0,01 | **3,98%** | €3,97 | 6,0 uur | $0,0 mln |
| 11-26 22:05 | kraken | CSPR | kraken | 4,00% | 0,50% (1 keer) | 1,70% | 5,11% | €0,00 | **3,91%** | €3,91 | 72 min | $0,0 mln |
| 11-21 06:09 | kraken | AGLD | mexc | 0,54% | 0,01% (1 keer) | 0,26% | 4,12% | €0,01 | **3,87%** | €3,86 | 52 min | $0,0 mln |
| 11-21 06:17 | kraken | BB | mexc | 0,32% | 0,01% (1 keer) | 0,20% | 3,81% | €0,01 | **3,62%** | €3,61 | 52 min | $0,0 mln |
| 11-23 13:06 | kraken | IOTX | mexc | 0,11% | 0,01% (1 keer) | 0,20% | 3,79% | €0,01 | **3,60%** | €3,59 | 72 min | $0,0 mln |

**Afgeronde pieken B, per dag**

| Dag | Aantal (alle / MiCA / grijs) | Mediane winst bij €500 | Mediane duur |
|---|---|---|---|
| 2026-11-19 | 231 / 127 / 104 | -€3,28 | 74 min |
| 2026-11-20 | 910 / 562 / 348 | -€3,57 | 94 min |
| 2026-11-21 | 910 / 565 / 345 | -€3,87 | 64 min |
| 2026-11-22 | 876 / 573 / 303 | -€3,55 | 2,1 uur |
| 2026-11-23 | 924 / 570 / 354 | -€3,82 | 60 min |
| 2026-11-24 | 811 / 531 / 280 | -€3,58 | 92 min |
| 2026-11-25 | 849 / 552 / 297 | -€3,15 | 118 min |
| 2026-11-26 | 865 / 605 / 260 | -€3,58 | 84 min |
| 2026-11-27 | 28 / 12 / 16 | -€3,25 | 58 min |

| Inleg | Kan meedoen (alle / MiCA) | Minimum onbekend | Tegelijk open (hoogst) | Met één pot gepakt | Mediane winst per keer | Winst met één pot | Per week (GOK) |
|---|---|---|---|---|---|---|---|
| €100 | 2223 / 1910 | 4164 | 130 | 33 | -€0,29 | -€7,94 | -€7,77 |
| €150 | 2240 / 1923 | 4164 | 130 | 33 | -€0,43 | -€11,89 | -€11,63 |
| €200 | 2240 / 1923 | 4164 | 130 | 33 | -€0,57 | -€15,86 | -€15,51 |
| €500 | 6404 / 4097 | 4164 | 200 | 68 | -€1,36 | -€96,56 | -€94,45 |
| €2.000 | 6404 / 4097 | 4164 | 200 | 68 | -€5,44 | -€385,21 | -€376,78 |
| €5.000 | 6404 / 4097 | 4164 | 200 | 68 | -€13,60 | -€962,59 | -€941,53 |

Met één pot: je pakt een moment als je geld vrij is, bij gelijke start het beste. "Tegelijk open" zegt hoeveel potten je nodig had om alles te pakken. Bij €100 tot €200 doet een moment alleen mee als de minimale bedragen bekend zijn en eronder liggen; vanaf €500 telt onbekend mee (meestal €1 tot €10).

Vergund bij B: perp- en spotbeurs hebben een MiCA-vergunning voor spot. Of de EU-dochter perps aan Nederlandse particulieren geeft, is niet nagekeken (GOK, vaak niet of beperkt). De som is lineair in de inleg (GOK): bij een dunne perp kost een grotere order meer dan de laatste prijs.

## C. Stablecoins

**C1, tussen beurzen** (dezelfde stablecoin goedkoper kopen dan elders verkopen, na alle kosten): 4118 momenten, waarvan **1011 echt**.

**Echte momenten C1, per dag**

| Dag | Aantal (alle / MiCA / grijs) | Mediane winst bij €500 | Mediane duur |
|---|---|---|---|
| 2026-11-20 | 173 / 99 / 74 | €0,03 | 2 min |
| 2026-11-21 | 188 / 109 / 79 | €0,04 | 3 min |
| 2026-11-22 | 189 / 0 / 189 | €0,11 | 1 min |
| 2026-11-23 | 37 / 0 / 37 | €0,05 | 1 min |
| 2026-11-24 | 75 / 1 / 74 | €0,03 | 45 s |
| 2026-11-25 | 140 / 0 / 140 | €0,02 | 2 min |
| 2026-11-26 | 190 / 0 / 190 | €0,03 | 2 min |
| 2026-11-27 | 19 / 0 / 19 | -€0,01 | 2 min |

| Inleg | Kan meedoen (alle / MiCA) | Minimum onbekend | Tegelijk open (hoogst) | Met één pot gepakt | Mediane winst per keer | Winst met één pot | Per week (GOK) |
|---|---|---|---|---|---|---|---|
| €100 | 467 / 39 | 544 | 3 | 202 | -€0,00 | -€41,36 | -€40,45 |
| €150 | 467 / 39 | 544 | 3 | 202 | €0,01 | -€32,81 | -€32,10 |
| €200 | 467 / 39 | 544 | 3 | 202 | €0,02 | -€24,32 | -€23,79 |
| €500 | 1011 / 209 | 544 | 9 | 230 | €0,08 | €34,62 | €33,86 |
| €2.000 | 1011 / 209 | 544 | 9 | 230 | €0,29 | €172,40 | €168,63 |
| €5.000 | 1011 / 209 | 544 | 9 | 230 | €0,37 | €338,64 | €331,23 |

Met één pot: je pakt een moment als je geld vrij is, bij gelijke start het beste. "Tegelijk open" zegt hoeveel potten je nodig had om alles te pakken. Bij €100 tot €200 doet een moment alleen mee als de minimale bedragen bekend zijn en eronder liggen; vanaf €500 telt onbekend mee (meestal €1 tot €10).

**C2, naast de gewone prijs** (minstens 0,3% naast de basislijn: de mediaan per dag over de laatste 45 dagen): 2098 momenten met basislijn, waarvan 1612 met minstens €100 op het boek en **917 met winst na 2 keer takerkosten** (bij de eerste meting). Zonder basislijn (munt te nieuw of geen bron, niet geteld): 33. Geen arbitrage: je wint alleen als de koers naar zijn gewone prijs terugkomt (GOK).

Meest gezien: USDQ-USD op kraken (duur) 495 keer, EURQ-EUR op kraken (duur) 255 keer, EURQ-USD op kraken (duur) 210 keer, USDC-USD op bitfinex (duur) 170 keer, USDT-EUR op bitget (duur) 168 keer, USDT-EUR op kucoin (duur) 130 keer, USDC-EUR op bitget (duur) 47 keer, EURQ-USDT op xt (goedkoop) 39 keer.

**C2 met winst na kosten, per dag**

| Dag | Aantal (alle / MiCA / grijs) | Mediane winst bij €500 | Mediane duur |
|---|---|---|---|
| 2026-11-19 | 5 / 4 / 1 | €0,81 | 5 min |
| 2026-11-20 | 167 / 97 / 70 | €0,59 | 45 s |
| 2026-11-21 | 313 / 99 / 214 | €1,54 | 15 s |
| 2026-11-22 | 100 / 77 / 23 | €0,11 | 4 min |
| 2026-11-23 | 46 / 40 / 6 | €0,07 | 11 min |
| 2026-11-24 | 31 / 25 / 6 | €0,41 | 4 min |
| 2026-11-25 | 162 / 144 / 18 | €0,18 | 1 min |
| 2026-11-26 | 83 / 17 / 66 | €0,50 | 2 min |
| 2026-11-27 | 10 / 0 / 10 | €0,51 | 3 min |

| Inleg | Kan meedoen (alle / MiCA) | Minimum onbekend | Tegelijk open (hoogst) | Met één pot gepakt | Mediane winst per keer | Winst met één pot | Per week (GOK) |
|---|---|---|---|---|---|---|---|
| €100 | 913 / 503 | 4 | 8 | 218 | €0,10 | €38,60 | €37,76 |
| €150 | 913 / 503 | 4 | 8 | 213 | €0,15 | €53,73 | €52,56 |
| €200 | 913 / 503 | 4 | 8 | 231 | €0,20 | €68,24 | €66,75 |
| €500 | 917 / 503 | 4 | 8 | 231 | €0,50 | €137,62 | €134,61 |
| €2.000 | 917 / 503 | 4 | 8 | 219 | €1,96 | €443,32 | €433,62 |
| €5.000 | 917 / 503 | 4 | 8 | 220 | €4,21 | €913,59 | €893,60 |

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

