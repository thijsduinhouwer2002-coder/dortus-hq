# Kansenradar: rapport

Gemaakt 2026-11-20 02:47 UTC. Gemeten: **11,1 uur** in 6 run(s). Cijfers zijn GEZIEN (eigen metingen uit openbare API's), behalve waar GOK staat. Uitleg: `platformen/ai-handel/radar/README.md`.

## Het antwoord tot nu toe

- **A, nieuwe noteringen:** 6 nieuwe munten gezien, 0 echte prijsverschillen daarna; met één pot van €150 had je hier tot nu toe niets kunnen pakken.
- **B, funding-pieken:** 264 pieken afgerond met spot en perp, waarvan 14 met winst na alle kosten bij €150; met één pot van €150 had je 1 keer kunnen instappen, samen -€0,45 (van €150 gaat €100 in de positie, GOK).
- **C1, stablecoin tussen beurzen:** 0 echte momenten; met één pot van €150 had je hier tot nu toe niets kunnen pakken.
- **C2, stablecoin naast zijn gewone prijs:** 5 momenten met winst na kosten; met één pot van €150 had je 4 keer kunnen instappen, samen €4,68. Dit is geen arbitrage: je wint alleen als de koers terugkomt.

Alle sommen zijn een **bovengrens (GOK)**: we kijken elke 15 seconden tot 3 minuten, snelle partijen elke milliseconde. Wat we zien, is vaak al deels weg voor een gewone gebruiker zijn order plaatst. Apart gezet en niet geteld: 823 regels uit de eerste uren (oude code of het oude Kraken-tarief, zie onderaan).

## A. Nieuwe noteringen

Nieuwe munten op een beurs: **6** (waarvan 0 bij de eerste vergelijking na de start: die kunnen in het gat tussen twee runs genoteerd zijn); 1 stonden al op een andere beurs met dezelfde quote. Prijsverschillen daarna: 1, waarvan **0 echt**.

| Tijd | Beurs | Munt | Al op | Opnemen / storten op de nieuwe beurs |
|---|---|---|---|---|
| 11-19 18:02 | gate | ANTON-USDT | - | dicht / open |
| 11-19 18:32 | okx | XANT-USDT | - | onbekend / onbekend |
| 11-19 18:32 | okx | XANT-USDC | - | onbekend / onbekend |
| 11-19 19:41 | gate | ANTX-USDT | - | dicht / open |
| 11-20 02:32 | bingx | ANTB-USDT | - | onbekend / onbekend |
| 11-20 02:32 | bingx | ANTX-USDT | gate | onbekend / onbekend |

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

Positieve pieken (boven 0,1% per 8 uur, uit onder 0,05% na minstens één verrekening): **264 afgerond en te rekenen**. Verder: spotkoers onbekend 0, andere munt met dezelfde naam 10, geen spotmarkt 187, onderbroken door een te lang gat tussen runs 0; negatieve pieken 839 (dan moet je spot shorten, dat kan een particulier meestal niet). Open pieken gaan mee naar de volgende run, dus een piek betaalt maar één keer de kosten.

Som per piek: verrekende funding, min 4 keer takerkosten (spot in en uit, perp in en uit), plus of min het prijsverschil tussen spot en perp, min één keer overmaken (opname van USDT of USDC) als spot en perp op twee beurzen zitten. Inleg = 2/3 spot en 1/3 onderpand voor de short bij 2x hefboom (GOK). Bij 2x kan een sprong van ±50% de short liquideren; dat zit niet in de som.

| Begin | Perp | Munt | Spot | Hoogste funding per 8 uur | Ontvangen funding | Kosten | Prijsverschil | Overmaken | Netto | Winst bij €150 | Duur | Handel per dag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 11-19 19:03 | kraken | TREAD | kraken | 4,00% | -0,40% (1 keer) | 1,70% | 4,73% | €0,00 | **2,62%** | €2,62 | 90 min | $0,0 mln |
| 11-19 17:03 | kraken | TREAD | kraken | 4,00% | -0,40% (1 keer) | 1,70% | 4,05% | €0,00 | **1,94%** | €1,94 | 88 min | $0,0 mln |
| 11-19 17:05 | kraken | CHILLGUY | mexc | 0,17% | 0,01% (1 keer) | 0,26% | 1,88% | €0,01 | **1,63%** | €1,62 | 78 min | $0,0 mln |
| 11-19 20:15 | kraken | GOAT | kraken | 0,13% | 0,01% (1 keer) | 1,70% | 2,48% | €0,00 | **0,79%** | €0,79 | 74 min | $0,0 mln |
| 11-19 22:21 | kraken | PIXEL | mexc | 0,16% | 0,00% (1 keer) | 0,20% | 0,97% | €0,01 | **0,77%** | €0,76 | 40 min | $0,0 mln |
| 11-19 18:41 | kraken | CHILLGUY | mexc | 0,19% | 0,08% (6 keer) | 0,26% | 0,85% | €0,01 | **0,66%** | €0,65 | 5,7 uur | $0,0 mln |
| 11-19 21:03 | kraken | TREAD | kraken | 4,00% | -0,40% (1 keer) | 1,70% | 2,56% | €0,00 | **0,46%** | €0,46 | 90 min | $0,0 mln |
| 11-19 17:05 | kraken | PEOPLE | mexc | 0,11% | 0,00% (1 keer) | 0,26% | 0,67% | €0,01 | **0,41%** | €0,40 | 56 min | $0,0 mln |
| 11-19 16:47 | bingx | BULLA | mexc | 0,12% | 0,02% (1 keer) | 0,26% | 0,52% | €0,01 | **0,28%** | €0,27 | 3,2 uur | $1,6 mln |
| 11-19 16:41 | mexc | BULLA | mexc | 0,12% | 0,02% (1 keer) | 0,20% | 0,43% | €0,00 | **0,25%** | €0,25 | 3,3 uur | $1,0 mln |

**Afgeronde pieken B, per dag**

| Dag | Aantal (alle / MiCA / grijs) | Mediane winst bij €500 | Mediane duur |
|---|---|---|---|
| 2026-11-19 | 221 / 121 / 100 | -€3,35 | 72 min |
| 2026-11-20 | 43 / 23 / 20 | -€4,91 | 54 min |

| Inleg | Kan meedoen (alle / MiCA) | Minimum onbekend | Tegelijk open (hoogst) | Met één pot gepakt | Mediane winst per keer | Winst met één pot | Per week (GOK) |
|---|---|---|---|---|---|---|---|
| €100 | 64 / 56 | 200 | 35 | 1 | -€0,30 | -€0,30 | -€4,55 |
| €150 | 64 / 56 | 200 | 35 | 1 | -€0,45 | -€0,45 | -€6,82 |
| €200 | 64 / 56 | 200 | 35 | 1 | -€0,60 | -€0,60 | -€9,09 |
| €500 | 264 / 144 | 200 | 69 | 2 | -€1,81 | -€3,62 | -€54,85 |
| €2.000 | 264 / 144 | 200 | 69 | 2 | -€7,24 | -€14,47 | -€219,26 |
| €5.000 | 264 / 144 | 200 | 69 | 2 | -€18,08 | -€36,16 | -€547,93 |

Met één pot: je pakt een moment als je geld vrij is, bij gelijke start het beste. "Tegelijk open" zegt hoeveel potten je nodig had om alles te pakken. Bij €100 tot €200 doet een moment alleen mee als de minimale bedragen bekend zijn en eronder liggen; vanaf €500 telt onbekend mee (meestal €1 tot €10).

Vergund bij B: perp- en spotbeurs hebben een MiCA-vergunning voor spot. Of de EU-dochter perps aan Nederlandse particulieren geeft, is niet nagekeken (GOK, vaak niet of beperkt). De som is lineair in de inleg (GOK): bij een dunne perp kost een grotere order meer dan de laatste prijs.

## C. Stablecoins

**C1, tussen beurzen** (dezelfde stablecoin goedkoper kopen dan elders verkopen, na alle kosten): 464 momenten, waarvan **0 echt**.

**Echte momenten C1, per dag:** nog geen momenten.

| Inleg | Kan meedoen (alle / MiCA) | Minimum onbekend | Tegelijk open (hoogst) | Met één pot gepakt | Mediane winst per keer | Winst met één pot | Per week (GOK) |
|---|---|---|---|---|---|---|---|
| €100 | 0 / 0 | 0 | 0 | 0 | - | €0,00 | €0,00 |
| €150 | 0 / 0 | 0 | 0 | 0 | - | €0,00 | €0,00 |
| €200 | 0 / 0 | 0 | 0 | 0 | - | €0,00 | €0,00 |
| €500 | 0 / 0 | 0 | 0 | 0 | - | €0,00 | €0,00 |
| €2.000 | 0 / 0 | 0 | 0 | 0 | - | €0,00 | €0,00 |
| €5.000 | 0 / 0 | 0 | 0 | 0 | - | €0,00 | €0,00 |

Met één pot: je pakt een moment als je geld vrij is, bij gelijke start het beste. "Tegelijk open" zegt hoeveel potten je nodig had om alles te pakken. Bij €100 tot €200 doet een moment alleen mee als de minimale bedragen bekend zijn en eronder liggen; vanaf €500 telt onbekend mee (meestal €1 tot €10).

**C2, naast de gewone prijs** (minstens 0,3% naast de basislijn: de mediaan per dag over de laatste 45 dagen): 239 momenten met basislijn, waarvan 6 met minstens €100 op het boek en **5 met winst na 2 keer takerkosten** (bij de eerste meting). Zonder basislijn (munt te nieuw of geen bron, niet geteld): 2. Geen arbitrage: je wint alleen als de koers naar zijn gewone prijs terugkomt (GOK).

Meest gezien: TUSD-USDT op kucoin (goedkoop) 2 keer, EURC-USD op cryptocom (duur) 2 keer, PYUSD-USDT op htx (goedkoop) 2 keer.

**C2 met winst na kosten, per dag**

| Dag | Aantal (alle / MiCA / grijs) | Mediane winst bij €500 | Mediane duur |
|---|---|---|---|
| 2026-11-19 | 5 / 4 / 1 | €0,81 | 5 min |

| Inleg | Kan meedoen (alle / MiCA) | Minimum onbekend | Tegelijk open (hoogst) | Met één pot gepakt | Mediane winst per keer | Winst met één pot | Per week (GOK) |
|---|---|---|---|---|---|---|---|
| €100 | 5 / 4 | 0 | 2 | 4 | €0,79 | €3,25 | €49,29 |
| €150 | 5 / 4 | 0 | 2 | 4 | €1,19 | €4,68 | €70,87 |
| €200 | 5 / 4 | 0 | 2 | 4 | €1,23 | €5,52 | €83,71 |
| €500 | 5 / 4 | 0 | 2 | 4 | €1,47 | €10,61 | €160,74 |
| €2.000 | 5 / 4 | 0 | 2 | 4 | €1,96 | €33,20 | €503,01 |
| €5.000 | 5 / 4 | 0 | 2 | 4 | €1,96 | €40,87 | €619,34 |

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

