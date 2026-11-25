# Kansenradar: rapport

Gemaakt 2026-11-25 10:29 UTC. Gemeten: **133,5 uur** in 29 run(s). Cijfers zijn GEZIEN (eigen metingen uit openbare API's), behalve waar GOK staat. Uitleg: `onderzoek/ai-handel/radar/README.md`.

## Het antwoord tot nu toe

- **A, nieuwe noteringen:** 49 nieuwe munten gezien, 35 echte prijsverschillen daarna; met één pot van €150 had je 16 keer kunnen instappen, samen €19,54.
- **B, funding-pieken:** 4892 pieken afgerond met spot en perp, waarvan 239 met winst na alle kosten bij €150; met één pot van €150 had je 23 keer kunnen instappen, samen -€7,65 (van €150 gaat €100 in de positie, GOK).
- **C1, stablecoin tussen beurzen:** 678 echte momenten; met één pot van €150 had je 161 keer kunnen instappen, samen -€34,31.
- **C2, stablecoin naast zijn gewone prijs:** 765 momenten met winst na kosten; met één pot van €150 had je 208 keer kunnen instappen, samen €48,24. Dit is geen arbitrage: je wint alleen als de koers terugkomt.

Alle sommen zijn een **bovengrens (GOK)**: we kijken elke 15 seconden tot 3 minuten, snelle partijen elke milliseconde. Wat we zien, is vaak al deels weg voor een gewone gebruiker zijn order plaatst. Apart gezet en niet geteld: 823 regels uit de eerste uren (oude code of het oude Kraken-tarief, zie onderaan).

## A. Nieuwe noteringen

Nieuwe munten op een beurs: **49** (waarvan 2 bij de eerste vergelijking na de start: die kunnen in het gat tussen twee runs genoteerd zijn); 31 stonden al op een andere beurs met dezelfde quote. Prijsverschillen daarna: 291, waarvan **35 echt**.

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
| 2026-11-25 | 35 / 0 / 35 | €1,11 | 2 min |

| Inleg | Kan meedoen (alle / MiCA) | Minimum onbekend | Tegelijk open (hoogst) | Met één pot gepakt | Mediane winst per keer | Winst met één pot | Per week (GOK) |
|---|---|---|---|---|---|---|---|
| €100 | 22 / 0 | 13 | 2 | 16 | €0,89 | €14,30 | €17,99 |
| €150 | 22 / 0 | 13 | 2 | 16 | €1,09 | €19,54 | €24,59 |
| €200 | 22 / 0 | 13 | 2 | 16 | €1,10 | €19,96 | €25,12 |
| €500 | 35 / 0 | 13 | 3 | 16 | €1,10 | €21,20 | €26,68 |
| €2.000 | 35 / 0 | 13 | 3 | 16 | €1,10 | €21,20 | €26,68 |
| €5.000 | 35 / 0 | 13 | 3 | 16 | €1,10 | €21,20 | €26,68 |

Met één pot: je pakt een moment als je geld vrij is, bij gelijke start het beste. "Tegelijk open" zegt hoeveel potten je nodig had om alles te pakken. Bij €100 tot €200 doet een moment alleen mee als de minimale bedragen bekend zijn en eronder liggen; vanaf €500 telt onbekend mee (meestal €1 tot €10).

## B. Funding-pieken

Positieve pieken (boven 0,1% per 8 uur, uit onder 0,05% na minstens één verrekening): **4892 afgerond en te rekenen**. Verder: spotkoers onbekend 0, andere munt met dezelfde naam 208, geen spotmarkt 2464, onderbroken door een te lang gat tussen runs 0; negatieve pieken 10851 (dan moet je spot shorten, dat kan een particulier meestal niet). Open pieken gaan mee naar de volgende run, dus een piek betaalt maar één keer de kosten.

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
| 2026-11-24 | 807 / 531 / 276 | -€3,61 | 92 min |
| 2026-11-25 | 235 / 147 / 88 | -€3,24 | 72 min |

| Inleg | Kan meedoen (alle / MiCA) | Minimum onbekend | Tegelijk open (hoogst) | Met één pot gepakt | Mediane winst per keer | Winst met één pot | Per week (GOK) |
|---|---|---|---|---|---|---|---|
| €100 | 1665 / 1409 | 3221 | 129 | 23 | -€0,29 | -€5,12 | -€6,44 |
| €150 | 1671 / 1412 | 3221 | 129 | 23 | -€0,43 | -€7,65 | -€9,63 |
| €200 | 1671 / 1412 | 3221 | 129 | 23 | -€0,57 | -€10,20 | -€12,84 |
| €500 | 4892 / 3074 | 3221 | 199 | 48 | -€1,33 | -€67,08 | -€84,41 |
| €2.000 | 4892 / 3074 | 3221 | 199 | 48 | -€5,30 | -€267,61 | -€336,77 |
| €5.000 | 4892 / 3074 | 3221 | 199 | 48 | -€13,24 | -€668,72 | -€841,53 |

Met één pot: je pakt een moment als je geld vrij is, bij gelijke start het beste. "Tegelijk open" zegt hoeveel potten je nodig had om alles te pakken. Bij €100 tot €200 doet een moment alleen mee als de minimale bedragen bekend zijn en eronder liggen; vanaf €500 telt onbekend mee (meestal €1 tot €10).

Vergund bij B: perp- en spotbeurs hebben een MiCA-vergunning voor spot. Of de EU-dochter perps aan Nederlandse particulieren geeft, is niet nagekeken (GOK, vaak niet of beperkt). De som is lineair in de inleg (GOK): bij een dunne perp kost een grotere order meer dan de laatste prijs.

## C. Stablecoins

**C1, tussen beurzen** (dezelfde stablecoin goedkoper kopen dan elders verkopen, na alle kosten): 3230 momenten, waarvan **678 echt**.

**Echte momenten C1, per dag**

| Dag | Aantal (alle / MiCA / grijs) | Mediane winst bij €500 | Mediane duur |
|---|---|---|---|
| 2026-11-20 | 173 / 99 / 74 | €0,03 | 2 min |
| 2026-11-21 | 188 / 109 / 79 | €0,04 | 3 min |
| 2026-11-22 | 189 / 0 / 189 | €0,11 | 1 min |
| 2026-11-23 | 37 / 0 / 37 | €0,05 | 1 min |
| 2026-11-24 | 75 / 1 / 74 | €0,03 | 45 s |
| 2026-11-25 | 16 / 0 / 16 | €0,03 | 30 s |

| Inleg | Kan meedoen (alle / MiCA) | Minimum onbekend | Tegelijk open (hoogst) | Met één pot gepakt | Mediane winst per keer | Winst met één pot | Per week (GOK) |
|---|---|---|---|---|---|---|---|
| €100 | 245 / 39 | 433 | 3 | 161 | -€0,01 | -€41,81 | -€52,62 |
| €150 | 245 / 39 | 433 | 3 | 161 | -€0,01 | -€34,31 | -€43,18 |
| €200 | 245 / 39 | 433 | 3 | 161 | -€0,00 | -€26,85 | -€33,79 |
| €500 | 678 / 209 | 433 | 9 | 198 | €0,07 | €27,59 | €34,72 |
| €2.000 | 678 / 209 | 433 | 9 | 198 | €0,27 | €142,55 | €179,39 |
| €5.000 | 678 / 209 | 433 | 9 | 198 | €0,31 | €283,27 | €356,47 |

Met één pot: je pakt een moment als je geld vrij is, bij gelijke start het beste. "Tegelijk open" zegt hoeveel potten je nodig had om alles te pakken. Bij €100 tot €200 doet een moment alleen mee als de minimale bedragen bekend zijn en eronder liggen; vanaf €500 telt onbekend mee (meestal €1 tot €10).

**C2, naast de gewone prijs** (minstens 0,3% naast de basislijn: de mediaan per dag over de laatste 45 dagen): 1776 momenten met basislijn, waarvan 1354 met minstens €100 op het boek en **765 met winst na 2 keer takerkosten** (bij de eerste meting). Zonder basislijn (munt te nieuw of geen bron, niet geteld): 25. Geen arbitrage: je wint alleen als de koers naar zijn gewone prijs terugkomt (GOK).

Meest gezien: USDQ-USD op kraken (duur) 409 keer, EURQ-EUR op kraken (duur) 246 keer, USDC-USD op bitfinex (duur) 170 keer, EURQ-USD op kraken (duur) 155 keer, USDT-EUR op kucoin (duur) 130 keer, USDT-EUR op bitget (duur) 79 keer, USDC-EUR op bitget (duur) 46 keer, TUSD-USDT op kucoin (goedkoop) 27 keer.

**C2 met winst na kosten, per dag**

| Dag | Aantal (alle / MiCA / grijs) | Mediane winst bij €500 | Mediane duur |
|---|---|---|---|
| 2026-11-19 | 5 / 4 / 1 | €0,81 | 5 min |
| 2026-11-20 | 167 / 97 / 70 | €0,59 | 45 s |
| 2026-11-21 | 313 / 99 / 214 | €1,54 | 15 s |
| 2026-11-22 | 100 / 77 / 23 | €0,11 | 4 min |
| 2026-11-23 | 46 / 40 / 6 | €0,07 | 11 min |
| 2026-11-24 | 31 / 25 / 6 | €0,41 | 4 min |
| 2026-11-25 | 103 / 103 / 0 | €0,18 | 1 min |

| Inleg | Kan meedoen (alle / MiCA) | Minimum onbekend | Tegelijk open (hoogst) | Met één pot gepakt | Mediane winst per keer | Winst met één pot | Per week (GOK) |
|---|---|---|---|---|---|---|---|
| €100 | 763 / 445 | 2 | 8 | 213 | €0,10 | €34,81 | €43,81 |
| €150 | 763 / 445 | 2 | 8 | 208 | €0,15 | €48,24 | €60,70 |
| €200 | 763 / 445 | 2 | 8 | 208 | €0,20 | €57,05 | €71,80 |
| €500 | 765 / 445 | 2 | 8 | 208 | €0,36 | €107,03 | €134,70 |
| €2.000 | 765 / 445 | 2 | 8 | 196 | €0,44 | €321,67 | €404,80 |
| €5.000 | 765 / 445 | 2 | 8 | 197 | €0,44 | €639,26 | €804,46 |

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

