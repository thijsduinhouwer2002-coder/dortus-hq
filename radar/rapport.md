# Kansenradar: rapport

Gemaakt 2026-11-20 13:44 UTC. Gemeten: **21,4 uur** in 8 run(s). Cijfers zijn GEZIEN (eigen metingen uit openbare API's), behalve waar GOK staat. Uitleg: `platformen/ai-handel/radar/README.md`.

## Het antwoord tot nu toe

- **A, nieuwe noteringen:** 23 nieuwe munten gezien, 0 echte prijsverschillen daarna; met één pot van €150 had je hier tot nu toe niets kunnen pakken.
- **B, funding-pieken:** 600 pieken afgerond met spot en perp, waarvan 37 met winst na alle kosten bij €150; met één pot van €150 had je 1 keer kunnen instappen, samen -€0,10 (van €150 gaat €100 in de positie, GOK).
- **C1, stablecoin tussen beurzen:** 10 echte momenten; met één pot van €150 had je 5 keer kunnen instappen, samen €0,05.
- **C2, stablecoin naast zijn gewone prijs:** 15 momenten met winst na kosten; met één pot van €150 had je 14 keer kunnen instappen, samen €6,11. Dit is geen arbitrage: je wint alleen als de koers terugkomt.

Alle sommen zijn een **bovengrens (GOK)**: we kijken elke 15 seconden tot 3 minuten, snelle partijen elke milliseconde. Wat we zien, is vaak al deels weg voor een gewone gebruiker zijn order plaatst. Apart gezet en niet geteld: 823 regels uit de eerste uren (oude code of het oude Kraken-tarief, zie onderaan).

## A. Nieuwe noteringen

Nieuwe munten op een beurs: **23** (waarvan 0 bij de eerste vergelijking na de start: die kunnen in het gat tussen twee runs genoteerd zijn); 14 stonden al op een andere beurs met dezelfde quote. Prijsverschillen daarna: 6, waarvan **0 echt**.

| Tijd | Beurs | Munt | Al op | Opnemen / storten op de nieuwe beurs |
|---|---|---|---|---|
| 11-20 06:50 | mexc (grijs) | CLEAR-USDT | - | onbekend / onbekend |
| 11-20 07:02 | poloniex (grijs) | MMTSUI-USDT | - | dicht / open |
| 11-20 10:49 | xt (grijs) | ARB3L-USDT | gate | onbekend / onbekend |
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

Positieve pieken (boven 0,1% per 8 uur, uit onder 0,05% na minstens één verrekening): **600 afgerond en te rekenen**. Verder: spotkoers onbekend 0, andere munt met dezelfde naam 17, geen spotmarkt 362, onderbroken door een te lang gat tussen runs 0; negatieve pieken 1700 (dan moet je spot shorten, dat kan een particulier meestal niet). Open pieken gaan mee naar de volgende run, dus een piek betaalt maar één keer de kosten.

Som per piek: verrekende funding, min 4 keer takerkosten (spot in en uit, perp in en uit), plus of min het prijsverschil tussen spot en perp, min één keer overmaken (opname van USDT of USDC) als spot en perp op twee beurzen zitten. Inleg = 2/3 spot en 1/3 onderpand voor de short bij 2x hefboom (GOK). Bij 2x kan een sprong van ±50% de short liquideren; dat zit niet in de som.

| Begin | Perp | Munt | Spot | Hoogste funding per 8 uur | Ontvangen funding | Kosten | Prijsverschil | Overmaken | Netto | Winst bij €150 | Duur | Handel per dag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 11-19 19:03 | kraken | TREAD | kraken | 4,00% | -0,40% (1 keer) | 1,70% | 4,73% | €0,00 | **2,62%** | €2,62 | 90 min | $0,0 mln |
| 11-20 02:03 | kraken | ZIG | kraken | 2,74% | 0,76% (3 keer) | 1,70% | 3,53% | €0,00 | **2,59%** | €2,59 | 3,0 uur | $0,0 mln |
| 11-20 05:23 | kraken | CHILLGUY | mexc | 0,20% | 0,01% (1 keer) | 0,26% | 2,69% | €0,01 | **2,44%** | €2,43 | 50 min | $0,0 mln |
| 11-20 08:13 | bingx | MYX | bingx | 0,25% | 0,05% (1 keer) | 0,30% | 2,41% | €0,00 | **2,16%** | €2,16 | 3,8 uur | $0,8 mln |
| 11-19 16:21 | gate | 牛逼 | mexc | 3,51% | 1,95% (3 keer) | 0,31% | 0,42% | €0,01 | **2,06%** | €2,05 | 11,8 uur | $0,1 mln |
| 11-19 17:03 | kraken | TREAD | kraken | 4,00% | -0,40% (1 keer) | 1,70% | 4,05% | €0,00 | **1,94%** | €1,94 | 88 min | $0,0 mln |
| 11-20 08:43 | gate | KERNEL | gate | 4,00% | -0,88% (1 keer) | 0,55% | 3,16% | €0,00 | **1,73%** | €1,73 | 3,3 uur | $0,0 mln |
| 11-19 17:05 | kraken | CHILLGUY | mexc | 0,17% | 0,01% (1 keer) | 0,26% | 1,88% | €0,01 | **1,63%** | €1,62 | 78 min | $0,0 mln |
| 11-20 07:47 | kucoin | REKT | kucoin | 0,89% | 0,07% (2 keer) | 0,72% | 2,09% | €0,00 | **1,44%** | €1,44 | 74 min | $0,6 mln |
| 11-20 05:01 | kraken | ORDI | mexc | 0,14% | -0,01% (1 keer) | 0,20% | 1,04% | €0,01 | **0,84%** | €0,83 | 60 min | $0,0 mln |

**Afgeronde pieken B, per dag**

| Dag | Aantal (alle / MiCA / grijs) | Mediane winst bij €500 | Mediane duur |
|---|---|---|---|
| 2026-11-19 | 229 / 126 / 103 | -€3,33 | 74 min |
| 2026-11-20 | 371 / 222 / 149 | -€3,52 | 84 min |

| Inleg | Kan meedoen (alle / MiCA) | Minimum onbekend | Tegelijk open (hoogst) | Met één pot gepakt | Mediane winst per keer | Winst met één pot | Per week (GOK) |
|---|---|---|---|---|---|---|---|
| €100 | 196 / 182 | 404 | 70 | 1 | -€0,07 | -€0,07 | -€0,55 |
| €150 | 196 / 182 | 404 | 70 | 1 | -€0,10 | -€0,10 | -€0,78 |
| €200 | 196 / 182 | 404 | 70 | 1 | -€0,14 | -€0,14 | -€1,10 |
| €500 | 600 / 348 | 404 | 113 | 4 | -€1,08 | €3,24 | €25,41 |
| €2.000 | 600 / 348 | 404 | 113 | 4 | -€4,30 | €12,99 | €101,87 |
| €5.000 | 600 / 348 | 404 | 113 | 4 | -€10,73 | €32,51 | €254,95 |

Met één pot: je pakt een moment als je geld vrij is, bij gelijke start het beste. "Tegelijk open" zegt hoeveel potten je nodig had om alles te pakken. Bij €100 tot €200 doet een moment alleen mee als de minimale bedragen bekend zijn en eronder liggen; vanaf €500 telt onbekend mee (meestal €1 tot €10).

Vergund bij B: perp- en spotbeurs hebben een MiCA-vergunning voor spot. Of de EU-dochter perps aan Nederlandse particulieren geeft, is niet nagekeken (GOK, vaak niet of beperkt). De som is lineair in de inleg (GOK): bij een dunne perp kost een grotere order meer dan de laatste prijs.

## C. Stablecoins

**C1, tussen beurzen** (dezelfde stablecoin goedkoper kopen dan elders verkopen, na alle kosten): 817 momenten, waarvan **10 echt**.

**Echte momenten C1, per dag**

| Dag | Aantal (alle / MiCA / grijs) | Mediane winst bij €500 | Mediane duur |
|---|---|---|---|
| 2026-11-20 | 10 / 0 / 10 | €0,03 | 1 min |

| Inleg | Kan meedoen (alle / MiCA) | Minimum onbekend | Tegelijk open (hoogst) | Met één pot gepakt | Mediane winst per keer | Winst met één pot | Per week (GOK) |
|---|---|---|---|---|---|---|---|
| €100 | 5 / 0 | 5 | 1 | 5 | -€0,01 | €0,00 | €0,04 |
| €150 | 5 / 0 | 5 | 1 | 5 | -€0,01 | €0,05 | €0,41 |
| €200 | 5 / 0 | 5 | 1 | 5 | -€0,00 | €0,10 | €0,79 |
| €500 | 10 / 0 | 5 | 1 | 10 | €0,03 | €0,55 | €4,28 |
| €2.000 | 10 / 0 | 5 | 1 | 10 | €0,15 | €1,78 | €13,92 |
| €5.000 | 10 / 0 | 5 | 1 | 10 | €0,19 | €2,46 | €19,29 |

Met één pot: je pakt een moment als je geld vrij is, bij gelijke start het beste. "Tegelijk open" zegt hoeveel potten je nodig had om alles te pakken. Bij €100 tot €200 doet een moment alleen mee als de minimale bedragen bekend zijn en eronder liggen; vanaf €500 telt onbekend mee (meestal €1 tot €10).

**C2, naast de gewone prijs** (minstens 0,3% naast de basislijn: de mediaan per dag over de laatste 45 dagen): 267 momenten met basislijn, waarvan 16 met minstens €100 op het boek en **15 met winst na 2 keer takerkosten** (bij de eerste meting). Zonder basislijn (munt te nieuw of geen bron, niet geteld): 4. Geen arbitrage: je wint alleen als de koers naar zijn gewone prijs terugkomt (GOK).

Meest gezien: USDT-EUR op bitget (duur) 9 keer, TUSD-USDT op kucoin (goedkoop) 2 keer, EURC-USD op cryptocom (duur) 2 keer, PYUSD-USDT op htx (goedkoop) 2 keer, EURQ-USD op kraken (duur) 1 keer.

**C2 met winst na kosten, per dag**

| Dag | Aantal (alle / MiCA / grijs) | Mediane winst bij €500 | Mediane duur |
|---|---|---|---|
| 2026-11-19 | 5 / 4 / 1 | €0,81 | 5 min |
| 2026-11-20 | 10 / 1 / 9 | €0,50 | 1 min |

| Inleg | Kan meedoen (alle / MiCA) | Minimum onbekend | Tegelijk open (hoogst) | Met één pot gepakt | Mediane winst per keer | Winst met één pot | Per week (GOK) |
|---|---|---|---|---|---|---|---|
| €100 | 15 / 5 | 0 | 2 | 14 | €0,11 | €4,21 | €33,00 |
| €150 | 15 / 5 | 0 | 2 | 14 | €0,16 | €6,11 | €47,88 |
| €200 | 15 / 5 | 0 | 2 | 14 | €0,22 | €7,43 | €58,25 |
| €500 | 15 / 5 | 0 | 2 | 14 | €0,55 | €15,35 | €120,37 |
| €2.000 | 15 / 5 | 0 | 2 | 14 | €2,01 | €51,62 | €404,78 |
| €5.000 | 15 / 5 | 0 | 2 | 14 | €4,39 | €82,70 | €648,54 |

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

