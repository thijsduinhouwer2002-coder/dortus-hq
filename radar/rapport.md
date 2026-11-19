# Kansenradar: rapport

Gemaakt 2026-11-19 19:05 UTC. Gemeten: **3,6 uur** in 5 run(s). Cijfers zijn GEZIEN (eigen metingen uit openbare API's), behalve waar GOK staat. Uitleg: `platformen/ai-handel/radar/README.md`.

## Het antwoord tot nu toe

- **A, nieuwe noteringen:** 3 nieuwe munten gezien, 0 echte prijsverschillen daarna; met één pot van €150 had je hier tot nu toe niets kunnen pakken.
- **B, funding-pieken:** 44 pieken afgerond met spot en perp, waarvan 5 met winst na alle kosten bij €150; met één pot van €150 had je 1 keer kunnen instappen, samen -€0,76 (van €150 gaat €100 in de positie, GOK).
- **C1, stablecoin tussen beurzen:** 0 echte momenten; met één pot van €150 had je hier tot nu toe niets kunnen pakken.
- **C2, stablecoin naast zijn gewone prijs:** 2 momenten met winst na kosten; met één pot van €150 had je 2 keer kunnen instappen, samen €2,30. Dit is geen arbitrage: je wint alleen als de koers terugkomt.

Alle sommen zijn een **bovengrens (GOK)**: we kijken elke 15 seconden tot 3 minuten, snelle partijen elke milliseconde. Wat we zien, is vaak al deels weg voor een gewone gebruiker zijn order plaatst. Apart gezet en niet geteld: 823 regels uit de eerste uren (oude code of het oude Kraken-tarief, zie onderaan).

## A. Nieuwe noteringen

Nieuwe munten op een beurs: **3** (waarvan 0 bij de eerste vergelijking na de start: die kunnen in het gat tussen twee runs genoteerd zijn); 0 stonden al op een andere beurs met dezelfde quote. Prijsverschillen daarna: 0, waarvan **0 echt**.

| Tijd | Beurs | Munt | Al op | Opnemen / storten op de nieuwe beurs |
|---|---|---|---|---|
| 11-19 18:02 | gate | ANTON-USDT | - | dicht / open |
| 11-19 18:32 | okx | XANT-USDT | - | onbekend / onbekend |
| 11-19 18:32 | okx | XANT-USDC | - | onbekend / onbekend |

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

Positieve pieken (boven 0,1% per 8 uur, uit onder 0,05% na minstens één verrekening): **44 afgerond en te rekenen**. Verder: spotkoers onbekend 0, andere munt met dezelfde naam 3, geen spotmarkt 37, onderbroken door een te lang gat tussen runs 0; negatieve pieken 161 (dan moet je spot shorten, dat kan een particulier meestal niet). Open pieken gaan mee naar de volgende run, dus een piek betaalt maar één keer de kosten.

Som per piek: verrekende funding, min 4 keer takerkosten (spot in en uit, perp in en uit), plus of min het prijsverschil tussen spot en perp, min één keer overmaken (opname van USDT of USDC) als spot en perp op twee beurzen zitten. Inleg = 2/3 spot en 1/3 onderpand voor de short bij 2x hefboom (GOK). Bij 2x kan een sprong van ±50% de short liquideren; dat zit niet in de som.

| Begin | Perp | Munt | Spot | Hoogste funding per 8 uur | Ontvangen funding | Kosten | Prijsverschil | Overmaken | Netto | Winst bij €150 | Duur | Handel per dag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 11-19 17:03 | kraken | TREAD | kraken | 4,00% | -0,40% (1 keer) | 1,70% | 4,05% | €0,00 | **1,94%** | €1,94 | 88 min | $0,0 mln |
| 11-19 17:05 | kraken | CHILLGUY | mexc | 0,17% | 0,01% (1 keer) | 0,26% | 1,88% | €0,01 | **1,63%** | €1,62 | 78 min | $0,0 mln |
| 11-19 17:05 | kraken | PEOPLE | mexc | 0,11% | 0,00% (1 keer) | 0,26% | 0,67% | €0,01 | **0,41%** | €0,40 | 56 min | $0,0 mln |
| 11-19 18:17 | kraken | CSPR | kraken | 4,00% | 0,50% (1 keer) | 1,70% | 1,35% | €0,00 | **0,15%** | €0,15 | 44 min | $0,0 mln |
| 11-19 16:29 | kraken | BB | mexc | 0,12% | 0,01% (1 keer) | 0,20% | 0,34% | €0,01 | **0,15%** | €0,14 | 33 min | $0,0 mln |
| 11-19 18:03 | kraken | SKHY | htx | 0,16% | 0,01% (1 keer) | 0,50% | 0,32% | €0,01 | **-0,17%** | -€0,18 | 58 min | $2,3 mln |
| 11-19 16:25 | kraken | INTC | htx | 0,22% | 0,00% (1 keer) | 0,50% | 0,24% | €0,01 | **-0,26%** | -€0,27 | 37 min | $0,8 mln |
| 11-19 16:23 | hyperliquid | RESOLV | mexc | 0,10% | 0,01% (1 keer) | 0,25% | -0,12% | €0,01 | **-0,36%** | -€0,37 | 45 min | $0,0 mln |
| 11-19 18:03 | kraken | PIXEL | mexc | 0,28% | 0,03% (1 keer) | 0,20% | -0,19% | €0,01 | **-0,36%** | -€0,37 | 62 min | $0,0 mln |
| 11-19 17:09 | kraken | METAX | mexc | 0,11% | 0,00% (1 keer) | 0,26% | -0,13% | €0,01 | **-0,39%** | -€0,40 | 52 min | $1,2 mln |

**Afgeronde pieken B, per dag**

| Dag | Aantal (alle / MiCA / grijs) | Mediane winst bij €500 | Mediane duur |
|---|---|---|---|
| 2026-11-19 | 44 / 21 / 23 | -€4,22 | 52 min |

| Inleg | Kan meedoen (alle / MiCA) | Minimum onbekend | Tegelijk open (hoogst) | Met één pot gepakt | Mediane winst per keer | Winst met één pot | Per week (GOK) |
|---|---|---|---|---|---|---|---|
| €100 | 1 / 1 | 43 | 1 | 1 | -€0,51 | -€0,51 | -€23,90 |
| €150 | 1 / 1 | 43 | 1 | 1 | -€0,76 | -€0,76 | -€35,61 |
| €200 | 1 / 1 | 43 | 1 | 1 | -€1,01 | -€1,01 | -€47,32 |
| €500 | 44 / 21 | 43 | 17 | 3 | -€3,10 | -€14,44 | -€676,58 |
| €2.000 | 44 / 21 | 43 | 17 | 3 | -€12,37 | -€57,72 | -€2.704,45 |
| €5.000 | 44 / 21 | 43 | 17 | 3 | -€30,90 | -€144,28 | -€6.760,19 |

Met één pot: je pakt een moment als je geld vrij is, bij gelijke start het beste. "Tegelijk open" zegt hoeveel potten je nodig had om alles te pakken. Bij €100 tot €200 doet een moment alleen mee als de minimale bedragen bekend zijn en eronder liggen; vanaf €500 telt onbekend mee (meestal €1 tot €10).

Vergund bij B: perp- en spotbeurs hebben een MiCA-vergunning voor spot. Of de EU-dochter perps aan Nederlandse particulieren geeft, is niet nagekeken (GOK, vaak niet of beperkt). De som is lineair in de inleg (GOK): bij een dunne perp kost een grotere order meer dan de laatste prijs.

## C. Stablecoins

**C1, tussen beurzen** (dezelfde stablecoin goedkoper kopen dan elders verkopen, na alle kosten): 192 momenten, waarvan **0 echt**.

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

**C2, naast de gewone prijs** (minstens 0,3% naast de basislijn: de mediaan per dag over de laatste 45 dagen): 23 momenten met basislijn, waarvan 2 met minstens €100 op het boek en **2 met winst na 2 keer takerkosten** (bij de eerste meting). Zonder basislijn (munt te nieuw of geen bron, niet geteld): 1. Geen arbitrage: je wint alleen als de koers naar zijn gewone prijs terugkomt (GOK).

Meest gezien: TUSD-USDT op kucoin (goedkoop) 1 keer, EURC-USD op cryptocom (duur) 1 keer.

**C2 met winst na kosten, per dag**

| Dag | Aantal (alle / MiCA / grijs) | Mediane winst bij €500 | Mediane duur |
|---|---|---|---|
| 2026-11-19 | 2 / 2 / 0 | €3,83 | 3 min |

| Inleg | Kan meedoen (alle / MiCA) | Minimum onbekend | Tegelijk open (hoogst) | Met één pot gepakt | Mediane winst per keer | Winst met één pot | Per week (GOK) |
|---|---|---|---|---|---|---|---|
| €100 | 2 / 2 | 0 | 1 | 2 | €0,77 | €1,53 | €71,85 |
| €150 | 2 / 2 | 0 | 1 | 2 | €1,15 | €2,30 | €107,78 |
| €200 | 2 / 2 | 0 | 1 | 2 | €1,53 | €3,07 | €143,71 |
| €500 | 2 / 2 | 0 | 1 | 2 | €3,83 | €7,67 | €359,26 |
| €2.000 | 2 / 2 | 0 | 1 | 2 | €14,63 | €29,27 | €1.371,39 |
| €5.000 | 2 / 2 | 0 | 1 | 2 | €18,47 | €36,95 | €1.731,08 |

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

