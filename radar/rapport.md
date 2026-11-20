# Kansenradar: rapport

Gemaakt 2026-11-20 11:13 UTC. Gemeten: **18,9 uur** in 8 run(s). Cijfers zijn GEZIEN (eigen metingen uit openbare API's), behalve waar GOK staat. Uitleg: `platformen/ai-handel/radar/README.md`.

## Het antwoord tot nu toe

- **A, nieuwe noteringen:** 17 nieuwe munten gezien, 0 echte prijsverschillen daarna; met één pot van €150 had je hier tot nu toe niets kunnen pakken.
- **B, funding-pieken:** 493 pieken afgerond met spot en perp, waarvan 29 met winst na alle kosten bij €150; met één pot van €150 had je 3 keer kunnen instappen, samen -€1,65 (van €150 gaat €100 in de positie, GOK).
- **C1, stablecoin tussen beurzen:** 5 echte momenten; met één pot van €150 had je 5 keer kunnen instappen, samen €0,05.
- **C2, stablecoin naast zijn gewone prijs:** 6 momenten met winst na kosten; met één pot van €150 had je 5 keer kunnen instappen, samen €4,68. Dit is geen arbitrage: je wint alleen als de koers terugkomt.

Alle sommen zijn een **bovengrens (GOK)**: we kijken elke 15 seconden tot 3 minuten, snelle partijen elke milliseconde. Wat we zien, is vaak al deels weg voor een gewone gebruiker zijn order plaatst. Apart gezet en niet geteld: 823 regels uit de eerste uren (oude code of het oude Kraken-tarief, zie onderaan).

## A. Nieuwe noteringen

Nieuwe munten op een beurs: **17** (waarvan 0 bij de eerste vergelijking na de start: die kunnen in het gat tussen twee runs genoteerd zijn); 8 stonden al op een andere beurs met dezelfde quote. Prijsverschillen daarna: 3, waarvan **0 echt**.

| Tijd | Beurs | Munt | Al op | Opnemen / storten op de nieuwe beurs |
|---|---|---|---|---|
| 11-19 18:32 | okx | XANT-USDC | - | onbekend / onbekend |
| 11-19 19:41 | gate | ANTX-USDT | - | dicht / open |
| 11-20 02:32 | bingx | ANTB-USDT | - | onbekend / onbekend |
| 11-20 02:32 | bingx | ANTX-USDT | gate | onbekend / onbekend |
| 11-20 04:44 | mexc (grijs) | FIONA-USDT | - | onbekend / onbekend |
| 11-20 06:02 | bingx | MUSEBOOK-USDT | gate, poloniex | onbekend / onbekend |
| 11-20 06:50 | mexc (grijs) | CLEAR-USDT | - | onbekend / onbekend |
| 11-20 07:02 | poloniex (grijs) | MMTSUI-USDT | - | dicht / open |
| 11-20 10:49 | xt (grijs) | ARB3L-USDT | gate | onbekend / onbekend |
| 11-20 10:49 | xt (grijs) | DUSK3S-USDT | - | onbekend / onbekend |
| 11-20 10:49 | xt (grijs) | GALA3L-USDT | gate | onbekend / onbekend |
| 11-20 10:49 | xt (grijs) | OP3L-USDT | gate | onbekend / onbekend |
| 11-20 10:49 | xt (grijs) | SHIB3L-USDT | gate | onbekend / onbekend |
| 11-20 10:49 | xt (grijs) | SOL3L-USDT | gate | onbekend / onbekend |
| 11-20 10:49 | xt (grijs) | XPL3S-USDT | gate | onbekend / onbekend |

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

Positieve pieken (boven 0,1% per 8 uur, uit onder 0,05% na minstens één verrekening): **493 afgerond en te rekenen**. Verder: spotkoers onbekend 0, andere munt met dezelfde naam 16, geen spotmarkt 324, onderbroken door een te lang gat tussen runs 0; negatieve pieken 1519 (dan moet je spot shorten, dat kan een particulier meestal niet). Open pieken gaan mee naar de volgende run, dus een piek betaalt maar één keer de kosten.

Som per piek: verrekende funding, min 4 keer takerkosten (spot in en uit, perp in en uit), plus of min het prijsverschil tussen spot en perp, min één keer overmaken (opname van USDT of USDC) als spot en perp op twee beurzen zitten. Inleg = 2/3 spot en 1/3 onderpand voor de short bij 2x hefboom (GOK). Bij 2x kan een sprong van ±50% de short liquideren; dat zit niet in de som.

| Begin | Perp | Munt | Spot | Hoogste funding per 8 uur | Ontvangen funding | Kosten | Prijsverschil | Overmaken | Netto | Winst bij €150 | Duur | Handel per dag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 11-19 19:03 | kraken | TREAD | kraken | 4,00% | -0,40% (1 keer) | 1,70% | 4,73% | €0,00 | **2,62%** | €2,62 | 90 min | $0,0 mln |
| 11-20 02:03 | kraken | ZIG | kraken | 2,74% | 0,76% (3 keer) | 1,70% | 3,53% | €0,00 | **2,59%** | €2,59 | 3,0 uur | $0,0 mln |
| 11-20 05:23 | kraken | CHILLGUY | mexc | 0,20% | 0,01% (1 keer) | 0,26% | 2,69% | €0,01 | **2,44%** | €2,43 | 50 min | $0,0 mln |
| 11-19 16:21 | gate | 牛逼 | mexc | 3,51% | 1,95% (3 keer) | 0,31% | 0,42% | €0,01 | **2,06%** | €2,05 | 11,8 uur | $0,1 mln |
| 11-19 17:03 | kraken | TREAD | kraken | 4,00% | -0,40% (1 keer) | 1,70% | 4,05% | €0,00 | **1,94%** | €1,94 | 88 min | $0,0 mln |
| 11-19 17:05 | kraken | CHILLGUY | mexc | 0,17% | 0,01% (1 keer) | 0,26% | 1,88% | €0,01 | **1,63%** | €1,62 | 78 min | $0,0 mln |
| 11-20 07:47 | kucoin | REKT | kucoin | 0,89% | 0,07% (2 keer) | 0,72% | 2,09% | €0,00 | **1,44%** | €1,44 | 74 min | $0,6 mln |
| 11-20 05:01 | kraken | ORDI | mexc | 0,14% | -0,01% (1 keer) | 0,20% | 1,04% | €0,01 | **0,84%** | €0,83 | 60 min | $0,0 mln |
| 11-19 20:15 | kraken | GOAT | kraken | 0,13% | 0,01% (1 keer) | 1,70% | 2,48% | €0,00 | **0,79%** | €0,79 | 74 min | $0,0 mln |
| 11-19 22:21 | kraken | PIXEL | mexc | 0,16% | 0,00% (1 keer) | 0,20% | 0,97% | €0,01 | **0,77%** | €0,76 | 40 min | $0,0 mln |

**Afgeronde pieken B, per dag**

| Dag | Aantal (alle / MiCA / grijs) | Mediane winst bij €500 | Mediane duur |
|---|---|---|---|
| 2026-11-19 | 228 / 125 / 103 | -€3,33 | 74 min |
| 2026-11-20 | 265 / 153 / 112 | -€3,73 | 70 min |

| Inleg | Kan meedoen (alle / MiCA) | Minimum onbekend | Tegelijk open (hoogst) | Met één pot gepakt | Mediane winst per keer | Winst met één pot | Per week (GOK) |
|---|---|---|---|---|---|---|---|
| €100 | 150 / 137 | 343 | 69 | 3 | -€0,27 | -€1,10 | -€9,77 |
| €150 | 150 / 137 | 343 | 69 | 3 | -€0,41 | -€1,65 | -€14,65 |
| €200 | 150 / 137 | 343 | 69 | 3 | -€0,54 | -€2,19 | -€19,44 |
| €500 | 493 / 278 | 343 | 112 | 5 | -€2,17 | -€8,70 | -€77,25 |
| €2.000 | 493 / 278 | 343 | 112 | 5 | -€8,67 | -€34,70 | -€308,10 |
| €5.000 | 493 / 278 | 343 | 112 | 5 | -€21,65 | -€86,67 | -€769,53 |

Met één pot: je pakt een moment als je geld vrij is, bij gelijke start het beste. "Tegelijk open" zegt hoeveel potten je nodig had om alles te pakken. Bij €100 tot €200 doet een moment alleen mee als de minimale bedragen bekend zijn en eronder liggen; vanaf €500 telt onbekend mee (meestal €1 tot €10).

Vergund bij B: perp- en spotbeurs hebben een MiCA-vergunning voor spot. Of de EU-dochter perps aan Nederlandse particulieren geeft, is niet nagekeken (GOK, vaak niet of beperkt). De som is lineair in de inleg (GOK): bij een dunne perp kost een grotere order meer dan de laatste prijs.

## C. Stablecoins

**C1, tussen beurzen** (dezelfde stablecoin goedkoper kopen dan elders verkopen, na alle kosten): 690 momenten, waarvan **5 echt**.

**Echte momenten C1, per dag**

| Dag | Aantal (alle / MiCA / grijs) | Mediane winst bij €500 | Mediane duur |
|---|---|---|---|
| 2026-11-20 | 5 / 0 / 5 | €0,02 | 2 min |

| Inleg | Kan meedoen (alle / MiCA) | Minimum onbekend | Tegelijk open (hoogst) | Met één pot gepakt | Mediane winst per keer | Winst met één pot | Per week (GOK) |
|---|---|---|---|---|---|---|---|
| €100 | 5 / 0 | 0 | 1 | 5 | -€0,01 | €0,00 | €0,04 |
| €150 | 5 / 0 | 0 | 1 | 5 | -€0,01 | €0,05 | €0,47 |
| €200 | 5 / 0 | 0 | 1 | 5 | -€0,00 | €0,10 | €0,89 |
| €500 | 5 / 0 | 0 | 1 | 5 | €0,02 | €0,39 | €3,45 |
| €2.000 | 5 / 0 | 0 | 1 | 5 | €0,15 | €1,18 | €10,52 |
| €5.000 | 5 / 0 | 0 | 1 | 5 | €0,19 | €1,47 | €13,07 |

Met één pot: je pakt een moment als je geld vrij is, bij gelijke start het beste. "Tegelijk open" zegt hoeveel potten je nodig had om alles te pakken. Bij €100 tot €200 doet een moment alleen mee als de minimale bedragen bekend zijn en eronder liggen; vanaf €500 telt onbekend mee (meestal €1 tot €10).

**C2, naast de gewone prijs** (minstens 0,3% naast de basislijn: de mediaan per dag over de laatste 45 dagen): 257 momenten met basislijn, waarvan 7 met minstens €100 op het boek en **6 met winst na 2 keer takerkosten** (bij de eerste meting). Zonder basislijn (munt te nieuw of geen bron, niet geteld): 4. Geen arbitrage: je wint alleen als de koers naar zijn gewone prijs terugkomt (GOK).

Meest gezien: TUSD-USDT op kucoin (goedkoop) 2 keer, EURC-USD op cryptocom (duur) 2 keer, PYUSD-USDT op htx (goedkoop) 2 keer, EURQ-USD op kraken (duur) 1 keer.

**C2 met winst na kosten, per dag**

| Dag | Aantal (alle / MiCA / grijs) | Mediane winst bij €500 | Mediane duur |
|---|---|---|---|
| 2026-11-19 | 5 / 4 / 1 | €0,81 | 5 min |
| 2026-11-20 | 1 / 1 / 0 | €0,01 | 6 min |

| Inleg | Kan meedoen (alle / MiCA) | Minimum onbekend | Tegelijk open (hoogst) | Met één pot gepakt | Mediane winst per keer | Winst met één pot | Per week (GOK) |
|---|---|---|---|---|---|---|---|
| €100 | 6 / 5 | 0 | 2 | 5 | €0,16 | €3,26 | €28,94 |
| €150 | 6 / 5 | 0 | 2 | 5 | €0,25 | €4,68 | €41,58 |
| €200 | 6 / 5 | 0 | 2 | 5 | €0,33 | €5,53 | €49,10 |
| €500 | 6 / 5 | 0 | 2 | 5 | €0,81 | €10,61 | €94,24 |
| €2.000 | 6 / 5 | 0 | 2 | 5 | €1,80 | €33,20 | €294,79 |
| €5.000 | 6 / 5 | 0 | 2 | 5 | €1,80 | €40,88 | €362,95 |

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

