# Kansenradar: rapport

Gemaakt 2026-11-25 12:11 UTC. Gemeten: **134,9 uur** in 30 run(s). Cijfers zijn GEZIEN (eigen metingen uit openbare API's), behalve waar GOK staat. Uitleg: `onderzoek/ai-handel/radar/README.md`.

## Het antwoord tot nu toe

- **A, nieuwe noteringen:** 49 nieuwe munten gezien, 43 echte prijsverschillen daarna; met één pot van €150 had je 19 keer kunnen instappen, samen €22,05.
- **B, funding-pieken:** 4989 pieken afgerond met spot en perp, waarvan 243 met winst na alle kosten bij €150; met één pot van €150 had je 24 keer kunnen instappen, samen -€8,06 (van €150 gaat €100 in de positie, GOK).
- **C1, stablecoin tussen beurzen:** 684 echte momenten; met één pot van €150 had je 167 keer kunnen instappen, samen -€34,96.
- **C2, stablecoin naast zijn gewone prijs:** 798 momenten met winst na kosten; met één pot van €150 had je 179 keer kunnen instappen, samen €43,50. Dit is geen arbitrage: je wint alleen als de koers terugkomt.

Alle sommen zijn een **bovengrens (GOK)**: we kijken elke 15 seconden tot 3 minuten, snelle partijen elke milliseconde. Wat we zien, is vaak al deels weg voor een gewone gebruiker zijn order plaatst. Apart gezet en niet geteld: 823 regels uit de eerste uren (oude code of het oude Kraken-tarief, zie onderaan).

## A. Nieuwe noteringen

Nieuwe munten op een beurs: **49** (waarvan 2 bij de eerste vergelijking na de start: die kunnen in het gat tussen twee runs genoteerd zijn); 31 stonden al op een andere beurs met dezelfde quote. Prijsverschillen daarna: 313, waarvan **43 echt**.

| Tijd | Beurs | Munt | Al op | Opnemen / storten op de nieuwe beurs |
|---|---|---|---|---|
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
| 11-25 03:04 | mexc (grijs) | JIMMY-USDT | - | onbekend / onbekend |
| 11-25 07:22 | poloniex (grijs) | HBAR-USDT | bitget, gate, kucoin, mexc, okx, bingx, coinbase, cryptocom, htx, xt | dicht / open |
| 11-25 07:40 | poloniex (grijs) | XPL-USDT | bitget, gate, kucoin, mexc, okx, bingx, bitfinex, htx, xt | dicht / open |

**Echte momenten A, per dag**

| Dag | Aantal (alle / MiCA / grijs) | Mediane winst bij €500 | Mediane duur |
|---|---|---|---|
| 2026-11-25 | 43 / 0 / 43 | €0,98 | 3 min |

| Inleg | Kan meedoen (alle / MiCA) | Minimum onbekend | Tegelijk open (hoogst) | Met één pot gepakt | Mediane winst per keer | Winst met één pot | Per week (GOK) |
|---|---|---|---|---|---|---|---|
| €100 | 27 / 0 | 16 | 2 | 19 | €0,80 | €16,66 | €20,75 |
| €150 | 27 / 0 | 16 | 2 | 19 | €1,04 | €22,05 | €27,45 |
| €200 | 27 / 0 | 16 | 2 | 19 | €1,04 | €22,46 | €27,97 |
| €500 | 43 / 0 | 16 | 3 | 19 | €1,04 | €23,84 | €29,68 |
| €2.000 | 43 / 0 | 16 | 3 | 19 | €1,04 | €23,84 | €29,68 |
| €5.000 | 43 / 0 | 16 | 3 | 19 | €1,04 | €23,84 | €29,68 |

Met één pot: je pakt een moment als je geld vrij is, bij gelijke start het beste. "Tegelijk open" zegt hoeveel potten je nodig had om alles te pakken. Bij €100 tot €200 doet een moment alleen mee als de minimale bedragen bekend zijn en eronder liggen; vanaf €500 telt onbekend mee (meestal €1 tot €10).

## B. Funding-pieken

Positieve pieken (boven 0,1% per 8 uur, uit onder 0,05% na minstens één verrekening): **4989 afgerond en te rekenen**. Verder: spotkoers onbekend 0, andere munt met dezelfde naam 211, geen spotmarkt 2487, onderbroken door een te lang gat tussen runs 0; negatieve pieken 10988 (dan moet je spot shorten, dat kan een particulier meestal niet). Open pieken gaan mee naar de volgende run, dus een piek betaalt maar één keer de kosten.

Som per piek: verrekende funding, min 4 keer takerkosten (spot in en uit, perp in en uit), plus of min het prijsverschil tussen spot en perp, min één keer overmaken (opname van USDT of USDC) als spot en perp op twee beurzen zitten. Inleg = 2/3 spot en 1/3 onderpand voor de short bij 2x hefboom (GOK). Bij 2x kan een sprong van ±50% de short liquideren; dat zit niet in de som.

| Begin | Perp | Munt | Spot | Hoogste funding per 8 uur | Ontvangen funding | Kosten | Prijsverschil | Overmaken | Netto | Winst bij €150 | Duur | Handel per dag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 11-24 12:40 | hyperliquid | ACE | mexc | 4,00% | 8,35% (18 keer) | 0,19% | 12,03% | €0,01 | **20,19%** | €20,18 | 17,5 uur | $2,9 mln |
| 11-25 10:00 | gate | GUA | gate | 0,23% | 0,06% (1 keer) | 0,55% | 9,98% | €0,00 | **9,49%** | €9,49 | 2,1 uur | $4,4 mln |
| 11-20 16:08 | kraken | MNT | kraken | 4,00% | 7,22% (15 keer) | 1,70% | 2,71% | €0,00 | **8,23%** | €8,23 | 15,1 uur | $0,0 mln |
| 11-23 13:16 | gate | 牛逼 | mexc | 0,17% | 0,00% (1 keer) | 0,31% | 7,33% | €0,01 | **7,02%** | €7,01 | 62 min | $0,1 mln |
| 11-21 14:02 | kucoin | SPORTFUN | bingx | 0,24% | 0,05% (1 keer) | 0,32% | 6,74% | €0,01 | **6,48%** | €6,47 | 2,6 uur | $0,0 mln |
| 11-21 01:20 | kucoin | SPORTFUN | bingx | 2,10% | 1,05% (1 keer) | 0,32% | 3,25% | €0,01 | **3,98%** | €3,97 | 6,0 uur | $0,0 mln |
| 11-21 06:09 | kraken | AGLD | mexc | 0,54% | 0,01% (1 keer) | 0,26% | 4,12% | €0,01 | **3,87%** | €3,86 | 52 min | $0,0 mln |
| 11-21 06:17 | kraken | BB | mexc | 0,32% | 0,01% (1 keer) | 0,20% | 3,81% | €0,01 | **3,62%** | €3,61 | 52 min | $0,0 mln |
| 11-23 13:06 | kraken | IOTX | mexc | 0,11% | 0,01% (1 keer) | 0,20% | 3,79% | €0,01 | **3,60%** | €3,59 | 72 min | $0,0 mln |
| 11-21 06:09 | kraken | PIXEL | mexc | 0,17% | 0,01% (1 keer) | 0,20% | 3,54% | €0,01 | **3,35%** | €3,34 | 58 min | $0,0 mln |

**Afgeronde pieken B, per dag**

| Dag | Aantal (alle / MiCA / grijs) | Mediane winst bij €500 | Mediane duur |
|---|---|---|---|
| 2026-11-19 | 231 / 127 / 104 | -€3,28 | 74 min |
| 2026-11-20 | 910 / 562 / 348 | -€3,57 | 94 min |
| 2026-11-21 | 910 / 565 / 345 | -€3,87 | 64 min |
| 2026-11-22 | 876 / 573 / 303 | -€3,55 | 2,1 uur |
| 2026-11-23 | 923 / 569 / 354 | -€3,82 | 60 min |
| 2026-11-24 | 810 / 531 / 279 | -€3,59 | 92 min |
| 2026-11-25 | 329 / 208 / 121 | -€3,16 | 106 min |

| Inleg | Kan meedoen (alle / MiCA) | Minimum onbekend | Tegelijk open (hoogst) | Met één pot gepakt | Mediane winst per keer | Winst met één pot | Per week (GOK) |
|---|---|---|---|---|---|---|---|
| €100 | 1713 / 1453 | 3270 | 129 | 24 | -€0,28 | -€5,39 | -€6,71 |
| €150 | 1719 / 1456 | 3270 | 129 | 24 | -€0,42 | -€8,06 | -€10,04 |
| €200 | 1719 / 1456 | 3270 | 129 | 24 | -€0,56 | -€10,75 | -€13,39 |
| €500 | 4989 / 3135 | 3270 | 199 | 47 | -€1,30 | -€64,08 | -€79,79 |
| €2.000 | 4989 / 3135 | 3270 | 199 | 47 | -€5,22 | -€255,66 | -€318,35 |
| €5.000 | 4989 / 3135 | 3270 | 199 | 47 | -€13,05 | -€638,87 | -€795,52 |

Met één pot: je pakt een moment als je geld vrij is, bij gelijke start het beste. "Tegelijk open" zegt hoeveel potten je nodig had om alles te pakken. Bij €100 tot €200 doet een moment alleen mee als de minimale bedragen bekend zijn en eronder liggen; vanaf €500 telt onbekend mee (meestal €1 tot €10).

Vergund bij B: perp- en spotbeurs hebben een MiCA-vergunning voor spot. Of de EU-dochter perps aan Nederlandse particulieren geeft, is niet nagekeken (GOK, vaak niet of beperkt). De som is lineair in de inleg (GOK): bij een dunne perp kost een grotere order meer dan de laatste prijs.

## C. Stablecoins

**C1, tussen beurzen** (dezelfde stablecoin goedkoper kopen dan elders verkopen, na alle kosten): 3255 momenten, waarvan **684 echt**.

**Echte momenten C1, per dag**

| Dag | Aantal (alle / MiCA / grijs) | Mediane winst bij €500 | Mediane duur |
|---|---|---|---|
| 2026-11-20 | 173 / 99 / 74 | €0,03 | 2 min |
| 2026-11-21 | 188 / 109 / 79 | €0,04 | 3 min |
| 2026-11-22 | 189 / 0 / 189 | €0,11 | 1 min |
| 2026-11-23 | 37 / 0 / 37 | €0,05 | 1 min |
| 2026-11-24 | 75 / 1 / 74 | €0,03 | 45 s |
| 2026-11-25 | 22 / 0 / 22 | €0,03 | 38 s |

| Inleg | Kan meedoen (alle / MiCA) | Minimum onbekend | Tegelijk open (hoogst) | Met één pot gepakt | Mediane winst per keer | Winst met één pot | Per week (GOK) |
|---|---|---|---|---|---|---|---|
| €100 | 251 / 39 | 433 | 3 | 167 | -€0,01 | -€42,57 | -€53,01 |
| €150 | 251 / 39 | 433 | 3 | 167 | -€0,01 | -€34,96 | -€43,53 |
| €200 | 251 / 39 | 433 | 3 | 167 | -€0,00 | -€27,39 | -€34,10 |
| €500 | 684 / 209 | 433 | 9 | 204 | €0,07 | €27,67 | €34,45 |
| €2.000 | 684 / 209 | 433 | 9 | 204 | €0,27 | €143,90 | €179,18 |
| €5.000 | 684 / 209 | 433 | 9 | 204 | €0,31 | €284,86 | €354,70 |

Met één pot: je pakt een moment als je geld vrij is, bij gelijke start het beste. "Tegelijk open" zegt hoeveel potten je nodig had om alles te pakken. Bij €100 tot €200 doet een moment alleen mee als de minimale bedragen bekend zijn en eronder liggen; vanaf €500 telt onbekend mee (meestal €1 tot €10).

**C2, naast de gewone prijs** (minstens 0,3% naast de basislijn: de mediaan per dag over de laatste 45 dagen): 1829 momenten met basislijn, waarvan 1405 met minstens €100 op het boek en **798 met winst na 2 keer takerkosten** (bij de eerste meting). Zonder basislijn (munt te nieuw of geen bron, niet geteld): 26. Geen arbitrage: je wint alleen als de koers naar zijn gewone prijs terugkomt (GOK).

Meest gezien: USDQ-USD op kraken (duur) 412 keer, EURQ-EUR op kraken (duur) 247 keer, EURQ-USD op kraken (duur) 202 keer, USDC-USD op bitfinex (duur) 170 keer, USDT-EUR op kucoin (duur) 130 keer, USDT-EUR op bitget (duur) 79 keer, USDC-EUR op bitget (duur) 46 keer, TUSD-USDT op kucoin (goedkoop) 27 keer.

**C2 met winst na kosten, per dag**

| Dag | Aantal (alle / MiCA / grijs) | Mediane winst bij €500 | Mediane duur |
|---|---|---|---|
| 2026-11-19 | 5 / 4 / 1 | €0,81 | 5 min |
| 2026-11-20 | 167 / 97 / 70 | €0,59 | 45 s |
| 2026-11-21 | 313 / 99 / 214 | €1,54 | 15 s |
| 2026-11-22 | 100 / 77 / 23 | €0,11 | 4 min |
| 2026-11-23 | 46 / 40 / 6 | €0,07 | 11 min |
| 2026-11-24 | 31 / 25 / 6 | €0,41 | 4 min |
| 2026-11-25 | 136 / 136 / 0 | €0,15 | 1 min |

| Inleg | Kan meedoen (alle / MiCA) | Minimum onbekend | Tegelijk open (hoogst) | Met één pot gepakt | Mediane winst per keer | Winst met één pot | Per week (GOK) |
|---|---|---|---|---|---|---|---|
| €100 | 796 / 478 | 2 | 8 | 184 | €0,10 | €31,04 | €38,65 |
| €150 | 796 / 478 | 2 | 8 | 179 | €0,15 | €43,50 | €54,17 |
| €200 | 796 / 478 | 2 | 8 | 179 | €0,20 | €51,68 | €64,35 |
| €500 | 798 / 478 | 2 | 8 | 179 | €0,43 | €99,78 | €124,24 |
| €2.000 | 798 / 478 | 2 | 8 | 167 | €0,73 | €314,42 | €391,51 |
| €5.000 | 798 / 478 | 2 | 8 | 168 | €0,77 | €632,01 | €786,97 |

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

