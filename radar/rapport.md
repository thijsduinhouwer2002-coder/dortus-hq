# Kansenradar: rapport

Gemaakt 2026-11-19 16:35 UTC. Gemeten: **1,1 uur** in 4 run(s). Cijfers zijn GEZIEN (eigen metingen uit openbare API's), behalve waar GOK staat. Uitleg: `platformen/ai-handel/radar/README.md`.

## Het antwoord tot nu toe

- **A, nieuwe noteringen:** 0 nieuwe munten gezien, 0 echte prijsverschillen daarna; met één pot van €150 had je hier tot nu toe niets kunnen pakken.
- **B, funding-pieken:** 0 pieken afgerond met spot en perp, waarvan 0 met winst na alle kosten bij €150; met één pot van €150 had je hier tot nu toe niets kunnen pakken (van €150 gaat €100 in de positie, GOK).
- **C1, stablecoin tussen beurzen:** 0 echte momenten; met één pot van €150 had je hier tot nu toe niets kunnen pakken.
- **C2, stablecoin naast zijn gewone prijs:** 0 momenten met winst na kosten; met één pot van €150 had je hier tot nu toe niets kunnen pakken. Dit is geen arbitrage: je wint alleen als de koers terugkomt.

Alle sommen zijn een **bovengrens (GOK)**: we kijken elke 15 seconden tot 3 minuten, snelle partijen elke milliseconde. Wat we zien, is vaak al deels weg voor een gewone gebruiker zijn order plaatst. Apart gezet en niet geteld: 823 regels uit de eerste uren (oude code of het oude Kraken-tarief, zie onderaan).

## A. Nieuwe noteringen

Nieuwe munten op een beurs: **0** (waarvan 0 bij de eerste vergelijking na de start: die kunnen in het gat tussen twee runs genoteerd zijn); 0 stonden al op een andere beurs met dezelfde quote. Prijsverschillen daarna: 0, waarvan **0 echt**.

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

Positieve pieken (boven 0,1% per 8 uur, uit onder 0,05% na minstens één verrekening): **0 afgerond en te rekenen**. Verder: spotkoers onbekend 0, andere munt met dezelfde naam 0, geen spotmarkt 5, onderbroken door een te lang gat tussen runs 0; negatieve pieken 2 (dan moet je spot shorten, dat kan een particulier meestal niet). Open pieken gaan mee naar de volgende run, dus een piek betaalt maar één keer de kosten.

Som per piek: verrekende funding, min 4 keer takerkosten (spot in en uit, perp in en uit), plus of min het prijsverschil tussen spot en perp, min één keer overmaken (opname van USDT of USDC) als spot en perp op twee beurzen zitten. Inleg = 2/3 spot en 1/3 onderpand voor de short bij 2x hefboom (GOK). Bij 2x kan een sprong van ±50% de short liquideren; dat zit niet in de som.

**Afgeronde pieken B, per dag:** nog geen momenten.

| Inleg | Kan meedoen (alle / MiCA) | Minimum onbekend | Tegelijk open (hoogst) | Met één pot gepakt | Mediane winst per keer | Winst met één pot | Per week (GOK) |
|---|---|---|---|---|---|---|---|
| €100 | 0 / 0 | 0 | 0 | 0 | - | €0,00 | - |
| €150 | 0 / 0 | 0 | 0 | 0 | - | €0,00 | - |
| €200 | 0 / 0 | 0 | 0 | 0 | - | €0,00 | - |
| €500 | 0 / 0 | 0 | 0 | 0 | - | €0,00 | - |
| €2.000 | 0 / 0 | 0 | 0 | 0 | - | €0,00 | - |
| €5.000 | 0 / 0 | 0 | 0 | 0 | - | €0,00 | - |

Met één pot: je pakt een moment als je geld vrij is, bij gelijke start het beste. "Tegelijk open" zegt hoeveel potten je nodig had om alles te pakken. Bij €100 tot €200 doet een moment alleen mee als de minimale bedragen bekend zijn en eronder liggen; vanaf €500 telt onbekend mee (meestal €1 tot €10).

Vergund bij B: perp- en spotbeurs hebben een MiCA-vergunning voor spot. Of de EU-dochter perps aan Nederlandse particulieren geeft, is niet nagekeken (GOK, vaak niet of beperkt). De som is lineair in de inleg (GOK): bij een dunne perp kost een grotere order meer dan de laatste prijs.

## C. Stablecoins

**C1, tussen beurzen** (dezelfde stablecoin goedkoper kopen dan elders verkopen, na alle kosten): 78 momenten, waarvan **0 echt**.

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

**C2, naast de gewone prijs** (minstens 0,3% naast de basislijn: de mediaan per dag over de laatste 45 dagen): 6 momenten met basislijn, waarvan 0 met minstens €100 op het boek en **0 met winst na 2 keer takerkosten** (bij de eerste meting). Zonder basislijn (munt te nieuw of geen bron, niet geteld): 1. Geen arbitrage: je wint alleen als de koers naar zijn gewone prijs terugkomt (GOK).

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

