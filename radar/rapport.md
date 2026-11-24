# Kansenradar: rapport

Gemaakt 2026-11-24 00:53 UTC. Gemeten: **101,0 uur** in 23 run(s). Cijfers zijn GEZIEN (eigen metingen uit openbare API's), behalve waar GOK staat. Uitleg: `onderzoek/ai-handel/radar/README.md`.

## Het antwoord tot nu toe

- **A, nieuwe noteringen:** 38 nieuwe munten gezien, 0 echte prijsverschillen daarna; met één pot van €150 had je hier tot nu toe niets kunnen pakken.
- **B, funding-pieken:** 3826 pieken afgerond met spot en perp, waarvan 207 met winst na alle kosten bij €150; met één pot van €150 had je 16 keer kunnen instappen, samen -€5,90 (van €150 gaat €100 in de positie, GOK).
- **C1, stablecoin tussen beurzen:** 588 echte momenten; met één pot van €150 had je 99 keer kunnen instappen, samen -€33,37.
- **C2, stablecoin naast zijn gewone prijs:** 629 momenten met winst na kosten; met één pot van €150 had je 137 keer kunnen instappen, samen €32,00. Dit is geen arbitrage: je wint alleen als de koers terugkomt.

Alle sommen zijn een **bovengrens (GOK)**: we kijken elke 15 seconden tot 3 minuten, snelle partijen elke milliseconde. Wat we zien, is vaak al deels weg voor een gewone gebruiker zijn order plaatst. Apart gezet en niet geteld: 823 regels uit de eerste uren (oude code of het oude Kraken-tarief, zie onderaan).

## A. Nieuwe noteringen

Nieuwe munten op een beurs: **38** (waarvan 0 bij de eerste vergelijking na de start: die kunnen in het gat tussen twee runs genoteerd zijn); 21 stonden al op een andere beurs met dezelfde quote. Prijsverschillen daarna: 14, waarvan **0 echt**.

| Tijd | Beurs | Munt | Al op | Opnemen / storten op de nieuwe beurs |
|---|---|---|---|---|
| 11-20 14:01 | bitget (grijs) | CLEAR-USDT | mexc | open / open |
| 11-20 14:31 | kucoin | ANTX-USDT | gate, mexc, bingx | dicht / open |
| 11-20 15:04 | kraken | BFI-USD | - | open / open |
| 11-22 04:09 | mexc (grijs) | RINGS-USDT | - | onbekend / onbekend |
| 11-23 05:02 | poloniex (grijs) | SNDK-USDT | - | dicht / dicht |
| 11-23 05:32 | poloniex (grijs) | MU-USDT | - | dicht / open |
| 11-23 07:32 | htx (grijs) | MU-USDT | poloniex | dicht / open |
| 11-23 08:02 | kucoin | CLEAR-USDT | bitget, gate, mexc | dicht / open |
| 11-23 08:02 | gate | CLEAR-USDT | bitget, kucoin, mexc | dicht / open |
| 11-23 10:01 | poloniex (grijs) | RAXOL-USDT | - | dicht / open |
| 11-23 10:01 | xt (grijs) | ANTX-USDT | gate, kucoin, mexc, bingx | dicht / open |
| 11-23 10:01 | xt (grijs) | CLEAR-USDT | bitget, gate, kucoin, mexc | dicht / open |
| 11-23 15:30 | bitfinex (grijs) | CREST-USD | - | onbekend / onbekend |
| 11-23 15:30 | bitfinex (grijs) | CREST-USDT | - | onbekend / onbekend |
| 11-23 15:30 | bitfinex (grijs) | LBAF-USD | - | onbekend / onbekend |

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

Positieve pieken (boven 0,1% per 8 uur, uit onder 0,05% na minstens één verrekening): **3826 afgerond en te rekenen**. Verder: spotkoers onbekend 0, andere munt met dezelfde naam 148, geen spotmarkt 1899, onderbroken door een te lang gat tussen runs 0; negatieve pieken 8290 (dan moet je spot shorten, dat kan een particulier meestal niet). Open pieken gaan mee naar de volgende run, dus een piek betaalt maar één keer de kosten.

Som per piek: verrekende funding, min 4 keer takerkosten (spot in en uit, perp in en uit), plus of min het prijsverschil tussen spot en perp, min één keer overmaken (opname van USDT of USDC) als spot en perp op twee beurzen zitten. Inleg = 2/3 spot en 1/3 onderpand voor de short bij 2x hefboom (GOK). Bij 2x kan een sprong van ±50% de short liquideren; dat zit niet in de som.

| Begin | Perp | Munt | Spot | Hoogste funding per 8 uur | Ontvangen funding | Kosten | Prijsverschil | Overmaken | Netto | Winst bij €150 | Duur | Handel per dag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 11-20 16:08 | kraken | MNT | kraken | 4,00% | 7,22% (15 keer) | 1,70% | 2,71% | €0,00 | **8,23%** | €8,23 | 15,1 uur | $0,0 mln |
| 11-23 13:16 | gate | 牛逼 | mexc | 0,17% | 0,00% (1 keer) | 0,31% | 7,33% | €0,01 | **7,02%** | €7,01 | 62 min | $0,1 mln |
| 11-21 14:02 | kucoin | SPORTFUN | bingx | 0,24% | 0,05% (1 keer) | 0,32% | 6,74% | €0,01 | **6,48%** | €6,47 | 2,6 uur | $0,0 mln |
| 11-21 01:20 | kucoin | SPORTFUN | bingx | 2,10% | 1,05% (1 keer) | 0,32% | 3,25% | €0,01 | **3,98%** | €3,97 | 6,0 uur | $0,0 mln |
| 11-21 06:09 | kraken | AGLD | mexc | 0,54% | 0,01% (1 keer) | 0,26% | 4,12% | €0,01 | **3,87%** | €3,86 | 52 min | $0,0 mln |
| 11-21 06:17 | kraken | BB | mexc | 0,32% | 0,01% (1 keer) | 0,20% | 3,81% | €0,01 | **3,62%** | €3,61 | 52 min | $0,0 mln |
| 11-23 13:06 | kraken | IOTX | mexc | 0,11% | 0,01% (1 keer) | 0,20% | 3,79% | €0,01 | **3,60%** | €3,59 | 72 min | $0,0 mln |
| 11-21 06:09 | kraken | PIXEL | mexc | 0,17% | 0,01% (1 keer) | 0,20% | 3,54% | €0,01 | **3,35%** | €3,34 | 58 min | $0,0 mln |
| 11-23 17:04 | kraken | BRETT | bingx | 0,15% | 0,00% (1 keer) | 0,30% | 3,26% | €0,01 | **2,96%** | €2,95 | 56 min | $0,0 mln |
| 11-23 04:44 | kraken | AGLD | mexc | 4,00% | 1,09% (3 keer) | 0,26% | 2,10% | €0,01 | **2,94%** | €2,93 | 2,4 uur | $0,0 mln |

**Afgeronde pieken B, per dag**

| Dag | Aantal (alle / MiCA / grijs) | Mediane winst bij €500 | Mediane duur |
|---|---|---|---|
| 2026-11-19 | 231 / 127 / 104 | -€3,28 | 74 min |
| 2026-11-20 | 910 / 562 / 348 | -€3,57 | 94 min |
| 2026-11-21 | 910 / 565 / 345 | -€3,87 | 64 min |
| 2026-11-22 | 873 / 572 / 301 | -€3,56 | 2,0 uur |
| 2026-11-23 | 902 / 558 / 344 | -€3,84 | 60 min |

| Inleg | Kan meedoen (alle / MiCA) | Minimum onbekend | Tegelijk open (hoogst) | Met één pot gepakt | Mediane winst per keer | Winst met één pot | Per week (GOK) |
|---|---|---|---|---|---|---|---|
| €100 | 1265 / 1051 | 2557 | 126 | 16 | -€0,28 | -€3,94 | -€6,56 |
| €150 | 1269 / 1052 | 2557 | 126 | 16 | -€0,42 | -€5,90 | -€9,82 |
| €200 | 1269 / 1052 | 2557 | 126 | 16 | -€0,55 | -€7,85 | -€13,06 |
| €500 | 3826 / 2384 | 2557 | 182 | 38 | -€1,33 | -€56,83 | -€94,57 |
| €2.000 | 3826 / 2384 | 2557 | 182 | 38 | -€5,30 | -€226,68 | -€377,22 |
| €5.000 | 3826 / 2384 | 2557 | 182 | 38 | -€13,24 | -€566,43 | -€942,60 |

Met één pot: je pakt een moment als je geld vrij is, bij gelijke start het beste. "Tegelijk open" zegt hoeveel potten je nodig had om alles te pakken. Bij €100 tot €200 doet een moment alleen mee als de minimale bedragen bekend zijn en eronder liggen; vanaf €500 telt onbekend mee (meestal €1 tot €10).

Vergund bij B: perp- en spotbeurs hebben een MiCA-vergunning voor spot. Of de EU-dochter perps aan Nederlandse particulieren geeft, is niet nagekeken (GOK, vaak niet of beperkt). De som is lineair in de inleg (GOK): bij een dunne perp kost een grotere order meer dan de laatste prijs.

## C. Stablecoins

**C1, tussen beurzen** (dezelfde stablecoin goedkoper kopen dan elders verkopen, na alle kosten): 2770 momenten, waarvan **588 echt**.

**Echte momenten C1, per dag**

| Dag | Aantal (alle / MiCA / grijs) | Mediane winst bij €500 | Mediane duur |
|---|---|---|---|
| 2026-11-20 | 173 / 99 / 74 | €0,03 | 2 min |
| 2026-11-21 | 188 / 109 / 79 | €0,04 | 3 min |
| 2026-11-22 | 189 / 0 / 189 | €0,11 | 1 min |
| 2026-11-23 | 37 / 0 / 37 | €0,05 | 1 min |
| 2026-11-24 | 1 / 0 / 1 | €0,02 | 15 s |

| Inleg | Kan meedoen (alle / MiCA) | Minimum onbekend | Tegelijk open (hoogst) | Met één pot gepakt | Mediane winst per keer | Winst met één pot | Per week (GOK) |
|---|---|---|---|---|---|---|---|
| €100 | 171 / 39 | 417 | 3 | 99 | -€0,01 | -€39,26 | -€65,33 |
| €150 | 171 / 39 | 417 | 3 | 99 | -€0,01 | -€33,37 | -€55,53 |
| €200 | 171 / 39 | 417 | 3 | 99 | -€0,00 | -€27,49 | -€45,75 |
| €500 | 588 / 208 | 417 | 9 | 134 | €0,05 | €18,75 | €31,20 |
| €2.000 | 588 / 208 | 417 | 9 | 134 | €0,24 | €101,87 | €169,53 |
| €5.000 | 588 / 208 | 417 | 9 | 134 | €0,28 | €198,21 | €329,85 |

Met één pot: je pakt een moment als je geld vrij is, bij gelijke start het beste. "Tegelijk open" zegt hoeveel potten je nodig had om alles te pakken. Bij €100 tot €200 doet een moment alleen mee als de minimale bedragen bekend zijn en eronder liggen; vanaf €500 telt onbekend mee (meestal €1 tot €10).

**C2, naast de gewone prijs** (minstens 0,3% naast de basislijn: de mediaan per dag over de laatste 45 dagen): 1253 momenten met basislijn, waarvan 867 met minstens €100 op het boek en **629 met winst na 2 keer takerkosten** (bij de eerste meting). Zonder basislijn (munt te nieuw of geen bron, niet geteld): 19. Geen arbitrage: je wint alleen als de koers naar zijn gewone prijs terugkomt (GOK).

Meest gezien: EURQ-EUR op kraken (duur) 217 keer, USDC-USD op bitfinex (duur) 170 keer, USDQ-USD op kraken (duur) 131 keer, USDT-EUR op kucoin (duur) 130 keer, USDT-EUR op bitget (duur) 79 keer, USDC-EUR op bitget (duur) 46 keer, TUSD-USDT op kucoin (goedkoop) 27 keer, USDC-EUR op kucoin (duur) 17 keer.

**C2 met winst na kosten, per dag**

| Dag | Aantal (alle / MiCA / grijs) | Mediane winst bij €500 | Mediane duur |
|---|---|---|---|
| 2026-11-19 | 5 / 4 / 1 | €0,81 | 5 min |
| 2026-11-20 | 167 / 97 / 70 | €0,59 | 45 s |
| 2026-11-21 | 313 / 99 / 214 | €1,54 | 15 s |
| 2026-11-22 | 100 / 77 / 23 | €0,11 | 4 min |
| 2026-11-23 | 44 / 38 / 6 | €0,06 | 10 min |

| Inleg | Kan meedoen (alle / MiCA) | Minimum onbekend | Tegelijk open (hoogst) | Met één pot gepakt | Mediane winst per keer | Winst met één pot | Per week (GOK) |
|---|---|---|---|---|---|---|---|
| €100 | 627 / 315 | 2 | 8 | 142 | €0,11 | €22,01 | €36,63 |
| €150 | 627 / 315 | 2 | 8 | 137 | €0,16 | €32,00 | €53,25 |
| €200 | 627 / 315 | 2 | 8 | 137 | €0,20 | €38,86 | €64,66 |
| €500 | 629 / 315 | 2 | 8 | 137 | €0,50 | €78,72 | €130,99 |
| €2.000 | 629 / 315 | 2 | 8 | 124 | €1,88 | €250,82 | €417,39 |
| €5.000 | 629 / 315 | 2 | 8 | 125 | €2,42 | €493,41 | €821,08 |

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

