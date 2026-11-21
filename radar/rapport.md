# Kansenradar: rapport

Gemaakt 2026-11-21 00:10 UTC. Gemeten: **31,3 uur** in 10 run(s). Cijfers zijn GEZIEN (eigen metingen uit openbare API's), behalve waar GOK staat. Uitleg: `platformen/ai-handel/radar/README.md`.

## Het antwoord tot nu toe

- **A, nieuwe noteringen:** 26 nieuwe munten gezien, 0 echte prijsverschillen daarna; met één pot van €150 had je hier tot nu toe niets kunnen pakken.
- **B, funding-pieken:** 1071 pieken afgerond met spot en perp, waarvan 62 met winst na alle kosten bij €150; met één pot van €150 had je 4 keer kunnen instappen, samen -€1,55 (van €150 gaat €100 in de positie, GOK).
- **C1, stablecoin tussen beurzen:** 173 echte momenten; met één pot van €150 had je 35 keer kunnen instappen, samen -€27,34.
- **C2, stablecoin naast zijn gewone prijs:** 172 momenten met winst na kosten; met één pot van €150 had je 89 keer kunnen instappen, samen €23,25. Dit is geen arbitrage: je wint alleen als de koers terugkomt.

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

Positieve pieken (boven 0,1% per 8 uur, uit onder 0,05% na minstens één verrekening): **1071 afgerond en te rekenen**. Verder: spotkoers onbekend 0, andere munt met dezelfde naam 29, geen spotmarkt 550, onderbroken door een te lang gat tussen runs 0; negatieve pieken 2920 (dan moet je spot shorten, dat kan een particulier meestal niet). Open pieken gaan mee naar de volgende run, dus een piek betaalt maar één keer de kosten.

Som per piek: verrekende funding, min 4 keer takerkosten (spot in en uit, perp in en uit), plus of min het prijsverschil tussen spot en perp, min één keer overmaken (opname van USDT of USDC) als spot en perp op twee beurzen zitten. Inleg = 2/3 spot en 1/3 onderpand voor de short bij 2x hefboom (GOK). Bij 2x kan een sprong van ±50% de short liquideren; dat zit niet in de som.

| Begin | Perp | Munt | Spot | Hoogste funding per 8 uur | Ontvangen funding | Kosten | Prijsverschil | Overmaken | Netto | Winst bij €150 | Duur | Handel per dag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 11-20 18:12 | kraken | BRETT | bingx | 0,11% | 0,00% (1 keer) | 0,30% | 3,18% | €0,01 | **2,88%** | €2,87 | 48 min | $0,0 mln |
| 11-19 19:03 | kraken | TREAD | kraken | 4,00% | -0,40% (1 keer) | 1,70% | 4,73% | €0,00 | **2,62%** | €2,62 | 90 min | $0,0 mln |
| 11-20 02:03 | kraken | ZIG | kraken | 2,74% | 0,76% (3 keer) | 1,70% | 3,53% | €0,00 | **2,59%** | €2,59 | 3,0 uur | $0,0 mln |
| 11-20 05:23 | kraken | CHILLGUY | mexc | 0,20% | 0,01% (1 keer) | 0,26% | 2,69% | €0,01 | **2,44%** | €2,43 | 50 min | $0,0 mln |
| 11-20 15:03 | kraken | PIXEL | mexc | 0,69% | 0,04% (1 keer) | 0,20% | 2,35% | €0,01 | **2,20%** | €2,19 | 69 min | $0,0 mln |
| 11-20 08:13 | bingx | MYX | bingx | 0,25% | 0,05% (1 keer) | 0,30% | 2,41% | €0,00 | **2,16%** | €2,16 | 3,8 uur | $0,8 mln |
| 11-19 16:21 | gate | 牛逼 | mexc | 3,51% | 1,95% (3 keer) | 0,31% | 0,42% | €0,01 | **2,06%** | €2,05 | 11,8 uur | $0,1 mln |
| 11-19 17:03 | kraken | TREAD | kraken | 4,00% | -0,40% (1 keer) | 1,70% | 4,05% | €0,00 | **1,94%** | €1,94 | 88 min | $0,0 mln |
| 11-20 21:20 | kucoin | REKT | kucoin | 0,89% | 0,07% (1 keer) | 0,72% | 2,53% | €0,00 | **1,88%** | €1,88 | 68 min | $0,8 mln |
| 11-20 08:43 | gate | KERNEL | gate | 4,00% | -0,88% (1 keer) | 0,55% | 3,16% | €0,00 | **1,73%** | €1,73 | 3,3 uur | $0,0 mln |

**Afgeronde pieken B, per dag**

| Dag | Aantal (alle / MiCA / grijs) | Mediane winst bij €500 | Mediane duur |
|---|---|---|---|
| 2026-11-19 | 229 / 126 / 103 | -€3,33 | 74 min |
| 2026-11-20 | 842 / 535 / 307 | -€3,58 | 75 min |

| Inleg | Kan meedoen (alle / MiCA) | Minimum onbekend | Tegelijk open (hoogst) | Met één pot gepakt | Mediane winst per keer | Winst met één pot | Per week (GOK) |
|---|---|---|---|---|---|---|---|
| €100 | 346 / 321 | 724 | 91 | 4 | -€0,26 | -€1,04 | -€5,59 |
| €150 | 347 / 321 | 724 | 92 | 4 | -€0,38 | -€1,55 | -€8,33 |
| €200 | 347 / 321 | 724 | 92 | 4 | -€0,51 | -€2,08 | -€11,18 |
| €500 | 1071 / 661 | 724 | 148 | 11 | -€1,00 | €5,84 | €31,39 |
| €2.000 | 1071 / 661 | 724 | 148 | 11 | -€3,97 | €23,62 | €126,95 |
| €5.000 | 1071 / 661 | 724 | 148 | 11 | -€9,90 | €59,17 | €318,01 |

Met één pot: je pakt een moment als je geld vrij is, bij gelijke start het beste. "Tegelijk open" zegt hoeveel potten je nodig had om alles te pakken. Bij €100 tot €200 doet een moment alleen mee als de minimale bedragen bekend zijn en eronder liggen; vanaf €500 telt onbekend mee (meestal €1 tot €10).

Vergund bij B: perp- en spotbeurs hebben een MiCA-vergunning voor spot. Of de EU-dochter perps aan Nederlandse particulieren geeft, is niet nagekeken (GOK, vaak niet of beperkt). De som is lineair in de inleg (GOK): bij een dunne perp kost een grotere order meer dan de laatste prijs.

## C. Stablecoins

**C1, tussen beurzen** (dezelfde stablecoin goedkoper kopen dan elders verkopen, na alle kosten): 1416 momenten, waarvan **173 echt**.

**Echte momenten C1, per dag**

| Dag | Aantal (alle / MiCA / grijs) | Mediane winst bij €500 | Mediane duur |
|---|---|---|---|
| 2026-11-20 | 170 / 98 / 72 | €0,03 | 1 min |
| 2026-11-21 | 3 / 1 / 2 | -€0,63 | 30 s |

| Inleg | Kan meedoen (alle / MiCA) | Minimum onbekend | Tegelijk open (hoogst) | Met één pot gepakt | Mediane winst per keer | Winst met één pot | Per week (GOK) |
|---|---|---|---|---|---|---|---|
| €100 | 39 / 15 | 134 | 3 | 35 | -€0,92 | -€28,58 | -€153,59 |
| €150 | 39 / 15 | 134 | 3 | 35 | -€0,88 | -€27,34 | -€146,92 |
| €200 | 39 / 15 | 134 | 3 | 35 | -€0,83 | -€26,10 | -€140,30 |
| €500 | 173 / 99 | 134 | 6 | 65 | €0,03 | €0,71 | €3,81 |
| €2.000 | 173 / 99 | 134 | 6 | 65 | €0,16 | €30,17 | €162,13 |
| €5.000 | 173 / 99 | 134 | 6 | 65 | €0,24 | €55,03 | €295,78 |

Met één pot: je pakt een moment als je geld vrij is, bij gelijke start het beste. "Tegelijk open" zegt hoeveel potten je nodig had om alles te pakken. Bij €100 tot €200 doet een moment alleen mee als de minimale bedragen bekend zijn en eronder liggen; vanaf €500 telt onbekend mee (meestal €1 tot €10).

**C2, naast de gewone prijs** (minstens 0,3% naast de basislijn: de mediaan per dag over de laatste 45 dagen): 454 momenten met basislijn, waarvan 173 met minstens €100 op het boek en **172 met winst na 2 keer takerkosten** (bij de eerste meting). Zonder basislijn (munt te nieuw of geen bron, niet geteld): 6. Geen arbitrage: je wint alleen als de koers naar zijn gewone prijs terugkomt (GOK).

Meest gezien: USDT-EUR op kucoin (duur) 79 keer, USDT-EUR op bitget (duur) 46 keer, USDC-EUR op kucoin (duur) 13 keer, USDC-USD op bitfinex (duur) 12 keer, USDC-EUR op bitget (duur) 9 keer, PYUSD-USDT op htx (goedkoop) 3 keer, TUSD-USDT op kucoin (goedkoop) 2 keer, EURC-USD op cryptocom (duur) 2 keer.

**C2 met winst na kosten, per dag**

| Dag | Aantal (alle / MiCA / grijs) | Mediane winst bij €500 | Mediane duur |
|---|---|---|---|
| 2026-11-19 | 5 / 4 / 1 | €0,81 | 5 min |
| 2026-11-20 | 163 / 96 / 67 | €0,59 | 45 s |
| 2026-11-21 | 4 / 0 / 4 | €0,50 | 22 s |

| Inleg | Kan meedoen (alle / MiCA) | Minimum onbekend | Tegelijk open (hoogst) | Met één pot gepakt | Mediane winst per keer | Winst met één pot | Per week (GOK) |
|---|---|---|---|---|---|---|---|
| €100 | 172 / 100 | 0 | 5 | 89 | €0,13 | €15,66 | €84,17 |
| €150 | 172 / 100 | 0 | 5 | 89 | €0,20 | €23,25 | €124,96 |
| €200 | 172 / 100 | 0 | 5 | 89 | €0,26 | €30,25 | €162,58 |
| €500 | 172 / 100 | 0 | 5 | 89 | €0,65 | €71,63 | €384,96 |
| €2.000 | 172 / 100 | 0 | 5 | 89 | €2,42 | €264,99 | €1.424,19 |
| €5.000 | 172 / 100 | 0 | 5 | 90 | €5,03 | €556,56 | €2.991,22 |

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

