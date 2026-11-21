# Kansenradar: rapport

Gemaakt 2026-11-21 14:07 UTC. Gemeten: **44,4 uur** in 12 run(s). Cijfers zijn GEZIEN (eigen metingen uit openbare API's), behalve waar GOK staat. Uitleg: `platformen/ai-handel/radar/README.md`.

## Het antwoord tot nu toe

- **A, nieuwe noteringen:** 26 nieuwe munten gezien, 0 echte prijsverschillen daarna; met één pot van €150 had je hier tot nu toe niets kunnen pakken.
- **B, funding-pieken:** 1597 pieken afgerond met spot en perp, waarvan 103 met winst na alle kosten bij €150; met één pot van €150 had je 3 keer kunnen instappen, samen -€1,25 (van €150 gaat €100 in de positie, GOK).
- **C1, stablecoin tussen beurzen:** 342 echte momenten; met één pot van €150 had je 52 keer kunnen instappen, samen -€34,73.
- **C2, stablecoin naast zijn gewone prijs:** 443 momenten met winst na kosten; met één pot van €150 had je 62 keer kunnen instappen, samen €17,63. Dit is geen arbitrage: je wint alleen als de koers terugkomt.

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

Positieve pieken (boven 0,1% per 8 uur, uit onder 0,05% na minstens één verrekening): **1597 afgerond en te rekenen**. Verder: spotkoers onbekend 0, andere munt met dezelfde naam 63, geen spotmarkt 684, onderbroken door een te lang gat tussen runs 0; negatieve pieken 4368 (dan moet je spot shorten, dat kan een particulier meestal niet). Open pieken gaan mee naar de volgende run, dus een piek betaalt maar één keer de kosten.

Som per piek: verrekende funding, min 4 keer takerkosten (spot in en uit, perp in en uit), plus of min het prijsverschil tussen spot en perp, min één keer overmaken (opname van USDT of USDC) als spot en perp op twee beurzen zitten. Inleg = 2/3 spot en 1/3 onderpand voor de short bij 2x hefboom (GOK). Bij 2x kan een sprong van ±50% de short liquideren; dat zit niet in de som.

| Begin | Perp | Munt | Spot | Hoogste funding per 8 uur | Ontvangen funding | Kosten | Prijsverschil | Overmaken | Netto | Winst bij €150 | Duur | Handel per dag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 11-20 16:08 | kraken | MNT | kraken | 4,00% | 7,22% (15 keer) | 1,70% | 2,71% | €0,00 | **8,23%** | €8,23 | 15,1 uur | $0,0 mln |
| 11-21 01:20 | kucoin | SPORTFUN | bingx | 2,10% | 1,05% (1 keer) | 0,32% | 3,25% | €0,01 | **3,98%** | €3,97 | 6,0 uur | $0,0 mln |
| 11-21 06:09 | kraken | AGLD | mexc | 0,54% | 0,01% (1 keer) | 0,26% | 4,12% | €0,01 | **3,87%** | €3,86 | 52 min | $0,0 mln |
| 11-21 06:17 | kraken | BB | mexc | 0,32% | 0,01% (1 keer) | 0,20% | 3,81% | €0,01 | **3,62%** | €3,61 | 52 min | $0,0 mln |
| 11-21 06:09 | kraken | PIXEL | mexc | 0,17% | 0,01% (1 keer) | 0,20% | 3,54% | €0,01 | **3,35%** | €3,34 | 58 min | $0,0 mln |
| 11-20 18:12 | kraken | BRETT | bingx | 0,11% | 0,00% (1 keer) | 0,30% | 3,18% | €0,01 | **2,88%** | €2,87 | 48 min | $0,0 mln |
| 11-19 19:03 | kraken | TREAD | kraken | 4,00% | -0,40% (1 keer) | 1,70% | 4,73% | €0,00 | **2,62%** | €2,62 | 90 min | $0,0 mln |
| 11-20 02:03 | kraken | ZIG | kraken | 2,74% | 0,76% (3 keer) | 1,70% | 3,53% | €0,00 | **2,59%** | €2,59 | 3,0 uur | $0,0 mln |
| 11-20 05:23 | kraken | CHILLGUY | mexc | 0,20% | 0,01% (1 keer) | 0,26% | 2,69% | €0,01 | **2,44%** | €2,43 | 50 min | $0,0 mln |
| 11-20 15:03 | kraken | PIXEL | mexc | 0,69% | 0,04% (1 keer) | 0,20% | 2,35% | €0,01 | **2,20%** | €2,19 | 69 min | $0,0 mln |

**Afgeronde pieken B, per dag**

| Dag | Aantal (alle / MiCA / grijs) | Mediane winst bij €500 | Mediane duur |
|---|---|---|---|
| 2026-11-19 | 231 / 127 / 104 | -€3,28 | 74 min |
| 2026-11-20 | 908 / 561 / 347 | -€3,57 | 94 min |
| 2026-11-21 | 458 / 300 / 158 | -€4,00 | 58 min |

| Inleg | Kan meedoen (alle / MiCA) | Minimum onbekend | Tegelijk open (hoogst) | Met één pot gepakt | Mediane winst per keer | Winst met één pot | Per week (GOK) |
|---|---|---|---|---|---|---|---|
| €100 | 502 / 447 | 1093 | 97 | 3 | -€0,58 | -€0,83 | -€3,14 |
| €150 | 504 / 447 | 1093 | 98 | 3 | -€0,87 | -€1,25 | -€4,73 |
| €200 | 504 / 447 | 1093 | 98 | 3 | -€1,16 | -€1,66 | -€6,28 |
| €500 | 1597 / 988 | 1093 | 159 | 20 | -€1,25 | -€16,01 | -€60,53 |
| €2.000 | 1597 / 988 | 1093 | 159 | 20 | -€4,98 | -€63,62 | -€240,55 |
| €5.000 | 1597 / 988 | 1093 | 159 | 20 | -€12,45 | -€158,83 | -€600,55 |

Met één pot: je pakt een moment als je geld vrij is, bij gelijke start het beste. "Tegelijk open" zegt hoeveel potten je nodig had om alles te pakken. Bij €100 tot €200 doet een moment alleen mee als de minimale bedragen bekend zijn en eronder liggen; vanaf €500 telt onbekend mee (meestal €1 tot €10).

Vergund bij B: perp- en spotbeurs hebben een MiCA-vergunning voor spot. Of de EU-dochter perps aan Nederlandse particulieren geeft, is niet nagekeken (GOK, vaak niet of beperkt). De som is lineair in de inleg (GOK): bij een dunne perp kost een grotere order meer dan de laatste prijs.

## C. Stablecoins

**C1, tussen beurzen** (dezelfde stablecoin goedkoper kopen dan elders verkopen, na alle kosten): 1985 momenten, waarvan **342 echt**.

**Echte momenten C1, per dag**

| Dag | Aantal (alle / MiCA / grijs) | Mediane winst bij €500 | Mediane duur |
|---|---|---|---|
| 2026-11-20 | 173 / 99 / 74 | €0,03 | 2 min |
| 2026-11-21 | 169 / 109 / 60 | €0,03 | 2 min |

| Inleg | Kan meedoen (alle / MiCA) | Minimum onbekend | Tegelijk open (hoogst) | Met één pot gepakt | Mediane winst per keer | Winst met één pot | Per week (GOK) |
|---|---|---|---|---|---|---|---|
| €100 | 81 / 39 | 261 | 3 | 52 | -€0,92 | -€39,29 | -€148,57 |
| €150 | 81 / 39 | 261 | 3 | 52 | -€0,87 | -€34,73 | -€131,31 |
| €200 | 81 / 39 | 261 | 3 | 52 | -€0,83 | -€30,18 | -€114,12 |
| €500 | 342 / 208 | 261 | 9 | 87 | €0,03 | €8,57 | €32,42 |
| €2.000 | 342 / 208 | 261 | 9 | 87 | €0,32 | €64,13 | €242,50 |
| €5.000 | 342 / 208 | 261 | 9 | 87 | €0,40 | €126,76 | €479,29 |

Met één pot: je pakt een moment als je geld vrij is, bij gelijke start het beste. "Tegelijk open" zegt hoeveel potten je nodig had om alles te pakken. Bij €100 tot €200 doet een moment alleen mee als de minimale bedragen bekend zijn en eronder liggen; vanaf €500 telt onbekend mee (meestal €1 tot €10).

**C2, naast de gewone prijs** (minstens 0,3% naast de basislijn: de mediaan per dag over de laatste 45 dagen): 746 momenten met basislijn, waarvan 450 met minstens €100 op het boek en **443 met winst na 2 keer takerkosten** (bij de eerste meting). Zonder basislijn (munt te nieuw of geen bron, niet geteld): 9. Geen arbitrage: je wint alleen als de koers naar zijn gewone prijs terugkomt (GOK).

Meest gezien: USDC-USD op bitfinex (duur) 170 keer, USDT-EUR op kucoin (duur) 130 keer, USDT-EUR op bitget (duur) 68 keer, USDC-EUR op kucoin (duur) 17 keer, USDC-EUR op bitget (duur) 17 keer, TUSD-USDT op kucoin (goedkoop) 14 keer, USDQ-USD op kraken (duur) 9 keer, PYUSD-USDT op htx (goedkoop) 6 keer.

**C2 met winst na kosten, per dag**

| Dag | Aantal (alle / MiCA / grijs) | Mediane winst bij €500 | Mediane duur |
|---|---|---|---|
| 2026-11-19 | 5 / 4 / 1 | €0,81 | 5 min |
| 2026-11-20 | 167 / 97 / 70 | €0,59 | 45 s |
| 2026-11-21 | 271 / 76 / 195 | €1,59 | 15 s |

| Inleg | Kan meedoen (alle / MiCA) | Minimum onbekend | Tegelijk open (hoogst) | Met één pot gepakt | Mediane winst per keer | Winst met één pot | Per week (GOK) |
|---|---|---|---|---|---|---|---|
| €100 | 443 / 177 | 0 | 8 | 62 | €0,12 | €11,91 | €45,02 |
| €150 | 443 / 177 | 0 | 8 | 62 | €0,19 | €17,63 | €66,67 |
| €200 | 443 / 177 | 0 | 8 | 62 | €0,25 | €22,76 | €86,04 |
| €500 | 443 / 177 | 0 | 8 | 62 | €0,62 | €52,93 | €200,14 |
| €2.000 | 443 / 177 | 0 | 8 | 62 | €2,33 | €190,93 | €721,92 |
| €5.000 | 443 / 177 | 0 | 8 | 63 | €4,90 | €383,08 | €1.448,43 |

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

