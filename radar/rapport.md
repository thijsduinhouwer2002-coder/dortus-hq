# Kansenradar: rapport

Gemaakt 2026-11-25 07:27 UTC. Gemeten: **130,5 uur** in 29 run(s). Cijfers zijn GEZIEN (eigen metingen uit openbare API's), behalve waar GOK staat. Uitleg: `onderzoek/ai-handel/radar/README.md`.

## Het antwoord tot nu toe

- **A, nieuwe noteringen:** 48 nieuwe munten gezien, 1 echte prijsverschillen daarna; met één pot van €150 had je 1 keer kunnen instappen, samen €2,09.
- **B, funding-pieken:** 4760 pieken afgerond met spot en perp, waarvan 236 met winst na alle kosten bij €150; met één pot van €150 had je 24 keer kunnen instappen, samen -€8,02 (van €150 gaat €100 in de positie, GOK).
- **C1, stablecoin tussen beurzen:** 673 echte momenten; met één pot van €150 had je 156 keer kunnen instappen, samen -€34,43.
- **C2, stablecoin naast zijn gewone prijs:** 727 momenten met winst na kosten; met één pot van €150 had je 170 keer kunnen instappen, samen €43,29. Dit is geen arbitrage: je wint alleen als de koers terugkomt.

Alle sommen zijn een **bovengrens (GOK)**: we kijken elke 15 seconden tot 3 minuten, snelle partijen elke milliseconde. Wat we zien, is vaak al deels weg voor een gewone gebruiker zijn order plaatst. Apart gezet en niet geteld: 823 regels uit de eerste uren (oude code of het oude Kraken-tarief, zie onderaan).

## A. Nieuwe noteringen

Nieuwe munten op een beurs: **48** (waarvan 2 bij de eerste vergelijking na de start: die kunnen in het gat tussen twee runs genoteerd zijn); 30 stonden al op een andere beurs met dezelfde quote. Prijsverschillen daarna: 47, waarvan **1 echt**.

| Tijd | Beurs | Munt | Al op | Opnemen / storten op de nieuwe beurs |
|---|---|---|---|---|
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
| 11-25 03:04 | mexc (grijs) | JIMMY-USDT | - | onbekend / onbekend |
| 11-25 07:22 | poloniex (grijs) | HBAR-USDT | bitget, gate, kucoin, mexc, okx, bingx, coinbase, cryptocom, htx, xt | dicht / open |

**Echte momenten A, per dag**

| Dag | Aantal (alle / MiCA / grijs) | Mediane winst bij €500 | Mediane duur |
|---|---|---|---|
| 2026-11-25 | 1 / 0 / 1 | €2,35 | 1 min |

| Inleg | Kan meedoen (alle / MiCA) | Minimum onbekend | Tegelijk open (hoogst) | Met één pot gepakt | Mediane winst per keer | Winst met één pot | Per week (GOK) |
|---|---|---|---|---|---|---|---|
| €100 | 1 / 0 | 0 | 1 | 1 | €1,28 | €1,28 | €1,65 |
| €150 | 1 / 0 | 0 | 1 | 1 | €2,09 | €2,09 | €2,69 |
| €200 | 1 / 0 | 0 | 1 | 1 | €2,35 | €2,35 | €3,02 |
| €500 | 1 / 0 | 0 | 1 | 1 | €2,35 | €2,35 | €3,02 |
| €2.000 | 1 / 0 | 0 | 1 | 1 | €2,35 | €2,35 | €3,02 |
| €5.000 | 1 / 0 | 0 | 1 | 1 | €2,35 | €2,35 | €3,02 |

Met één pot: je pakt een moment als je geld vrij is, bij gelijke start het beste. "Tegelijk open" zegt hoeveel potten je nodig had om alles te pakken. Bij €100 tot €200 doet een moment alleen mee als de minimale bedragen bekend zijn en eronder liggen; vanaf €500 telt onbekend mee (meestal €1 tot €10).

## B. Funding-pieken

Positieve pieken (boven 0,1% per 8 uur, uit onder 0,05% na minstens één verrekening): **4760 afgerond en te rekenen**. Verder: spotkoers onbekend 0, andere munt met dezelfde naam 202, geen spotmarkt 2366, onderbroken door een te lang gat tussen runs 0; negatieve pieken 10576 (dan moet je spot shorten, dat kan een particulier meestal niet). Open pieken gaan mee naar de volgende run, dus een piek betaalt maar één keer de kosten.

Som per piek: verrekende funding, min 4 keer takerkosten (spot in en uit, perp in en uit), plus of min het prijsverschil tussen spot en perp, min één keer overmaken (opname van USDT of USDC) als spot en perp op twee beurzen zitten. Inleg = 2/3 spot en 1/3 onderpand voor de short bij 2x hefboom (GOK). Bij 2x kan een sprong van ±50% de short liquideren; dat zit niet in de som.

| Begin | Perp | Munt | Spot | Hoogste funding per 8 uur | Ontvangen funding | Kosten | Prijsverschil | Overmaken | Netto | Winst bij €150 | Duur | Handel per dag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 11-24 12:40 | hyperliquid | ACE | mexc | 4,00% | 8,35% (18 keer) | 0,19% | 12,03% | €0,01 | **20,19%** | €20,18 | 17,5 uur | $2,9 mln |
| 11-20 16:08 | kraken | MNT | kraken | 4,00% | 7,22% (15 keer) | 1,70% | 2,71% | €0,00 | **8,23%** | €8,23 | 15,1 uur | $0,0 mln |
| 11-23 13:16 | gate | 牛逼 | mexc | 0,17% | 0,00% (1 keer) | 0,31% | 7,33% | €0,01 | **7,02%** | €7,01 | 62 min | $0,1 mln |
| 11-21 14:02 | kucoin | SPORTFUN | bingx | 0,24% | 0,05% (1 keer) | 0,32% | 6,74% | €0,01 | **6,48%** | €6,47 | 2,6 uur | $0,0 mln |
| 11-21 01:20 | kucoin | SPORTFUN | bingx | 2,10% | 1,05% (1 keer) | 0,32% | 3,25% | €0,01 | **3,98%** | €3,97 | 6,0 uur | $0,0 mln |
| 11-21 06:09 | kraken | AGLD | mexc | 0,54% | 0,01% (1 keer) | 0,26% | 4,12% | €0,01 | **3,87%** | €3,86 | 52 min | $0,0 mln |
| 11-21 06:17 | kraken | BB | mexc | 0,32% | 0,01% (1 keer) | 0,20% | 3,81% | €0,01 | **3,62%** | €3,61 | 52 min | $0,0 mln |
| 11-23 13:06 | kraken | IOTX | mexc | 0,11% | 0,01% (1 keer) | 0,20% | 3,79% | €0,01 | **3,60%** | €3,59 | 72 min | $0,0 mln |
| 11-21 06:09 | kraken | PIXEL | mexc | 0,17% | 0,01% (1 keer) | 0,20% | 3,54% | €0,01 | **3,35%** | €3,34 | 58 min | $0,0 mln |
| 11-23 17:04 | kraken | BRETT | bingx | 0,15% | 0,00% (1 keer) | 0,30% | 3,26% | €0,01 | **2,96%** | €2,95 | 56 min | $0,0 mln |

**Afgeronde pieken B, per dag**

| Dag | Aantal (alle / MiCA / grijs) | Mediane winst bij €500 | Mediane duur |
|---|---|---|---|
| 2026-11-19 | 231 / 127 / 104 | -€3,28 | 74 min |
| 2026-11-20 | 910 / 562 / 348 | -€3,57 | 94 min |
| 2026-11-21 | 910 / 565 / 345 | -€3,87 | 64 min |
| 2026-11-22 | 876 / 573 / 303 | -€3,55 | 2,1 uur |
| 2026-11-23 | 923 / 569 / 354 | -€3,82 | 60 min |
| 2026-11-24 | 805 / 531 / 274 | -€3,62 | 89 min |
| 2026-11-25 | 105 / 62 / 43 | -€4,05 | 56 min |

| Inleg | Kan meedoen (alle / MiCA) | Minimum onbekend | Tegelijk open (hoogst) | Met één pot gepakt | Mediane winst per keer | Winst met één pot | Per week (GOK) |
|---|---|---|---|---|---|---|---|
| €100 | 1602 / 1352 | 3153 | 129 | 24 | -€0,28 | -€5,37 | -€6,91 |
| €150 | 1607 / 1354 | 3153 | 129 | 24 | -€0,42 | -€8,02 | -€10,32 |
| €200 | 1607 / 1354 | 3153 | 129 | 24 | -€0,55 | -€10,69 | -€13,76 |
| €500 | 4760 / 2989 | 3153 | 199 | 48 | -€1,28 | -€67,25 | -€86,57 |
| €2.000 | 4760 / 2989 | 3153 | 199 | 48 | -€5,12 | -€268,27 | -€345,36 |
| €5.000 | 4760 / 2989 | 3153 | 199 | 48 | -€12,80 | -€670,37 | -€863,00 |

Met één pot: je pakt een moment als je geld vrij is, bij gelijke start het beste. "Tegelijk open" zegt hoeveel potten je nodig had om alles te pakken. Bij €100 tot €200 doet een moment alleen mee als de minimale bedragen bekend zijn en eronder liggen; vanaf €500 telt onbekend mee (meestal €1 tot €10).

Vergund bij B: perp- en spotbeurs hebben een MiCA-vergunning voor spot. Of de EU-dochter perps aan Nederlandse particulieren geeft, is niet nagekeken (GOK, vaak niet of beperkt). De som is lineair in de inleg (GOK): bij een dunne perp kost een grotere order meer dan de laatste prijs.

## C. Stablecoins

**C1, tussen beurzen** (dezelfde stablecoin goedkoper kopen dan elders verkopen, na alle kosten): 3218 momenten, waarvan **673 echt**.

**Echte momenten C1, per dag**

| Dag | Aantal (alle / MiCA / grijs) | Mediane winst bij €500 | Mediane duur |
|---|---|---|---|
| 2026-11-20 | 173 / 99 / 74 | €0,03 | 2 min |
| 2026-11-21 | 188 / 109 / 79 | €0,04 | 3 min |
| 2026-11-22 | 189 / 0 / 189 | €0,11 | 1 min |
| 2026-11-23 | 37 / 0 / 37 | €0,05 | 1 min |
| 2026-11-24 | 75 / 1 / 74 | €0,03 | 45 s |
| 2026-11-25 | 11 / 0 / 11 | €0,03 | 30 s |

| Inleg | Kan meedoen (alle / MiCA) | Minimum onbekend | Tegelijk open (hoogst) | Met één pot gepakt | Mediane winst per keer | Winst met één pot | Per week (GOK) |
|---|---|---|---|---|---|---|---|
| €100 | 240 / 39 | 433 | 3 | 156 | -€0,01 | -€41,86 | -€53,89 |
| €150 | 240 / 39 | 433 | 3 | 156 | -€0,01 | -€34,43 | -€44,32 |
| €200 | 240 / 39 | 433 | 3 | 156 | -€0,00 | -€27,03 | -€34,80 |
| €500 | 673 / 209 | 433 | 9 | 193 | €0,06 | €26,99 | €34,75 |
| €2.000 | 673 / 209 | 433 | 9 | 193 | €0,26 | €140,11 | €180,37 |
| €5.000 | 673 / 209 | 433 | 9 | 193 | €0,29 | €278,85 | €358,97 |

Met één pot: je pakt een moment als je geld vrij is, bij gelijke start het beste. "Tegelijk open" zegt hoeveel potten je nodig had om alles te pakken. Bij €100 tot €200 doet een moment alleen mee als de minimale bedragen bekend zijn en eronder liggen; vanaf €500 telt onbekend mee (meestal €1 tot €10).

**C2, naast de gewone prijs** (minstens 0,3% naast de basislijn: de mediaan per dag over de laatste 45 dagen): 1712 momenten met basislijn, waarvan 1294 met minstens €100 op het boek en **727 met winst na 2 keer takerkosten** (bij de eerste meting). Zonder basislijn (munt te nieuw of geen bron, niet geteld): 25. Geen arbitrage: je wint alleen als de koers naar zijn gewone prijs terugkomt (GOK).

Meest gezien: USDQ-USD op kraken (duur) 403 keer, EURQ-EUR op kraken (duur) 246 keer, USDC-USD op bitfinex (duur) 170 keer, USDT-EUR op kucoin (duur) 130 keer, EURQ-USD op kraken (duur) 101 keer, USDT-EUR op bitget (duur) 79 keer, USDC-EUR op bitget (duur) 46 keer, TUSD-USDT op kucoin (goedkoop) 27 keer.

**C2 met winst na kosten, per dag**

| Dag | Aantal (alle / MiCA / grijs) | Mediane winst bij €500 | Mediane duur |
|---|---|---|---|
| 2026-11-19 | 5 / 4 / 1 | €0,81 | 5 min |
| 2026-11-20 | 167 / 97 / 70 | €0,59 | 45 s |
| 2026-11-21 | 313 / 99 / 214 | €1,54 | 15 s |
| 2026-11-22 | 100 / 77 / 23 | €0,11 | 4 min |
| 2026-11-23 | 46 / 40 / 6 | €0,07 | 11 min |
| 2026-11-24 | 31 / 25 / 6 | €0,41 | 4 min |
| 2026-11-25 | 65 / 65 / 0 | €0,20 | 1 min |

| Inleg | Kan meedoen (alle / MiCA) | Minimum onbekend | Tegelijk open (hoogst) | Met één pot gepakt | Mediane winst per keer | Winst met één pot | Per week (GOK) |
|---|---|---|---|---|---|---|---|
| €100 | 725 / 407 | 2 | 8 | 175 | €0,10 | €30,96 | €39,86 |
| €150 | 725 / 407 | 2 | 8 | 170 | €0,16 | €43,29 | €55,74 |
| €200 | 725 / 407 | 2 | 8 | 170 | €0,20 | €51,52 | €66,33 |
| €500 | 727 / 407 | 2 | 8 | 170 | €0,50 | €99,94 | €128,66 |
| €2.000 | 727 / 407 | 2 | 8 | 158 | €0,93 | €314,58 | €404,97 |
| €5.000 | 727 / 407 | 2 | 8 | 159 | €1,02 | €632,17 | €813,82 |

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

