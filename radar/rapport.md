# Kansenradar: rapport

Gemaakt 2026-11-20 16:16 UTC. Gemeten: **23,8 uur** in 9 run(s). Cijfers zijn GEZIEN (eigen metingen uit openbare API's), behalve waar GOK staat. Uitleg: `platformen/ai-handel/radar/README.md`.

## Het antwoord tot nu toe

- **A, nieuwe noteringen:** 26 nieuwe munten gezien, 0 echte prijsverschillen daarna; met één pot van €150 had je hier tot nu toe niets kunnen pakken.
- **B, funding-pieken:** 713 pieken afgerond met spot en perp, waarvan 44 met winst na alle kosten bij €150; met één pot van €150 had je 2 keer kunnen instappen, samen -€0,61 (van €150 gaat €100 in de positie, GOK).
- **C1, stablecoin tussen beurzen:** 43 echte momenten; met één pot van €150 had je 12 keer kunnen instappen, samen -€4,69.
- **C2, stablecoin naast zijn gewone prijs:** 46 momenten met winst na kosten; met één pot van €150 had je 12 keer kunnen instappen, samen €5,77. Dit is geen arbitrage: je wint alleen als de koers terugkomt.

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

Positieve pieken (boven 0,1% per 8 uur, uit onder 0,05% na minstens één verrekening): **713 afgerond en te rekenen**. Verder: spotkoers onbekend 0, andere munt met dezelfde naam 21, geen spotmarkt 404, onderbroken door een te lang gat tussen runs 0; negatieve pieken 2066 (dan moet je spot shorten, dat kan een particulier meestal niet). Open pieken gaan mee naar de volgende run, dus een piek betaalt maar één keer de kosten.

Som per piek: verrekende funding, min 4 keer takerkosten (spot in en uit, perp in en uit), plus of min het prijsverschil tussen spot en perp, min één keer overmaken (opname van USDT of USDC) als spot en perp op twee beurzen zitten. Inleg = 2/3 spot en 1/3 onderpand voor de short bij 2x hefboom (GOK). Bij 2x kan een sprong van ±50% de short liquideren; dat zit niet in de som.

| Begin | Perp | Munt | Spot | Hoogste funding per 8 uur | Ontvangen funding | Kosten | Prijsverschil | Overmaken | Netto | Winst bij €150 | Duur | Handel per dag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 11-19 19:03 | kraken | TREAD | kraken | 4,00% | -0,40% (1 keer) | 1,70% | 4,73% | €0,00 | **2,62%** | €2,62 | 90 min | $0,0 mln |
| 11-20 02:03 | kraken | ZIG | kraken | 2,74% | 0,76% (3 keer) | 1,70% | 3,53% | €0,00 | **2,59%** | €2,59 | 3,0 uur | $0,0 mln |
| 11-20 05:23 | kraken | CHILLGUY | mexc | 0,20% | 0,01% (1 keer) | 0,26% | 2,69% | €0,01 | **2,44%** | €2,43 | 50 min | $0,0 mln |
| 11-20 15:03 | kraken | PIXEL | mexc | 0,69% | 0,04% (1 keer) | 0,20% | 2,35% | €0,01 | **2,20%** | €2,19 | 69 min | $0,0 mln |
| 11-20 08:13 | bingx | MYX | bingx | 0,25% | 0,05% (1 keer) | 0,30% | 2,41% | €0,00 | **2,16%** | €2,16 | 3,8 uur | $0,8 mln |
| 11-19 16:21 | gate | 牛逼 | mexc | 3,51% | 1,95% (3 keer) | 0,31% | 0,42% | €0,01 | **2,06%** | €2,05 | 11,8 uur | $0,1 mln |
| 11-19 17:03 | kraken | TREAD | kraken | 4,00% | -0,40% (1 keer) | 1,70% | 4,05% | €0,00 | **1,94%** | €1,94 | 88 min | $0,0 mln |
| 11-20 08:43 | gate | KERNEL | gate | 4,00% | -0,88% (1 keer) | 0,55% | 3,16% | €0,00 | **1,73%** | €1,73 | 3,3 uur | $0,0 mln |
| 11-19 17:05 | kraken | CHILLGUY | mexc | 0,17% | 0,01% (1 keer) | 0,26% | 1,88% | €0,01 | **1,63%** | €1,62 | 78 min | $0,0 mln |
| 11-20 07:47 | kucoin | REKT | kucoin | 0,89% | 0,07% (2 keer) | 0,72% | 2,09% | €0,00 | **1,44%** | €1,44 | 74 min | $0,6 mln |

**Afgeronde pieken B, per dag**

| Dag | Aantal (alle / MiCA / grijs) | Mediane winst bij €500 | Mediane duur |
|---|---|---|---|
| 2026-11-19 | 229 / 126 / 103 | -€3,33 | 74 min |
| 2026-11-20 | 484 / 290 / 194 | -€3,58 | 74 min |

| Inleg | Kan meedoen (alle / MiCA) | Minimum onbekend | Tegelijk open (hoogst) | Met één pot gepakt | Mediane winst per keer | Winst met één pot | Per week (GOK) |
|---|---|---|---|---|---|---|---|
| €100 | 222 / 206 | 491 | 70 | 2 | -€0,21 | -€0,41 | -€2,90 |
| €150 | 222 / 206 | 491 | 70 | 2 | -€0,30 | -€0,61 | -€4,31 |
| €200 | 222 / 206 | 491 | 70 | 2 | -€0,41 | -€0,82 | -€5,80 |
| €500 | 713 / 416 | 491 | 113 | 6 | -€1,27 | €3,42 | €24,19 |
| €2.000 | 713 / 416 | 491 | 113 | 6 | -€5,05 | €13,80 | €97,59 |
| €5.000 | 713 / 416 | 491 | 113 | 6 | -€12,62 | €34,56 | €244,40 |

Met één pot: je pakt een moment als je geld vrij is, bij gelijke start het beste. "Tegelijk open" zegt hoeveel potten je nodig had om alles te pakken. Bij €100 tot €200 doet een moment alleen mee als de minimale bedragen bekend zijn en eronder liggen; vanaf €500 telt onbekend mee (meestal €1 tot €10).

Vergund bij B: perp- en spotbeurs hebben een MiCA-vergunning voor spot. Of de EU-dochter perps aan Nederlandse particulieren geeft, is niet nagekeken (GOK, vaak niet of beperkt). De som is lineair in de inleg (GOK): bij een dunne perp kost een grotere order meer dan de laatste prijs.

## C. Stablecoins

**C1, tussen beurzen** (dezelfde stablecoin goedkoper kopen dan elders verkopen, na alle kosten): 1014 momenten, waarvan **43 echt**.

**Echte momenten C1, per dag**

| Dag | Aantal (alle / MiCA / grijs) | Mediane winst bij €500 | Mediane duur |
|---|---|---|---|
| 2026-11-20 | 43 / 17 / 26 | €0,08 | 1 min |

| Inleg | Kan meedoen (alle / MiCA) | Minimum onbekend | Tegelijk open (hoogst) | Met één pot gepakt | Mediane winst per keer | Winst met één pot | Per week (GOK) |
|---|---|---|---|---|---|---|---|
| €100 | 13 / 5 | 30 | 2 | 12 | -€0,20 | -€4,99 | -€35,29 |
| €150 | 13 / 5 | 30 | 2 | 12 | -€0,17 | -€4,69 | -€33,16 |
| €200 | 13 / 5 | 30 | 2 | 12 | -€0,15 | -€4,39 | -€31,04 |
| €500 | 43 / 17 | 30 | 5 | 20 | €0,03 | €1,29 | €9,12 |
| €2.000 | 43 / 17 | 30 | 5 | 20 | €0,15 | €4,68 | €33,13 |
| €5.000 | 43 / 17 | 30 | 5 | 20 | €0,19 | €6,39 | €45,17 |

Met één pot: je pakt een moment als je geld vrij is, bij gelijke start het beste. "Tegelijk open" zegt hoeveel potten je nodig had om alles te pakken. Bij €100 tot €200 doet een moment alleen mee als de minimale bedragen bekend zijn en eronder liggen; vanaf €500 telt onbekend mee (meestal €1 tot €10).

**C2, naast de gewone prijs** (minstens 0,3% naast de basislijn: de mediaan per dag over de laatste 45 dagen): 309 momenten met basislijn, waarvan 47 met minstens €100 op het boek en **46 met winst na 2 keer takerkosten** (bij de eerste meting). Zonder basislijn (munt te nieuw of geen bron, niet geteld): 5. Geen arbitrage: je wint alleen als de koers naar zijn gewone prijs terugkomt (GOK).

Meest gezien: USDT-EUR op bitget (duur) 17 keer, USDT-EUR op kucoin (duur) 13 keer, USDC-EUR op kucoin (duur) 6 keer, TUSD-USDT op kucoin (goedkoop) 2 keer, EURC-USD op cryptocom (duur) 2 keer, PYUSD-USDT op htx (goedkoop) 2 keer, EURQ-USD op kraken (duur) 1 keer, USDS-USDT op poloniex (goedkoop) 1 keer.

**C2 met winst na kosten, per dag**

| Dag | Aantal (alle / MiCA / grijs) | Mediane winst bij €500 | Mediane duur |
|---|---|---|---|
| 2026-11-19 | 5 / 4 / 1 | €0,81 | 5 min |
| 2026-11-20 | 41 / 22 / 19 | €0,55 | 45 s |

| Inleg | Kan meedoen (alle / MiCA) | Minimum onbekend | Tegelijk open (hoogst) | Met één pot gepakt | Mediane winst per keer | Winst met één pot | Per week (GOK) |
|---|---|---|---|---|---|---|---|
| €100 | 46 / 26 | 0 | 4 | 12 | €0,12 | €3,98 | €28,17 |
| €150 | 46 / 26 | 0 | 4 | 12 | €0,18 | €5,77 | €40,80 |
| €200 | 46 / 26 | 0 | 4 | 12 | €0,23 | €6,98 | €49,35 |
| €500 | 46 / 26 | 0 | 4 | 12 | €0,59 | €14,23 | €100,66 |
| €2.000 | 46 / 26 | 0 | 4 | 12 | €1,99 | €46,50 | €328,83 |
| €5.000 | 46 / 26 | 0 | 4 | 12 | €3,31 | €68,72 | €485,94 |

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

