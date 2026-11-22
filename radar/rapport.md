# Kansenradar: rapport

Gemaakt 2026-11-22 01:48 UTC. Gemeten: **55,8 uur** in 15 run(s). Cijfers zijn GEZIEN (eigen metingen uit openbare API's), behalve waar GOK staat. Uitleg: `platformen/ai-handel/radar/README.md`.

## Het antwoord tot nu toe

- **A, nieuwe noteringen:** 26 nieuwe munten gezien, 0 echte prijsverschillen daarna; met één pot van €150 had je hier tot nu toe niets kunnen pakken.
- **B, funding-pieken:** 2046 pieken afgerond met spot en perp, waarvan 124 met winst na alle kosten bij €150; met één pot van €150 had je 5 keer kunnen instappen, samen -€1,21 (van €150 gaat €100 in de positie, GOK).
- **C1, stablecoin tussen beurzen:** 378 echte momenten; met één pot van €150 had je 55 keer kunnen instappen, samen -€33,83.
- **C2, stablecoin naast zijn gewone prijs:** 499 momenten met winst na kosten; met één pot van €150 had je 72 keer kunnen instappen, samen €20,35. Dit is geen arbitrage: je wint alleen als de koers terugkomt.

Alle sommen zijn een **bovengrens (GOK)**: we kijken elke 15 seconden tot 3 minuten, snelle partijen elke milliseconde. Wat we zien, is vaak al deels weg voor een gewone gebruiker zijn order plaatst. Apart gezet en niet geteld: 823 regels uit de eerste uren (oude code of het oude Kraken-tarief, zie onderaan).

## A. Nieuwe noteringen

Nieuwe munten op een beurs: **26** (waarvan 0 bij de eerste vergelijking na de start: die kunnen in het gat tussen twee runs genoteerd zijn); 16 stonden al op een andere beurs met dezelfde quote. Prijsverschillen daarna: 14, waarvan **0 echt**.

| Tijd | Beurs | Munt | Al op | Opnemen / storten op de nieuwe beurs |
|---|---|---|---|---|
| 11-20 10:49 | xt (grijs) | DUSK3S-USDT | - | onbekend / onbekend |
| 11-20 10:49 | xt (grijs) | GALA3L-USDT | gate | onbekend / onbekend |
| 11-20 10:49 | xt (grijs) | OP3L-USDT | gate | onbekend / onbekend |
| 11-20 10:49 | xt (grijs) | SHIB3L-USDT | gate | onbekend / onbekend |
| 11-20 10:49 | xt (grijs) | SOL3L-USDT | gate | onbekend / onbekend |
| 11-20 10:49 | xt (grijs) | XPL3S-USDT | gate | onbekend / onbekend |
| 11-20 11:19 | mexc (grijs) | ANTON-USDT | gate | onbekend / onbekend |
| 11-20 11:19 | mexc (grijs) | ANTX-USDT | gate, bingx | onbekend / onbekend |
| 11-20 12:01 | poloniex (grijs) | PIEVERSE-USDT | gate, kucoin, mexc, bingx | dicht / open |
| 11-20 12:31 | poloniex (grijs) | VVV-USDT | gate, kucoin, mexc, okx, bingx | dicht / open |
| 11-20 13:01 | htx (grijs) | PIEVERSE-USDT | gate, kucoin, mexc, bingx, poloniex | dicht / open |
| 11-20 13:31 | htx (grijs) | VVV-USDT | gate, kucoin, mexc, okx, bingx, poloniex | dicht / open |
| 11-20 14:01 | bitget (grijs) | CLEAR-USDT | mexc | open / open |
| 11-20 14:31 | kucoin | ANTX-USDT | gate, mexc, bingx | dicht / open |
| 11-20 15:04 | kraken | BFI-USD | - | open / open |

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

Positieve pieken (boven 0,1% per 8 uur, uit onder 0,05% na minstens één verrekening): **2046 afgerond en te rekenen**. Verder: spotkoers onbekend 0, andere munt met dezelfde naam 91, geen spotmarkt 849, onderbroken door een te lang gat tussen runs 0; negatieve pieken 5101 (dan moet je spot shorten, dat kan een particulier meestal niet). Open pieken gaan mee naar de volgende run, dus een piek betaalt maar één keer de kosten.

Som per piek: verrekende funding, min 4 keer takerkosten (spot in en uit, perp in en uit), plus of min het prijsverschil tussen spot en perp, min één keer overmaken (opname van USDT of USDC) als spot en perp op twee beurzen zitten. Inleg = 2/3 spot en 1/3 onderpand voor de short bij 2x hefboom (GOK). Bij 2x kan een sprong van ±50% de short liquideren; dat zit niet in de som.

| Begin | Perp | Munt | Spot | Hoogste funding per 8 uur | Ontvangen funding | Kosten | Prijsverschil | Overmaken | Netto | Winst bij €150 | Duur | Handel per dag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 11-20 16:08 | kraken | MNT | kraken | 4,00% | 7,22% (15 keer) | 1,70% | 2,71% | €0,00 | **8,23%** | €8,23 | 15,1 uur | $0,0 mln |
| 11-21 14:02 | kucoin | SPORTFUN | bingx | 0,24% | 0,05% (1 keer) | 0,32% | 6,74% | €0,01 | **6,48%** | €6,47 | 2,6 uur | $0,0 mln |
| 11-21 01:20 | kucoin | SPORTFUN | bingx | 2,10% | 1,05% (1 keer) | 0,32% | 3,25% | €0,01 | **3,98%** | €3,97 | 6,0 uur | $0,0 mln |
| 11-21 06:09 | kraken | AGLD | mexc | 0,54% | 0,01% (1 keer) | 0,26% | 4,12% | €0,01 | **3,87%** | €3,86 | 52 min | $0,0 mln |
| 11-21 06:17 | kraken | BB | mexc | 0,32% | 0,01% (1 keer) | 0,20% | 3,81% | €0,01 | **3,62%** | €3,61 | 52 min | $0,0 mln |
| 11-21 06:09 | kraken | PIXEL | mexc | 0,17% | 0,01% (1 keer) | 0,20% | 3,54% | €0,01 | **3,35%** | €3,34 | 58 min | $0,0 mln |
| 11-20 18:12 | kraken | BRETT | bingx | 0,11% | 0,00% (1 keer) | 0,30% | 3,18% | €0,01 | **2,88%** | €2,87 | 48 min | $0,0 mln |
| 11-19 19:03 | kraken | TREAD | kraken | 4,00% | -0,40% (1 keer) | 1,70% | 4,73% | €0,00 | **2,62%** | €2,62 | 90 min | $0,0 mln |
| 11-20 02:03 | kraken | ZIG | kraken | 2,74% | 0,76% (3 keer) | 1,70% | 3,53% | €0,00 | **2,59%** | €2,59 | 3,0 uur | $0,0 mln |
| 11-20 05:23 | kraken | CHILLGUY | mexc | 0,20% | 0,01% (1 keer) | 0,26% | 2,69% | €0,01 | **2,44%** | €2,43 | 50 min | $0,0 mln |

**Afgeronde pieken B, per dag**

| Dag | Aantal (alle / MiCA / grijs) | Mediane winst bij €500 | Mediane duur |
|---|---|---|---|
| 2026-11-19 | 231 / 127 / 104 | -€3,28 | 74 min |
| 2026-11-20 | 909 / 561 / 348 | -€3,57 | 94 min |
| 2026-11-21 | 892 / 557 / 335 | -€3,88 | 62 min |
| 2026-11-22 | 14 / 10 / 4 | -€6,63 | 50 min |

| Inleg | Kan meedoen (alle / MiCA) | Minimum onbekend | Tegelijk open (hoogst) | Met één pot gepakt | Mediane winst per keer | Winst met één pot | Per week (GOK) |
|---|---|---|---|---|---|---|---|
| €100 | 648 / 549 | 1395 | 97 | 5 | -€0,18 | -€0,81 | -€2,44 |
| €150 | 651 / 549 | 1395 | 98 | 5 | -€0,27 | -€1,21 | -€3,65 |
| €200 | 651 / 549 | 1395 | 98 | 5 | -€0,36 | -€1,61 | -€4,85 |
| €500 | 2046 / 1255 | 1395 | 160 | 24 | -€1,23 | -€24,90 | -€75,01 |
| €2.000 | 2046 / 1255 | 1395 | 160 | 24 | -€4,90 | -€99,09 | -€298,50 |
| €5.000 | 2046 / 1255 | 1395 | 160 | 24 | -€12,26 | -€247,48 | -€745,51 |

Met één pot: je pakt een moment als je geld vrij is, bij gelijke start het beste. "Tegelijk open" zegt hoeveel potten je nodig had om alles te pakken. Bij €100 tot €200 doet een moment alleen mee als de minimale bedragen bekend zijn en eronder liggen; vanaf €500 telt onbekend mee (meestal €1 tot €10).

Vergund bij B: perp- en spotbeurs hebben een MiCA-vergunning voor spot. Of de EU-dochter perps aan Nederlandse particulieren geeft, is niet nagekeken (GOK, vaak niet of beperkt). De som is lineair in de inleg (GOK): bij een dunne perp kost een grotere order meer dan de laatste prijs.

## C. Stablecoins

**C1, tussen beurzen** (dezelfde stablecoin goedkoper kopen dan elders verkopen, na alle kosten): 2094 momenten, waarvan **378 echt**.

**Echte momenten C1, per dag**

| Dag | Aantal (alle / MiCA / grijs) | Mediane winst bij €500 | Mediane duur |
|---|---|---|---|
| 2026-11-20 | 173 / 99 / 74 | €0,03 | 2 min |
| 2026-11-21 | 188 / 109 / 79 | €0,04 | 3 min |
| 2026-11-22 | 17 / 0 / 17 | €0,11 | 45 s |

| Inleg | Kan meedoen (alle / MiCA) | Minimum onbekend | Tegelijk open (hoogst) | Met één pot gepakt | Mediane winst per keer | Winst met één pot | Per week (GOK) |
|---|---|---|---|---|---|---|---|
| €100 | 98 / 39 | 280 | 3 | 55 | -€0,91 | -€38,71 | -€116,62 |
| €150 | 98 / 39 | 280 | 3 | 55 | -€0,86 | -€33,83 | -€101,91 |
| €200 | 98 / 39 | 280 | 3 | 55 | -€0,82 | -€28,96 | -€87,25 |
| €500 | 378 / 208 | 280 | 9 | 89 | €0,03 | €11,25 | €33,88 |
| €2.000 | 378 / 208 | 280 | 9 | 89 | €0,32 | €74,69 | €224,99 |
| €5.000 | 378 / 208 | 280 | 9 | 89 | €0,45 | €151,22 | €455,54 |

Met één pot: je pakt een moment als je geld vrij is, bij gelijke start het beste. "Tegelijk open" zegt hoeveel potten je nodig had om alles te pakken. Bij €100 tot €200 doet een moment alleen mee als de minimale bedragen bekend zijn en eronder liggen; vanaf €500 telt onbekend mee (meestal €1 tot €10).

**C2, naast de gewone prijs** (minstens 0,3% naast de basislijn: de mediaan per dag over de laatste 45 dagen): 842 momenten met basislijn, waarvan 533 met minstens €100 op het boek en **499 met winst na 2 keer takerkosten** (bij de eerste meting). Zonder basislijn (munt te nieuw of geen bron, niet geteld): 11. Geen arbitrage: je wint alleen als de koers naar zijn gewone prijs terugkomt (GOK).

Meest gezien: USDC-USD op bitfinex (duur) 170 keer, USDT-EUR op kucoin (duur) 130 keer, USDT-EUR op bitget (duur) 71 keer, EURQ-EUR op kraken (duur) 48 keer, USDC-EUR op bitget (duur) 35 keer, TUSD-USDT op kucoin (goedkoop) 20 keer, USDC-EUR op kucoin (duur) 17 keer, USDQ-USD op kraken (duur) 15 keer.

**C2 met winst na kosten, per dag**

| Dag | Aantal (alle / MiCA / grijs) | Mediane winst bij €500 | Mediane duur |
|---|---|---|---|
| 2026-11-19 | 5 / 4 / 1 | €0,81 | 5 min |
| 2026-11-20 | 167 / 97 / 70 | €0,59 | 45 s |
| 2026-11-21 | 313 / 99 / 214 | €1,54 | 15 s |
| 2026-11-22 | 14 / 10 / 4 | €0,09 | 4 min |

| Inleg | Kan meedoen (alle / MiCA) | Minimum onbekend | Tegelijk open (hoogst) | Met één pot gepakt | Mediane winst per keer | Winst met één pot | Per week (GOK) |
|---|---|---|---|---|---|---|---|
| €100 | 499 / 210 | 0 | 8 | 72 | €0,12 | €13,74 | €41,39 |
| €150 | 499 / 210 | 0 | 8 | 72 | €0,18 | €20,35 | €61,29 |
| €200 | 499 / 210 | 0 | 8 | 72 | €0,24 | €25,89 | €78,01 |
| €500 | 499 / 210 | 0 | 8 | 72 | €0,60 | €58,51 | €176,24 |
| €2.000 | 499 / 210 | 0 | 8 | 72 | €2,22 | €205,94 | €620,39 |
| €5.000 | 499 / 210 | 0 | 8 | 73 | €4,79 | €414,92 | €1.249,93 |

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

