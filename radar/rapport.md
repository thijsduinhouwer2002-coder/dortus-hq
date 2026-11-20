# Kansenradar: rapport

Gemaakt 2026-11-20 00:17 UTC. Gemeten: **8,6 uur** in 6 run(s). Cijfers zijn GEZIEN (eigen metingen uit openbare API's), behalve waar GOK staat. Uitleg: `platformen/ai-handel/radar/README.md`.

## Het antwoord tot nu toe

- **A, nieuwe noteringen:** 4 nieuwe munten gezien, 0 echte prijsverschillen daarna; met één pot van €150 had je hier tot nu toe niets kunnen pakken.
- **B, funding-pieken:** 193 pieken afgerond met spot en perp, waarvan 13 met winst na alle kosten bij €150; met één pot van €150 had je 1 keer kunnen instappen, samen -€0,53 (van €150 gaat €100 in de positie, GOK).
- **C1, stablecoin tussen beurzen:** 0 echte momenten; met één pot van €150 had je hier tot nu toe niets kunnen pakken.
- **C2, stablecoin naast zijn gewone prijs:** 3 momenten met winst na kosten; met één pot van €150 had je 3 keer kunnen instappen, samen €4,43. Dit is geen arbitrage: je wint alleen als de koers terugkomt.

Alle sommen zijn een **bovengrens (GOK)**: we kijken elke 15 seconden tot 3 minuten, snelle partijen elke milliseconde. Wat we zien, is vaak al deels weg voor een gewone gebruiker zijn order plaatst. Apart gezet en niet geteld: 823 regels uit de eerste uren (oude code of het oude Kraken-tarief, zie onderaan).

## A. Nieuwe noteringen

Nieuwe munten op een beurs: **4** (waarvan 0 bij de eerste vergelijking na de start: die kunnen in het gat tussen twee runs genoteerd zijn); 0 stonden al op een andere beurs met dezelfde quote. Prijsverschillen daarna: 0, waarvan **0 echt**.

| Tijd | Beurs | Munt | Al op | Opnemen / storten op de nieuwe beurs |
|---|---|---|---|---|
| 11-19 18:02 | gate | ANTON-USDT | - | dicht / open |
| 11-19 18:32 | okx | XANT-USDT | - | onbekend / onbekend |
| 11-19 18:32 | okx | XANT-USDC | - | onbekend / onbekend |
| 11-19 19:41 | gate | ANTX-USDT | - | dicht / open |

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

Positieve pieken (boven 0,1% per 8 uur, uit onder 0,05% na minstens één verrekening): **193 afgerond en te rekenen**. Verder: spotkoers onbekend 0, andere munt met dezelfde naam 6, geen spotmarkt 118, onderbroken door een te lang gat tussen runs 0; negatieve pieken 696 (dan moet je spot shorten, dat kan een particulier meestal niet). Open pieken gaan mee naar de volgende run, dus een piek betaalt maar één keer de kosten.

Som per piek: verrekende funding, min 4 keer takerkosten (spot in en uit, perp in en uit), plus of min het prijsverschil tussen spot en perp, min één keer overmaken (opname van USDT of USDC) als spot en perp op twee beurzen zitten. Inleg = 2/3 spot en 1/3 onderpand voor de short bij 2x hefboom (GOK). Bij 2x kan een sprong van ±50% de short liquideren; dat zit niet in de som.

| Begin | Perp | Munt | Spot | Hoogste funding per 8 uur | Ontvangen funding | Kosten | Prijsverschil | Overmaken | Netto | Winst bij €150 | Duur | Handel per dag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 11-19 19:03 | kraken | TREAD | kraken | 4,00% | -0,40% (1 keer) | 1,70% | 4,73% | €0,00 | **2,62%** | €2,62 | 90 min | $0,0 mln |
| 11-19 17:03 | kraken | TREAD | kraken | 4,00% | -0,40% (1 keer) | 1,70% | 4,05% | €0,00 | **1,94%** | €1,94 | 88 min | $0,0 mln |
| 11-19 17:05 | kraken | CHILLGUY | mexc | 0,17% | 0,01% (1 keer) | 0,26% | 1,88% | €0,01 | **1,63%** | €1,62 | 78 min | $0,0 mln |
| 11-19 20:15 | kraken | GOAT | kraken | 0,13% | 0,01% (1 keer) | 1,70% | 2,48% | €0,00 | **0,79%** | €0,79 | 74 min | $0,0 mln |
| 11-19 22:21 | kraken | PIXEL | mexc | 0,16% | 0,00% (1 keer) | 0,20% | 0,97% | €0,01 | **0,77%** | €0,76 | 40 min | $0,0 mln |
| 11-19 21:03 | kraken | TREAD | kraken | 4,00% | -0,40% (1 keer) | 1,70% | 2,56% | €0,00 | **0,46%** | €0,46 | 90 min | $0,0 mln |
| 11-19 17:05 | kraken | PEOPLE | mexc | 0,11% | 0,00% (1 keer) | 0,26% | 0,67% | €0,01 | **0,41%** | €0,40 | 56 min | $0,0 mln |
| 11-19 16:47 | bingx | BULLA | mexc | 0,12% | 0,02% (1 keer) | 0,26% | 0,52% | €0,01 | **0,28%** | €0,27 | 3,2 uur | $1,6 mln |
| 11-19 16:41 | mexc | BULLA | mexc | 0,12% | 0,02% (1 keer) | 0,20% | 0,43% | €0,00 | **0,25%** | €0,25 | 3,3 uur | $1,0 mln |
| 11-19 17:37 | gate | MANTRA | gate | 0,31% | 0,04% (1 keer) | 0,55% | 0,73% | €0,00 | **0,22%** | €0,22 | 2,4 uur | $0,3 mln |

**Afgeronde pieken B, per dag**

| Dag | Aantal (alle / MiCA / grijs) | Mediane winst bij €500 | Mediane duur |
|---|---|---|---|
| 2026-11-19 | 193 / 103 / 90 | -€3,50 | 64 min |

| Inleg | Kan meedoen (alle / MiCA) | Minimum onbekend | Tegelijk open (hoogst) | Met één pot gepakt | Mediane winst per keer | Winst met één pot | Per week (GOK) |
|---|---|---|---|---|---|---|---|
| €100 | 49 / 44 | 144 | 32 | 1 | -€0,35 | -€0,35 | -€6,85 |
| €150 | 49 / 44 | 144 | 32 | 1 | -€0,53 | -€0,53 | -€10,37 |
| €200 | 49 / 44 | 144 | 32 | 1 | -€0,71 | -€0,71 | -€13,89 |
| €500 | 193 / 103 | 144 | 61 | 2 | -€2,47 | -€4,94 | -€96,65 |
| €2.000 | 193 / 103 | 144 | 61 | 2 | -€9,88 | -€19,75 | -€386,40 |
| €5.000 | 193 / 103 | 144 | 61 | 2 | -€24,68 | -€49,36 | -€965,71 |

Met één pot: je pakt een moment als je geld vrij is, bij gelijke start het beste. "Tegelijk open" zegt hoeveel potten je nodig had om alles te pakken. Bij €100 tot €200 doet een moment alleen mee als de minimale bedragen bekend zijn en eronder liggen; vanaf €500 telt onbekend mee (meestal €1 tot €10).

Vergund bij B: perp- en spotbeurs hebben een MiCA-vergunning voor spot. Of de EU-dochter perps aan Nederlandse particulieren geeft, is niet nagekeken (GOK, vaak niet of beperkt). De som is lineair in de inleg (GOK): bij een dunne perp kost een grotere order meer dan de laatste prijs.

## C. Stablecoins

**C1, tussen beurzen** (dezelfde stablecoin goedkoper kopen dan elders verkopen, na alle kosten): 321 momenten, waarvan **0 echt**.

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

**C2, naast de gewone prijs** (minstens 0,3% naast de basislijn: de mediaan per dag over de laatste 45 dagen): 230 momenten met basislijn, waarvan 4 met minstens €100 op het boek en **3 met winst na 2 keer takerkosten** (bij de eerste meting). Zonder basislijn (munt te nieuw of geen bron, niet geteld): 2. Geen arbitrage: je wint alleen als de koers naar zijn gewone prijs terugkomt (GOK).

Meest gezien: EURC-USD op cryptocom (duur) 2 keer, TUSD-USDT op kucoin (goedkoop) 1 keer, PYUSD-USDT op htx (goedkoop) 1 keer.

**C2 met winst na kosten, per dag**

| Dag | Aantal (alle / MiCA / grijs) | Mediane winst bij €500 | Mediane duur |
|---|---|---|---|
| 2026-11-19 | 3 / 3 / 0 | €2,13 | 2 min |

| Inleg | Kan meedoen (alle / MiCA) | Minimum onbekend | Tegelijk open (hoogst) | Met één pot gepakt | Mediane winst per keer | Winst met één pot | Per week (GOK) |
|---|---|---|---|---|---|---|---|
| €100 | 3 / 3 | 0 | 1 | 3 | €1,42 | €3,09 | €60,42 |
| €150 | 3 / 3 | 0 | 1 | 3 | €2,13 | €4,43 | €86,70 |
| €200 | 3 / 3 | 0 | 1 | 3 | €2,13 | €5,20 | €101,70 |
| €500 | 3 / 3 | 0 | 1 | 3 | €2,13 | €9,80 | €191,71 |
| €2.000 | 3 / 3 | 0 | 1 | 3 | €2,13 | €31,40 | €614,33 |
| €5.000 | 3 / 3 | 0 | 1 | 3 | €2,13 | €39,08 | €764,52 |

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

