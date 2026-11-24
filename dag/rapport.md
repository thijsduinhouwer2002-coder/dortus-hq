# Schaduwbot Polymarket: rapport

Denkbeeldige makerbot in jonge temperatuurmarkten. Geen account, geen geld, niets geplaatst. Beloning = GOK (formule van Polymarket; voor de concurrentie een ondergrens en een hoge schatting). Vullingen en verlies = GEZIEN (echte trades en gemeten midden), behalve waar GOK staat.

**Met €150: netto $-1.32 tot $1.94 per dag (GOK)**, in 2 gemiddelde markten tegelijk (variant 1c, ondergrens tot hoge schatting van de beloning, min het verlies op vullingen).

Gemeten: 23 runs, 7724 minuten (128.7 uur) (GEZIEN). Markten in de data: 3464. Uitslag bekend voor 2464 markten.

## Variant 1c (orders op 1 cent van het midden)

| Dag (UTC) | Minuten gemeten | Markten gem. | Orders op het boek gem. | Hoogste stand voorraadgeld | Beloning ondergrens tot hoge schatting (GOK) | Vullingen los / streng | Gevuld | Resultaat vullingen 1 uur later | Tegen uitslag | Netto (ondergrens tot hoge schatting, alleen vullingen met prijs 1 uur later) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-19 | 895 | 245 | $4,642 | $4,694 | $220 tot $466 | 2987 / 2103 | $9,892 | $-203 (14 nog zonder prijs) | $-543 (2987 van 2987 beslist) | $16.92 tot $262 |
| 2026-11-20 | 1420 | 254 | $4,828 | $9,026 | $410 tot $843 | 4074 / 2965 | $13,129 | $-370 (114 nog zonder prijs) | $-325 (4074 van 4074 beslist) | $40.19 tot $473 |
| 2026-11-21 | 1410 | 216 | $4,096 | $10,171 | $343 tot $704 | 4798 / 3271 | $15,012 | $-538 (97 nog zonder prijs) | $-427 (4798 van 4798 beslist) | $-195 tot $166 |
| 2026-11-22 | 1432 | 191 | $3,616 | $9,582 | $352 tot $709 | 4422 / 3346 | $14,301 | $-490 (36 nog zonder prijs) | $147 (3720 van 4422 beslist) | $-138 tot $220 |
| 2026-11-23 | 1432 | 168 | $3,195 | $8,779 | $329 tot $661 | 4847 / 3681 | $15,405 | $-400 (38 nog zonder prijs) | $-63.20 (1624 van 4847 beslist) | $-71.36 tot $261 |
| 2026-11-24 | 1135 | 161 | $3,010 | $7,728 | $242 tot $497 | 3432 / 2423 | $11,636 | $-234 (176 nog zonder prijs) | $0.00 (0 van 3432 beslist) | $7.41 tot $263 |
| **Totaal** | 7724 | | $3,878 | $10,171 | $1,896 tot $3,880 | 24560 / 17789 | $79,376 | $-2,235 | $-1,211 | $-339 tot $1,645 |

Resultaat vullingen 5 minuten later (vroege aanwijzing, GEZIEN): $-1,674 over 24511 vullingen en $79,232, dus -2.11% per gevulde dollar.

Verlies per gevulde dollar, 1 uur later: -2.86% over $78,086 (GEZIEN; B mat −1,05% voor alle makers binnen 1 cent, D −0,1 tot −0,3% voor alle makers in temperatuurmarkten). Alleen strenge vullingen: -3.72%.

**Opgeschaald (GOK):** per dag $-70.16 (ondergrens) tot $300 (hoge schatting) netto (gemeten minuten × 1440 / 7724).

475 van de 24560 vullingen ($1,290) hebben nog geen prijs 1 uur later. Die tellen niet als 0: hun verlies is geschat met het verlies per dollar van de andere vullingen (1 uur later, -2.86%): $-36.92 (GOK).

Geld dat de bot nodig had: gemiddeld $3,878 in open orders plus de hoogste stand van $10,171 vastzittend in gevulde voorraad tot de uitslag (JA en NEE per markt tegen elkaar weggestreept; vrij ±30 uur na het begin van de dag, GOK) = **$14,049**. De voorraad groeit tot de eerste markten beslist zijn (2 tot 3 dagen na de start), dus tot dan is dit getal te laag.

| Inleg | Te gebruiken (× 1.0 $/€, hooguit orders plus voorraad) | Netto over 90 dagen (GOK) |
|---|---|---|
| €2,000 | $2,000 | $-899 tot $3,842 |
| €5,000 | $5,000 | $-2,247 tot $9,605 |

Opschalen gaat lineair met het geld dat de bot nodig had (orders plus voorraad), en nooit daarboven: meer geld in dezelfde markten geeft geen evenredig grotere beloning (je deelt de pot). Kansspelbelasting (37,8%, mogelijk) en het verbod in Nederland staan hier niet in; zie README.

Tegen de uitslag (de bot houdt zijn voorraad tot de uitslag): $-1,211 over 17203 vullingen en $55,360, dus -2.19% per gevulde dollar (GEZIEN).

- Hoogste temperatuur: 5 minuten later -2.04% per dollar over 23605 vullingen, 1 uur later -2.78% over 23158 (GEZIEN).
- Laagste temperatuur: 5 minuten later -3.96% per dollar over 906 vullingen, 1 uur later -4.79% over 891 (GEZIEN).

## Variant 3c (orders op 3 cent van het midden)

| Dag (UTC) | Minuten gemeten | Markten gem. | Orders op het boek gem. | Hoogste stand voorraadgeld | Beloning ondergrens tot hoge schatting (GOK) | Vullingen los / streng | Gevuld | Resultaat vullingen 1 uur later | Tegen uitslag | Netto (ondergrens tot hoge schatting, alleen vullingen met prijs 1 uur later) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-19 | 895 | 245 | $4,576 | $1,364 | $51.06 tot $127 | 490 / 352 | $1,800 | $-52.50 (6 nog zonder prijs) | $-84.53 (490 van 490 beslist) | $-1.45 tot $74.53 |
| 2026-11-20 | 1420 | 254 | $4,737 | $3,186 | $98.64 tot $260 | 751 / 478 | $2,718 | $-74.90 (31 nog zonder prijs) | $145 (751 van 751 beslist) | $23.74 tot $185 |
| 2026-11-21 | 1410 | 216 | $4,034 | $4,020 | $86.17 tot $230 | 966 / 606 | $3,482 | $-94.48 (14 nog zonder prijs) | $-66.21 (966 van 966 beslist) | $-8.31 tot $135 |
| 2026-11-22 | 1432 | 191 | $3,551 | $3,943 | $88.97 tot $234 | 867 / 549 | $3,240 | $-71.94 (11 nog zonder prijs) | $-215 (703 van 867 beslist) | $17.03 tot $162 |
| 2026-11-23 | 1432 | 168 | $3,136 | $3,949 | $83.83 tot $220 | 1159 / 776 | $4,375 | $-98.61 (6 nog zonder prijs) | $-70.04 (445 van 1159 beslist) | $-14.78 tot $122 |
| 2026-11-24 | 1135 | 161 | $2,982 | $3,593 | $59.60 tot $159 | 784 / 476 | $3,281 | $-40.89 (37 nog zonder prijs) | $0.00 (0 van 784 beslist) | $18.71 tot $118 |
| **Totaal** | 7724 | | $3,815 | $4,020 | $468 tot $1,230 | 5017 / 3237 | $18,895 | $-433 | $-291 | $34.95 tot $797 |

Resultaat vullingen 5 minuten later (vroege aanwijzing, GEZIEN): $-446 over 5003 vullingen en $18,839, dus -2.37% per gevulde dollar.

Verlies per gevulde dollar, 1 uur later: -2.33% over $18,611 (GEZIEN; B mat −1,05% voor alle makers binnen 1 cent, D −0,1 tot −0,3% voor alle makers in temperatuurmarkten). Alleen strenge vullingen: -3.47%.

**Opgeschaald (GOK):** per dag $5.28 (ondergrens) tot $147 (hoge schatting) netto (gemeten minuten × 1440 / 7724).

105 van de 5017 vullingen ($284) hebben nog geen prijs 1 uur later. Die tellen niet als 0: hun verlies is geschat met het verlies per dollar van de andere vullingen (1 uur later, -2.33%): $-6.62 (GOK).

Geld dat de bot nodig had: gemiddeld $3,815 in open orders plus de hoogste stand van $4,020 vastzittend in gevulde voorraad tot de uitslag (JA en NEE per markt tegen elkaar weggestreept; vrij ±30 uur na het begin van de dag, GOK) = **$7,835**. De voorraad groeit tot de eerste markten beslist zijn (2 tot 3 dagen na de start), dus tot dan is dit getal te laag.

| Inleg | Te gebruiken (× 1.0 $/€, hooguit orders plus voorraad) | Netto over 90 dagen (GOK) |
|---|---|---|
| €2,000 | $2,000 | $121 tot $3,384 |
| €5,000 | $5,000 | $303 tot $8,461 |

Opschalen gaat lineair met het geld dat de bot nodig had (orders plus voorraad), en nooit daarboven: meer geld in dezelfde markten geeft geen evenredig grotere beloning (je deelt de pot). Kansspelbelasting (37,8%, mogelijk) en het verbod in Nederland staan hier niet in; zie README.

Tegen de uitslag (de bot houdt zijn voorraad tot de uitslag): $-291 over 3355 vullingen en $12,410, dus -2.35% per gevulde dollar (GEZIEN).

- Hoogste temperatuur: 5 minuten later -2.34% per dollar over 4768 vullingen, 1 uur later -2.33% over 4669 (GEZIEN).
- Laagste temperatuur: 5 minuten later -2.86% per dollar over 235 vullingen, 1 uur later -2.02% over 233 (GEZIEN).

## Met weinig geld: €100, €150 en €200 (variant 1c, GOK)

Een kleine inleg staat maar in een paar markten tegelijk. Per markt is nodig: de orders zelf (minimale grootte van die markt, vaak 20 aandelen, soms 100, afgerond op de tick van de markt, zoals gemeten) plus ruimte voor voorraad tot de rem (2 keer de ordergrootte aan de duurste kant). Markten die meer vragen dan de hele inleg vallen af. Gerekend over 1485 markten met minstens 60 gemeten minuten.

| Inleg | Gemiddelde markten: aantal | Beloning per dag | Netto per dag | Achteraf beste markten: aantal | Beloning per dag | Netto per dag |
|---|---|---|---|---|---|---|
| €100 | 1 | $1.58 tot $3.21 | $-0.66 tot $0.97 | 2 | $23.89 tot $43.73 | $-16.25 tot $3.60 |
| €150 | 2 | $3.16 tot $6.42 | $-1.32 tot $1.94 | 3 | $32.73 tot $59.86 | $-26.96 tot $0.17 |
| €200 | 3 | $4.73 tot $9.63 | $-1.98 tot $2.91 | 4 | $42.19 tot $76.70 | $-17.50 tot $17.01 |

Lees zo: per dag = gemeten opbrengst per markt-minuut × 1440 × aantal markten (GOK). "Achteraf beste" kiest de markten die in deze data het meest opleverden per dollar; dat is te mooi, want vooraf weet je niet welke dat zijn. Netto = beloning min het verlies op vullingen 1 uur later; vullingen zonder prijs 1 uur later zijn geschat met het verlies per dollar van de rest (-2.86%). Polymarket betaalt pas uit vanaf $1 beloning per dag (docs Liquidity Rewards); daaronder krijg je niets, maar het verlies op vullingen blijft. Geen belasting of verbod in Nederland meegerekend.

## Per markt (variant 1c)

Slechtste 10 en beste 10 op netto (beloning ondergrens plus resultaat 1 uur later).

| Markt | Minuten | Beloning ondergrens tot hoge schatting (GOK) | Vullingen | 1 uur later | Tegen uitslag |
|---|---|---|---|---|---|
| highest wellington-on-november-23 19°C | 1574 | $4.66 tot $9.54 | 70 | $-35.02 | $-59.48 |
| highest dallas-on-november-22 68-69°F | 2374 | $3.83 tot $7.62 | 52 | $-31.50 | $-104 |
| highest dallas-on-november-22 64-65°F | 2463 | $2.93 tot $6.04 | 36 | $-24.15 | $-54.33 |
| highest paris-on-november-23 7°C | 2345 | $4.20 tot $9.02 | 69 | $-21.89 | $-93.47 |
| highest taipei-on-november-24 21°C | 951 | $1.50 tot $3.00 | 33 | $-17.79 | $24.65 |
| highest hong-kong-on-november-24 22°C | 1464 | $4.44 tot $8.79 | 89 | $-20.19 | $0.00 |
| highest toronto-on-november-23 12°C | 1200 | $2.93 tot $5.19 | 44 | $-18.45 | $21.60 |
| highest tel-aviv-on-november-25 24°C | 1520 | $5.55 tot $11.50 | 30 | $-20.61 | $0.00 |
| highest wellington-on-november-23 18°C | 1574 | $4.34 tot $9.03 | 56 | $-18.80 | $28.93 |
| highest san-francisco-on-november-22 54-55°F | 2416 | $3.52 tot $6.93 | 50 | $-17.70 | $-14.69 |
| ... | | | | | |
| highest ankara-on-november-24 11°C | 1121 | $1.60 tot $3.18 | 36 | $7.26 | $0.00 |
| highest chicago-on-november-22 56-57°F | 2262 | $3.74 tot $6.27 | 57 | $6.34 | $11.46 |
| highest hong-kong-on-november-20 18°C | 291 | $0.22 tot $0.54 | 39 | $9.97 | $-5.92 |
| highest london-on-november-22 9°C | 2445 | $3.23 tot $7.12 | 45 | $7.23 | $18.39 |
| highest milan-on-november-21 16°C | 2085 | $6.23 tot $9.85 | 31 | $4.59 | $15.46 |
| highest shanghai-on-november-24 13°C | 1688 | $4.18 tot $8.74 | 69 | $7.87 | $3.57 |
| highest helsinki-on-november-20 5°C | 740 | $1.97 tot $3.93 | 35 | $10.10 | $-2.39 |
| highest seoul-on-november-24 6°C | 1617 | $3.16 tot $6.36 | 96 | $10.08 | $6.78 |
| highest nyc-on-november-25 48-49°F | 2141 | $6.83 tot $11.74 | 38 | $14.28 | $0.00 |
| highest warsaw-on-november-25 5°C | 3302 | $3.63 tot $7.30 | 29 | $87.78 | $0.00 |

## Per stad (variant 1c)

| Stad | Beloning ondergrens tot hoge schatting (GOK) | Vullingen | 1 uur later | Netto ondergrens |
|---|---|---|---|---|
| warsaw (highest) | $42.39 tot $88.91 | 404 | $61.85 | $104 |
| seoul (highest) | $39.31 tot $83.02 | 736 | $-3.67 | $35.64 |
| miami (lowest) | $45.63 tot $79.44 | 109 | $-16.34 | $29.29 |
| london (lowest) | $33.23 tot $60.45 | 193 | $-8.55 | $24.67 |
| chengdu (highest) | $38.63 tot $84.33 | 396 | $-14.85 | $23.79 |
| beijing (highest) | $33.06 tot $70.23 | 427 | $-12.05 | $21.01 |
| nyc (highest) | $57.04 tot $117 | 945 | $-36.66 | $20.38 |
| paris (lowest) | $39.18 tot $72.37 | 125 | $-22.56 | $16.62 |
| wuhan (highest) | $37.94 tot $80.24 | 328 | $-23.13 | $14.80 |
| manila (highest) | $23.14 tot $46.50 | 186 | $-9.63 | $13.51 |
| kuala-lumpur (highest) | $27.55 tot $52.78 | 265 | $-15.93 | $11.62 |
| austin (highest) | $51.13 tot $106 | 541 | $-40.92 | $10.21 |
| karachi (highest) | $27.69 tot $54.67 | 226 | $-17.74 | $9.95 |
| mexico-city (highest) | $32.78 tot $63.61 | 203 | $-22.87 | $9.91 |
| milan (highest) | $40.45 tot $82.44 | 553 | $-32.38 | $8.07 |
| chongqing (highest) | $40.62 tot $84.43 | 334 | $-32.59 | $8.03 |
| munich (highest) | $42.55 tot $89.37 | 629 | $-36.11 | $6.44 |
| jeddah (highest) | $21.27 tot $42.83 | 155 | $-15.64 | $5.63 |
| shanghai (lowest) | $11.87 tot $21.75 | 41 | $-7.06 | $4.81 |
| shenzhen (highest) | $28.75 tot $60.03 | 500 | $-24.47 | $4.29 |
| singapore (highest) | $39.37 tot $84.17 | 521 | $-35.46 | $3.91 |
| nyc (lowest) | $13.77 tot $23.27 | 88 | $-13.22 | $0.56 |
| sao-paulo (highest) | $31.73 tot $62.97 | 360 | $-31.71 | $0.01 |
| houston (highest) | $57.66 tot $119 | 829 | $-57.92 | $-0.27 |
| seoul (lowest) | $23.39 tot $43.99 | 134 | $-24.63 | $-1.24 |
| tokyo (highest) | $34.31 tot $75.35 | 600 | $-36.65 | $-2.33 |
| london (highest) | $46.69 tot $102 | 914 | $-49.67 | $-2.98 |
| los-angeles (highest) | $37.03 tot $81.80 | 687 | $-40.60 | $-3.57 |
| buenos-aires (highest) | $27.77 tot $53.81 | 369 | $-33.63 | $-5.86 |
| moscow (highest) | $27.36 tot $54.87 | 326 | $-34.57 | $-7.21 |
| tokyo (lowest) | $13.47 tot $22.88 | 66 | $-21.97 | $-8.50 |
| ankara (highest) | $30.74 tot $59.80 | 468 | $-39.39 | $-8.66 |
| qingdao (highest) | $24.17 tot $48.01 | 271 | $-34.90 | $-10.74 |
| taipei (highest) | $30.34 tot $56.25 | 338 | $-43.22 | $-12.87 |
| shanghai (highest) | $39.74 tot $85.82 | 743 | $-54.64 | $-14.90 |
| madrid (highest) | $39.79 tot $87.31 | 577 | $-54.87 | $-15.08 |
| chicago (highest) | $47.04 tot $87.95 | 684 | $-62.15 | $-15.11 |
| lucknow (highest) | $45.11 tot $93.18 | 438 | $-60.93 | $-15.82 |
| miami (highest) | $47.89 tot $101 | 672 | $-68.63 | $-20.74 |
| guangzhou (highest) | $45.39 tot $92.45 | 615 | $-66.28 | $-20.89 |
| hong-kong (lowest) | $8.62 tot $15.32 | 151 | $-32.56 | $-23.94 |
| san-francisco (highest) | $35.12 tot $68.46 | 468 | $-61.63 | $-26.52 |
| amsterdam (highest) | $37.81 tot $82.49 | 682 | $-65.26 | $-27.45 |
| tel-aviv (highest) | $50.44 tot $108 | 411 | $-78.78 | $-28.33 |
| atlanta (highest) | $51.31 tot $109 | 959 | $-91.78 | $-40.47 |
| toronto (highest) | $26.80 tot $53.02 | 474 | $-71.82 | $-45.02 |
| busan (highest) | $39.04 tot $82.83 | 538 | $-85.58 | $-46.54 |
| hong-kong (highest) | $34.84 tot $73.38 | 905 | $-94.04 | $-59.20 |
| dallas (highest) | $48.84 tot $103 | 644 | $-109 | $-60.60 |
| helsinki (highest) | $56.50 tot $115 | 779 | $-123 | $-66.94 |
| wellington (highest) | $35.60 tot $77.91 | 553 | $-103 | $-67.28 |
| paris (highest) | $53.78 tot $116 | 1000 | $-122 | $-67.73 |

Grenzen: de beloning is een schatting (het echte aangepaste midden en de scores per maker zijn niet openbaar); een vulling telt 'los' als een trade op of door onze prijs gaat en 'streng' als hij erdoorheen gaat (de wachtrij is onbekend); trades staan 1 tot 2 minuten later in de Data API, dus de voorraadrem reageert iets te laat. Dit is meten, geen advies.
