# Kansenradar: rapport

Gemaakt 2026-11-19 18:05 UTC. Gemeten: **2,6 uur** in 5 run(s). Cijfers zijn GEZIEN (eigen metingen uit openbare API's), behalve waar GOK staat. Uitleg: `platformen/ai-handel/radar/README.md`.

## Het antwoord tot nu toe

- **A, nieuwe noteringen:** 1 nieuwe munten gezien, 0 echte prijsverschillen daarna; met één pot van €150 had je hier tot nu toe niets kunnen pakken.
- **B, funding-pieken:** 25 pieken afgerond met spot en perp, waarvan 2 met winst na alle kosten bij €150; met één pot van €150 had je hier tot nu toe niets kunnen pakken (van €150 gaat €100 in de positie, GOK).
- **C1, stablecoin tussen beurzen:** 0 echte momenten; met één pot van €150 had je hier tot nu toe niets kunnen pakken.
- **C2, stablecoin naast zijn gewone prijs:** 0 momenten met winst na kosten; met één pot van €150 had je hier tot nu toe niets kunnen pakken. Dit is geen arbitrage: je wint alleen als de koers terugkomt.

Alle sommen zijn een **bovengrens (GOK)**: we kijken elke 15 seconden tot 3 minuten, snelle partijen elke milliseconde. Wat we zien, is vaak al deels weg voor een gewone gebruiker zijn order plaatst. Apart gezet en niet geteld: 823 regels uit de eerste uren (oude code of het oude Kraken-tarief, zie onderaan).

## A. Nieuwe noteringen

Nieuwe munten op een beurs: **1** (waarvan 0 bij de eerste vergelijking na de start: die kunnen in het gat tussen twee runs genoteerd zijn); 0 stonden al op een andere beurs met dezelfde quote. Prijsverschillen daarna: 0, waarvan **0 echt**.

| Tijd | Beurs | Munt | Al op | Opnemen / storten op de nieuwe beurs |
|---|---|---|---|---|
| 11-19 18:02 | gate | ANTON-USDT | - | dicht / open |

**Echte momenten A, per dag:** nog geen momenten.

| Inleg | Kan meedoen (alle / MiCA) | Minimum onbekend | Tegelijk open (hoogst) | Met één pot gepakt | Mediane winst per keer | Winst met één pot | Per week (GOK) |
|---|---|---|---|---|---|---|---|
| €100 | 0 / 0 | 0 | 0 | 0 | - | €0,00 | - |
| €150 | 0 / 0 | 0 | 0 | 0 | - | €0,00 | - |
| €200 | 0 / 0 | 0 | 0 | 0 | - | €0,00 | - |
| €500 | 0 / 0 | 0 | 0 | 0 | - | €0,00 | - |
| €2.000 | 0 / 0 | 0 | 0 | 0 | - | €0,00 | - |
| €5.000 | 0 / 0 | 0 | 0 | 0 | - | €0,00 | - |

Met één pot: je pakt een moment als je geld vrij is, bij gelijke start het beste. "Tegelijk open" zegt hoeveel potten je nodig had om alles te pakken. Bij €100 tot €200 doet een moment alleen mee als de minimale bedragen bekend zijn en eronder liggen; vanaf €500 telt onbekend mee (meestal €1 tot €10).

## B. Funding-pieken

Positieve pieken (boven 0,1% per 8 uur, uit onder 0,05% na minstens één verrekening): **25 afgerond en te rekenen**. Verder: spotkoers onbekend 0, andere munt met dezelfde naam 2, geen spotmarkt 25, onderbroken door een te lang gat tussen runs 0; negatieve pieken 100 (dan moet je spot shorten, dat kan een particulier meestal niet). Open pieken gaan mee naar de volgende run, dus een piek betaalt maar één keer de kosten.

Som per piek: verrekende funding, min 4 keer takerkosten (spot in en uit, perp in en uit), plus of min het prijsverschil tussen spot en perp, min één keer overmaken (opname van USDT of USDC) als spot en perp op twee beurzen zitten. Inleg = 2/3 spot en 1/3 onderpand voor de short bij 2x hefboom (GOK). Bij 2x kan een sprong van ±50% de short liquideren; dat zit niet in de som.

| Begin | Perp | Munt | Spot | Hoogste funding per 8 uur | Ontvangen funding | Kosten | Prijsverschil | Overmaken | Netto | Winst bij €150 | Duur | Handel per dag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 11-19 17:05 | kraken | PEOPLE | mexc | 0,11% | 0,00% (1 keer) | 0,26% | 0,67% | €0,01 | **0,41%** | €0,40 | 56 min | $0,0 mln |
| 11-19 16:29 | kraken | BB | mexc | 0,12% | 0,01% (1 keer) | 0,20% | 0,34% | €0,01 | **0,15%** | €0,14 | 33 min | $0,0 mln |
| 11-19 16:25 | kraken | INTC | htx | 0,22% | 0,00% (1 keer) | 0,50% | 0,24% | €0,01 | **-0,26%** | -€0,27 | 37 min | $0,8 mln |
| 11-19 16:23 | hyperliquid | RESOLV | mexc | 0,10% | 0,01% (1 keer) | 0,25% | -0,12% | €0,01 | **-0,36%** | -€0,37 | 45 min | $0,0 mln |
| 11-19 17:09 | kraken | METAX | mexc | 0,11% | 0,00% (1 keer) | 0,26% | -0,13% | €0,01 | **-0,39%** | -€0,40 | 52 min | $1,2 mln |
| 11-19 16:37 | kraken | SKHY | htx | 0,19% | 0,00% (1 keer) | 0,50% | -0,07% | €0,01 | **-0,56%** | -€0,57 | 24 min | $2,1 mln |
| 11-19 17:03 | kraken | AGLD | mexc | 0,17% | -0,02% (1 keer) | 0,26% | -0,30% | €0,01 | **-0,57%** | -€0,58 | 58 min | $0,0 mln |
| 11-19 16:23 | kraken | AMD | htx | 0,22% | 0,01% (1 keer) | 0,50% | -0,27% | €0,01 | **-0,76%** | -€0,77 | 39 min | $0,5 mln |
| 11-19 16:21 | kraken | NBIS | htx | 0,19% | 0,00% (1 keer) | 0,50% | -0,43% | €0,01 | **-0,93%** | -€0,94 | 41 min | $0,4 mln |
| 11-19 17:17 | kraken | GALA | kraken | 0,13% | 0,01% (1 keer) | 1,70% | 0,75% | €0,00 | **-0,94%** | -€0,94 | 44 min | $0,1 mln |

**Afgeronde pieken B, per dag**

| Dag | Aantal (alle / MiCA / grijs) | Mediane winst bij €500 | Mediane duur |
|---|---|---|---|
| 2026-11-19 | 25 / 11 / 14 | -€4,48 | 44 min |

| Inleg | Kan meedoen (alle / MiCA) | Minimum onbekend | Tegelijk open (hoogst) | Met één pot gepakt | Mediane winst per keer | Winst met één pot | Per week (GOK) |
|---|---|---|---|---|---|---|---|
| €100 | 0 / 0 | 25 | 0 | 0 | - | €0,00 | - |
| €150 | 0 / 0 | 25 | 0 | 0 | - | €0,00 | - |
| €200 | 0 / 0 | 25 | 0 | 0 | - | €0,00 | - |
| €500 | 25 / 11 | 25 | 13 | 2 | -€5,96 | -€11,91 | - |
| €2.000 | 25 / 11 | 25 | 13 | 2 | -€23,81 | -€47,62 | - |
| €5.000 | 25 / 11 | 25 | 13 | 2 | -€59,52 | -€119,03 | - |

Met één pot: je pakt een moment als je geld vrij is, bij gelijke start het beste. "Tegelijk open" zegt hoeveel potten je nodig had om alles te pakken. Bij €100 tot €200 doet een moment alleen mee als de minimale bedragen bekend zijn en eronder liggen; vanaf €500 telt onbekend mee (meestal €1 tot €10).

Vergund bij B: perp- en spotbeurs hebben een MiCA-vergunning voor spot. Of de EU-dochter perps aan Nederlandse particulieren geeft, is niet nagekeken (GOK, vaak niet of beperkt). De som is lineair in de inleg (GOK): bij een dunne perp kost een grotere order meer dan de laatste prijs.

## C. Stablecoins

**C1, tussen beurzen** (dezelfde stablecoin goedkoper kopen dan elders verkopen, na alle kosten): 153 momenten, waarvan **0 echt**.

**Echte momenten C1, per dag:** nog geen momenten.

| Inleg | Kan meedoen (alle / MiCA) | Minimum onbekend | Tegelijk open (hoogst) | Met één pot gepakt | Mediane winst per keer | Winst met één pot | Per week (GOK) |
|---|---|---|---|---|---|---|---|
| €100 | 0 / 0 | 0 | 0 | 0 | - | €0,00 | - |
| €150 | 0 / 0 | 0 | 0 | 0 | - | €0,00 | - |
| €200 | 0 / 0 | 0 | 0 | 0 | - | €0,00 | - |
| €500 | 0 / 0 | 0 | 0 | 0 | - | €0,00 | - |
| €2.000 | 0 / 0 | 0 | 0 | 0 | - | €0,00 | - |
| €5.000 | 0 / 0 | 0 | 0 | 0 | - | €0,00 | - |

Met één pot: je pakt een moment als je geld vrij is, bij gelijke start het beste. "Tegelijk open" zegt hoeveel potten je nodig had om alles te pakken. Bij €100 tot €200 doet een moment alleen mee als de minimale bedragen bekend zijn en eronder liggen; vanaf €500 telt onbekend mee (meestal €1 tot €10).

**C2, naast de gewone prijs** (minstens 0,3% naast de basislijn: de mediaan per dag over de laatste 45 dagen): 9 momenten met basislijn, waarvan 0 met minstens €100 op het boek en **0 met winst na 2 keer takerkosten** (bij de eerste meting). Zonder basislijn (munt te nieuw of geen bron, niet geteld): 1. Geen arbitrage: je wint alleen als de koers naar zijn gewone prijs terugkomt (GOK).

**C2 met winst na kosten, per dag:** nog geen momenten.

| Inleg | Kan meedoen (alle / MiCA) | Minimum onbekend | Tegelijk open (hoogst) | Met één pot gepakt | Mediane winst per keer | Winst met één pot | Per week (GOK) |
|---|---|---|---|---|---|---|---|
| €100 | 0 / 0 | 0 | 0 | 0 | - | €0,00 | - |
| €150 | 0 / 0 | 0 | 0 | 0 | - | €0,00 | - |
| €200 | 0 / 0 | 0 | 0 | 0 | - | €0,00 | - |
| €500 | 0 / 0 | 0 | 0 | 0 | - | €0,00 | - |
| €2.000 | 0 / 0 | 0 | 0 | 0 | - | €0,00 | - |
| €5.000 | 0 / 0 | 0 | 0 | 0 | - | €0,00 | - |

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

