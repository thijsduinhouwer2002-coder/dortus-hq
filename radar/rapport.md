# Kansenradar: rapport

Gemaakt 2026-11-27 18:29 UTC. Gemeten: **187,2 uur** in 39 run(s). Cijfers zijn GEZIEN (eigen metingen uit openbare API's), behalve waar GOK staat. Uitleg: `onderzoek/ai-handel/radar/README.md`.

## Het antwoord tot nu toe

- **A, nieuwe noteringen:** 101 nieuwe munten gezien, 43 echte prijsverschillen daarna; met één pot van €150 had je 19 keer kunnen instappen, samen €22,05.
- **B, funding-pieken:** 7086 pieken afgerond met spot en perp, waarvan 314 met winst na alle kosten bij €150; met één pot van €150 had je 37 keer kunnen instappen, samen -€15,45 (van €150 gaat €100 in de positie, GOK).
- **C1, stablecoin tussen beurzen:** 1079 echte momenten; met één pot van €150 had je 213 keer kunnen instappen, samen -€32,30.
- **C2, stablecoin naast zijn gewone prijs:** 939 momenten met winst na kosten; met één pot van €150 had je 220 keer kunnen instappen, samen €57,55. Dit is geen arbitrage: je wint alleen als de koers terugkomt.

Alle sommen zijn een **bovengrens (GOK)**: we kijken elke 15 seconden tot 3 minuten, snelle partijen elke milliseconde. Wat we zien, is vaak al deels weg voor een gewone gebruiker zijn order plaatst. Apart gezet en niet geteld: 823 regels uit de eerste uren (oude code of het oude Kraken-tarief, zie onderaan).

## A. Nieuwe noteringen

Nieuwe munten op een beurs: **101** (waarvan 2 bij de eerste vergelijking na de start: die kunnen in het gat tussen twee runs genoteerd zijn); 60 stonden al op een andere beurs met dezelfde quote. Prijsverschillen daarna: 358, waarvan **43 echt**.

| Tijd | Beurs | Munt | Al op | Opnemen / storten op de nieuwe beurs |
|---|---|---|---|---|
| 11-27 08:00 | htx (grijs) | APP-USDT | poloniex | dicht / open |
| 11-27 08:00 | htx (grijs) | BABA-USDT | poloniex | dicht / open |
| 11-27 08:00 | htx (grijs) | DRAM-USDT | poloniex | dicht / open |
| 11-27 08:00 | htx (grijs) | EWY-USDT | poloniex | dicht / open |
| 11-27 08:00 | htx (grijs) | HOOD-USDT | poloniex | dicht / open |
| 11-27 08:00 | htx (grijs) | INTW-USDT | poloniex | dicht / open |
| 11-27 08:00 | htx (grijs) | LITE-USDT | poloniex | dicht / open |
| 11-27 08:00 | htx (grijs) | META-USDT | poloniex | dicht / open |
| 11-27 08:00 | htx (grijs) | MRVL-USDT | poloniex | dicht / open |
| 11-27 08:00 | htx (grijs) | MSFT-USDT | poloniex | dicht / open |
| 11-27 08:00 | htx (grijs) | ORCL-USDT | poloniex | dicht / open |
| 11-27 08:00 | htx (grijs) | PLTR-USDT | poloniex | dicht / open |
| 11-27 08:00 | htx (grijs) | SPY-USDT | poloniex, xt | dicht / open |
| 11-27 09:01 | kucoin | KNTQ-USDT | mexc | dicht / open |
| 11-27 10:01 | kucoin | GAIB-USDT | mexc, xt | dicht / open |

**Echte momenten A, per dag**

| Dag | Aantal (alle / MiCA / grijs) | Mediane winst bij €500 | Mediane duur |
|---|---|---|---|
| 2026-11-25 | 43 / 0 / 43 | €0,98 | 3 min |

| Inleg | Kan meedoen (alle / MiCA) | Minimum onbekend | Tegelijk open (hoogst) | Met één pot gepakt | Mediane winst per keer | Winst met één pot | Per week (GOK) |
|---|---|---|---|---|---|---|---|
| €100 | 27 / 0 | 16 | 2 | 19 | €0,80 | €16,66 | €14,95 |
| €150 | 27 / 0 | 16 | 2 | 19 | €1,04 | €22,05 | €19,79 |
| €200 | 27 / 0 | 16 | 2 | 19 | €1,04 | €22,46 | €20,16 |
| €500 | 43 / 0 | 16 | 3 | 19 | €1,04 | €23,84 | €21,39 |
| €2.000 | 43 / 0 | 16 | 3 | 19 | €1,04 | €23,84 | €21,39 |
| €5.000 | 43 / 0 | 16 | 3 | 19 | €1,04 | €23,84 | €21,39 |

Met één pot: je pakt een moment als je geld vrij is, bij gelijke start het beste. "Tegelijk open" zegt hoeveel potten je nodig had om alles te pakken. Bij €100 tot €200 doet een moment alleen mee als de minimale bedragen bekend zijn en eronder liggen; vanaf €500 telt onbekend mee (meestal €1 tot €10).

## B. Funding-pieken

Positieve pieken (boven 0,1% per 8 uur, uit onder 0,05% na minstens één verrekening): **7086 afgerond en te rekenen**. Verder: spotkoers onbekend 0, andere munt met dezelfde naam 298, geen spotmarkt 3426, onderbroken door een te lang gat tussen runs 0; negatieve pieken 13932 (dan moet je spot shorten, dat kan een particulier meestal niet). Open pieken gaan mee naar de volgende run, dus een piek betaalt maar één keer de kosten.

Som per piek: verrekende funding, min 4 keer takerkosten (spot in en uit, perp in en uit), plus of min het prijsverschil tussen spot en perp, min één keer overmaken (opname van USDT of USDC) als spot en perp op twee beurzen zitten. Inleg = 2/3 spot en 1/3 onderpand voor de short bij 2x hefboom (GOK). Bij 2x kan een sprong van ±50% de short liquideren; dat zit niet in de som.

| Begin | Perp | Munt | Spot | Hoogste funding per 8 uur | Ontvangen funding | Kosten | Prijsverschil | Overmaken | Netto | Winst bij €150 | Duur | Handel per dag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 11-24 12:40 | hyperliquid | ACE | mexc | 4,00% | 8,35% (18 keer) | 0,19% | 12,03% | €0,01 | **20,19%** | €20,18 | 17,5 uur | $2,9 mln |
| 11-25 10:00 | gate | GUA | gate | 0,23% | 0,06% (1 keer) | 0,55% | 9,98% | €0,00 | **9,49%** | €9,49 | 2,1 uur | $4,4 mln |
| 11-20 16:08 | kraken | MNT | kraken | 4,00% | 7,22% (15 keer) | 1,70% | 2,71% | €0,00 | **8,23%** | €8,23 | 15,1 uur | $0,0 mln |
| 11-23 13:16 | gate | 牛逼 | mexc | 0,17% | 0,00% (1 keer) | 0,31% | 7,33% | €0,01 | **7,02%** | €7,01 | 62 min | $0,1 mln |
| 11-27 12:35 | bingx | MONTRA | mexc | 0,16% | -0,02% (1 keer) | 0,26% | 6,91% | €0,01 | **6,63%** | €6,62 | 3,4 uur | $0,0 mln |
| 11-21 14:02 | kucoin | SPORTFUN | bingx | 0,24% | 0,05% (1 keer) | 0,32% | 6,74% | €0,01 | **6,48%** | €6,47 | 2,6 uur | $0,0 mln |
| 11-21 01:20 | kucoin | SPORTFUN | bingx | 2,10% | 1,05% (1 keer) | 0,32% | 3,25% | €0,01 | **3,98%** | €3,97 | 6,0 uur | $0,0 mln |
| 11-26 22:05 | kraken | CSPR | kraken | 4,00% | 0,50% (1 keer) | 1,70% | 5,11% | €0,00 | **3,91%** | €3,91 | 72 min | $0,0 mln |
| 11-21 06:09 | kraken | AGLD | mexc | 0,54% | 0,01% (1 keer) | 0,26% | 4,12% | €0,01 | **3,87%** | €3,86 | 52 min | $0,0 mln |
| 11-21 06:17 | kraken | BB | mexc | 0,32% | 0,01% (1 keer) | 0,20% | 3,81% | €0,01 | **3,62%** | €3,61 | 52 min | $0,0 mln |

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
| 2026-11-26 | 872 / 607 / 265 | -€3,56 | 89 min |
| 2026-11-27 | 703 / 444 / 259 | -€3,46 | 62 min |

| Inleg | Kan meedoen (alle / MiCA) | Minimum onbekend | Tegelijk open (hoogst) | Met één pot gepakt | Mediane winst per keer | Winst met één pot | Per week (GOK) |
|---|---|---|---|---|---|---|---|
| €100 | 2453 / 2113 | 4615 | 130 | 37 | -€0,30 | -€10,32 | -€9,26 |
| €150 | 2471 / 2127 | 4615 | 130 | 37 | -€0,46 | -€15,45 | -€13,87 |
| €200 | 2471 / 2127 | 4615 | 130 | 37 | -€0,61 | -€20,62 | -€18,51 |
| €500 | 7086 / 4531 | 4615 | 200 | 72 | -€1,42 | -€106,97 | -€96,01 |
| €2.000 | 7086 / 4531 | 4615 | 200 | 72 | -€5,64 | -€426,83 | -€383,10 |
| €5.000 | 7086 / 4531 | 4615 | 200 | 72 | -€14,11 | -€1.066,62 | -€957,33 |

Met één pot: je pakt een moment als je geld vrij is, bij gelijke start het beste. "Tegelijk open" zegt hoeveel potten je nodig had om alles te pakken. Bij €100 tot €200 doet een moment alleen mee als de minimale bedragen bekend zijn en eronder liggen; vanaf €500 telt onbekend mee (meestal €1 tot €10).

Vergund bij B: perp- en spotbeurs hebben een MiCA-vergunning voor spot. Of de EU-dochter perps aan Nederlandse particulieren geeft, is niet nagekeken (GOK, vaak niet of beperkt). De som is lineair in de inleg (GOK): bij een dunne perp kost een grotere order meer dan de laatste prijs.

## C. Stablecoins

**C1, tussen beurzen** (dezelfde stablecoin goedkoper kopen dan elders verkopen, na alle kosten): 4363 momenten, waarvan **1079 echt**.

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
| 2026-11-27 | 87 / 0 / 87 | €0,01 | 5 min |

| Inleg | Kan meedoen (alle / MiCA) | Minimum onbekend | Tegelijk open (hoogst) | Met één pot gepakt | Mediane winst per keer | Winst met één pot | Per week (GOK) |
|---|---|---|---|---|---|---|---|
| €100 | 514 / 39 | 565 | 3 | 213 | -€0,00 | -€41,07 | -€36,86 |
| €150 | 514 / 39 | 565 | 3 | 213 | €0,01 | -€32,30 | -€28,99 |
| €200 | 514 / 39 | 565 | 3 | 213 | €0,02 | -€23,57 | -€21,15 |
| €500 | 1079 / 209 | 565 | 9 | 241 | €0,08 | €36,61 | €32,86 |
| €2.000 | 1079 / 209 | 565 | 9 | 241 | €0,29 | €179,23 | €160,87 |
| €5.000 | 1079 / 209 | 565 | 9 | 241 | €0,34 | €351,91 | €315,86 |

Met één pot: je pakt een moment als je geld vrij is, bij gelijke start het beste. "Tegelijk open" zegt hoeveel potten je nodig had om alles te pakken. Bij €100 tot €200 doet een moment alleen mee als de minimale bedragen bekend zijn en eronder liggen; vanaf €500 telt onbekend mee (meestal €1 tot €10).

**C2, naast de gewone prijs** (minstens 0,3% naast de basislijn: de mediaan per dag over de laatste 45 dagen): 2202 momenten met basislijn, waarvan 1692 met minstens €100 op het boek en **939 met winst na 2 keer takerkosten** (bij de eerste meting). Zonder basislijn (munt te nieuw of geen bron, niet geteld): 35. Geen arbitrage: je wint alleen als de koers naar zijn gewone prijs terugkomt (GOK).

Meest gezien: USDQ-USD op kraken (duur) 531 keer, EURQ-EUR op kraken (duur) 257 keer, EURQ-USD op kraken (duur) 212 keer, USDT-EUR op bitget (duur) 180 keer, USDC-USD op bitfinex (duur) 170 keer, USDT-EUR op kucoin (duur) 130 keer, EURQ-USDT op xt (goedkoop) 62 keer, USDC-EUR op bitget (duur) 47 keer.

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
| 2026-11-27 | 32 / 8 / 24 | €0,51 | 3 min |

| Inleg | Kan meedoen (alle / MiCA) | Minimum onbekend | Tegelijk open (hoogst) | Met één pot gepakt | Mediane winst per keer | Winst met één pot | Per week (GOK) |
|---|---|---|---|---|---|---|---|
| €100 | 934 / 511 | 5 | 8 | 225 | €0,10 | €41,81 | €37,53 |
| €150 | 934 / 511 | 5 | 8 | 220 | €0,15 | €57,55 | €51,66 |
| €200 | 934 / 511 | 5 | 8 | 238 | €0,20 | €72,31 | €64,90 |
| €500 | 939 / 511 | 5 | 8 | 238 | €0,50 | €143,21 | €128,54 |
| €2.000 | 939 / 511 | 5 | 8 | 232 | €1,97 | €468,40 | €420,41 |
| €5.000 | 939 / 511 | 5 | 8 | 233 | €4,13 | €958,22 | €860,04 |

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

