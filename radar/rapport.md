# Kansenradar: rapport

Gemaakt 2026-11-24 22:08 UTC. Gemeten: **121,7 uur** in 27 run(s). Cijfers zijn GEZIEN (eigen metingen uit openbare API's), behalve waar GOK staat. Uitleg: `onderzoek/ai-handel/radar/README.md`.

## Het antwoord tot nu toe

- **A, nieuwe noteringen:** 46 nieuwe munten gezien, 0 echte prijsverschillen daarna; met één pot van €150 had je hier tot nu toe niets kunnen pakken.
- **B, funding-pieken:** 4570 pieken afgerond met spot en perp, waarvan 229 met winst na alle kosten bij €150; met één pot van €150 had je 21 keer kunnen instappen, samen -€6,58 (van €150 gaat €100 in de positie, GOK).
- **C1, stablecoin tussen beurzen:** 652 echte momenten; met één pot van €150 had je 149 keer kunnen instappen, samen -€34,52.
- **C2, stablecoin naast zijn gewone prijs:** 658 momenten met winst na kosten; met één pot van €150 had je 152 keer kunnen instappen, samen €41,37. Dit is geen arbitrage: je wint alleen als de koers terugkomt.

Alle sommen zijn een **bovengrens (GOK)**: we kijken elke 15 seconden tot 3 minuten, snelle partijen elke milliseconde. Wat we zien, is vaak al deels weg voor een gewone gebruiker zijn order plaatst. Apart gezet en niet geteld: 823 regels uit de eerste uren (oude code of het oude Kraken-tarief, zie onderaan).

## A. Nieuwe noteringen

Nieuwe munten op een beurs: **46** (waarvan 2 bij de eerste vergelijking na de start: die kunnen in het gat tussen twee runs genoteerd zijn); 29 stonden al op een andere beurs met dezelfde quote. Prijsverschillen daarna: 41, waarvan **0 echt**.

| Tijd | Beurs | Munt | Al op | Opnemen / storten op de nieuwe beurs |
|---|---|---|---|---|
| 11-23 08:02 | gate | CLEAR-USDT | bitget, kucoin, mexc | dicht / open |
| 11-23 10:01 | poloniex (grijs) | RAXOL-USDT | - | dicht / open |
| 11-23 10:01 | xt (grijs) | ANTX-USDT | gate, kucoin, mexc, bingx | dicht / open |
| 11-23 10:01 | xt (grijs) | CLEAR-USDT | bitget, gate, kucoin, mexc | dicht / open |
| 11-23 15:30 | bitfinex (grijs) | CREST-USD | - | onbekend / onbekend |
| 11-23 15:30 | bitfinex (grijs) | CREST-USDT | - | onbekend / onbekend |
| 11-23 15:30 | bitfinex (grijs) | LBAF-USD | - | onbekend / onbekend |
| 11-24 05:00 | poloniex (grijs) | PAXG-USDT | bitget, gate, kucoin, okx, bingx, cryptocom, xt | dicht / open |
| 11-24 06:00 | poloniex (grijs) | KMNO-USDT | bitget, gate, kucoin, mexc, okx, bingx | dicht / open |
| 11-24 06:30 | poloniex (grijs) | IRYS-USDT | bitget, gate, kucoin, mexc, okx, bingx, xt | dicht / open |
| 11-24 07:01 | cryptocom | RITUAL-USD | coinbase | onbekend / onbekend |
| 11-24 07:01 | bingx | 4EVER-USDT | gate | onbekend / onbekend |
| 11-24 07:07 | bingx | MTV-USDT | gate, kucoin | onbekend / onbekend |
| 11-24 10:01 | htx (grijs) | SNDK-USDT | poloniex | dicht / dicht |
| 11-24 13:47 | mexc (grijs) | PEARL-USDT | gate | onbekend / onbekend |

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

Positieve pieken (boven 0,1% per 8 uur, uit onder 0,05% na minstens één verrekening): **4570 afgerond en te rekenen**. Verder: spotkoers onbekend 0, andere munt met dezelfde naam 182, geen spotmarkt 2221, onderbroken door een te lang gat tussen runs 0; negatieve pieken 9922 (dan moet je spot shorten, dat kan een particulier meestal niet). Open pieken gaan mee naar de volgende run, dus een piek betaalt maar één keer de kosten.

Som per piek: verrekende funding, min 4 keer takerkosten (spot in en uit, perp in en uit), plus of min het prijsverschil tussen spot en perp, min één keer overmaken (opname van USDT of USDC) als spot en perp op twee beurzen zitten. Inleg = 2/3 spot en 1/3 onderpand voor de short bij 2x hefboom (GOK). Bij 2x kan een sprong van ±50% de short liquideren; dat zit niet in de som.

| Begin | Perp | Munt | Spot | Hoogste funding per 8 uur | Ontvangen funding | Kosten | Prijsverschil | Overmaken | Netto | Winst bij €150 | Duur | Handel per dag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 11-20 16:08 | kraken | MNT | kraken | 4,00% | 7,22% (15 keer) | 1,70% | 2,71% | €0,00 | **8,23%** | €8,23 | 15,1 uur | $0,0 mln |
| 11-23 13:16 | gate | 牛逼 | mexc | 0,17% | 0,00% (1 keer) | 0,31% | 7,33% | €0,01 | **7,02%** | €7,01 | 62 min | $0,1 mln |
| 11-21 14:02 | kucoin | SPORTFUN | bingx | 0,24% | 0,05% (1 keer) | 0,32% | 6,74% | €0,01 | **6,48%** | €6,47 | 2,6 uur | $0,0 mln |
| 11-21 01:20 | kucoin | SPORTFUN | bingx | 2,10% | 1,05% (1 keer) | 0,32% | 3,25% | €0,01 | **3,98%** | €3,97 | 6,0 uur | $0,0 mln |
| 11-21 06:09 | kraken | AGLD | mexc | 0,54% | 0,01% (1 keer) | 0,26% | 4,12% | €0,01 | **3,87%** | €3,86 | 52 min | $0,0 mln |
| 11-21 06:17 | kraken | BB | mexc | 0,32% | 0,01% (1 keer) | 0,20% | 3,81% | €0,01 | **3,62%** | €3,61 | 52 min | $0,0 mln |
| 11-23 13:06 | kraken | IOTX | mexc | 0,11% | 0,01% (1 keer) | 0,20% | 3,79% | €0,01 | **3,60%** | €3,59 | 72 min | $0,0 mln |
| 11-21 06:09 | kraken | PIXEL | mexc | 0,17% | 0,01% (1 keer) | 0,20% | 3,54% | €0,01 | **3,35%** | €3,34 | 58 min | $0,0 mln |
| 11-23 17:04 | kraken | BRETT | bingx | 0,15% | 0,00% (1 keer) | 0,30% | 3,26% | €0,01 | **2,96%** | €2,95 | 56 min | $0,0 mln |
| 11-23 04:44 | kraken | AGLD | mexc | 4,00% | 1,09% (3 keer) | 0,26% | 2,10% | €0,01 | **2,94%** | €2,93 | 2,4 uur | $0,0 mln |

**Afgeronde pieken B, per dag**

| Dag | Aantal (alle / MiCA / grijs) | Mediane winst bij €500 | Mediane duur |
|---|---|---|---|
| 2026-11-19 | 231 / 127 / 104 | -€3,28 | 74 min |
| 2026-11-20 | 910 / 562 / 348 | -€3,57 | 94 min |
| 2026-11-21 | 910 / 565 / 345 | -€3,87 | 64 min |
| 2026-11-22 | 876 / 573 / 303 | -€3,55 | 2,1 uur |
| 2026-11-23 | 922 / 569 / 353 | -€3,83 | 60 min |
| 2026-11-24 | 721 / 483 / 238 | -€3,71 | 69 min |

| Inleg | Kan meedoen (alle / MiCA) | Minimum onbekend | Tegelijk open (hoogst) | Met één pot gepakt | Mediane winst per keer | Winst met één pot | Per week (GOK) |
|---|---|---|---|---|---|---|---|
| €100 | 1549 / 1304 | 3016 | 129 | 21 | -€0,27 | -€4,40 | -€6,08 |
| €150 | 1554 / 1306 | 3016 | 129 | 21 | -€0,41 | -€6,58 | -€9,09 |
| €200 | 1554 / 1306 | 3016 | 129 | 21 | -€0,54 | -€8,76 | -€12,10 |
| €500 | 4570 / 2879 | 3016 | 198 | 45 | -€1,35 | -€75,82 | -€104,70 |
| €2.000 | 4570 / 2879 | 3016 | 198 | 45 | -€5,38 | -€302,61 | -€417,86 |
| €5.000 | 4570 / 2879 | 3016 | 198 | 45 | -€13,43 | -€756,23 | -€1.044,24 |

Met één pot: je pakt een moment als je geld vrij is, bij gelijke start het beste. "Tegelijk open" zegt hoeveel potten je nodig had om alles te pakken. Bij €100 tot €200 doet een moment alleen mee als de minimale bedragen bekend zijn en eronder liggen; vanaf €500 telt onbekend mee (meestal €1 tot €10).

Vergund bij B: perp- en spotbeurs hebben een MiCA-vergunning voor spot. Of de EU-dochter perps aan Nederlandse particulieren geeft, is niet nagekeken (GOK, vaak niet of beperkt). De som is lineair in de inleg (GOK): bij een dunne perp kost een grotere order meer dan de laatste prijs.

## C. Stablecoins

**C1, tussen beurzen** (dezelfde stablecoin goedkoper kopen dan elders verkopen, na alle kosten): 3097 momenten, waarvan **652 echt**.

**Echte momenten C1, per dag**

| Dag | Aantal (alle / MiCA / grijs) | Mediane winst bij €500 | Mediane duur |
|---|---|---|---|
| 2026-11-20 | 173 / 99 / 74 | €0,03 | 2 min |
| 2026-11-21 | 188 / 109 / 79 | €0,04 | 3 min |
| 2026-11-22 | 189 / 0 / 189 | €0,11 | 1 min |
| 2026-11-23 | 37 / 0 / 37 | €0,05 | 1 min |
| 2026-11-24 | 65 / 1 / 64 | €0,08 | 45 s |

| Inleg | Kan meedoen (alle / MiCA) | Minimum onbekend | Tegelijk open (hoogst) | Met één pot gepakt | Mediane winst per keer | Winst met één pot | Per week (GOK) |
|---|---|---|---|---|---|---|---|
| €100 | 231 / 39 | 421 | 3 | 149 | -€0,01 | -€41,89 | -€57,84 |
| €150 | 231 / 39 | 421 | 3 | 149 | -€0,01 | -€34,52 | -€47,67 |
| €200 | 231 / 39 | 421 | 3 | 149 | -€0,00 | -€27,19 | -€37,55 |
| €500 | 652 / 209 | 421 | 9 | 186 | €0,07 | €26,49 | €36,57 |
| €2.000 | 652 / 209 | 421 | 9 | 186 | €0,27 | €138,31 | €190,99 |
| €5.000 | 652 / 209 | 421 | 9 | 186 | €0,32 | €276,76 | €382,16 |

Met één pot: je pakt een moment als je geld vrij is, bij gelijke start het beste. "Tegelijk open" zegt hoeveel potten je nodig had om alles te pakken. Bij €100 tot €200 doet een moment alleen mee als de minimale bedragen bekend zijn en eronder liggen; vanaf €500 telt onbekend mee (meestal €1 tot €10).

**C2, naast de gewone prijs** (minstens 0,3% naast de basislijn: de mediaan per dag over de laatste 45 dagen): 1575 momenten met basislijn, waarvan 1177 met minstens €100 op het boek en **658 met winst na 2 keer takerkosten** (bij de eerste meting). Zonder basislijn (munt te nieuw of geen bron, niet geteld): 23. Geen arbitrage: je wint alleen als de koers naar zijn gewone prijs terugkomt (GOK).

Meest gezien: USDQ-USD op kraken (duur) 381 keer, EURQ-EUR op kraken (duur) 238 keer, USDC-USD op bitfinex (duur) 170 keer, USDT-EUR op kucoin (duur) 130 keer, USDT-EUR op bitget (duur) 79 keer, USDC-EUR op bitget (duur) 46 keer, TUSD-USDT op kucoin (goedkoop) 27 keer, EURQ-USDT op xt (goedkoop) 27 keer.

**C2 met winst na kosten, per dag**

| Dag | Aantal (alle / MiCA / grijs) | Mediane winst bij €500 | Mediane duur |
|---|---|---|---|
| 2026-11-19 | 5 / 4 / 1 | €0,81 | 5 min |
| 2026-11-20 | 167 / 97 / 70 | €0,59 | 45 s |
| 2026-11-21 | 313 / 99 / 214 | €1,54 | 15 s |
| 2026-11-22 | 100 / 77 / 23 | €0,11 | 4 min |
| 2026-11-23 | 46 / 40 / 6 | €0,07 | 11 min |
| 2026-11-24 | 27 / 21 / 6 | €0,51 | 5 min |

| Inleg | Kan meedoen (alle / MiCA) | Minimum onbekend | Tegelijk open (hoogst) | Met één pot gepakt | Mediane winst per keer | Winst met één pot | Per week (GOK) |
|---|---|---|---|---|---|---|---|
| €100 | 656 / 338 | 2 | 8 | 157 | €0,11 | €29,46 | €40,68 |
| €150 | 656 / 338 | 2 | 8 | 152 | €0,16 | €41,37 | €57,13 |
| €200 | 656 / 338 | 2 | 8 | 152 | €0,21 | €49,32 | €68,11 |
| €500 | 658 / 338 | 2 | 8 | 152 | €0,50 | €96,96 | €133,89 |
| €2.000 | 658 / 338 | 2 | 8 | 140 | €1,93 | €311,60 | €430,27 |
| €5.000 | 658 / 338 | 2 | 8 | 141 | €2,44 | €629,19 | €868,82 |

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

